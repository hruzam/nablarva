# Phase 0 publication package — preparation only

Snapshot: **2026-10-20T22:55:50.833830+00:00** (2026-10-21 00:55:50 CEST).
Captured STATUS stamp: `d98371cf`. This is historical captured state; later STATUS,
review and next-phase proposal files are not represented. No staging, commit,
push, deployment, prune or next-phase work was performed.

| repository | exact captured HEAD | files | changed / unchanged |
|---|---|---:|---:|
| Nablarva | `fff20b8de570e5d66381ab540d9474ddfff07750` | 875 | 806 / 69 |
| ia-sync | `55e615766143062fe018d29f3e914f9c785fffb5` | 12 | 12 / 0 |

## Scope and prerequisites

Nablarva payload: complete `.dev/session/composer-01-parse/` except this
`evidence/publication.phase0/` directory, plus `.dev/session/flag.md`,
`PROJECT-DESIGN.md` and `toolbox/termbrana/README.md`. This includes the final
`29.builder.return.md`, raw19, prior reviews, complete failure histories and
independent PASS. ia-sync payload: ten files under `zsh/termbrana/`,
`journal.host-cleanup.md`, and only
`.dev/session/germline-07-make-program/raw/brief.germline-contract-testing.md`.
The copied brief preserves historical links relative to its original evidence home.

Review requires both captured base commits and the approved v4/source receipt
retained in the bed. Flight's G05 C1 response is already in ia-sync HEAD; it is a
cited dependency, not a new payload change. Other G04/G05/G06/G07 state, Nablarva
X3/X4/VIST/IDE work, pulse, live configuration and runtime files are excluded.
Per-repo `*.excluded-changes.json` records observed omitted dirty paths, including
this package's own artifacts. Later foreign changes are not frozen by that list.

## Proposed commit units — require separate publication authority

1. **Nablarva: preserve composer Phase 0 and approved product direction.** Only the
   806 paths in `nablarva.changed.paths.nul`: bed additions/changes and reviewed
   L17/product sections. The 69 unchanged references are preserved in the archive
   and already belong to the base; they need no staging.
2. **ia-sync: add verified inert composition source and requested testing brief.**
   Only the 12 paths in `ia-sync.changed.paths.nul`: source family, composer journal
   entry and the one raw brief copy. No sibling session directory is a staging unit.

The text lists expose the exact same paths for review. NUL lists can later be
passed to `git --literal-pathspecs -C <repo> add --pathspec-from-file=<absolute-list>
--pathspec-file-nul` **only after separate authorization and a passing recheck**.
Do not add whole directories or use broad `git add .`/`-A`. Nothing here runs add.

## Artifacts and validation

- `snapshot.json`: roots, heads, timestamp, captured dirty paths and index identity.
- `manifest.json`: 887 sorted repo/path records with SHA256, size, mode and
  disposition (812 new, six modified, 69 unchanged references).
- `payload.tar.gz`, `payload.sha256`: 25,873,046 uncompressed payload bytes;
  repo-prefixed safe regular members, no symlinks/caches. Archive SHA256
  `649e789bc2d3b3ea40658339a393a4f2d289c56b1ec5fdace14ca997cf10e734`.
- Per-repo `*.tracked.patch`: only five tracked Nablarva changes and the ia-sync
  journal change; new files are in the archive. Patches passed `git apply --check`
  against temporary HEAD files. Shared hunks were reviewed for foreign changes.
- `checks.json`: all 887 extracted size/hash comparisons, raw19/v3/v4 pins, exact
  ten-file source receipt, brief equality, retained FAIL/FAIL/PASS/PASS benchmarks,
  temporary patch applicability and unchanged live heads/indices/payload: PASS.
  No suite or benchmark was rerun. `capture.py` records the one-shot construction;
  it refuses to overwrite a completed snapshot. `PACKAGE.SHA256` hashes all package
  artifacts except itself; package files are outside their own payload.

## Recheck immediately before any future staging

From this directory, run these read-only checks; neither grants staging authority:

```sh
sha256sum -c PACKAGE.SHA256
PYTHONDONTWRITEBYTECODE=1 python3 -B recheck.py
```

The recheck requires identical heads, every payload byte/mode, complete payload
path sets, exact changed-path sets and scoped index state. It detects extra and
missing files as well as edits to existing files. Any drift, including a later
STATUS or new POINT, is a stop: obtain a fresh reviewed capture in a new destination,
preserve this package, and review new/foreign hunks. After either proposed commit
changes a HEAD, this original two-repo baseline also needs explicit reconciliation;
do not suppress the check. Independently inspect excluded work before publication.
