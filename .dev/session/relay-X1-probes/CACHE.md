---
kind: session cache for the lead of relay-X1-probes — uncanonical; pointers and findings only. STATUS.md and RUNBOOK.md win on conflict.
by: myShell (claude a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66, home) · 2026-11-22 ~06:20 CET
authority: Majkee 2026-11-22, typed in the myShell session — a cheaper agent checks Trajectory's transcript for orphans; the result is
  "collected synthetized and add as `CACHE`.md in new successing session with `*-X1-*` assignation"
method: Transcript of the predecessor session (claude d1ca16e9-073e-46d9-ba7d-26a816c38a67, snapshot 2026-11-22T04:55Z, last entry 04:35Z)
  flattened by script to operator words, replies and tool-call lines; read whole by a `field` subagent; every candidate checked
  against this bed, relay-X0-carryover, the ledgers and the cold-start card. myShell re-checked the items below marked "re-checked".
state: this file is untracked — the bed has no pen yet. The lead commits it, edits it or deletes it.
---

# CACHE · relay-X1-probes

What the predecessor's session knew that the RUNBOOK, STATUS, handoff and cold-start card do not say. `L<n>` = line in the raw
transcript `~/.claude/projects/-home-hruzam-ia-sync/d1ca16e9-073e-46d9-ba7d-26a816c38a67.jsonl`.

## Open — nobody holds these

> Correction by myShell, 2026-11-22 ~15:00 CET: two items below were solved after this file was written and are no longer open.
> `flight` now has `maxTurns: 100` (`~/.claude/agents/flight.md`), and the RUNBOOK guide no longer says "prune" — session close is
> "retire" (reposoma d906652, 06:29 CET). The handoff item was taken by the lead as cycle 04. Checked by the lead in `_bus/03.lead.verdict.md`.

- [ ] **The handoff's last edits were read by nobody but their author.** `../relay-X0-carryover/raw/handoff.successor-stage.2026-11-22.md`
  is draft 4 and is this bed's starting document. Oraculum's cycle-18 read was of draft 3; she asked for three edits and never saw the
  result. Majkee's H2–H6 answers were also written in by the author alone. The predecessor said so to Majkee (L4213, 02:37Z: "read by
  nobody but me"), but no file in this bed carries it (re-checked). Suggested first cycle: one non-author read of draft 4 against
  cycle 18's three points (`../relay-X0-carryover/_bus/18.*`) before any release-request sheet is written.
- [ ] **`flight` carries `maxTurns: 30`.** The card recommends the `flight` build. `~/.claude/agents/flight.md` line 15 has `maxTurns: 30`
  and line 13 `model: claude-sonnet-4-6` (re-checked). Nobody verified whether the turn limit applies to an interactive main session.
  The warning exists only in `raw/decision.majkee.successor-seat.2026-11-22.md` §2 — not in the card, RUNBOOK or STATUS. If a long run
  stops at a fixed turn count, look there first; the model is Majkee's to set at launch.
- [ ] **RUNBOOK guide still says "prune the directory".** `~/reposoma/raw.guides/runbook/GUIDE.md` line 217 (re-checked). Majkee, L4559:
  "pruning was mistake, i am trying to not do them again." Recorded in `raw/decision.majkee.successor-seat.2026-11-22.md` §1 as his to
  change; no task exists for it. Until it changes, a seat following the guide at gate closure would prune. Owner: Majkee.
- [ ] **Original capture folders still sit in `/tmp`.** `/tmp/vc08r1.tkz50zbf` and `/tmp/vc08r2.kk50sqqh` exist (re-checked 2026-11-22).
  No file says whether they are kept or deleted; a reboot removes them. Nothing is at risk — full copies are in custody. Owner: Majkee.
- [ ] **Context table at hand-over was spoken, not filed.** At about 04:35Z the predecessor told Majkee: auditor 82%, exec desk 67%,
  Oraculum 57% (about three more reads), controller 40%. Only the controller advice is on disk (`raw/decision.majkee.successor-seat.2026-11-22.md` §2:
  replace it before any Codex-origin row or crawling job). The numbers are stale by now — read the pane footers again before assigning.

## Changed since the handoff was written

- **Custody now has a second copy, on office.** STATUS `private_evidence` and the relay ledger say "on home". On 2026-11-22T04:56Z myShell
  copied `~/.local/share/nablarva/custody/` to the same path on office (`hruzam-120922`) on Majkee's word ("to same place on office via
  tailnet/SSH"). 189 files, 426,706 bytes, SHA-256 identical per file on both hosts, folders 0700, files 0600. Home originals are kept.
  The ledger's custody entries and STATUS do not say this yet — the lead's to record.
- **Window `lead` exists**, index 6, pane `%70`, a bare shell at 2026-11-22 ~06:15 CET (`raw/return.exec.window-lead.2026-11-22.md`).
- **Office has not pulled.** Its next pull brings the closing STATUS of `vist-X0-helloWorld`; unpushed office work there is resolved by
  hand, never by rebase (L12). Majkee: this goes through the `controller` session.

## Worth carrying (lessons with a source on disk, easy to miss)

- **Give child seats fact-gathering, not verdicts.** Asked for a verdict, two of three helpers hedged; asked to collect facts into their
  own files with the parent judging, the table could be checked · `raw/runbook-input.spawning-and-seats.trajectory.2026-11-22.md`.
- **Oraculum is strongest as the opposing reader of a document**, not as a senior-dev partner; she was mis-assigned twice ·
  same file, and `raw/runbook-input.decision-desk.exec.2026-11-22.md`.
- **Quote Majkee's own reply under every confirmed summary** (the exec desk's rule R1). It made fifteen of fifteen quoted lines
  checkable in one pass · `raw/runbook-input.decision-desk.exec.2026-11-22.md`.
- **An uncertain send stays uncertain.** One look-first paste into a Claude pane (r06) was staged, got Enter with exit 0, and did not
  submit; a second Enter did not submit it either. Cause unknown. Nothing is repeated and no door is switched until the receipt is
  reconciled from the file or the pane · `../relay-X0-carryover/raw/pokes.log.md`, cycles 06 and 09.
- **The predecessor did almost everything alone** and names that as a cost: stale sentences were found only by outside readers.
  Majkee wants the lead to delegate cheap work · `raw/decision.majkee.successor-seat.2026-11-22.md` §2.

## Coverage and limits

- Read whole: the flattened transcript (54 operator messages, 91 replies, 413 tool-call lines, 7 tool errors). Tool results and the
  model's private reasoning are not in it. Bus files 01–19 and goals G0–G10 were not read one by one; their STATUS summaries were used.
- The predecessor session kept working after the snapshot (it is on call in window `engineer`). Anything it did after 04:55Z is not covered.
- Not verified from home: office's working tree; whether the stray Claude transcript named in
  `../relay-X0-carryover/raw/incident.stray-claude-session.2026-11-21.md` is still present.
- The continuity note `raw/note.to-myshell.continuity.trajectory.2026-11-22.md` lists seven further ownerless items; they are not repeated here.
