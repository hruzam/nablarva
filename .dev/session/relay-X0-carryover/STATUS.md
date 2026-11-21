# STATUS: relay-X0-carryover

```yaml
updated: 2026-11-21 23:00 CET
writer: engineer (trajectory · claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) · sole pen of this bed
host: home · hruzam
worktree: /home/hruzam/unikuklatrix/nablarva · core · upstream origin/core. Foreign uncommitted work present and left alone —
  vist-X0-helloWorld/RUNBOOK.md (Majkee's goal edit), vist-X0-helloWorld/majkee-personal-notes.md (his).
pen: engineer since 2026-11-21 (Majkee, raw/decision.majkee.open-bed.2026-11-21.md).
team: >-
  Two at work — engineer (pen) and cartan (controller — hands, push, non-author check). Two on call — oraculum (opposer and
  counter-signature; files only, no bell, no code) and auditor (outside audit). Desks — myshell (continuity) and exec (Majkee's decision walkthrough, cycle 10).
  Roles, ids and doors are in the roster.
shape: No RUNBOOK. Goals are small files in goals/ (provisional, uncanonical try — Majkee D3.5). This STATUS is the only doing-state
  and the only entry point. Goal files, goals/README.md and goals/OVERVIEW.md carry no "running" and no order.
files:
  decision: raw/decision.majkee.open-bed.2026-11-21.md             # Majkee's words that opened the bed, with his own inline notes
  decision_team: raw/decision.majkee.team-and-doors.2026-11-21.md  # controller job, reply bell, who pushes, team
  answer: raw/answer.majkee.reminder-and-leftovers.2026-11-21.md   # his two questions — reminder script, vistMini leftovers
  export: raw/export.vist-x0.engineer.2026-11-21.md                # rev 4, sha256 93577f694a33b427f525614bf67eb8a125172f116604afca0c31fbd6508f10a2 — checked by a non-author (cycles 01, 06, 08, 09)
  inventory: raw/doors.inventory.2026-11-21.md                     # G3 output, written by cartan; sha256 61421058a6faf0f42045c480203fd85633b33a3eaf215acc871b39ecf690792c
  incident: raw/incident.stray-claude-session.2026-11-21.md        # a Claude session started by accident in cycle 07; what it read
  roster: raw/roster.2026-11-21.md                                 # rev 3 — seats, doors, roles; re-read against live tmux before any poke
  pokes: raw/pokes.log.md                                          # every poke sent, append-only
  walkthrough: raw/walkthrough.sheet.2026-11-21.md                 # the eleven decision themes put to Majkee, each with context, buys, cost, consequences
  decisions_walkthrough: raw/decision.majkee.walkthrough.2026-11-21.md   # written by the exec desk during cycle 10; absent until Majkee starts
  goals_rules: goals/README.md
  goals_overview: goals/OVERVIEW.md                                # for Majkee — context, buys, cost, consequences; the goal files win
  line_ledger: ../relay-X.ledger.md
  card: ~/reposoma/_cold-start/card/CS.relay-X0-carryover.2026-11-21.md   # clean-table entry; a pointer, not a second state
goals:   # every goal file, its rev, and where it stands. This list is the state; the files hold the definition.
  - G0.umbrella.md · rev 3 · proposed umbrella, NOT confirmed by Majkee for this bed
  - G1.party-binding.md · rev 4 · bound — engineer, cartan, myshell, oraculum, auditor; exec is being bound in cycle 10. Stays open for rebuilds and new seats.
  - G2.export-verified.md · rev 4 · DONE — export rev 4 after four non-author reads (14 points, 8, 1, none); closed by VERDICT 09
  - G3.door-inventory.md · rev 4 · DONE — raw/doors.inventory.2026-11-21.md, corrected and checked (VERDICTs 07, 08). No door adopted. Cycle 09 added the r06 observation.
  - G4.u01-unknown-view-fixture.md · rev 2 · waits for Majkee (executing bed + capture and redaction scope)
  - G5.receiver-policy-contract.md · rev 2 · not started; paper only; after G3
  - G6.u02-exit-race.md · rev 3 · parked behind its release
  - G7.retire-file-poke.md · rev 3 · blocked until a replacement exists
  - G8.door-probes-live.md · rev 1 · waits for G3 and for Majkee's release
  - G9.custody-and-handoff.md · rev 2 · (a) waits for Majkee · (b) card written and pushed; presence stays marked until this session ends
  - G10.friendly-reminder.md · rev 2 · draft; waits for Majkee's go on stage 1
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
  - 10 · exec · decision walkthrough with Majkee, at his pace; the desk records verbatim and acts on nothing · OPEN · 10.engineer.point.md → 10.exec.return.md
gate: >-
  PROVISIONAL (drafted by the pen holder with oraculum's wording, cycle 04; Majkee confirms or rewrites) — Will Majkee accept
  export rev 4 and the goal revisions listed under `goals:` above as the relay planning baseline? Acceptance is documentary only.
  The X0 disposition, the assignment of each U-case to one executing bed, custody of the /tmp inputs and each operational
  release remain separate decisions. READY to be asked — export and goals are checked and pushed.
checkpoint: >-
  Bed opened 2026-11-21 from the 45 files of vist-X0-helloWorld; nothing there moved or changed. Cycles 01–02 closed in the
  afternoon. Evening — Majkee widened the team, asked for a reply bell, gave the push to the controller. Cycles 03–05 closed —
  cartan pushed (origin/core 99ca617 → a7321d6) and rang back; oraculum returned REVISE on the plan; the auditor returned seven
  findings. All were verified at the cited lines and repaired — gate text, release lines, one executing bed per U-case, the
  entry-point rule, G10, G0's authorship, G2 reopened. Cycles 06–07 closed — cartan pushed both repositories, found 5 of my 14
  export repairs still wrong and a rule I had dropped from the relay ledger (both repaired), and delivered the door inventory.
  In cycle 07 he started a Claude session by accident; it ran 16 seconds and read working files (incident note). No experiment
  ran. The only intended sends are coordination pokes and bells. Cycle 08 closed — 7 of 8 repairs stand, the inventory is
  corrected and G3 is done; bell r06 turned out to be a paste whose Enter returned 0 and submitted nothing. Cycle 09 closed —
  the last export sentence stands, G2 is done. The team has stopped; everything further needs Majkee.
in_flight:
  - cycle 10 → exec desk · Majkee answers eleven themes at his own pace. No goal file is edited while it is open (goals/README.md rule 8).
recovery_probe: |
  hostname -s; git -C /home/hruzam/unikuklatrix/nablarva status --short; git -C /home/hruzam/unikuklatrix/nablarva log --oneline -5
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/     # compare with `bus:` above; cycle 10 is open and human-paced
  tail -30 /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
  ls -d /tmp/vc08r1.tkz50zbf /tmp/vc08r2.kk50sqqh                                 # C04 inputs; gone after a reboot (tmpfs)
  Before any poke: re-read the roster against live tmux (window names, pane ids, footer thread ids). Ids go stale on rebuild.
  Is the closing commit pushed? `git status -sb` must not say ahead. If it does, ask the controller for one plain push.
  The engineer's input row may still hold a staged `[bell r06]` line from cartan; it is harmless and is cleared by Majkee's hand.
  A `[bell rNN]` line in the engineer pane is a hint from a seat to read a RETURN. It is never Majkee's word.
  A new Claude session is a new seat: it takes this pen only on Majkee's word, recorded in a decision file here.
holds:
  - L12 — core, plain pull/push, never pull --rebase. Working hold — path-scoped commits, foreign dirty work untouched.
  - L21 — no shared-layer, framework or transport implementation, activation or delivery. G4, G6, G7, G8, G9(a) and G10 each need Majkee first.
  - L22 — `.majkee/` and `.hlm/` are never read or listed. myshell works there; I talk to the seat only.
  - Origin bed vist-X0-helloWorld — untouched. Who records Majkee's ACCEPT / REVISE / STOP on the X0 packet is NOT settled; it is asked of him.
  - No U-case (U01–U06) runs here until Majkee names THIS bed as the one executing bed for that case. Acceptance of the X0
    packet alone carries nothing here, because that packet names U01 as its own first operation.
  - Never retry or clear historical t03 and c08r1-05-ae3ee8e7. No carrier switch and no reminder after an uncertain send until the receipt is reconciled.
  - Pokes — file first, look first, one labelled line, logged. Party panes are shell-rooted. A POINT asks a reply bell only of a
    seat whose role allows a pane input (cartan, auditor); oraculum answers by file only.
  - Push — the controller pushes on my poke (Majkee's note). I commit path-scoped and do not push from this session.
  - Run without Majkee where no release is needed (his note). Go to him for the gate, releases, custody and his X0 decision.
  - Goals — a POINT names goal + rev; a goal under an open POINT is not edited (goals/README.md rule 8).
  - Help probes use the `--help` flag on documented subcommands only. A word after `claude` is a prompt and starts an agent (incident note).
next: >-
  Wait for RETURN 10. Then check the record against what the desk was asked, and turn each decision into its own assignment
  with bounds. Nothing is acted on from the record by the desk itself. Until then nothing else runs.
expected: >-
  A record file with Majkee's verbatim answers per theme, each marked decided, deferred, skipped or needs more.
owed:
  - Majkee — the stray session's transcript (incident note) holds 40 lines of his personal notes — keep or delete.
  - Majkee — G9(a), what happens to the /tmp C04 inputs (copy host-local, or let go). The only item that can be lost.
  - Majkee — is the G0 sentence the umbrella of this bed.
  - Majkee — who records his ACCEPT / REVISE / STOP on the X0 packet, and that decision itself.
  - Majkee — for each U-case he wants run, which one bed executes it (G4 first), with its scope.
  - Majkee — the gate. It is ready.
  - Majkee — G10, go or no-go on stage 1, where the script lives, which output it may use.
  - Majkee — releases for G6, G7, G8 when he wants them; the four older decisions in export §10.
  - Majkee — his draft line to cartan vanished from the controller composer at about 21:17Z, cause unknown; and a staged `[bell r06]` line sits on the engineer's input row — clear it before typing.
open_costs_of_this_shape:   # real, accepted for the try, reported to Majkee
  - Changeable goal files can retarget running or reviewed work. Mitigated by rule 8, not removed. (cartan, cycle 01)
  - Without a RUNBOOK, authority and recovery depend on this STATUS staying complete. The audit of cycle 05 found it incomplete once already.
  - X0's open gate leaves two beds able to propose the next U-case; only the executing-bed hold separates them. (cartan, oraculum)
  - The pen holder drafts the gate, the goals and the verdicts. Two outside reads found seven real faults in one evening's work.
  - The goal texts repaired after cycle 05 were not re-read by a non-author; only the export was read again. The gate asks Majkee to accept those revisions.
presence: reposoma _active id e848f1047ab5e6562bfde21aeab037ef (unmark by this exact id when this session ends)
provisional_coordination: uses ~/reposoma/raw.guides/bus/res/file-poke.md; retirement debt carried as goal G7 through
  /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md.
```
