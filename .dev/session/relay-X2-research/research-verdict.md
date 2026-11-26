---
kind: research VERDICT of the L14 D4 gate — the relay program
by: lead (flight · claude 689d87d0-6d49-4c5c-ae33-7fe561e92ac8) · 2026-11-26 · home
status: DRAFT 2 — written with all three research lines and both evidence maps read. Not yet opposed by the auditor, not committed as the verdict, not seen by Majkee as a verdict. The blind answer of L14 D7 does not exist — the brief is not sent. Draft 1 (04:12 UTC, never committed) recommended against the PTY chapter; that repeated a rule struck on 2026-10-02 and is withdrawn — see §8.
gate: Majkee records GO or STOP on this verdict. It locks no architecture, opens neither relay-X3-pty nor relay-X4-tracker, releases no build and qualifies no door.
judged: the relay program — a PTY impulse layer for relay between interactive CLI agent sessions, and a mechanical tracker of their states — under L14 D1, D2, D5 and D6 as given. The constraints are inputs and are not judged.
---

# Verdict

**ADOPT.** Ranked: 1. ADOPT · 2. REFUSE · 3. REINVENT.

Both halves of the program already exist — in signals the vendors' programs emit themselves, in tmux, and in this
line's own practice. What is left to make is narrow. The two reserved chapters keep their order and open narrowed,
not as the program of 2026-09-30.

What is adopted, by name:

1. **The states of a session** come from what the session's own program emits — today its hooks; next the program
   status sequence, OSC 7501, which Claude Code, Codex CLI and Antigravity CLI already write into the terminal and
   which tmux's development branch stores per pane since 2026-11-12. No classifier of screen content is built.
2. **The floor under those states** — is the agent alive, did it exit — comes from the terminal and the operating
   system, as D1 holds and as the lab is already contracted to measure. Hooks do not replace it.
3. **The relay** is the practice this line runs: a file, a one-line pointer, a finite watch on the reply file.

The delta to make:

- a small normaliser that writes one state per session into a file on the file plane;
- a receipt: the receiver's own hook writes the pointer's nonce, so delivery is never read from a carrier's answer;
- one send recipe for the terminal impulse, gated by the state file instead of a look at the screen — if and only if
  Majkee reconciles it with L4.

**The falsifier.** On the installed versions, in witnessed samples of Claude Code or Codex CLI, the emitted state —
from hooks, or from OSC 7501 once tmux carries it — disagrees with an independent observer on *idle* or on *waiting
for approval* in more than one of ten events. Then the vendors' signals are not a sensor, the screen is the only
place left to look, and the tracker must be reinvented.

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
| M1, M2 | `prior-evidence.map.md`, `prior-evidence.map-2.md` | where the earlier evidence lies; M1 carries three known errors, named in STATUS |
| O | `.dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md` and `vendor-events.catalogue.2026-10-02.md` | the project's own research of October |
| G | `meshup/lab.observability-probes.2026-08-01/DESIGN.md`, line 14 · `meshup/extraction.driller-onion.2026-06/DESIGN.md`, line 27 | the record of the rule struck on 2026-10-02 |
| T | `../../termpanum-X0-source-contract/raw/source-contract.md` and `research-disposition.md` | the packet accepted on 2026-10-22 as input to this decision |

Every research file says of itself that pages were read through a summarising fetch, not raw bytes. W and R are one
line of research; A is a second, made apart from it. Where they disagreed, the primary pages were read again (X).
Nothing in this bed was tested: no session was started, no door was tried, no state was listed.

# 2. Wheel check — does something existing cover it?

**The tracker: yes, in two families, and the families differ in what breaks them.**

- *Emitted signals and records.* Three published tools turn vendor hooks into status files or tmux indicators for
  Claude Code and Codex — working, waiting, done (W rows 36, 37, 38). One reads the CLIs' own session files and says
  those formats are undocumented and may change (W row 35). A fifth combines process identity, hooks, logs and
  terminal patterns over existing tmux sessions, last commit 2026-11-25 (A, ccmux).
- *The screen.* At least six published tools classify a session from pane content (W rows 27, 28, 31, 33; R point 6
  for the two largest, whose documents name screen rules as the main mechanism). Their own records show the cost:
  rules pinned to one CLI version's captured screens (W row 28), a busy-marker that stopped matching a new Claude
  Code build (W row 48), a scrape that fired on text in the scrollback (W row 49), a prompt glyph read as idle
  while the session worked (M2, group H).

The seed's hypothesis of 2026-09-30 — none of the nine tools it lists reads state off the screen — stands as
"confirmed" in `HYPOTHESES.md` (2026-10-02). Today it partly holds: six of the nine read records or hooks; one polls
the screen in one of its modes and one inspects a pane region before it pastes (W §6a).

**The relay: in parts, never whole.** The two-plane pattern — the door carries a pointer, the file carries the
content — is published at least three times: a pointer-only wake through `codex queue` with the content supplied by
a hook (W row 4); a mailbox holding the bodies while the host receives a notice id (W row 6); and a paper of
2026-06-12 in which Claude and Codex keep messages in files and are only notified to read them (A, tap). Three
further projects claim cross-vendor delivery with acknowledgments; their claims are their READMEs' (A rows 12 to
14), and the auditor would not rest a decision on them. No published relay was found that confirms, across
vendors, that the recipient's turn read the file (A, gap 4; W §5, gap 3).

**The terminal as the place to type: a known practice with known failures.** Independent reports of the last three
months: a multiline send left unsubmitted in Codex's composer while the sender reported success; Enter swallowed by
Claude Code; a send landing on a half-typed human draft (W rows 42 to 46). Four repositories report one remedy —
one bracketed paste, then a single Enter (W §6b; M2, group H, names the same). The manual of the installed tmux
keeps the two apart: a bracketed paste is not a submission (C6; A, tmux manual).

**The project's own earlier judgment.** O concluded on 2026-10-01 that reading meaning from the screen is redundant
for Claude Code and Codex, and stays a narrow contingency for Antigravity CLI's one missing state. T recommends
ADOPT for one narrow thing — a pane's output captured with tmux `pipe-pane` as the lab's source method — and says
of itself that it is not this verdict. Neither is contradicted here.

# 3. Overengineering check — would a smaller composition serve?

The need, as the brief states it: routine relay runs without the operator; only strategic decisions reach him.

**What the smaller composition already does.** In this bed, on 2026-11-26 between 03:58 and 04:16 UTC, the lead put
six POINTs to three seats of the other vendor and had six RETURNs — five of them 39 to 81 seconds after the call,
one, a research task, after 11 minutes 45 seconds (`raw/pokes.log.md`). The operator carried none. The predecessor
bed logged 48 such pokes, each with a documented outcome (P, handoff §3). The parts: files, a one-line pointer, a
finite watch on the reply file, a bell as a hint, a one-line notifier for the operator.

**What it lacks, and the smallest thing that closes each lack.**

| Lack | Seen where | Smallest thing that closes it |
|---|---|---|
| The sender learns of delivery only from the reply. A message can be accepted and arrive two days later, or not be seen. | P: five accepted, three arrived in seconds, one after 2 days 2 h, one unresolved | a receipt file written by the receiver's prompt-submit hook, carrying the pointer's nonce |
| Nobody sees that a seat waits for an approval. | P, packet 3: a chooser stood for 438 seconds; the session's record named no wait | the permission-request hook writes "waiting" into the state file |
| "Idle" does not say how the last turn ended. | the predecessor's process record, fault 5 | the stop hook writes how the turn ended |
| An agent that has died looks like a quiet agent. | O: Codex's session-end hook missed 3 of 10 clean exits in one report (`codex exec`, macOS, 0.158.0); no hook fires on a hard kill. A: the pane's shell may outlive the agent. | the agent's process, watched by the operating system or by tmux — the floor of D1, not a hook |
| A bell is pasted while the receiving session runs a turn. | this bed, cycle 03 | the receiver's state file, read before the bell |

Four of the five are closed by a hook and a file. The fourth is closed only by the floor — which is why the rule
"stop building the tap when hooks cover every state" was struck (G), and why this verdict does not revive it.

**What a screen classifier would add over that:** whether the composer holds an unsent draft (W rows 44, 45). No
vendor emits it. It is one property of one row of the screen, and it matters only to a sender that types into the
pane.

# 4. Vendor-harness check — what do the vendors ship, and what would retire the build?

| | State without reading the screen | A way in for a message | Marks |
|---|---|---|---|
| **Claude Code** 2.1.332 (installed) | hooks for prompt, tool use, permission request, notification, stop, compaction before and after, session end (W row 15; A) · `claude agents --json`, since 2.1.145 of 2026-05-19, documented as listing every live session with busy, waiting or idle and what it waits for (A; R 3b; L) · OSC 7501 since 2.1.295 of 2026-10-08 | messages between Claude sessions, on by default since 2.1.224 of 2026-08-07; a notice when a session next goes idle, 2.1.236 (W row 13; A) · a per-session inbox socket offered to "a script or hook", auth line documented, message format not (R 3c) · channels, a preview since 2.1.80 (A) | agent view is a research preview; whether the listing reports a session in a tmux pane is untested |
| **Codex CLI** 0.172.0 (installed) | fourteen hook events, among them permission request, stop, interrupt, compaction, session end; on by default since 0.124.0 of 2026-04-23 (R 2d; A) · thread status through the app server, for a client of the server that owns the thread (W row 21; A) · OSC 7501 since 0.163.0 of 2026-10-15, with blocking kinds since 0.164.0 (A) | `codex queue` since 0.149.0 of 2026-08-20; optional resume since 0.166.0; acceptance says nothing of receipt (R 2a; A) · a native mailbox within one session tree, 0.171 and 0.172 (R 2b) | hooks must be trusted before they run; one report of the status sequence saying idle while a prompt waited (R 2c, issue 60296) |
| **Antigravity CLI** 1.5.x | the status-line script receives `agent_state`, `tool_confirmation_pending` and a count of queued input (R 4b; A) · six hook events, none for permission, compaction or exit (R 4a) · OSC 7501 since 1.4.0 of 2026-10-16 (A) | none found into a running interactive session; the vendor called its agent API internal on 2026-06-30 and a request for one is open (A, gap 2) | — |
| **Gemini CLI** 0.71.1 | hooks on by default since 0.26.0: before and after the agent loop, tool permission, before compression, session end best-effort (A) · no OSC 7501; a request is open (A) | ACP, for the client that owns the connection (A) | serves organizations and paid keys only since 2026-06-18 |

**What changed since the project last looked, on 2026-10-02.**

- Then, Antigravity CLI had no signal for *waiting for approval* — the one state for which a screen classifier stayed
  a live contingency (O, verdict). Now its status-line data carries `tool_confirmation_pending`, and it emits the
  status sequence with a blocked state. On paper the contingency is closed; nothing was tested.
- Then, the only vendor-native state signal inside the terminal stream was a bell (M2, group H). Now three of the
  four CLIs write a discrete state — idle, working, blocked, done, error — into the terminal themselves.
- Then and now: hooks miss exits, and no vendor ships a door between vendors.

**The native change that would retire the build.**

- *For the tracker:* a tmux release that carries the commit of 2026-11-12. It adds the pane formats
  `pane_program_state`, `pane_program_name` and `pane_program_message`; a second commit of 2026-11-23 forwards the
  active pane's report (X). Neither is in a release; the newest release is 3.8 of 2026-09-09; this host runs 3.7c.
  With it, the tracker's classification is one tmux format per pane, for every CLI that emits — a discrete state,
  carried by the terminal, with no comprehension: what D1 and the pending D3 ask for, arriving from upstream. Its
  limits, from the sources: the protocol has no state for compaction (A, gap 1); Gemini CLI does not emit it;
  Claude Code's documentation says that inside tmux it asks tmux for support (R point 1), so on 3.7c it very
  likely stays silent.
- *For the relay:* nothing. Each first-class vendor ships a door for its own sessions; none ships or has announced
  one across vendors, and D1 parks the doors that exist.

# 5. Why this ranking

**ADOPT first.** For every state the tracker was to classify, an emitted signal exists on both first-class
endpoints, a second channel for the same states is landing in the terminal layer itself, and published tools already
turn the first into files. The relay this line runs already keeps the operator out of routine. The delta is small
and every piece of it has a test.

**REFUSE second.** If the delta is not wanted, the right course is the present practice with its known lacks, and
the lab's floor as D1 already plans it — not the program.

**REINVENT last.** A classifier of the screen would be at least the seventh published one, with the breakage the
others document, for states the vendors' programs now emit — built in the months in which that emission is moving
into tmux. A relay system of our own would rebuild what five published projects built, each with its own transport
and store. REINVENT becomes right only if the falsifier is observed.

# 6. The delta, named

1. **State file.** One line per session — session, state, time, how the last turn ended — written from emitted
   signals only: hooks for Claude Code and Codex CLI, the status-line script for Antigravity CLI; the tmux pane
   format in their place once a release carries it. The states are the four the events map of 2026-10-02 already
   drafted: working, waiting, idle, exited.
2. **Floor.** The agent's process and the pane's output, by tmux and the operating system — the lab's source method
   of T. It supplies *exited* and catches what the signals miss. It is measured, not interpreted.
3. **Receipt.** The receiver's prompt-submit hook writes the pointer's nonce into a receipt file. Accepted, received
   and answered stay three separate facts.
4. **The carrier stays replaceable.** Whatever rings — `codex queue`, a paste into the pane, the operator's hand — is
   a doorbell. No carrier's answer is read as delivery.

No external tool's code is adopted. The nearest bring their own transport and state store, and several are one
author's work (W, maintenance column; A, rows marked "claimed"). They are adopted as evidence that the pattern holds.

# 7. Conditions — each with its test

A later bed tests these; this one ran nothing.

1. **The emitted states are right.** For one Claude Code and one Codex session in tmux panes on the installed
   versions, each of working, idle and waiting for approval produces its state line. Test: an observer that does not
   read the state file — the lab's tap, or a person — notes ten events per vendor; the file is compared afterwards.
   This is the falsifier's test.
2. **A message that arrives is seen to arrive.** A pointer sent by each carrier in use produces a receipt with its
   nonce. Test: ten sends per carrier, two of them at a session whose last turn was aborted — the case of P, packet 4.
3. **A dead agent is told from a quiet one.** Test: end the agent's process in a pane whose shell survives; the
   state file says exited, not idle.
4. **The hooks stay trusted across an update.** Test: after one update of Codex CLI, condition 1 once more.
5. **The terminal's own signal agrees.** Test: with a tmux at or after the commit of 2026-11-12, the pane format is
   compared with the state file on the same ten events. If it agrees, the hook scripts for those states retire.

If condition 1 fails for one vendor on one state, the delta is still right for the rest, and that one state on that
one vendor is the question a screen classifier would be opened for — one state, not a program.

# 8. The constraints: what they cost, and one correction of this verdict's own first draft

- **The floor of D1 is unconditional.** The first draft of this verdict said "no relay-X3-pty". That was the rule of
  the Termpanum brief — stop building the tap when hooks cover every state — which Majkee struck on 2026-10-02 because
  it made the vendor-invariant floor depend on vendor features (G). The draft is withdrawn on that point. The cost
  of the floor is the lab's qualification and its collector, even where hooks cover. What it buys is real on the
  evidence: missed exits, the hard kill, and a check on the vendors' own signals — condition 1 needs exactly such an
  observer.
- **"No vendor features where avoidable."** Hooks and the status sequence are vendor features. The record of the
  strike already places them — "the PTY tap is built; hooks enrich" (G). This verdict leans on that enrichment for
  every state but *exited*. If that is more weight than "enrich" was meant to bear, the verdict fails on a
  constraint, not on evidence, and Majkee is the one to say so.
- **L4 with D1's parked doors** leaves no clean way to ring a Codex seat: an agent may not type into a pane, and the
  vendor's door is weather — yet this line's pokes use that door, provisionally, and the samples show it can hold a
  message for days. The receipt makes that failure visible; it does not remove it. Which carrier rings is
  architecture, and is not decided here.

# 9. What this verdict does not show

- That any hook fires as documented on this host, or that any CLI emits the status sequence inside tmux.
- That `claude agents --json` reports a session attached in a tmux pane; that the inbox socket accepts a message from
  a script that is not the session's child. Each is a cheap test for a later bed.
- When tmux will release the two commits.
- That the figure of three missed exits in ten holds for an interactive Codex 0.172.0 on Linux; it is one report,
  for `codex exec` on macOS at 0.158.0.
- The phone lens. Each vendor ships a remote control for its own sessions (W §4; A); a lens across vendors is shipped
  by none. A state file on the file plane is something a thin lens can read; no more is claimed.
- Dates: where a release page shows day and month only, the year is inferred (R, header).

# 10. If he says GO

The verdict becomes the founding reference of what opens next under L14, in the order L14 fixes.

- `relay-X3-pty`, narrowed to two questions: the floor — which the lab's contract of 2026-10-22 already frames, and
  whose qualification names "an applicable recorded L14 D4 verdict" as its first prerequisite (T) — and the one send
  recipe, with L4 reconciled or not.
- `relay-X4-tracker`, narrowed to the normaliser of §6 and the receipt, with the tests of §7. No classifier of the
  screen.

Whether this verdict is that applicable verdict for the lab's qualification is Majkee's to say; it is not claimed
here. The file-poke stays provisional until a bed maps what the receipt covers.
