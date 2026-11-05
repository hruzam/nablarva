# Current Phase 0 preservation package — preparation only

Snapshot: **2026-10-21T02:28:58.322744+00:00** (04:28:58 CEST).
Captured STATUS stamp: `64860023`; cycle37 documentation cleanup is ACCEPT and
cycle38 preservation review is pending. This package includes the finalized
`38.builder.return.md`. Later head STATUS, verdict or report changes are
post-capture; no future file is represented as captured. No staging, commit,
push, delivery, deployment, activation, product test run or pruning occurred.

| repository | exact captured HEAD | files | changed / unchanged |
|---|---|---:|---:|
| Nablarva | `fff20b8de570e5d66381ab540d9474ddfff07750` | 929 | 860 / 69 |
| ia-sync | `55e615766143062fe018d29f3e914f9c785fffb5` | 12 | 12 / 0 |

## Exact scope and retained dependencies

Nablarva payload is the complete `.dev/session/composer-01-parse/` except
`evidence/publication.phase0/` and `evidence/preservation.phase0.cleanup/`, plus
`.dev/session/flag.md`, `PROJECT-DESIGN.md`, `toolbox/termbrana/README.md` and only
`.dev/session/termbrana-X1-composer-sourcing/raw/handoff.cartan.runbook-preparation.2026-10-21.md`.
It retains raw19, every prior grammar/candidate/review, both failed timing runs,
subsequent PASS evidence and the accepted cleanup/report records.

ia-sync payload is the exact accepted ten files in `zsh/termbrana/`, the
Composer-only diff of `journal.host-cleanup.md`, and only
`.dev/session/germline-07-make-program/raw/brief.germline-contract-testing.md`.
Source facts remain uncommitted source-only evidence; this capture creates no
commit pin, loader, live role or sending authority. The copied brief's historical
relative links continue to refer to its original Composer evidence home.

Both preservation-package directories are outside this payload. Package29 stays
unchanged and separately retained at `../publication.phase0/`: all twenty checksum
entries passed. Its archive SHA256 is
`649e789bc2d3b3ea40658339a393a4f2d289c56b1ec5fdace14ca997cf10e734`;
its `PACKAGE.SHA256` identity is
`0dca1f582ba611f195cda83fd6b480bbd46f30016c9cdb169cc664305f26b06d`.
Neither dependency is nested in the new archive.

One original input ZIP remains opaque history: Composer
`evidence/import/files.zip`, 11,408 bytes, SHA256
`7d7251b6ed19ba07747dd3cee72388a22b1813c13a9b62a0d44fd63b1ae70aa1`.
The initial guard rejected it before creating a snapshot. Cartan clarified that
POINT38 prohibits preservation-package nesting; this exact existing input stays
within the complete-bed scope. Its identity matches package29. It was neither
extracted nor executed; any other unexpected archive still fails the guard.

Flight's G05 C1 response is already in ia-sync HEAD at
`.dev/session/germline-05-sella-germline-audit/_bus/RETURN.01.c1-composition.cartan.md`
(SHA256 `a2b989540f241adccc2f13d12d215d585620887aa04bec823bf2af1e78b1009a`).
It remains a cited committed dependency, outside the new payload.

Other G06/G07/X2/architecture/VIST state, pulse, personal reposoma journal, live
configuration/runtime/credentials and sealed `.hlm` are excluded. Only allowlisted
paths were inspected; omissions state scope, not an inventory of all foreign work.
No vault content was read. Shared allowed hunks were checked for Composer ownership.

## Proposed commit units and prerequisites

1. **Nablarva:** only the 860 paths in `nablarva.changed.paths.nul`: Composer
   records, reviewed RUNBOOK/STATUS/L17 and two product-doc sections, plus the exact
   requested X1 raw handoff. The 69 unchanged references need no staging.
2. **ia-sync:** only the twelve paths in `ia-sync.changed.paths.nul`: accepted
   inert source family, Composer journal entry and exact G07 brief. A sibling
   session directory is not a staging unit.

These are proposals requiring separate publication authority and a current passing
reconciliation. Do not stage whole directories. Require both captured base commits,
source/v4 receipts, independent head review, separately retained package29 and
review of shared/foreign hunks before publication. Durable evidence pins and process
observation promotion remain owed before any closure/prune; this capture grants none.

## Artifacts and observed checks

- `manifest.json`: 941 sorted repo/path/hash/size/mode/disposition records;
  866 new, six modified, 69 unchanged references; 26,261,819 payload bytes.
- `payload.tar.gz`: 970,828 compressed bytes; SHA256
  `ed95f7dce28c60b0dfd0fc66eef00cc906afa8322c899892be3adfee05aaec0f`.
  All 941 names, counts, regular-file types, sizes, hashes and modes match the
  manifest; temporary extracted bytes/modes match. No excluded member or symlink.
- `snapshot.json`: exact time, heads, captured changed paths and index identities.
  Index paths were resolved with `git rev-parse --git-path index`.
- Per-repo text/NUL changed lists agree; scoped status and tracked patches retain
  only the allowed scope. Both patches passed `git apply --check` against temporary
  HEAD files. Real heads and indices were unchanged.
- `checks.json`: raw19/v3/v4 pins, ten source identities, G07 brief equality,
  retained FAIL/FAIL/PASS/PASS history, old twenty checksums and strict live recheck
  all PASS. No product suite or benchmark reran.
- `comparison.package29.json`: 884 identical files, only STATUS and the two accepted
  cleanup docs modified, 54 later Composer records/exact X1 handoff added, none
  removed and no unexpected drift.
- `report-check.json`: substantive contextual-report claims and owner boundaries
  checked against actual docs/evidence; saved timing statistics recomputed. Its
  package completion reference is now fulfilled by this README. The future38
  head-verdict link intentionally remains pending and supplies no prior PASS.
- `capture.py` records the one-shot construction and refuses to overwrite a
  completed snapshot. `PACKAGE.SHA256` hashes every package file except itself;
  package metadata is outside its own payload.

## Read-only recheck before any future publication

From this directory:

```sh
sha256sum -c PACKAGE.SHA256
PYTHONDONTWRITEBYTECODE=1 python3 -B recheck.py
```

The recheck requires identical heads, payload bytes/modes and complete path sets,
changed-path sets, resolved index paths and scoped index state. Extra/missing files
and later STATUS/report/verdict edits cause a hold. Preserve this frozen package;
reconcile new state in a fresh reviewed destination rather than suppressing drift
or overwriting it. After a commit changes either HEAD, the captured baseline also
requires explicit reconciliation. These commands grant no staging authority.
