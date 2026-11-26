# Side quest s02 — office custody copy

**Done.** Office (`hruzam-120922`) now has the complete chooser custody folder.

| Host | Files before | Bytes before | Files after | Bytes after |
|---|---:|---:|---:|---:|
| Home (`hruzam`) | 169 | 5,538,087 | 169 | 5,538,087 |
| Office (`hruzam-120922`) | 160 | 4,181,188 | 169 | 5,538,087 |

```sh
rsync -a --no-owner --no-group --ignore-existing --itemize-changes \
  -e 'ssh -o BatchMode=yes -o ConnectTimeout=8' \
  /home/hruzam/.local/share/nablarva/custody/x1-chooser-2026-11-23/ \
  office:/home/hruzam/.local/share/nablarva/custody/x1-chooser-2026-11-23/
```

Rsync exited 0. It added nine files (1,356,899 bytes) under
`tracker-sample2-2026-11-26.rsztjnz1/` and synchronized the custody root's
modification time. Before the transfer, all 160 existing office files
matched home by SHA-256. After the transfer, independent SHA-256 scans
on both hosts matched all 169 relative file paths. All file and directory
modification times matched at nanosecond resolution. Files were 0600 and
all three directories, including the root, were 0700 on both hosts.

Home file hashes and the modes and modification times of its files and
directories were unchanged. All 160 existing office files retained their
hashes, modes, and modification times. No refused paths, differing files,
office-only paths, or deletions. No commit, push, ledger edit, or bell.
