---
what: assay's verdict on the normal-profile witness, landed by the head (oraculum · claude)
date: 2026-11-16
verdict: PASS WITH GAPS
note: condensed by the head from assay's hand-back; figures are assay's, unchanged. Times local (CET).
inputs: witness/recording.jsonl (28,003 records), witness/CHECKLIST.md, _bus/01, 02, 03, the install task, installed and source package files
---
# Assay — witness verification

Method: streaming scripts over the whole recording; cmp, ls, sha256 on installed, source and
synthetic files. Assay did not touch Sublime, /run/user/1000, .majkee or .hlm.

## Stamps
21 stamps, 1 to 21, in order, none repeated. Steps 1–5 at 01:29–01:35; steps 6–17 at
07:26–08:01; steps 18–21 at 09:02–09:08. End record: 21 stamps, forbidden_hits empty, SIGINT
09:09:11. Missing: any 4b stamp; "13 waited". Stamps 16 and 17 were typed 18 and 11 minutes
after their events.

## Clauses
1. Stamps — PASS WITH GAPS (4b not done; "13 waited" absent).
2. Unshared views publish nothing — PASS. All 27,980 written samples have empty
   forbidden_hits; the marker is really in private.md. Only two paths were ever published,
   overnight included: shared-one.md and shared-two.md under /tmp/sublime-observer-witness/.
   private.md, .env and .majkee appear nowhere. The .majkee refusal happened before the
   recorder started, so the recording is weak evidence for it.
3. Unshare, close, quit — PASS. Each is one sample change; nothing left behind; on quit the
   whole root was gone 1.0 s after the last heartbeat.
4. Restart — PASS. New epoch each time; root absent in between; first sample of each new
   epoch has empty index and views; no sample mixes epochs; shares did not survive.
5. Crash — PASS. Last heartbeat 07:36:02.553; a rule-following reader accepted the capture
   until about 07:36:05.55 (at most about 3 s after the kill, inferred); the whole tree stayed
   until the root vanished at 07:36:07.86 (about 2.3 s of stale residue); nothing remained at
   the restart (07:36:25.7). Who removed it is not shown (inferred: the orphaned plugin host).
   publisher.json pid was 4012592, not the killed 4012466 (inferred: main process versus
   plugin host; the recording cannot link them).
6. Selection and scroll — PASS with a stated limit. Values changed only in steps that match
   typing, a click-drag selection [1462,1480] and scrolling to the bottom and back; the
   selection stayed fixed while the viewport scrolled. The recording cannot show focus,
   samples at 100 ms, and cannot separate operator from package as the cause.
7. Removal and reinstall — PASS. Root absent 07:40:34 to 07:49:52 while the same pid kept
   running; new epoch after reinstall. plugin_python 3.14.6 and build 4215 in all four epochs.
8. Fresh reads — PASS on consistency. Claude and Codex each: four reads succeeded, no prompt
   reported, publisher live (Codex heartbeat age 0.24 s), epoch, seq 3, revision 167, path,
   size 4885 and text.167 all match recorder samples; text hash equals the saved
   shared-one.md. Reader remarks: Claude — 1 s clock resolution, captured_at was 80 s old;
   Codex — heartbeat_at is not labelled as Unix time. Deviations: both sessions started in
   another cwd than the bed (ia-sync and nablarva); Codex ran with approvals "auto_review",
   so a silent auto-approval cannot be excluded. Permission claims rest on the returns' own
   words.
9. Install integrity — PASS. Five installed files identical to source; exactly five entries;
   no staging directory. The three-file listing pasted into the task file is a truncated
   paste (its "total 56" equals the five-file listing; inferred).
10. Cost — PASS. Recorder 10.00 samples/s, sample time median 2.45 ms, max 11.1 ms.
    Publisher heartbeat gap median 1.001 s, worst 1.067 s over all live epochs.
11. Surprises — step 15 is NOT shown: in the epoch 07:36:25–07:40:33 no share existed, so
    the 20 s of typing happened unshared. An extra share of shared-one ran 08:01:14–09:01:54
    (not a checklist step). 30 transient "vanished .tmp-publisher.json" listing errors, one
    sample each. No parse errors, no missing text file, no epoch mismatch; `current` absent
    whenever two shares existed.

## Not shown by this witness
Typing under publication (step 15); step 4b; focus, marker, palette entry, refusal messages,
typing feel, console (operator's eyes); relation of pid 4012466 to 4012592 and who cleaned up
after the kill; Python 3.8, other hosts, concurrent readers; the Codex auto_review caveat.

## Short repeat needed
Share shared-one and type about 20 s with stamps before and after; step 4b; optionally the
publisher pid beside the editor pid.

## Not checked by assay
Sublime processes; /run/user/1000 contents; behaviour of the five source files; overnight
text content; view and buffer ids in index versus the returns.
