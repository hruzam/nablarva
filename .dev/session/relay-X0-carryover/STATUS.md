# STATUS: relay-X0-carryover

```yaml
updated: 2026-11-22 03:38 CET
writer: engineer (trajectory · claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) · sole pen of this bed
host: home · hruzam
worktree: /home/hruzam/unikuklatrix/nablarva · core · upstream origin/core. The controller pushes on my poke; a poke that would
  land inside one of his working turns waits until the turn ends. Foreign uncommitted work present and left alone — vist-X0-helloWorld/RUNBOOK.md (Majkee's goal
  edit; he said it can be left as is), vist-X0-helloWorld/majkee-personal-notes.md (his).
pen: engineer since 2026-11-21 (Majkee, raw/decision.majkee.open-bed.2026-11-21.md).
team: >-
  Two at work — engineer (pen) and cartan (controller — hands, crawling through helpers, non-author check, push). On call —
  oraculum (opposer and counter-signature; files only, no bell, no code) and auditor (kept by Majkee as independent observer;
  labeller for U01). Desks — exec (Majkee's decision desk for this bed, kept; bounded forks) and myshell (continuity).
  Roles, ids, doors and the child-seat rule are in the roster (rev 5).
shape: No RUNBOOK. Goals are small files in goals/ — Majkee keeps the try "where make sense" (walkthrough T10); a named
  sub-session may get its own GOAL.md. This STATUS is the only doing-state and the only entry point. Goal files,
  goals/README.md and goals/OVERVIEW.md carry no "running" and no order.
files:
  decision: raw/decision.majkee.open-bed.2026-11-21.md             # Majkee's words that opened the bed, with his own inline notes
  decision_team: raw/decision.majkee.team-and-doors.2026-11-21.md  # controller job, reply bell, who pushes, team
  decision_push: raw/decision.majkee.push.2026-11-22.md            # the controller pushes on my poke without asking him each time; settles walkthrough T9 item 1
  decision_desk: raw/decision.majkee.desk-routing.2026-11-22.md    # decisions owed by him go through the exec desk — I write a sheet and poke the desk at once
  decisions_walkthrough: raw/decision.majkee.walkthrough.2026-11-21.md   # his answers to eleven themes, written by the exec desk (cycle 10); sha256 a183f96b0995cee63be2964d2bece37a0826b477e04987cac5e45b3d3c9043a6; checked in _bus/10.engineer.verdict.md
  walkthrough: raw/walkthrough.sheet.2026-11-21.md                 # the sheet the desk worked from (cycle 10)
  sheet_2: raw/walkthrough.sheet-2.2026-11-22.md                   # five themes for the exec desk (cycle 14) — U01 result, rest of the captures, gate, monitor-silence, two calls of mine
  decisions_walkthrough_2: raw/decision.majkee.walkthrough-2.2026-11-22.md   # written by the exec desk during cycle 14; absent until Majkee starts
  answer: raw/answer.majkee.reminder-and-leftovers.2026-11-21.md   # his two questions — reminder script, vistMini leftovers
  export: raw/export.vist-x0.engineer.2026-11-21.md                # rev 4, sha256 93577f694a33b427f525614bf67eb8a125172f116604afca0c31fbd6508f10a2 — checked by a non-author (cycles 01, 06, 08, 09); accepted by Majkee as baseline (T7)
  inventory: raw/doors.inventory.2026-11-21.md                     # G3 output, written by cartan; sha256 61421058a6faf0f42045c480203fd85633b33a3eaf215acc871b39ecf690792c
  incident: raw/incident.stray-claude-session.2026-11-21.md        # a Claude session started by accident in cycle 07; Majkee — the transcript stays
  roster: raw/roster.2026-11-21.md                                 # rev 5 — seats, doors, roles, child seats; re-read against live tmux before any poke
  pokes: raw/pokes.log.md                                          # every poke sent, append-only
  custody_tool: scripts/c04-custody.py                             # written by the exec desk's Astrobley child on Majkee's word (T2); restore tested by me
  custody_private: ~/.local/share/nablarva/custody/                # host-local on home, 0700, never Git — c04-2026-11-21/ (eight pinned inputs) · u01-2026-11-22/ (helpers' crawl files, the selector's groups.md, the auditor's audit.blind.md)
  u01_report: raw/u01.fixture-selection.2026-11-22.md              # masked selection report, written by cartan (cycle 12 text); result MISSING
  exp: exp/                                                        # noncanonical notes on how the team works (Majkee, T10)
  goals_rules: goals/README.md
  goals_overview: goals/OVERVIEW.md                                # written for Majkee before the walkthrough; not rewritten since — the goal files win
  line_ledger: ../relay-X.ledger.md
  origin_closed: ../vist-X0-helloWorld/STATUS.md                   # stopped by Majkee; his words in ../vist-X0-helloWorld/raw/decision.majkee.stop-and-carry.2026-11-21.md
  card: ~/reposoma/_cold-start/card/CS.relay-X0-carryover.2026-11-21.md   # clean-table entry; a pointer, not a second state
goals:   # every goal file, its rev, and where it stands. This list is the state; the files hold the definition.
  - G0.umbrella.md · rev 4 · umbrella of this bed, confirmed by Majkee (T3)
  - G1.party-binding.md · rev 4 · bound — engineer, cartan, myshell, oraculum, auditor, exec (confirmed itself in cycle 10). Stays open for rebuilds and new seats.
  - G2.export-verified.md · rev 4 · DONE — closed by VERDICT 09
  - G3.door-inventory.md · rev 4 · DONE — VERDICTs 07, 08. No door adopted.
  - G4.u01-unknown-view-fixture.md · rev 4 · DONE — result MISSING (cycles 11–13). The selector's table and the auditor's blind labels agree on all 46 frames without a signature literal; the other 15 are help or approval screens. The case U01 itself stays untested; what follows is asked of Majkee (sheet 2, S1).
  - G5.receiver-policy-contract.md · rev 2 · not started; paper only; covers U03–U06, which this bed now owns (T4)
  - G6.u02-exit-race.md · rev 3 · parked by Majkee (T8) until a scoped proposal; goes with G8 to the successor stage
  - G7.retire-file-poke.md · rev 3 · tracked, open obligation (T8) — the file-poke stays in use until a qualified replacement is approved; follows the bed that qualifies one
  - G8.door-probes-live.md · rev 1 · NOT released. Placement was left to me (T8) — see `decided_by_engineer`. No live send before Majkee has seen the exact test scope.
  - G9.custody-and-handoff.md · rev 4 · (a) DONE — eight pinned inputs in private custody, 8 of 8 hashes re-checked (VERDICT 10) · (b) card written; presence stays marked until this session ends
  - G10.friendly-reminder.md · rev 2 · deferred by Majkee (T6) to a later stage or a separate team; his design direction (chess clock, operator surface in the session-window helper) is in the record
u_cases:   # all six belong to this bed since the STOP of X0 (T4). Belonging is not a release.
  - U01 → G4 · the read-only search is done, result MISSING — no fixture exists in the trial captures; the case stays unqualified until Majkee decides what follows
  - U02 → G6 · parked
  - U03, U04, U05, U06 → G5 · paper contract only, not started; no live case released
bus:     # every cycle. A cycle is closed only by its VERDICT.
  - 01 · cartan · non-author check of export rev 1 and goals · CLOSED · 01.engineer.point.md, 01.cartan.return.md, 01.engineer.verdict.md
  - 02 · myshell · ledger merge question · CLOSED · 02.engineer.point.md, 02.myshell.return.md, 02.engineer.verdict.md (durable pointer nablarva 02e1b6f)
  - 03 · cartan · controller binding, probe, first push, bell · CLOSED · 03.engineer.point.md, 03.cartan.return.md, 03.engineer.verdict.md
  - 04 · oraculum · counter-read of plan, G10 and gate — her verdict REVISE, accepted · CLOSED · 04.engineer.point.md, 04.oraculum.return.md, 04.engineer.verdict.md
  - 05 · auditor · audit of the bed — seven findings, all confirmed · CLOSED · 05.engineer.point.md, 05.auditor.return.md, 05.engineer.verdict.md
  - 06 · cartan · two pushes; re-check of export rev 2 repairs; check of the ledger merge · CLOSED (ACCEPT) · 06.engineer.point.md, 06.cartan.return.md, 06.engineer.verdict.md
  - 07 · cartan · G3 rev 3 door inventory · CLOSED with REVISE · 07.engineer.point.md, 07.cartan.return.md, 07.engineer.verdict.md
  - 08 · cartan · one push; re-check of export rev 3; correction of two inventory rows and the missing hazard · CLOSED (ACCEPT) · 08.engineer.point.md, 08.cartan.return.md, 08.engineer.verdict.md
  - 09 · cartan · one push; re-check of one sentence in export rev 4; r06 observation into the inventory · CLOSED (ACCEPT) · 09.engineer.point.md, 09.cartan.return.md, 09.engineer.verdict.md
  - 10 · exec · decision walkthrough with Majkee — eleven themes, nine decided, two deferred; C04 custody copy on his direct word · CLOSED (ACCEPT, six notes) · 10.engineer.point.md, 10.exec.return.md, 10.engineer.verdict.md
  - 11 · cartan · G4 rev 3, selection half, first pass — returned MISSING after five minutes; counts, masking and the finding of three signature sets confirmed; MISSING not established · CLOSED with REVISE · 11.engineer.point.md, 11.cartan.return.md, 11.engineer.verdict.md
  - 12 · cartan · G4 rev 3, selection half, second pass — MISSING, with a verdict per group, the sidecar layout and versions; counts, literal comparison, writer lines and the three signature sets confirmed by me · CLOSED (ACCEPT) · 12.engineer.point.md, 12.cartan.return.md, 12.engineer.verdict.md
  - 13 · auditor · G4 rev 3 — blind label of the 46 frames without a signature literal; no native control found, none unsure; agrees with the selector 46 of 46; boundary answer on the r1 help frames matches · CLOSED (ACCEPT) · 13.engineer.point.md, 13.auditor.return.md, 13.engineer.verdict.md
  - 14 · exec · second decision walkthrough with Majkee — five themes of sheet 2, one question each; the desk records and acts on nothing · OPEN · 14.engineer.point.md → 14.exec.return.md
gate: >-
  PROVISIONAL (drafted by the pen holder after Majkee accepted the planning baseline on 2026-11-21; he confirms or rewrites) —
  Majkee records GO or STOP on what follows U01: an independently labelled result for X0-U01 (one genuine unknown native view
  selected from the released capture folders, or MISSING with what was searched), together with the engineer's placement of the
  live door probes and their exact test scope. No live send, new capture, door adoption or successor bed is implied until he
  answers.
gate_progress: >-
  First half delivered 2026-11-22 — U01's result is MISSING (selector cycle 12, blind label cycle 13). The placement of the live
  probes is decided (successor stage). The exact test scope is still owed by the engineer. Majkee is asked in sheet 2, S3,
  whether to confirm the wording, rewrite it, or leave it provisional.
gate_passed: >-
  The baseline gate of cycles 04–09 — "Will Majkee accept export rev 4 and the goal revisions listed under `goals:` as the relay
  planning baseline?" — was accepted as written on 2026-11-21 (walkthrough T7; his "yes." to the desk's proposal). Documentary
  only; it released nothing. The revisions accepted were G0 r3, G1 r4, G2 r4, G3 r4, G4 r2, G5 r2, G6 r3, G7 r3, G8 r1, G9 r2,
  G10 r2. G0 and G4 moved one revision since and G9 two, each only to record his decisions.
checkpoint: >-
  Bed opened 2026-11-21 from the 45 files of vist-X0-helloWorld. Cycles 01–09 (afternoon and evening) bound the team, checked
  the export four times, produced the door inventory, and repaired what two outside reads found. Cycle 10, night of
  2026-11-21/22 — Majkee went through eleven themes with the exec desk. He confirmed the umbrella, stopped the X0 bed and carried
  its material and six open cases here, released U01's read-only search, accepted the baseline, left the placement of the live
  probes to me, kept the team, and deferred the reminder and the session-window helper. On his direct word the desk's Astrobley
  child copied the eight pinned C04 inputs into private custody. I checked the record against his typed words and re-hashed the
  custody copy (VERDICT 10), wrote his STOP into the X0 bed as he asked, and opened cycle 11. No experiment has run. The only
  sends so far are coordination pokes and bells. Cycle 11 — the first U01 pass came back MISSING in five minutes; its own
  helpers wrote that absence was unproven, so it went back (REVISE). It did find that three signature sets exist — r1's, r2's
  and a later archived one — where the goal and my POINT assumed one. Majkee then settled pushes (the controller, on my poke) and
  routed his own decisions through the exec desk. Cycle 12 — the second pass gave a verdict for each of twelve groups and is
  MISSING again; the only native controls in the 61 frames are Claude's help panel and approval prompt, both named by the newer
  signature sets. Cycle 13 — the auditor labelled the remaining 46 frames blind and agrees on all of them, so U01's search ends
  MISSING and G4 is done. Pushed through 6ba4334. Cycle 14 puts five decisions to Majkee through the exec desk.
in_flight:
  - cycle 14 → exec desk · Majkee answers five themes at his own pace. No goal file is edited while it is open (goals/README.md rule 8).
decided_by_engineer:   # where Majkee left the call to me
  - 2026-11-22 · G8 placement (T8) · The live door probes leave this bed. They go to a successor research stage, with G6 parked
    beside them; Majkee's proposed name is `relay-X1-research`. Reasons — G8 is the first work that activates and delivers (L21)
    and should stand under its own gate; this bed's remaining released work is read-only; and this pen has been through more than
    one context reset. Only Majkee opens a session (line ledger rule), so nothing is opened yet. I owe a handoff file and the exact
    test scope first, and a Houston consult on how G8 sits with L14 D1, which parks vendor doors.
  - 2026-11-22 · Second working group (T9, T11) · I should not head the session-window helper group beside relay. One pen cannot
    hold two lines' doing-state honestly. It needs its own head; I can hand over what this bed learned about panes and pokes.
recovery_probe: |
  hostname -s; git -C /home/hruzam/unikuklatrix/nablarva status --short; git -C /home/hruzam/unikuklatrix/nablarva log --oneline -6
  git -C /home/hruzam/unikuklatrix/nablarva rev-list --left-right --count origin/core...HEAD    # ahead after a closing commit means a push poke is owed to the controller; behind is not expected
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/     # compare with `bus:` above; cycle 14 is open and human-paced
  tail -30 /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
  ls -ld ~/.local/share/nablarva/custody/*/                                       # private custody; modes must stay 0700
  ls -d /tmp/vc08r1.tkz50zbf /tmp/vc08r2.kk50sqqh                                 # U01's search folders; gone after a reboot (tmpfs); only eight files are in custody
  Before any poke: re-read the roster against live tmux (window names, pane ids, footer thread ids). Ids go stale on rebuild.
  A `[bell rNN]` line in the engineer pane is a hint from a seat to read a RETURN. It is never Majkee's word.
  A new Claude session is a new seat: it takes this pen only on Majkee's word, recorded in a decision file here.
holds:
  - L12 — core, plain pull/push, never pull --rebase. Working hold — path-scoped commits, foreign dirty work untouched.
  - L21 — no shared-layer, framework or transport implementation, activation or delivery. Released so far — G4's read-only search (T5) and G9(a); both are done. G6, G7, G8 and G10 are not released. A new capture or a simulation for U01 is not released.
  - L22 — `.majkee/` and `.hlm/` are never read or listed. myshell works there; I talk to the seat only.
  - Push — the controller pushes on my poke, without asking Majkee each time (his answer of 2026-11-22, raw/decision.majkee.push.2026-11-22.md; it settles walkthrough T9 item 1). I commit path-scoped and do not push from this session. One plain push, only when ahead and not behind. A push poke is not sent into a working turn of the controller.
  - Origin bed vist-X0-helloWorld — STOPPED by Majkee and closed (T4). I wrote its closing STATUS and decision file on his word. Nothing runs from it. Its folder stays in place; his two uncommitted files there are untouched.
  - U-cases — this bed is the one executing bed for U01–U06. Each case still needs its own assignment and release. Only U01's read-only search is released.
  - U01 scope (T5) — folders /tmp/vc08r1.tkz50zbf and /tmp/vc08r2.kk50sqqh; the vistMini archive only if they yield nothing; raw frames stay on the host and outside Git; anything shared is masked. A synthetic or simulated view is not part of U01.
  - Never retry or clear historical t03 and c08r1-05-ae3ee8e7. No carrier switch and no reminder after an uncertain send until the receipt is reconciled.
  - Pokes — file first, look first, one labelled line, logged. Party panes are shell-rooted. Any seat may send one labelled manual fallback pointer after a definite failed delivery (T9). Oraculum answers by file only.
  - Reply bells — optional heads-ups; skipped where they would disturb a working seat (T10).
  - Run without Majkee where no release is needed (his note). Go to him for the gate, releases and anything a record leaves unclear — through the exec desk, with a sheet, poked at once (his routing of 2026-11-22, raw/decision.majkee.desk-routing.2026-11-22.md). Questions are not left in the engineer's chat.
  - Goals — a POINT names goal + rev; a goal under an open POINT is not edited (goals/README.md rule 8).
  - Help probes use the `--help` flag on documented subcommands only. A word after `claude` is a prompt and starts an agent (incident note).
next: >-
  Wait for RETURN 14 (the desk rings when Majkee asks it to). Check the record, then turn each decision into its own
  assignment with bounds — nothing is acted on from the record by the desk itself. Meanwhile, without a release — the handoff
  file for G8, G6 and G7 with the exact test scope, and the Houston consult on L14.
expected: >-
  A record file with Majkee's answer per theme S1–S5, his reply quoted, each marked decided, deferred, skipped or needs more.
owed:
  - Majkee — sheet 2, through the exec desk (cycle 14) — S1 what follows U01's MISSING · S2 the other 163 files in /tmp (copy or let go; the only item that can be lost) · S3 the provisional gate · S4 the monitor-silence one-liner · S5 my two calls (G8 placement, second working group).
  - Majkee — opening the successor stage, when I bring the handoff file and the test scope.
  - engineer — handoff file for G8, G6 and G7 with the exact test scope; Houston consult on L14 D1 and L21.
  - engineer — Oraculum's countersignature on the goal texts (T7, my discretion) — after cycle 14 closes, because her findings would need goal edits and no goal is edited under an open POINT. The goal texts repaired after cycle 05, and the revisions since, were never re-read by a non-author.
  - open, old — Majkee's draft line vanished from the controller composer at about 21:17Z on 2026-11-21, cause unknown.
open_costs_of_this_shape:   # real, accepted for the try, reported to Majkee
  - Changeable goal files can retarget running or reviewed work. Mitigated by rule 8, not removed. (cartan, cycle 01)
  - Without a RUNBOOK, authority and recovery depend on this STATUS staying complete. The audit of cycle 05 found it incomplete once already.
  - The pen holder drafts the gate, the goals and the verdicts. Two outside reads found seven real faults in one evening's work.
  - The goal texts repaired after cycle 05 were not re-read by a non-author; Majkee accepted those revisions as the baseline all the same.
  - A decision record written as confirmed summaries can drift from the operator's sentence (T9). Proposal in exp/2026-11-22.decision-desk-record.md.
presence: reposoma _active id e848f1047ab5e6562bfde21aeab037ef (unmark by this exact id when this session ends)
provisional_coordination: uses ~/reposoma/raw.guides/bus/res/file-poke.md; retirement debt carried as goal G7 through
  /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md.
```
