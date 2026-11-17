---
what: assay's verdict on the witness repeat (witness/recording-2.jsonl), landed by the head (oraculum · claude)
date: 2026-11-16
verdict: PASS WITH GAPS
note: condensed by the head from assay's hand-back; figures are assay's, unchanged. Times local.
---
# Assay — repeat verification

Method: streaming scripts over all 1,333 records; stat and sha256 of the synthetic file.
Assay did not touch Sublime, /run/user/1000, .majkee or .hlm.

## Stamps (8, in time order)
R1 09:53:10 · "R2" 09:53:27 (really the start of typing) · "R2 - stop (sorry, not marked
start), nothing bad happened." 09:57:30 · R3 09:58:44 · R4 start 10:02:06 · "R4 oppened
second view (duplicate)" 10:03:12 · R4 10:05:06 · R5 10:07:00. No "R4 moved".

## Clauses
- A. Stamps — FAIL on labels only: all present and ordered; two carry other text than asked.
- B. Publication scope — PASS. Only /tmp/sublime-observer-witness/shared-one.md was ever
  published; forbidden_hits empty in all samples; no share before the operator's share.
- C. Typing while shared — PASS. Window 243 s (not 20 s). Share present in 394 of 394
  samples; revision 0 to 161, never down. Heartbeat gap worst 1.025 s, median 1.001 s. Longest
  pause between revisions 47.9 s (inferred: typing pauses). No recorder gap over 300 ms.
  One epoch, publisher pid 98209.
- D. Second-view check — PASS WITH GAPS. Selection [{a:19, b:23}] identical at R3, R4 start,
  R4 and in every sample between. viewport_position [0.0, 0.0] in every sample. Revision
  161 to 319, characters 5002 to 5148; the second view never appeared as a separate share;
  index kept one entry. One field changed: visible_region end went 1838 → 1816 (10:00:19) →
  901 (10:01:30) → 1816 (10:01:48) → 901 (10:02:14, inside the window, held through R4) →
  1816 (10:05:11). Cause not determined by assay. Scroll constancy is only trivially shown
  because the view sat at the top of the file.
- E. After R5 — PASS. Share gone at 10:06:42; index empty, `current` absent, views empty;
  publisher still live; end record SIGINT.
- F. Surprises — 5 transient "vanished" listing errors on files being replaced; the file on
  disk was saved once during typing (09:56); the R4 edits were never saved.

## Not shown
Focus; which tab the operator's hands were in; anything shorter than 100 ms; the cause of
the visible_region changes; typing lag as felt (operator's words only); where in the file
the appended text went (inferred after the selection, since offsets 19–23 did not shift).

## Head's reading (not assay's)
- visible_region is the range of characters the view can display. A halving with the scroll
  position fixed at the top means the view's visible height roughly halved and later came
  back — the kind of change a panel, a split layout or a window resize produces. It also
  happened once before "R4 start". The package has no call that resizes anything (static
  test). Cause still to be asked of majkee; until then it is an open observation, not a pass.
- The head's REPEAT.md told majkee to keep the shared view at the top of the file. That made
  the scroll half of the check weak: a view at the top has nowhere to be pushed. This is a
  design fault of the step, not of the walk.
