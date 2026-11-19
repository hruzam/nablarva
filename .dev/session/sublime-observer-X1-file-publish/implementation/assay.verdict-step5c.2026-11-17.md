---
what: assay's verdict on step 5c (removal submitted before any editor notification), landed by the head (oraculum · claude)
date: 2026-11-17
verdict: PASS WITH GAPS — no blocker, no major
note: condensed by the head from assay's hand-back; figures are assay's, unchanged.
---
# Assay — step 5c

- **Hashes (observed):** publisher.py 0fb95e5c9509dd89786f41e2c4b9c133c620b04b9e0d51a1be5cac959e4d30cb;
  contract.py fc8d951bc31c7543259e6edde207a21322c78854789df28268dfbaa116489eef (unchanged);
  SublimeObserver.sublime-settings 449ad70ba465589e677dfb5e269599c9cb0ae7c2ce493fc91b3bf8be821b1d5d;
  SublimeObserver.sublime-commands 63940d84652e35b78b02225c91bf8b24bc5320de7af78211534222f64e5e4857;
  .python-version 5b02189ab1f9bb5caa7611320f35cd6a072da88db0533f62c4b3194f8bee4b79.
  Five files, no __pycache__.
- **Scope (inferred):** only publisher.py and tests/test_publisher.py carry a 2026-11-17
  mtime; no pre-5c copy was available for a content diff, so "nothing else changed in
  publisher.py" rests on the implementer's note and assay's full read.
- **Unit suite (observed):** 107 tests, OK.
- **Routes (observed by reading):** every path to `store.revoke` goes through
  `_Runtime.unshare` (publisher.py:210–226); seven callers (189, 238, 244, 271, 281, 336 and
  the poll's except branch). Nothing that can raise sits between `revoke()` (215) and the
  submission (216). The submission is skipped only when the writer is stopped, which also
  shuts the store down.
- **Fault injection, real threaded Writer (observed):** `status_message` and `erase_status`
  raising on unshare, sealed save, path unknown, close, invalid view at the poll, and
  unshare-then-reshare — nothing propagated, pending empty, old directory gone, heartbeat
  resumed, exactly one new directory on reshare.
- **Mutants (observed):** 9 of 10 caught, including clear-all-pending (only by the new
  two-revocations test). Not caught: submission placed before `revoke()`.
- **Side effects:** status marker still erased; reshare works; removal on the writer thread
  shares no state with the status-bar update (inferred).
- **Disposable trial (observed):** script unchanged and confined; run by assay, 22 of 22.

## Defects
- **minor** — the suite cannot catch "submit before revoke" because the test writer defers
  execution; with the real writer that ordering could leave a pending id forever. Current
  code is correct (215–216); the gap is in the tests only.
- **note** — publisher.py:204–207, the share route of `toggle` calls `set_status` and
  `status_message` unguarded after registering the share. If one raises, the share does not
  publish until its next event; nothing is written and nothing stays live (inferred).

## Not checked
A content diff against pre-5c publisher.py; a raising notification in the real editor; the
README, install task, shutdown path and reader beyond the suite; a stress run on the real
writer; the operator's editor and the live publication directory (untouched).
