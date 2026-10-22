#!/usr/bin/env python3
"""Read-only publication snapshot recheck. Does not stage, commit or apply files."""
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess

PACKAGE = Path(__file__).resolve().parent
ROOTS = {"nablarva": Path("/home/hruzam/unikuklatrix/nablarva"),
         "ia-sync": Path("/home/hruzam/ia-sync")}
BED = ".dev/session/composer-01-parse"
EXCLUDES = (BED + "/evidence/publication.phase0", BED + "/evidence/preservation.phase0.cleanup")
ORIGINAL_ZIP = BED + "/evidence/import/files.zip"
ORIGINAL_ZIP_SHA256 = "7d7251b6ed19ba07747dd3cee72388a22b1813c13a9b62a0d44fd63b1ae70aa1"
SCOPES = {"nablarva": [BED, ".dev/session/flag.md", "PROJECT-DESIGN.md",
                       "toolbox/termbrana/README.md",
                       ".dev/session/termbrana-X1-composer-sourcing/raw/handoff.cartan.runbook-preparation.2026-10-21.md"],
          "ia-sync": ["zsh/termbrana", "journal.host-cleanup.md",
                      ".dev/session/germline-07-make-program/raw/brief.germline-contract-testing.md"]}
ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0", PYTHONDONTWRITEBYTECODE="1")


def git(repo, *arguments):
    return subprocess.run(["git", *arguments], cwd=ROOTS[repo], env=ENV,
                          capture_output=True, check=True).stdout


def pathspecs(repo):
    result = [*SCOPES[repo], ":(exclude,glob)**/.hlm/**", ":(exclude,glob)**/.hlm"]
    if repo == "nablarva":
        result.extend(":(exclude)" + item for item in EXCLUDES)
    return result


def index_path(repo):
    path = Path(git(repo, "rev-parse", "--git-path", "index").decode().strip())
    return (path if path.is_absolute() else ROOTS[repo] / path).resolve()


def allowed(repo, relative):
    if ".hlm" in Path(relative).parts:
        return False
    if repo == "nablarva" and any(relative == item or relative.startswith(item + "/") for item in EXCLUDES):
        return False
    return any(relative == scope or relative.startswith(scope + "/")
               for scope in SCOPES[repo])


def inventory(repo):
    paths = []
    root = ROOTS[repo]

    def walk(path):
        relative = path.relative_to(root).as_posix()
        if not allowed(repo, relative):
            return
        mode = path.lstat().st_mode
        if stat.S_ISDIR(mode):
            assert path.name not in ("__pycache__", ".git"), relative
            for child in sorted(path.iterdir()):
                walk(child)
        else:
            assert stat.S_ISREG(mode), ("not a regular file", repo, relative)
            assert path.suffix not in (".pyc", ".pyo"), relative
            if relative.endswith((".tar", ".tar.gz", ".tgz", ".zip")):
                assert repo == "nablarva" and relative == ORIGINAL_ZIP, ("unexpected archive", relative)
                original = path.read_bytes()
                assert len(original) == 11408 and hashlib.sha256(original).hexdigest() == ORIGINAL_ZIP_SHA256, ("original ZIP identity drift", relative)
            assert path.name not in (".env", "credentials", "auth.json", ".DS_Store"), relative
            paths.append(relative)

    for scope in SCOPES[repo]:
        # Check the route to each scope as well as the descendants.
        path = root
        for part in Path(scope).parts:
            path = path / part
            assert not path.is_symlink(), ("symlink in scope route", str(path))
        walk(root / scope)
    return sorted(paths)


def changed(repo):
    tracked = git(repo, "diff", "--name-only", "-z", "HEAD", "--", *pathspecs(repo))
    new = git(repo, "ls-files", "--others", "--exclude-standard", "-z", "--", *pathspecs(repo))
    names = {name.decode() for name in (tracked + new).split(b"\0") if name}
    return sorted(name for name in names if allowed(repo, name))


def index_diff(repo):
    return git(repo, "diff", "--cached", "--binary", "--full-index", "--no-ext-diff",
               "HEAD", "--", *pathspecs(repo))


def main():
    metadata = json.loads((PACKAGE / "snapshot.json").read_text())
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    for repo in ROOTS:
        assert git(repo, "rev-parse", "HEAD").decode().strip() == metadata["repositories"][repo]["head"], (repo, "HEAD drift")
        assert str(index_path(repo)) == metadata["repositories"][repo]["git_index_path"], (repo, "index-path drift")
        wanted = [entry for entry in manifest if entry["repo"] == repo]
        expected_paths = sorted(entry["path"] for entry in wanted)
        assert inventory(repo) == expected_paths, (repo, "extra or missing payload paths")
        assert changed(repo) == metadata["repositories"][repo]["changed_paths"], (repo, "changed-path set drift")
        assert hashlib.sha256(index_diff(repo)).hexdigest() == metadata["repositories"][repo]["index_diff_sha256"], (repo, "scoped index drift")
        for entry in wanted:
            path = ROOTS[repo] / entry["path"]
            data = path.read_bytes()
            assert len(data) == entry["size"] and hashlib.sha256(data).hexdigest() == entry["sha256"], (repo, entry["path"], "byte drift")
            assert stat.S_IMODE(path.stat().st_mode) == entry["mode"], (repo, entry["path"], "mode drift")
    print(json.dumps({"status": "PASS", "payload_files": len(manifest),
                      "snapshot_at_utc": metadata["snapshot_at_utc"],
                      "meaning": "matches captured bytes and path sets; no staging authorized"}))


if __name__ == "__main__":
    main()
