#!/usr/bin/env python3
"""Private local custody for whole capture folders (Majkee, walkthrough 2, S2, 2026-11-22).

Copies every regular file of the source folders into a NEW private folder, keeps
relative paths and modification times, hashes each file before and after, and
writes MANIFEST.json last. Sources stay in place. No file content is printed.

    python3 capture-folders-custody.py DEST
    python3 capture-folders-custody.py DEST --source DIR [--source DIR ...]

Default sources are the two trial capture folders in /tmp on home. DEST must not
exist and must be outside any Git worktree. Folders are created 0700, files 0600.
Any symlink or special file in a source stops the run before anything is written.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import socket
import sys

DEFAULT_SOURCES = ("/tmp/vc08r1.tkz50zbf", "/tmp/vc08r2.kk50sqqh")
AUTHORITY = "relay-X0-carryover/raw/decision.majkee.walkthrough-2.2026-11-22.md, S2"
LIMIT = ("Bytes as found at copy time. No claim that the folders are complete or unchanged since the "
         "trial; only the eight C04 inputs are pinned by the X0 packet.")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(source):
    """All regular files below source, sorted. Refuse anything that is not a plain file or folder."""
    files = []
    for root, dirs, names in os.walk(source, followlinks=False):
        for name in dirs + names:
            p = Path(root) / name
            if p.is_symlink() or not (p.is_file() or p.is_dir()):
                raise ValueError(f"Unexpected file type, nothing copied: {p}")
        files.extend(Path(root) / name for name in names)
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--source", action="append", type=Path,
                        help="source folder; repeat for more than one (default: the two /tmp capture folders)")
    args = parser.parse_args()
    os.umask(0o077)

    sources = [s.resolve() for s in (args.source or [Path(s) for s in DEFAULT_SOURCES])]
    if len({s.name for s in sources}) != len(sources):
        raise ValueError("Source folders must have different names")
    for s in sources:
        if s.is_symlink() or not s.is_dir():
            raise ValueError(f"Source is not a folder: {s}")

    destination = args.destination.expanduser().resolve()
    if any((parent / ".git").exists() for parent in (destination, *destination.parents)):
        raise ValueError("Private evidence destination must be outside a Git worktree")

    # Read the whole source set before anything is created.
    plan = []
    for s in sources:
        for f in inventory(s):
            st = f.stat()
            plan.append((s, f, st.st_size, sha256(f), st.st_mtime_ns))

    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    destination.mkdir(mode=0o700)  # an existing folder is refused; from here on, failure removes only what this run made
    try:
        records = []
        for s, f, size, digest, mtime_ns in plan:
            relative = Path(s.name) / f.relative_to(s)
            target = destination / relative
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            data = f.read_bytes()
            if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
                raise ValueError(f"Source changed during the run: {f}")
            with target.open("xb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            os.utime(target, ns=(mtime_ns, mtime_ns))
            after = sha256(target)
            if target.stat().st_size != size or after != digest:
                raise ValueError(f"Copy differs from source: {target}")
            records.append({
                "source": str(f), "copy": str(relative), "bytes": size,
                "sha256_before": digest, "sha256_after": after,
                "mtime_utc": datetime.fromtimestamp(mtime_ns / 1e9, timezone.utc).isoformat(),
            })
        manifest = {
            "purpose": "Private custody of whole trial capture folders",
            "host": socket.gethostname(),
            "copied_utc": datetime.now(timezone.utc).isoformat(),
            "authority": AUTHORITY,
            "limit": LIMIT,
            "sources": [str(s) for s in sources],
            "file_count": len(records),
            "total_bytes": sum(r["bytes"] for r in records),
            "files": records,
        }
        with (destination / "MANIFEST.json").open("x") as stream:
            json.dump(manifest, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        shutil.rmtree(destination)
        raise
    print(f"copied: {len(records)} files, {sum(r['bytes'] for r in records)} bytes verified at {destination}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        sys.exit(str(error))
