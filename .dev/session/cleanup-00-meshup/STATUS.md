# STATUS — cleanup-00-meshup

```yaml
updated: "2026-10-01 --:-- +02:00 (wall clock not read)"
writer: oraculum · Claude
host: hruzam-120922 (office)
worktree: >
  /home/hruzam/unikuklatrix/nablarva · core · 9421376 · staged = complete cleanup candidate ·
  unstaged: pulse.md (cleanup row + pre-existing nablarva-03 row change), this bed, pre-existing untracked.
gate: >
  Majkee records GO or STOP on Cartan's audit confirming: every former meshup/ path resolves
  under raw.nablarva/ by the one-prefix rule (100 % git renames, zero content edits),
  meshup/REGISTRY.md maps every source to a design slug or names it orphan, each slug carries
  DESIGN.md + HYPOTHESES.md, and the three pointer files carry only the one-line redirect.
checkpoint: >
  majkee GO 2026-10-01 (chat) on Cartan RETURN 02 PASS. Ruling: keep raw/card.A–F.md + raw/slugmap.md
  in raw.nablarva/ (→ raw.nablarva/cleanup-00-meshup/). Commit authority for this closure delegated by
  the GO; executed via Delta.
in_flight: >
  @Delta (prompt-close): copy cards+slugmap to raw.nablarva/cleanup-00-meshup/, append inventory note to
  raw.nablarva/README.md, stage bed + pulse row only (HEAD pulse.md + cleanup row), COMMIT 1 cleanup;
  then remove router row, `git rm -r` the bed, COMMIT 2 closure; restore working-tree pulse.md so the
  nablarva-03 change survives unstaged. Side effects: two commits on core; bed gone from tree.
recovery_probe: |
  git -C /home/hruzam/unikuklatrix/nablarva log --oneline -3
  ls /home/hruzam/unikuklatrix/nablarva/raw.nablarva/cleanup-00-meshup/ 2>/dev/null
  git -C /home/hruzam/unikuklatrix/nablarva status --short .dev/session/pulse.md .dev/session/cleanup-00-meshup
  HEAD 9421376                         → Delta never ran; re-spawn prompt-close.
  one new commit, bed still present    → COMMIT 2 missing; run closure only.
  two new commits, bed absent, pulse.md shows only the -03 change → closed. This file no longer exists; you are reading git history.
holds: >
  Two commits authorized by majkee's GO, no push. pulse.md: cleanup row only; nablarva-03 change stays
  unstaged. Do not read .hlm/ or .dev/session/skill-report-test/. flag.md, other pulse rows, GEMINI.md,
  registry.nablarva.beacon.md: untouched. nablarva-01-design prune is not this gate.
next: >
  Delta executes prompt-close and reports; oraculum confirms `git log -3` and the archive listing to majkee.
expected: >
  COMMIT 1 stat: 51 renames, 1 deletion, additions under meshup/ + raw.nablarva/ (README, cleanup-00-meshup/ 7 files),
  3 pointer M, bed files, pulse.md +1 row. COMMIT 2: pulse.md −1 row, bed deleted. Working tree: pulse.md M (−03 only).
```
