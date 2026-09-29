# STATUS — ovitmugen-00-console

```yaml
updated: 2026-09-29 (carried-in tasks; stale holds resolved)
writer: trajectory · anthropic
host: office · hruzam-120922
worktree: |
  ia-sync main — P1 is committed at 0b95adf and pushed (origin/main a541808 contains it).
  Other writers' dirty paths in ia-sync are not ours.
  nablarva core — this bed plus, from 2026-09-29, pad.1-remote-cli-walk.md.
  Other writers' dirty paths in nablarva are not ours.
gate: >-
  Majkee records GO or STOP after walking ovitmugen v1 live on office: frame built from a
  preset, left tab switched from the runbook T modal and from the C-a t popup, split moved,
  and ov-down --idle keeping a tab with a running agent, with ov-selftest and runbook
  selftest green on office and home.
checkpoint: >-
  P1 was built and committed in ia-sync 0b95adf. The evidence is in that commit message:
  ov-selftest 21/21 on isolated sockets across 6 consecutive runs, a console Enter-switch smoke,
  a read-only dry-run and ls against the real default server (nothing created), zsh -n clean,
  runbook selftest PASS. Not deployed. P2 (the runbook T modal) has not started.
  Carried in on 2026-09-29, by majkee's rule "move where is closest session held in scope".
  These are tasks inside this session; they are not part of its gate:
  (1) res/examples.md — the walkthrough chapter for the session-browser GUIDE, at
  /home/hruzam/reposoma/raw.guides/session-browser/res/examples.md. It comes from runbook-tool-00,
  which is now pruned. majkee: "still need to have some backup file which teaches me". Write it
  after P2 lands, so it teaches the final TUI. Until then, the GUIDE's Verbs and TUI map
  sections teach the basics.
  (2) pad.1-remote-cli-walk.md — the deferred remote-cli tests (steps 0–6) and the muscle-memory
  drills. It comes from codex-remote-control-cli-01-wrapper, which is now pruned. Step 7 is done
  on both PCs and on the phone (majkee): the rotation debt is zero.
  (3) A parked idea from runbook-tool-00: receipt navigation in the browser, display-only.
  runbook-tool-00's home-selftest items are covered by this gate's "runbook selftest green on
  office and home".
in_flight: none
recovery_probe: >-
  Run git -C /home/hruzam/ia-sync log --oneline -1 0b95adf — it must resolve (P1 on the table).
  Then python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py selftest: OK means the table copy is
  sound; FAIL names the broken check. Then tmux -L ovitmugen ls: "no server" means no live frame
  exists (expected before deploy). Carried tasks: this bed's pad.1-remote-cli-walk.md exists,
  and the session-browser GUIDE has no res/examples.md yet.
holds:
  - No deploy.sh by this seat, ever; majkee deploys. runbook-upgrade-02-app, whose B0 hold this line once named, closed on 2026-09-27; any germline hold is germline-00-home's to lift.
  - ia-sync journal.host-cleanup.md is another writer's; the proposal lives in raw/journal-proposal.ia-sync.2026-09-25.md.
  - P2 edits /home/hruzam/ia-sync/zsh/session/runbook.py; start only on majkee's word. The old reason (muticula B4 sharing zsh/session/) is gone with the abandoned B1 plan.
  - Never send-keys into agent panes; tests only on isolated tmux sockets.
  - raw/brief.ovitmugen-sentinel.2026-09-04.md (@kukla) stays untouched until majkee rules.
  - Resolved 2026-09-29 — the push hold on b2b7901 (cartan-muticula): ia-sync was pushed through a541808 on 2026-09-27.
next: >-
  majkee tells trajectory whether P2 may edit runbook.py now. The earlier relay of the P1 notice
  to cartan-muticula is moot: that bed closed on 2026-09-27.
expected: >-
  majkee's word (go or wait on runbook.py); trajectory then rewrites STATUS with P2 in_flight or
  a wait hold.
```
