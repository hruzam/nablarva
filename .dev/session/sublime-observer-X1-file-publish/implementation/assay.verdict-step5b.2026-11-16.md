---
what: assay's verdict on step 5b (bounded revocation after the re-audit), landed by the head (oraculum · claude)
date: 2026-11-16
verdict: PASS WITH GAPS — no blocker, no major
note: condensed by the head from assay's hand-back; figures are assay's, unchanged.
---
# Assay — step 5b

- **Basics:** own run 105 tests OK; hashes contract.py fc8d951bc31c7543259e6edde207a21322c78854789df28268dfbaa116489eef,
  publisher.py f519aec57e196cf9c20f42c0a91b77f428615c96ab7ac7ef49cf0342fd06f8b2; five files;
  parses as Python 3.8 (not executed on 3.8); install task unchanged; static test unchanged.
- **R1 (bounded revocation):** `revoke()` marks the share pending under a lock with no I/O;
  the mark clears only after removal succeeds; `heartbeat()` reads the clock, then checks
  pending at execution time under the same lock. Real writer thread, real files, 400 rounds
  with slow queue, slow writes, two shares and jitter: 0 reads of a revoked capture at or
  after revoke + stale bound; 135 heartbeat writes in flight across the revoke, none stamped
  at or after it; heartbeat resumed with the other share readable 200 of 200.
- **Stuck pending:** ten cases (never-published share, double unshare, close during loading,
  sealed save, shutdown, removal failure) — pending clears or the publisher stops with a
  console line. Silent stuck state needs the writer thread itself to die (inferred, not
  tested); it fails closed.
- **Normal operation:** heartbeat age under 1.3 s over edit cycles; typing and sharing never
  set pending.
- **R2, R4:** closed. Untitled buffers are not unshared spuriously.
- **Mutation:** implementer's 10 caught on re-run; of assay's own 10, two uncaught — clearing
  all pending instead of one id (no test with two revocations pending at once; real code
  correct), and a near-equivalent reorder.
- **Regressions:** none. Lock race 3,196 starts, at most one owner. Disposable trial judged
  confined (reads /proc only for itself and its own children) and re-run by assay: 22 of 22.

## The gate sentence
True only if "the event" is the instant `revoke()` returns in the editor. For a crash, the
last heartbeat stamp precedes the death. False or unbounded for: (a) the time before the
editor dispatches the operator's action; (b) a sealed path found late — a changed name waits
for an event or the poll, a symlink retargeted under an unchanged name while idle is never
detected; (c) a reader that checked liveness earlier or skips the rule; (d) a wall clock
stepped back; (e) restart or unload: `stop()` does not mark pending, so a heartbeat blocked
behind a slow publish can stamp after the stop call — exceeded only if the process dies in
that window (inferred, minor); (f) a second writer after the root was replaced.

## Minor defects
No test for two simultaneous pending revocations; the (e) window.

## Not checked
Execution on Python 3.8; the real editor; trial-confinement mutations (saved evidence only);
a real filesystem stall.

Disclosure by assay: one `pgrep -c -f nablarva-observer-4215` with output discarded, to look
for leftover disposable processes; the pattern matches only the disposable path.
