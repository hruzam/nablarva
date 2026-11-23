# Side quest s01 — office custody copy

The copy is on office (`hruzam-120922`) at the same custody path. Both hosts had **245 files** at the final verification cutoff. Home held **1,324,140 bytes** and office held **1,323,142 bytes**. The difference is entirely in two live logs.

## Transfer and verification

```sh
rsync -a --no-owner --no-group --ignore-existing \
  -e 'ssh -o BatchMode=yes -o ConnectTimeout=8' \
  /home/hruzam/.local/share/nablarva/custody/x1-probes-2026-11-22/ \
  office:/home/hruzam/.local/share/nablarva/custody/x1-probes-2026-11-22/
```

The target was absent before the first pass. The first run exited 0 and verified 244 files. An additional home file appeared after that check, so I ran the same command once more to copy newly arrived files while retaining the snapshots already on office. The second run exited 0.

Independent Python SHA-256 checks over SSH verified **243 full-file hashes and modification times**. For the two shorter office logs, SHA-256 matched the corresponding home prefix exactly. Relative file sets and directory trees matched at the cutoff. Directory modification times matched, and all folders were 0700 and files 0600.

## Live — snapshot only

| Relative file | Home bytes | Office bytes | Verification |
|---|---:|---:|---|
| `tracker-manual.u7ady8az/chain.jsonl` | 247,371 | 246,849 | Matching SHA-256 over the copied prefix |
| `tracker-manual.u7ady8az/tracker.jsonl` | 113,506 | 113,030 | Matching SHA-256 over the copied prefix |
| `tracker-manual.u7ady8az/pty-output.jsonl` | Same as office at cutoff | Same as home at cutoff | Full hash and mtime matched. An open writer was observed. |

The three named writer processes remained active. No refusals, missing paths, unexplained hash differences, or invalid modes were observed. No deletion, Git operation, or pane input. This is a point-in-time copy. A final pass for later growth or new files remains a separate request.
