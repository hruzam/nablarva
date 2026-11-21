# STATUS: relay-X0-carryover

```yaml
updated: 2026-11-21 20:15 CET
writer: engineer (trajectory · claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) · sole pen of this bed
host: home · hruzam
worktree: /home/hruzam/unikuklatrix/nablarva · core · upstream origin/core. Foreign uncommitted work present and left alone —
  vist-X0-helloWorld/RUNBOOK.md (Majkee's goal edit), vist-X0-helloWorld/majkee-personal-notes.md (his).
pen: engineer since 2026-11-21 (Majkee, raw/decision.majkee.open-bed.2026-11-21.md). Co-thinker cartan (codex 01a1ff5e…), no pen.
shape: No RUNBOOK. Goals are small files in goals/ (provisional, uncanonical try — Majkee D3.5). This STATUS is the only doing-state
  and the only entry point; it names every other file (goals/README.md rule 9).
files:
  decision: raw/decision.majkee.open-bed.2026-11-21.md      # Majkee's words that opened the bed
  export: raw/export.vist-x0.engineer.2026-11-21.md         # rev 2, checked once by a non-author
  roster: raw/roster.2026-11-21.md                          # seats, doors, roles; re-read against live tmux before any poke
  pokes: raw/pokes.log.md                                   # every poke sent, append-only
  goals: goals/README.md                                    # rules + index G0–G9
  bus: _bus/                                                # cycle 01 (cartan check) and 02 (myshell) — both closed
  line_ledger: ../relay-X.ledger.md
  card: ~/reposoma/_cold-start/card/CS.relay-X0-carryover.2026-11-21.md   # clean-table entry; a pointer, not a second state
gate: >-
  PROVISIONAL (drafted by the pen holder; Majkee confirms or rewrites) — Majkee accepts the non-author-checked carry-over
  export and the first goal set as the clean-table start of relay work. Accepting it runs no goal that names a release.
checkpoint: >-
  Bed opened 2026-11-21. All 45 files of vist-X0-helloWorld read; nothing there moved or changed. Cycle 01 closed — cartan's
  non-author check (43 confirmed, 7 refuted, 7 missing-source) accepted, export repaired once to rev 2, goals revised (G3 made
  read-only, G8 and G9 added); the verdict pins every goal rev by sha256. Cycle 02 closed — myshell answered, ledger row added
  and committed with her merge. No experiment ran. The only sends were two coordination pokes (raw/pokes.log.md).
goals_done: G2 export-verified
goals_running: >-
  G1 party-binding — engineer, cartan, myshell bound and confirmed; oraculum not engaged, so not bound.
  G9 custody-and-handoff — part (b): card written, bed committed and pushed; presence stays marked until this session ends.
  Part (a) waits for Majkee.
in_flight: none
recovery_probe: |
  hostname -s; git -C /home/hruzam/unikuklatrix/nablarva status --short; git -C /home/hruzam/unikuklatrix/nablarva log --oneline -5
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/     # every POINT must have a RETURN and a VERDICT
  tail -20 /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
  ls -d /tmp/vc08r1.tkz50zbf /tmp/vc08r2.kk50sqqh                                 # C04 inputs; gone after a reboot (tmpfs)
  Before any poke: re-read the roster against live tmux (window names, pane ids, footer thread ids). Ids go stale on rebuild.
  A new Claude session is a new seat: it takes this pen only on Majkee's word, recorded in a decision file here.
holds:
  - L12 — core, plain pull/push, never pull --rebase. Working hold — path-scoped commits, foreign dirty work untouched.
  - L21 — no shared-layer, framework or transport implementation, activation or delivery. G4, G6, G7, G8 and G9(a) each need Majkee first.
  - L22 — `.majkee/` and `.hlm/` are never read. myshell works there; I talk to the seat only.
  - Origin bed vist-X0-helloWorld — read-only from here; its gate is open and its pen is elsewhere (office thread 01a1d582…).
  - No U-case (U01–U06) runs here until Majkee accepts the X0 packet or explicitly carries that case here.
  - Never retry or clear historical t03 and c08r1-05-ae3ee8e7. No carrier switch after an uncertain send.
  - Pokes — file first, look first, one labelled line, logged. Party panes are shell-rooted. cartan cannot reach tmux; he answers by file only.
  - Goals — a POINT names goal + rev; a goal under an open POINT is not edited (goals/README.md rule 8).
  - Push rarely (Majkee D3.6) — local commits as needed; push at hand-over or real need.
next: >-
  Majkee reads the gate text and the goal index and says his word. The first work that needs no release is G3 (read-only door
  inventory). The first that needs one is G9(a) custody, then G4.
expected: >-
  A confirmed or rewritten gate, the custody decision on disk, and either a release for G4 or a clear "not yet".
owed:
  - Majkee — confirm or rewrite the gate.
  - Majkee — G9(a), what happens to the /tmp C04 inputs (copy host-local, or let go).
  - Majkee — one line on what "controller job" means for Cartan beyond co-thinking (roster, open label).
  - Majkee — who records his ACCEPT / REVISE / STOP on the X0 packet; its pen sits on office and no seat on home holds it.
  - Majkee — releases per goal (G4, G6, G7, G8) when he wants them; the four older decisions in export §10.
open_costs_of_this_shape:   # cartan's objections, cycle 01 — real, accepted for the try, reported to Majkee
  - Changeable goal files can retarget running or reviewed work. Mitigated by rule 8, not removed.
  - Without a RUNBOOK, authority and recovery depend on this STATUS staying complete.
  - X0's open gate leaves two beds able to propose the next U-case; only the hold above separates them.
presence: reposoma _active id e848f1047ab5e6562bfde21aeab037ef (unmark by this exact id when this session ends)
provisional_coordination: uses ~/reposoma/raw.guides/bus/res/file-poke.md; retirement debt carried as goal G7 through
  /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md.
```
