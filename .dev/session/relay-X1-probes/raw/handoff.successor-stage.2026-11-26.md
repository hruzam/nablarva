---
kind: handoff from relay-X1-probes to the successor stage of the relay line
by: lead (flight · claude b155ba44-0c27-4b9c-85e1-8f74daad22d6) · 2026-11-26 · host home
status: DRAFT 1 — written at closure. Not yet checked by a second seat; not yet accepted by Majkee. Section 4 (the successor's gate) is deliberately empty until the lead has read L14's sources.
authority: Majkee, 2026-11-26 — raw/decision.majkee.close.2026-11-26.md
---

# Handoff from `relay-X1-probes` to the successor stage

## 0. What the successor is not

- **Not a continuation of the probes.** This bed's gate is met four times; its rows stand as "tried once". The
  successor does not rerun, extend or reinterpret them without its own release.
- **Not a qualification of `codex queue`.** By L14 D1 vendor doors are weather, parked. The four packets are
  observations of that weather. They qualify no door as a transport or as a replacement for the file-poke.
- **Not an exception to L4.** The one exception was spent in observation B.
- **Not released by this handoff.** Every activation and every send needs its own word (L21).

## 1. What this bed established — pointers, not copies

Four witnessed packets, each with Majkee's GO. Each row: nonce committed before the call, one call, an observer of the
other vendor that was not told the nonce and wrote its note before reading the sender's file.

| Packet | Rows | What was observed, in one line each | His word |
|---|---|---|---|
| `packet.md` | A, B | A: `codex queue` into an idle codex sample — arrived, receipt matches. B: tmux paste then Enter by an agent, the one L4 exception — spent | `raw/decision.majkee.gate-2.2026-11-23.md` |
| `packet-2.md` | C1, C2 | a queued message asks to act outside the sandbox: C1 refused by the session's policy without a visible chooser; C2 reviewed by the program itself, no chooser in the sampled frames | `raw/decision.majkee.gate-3.2026-11-23.md` |
| `packet-3.md` | D1 | with approval `on-request` and reviewer `user`: a chooser for the human; the turn stayed open 7 minutes; the record carried no entry naming the wait; his persistent yes stored a user-level rule | `raw/decision.majkee.gate-4.2026-11-23.md` |
| `packet-4.md` | E1, E2, E3 | a denial ended the whole turn (twice); a message accepted while a chooser stood left no trace at the receiver; twice an accepted message was not seen to arrive, both at a session whose last turn had been aborted — a candidate reading, not a result | `raw/decision.majkee.gate-5.2026-11-23.md` |

Read each packet's own "does not show" before citing it. Private evidence: two folders under
`~/.local/share/nablarva/custody/` on home and office, pointed at from `.dev/session/relay-X.ledger.md` (Solved).

**Carrier arithmetic of the chooser samples, for whoever cites it:** five calls accepted with exit 0 and a message id;
three arrived, two were not seen to arrive within their watches. The carrier's answer did not differ between them.

## 2. Open work that leaves this bed

| Item | State | Note for the successor |
|---|---|---|
| Lines 8 to 19 of the predecessor's release menu (`../relay-X0-carryover/raw/handoff.successor-stage.2026-11-22.md` §6): the `sample-claude` rows, the other senders, the U01 capture | never released — NOT RUN | the defects found in those lines are in `_bus/03.lead.verdict.md` (Carried) and `_bus/04.lead.verdict.md` (last row); settle them before any sheet asks those lines |
| U01 — one new real unknown-view capture | chosen in X0, not released here — NOT RUN | needs line 8 first |
| Cases X0-U01 … X0-U06 | belonged to this bed; not worked | belonging is not a release |
| G6 — the exit race (`../relay-X0-carryover/goals/G6.u02-exit-race.md`) | parked by Majkee | observation B is the only measurement at that seam; see `packet.md` |
| G5 — the paper receiver contract for U03–U06 | not started in this bed | paper work, no release needed to write it |
| G7 — retire the provisional file-poke (`../relay-X0-carryover/goals/G7.retire-file-poke.md`) | tracked debt, outside any gate so far | the file-poke itself rides on `codex queue` for codex seats: see the caution in §3 |
| Accepted and unarrived messages: lost or waiting; what releases one | open — nothing tried | two message ids are named in `packet-4.md`, "Left behind"; both samples are closed |
| A second message while a chooser stands, answered with **approval** | open — not tried | separates "a chooser stood" from "the turn was aborted" in packet 4's observation 5 |
| What the stored allow rule does later; a chooser across interrupt and resume; "No" with a note typed; whether a chooser ends by itself | open — not tried | `packet-3.md` and `packet-4.md`, "does not show". The rule is in his file; no seat touches it |
| A vigilance test of the operator, unannounced | offered by him on 2026-11-23, declined for this bed | his to raise again; nothing unannounced was run |

## 3. What the successor should know before it pokes anyone

- **A poke by `codex queue` can be accepted and not arrive.** In this bed every coordination poke to a seat was
  answered. In the samples, two accepted messages were not seen to arrive, both after the human had ended the
  session's last turn with `esc`. Candidate reading from two tries. A head that gets no RETURN from a seat the
  operator has just interrupted should suspect this first — and always pairs a poke with a finite watch on the RETURN
  file, never with trust in the carrier's exit code.
- **The session's process lessons** are in `.dev/observations/relay-X1-probes.flight.2026-11-26.md`. The successor's
  head reads it before authoring (runbook guide, observations_read).
- **Helpers built ad hoc** are listed once, with what each stands for:
  `.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md`.

## 4. The gate of the successor — to be proposed

Empty on purpose. L14 D4 names the next chapter `relay-X2-research` and calls it the verdict gate: research before
build, sweep → PTY research → tracker draft; D7 asks for a blind triangulation before the relay architecture is locked.
The lead reads those sources and brings Majkee one proposal — slug, gate sentence, umbrella, team, first release menu.
Until he has opened it, there is no successor bed.

## 5. Locks this touches

L4 (send-keys injection is a recorded death; the exception is spent) · L12 (core, plain pull and push, path-scoped
commits) · L14 D1, D2, D4, D7 · L20 (observations authorize nothing) · L21 (each activation and delivery its own
release) · L22 (operator vaults sealed).

## 6. Team at closure — Majkee, 2026-11-26

The lead (flight, window `lead`); the auditor (`%66`) and the controller's seat in `supervisor-relay` (`%59`) as the
second vendor; the exec desk (`%68`) for gavel loops. `seniorDev` and `myShell` are his for other work. Windows
`spare-codex` and `spare-claude` are free. `raw/decision.majkee.team-and-windows.2026-11-26.md`.

## 7. What stays behind

- The bed, tracked in Git, closed: its files are read by path. Deregistering it is a later word of his.
- Outside Git, on home: the sample folders, receipts, start scripts and instruction files under
  `~/.cache/nablarva/relay-x1-samples/`; the doorbell and the notifier under `~/.cache/nablarva/relay-x1-doorbell/`;
  the transcript reader under `~/.cache/nablarva/relay-x1-cache/`; the fork's originals under
  `~/.cache/nablarva/relay-x1-fork/`.
- A stored user-level allow rule for one `mkdir` prefix in `~/.codex/rules/default.rules` — his file.
- `CACHE.md`, `CACHE.exec.md`, `CACHE.lead.md` in the bed — untracked, his; never opened or staged by the lead.
- The original lead session and its continuation, idle; the transcript of the accidental Claude session of
  2026-11-22, kept.
