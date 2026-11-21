# STATUS: relay-X0-carryover

```yaml
updated: 2026-11-21 22:15 CET
writer: engineer (trajectory · claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) · sole pen of this bed
host: home · hruzam
worktree: /home/hruzam/unikuklatrix/nablarva · core · upstream origin/core. Foreign uncommitted work present and left alone —
  vist-X0-helloWorld/RUNBOOK.md (Majkee's goal edit), vist-X0-helloWorld/majkee-personal-notes.md (his).
pen: engineer since 2026-11-21 (Majkee, raw/decision.majkee.open-bed.2026-11-21.md).
team: >-
  Two at work — engineer (pen) and cartan (controller — hands, push, non-author check). Two on call — oraculum (opposer,
  counter-signature) and auditor (one bounded audit). Desk — myshell (continuity). Roles, ids and doors are in the roster.
shape: No RUNBOOK. Goals are small files in goals/ (provisional, uncanonical try — Majkee D3.5). This STATUS is the only doing-state
  and the only entry point; it names every other file (goals/README.md rule 9).
files:
  decision: raw/decision.majkee.open-bed.2026-11-21.md             # Majkee's words that opened the bed, with his own inline notes
  decision_team: raw/decision.majkee.team-and-doors.2026-11-21.md  # controller job, reply bell, who pushes, team
  answer: raw/answer.majkee.reminder-and-leftovers.2026-11-21.md   # his two questions — reminder script, vistMini leftovers
  export: raw/export.vist-x0.engineer.2026-11-21.md                # rev 2, checked once by a non-author
  roster: raw/roster.2026-11-21.md                                 # rev 2 — seats, doors, roles; re-read against live tmux before any poke
  pokes: raw/pokes.log.md                                          # every poke sent, append-only
  goals: goals/README.md                                           # rules + index G0–G10
  goals_overview: goals/OVERVIEW.md                                # for Majkee — context, buys, cost, consequences; the goal files win
  bus: _bus/                                                       # 01, 02 closed · 03 cartan, 04 oraculum, 05 auditor open
  line_ledger: ../relay-X.ledger.md
  card: ~/reposoma/_cold-start/card/CS.relay-X0-carryover.2026-11-21.md   # clean-table entry; a pointer, not a second state
gate: >-
  PROVISIONAL (drafted by the pen holder; Majkee confirms or rewrites) — Majkee accepts the non-author-checked carry-over
  export and the first goal set as the clean-table start of relay work. Accepting it runs no goal that names a release.
checkpoint: >-
  Bed opened 2026-11-21. All 45 files of vist-X0-helloWorld read; nothing there moved or changed. Cycle 01 closed — cartan's
  non-author check accepted, export repaired once to rev 2, goals revised. Cycle 02 closed — myshell answered, ledger row
  committed with her merge. Evening — Majkee widened the team, asked for a reply bell, gave the push to the controller and
  asked two questions (answered on disk; the reminder became draft goal G10). Cycles 03–05 dispatched to bind the wider team
  and to get two outside reads of the plan and the bed. No experiment ran. The only sends are coordination pokes (raw/pokes.log.md).
goals_done: G2 export-verified
goals_running: >-
  G1 party-binding rev 3 — engineer, cartan, myshell bound in cycles 01–02. Cycles 03–05 bind cartan's wider role, oraculum
  and the auditor, each with its own capability probe and the reply bell.
  G9 custody-and-handoff — part (b) done except the presence mark, which stays until this session ends. Part (a) waits for Majkee.
in_flight:
  - cycle 03 → cartan · _bus/03.engineer.point.md · return _bus/03.cartan.return.md · includes ONE plain git push of core if only ahead
  - cycle 04 → oraculum · _bus/04.engineer.point.md · return _bus/04.oraculum.return.md · read-only challenge of the plan, G10 and the gate text
  - cycle 05 → auditor · _bus/05.engineer.point.md · return _bus/05.auditor.return.md · read-only audit of this bed
  - Goal files are not edited while these are open (goals/README.md rule 8).
recovery_probe: |
  hostname -s; git -C /home/hruzam/unikuklatrix/nablarva status --short; git -C /home/hruzam/unikuklatrix/nablarva log --oneline -5
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/     # every POINT needs a RETURN and a VERDICT; 03–05 are open
  tail -30 /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
  ls -d /tmp/vc08r1.tkz50zbf /tmp/vc08r2.kk50sqqh                                 # C04 inputs; gone after a reboot (tmpfs)
  Before any poke: re-read the roster against live tmux (window names, pane ids, footer thread ids). Ids go stale on rebuild.
  Was the push of cycle 03 made? Compare `git rev-parse origin/core` with the RETURN before asking for another push.
  A new Claude session is a new seat: it takes this pen only on Majkee's word, recorded in a decision file here.
holds:
  - L12 — core, plain pull/push, never pull --rebase. Working hold — path-scoped commits, foreign dirty work untouched.
  - L21 — no shared-layer, framework or transport implementation, activation or delivery. G4, G6, G7, G8, G9(a) and G10 each need Majkee first.
  - L22 — `.majkee/` and `.hlm/` are never read. myshell works there; I talk to the seat only.
  - Origin bed vist-X0-helloWorld — untouched. Majkee said control is "shifted to home"; my reading is that I record his ACCEPT /
    REVISE / STOP there when he says it. He has not said it. His two uncommitted files there are his.
  - No U-case (U01–U06) runs here until Majkee accepts the X0 packet or explicitly carries that case here.
  - Never retry or clear historical t03 and c08r1-05-ae3ee8e7. No carrier switch after an uncertain send.
  - Pokes — file first, look first, one labelled line, logged. Party panes are shell-rooted. Every POINT carries a mandatory
    reply bell (Majkee's note); a bell is a hint and the file is the truth.
  - Push — the controller pushes on my poke (Majkee's note). I commit path-scoped and do not push from this session.
  - Run without Majkee where no release is needed (his note). Go to him for the gate, releases, custody and his X0 decision.
  - Goals — a POINT names goal + rev; a goal under an open POINT is not edited (goals/README.md rule 8).
next: >-
  Verify the three RETURNs against the files and write VERDICTs 03–05. Then cycle 06 — G3, the read-only door inventory, to cartan.
expected: >-
  cartan confirms from his own probe that his seat reaches tmux and the Git remote, and origin/core moves by one push.
  oraculum and the auditor each return findings that Majkee can read before he decides on the gate.
owed:
  - Majkee — confirm or rewrite the gate (two outside reads of it are on the way in cycles 04 and 05).
  - Majkee — G9(a), what happens to the /tmp C04 inputs (copy host-local, or let go).
  - Majkee — G10, go or no-go on stage 1, and where the script lives.
  - Majkee — his ACCEPT / REVISE / STOP on the X0 packet.
  - Majkee — releases per goal (G4, G6, G7, G8) when he wants them; the four older decisions in export §10.
  - Majkee — his line to cartan sat unsent in the controller composer at 20:58Z.
open_costs_of_this_shape:   # cartan's objections, cycle 01 — real, accepted for the try, reported to Majkee
  - Changeable goal files can retarget running or reviewed work. Mitigated by rule 8, not removed.
  - Without a RUNBOOK, authority and recovery depend on this STATUS staying complete.
  - X0's open gate leaves two beds able to propose the next U-case; only the hold above separates them.
presence: reposoma _active id e848f1047ab5e6562bfde21aeab037ef (unmark by this exact id when this session ends)
provisional_coordination: uses ~/reposoma/raw.guides/bus/res/file-poke.md; retirement debt carried as goal G7 through
  /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md.
```
