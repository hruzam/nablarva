---
kind: research VERDICT of the L14 D4 gate — the relay program
by: lead (flight · claude 689d87d0-6d49-4c5c-ae33-7fe561e92ac8) · 2026-11-26 · home
status: VERDICT — the text of RUNBOOK step 5. Third version. Opposed once by the auditor (cycle 07, REVISE on DRAFT 2); what was taken and what was not is in `_bus/07.lead.verdict.md`. The auditor has not read this version; its check of step 6 is outstanding. Majkee has not read it as the verdict.
history: DRAFT 1 (04:12 UTC, never committed) said ADOPT and "no relay-X3-pty" — that repeated a rule struck on 2026-10-02 and was withdrawn. DRAFT 2 (commit d95f6d9) said ADOPT with a delta of three things to make; the auditor showed that the delta answered failures nobody had seen in routine use, and that it designed an architecture. This version ranks REFUSE first.
blind: no answer to this bed's send copy of the L14 D7 brief exists — the brief is not sent. Whether the brief of 2026-09-30 was ever sent or answered is recorded as unknown (`meshup/seam.cross-vendor-relay.2026-08-05/DESIGN.md`, line 31).
gate: Majkee records GO or STOP on this verdict. It locks no architecture, opens neither relay-X3-pty nor relay-X4-tracker, releases no build and qualifies no door.
judged: the relay program — a PTY impulse layer for relay between interactive CLI agent sessions, and a mechanical tracker of their states — under L14 D1, D2, D5 and D6 as given. The constraints are inputs and are not judged.
---

# Verdict

**REFUSE** — the program as scoped on 2026-09-30 does not open now. Ranked: 1. REFUSE · 2. ADOPT · 3. REINVENT.

The program was scoped when the operator carried messages between sessions by hand. Since 2026-11-19 a smaller
composition carries them: a file, a one-line pointer, a finite watch on the reply file. Both things the program was
to build already run inside it in a hand-made form — a look at the recipient before each pointer, and, from a Codex
seat to a Claude lead, one bracketed paste and a single Enter. No failure of that composition in routine use is on
record that a tracker or an impulse layer of our own would have prevented.

So: no tracker draft, no chapter for an impulse layer. What runs keeps running and is counted. The floor of D1 —
the lab, its tap — is not part of this refusal; it stands under its own gate.

- **Second, ADOPT:** if the falsifier is observed, the evidence already says what to take — states from the signals
  the vendors' programs emit themselves, never a classifier of screen content — and only for the state the observed
  failure names.
- **Last, REINVENT:** right only if a state that a decision needs is served by no emitted signal, no native status
  surface and not by the floor.

**The falsifier.** In routine use — not in samples that set a recipient up on purpose — the poke logs of this line
show, within any fifty consecutive pointers, more than two that the operator had to carry or repair himself because
the sender could not tell from files whether the pointer had arrived or what state the recipient was in. Then the
smaller composition does not serve the need, and ADOPT leads. The number is a proposal; it is his to set.

**What REFUSE costs, said once and plainly.** The composition that runs is provisional, and its carrier toward a
Codex seat is a vendor door that D1 parks. Refusing the program leaves that debt standing (§7). Paying it is a
decision of Majkee's, not a build.

# 1. What was judged, and with what

Evidence, in this bed's `raw/` unless a path says otherwise:

| Short name | File | What it is |
|---|---|---|
| W | `research.wheel-and-harness.epoch.2026-11-26.md` | the lead's research child, first pass, 50 rows |
| R | `research.wheel-and-harness.refresh.epoch.2026-11-26.md` | its second, narrow pass on six unverified points |
| A | `research.wheel-and-harness.auditor.2026-11-26.md` | the auditor's child on the other vendor's model, from the question alone, without the seed's leads and without sight of W — 20 rows |
| X | `facts.tmux-release-and-7501.lead.2026-11-26.md` | tmux's release list and two commits, read from the primary pages |
| L | `facts.local-claude-side.lead.2026-11-26.md` | help text and environment of the installed Claude Code 2.1.332 |
| C2, C6 | `../_bus/02.controller.return.md`, `../_bus/06.controller.return.md` | installed Codex 0.172.0 help text; the manual of the installed tmux 3.7c, quoted |
| D | `../../relay-X0-carryover/raw/doors.inventory.2026-11-21.md` | this line's paper inventory of doors |
| P | the four packets of `../../relay-X1-probes/` and its handoff of 2026-11-26 | rows tried once each; they qualify no door |
| K | `raw/pokes.log.md` of this bed; the predecessor's count in its handoff, §3 | every pointer sent, what the carrier answered, when the RETURN was seen |
| M1, M2 | `prior-evidence.map.md`, `prior-evidence.map-2.md` | where the earlier evidence lies; M1 carries three known errors, named in STATUS |
| O | `.dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md`, `vendor-events.catalogue.2026-10-02.md`, `.dev/research/termpanum-events/events-map.v0.2026-10-02.md` | the project's own research of October |
| G | `meshup/lab.observability-probes.2026-08-01/DESIGN.md`, line 14 | the record of the rule struck on 2026-10-02 |
| T | `../../termpanum-X0-source-contract/raw/source-contract.md` and `research-disposition.md` | the packet accepted on 2026-10-22 as input to this decision |
| Q | `../_bus/07.auditor.return.md` | the auditor's opposition to DRAFT 2 |

W and R say of themselves that pages were read through a summarising fetch, not raw bytes; A makes no such statement
about itself. W and R are one line of research; A is a second, made apart from it. Where they disagreed on tmux, the
primary pages were read again (X) and A held. The auditor's child sampled the citations of DRAFT 2 against the three
tables (Q); its corrections are taken below. Nothing in this bed was tested: no session was started, no door was
tried, no state was listed.

# 2. Wheel check — does something existing cover it?

**The tracker: yes, in two families, and they break in different ways.**

- *Emitted signals and records.* Published tools turn vendor hooks or notifications into status files or tmux
  indicators, each for part of the field: one for working and done, one from Codex's completion notification, one
  for Claude Code only (W rows 36 to 38). One reads the CLIs' own session files and says those formats are
  undocumented and may change (W row 35). One combines process identity, hooks, logs and terminal patterns over
  existing tmux sessions, last commit 2026-11-25 (A, ccmux — its README's claim).
- *The screen.* At least six published tools classify a session from pane content (W rows 27, 28, 31, 33; R point 6
  for the two largest). Their own records show the cost: rules pinned to one CLI version's captured screens (W row
  28), a busy-marker that stopped matching a new Claude Code build (W row 48), a scrape that fired on text in the
  scrollback (W row 49).

The seed's hypothesis of 2026-09-30 — none of the nine tools it lists reads state off the screen — stands as
"confirmed" in `HYPOTHESES.md` (2026-10-02). Today it partly holds (W §6a): most of the nine read records or hooks,
one polls the screen in one of its modes, one inspects a pane region before it pastes, one's mechanism is unresolved;
several of the nine are messaging tools, not trackers.

**The relay: in parts.** The two-plane pattern — the door carries a pointer, the file carries the content — is
published at least three times: a pointer-only wake through `codex queue` with the content supplied by a hook (W row
4), a mailbox holding the bodies while the host receives a notice id (W row 6), and a paper of 2026-06-12 in which
Claude and Codex keep messages in files and are notified to read them (A, tap). Acknowledgment by the recipient is
published too: a Codex prompt-submit hook that acknowledges a message (W row 3), and one project that documents ACKs
across vendors in its README (A, Open Agent Bridge). No terminal-side acknowledgment was found that links a pointer
to the turn that read the file (A, gap 4).

**The terminal as the place to type: a known practice with reported failures.** Reports of the last three months,
each its own case: a multiline send left unsubmitted in Codex's composer while the sender reported success; Enter
swallowed by Claude Code; a send landing on a half-typed human draft (W rows 42 to 46). Several of them propose the
same remedy, one bracketed paste and then a single Enter; that is a remedy proposed, not one validated four times.
The manual of the installed tmux keeps the two apart: a bracketed paste is not a submission (C6).

**The project's own earlier judgment.** O concluded on 2026-10-01 that reading meaning from the screen is redundant
for Claude Code and Codex, and stays a narrow contingency for Antigravity CLI's one missing state. T recommends
ADOPT for one narrow thing — a pane's output captured with tmux `pipe-pane` as the lab's source method — and says
of itself that it is not this verdict. Neither is contradicted here.

**The wheel that is closest is our own.** What this line runs since 2026-11-19 is the two-plane pattern with a
finite watch and a log. Nothing published was found that does more for this operator's case with less.

# 3. Overengineering check — would a smaller composition serve?

The need, as the brief states it: routine relay runs without the operator; only strategic decisions reach him.

**It serves today.** In this bed, on 2026-11-26 between 03:58 and 04:26 UTC, the lead sent eight pointers to three
seats of the other vendor and saw eight RETURNs. The first six came 39, 64, 39, 48, 705 and 81 seconds after the
call — turnaround, the seat's work included; the 705 was a research task (K). The operator carried none. The
predecessor bed logged 48 coordination pokes, each with a documented outcome; one early one first timed out without
a RETURN (K; whether the operator had to step in for it is not in the handoff).

**What it is made of** — and this is the finding of the check: the program's two parts already run in it by hand.

| Part of the program | What runs in its place today | Its standing |
|---|---|---|
| a tracker of session state | before each pointer the sender looks at the recipient's pane: the right thread in the foreground, the input row empty, not working | a reading of the screen, done by the sender's own command; provisional |
| an impulse through the terminal | a Codex seat rings a Claude lead with one bracketed paste and a single Enter, look-first (RUNBOOK, "How this party talks") | allowed for this party by the RUNBOOK; provisional |
| — | a Claude lead rings a Codex seat through `codex queue` | a vendor door, parked by D1; used because no agent types into a Codex pane (L4); provisional |
| delivery known | a finite watch on the RETURN file; the carrier's answer is never read as delivery | this line's rule (harvest row U20) |

**What is on record against it — and what kind of record each is.**

| Lack | Where seen | Kind of record |
|---|---|---|
| A pointer is accepted and arrives late or not at all. | P: of five accepted, three arrived within seconds, one 2 days 2 hours later, one unresolved | samples at recipients set up on purpose with a chooser standing or a turn aborted; not routine use |
| A seat waits for an approval and nothing on the file plane says so. | P, packet 3: 424 samples of a chooser over 438.758 seconds; the session's record carried no entry naming the wait | a sample; the person and the observer could both see the chooser |
| "Idle" does not say how the last turn ended. | the predecessor's process record, fault 5: the one sample message not seen to arrive differed from the others in exactly that; "whether that is the cause is not known" | a lesson from the same samples |
| An agent that died looks like a quiet one. | not seen in this line. O: one upstream report of three missing session-end markers in ten clean exits, for `codex exec` on macOS at 0.158.0 | a report from elsewhere, another mode and platform |
| A bell arrives while the lead runs a turn. | this bed, cycle 03 | no failure: the bell queued and was read |

None of the five is a failure seen in routine use: three come from samples made on purpose, one from a report
elsewhere, one is no failure. The delta of DRAFT 2 — a state file, a receipt, a send recipe — was built on all
five. It also had costs the draft did not price (Q): handlers that must be kept trusted in the
operator's own configuration files, one adapter per vendor, and a receipt that can show a delay sooner but can
neither wake the recipient nor mend the delay.

**The helper inventory** of the predecessor line counts 46 helpers of five recurring kinds — bounded waiting,
independent observation, permission to proceed, private continuity, independent read-back
(`../eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md`, as the lead read it earlier in this sitting; not re-read
for this version). They are the pieces a small composition needs around it, and they already exist.

# 4. Vendor-harness check — what do the vendors ship, and what would retire the build?

| | State without reading the screen | A way in for a message | Marks |
|---|---|---|---|
| **Claude Code** 2.1.332 (installed) | hooks for prompt, tool use, permission request, notification, stop, compaction before and after, session end (W row 15; A) · `claude agents --json` since 2.1.145 of 2026-05-19, wait reasons since 2.1.162 of 2026-06-03; documented as listing every live session (A; R 3b; L) · the status sequence OSC 7501 since 2.1.295 of 2026-10-08 | messages between Claude sessions, on by default since 2.1.224 of 2026-08-07; a one-shot notice when a session next goes idle, 2.1.236 (W row 13; A) · a per-session inbox socket offered to "a script or hook", auth line documented, message format not (R 3c) · channels, a research preview since 2.1.80 (A) | agent view is a research preview; whether the listing reports a session in a tmux pane is untested |
| **Codex CLI** 0.172.0 (installed) | hooks on by default since 0.124.0 of 2026-04-23; the page read today lists fourteen events, among them permission request, stop, interrupt, compaction, session end (A; R 2d) · thread status for a client of the server that owns the thread (W row 21; A) · OSC 7501 since 0.163.0 of 2026-10-15, blocking kinds since 0.164.0 (A) | `codex queue` since 0.149.0 of 2026-08-20; optional resume since 0.166.0; acceptance says nothing of receipt (R 2a; A) · a native mailbox in 0.171 and 0.172 whose reach beyond one session tree is not stated — R infers a tree (R 2b) | hooks must be trusted before they run; one report of the status sequence saying idle while a prompt waited (R 2c) |
| **Antigravity CLI** 1.5.x | the status-line script receives `agent_state`, `tool_confirmation_pending`, a count of queued input (R 4b; A) · six hook events, none for permission, compaction or exit (R 4a) · OSC 7501 since 1.4.0 of 2026-10-16 (A) | Remote Control, opt-in, since 1.2.6; ACP for the client that owns the connection, since 1.5.0 (A). No supported delivery by a third party into an ordinary running session was found (A, gap 2) | — |
| **Gemini CLI** 0.71.1 | hooks on by default since 0.26.0: before and after the agent loop, tool permission, before compression, session end best-effort (A) · no OSC 7501, a request is open (A) | ACP, for the client that owns the connection (A) | for individuals it stopped serving Google AI Pro, Ultra and free Code Assist on 2026-06-18 (Google's notice of 2026-05-19, cited in `brief.blind.relay-research.corrections.2026-11-26.md`, C3) |

**What changed since the project last looked, on 2026-10-02.**

- Then, Antigravity CLI had no signal for *waiting for approval* — the one state for which a screen classifier stayed
  a live contingency (O). Now its status-line data carries `tool_confirmation_pending`. On paper the contingency is
  closed; nothing was tested.
- Now three of the four CLIs write a discrete state into the terminal themselves. The protocol's vocabulary — idle,
  working, blocked, done, error — is wider than what each emitter is shown to cover, and "blocked" alone need not
  tell a question from an approval.
- Then and now: hooks can miss an exit, and no vendor ships a door between vendors.

**The native change that would retire the build.**

- *For the tracker:* a tmux release that carries the commit of 2026-11-12, which adds the pane formats
  `pane_program_state`, `pane_program_name` and `pane_program_message` (X). It is in no release; the newest is 3.8
  of 2026-09-09; this host runs 3.7c. It would give access, per pane, to the state a program reports about itself
  — which could take the place of the sender's look at the screen. It would not verify that state, and it carries
  neither compaction nor the death of a process.
- *For the relay:* a supported way to address a message into a live session, with an acknowledgment correlated to
  the recipient's turn, on both first-class endpoints. Neither vendor need ship anything across vendors for that.
  Today Claude Code has it for Claude peers only; Codex has the way in without the acknowledgment. None found
  announced.

# 5. Why this ranking

**REFUSE first.** The need is being served by something smaller that already runs; the program's two parts exist in
it by hand; and of the lacks on record none is a failure of routine use. The RUNBOOK asks for a verdict on evidence
instead of on momentum. The evidence for building is research abundance — much exists that could be taken — and
that is not a need.

**ADOPT second.** If the need turns out unserved, nothing has to be invented. The things to take are named by three
research lines that agree: the vendors' own hooks; the program status a pane reports, once tmux releases it; the
published pattern of turning either into a record on the file plane. The delta is then the smallest thing that
serves the one state the failure names — and its shape is a design decision still owed (§7), not this verdict's.

**REINVENT last.** A classifier of the screen would be at least the seventh published one, with the breakage the
others document, for states the vendors' programs now emit.

# 6. Conditions — each with its test

1. **The composition keeps serving.** Test: the falsifier's count, kept in the poke logs the line already writes —
   pointer, carrier's answer, end of the watch, RETURN seen, and one more field: whether the operator had to step
   in. It costs one field, and nothing is built.
2. **The refusal does not hold up the floor.** Test: the lab's qualification names as its prerequisite "an applicable
   recorded L14 D4 verdict" (T), not a relay chapter; if Majkee does not take this verdict as that one, the
   condition fails and he should know it before he says GO or STOP.
3. **If ADOPT is triggered, an emitted state is taken only after it is compared with independent truth.** Test, as
   the auditor framed it (Q): a named mix of events per vendor, a tolerance in time, labels made by an observer who
   does not read the signal, "unknown" and "missing" as outcomes of their own — and a single false *idle* before an
   input counts as a failure whatever the aggregate. Two emitted signals agreeing with each other proves nothing.
4. **If a receipt is ever made, it keeps four facts apart:** accepted by the carrier; seen by the recipient's hook;
   file read; answered. Test: each has its own record, with the recipient and the turn named, and a deadline after
   which a missing one is reported.

# 7. Decisions owed — not made here

- **The carrier.** `codex queue` is the way this line rings a Codex seat, and D1 parks it as weather. The debt to
  retire the provisional file-poke (`relay-X.ledger.md`; goal G7 of `relay-X0-carryover`) needs three separate words
  from Majkee: that he accepts what a replacement covers, that he adopts its transport, that he retires the
  chapter. Two ways lie open and both are his: take the bridge that runs, with its vendor door, as what gets
  qualified — or hold D1 strictly, which means an impulse through the terminal into a Codex pane, which L4 forbids
  an agent today. Only the second would be a reason to open `relay-X3-pty`.
- **The shape of any state record.** The events map of 2026-10-02 holds that events are append-only facts and state
  is derived, never stored (O). DRAFT 2's stored state line ran against it. The auditor names an existing gate for
  per-writer observations and derived views (Q); who owns such a record, and how it overlaps, is owed before
  anything is written.
- **L4.** A state signal, however accurate, gives no agent the authority to type into a pane.

# 8. What the constraints cost

- **The floor of D1 is unconditional** — the rule "stop building the tap when hooks cover every state" was struck on
  2026-10-02 because it made the vendor-invariant floor depend on vendor features (G). Its cost is the lab's
  qualification and collector. This verdict does not touch it.
- **"No vendor features where avoidable"** makes the working carrier a parked one, and makes its only replacement a
  practice with reported failures that agents may not perform. That bind is the largest cost found, and it is a cost
  of two locks together, D1 and L4 — not of any evidence.
- **D2** — the file plane is the spine — costs nothing here: it is what makes the small composition work.

# 9. What this verdict does not show

- How often a delay of consequence happens in routine use, and what one costs the operator. The ranking of REFUSE
  over ADOPT turns on that, and only the count of condition 1 — or his own word — settles it.
- That any hook fires as documented on this host, or that any CLI emits the status sequence inside tmux.
- That `claude agents --json` reports a session attached in a tmux pane; that the inbox socket accepts a message from
  a script that is not the session's child.
- When tmux will release the two commits.
- That no vendor emits the composer's state, or that no relay retirement is announced: both are "none found" in
  bounded searches.
- The phone lens. Remote control of their own sessions is documented for Claude Code, Codex and Antigravity CLI
  (W §4; A); nothing here establishes it for Gemini CLI, and a lens across vendors is shipped by none.
- Dates: where a release page shows day and month only, the year is inferred (R, header).

# 10. For the gate

The recommendation: neither `relay-X3-pty` nor `relay-X4-tracker` opens now. The line keeps its bridge and adds the
one field of condition 1 to its poke logs. The lab's floor goes on under its own gate. The matter comes back when
the falsifier is observed, when tmux releases program status, or when Majkee decides the carrier (§7) — whichever
is first.

What GO and STOP mean on this verdict is his to say. As the lead reads the RUNBOOK: GO takes the verdict as the
recorded answer of L14 D4 — here, that the program stays closed on evidence; STOP sets the verdict aside.
