---
what: assay's verdict on step 5 (fix round after the Codex audit), landed by the head (oraculum · claude)
date: 2026-11-16
verdict: PASS WITH GAPS — no blocker, no major defect
note: condensed by the head from assay's hand-back; figures are assay's, unchanged.
---
# Assay — step 5

- **Own unit-test run:** 98 tests, OK. Payload exactly five files; hashes contract.py
  aed98299c12cb69c0cb93813eb2df803ee0894c830443851dc8be60a9721dfab, publisher.py
  59fd8126e54e2821ad04fbca8f764a5b4129471471b828acbcdd5e6f832cf98f; both parse as Python 3.8.
- **Disposable trial not re-run by assay:** its process scan reads `/proc/<pid>/exe` of every
  process, the operator's editor included, so assay did not call it confined. Trajectory's
  saved run (22 of 22) is the implementer's evidence only. The editor launch itself is
  sandboxed (bwrap, own runtime dir).
- **Ordered fixes present in code** (flock ownership, takeover gone; share id in text names;
  reader pins and re-reads; synchronous revoke, fail-closed stop; fresh inodes on update;
  unresolvable path refused; `current` before index; encoding flag).
- **Attacks with real processes and files:**
  - 9,000 racing starts by 6 processes on one root: 0 duplicate holders. 8 starts raised a
    contract error under that churn and did not publish (fail closed).
  - Start during another's shutdown: refused, and never retried for that process's life.
  - SIGKILL of a holder with two shares, 20 rounds: residue gone before the new publisher's
    first write.
  - Share switching at equal revisions, distinct bodies, 16,614 switches: rule-following
    reader 190,955 good reads, 0 wrong pairings; naive `current/`-only reader 242,963 good
    reads, 0 wrong pairings (missing file instead).
  - Removal failure: with `views/` unwritable the reader saw "not live" at once; with the
    whole root read-only the capture still passed the live check until the 3 s bound, then
    failed. Nothing passes after the bound.
  - Update block with a hard-linked destination: the unrelated file untouched.
- **Mutation:** implementer's 17 all caught on re-run. Of assay's own 14, not caught: the
  lock-file owner check, unlink-without-verify of the lock, dropping O_CLOEXEC, a harmless
  heartbeat re-arm. The reader's directory pin alone is also uncaught (the second state read
  covers it).
- **Static guard:** passes on the new code; `fcntl` used once for `flock`; no socket,
  subprocess, signal or view-changing call. Whether the test file was loosened cannot be
  diffed (untracked tree); its date predates step 5.
- **Task file:** version 1.1; all script blocks pass `bash -n`; check block ran read-only and
  printed "prereqs ok". Operator notes present; byte-identity not provable without a base.
- **Regressions:** none seen. Plugin reload inside a running editor not tested by assay
  (trajectory's trial check 10 covers it; first shown to assay's standard only at the smoke).

## Limits that remain (assay's opinion: acceptable, none breaks a gate clause)
- A publisher that starts while another is shutting down refuses for its whole life.
- A lock descriptor inherited through a bare fork would block the next start (fail closed).
- A capture already being written when a share is revoked finishes first: readable for
  milliseconds; "no capture presented as current" holds after removal completes or after the
  3 s bound.
- Save-as into a sealed path and removal failure are shown only by unit tests and file-level
  runs, not in the real editor.

## Minor defects
Contract error under extreme start contention; no catching test for lock ownership and
O_CLOEXEC; README contract not yet rewritten for the new read rule (head's closure work).
