---
kind: handoff from relay-X1-probes to the successor stage of the relay line
by: lead (flight · claude b155ba44-0c27-4b9c-85e1-8f74daad22d6) · 2026-11-26 · host home
status: DRAFT 3 — draft 1 was checked by the auditor, the seat of the other vendor — REVISE; all its points are taken here (_bus/30.auditor.return.md, _bus/30.lead.verdict.md), among them a fact new to the lead: one of the two unarrived messages arrived two days later. Section 4, the proposal for the successor, was added after that check began and has not been checked by a second seat. The auditor has not read this revision. Not yet accepted by Majkee.
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
| `packet.md` | A, B | A: `codex queue` into an idle codex sample — arrived, receipt matches. B: tmux paste then a separate Enter by an agent, the one L4 exception, spent — native turn, receipt matches; the nonce was visible at the paste, so the observer's blind interval ended there | `raw/decision.majkee.gate-2.2026-11-23.md` |
| `packet-2.md` | C1, C2 | a queued message asks to act outside the sandbox; no chooser was visible in the sampled frames of either try. C1: rejected by the session's effective policy. C2: a review status on the screen and the step carried out; who reviewed is inferred | `raw/decision.majkee.gate-3.2026-11-23.md` |
| `packet-3.md` | D1 | with approval `on-request` and reviewer `user`: a chooser for the human; the turn stayed open 7 minutes; the record carried no entry naming the wait; his persistent yes stored a user-level rule | `raw/decision.majkee.gate-4.2026-11-23.md` |
| `packet-4.md` | E1, E2, E3 | a denial ended the whole turn (twice); a message accepted while a chooser stood left no trace at the receiver; twice an accepted message was not seen to arrive within its watch, both at a session whose last turn had been aborted — a candidate reading, not a result; one of the two arrived two days later, see below | `raw/decision.majkee.gate-5.2026-11-23.md` |

Read each packet's own "does not show" before citing it. Private evidence: two folders under
`~/.local/share/nablarva/custody/` on home and office, pointed at from `.dev/session/relay-X.ledger.md` (Solved).

**Carrier arithmetic of the chooser samples, for whoever cites it:** five calls accepted with exit 0 and a message id;
three arrived, two were not seen to arrive within their watches. The carrier's answer did not differ between them.

**After the packets — one of the two arrived.** E3's second message (nonce `x1k-fe1e8c5f92`) arrived in the third
sample on 2026-11-25 at 23:18:05 UTC — 2 days, 2 hours and 5 minutes after the carrier accepted it, and just after a
turn made by hand in that session; payload and receipt match. Source: the auditor, `_bus/30.auditor.return.md`; its
private note `manual-check.md` with `SHA256SUMS` lies in
`~/.local/share/nablarva/custody/x1-chooser-2026-11-23/tracker-sample2-2026-11-26.rsztjnz1/` on home, and — that
folder's nine files being the ones the controller's second pass of 2026-11-26 added — on office. The lead did not order
that check and has not read the note. E2's first message is unresolved. How long the program keeps an accepted message
and what releases it remain unknown: one arrival after one manual turn is one observation. `packet-4.md` stays the
time-bounded record it is.

## 2. Open work that leaves this bed

| Item | State | Note for the successor |
|---|---|---|
| Lines 8 to 19 of the predecessor's release menu (`../relay-X0-carryover/raw/handoff.successor-stage.2026-11-22.md` §6): the `sample-claude` rows, the other senders, the U01 capture | never released — NOT RUN | the defects found in those lines are in `_bus/03.lead.verdict.md` (Carried) and `_bus/04.lead.verdict.md` (last row); settle them before any sheet asks those lines |
| U01 — one new real unknown-view capture | chosen in X0, not released here — NOT RUN | needs line 8 first |
| Cases X0-U01 … X0-U06 | belonged to this bed; not worked | belonging is not a release |
| G6 — the exit race (`../relay-X0-carryover/goals/G6.u02-exit-race.md`) | parked by Majkee | observation B is the only measurement at that seam; see `packet.md` |
| G5 — the paper receiver contract for U03–U06 (`../relay-X0-carryover/goals/G5.receiver-policy-contract.md`) | no work on it in this bed's record | paper work, no release needed to write it |
| G7 — retire the provisional file-poke (`../relay-X0-carryover/goals/G7.retire-file-poke.md`) | tracked debt, outside any gate so far | the file-poke itself rides on `codex queue` for codex seats: see the caution in §3 |
| Accepted messages that did not arrive within their watch: how long one is kept, and what releases it | open — one observation after the packets (§1): E3's second arrived two days later, just after a manual turn; E2's first is unresolved | message ids in `packet-4.md`, "Left behind"; both samples are closed |
| A second message while a chooser stands, answered with **approval** | open — not tried | separates "a chooser stood" from "the turn was aborted" in packet 4's observation 5 |
| What the stored allow rule does later; a chooser across interrupt and resume; "No" with a note typed; whether a chooser ends by itself | open — not tried | `packet-3.md` and `packet-4.md`, "does not show". The rule is in his file; no seat touches it |
| A vigilance test of the operator, unannounced | offered by him on 2026-11-23, declined for this bed | his to raise again; nothing unannounced was run |

## 3. What the successor should know before it pokes anyone

- **A message by `codex queue` can be accepted and arrive much later, or not be seen at all.** In the samples, of
  five accepted messages three arrived within seconds, one arrived two days later just after a manual turn, and one
  is unresolved (§1). The bed's own coordination pokes: 44 entries in `raw/pokes.log.md` and four in
  `raw/pokes.fork.log.md`, each with a documented outcome; by the auditor's reconciliation one early poke (p02) at
  first timed out without a RETURN. That is what was documented, not a delivery guarantee. A head pairs every poke
  with a finite watch on the RETURN file and does not read the carrier's exit code as delivery.
- **The session's process lessons** are in `.dev/observations/relay-X1-probes.flight.2026-11-26.md`. The successor's
  head reads it before authoring (runbook guide, observations_read).
- **Helpers built ad hoc** are listed once, with what each stands for:
  `.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md`.

## 4. The successor — proposed by the lead, nothing of it decided

**What L14 prescribes** (read on 2026-11-26: `../flag.md` L14 with the amendment of 2026-11-23;
`meshup/seam.cross-vendor-relay.2026-08-05/raw/decisions.relay.2026-09-30.md` D4 and D7;
`~/reposoma/raw.guides/runbook/res/research.md`):

- The next chapter is `relay-X2-research`, the big-scope research gate: one session that decides whether the relay
  program — a PTY impulse layer for session relay and its tracker, under D1 to D3 — should be built at all.
- It answers three checks, dated and sourced: **wheel** (does something existing cover it), **overengineering**
  (would a smaller composition of existing parts serve) and **vendor harness** (will the platforms ship it natively,
  and which native change would retire the build).
- It ends in one ranked verdict — **REINVENT, ADOPT or REFUSE** — with its recommendation on disk. `relay-X3-pty` and
  `relay-X4-tracker` open only after it.
- D7: two blind briefs to the other vendor line before the relay architecture is locked — one on research, one on
  architecture; each ends in a committed answer and a falsifier, never in consensus. D1, D2, D5 and D6 are his
  constraints to those briefs.

**The lead's proposal:**

| | Proposed | Why |
|---|---|---|
| Slug | `relay-X2-research` | the reserved name; X2 is free |
| Gate | *Majkee records GO or STOP on a recorded research VERDICT for the relay program — REINVENT, ADOPT or REFUSE, ranked, with its recommendation on disk — resting on a dated and sourced wheel check, overengineering check and vendor-harness check, with the blind research brief of L14 D7 returned beside it. The verdict locks no architecture and releases no build.* | the research guide's gate in this project's form; the last sentence keeps D7's second brief and the architecture lock outside |
| Evidence it may cite | the door inventory of X0; the four packets of X1; the helper inventory in `eSharp/raw/`; whatever sibling beds have qualified | cited as evidence, never as a verdict |
| Releases it needs | none to begin: reading, dated web research, one blind brief to the other vendor line. No session is started, nothing is sent into a sample | a research bed activates nothing |
| Team | the lead as its head; a dated-research seat for the three checks; the auditor as the checker of the verdict file; the controller's seat as second-vendor reader; the blind brief by a relay that carries no position; the exec desk for the gate | as he named the team on 2026-11-26 |

**Open points the lead cannot settle:**

1. **Who authors its RUNBOOK.** The predecessor's head wrote this bed's frame; the lead can do the same for X2 with
   the planning protocol, or he names a planning seat.
2. **Whether D7's research brief belongs inside X2** (proposed above) or before it.
3. **Overlap.** By their gate lines in `../pulse.md` — the lead has not read these beds — `terminal-workspace-X0-approaches`
   already gathers dated native and reuse alternatives for a shared terminal, and `termpanum-X1-source-qualification`
   and `nablarva-02-pipe-qualification` qualify sources and a native assignment path. The wheel check of X2 must
   start from what they hold, or it repeats them.
4. **The umbrella.** X0 and X1 carried his sentence about what the home trial can support. A research gate may want
   its own; none is proposed.

Until he has opened it, there is no successor bed.

## 5. Locks this touches

L4 (send-keys injection is a recorded death; the exception is spent) · L12 (core, plain pull and push), with path-scoped
commits by his word in `raw/decision.majkee.cache-and-commits.2026-11-22.md` · L14 D1, D2, D4, D7 · L20 (observations authorize nothing) · L21 (each activation and delivery its own
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
