# STATUS — ovitmugen-00-console

```yaml
updated: 2026-09-25 13:20 CEST
writer: trajectory · anthropic
host: office · hruzam-120922
worktree: |
  ia-sync main at 0b95adf (ours: ovitmugen P1, 8 paths), on top of b2b7901 (cartan-muticula,
  local, push not authorized). ahead 2, not pushed. Our paths clean. Other writers' dirty paths,
  not ours: AGENTS.md, journal.host-cleanup.md, claude|codex/skills/chatbot-port/SKILL.md,
  .dev/session/invariance-autonomy/, .dev/session/runbook-upgrade-02-app/, .dev/session/germline-00-home/,
  _staging/codex/germline-home.return.2026-09-25.md.
  nablarva core at fbb60fe + this bed commit (RUNBOOK, STATUS, notice, journal proposal, pulse row).
  Other writers' dirty paths, not ours: .dev/session/AGENTS.PROJECT-DESIGN.md, AGENTS.md,
  PROJECT.yaml, .shared/agents/convergence.md (deleted), .germline/.
gate: >-
  Majkee records GO or STOP after walking ovitmugen v1 live on office: frame built from a
  preset, left tab switched from the runbook T modal and from the C-a t popup, split moved,
  and ov-down --idle keeping a tab with a running agent, with ov-selftest and runbook
  selftest green on office and home.
checkpoint: >-
  P1 built and committed in ia-sync 0b95adf. Evidence in that commit message: ov-selftest
  21/21 on isolated sockets across 6 consecutive runs, console Enter-switch smoke, read-only
  dry-run and ls against the real default server (nothing created), zsh -n clean, runbook
  selftest PASS. Not deployed. P2 (runbook T modal) not started.
in_flight: none
recovery_probe: >-
  Run git -C /home/hruzam/ia-sync log --oneline -3 and git -C /home/hruzam/ia-sync status -sb.
  0b95adf present and our 8 paths clean means P1 is safe on the table; if 0b95adf is absent, P1
  was never committed: check git status for the ovitmugen paths before rebuilding anything.
  Run python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py selftest: OK means the table copy
  is sound; FAIL names the broken check. Then run tmux -L ovitmugen ls: "no server" means no
  live frame exists (expected before deploy); any listed session is a live frame to inspect.
holds:
  - No push of ia-sync while b2b7901 (cartan-muticula) is unauthorized for push.
  - No deploy.sh by this seat, ever; majkee deploys after runbook-upgrade-02-app lifts its B0/germline hold.
  - ia-sync journal.host-cleanup.md is another writer's; proposal lives in raw/journal-proposal.ia-sync.2026-09-25.md.
  - P2 edits /home/hruzam/ia-sync/zsh/session/runbook.py; start only after majkee's coordination word (muticula B4 shares zsh/session/).
  - Never send-keys into agent panes; tests only on isolated tmux sockets.
  - raw/brief.ovitmugen-sentinel.2026-09-04.md (@kukla) untouched until majkee rules.
next: >-
  majkee relays /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/raw/notice.ovitmugen-p1-zsh-session.2026-09-25.md
  to cartan-muticula and tells trajectory whether P2 may edit runbook.py now.
expected: >-
  majkee's word in this session (go or wait on runbook.py); trajectory then rewrites STATUS
  with P2 in_flight or a wait hold.
```
