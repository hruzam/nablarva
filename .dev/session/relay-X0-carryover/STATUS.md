# STATUS: relay-X0-carryover

```yaml
updated: 2026-11-21 22:45 CET
writer: engineer (trajectory · claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) · sole pen of this bed
host: home · hruzam
worktree: /home/hruzam/unikuklatrix/nablarva · core · upstream origin/core. Foreign uncommitted work present and left alone —
  vist-X0-helloWorld/RUNBOOK.md (Majkee's goal edit), vist-X0-helloWorld/majkee-personal-notes.md (his).
pen: engineer since 2026-11-21 (Majkee, raw/decision.majkee.open-bed.2026-11-21.md).
team: >-
  Two at work — engineer (pen) and cartan (controller — hands, push, non-author check). Two on call — oraculum (opposer and
  counter-signature; files only, no bell, no code) and auditor (outside audit). Desk — myshell (continuity).
  Roles, ids and doors are in the roster.
shape: No RUNBOOK. Goals are small files in goals/ (provisional, uncanonical try — Majkee D3.5). This STATUS is the only doing-state
  and the only entry point. Goal files, goals/README.md and goals/OVERVIEW.md carry no "running" and no order.
files:
  decision: raw/decision.majkee.open-bed.2026-11-21.md             # Majkee's words that opened the bed, with his own inline notes
  decision_team: raw/decision.majkee.team-and-doors.2026-11-21.md  # controller job, reply bell, who pushes, team
  answer: raw/answer.majkee.reminder-and-leftovers.2026-11-21.md   # his two questions — reminder script, vistMini leftovers
  export: raw/export.vist-x0.engineer.2026-11-21.md                # rev 2, sha256 e7b9d043… — rev 1 was checked; my repair is being re-checked (cycle 06)
  roster: raw/roster.2026-11-21.md                                 # rev 3 — seats, doors, roles; re-read against live tmux before any poke
  pokes: raw/pokes.log.md                                          # every poke sent, append-only
  goals_rules: goals/README.md
  goals_overview: goals/OVERVIEW.md                                # for Majkee — context, buys, cost, consequences; the goal files win
  line_ledger: ../relay-X.ledger.md
  card: ~/reposoma/_cold-start/card/CS.relay-X0-carryover.2026-11-21.md   # clean-table entry; a pointer, not a second state
goals:   # every goal file, its rev, and where it stands. This list is the state; the files hold the definition.
  - G0.umbrella.md · rev 3 · proposed umbrella, NOT confirmed by Majkee for this bed
  - G1.party-binding.md · rev 4 · bound — engineer, cartan, myshell, oraculum, auditor. Stays open for rebuilds and new seats.
  - G2.export-verified.md · rev 3 · REOPENED — running under cycle 06 (re-check of my repairs in export rev 2)
  - G3.door-inventory.md · rev 3 · running under cycle 07 (cartan, read-only)
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
  - 06 · cartan · two pushes; re-check of export rev 2 repairs; check of the ledger merge · OPEN · 06.engineer.point.md → 06.cartan.return.md
  - 07 · cartan · G3 rev 3 door inventory → raw/doors.inventory.2026-11-21.md · OPEN · 07.engineer.point.md → 07.cartan.return.md
gate: >-
  PROVISIONAL (drafted by the pen holder with oraculum's wording, cycle 04; Majkee confirms or rewrites) — Will Majkee accept
  export rev 2 and the goal revisions listed under `goals:` above as the relay planning baseline? Acceptance is documentary only.
  The X0 disposition, the assignment of each U-case to one executing bed, custody of the /tmp inputs and each operational
  release remain separate decisions. Not ready to be asked until cycle 06 confirms my repairs in export rev 2.
checkpoint: >-
  Bed opened 2026-11-21 from the 45 files of vist-X0-helloWorld; nothing there moved or changed. Cycles 01–02 closed in the
  afternoon. Evening — Majkee widened the team, asked for a reply bell, gave the push to the controller. Cycles 03–05 closed —
  cartan pushed (origin/core 99ca617 → a7321d6) and rang back; oraculum returned REVISE on the plan; the auditor returned seven
  findings. All were verified at the cited lines and repaired — gate text, release lines, one executing bed per U-case, the
  entry-point rule, G10, G0's authorship, G2 reopened. No experiment ran. The only sends are coordination pokes and bells.
in_flight:
  - cycle 06 → cartan · includes ONE plain git push each of nablarva core and reposoma core, if only ahead
  - cycle 07 → cartan · read-only; queued behind 06 on the same thread
  - G2 and G3 are not edited while these are open (goals/README.md rule 8).
recovery_probe: |
  hostname -s; git -C /home/hruzam/unikuklatrix/nablarva status --short; git -C /home/hruzam/unikuklatrix/nablarva log --oneline -5
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/     # compare with `bus:` above; 06 and 07 are open
  tail -30 /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
  ls -d /tmp/vc08r1.tkz50zbf /tmp/vc08r2.kk50sqqh                                 # C04 inputs; gone after a reboot (tmpfs)
  Before any poke: re-read the roster against live tmux (window names, pane ids, footer thread ids). Ids go stale on rebuild.
  Were the pushes of cycle 06 made? Compare `git rev-parse origin/core` in both repositories with the RETURN before asking again.
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
next: >-
  Verify RETURN 06 and RETURN 07 against the files and write their VERDICTs. If cycle 06 confirms the repairs, G2 is done again
  and the gate can be put to Majkee. After G3 the team has no further work that needs no release, except G5 on paper.
expected: >-
  Two pushed refs, a verdict per repaired finding of the export, a yes or a list on the ledger merge, and one inventory file
  of door candidates with unknowns written as unknown.
owed:
  - Majkee — G9(a), what happens to the /tmp C04 inputs (copy host-local, or let go). The only item that can be lost.
  - Majkee — is the G0 sentence the umbrella of this bed.
  - Majkee — who records his ACCEPT / REVISE / STOP on the X0 packet, and that decision itself.
  - Majkee — for each U-case he wants run, which one bed executes it (G4 first), with its scope.
  - Majkee — the gate, once cycle 06 is closed.
  - Majkee — G10, go or no-go on stage 1, where the script lives, which output it may use.
  - Majkee — releases for G6, G7, G8 when he wants them; the four older decisions in export §10.
  - Majkee — his line to cartan sat unsent in the controller composer at 21:07Z.
open_costs_of_this_shape:   # real, accepted for the try, reported to Majkee
  - Changeable goal files can retarget running or reviewed work. Mitigated by rule 8, not removed. (cartan, cycle 01)
  - Without a RUNBOOK, authority and recovery depend on this STATUS staying complete. The audit of cycle 05 found it incomplete once already.
  - X0's open gate leaves two beds able to propose the next U-case; only the executing-bed hold separates them. (cartan, oraculum)
  - The pen holder drafts the gate, the goals and the verdicts. Two outside reads found seven real faults in one evening's work.
presence: reposoma _active id e848f1047ab5e6562bfde21aeab037ef (unmark by this exact id when this session ends)
provisional_coordination: uses ~/reposoma/raw.guides/bus/res/file-poke.md; retirement debt carried as goal G7 through
  /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md.
```
