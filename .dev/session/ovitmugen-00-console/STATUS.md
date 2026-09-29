# STATUS — ovitmugen-00-console

```yaml
updated: 2026-09-29 (office walk GO; scenario 3 added; home selftests pending)
writer: trajectory · anthropic
host: office · hruzam-120922
worktree: |
  ia-sync main at a1d4d25 (ours: ovitmugen P2, 4 paths) on top of origin/main 89b81cb; ahead 1,
  not pushed. P1 0b95adf is already on origin. Other writers' dirty paths in ia-sync are not
  ours (e.g. zsh/ai/temple-project-map.zsh, journal.host-cleanup.md).
  nablarva core — this bed. Other writers' dirty paths in nablarva are not ours.
gate: >-
  Majkee records GO or STOP after walking ovitmugen v1 live on office: frame built from a
  preset, left tab switched from the runbook T modal and from the C-a t popup, split moved,
  and ov-down --idle keeping a tab with a running agent, with ov-selftest and runbook
  selftest green on office and home.
checkpoint: >-
  P1 on origin (0b95adf). P2 committed locally at a1d4d25: runbook T opens the ovitmugen console
  in runbook's own screen and Enter switches the frame's left pane; the bed overview carries a
  cached tmux line. Evidence in the commit message: runbook selftest PASS (with 8 bridge cases,
  real tmux never queried), ov-selftest OK, and a live isolated frame whose fixed pane was the
  real runbook — T, then Enter, moved the left pane to bus and the overview followed.
  Office deployed by majkee 2026-09-29, selftests green, walk in progress. Walk finding 1:
  quitting runbook (q / C-c, exit 0) left the fixed pane dead and ov-up revived only the left
  pane; fixed in ia-sync 794d328 (ov-up revives any dead frame pane; C-a r restarts the focused
  pane), ov-selftest OK with 2 new cases; 794d328 reached origin with another writer's push.
  GATE WALK: majkee walked it on office after deploy — GO (2026-09-29), office selftests green.
  Remaining gate condition: ov-selftest + rb-selftest green on HOME.
  After the walk: help key table + scenarios 1-2 (ia-sync 08d2081), rb-keys/t41 note (1062a31),
  console o = open the bed's frame, scenario 3 (rb-open → T → b → o), help at ≤ 40 columns
  (a4b0cb5, local). Earlier:
  P2.1 batch (majkee go) committed at ia-sync d7d35e0: C-a q numbers persist, console x x
  closes idle tabs (busy and last tab refused), b builds a missing bed, optional slug
  (frame → .dev/session/<bed> cwd → only frame), ov-ls hides grouped views. ov-selftest
  33/33 x3, runbook selftest PASS, live console smoke (b build, x x close) on isolated servers.
  Carried tasks (outside the gate): (1) res/examples.md for the session-browser GUIDE, to be
  written after the live walk so it teaches the final TUI; (2) this bed's
  pad.1-remote-cli-walk.md; (3) parked idea: display-only receipt navigation in the browser.
in_flight: none
recovery_probe: >-
  Run git -C /home/hruzam/ia-sync log --oneline -1 a1d4d25 — it must resolve, and
  git -C /home/hruzam/ia-sync status -sb shows whether it is still ahead (not pushed) or on origin.
  Then python3 /home/hruzam/ia-sync/zsh/session/runbook.py selftest and
  python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py selftest: PASS/OK means the table copy is
  sound; a FAIL names the check. tmux -L ovitmugen ls: "no server" = no live frame yet.
holds:
  - No deploy.sh by this seat, ever; majkee deploys. runbook-upgrade-02-app, whose B0 hold this line once named, closed on 2026-09-27; any germline hold is germline-00-home's to lift.
  - ia-sync journal.host-cleanup.md is another writer's; the proposal lives in raw/journal-proposal.ia-sync.2026-09-25.md.
  - P2 go given by majkee 2026-09-29 ("go with my blessing") and used: runbook.py edits limited to the T modal, the overview line, help text and selftest cases.
  - Never send-keys into agent panes; tests only on isolated tmux sockets.
  - raw/brief.ovitmugen-sentinel.2026-09-04.md (@kukla) stays untouched until majkee rules.
  - Resolved 2026-09-29 — the push hold on b2b7901 (cartan-muticula): ia-sync was pushed through a541808 on 2026-09-27.
next: >-
  majkee on HOME: git -C ~/ia-sync pull, bash deploy.sh, then ov-selftest and rb-selftest,
  and reports both results here.
expected: >-
  "ovitmugen selftest: OK" and "SELFTEST PASS" from home; trajectory then records the gate
  closed (GO) and parks the carried tasks (examples.md, pad.1, receipt navigation).
```
