#!/usr/bin/env python3
"""Private local custody for the eight pinned C04 inputs (Majkee, T2, 2026-11-21).

import DEST copies original /tmp inputs. export CUSTODY DEST restores the same
relative paths in a new private folder. Sources remain in place. Both operations
check frozen sizes/hashes before and after copying and write MANIFEST.json last.
No capture content is printed. Use python3 c04-custody.py --help for arguments.
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

PIN_SOURCE = "nablarva@2ef2ae37fb1f2ffc98c67c08f23a888068f399ff:.dev/session/vist-X0-helloWorld/raw/preparation.sources.2026-11-14.json"
ARCHIVE_MAP = "~/ia-sync/.dev/records/vist/2026-11-14/MANIFEST.json"
# Relative to /tmp for import, or the custody root for export.
PINS = (
    ("vc08r1.tkz50zbf/results.jsonl", 15255, "e2778f5aeb1cd837e7485573940fcfe2c33b940583e9988ccee41a00406c05cf"),
    ("vc08r1.tkz50zbf/codex-receipts.json", 1382, "43b6971dac2547c2bf91d97782ad7595b8f889270d3825fd5b644bee5baef799"),
    ("vc08r1.tkz50zbf/04-busy-before-queued.meta", 162, "57c466f793c75774369f4ac2aeb6625043eee4f411e40d94f2e2e77faeb890d8"),
    ("vc08r1.tkz50zbf/04-after.meta", 156, "34890c12d5e7e30c1c00ae285fbf301e931cd129bde187a02aafd69924e75fb3"),
    ("vc08r2.kk50sqqh/results.jsonl", 16603, "3dbbb0d66b1c51b58806de9314796227171ba06a48ebc977bd3959374224fccc"),
    ("vc08r2.kk50sqqh/codex-receipts.json", 1215, "de083ee61e4244863d32f034f9fdca4aa90f8156a5a912c6a6b3a6840c909587"),
    ("vc08r2.kk50sqqh/04-busy-before.meta", 162, "019a3fb5ebaf35ae6e05b4ec0a37def4d0ce8a047c764b91299cd395eada2845"),
    ("vc08r2.kk50sqqh/04-after.meta", 155, "5f5ffdd8dc2898988b011f5cb63a7d99920fe2c3faf22ef17d1a61336d5cddb2"),
)


def checked(path, size, expected_hash):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular file: {path}")
    data = path.read_bytes()
    if len(data) != size or hashlib.sha256(data).hexdigest() != expected_hash:
        raise ValueError(f"Frozen size/hash mismatch: {path}")
    return data


def transfer(operation, source, destination):
    destination = destination.expanduser().resolve()
    if any((parent / ".git").exists() for parent in (destination, *destination.parents)):
        raise ValueError("Private evidence destination must be outside a Git worktree")
    # Check the whole source set before creating the destination.
    payloads = [checked(source / name, size, digest) for name, size, digest in PINS]
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    destination.mkdir(mode=0o700)  # Exclusive ownership; an existing folder is refused.
    try:
        files = []
        for (name, size, digest), data in zip(PINS, payloads):
            target = destination / name
            target.parent.mkdir(mode=0o700, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            checked(target, size, digest)
            files.append({"original": str(Path("/tmp") / name), "source": str(source / name),
                          "copy": name, "bytes_before": size, "bytes_after": size,
                          "sha256_before": digest, "sha256_after": digest})
        manifest = {"purpose": "Private C04 evidence custody", "operation": operation,
                    "host": socket.gethostname(), "copied_utc": datetime.now(timezone.utc).isoformat(),
                    "pin_source": PIN_SOURCE, "archive_map": ARCHIVE_MAP,
                    "authority": "relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md, T2",
                    "limit": "Pinned bytes only; content correctness and capture completeness remain unqualified.",
                    "files": files}
        with (destination / "MANIFEST.json").open("x") as stream:
            json.dump(manifest, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        shutil.rmtree(destination)
        raise
    print(f"{operation}: {len(PINS)} files, {sum(size for _, size, _ in PINS)} bytes verified at {destination}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="operation", required=True)
    importer = commands.add_parser("import", help="Copy the eight original /tmp inputs into a new private folder")
    importer.add_argument("destination", type=Path)
    exporter = commands.add_parser("export", help="Copy pinned files from custody into a new private restore folder")
    exporter.add_argument("custody", type=Path)
    exporter.add_argument("destination", type=Path)
    args = parser.parse_args()
    os.umask(0o077)
    source = Path("/tmp") if args.operation == "import" else args.custody.expanduser().resolve()
    transfer(args.operation, source, args.destination)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        sys.exit(str(error))
