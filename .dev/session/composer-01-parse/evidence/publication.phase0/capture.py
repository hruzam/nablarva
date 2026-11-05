#!/usr/bin/env python3
"""One-shot exact-scope capture/temporary validation; never mutates a git repository."""
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess
import tarfile
import tempfile

from recheck import BED, ENV, PACKAGE, ROOTS, SCOPES, allowed, changed, git, index_diff, inventory


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(name, data):
    (PACKAGE / name).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def main():
    assert not (PACKAGE / "snapshot.json").exists(), "one-shot: preserve the existing capture"
    timestamp = datetime.now(timezone.utc).isoformat()
    snapshot = {"snapshot_at_utc": timestamp, "status_stamp": "d98371cf",
                "state_notice": "Captured state only; future STATUS/review/proposal bytes are not captured.",
                "repositories": {}}
    manifest, payload, commands = [], {}, []
    for repo, root in ROOTS.items():
        head = git(repo, "rev-parse", "HEAD").decode().strip()
        tracked = set(name.decode() for name in git(repo, "ls-tree", "-r", "--name-only", "-z", "HEAD", "--", *SCOPES[repo]).split(b"\0") if name)
        files, dirty = inventory(repo), changed(repo)
        assert set(dirty).issubset(files), (repo, "deleted or unsupported changed path")
        staged = index_diff(repo)
        assert not staged, (repo, "scoped staging already present")
        ignored = git(repo, "ls-files", "--others", "--ignored", "--exclude-standard", "-z", "--", *SCOPES[repo])
        assert not [p for p in ignored.split(b"\0") if p and allowed(repo, p.decode())], (repo, "ignored payload")
        modified = sorted(set(dirty) & tracked)
        expected_modified = ([BED + "/RUNBOOK.md", BED + "/STATUS.md", ".dev/session/flag.md",
                              "PROJECT-DESIGN.md", "toolbox/termbrana/README.md"]
                             if repo == "nablarva" else ["journal.host-cleanup.md"])
        assert modified == sorted(expected_modified), (repo, "unexpected tracked diff scope", modified)
        patch_command = ["git", "diff", "--binary", "--full-index", "--no-ext-diff", "--no-renames", "HEAD", "--", *modified]
        patch = git(repo, *patch_command[1:]) if modified else b""
        (PACKAGE / (repo + ".tracked.patch")).write_bytes(patch)
        (PACKAGE / (repo + ".changed.paths.txt")).write_text("".join(p + "\n" for p in dirty))
        (PACKAGE / (repo + ".changed.paths.nul")).write_bytes(b"".join(p.encode() + b"\0" for p in dirty))
        (PACKAGE / (repo + ".tracked-modified.paths.txt")).write_text("".join(p + "\n" for p in modified))
        all_status = git(repo, "status", "--porcelain=v1", "-uall", "-z")
        (PACKAGE / (repo + ".status.captured.nul")).write_bytes(all_status)
        excluded = []
        for record in all_status.split(b"\0"):
            if not record:
                continue
            assert record[0:1] not in (b"R", b"C") and record[1:2] not in (b"R", b"C"), "inspect rename/copy status explicitly"
            name = record[3:].decode()
            if not allowed(repo, name):
                excluded.append({"status": record[:2].decode(), "path": name})
        write_json(repo + ".excluded-changes.json", excluded)
        snapshot["repositories"][repo] = dict(root=str(root), head=head, changed_paths=dirty,
            tracked_modified_paths=modified, index_diff_sha256=sha(staged),
            git_index_sha256=sha((root / ".git/index").read_bytes()),
            tracked_patch_sha256=sha(patch), excluded_status_records=len(excluded))
        commands.append(dict(command=patch_command, cwd=str(root), exit=0,
                             purpose="capture only scoped tracked changes"))
        for relative in files:
            path = root / relative
            data = path.read_bytes()
            disposition = "new" if relative not in tracked else "modified" if relative in dirty else "unchanged_reference"
            member = repo + "/" + relative
            parts = PurePosixPath(member).parts
            assert not member.startswith("/") and ".." not in parts and "\n" not in member
            entry = dict(repo=repo, path=relative, sha256=sha(data), size=len(data),
                         disposition=disposition, mode=stat.S_IMODE(path.stat().st_mode))
            manifest.append(entry)
            payload[member] = data
    manifest.sort(key=lambda entry: (entry["repo"], entry["path"]))
    write_json("snapshot.json", snapshot)
    write_json("manifest.json", manifest)
    (PACKAGE / "payload.sha256").write_text("".join(entry["sha256"] + "  " + entry["repo"] + "/" + entry["path"] + "\n" for entry in manifest))
    with (PACKAGE / "payload.tar.gz").open("wb") as output:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.USTAR_FORMAT) as archive:
                for entry in manifest:
                    name = entry["repo"] + "/" + entry["path"]
                    info = tarfile.TarInfo(name)
                    info.size, info.mode, info.mtime = entry["size"], entry["mode"], 0
                    archive.addfile(info, io.BytesIO(payload[name]))
    checks = {"status": "PASS", "snapshot_at_utc": timestamp, "commands": commands,
              "manifest_files": len(manifest), "payload_bytes": sum(e["size"] for e in manifest),
              "dispositions": dict(Counter(e["disposition"] for e in manifest)),
              "per_repo": {repo: dict(Counter(e["disposition"] for e in manifest if e["repo"] == repo)) for repo in ROOTS}}
    with tempfile.TemporaryDirectory(prefix="composer-publication-check-") as temporary:
        extracted = Path(temporary) / "snapshot"
        extracted.mkdir()
        with tarfile.open(PACKAGE / "payload.tar.gz", "r:gz") as archive:
            members = archive.getmembers()
            assert [member.name for member in members] == [e["repo"] + "/" + e["path"] for e in manifest]
            assert len(set(member.name for member in members)) == len(manifest)
            for member in members:
                assert member.isfile() and not member.name.startswith("/") and ".." not in PurePosixPath(member.name).parts
                target = extracted / member.name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.extractfile(member).read())
        for entry in manifest:
            data = (extracted / entry["repo"] / entry["path"]).read_bytes()
            assert len(data) == entry["size"] and sha(data) == entry["sha256"]
        command = ["sha256sum", "-c", str(PACKAGE / "payload.sha256")]
        result = subprocess.run(command, cwd=extracted, env=ENV, capture_output=True)
        assert result.returncode == 0
        checks["commands"].append(dict(command=command, cwd="<temporary extracted snapshot>", exit=0, ok_lines=len(result.stdout.splitlines())))
        raw = extracted / "nablarva" / BED / "raw"
        assert len([p for p in raw.rglob("*") if p.is_file()]) == 19
        for pin in ["SHA256SUMS", "evidence/grammar.builder.v4.sha256", "evidence/grammar.builder.v3.sha256"]:
            command = ["sha256sum", "-c", pin]
            result = subprocess.run(command, cwd=raw.parent, env=ENV, capture_output=True)
            assert result.returncode == 0, result.stderr
            checks["commands"].append(dict(command=command, cwd="<temporary extracted Nablarva bed>", exit=0, stdout=result.stdout.decode()))
        receipt = json.loads((raw.parent / "evidence/source-copy.startup.phase0.json").read_text())["final_sha256"]
        source = extracted / "ia-sync/zsh/termbrana"
        observed = {p.relative_to(source).as_posix(): sha(p.read_bytes()) for p in source.rglob("*") if p.is_file()}
        assert observed == receipt and len(observed) == 10
        brief = extracted / "ia-sync/.dev/session/germline-07-make-program/raw/brief.germline-contract-testing.md"
        assert brief.read_bytes() == (raw.parent / "evidence/brief.germline-contract-testing.md").read_bytes()
        preserved = ["implementation.phase0/benchmark.first.json", "correction.phase0/benchmark.json", "startup.phase0/benchmark.json", "verification.phase0/declared/benchmark.json"]
        statuses = [json.loads((raw.parent / "evidence" / name).read_text())["status"] for name in preserved]
        assert statuses == ["FAIL", "FAIL", "PASS", "PASS"]
        checks["preserved_benchmark_statuses"] = dict(zip(preserved, statuses))
        for repo in ROOTS:
            baseline = Path(temporary) / (repo + "-base")
            baseline.mkdir()
            for relative in snapshot["repositories"][repo]["tracked_modified_paths"]:
                path = baseline / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(git(repo, "show", snapshot["repositories"][repo]["head"] + ":" + relative))
            patch = PACKAGE / (repo + ".tracked.patch")
            command = ["git", "apply", "--check", "--whitespace=nowarn", str(patch)]
            result = subprocess.run(command, cwd=baseline, env=ENV, capture_output=True)
            assert result.returncode == 0, result.stderr
            checks["commands"].append(dict(command=command, cwd="<temporary " + repo + " HEAD files>", exit=0))
    for repo, root in ROOTS.items():
        assert sha((root / ".git/index").read_bytes()) == snapshot["repositories"][repo]["git_index_sha256"], (repo, "index changed during capture")
    command = ["python3", "-B", str(PACKAGE / "recheck.py")]
    result = subprocess.run(command, env=ENV, capture_output=True)
    assert result.returncode == 0, result.stderr
    checks["commands"].append(dict(command=command, exit=0, stdout=result.stdout.decode()))
    checks.update(archive_sha256=sha((PACKAGE / "payload.tar.gz").read_bytes()),
                  archive_bytes=(PACKAGE / "payload.tar.gz").stat().st_size,
                  archive_members_safe_regular=True, extracted_hashes_match=True,
                  source_receipt_match=True, raw_count=19, raw_and_grammar_pins="PASS",
                  requested_brief_copy_identical=True, git_heads_indices_payload_unchanged=True,
                  shared_diff_review="RUNBOOK/STATUS, L17, product composition sections and composer journal entry only; no foreign hunks observed",
                  publication_performed=False, tests_rerun=False)
    write_json("checks.json", checks)
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
