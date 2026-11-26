---
kind: master brief to the CLI seats — Symmetry's synthesis of one day's collision on the relay program and the observation floor
by: Symmetry (claude.ai, Fable 5.2) · 2026-11-26 · at majkee's request
status: INPUT, not a verdict. It locks nothing, opens no bed, releases no build and no test. Nothing in it was run on the host.
reading_order: the lead of relay-X2-research reads this only after its own differences file on the blind relay answer is written. §3 and §4 contain Symmetry's comparison and would steer that list.
homes: filed by majkee in relay-X2-research/raw. The relay part bears on that bed; the floor part belongs to the lab line (termpanum / VIST) and its sources lie in .dev/_backlog/.
repo_state_read: github.com/hruzam/nablarva at 81f5e6f (shallow clone); .majkee/ and .hlm/ not opened.
---

# 0. Ten assumptions — strike what is wrong before reading on

1. The gate of relay-X2-research is still open: no GO or STOP is recorded.
2. Host: tmux 3.7c, Claude Code 2.1.332, Codex CLI 0.172.0. The kernel version is not known to me.
3. The lab's byte source is one `pipe-pane -O` per pane, and that slot is termpanum's.
4. "Relay" means: this seat can take one new item now. "Alert" means: a person's decision is outstanding. Majkee has not confirmed these two words.
5. L4 forbids an agent typing into another seat's pane. Whether a write by code that owns the PTY falls under it is undecided.
6. D3 is read strictly here: rebuilding the screen to match text on it counts as comprehension.
7. No seat has tested anything named in this document on the host.
8. Asymmetry's relay answer did not know that a file-poke already runs. Its first floor answer did not know the programs are coding agents. Its second floor answer knew both.
9. The seats have not read Symmetry's side note or any of Asymmetry's three answers, unless majkee filed them.
10. Majkee's six answers in `decision.majkee.brief-and-check.2026-11-26.md` are as drafted with Symmetry that evening; he may have changed them.

# 1. Inputs

Paths are relative to `/home/hruzam/unikuklatrix/nablarva`, as majkee gave them on 2026-11-27.
Symmetry has not seen these files at these paths; it read the same texts as uploads.

| Short | What | Path | Blind to |
|---|---|---|---|
| V | the verdict, third version — REFUSE · ADOPT · REINVENT | `.dev/session/relay-X2-research/research-verdict.md` | — |
| BR | the relay brief as sent to Asymmetry | `.dev/_backlog/first-blind-triangulation-relay/brief.symmetry.blind.relay-research.send-copy.2026-11-26.md` (the bed's own copy: `.dev/session/relay-X2-research/raw/brief.blind.relay-research.send-copy.2026-11-26.md`) | — |
| AR | Asymmetry, "Blind evidence review — tracking and relaying interactive CLI agents" — verdict ADOPT | `.dev/_backlog/first-blind-triangulation-relay/blind-relay-triangulation-asymmetry-2026-11-26.md` | the running file-poke; V |
| B1 | the floor brief, blind | `.dev/_backlog/blind-triangulation-programatic-approach/brief.blind.session-telemetry-floor.2026-11-26.md` | — |
| F1 | Asymmetry, "What an outside observer can know about a terminal session" | `.dev/_backlog/blind-triangulation-programatic-approach/asymmetry.session-telemetry-floor.blind-review.md` | agent context; everything of ours |
| B2 | the floor brief, open round 2 | `.dev/_backlog/blind-triangulation-programatic-approach/brief.open.session-telemetry-floor.round-2.2026-11-26.md` | — |
| F2 | Asymmetry, "Who owes the next action?" — open round 2 | `.dev/_backlog/blind-triangulation-programatic-approach/asymmetry.session-telemetry-floor.round-2.md` | nothing |
| N | Symmetry's side note, `note.symmetry.codex-submit-and-wake.2026-11-26.md` | path not given to Symmetry — majkee to fill in | — |
| — | this file | `.dev/session/relay-X2-research/raw/master.symmetry.relay-and-floor.collision.2026-11-26.md` | — |

The four floor paths were given as `dev/_backlog/…`, without the leading dot. `.dev/` is
assumed here; correct the table if the folder really is `dev/`.

F1 and F2 ran fixtures on Asymmetry's own Linux 6.18.57 host, with Codex 0.172.0-alpha.2 and
without tmux or Claude Code. Neither vendor TUI was exercised by anyone.

# 2. What stands — reached by sides that could not see each other

- **REINVENT is last.** V and AR both put a new screen classifier at the bottom.
- **Content in files, a short activation.** AR endorses exactly this part of the plan.
- **Sending is not receipt.** V's four facts (accepted · seen · file read · answered) and AR's four (queued · inserted · file-read · completed) are the same list.
- **One pair cannot be split from below.** Symmetry held "idle versus waiting on a blocking question" before F1. F1 reached it unprompted and showed two fixtures equal on every channel: bytes, CPU, wait channel, terminal modes, foreground group.
- **A status record in the byte stream is a declaration, not an observation.**

# 3. Where the sides differ

| Point | V | AR | Symmetry's reading |
|---|---|---|---|
| Rank one | REFUSE: the need is served by what runs | ADOPT hcom and vendor interfaces | AR answers "build or adopt". It could not see the need question. The two are less opposed than the words. |
| "ADOPT" means | take emitted signals, for one observed failure | take a product | hcom brings its own store, a launch wrapper and installed hooks. That is a platform. Its Codex adapter and tests are worth reading as borrowed scars; the product is not proposed here. |
| PTY as common layer | a constraint, not judged | narrowed | The relay brief wrote "his current choice". It should have said: an input, not for judgment. A defect of the brief. |
| Fallback | open `relay-X3-pty` only if D1 is held strictly | reverse to a narrow PTY relay if hcom and native doors fail on pinned versions where a small PTY relay passes | AR's falsifier and its last section are a ready acceptance list for that comparison. |

AR says it did not open "the earlier Wave review". V records as unknown whether the brief of
2026-09-30 was ever answered (dock item U2). This suggests an answer exists.

# 4. Corrections — each names what it corrects

**To V.**
- §4 lists Codex's permission-request hook as state without the screen. AR, from hcom's source: the hook can fire before an automatic reviewer decides, so it does not mean a person waits.
- §4 names a tmux release with OSC 7501 formats as the change that would retire a tracker. F2, from the pinned sources: Codex 0.172.0 writes the OSC 7501 record without waiting for the terminal to agree, and tmux 3.7c copies pane bytes to its pipe and control clients *before* parsing. Predicted: the lab's raw tap sees Codex's `blocked` record today. Untested.
- §4 leaves open whether `claude agents --json` lists a session in a tmux pane. F2 reads the documentation as covering live interactive rows, with `status: waiting` and a `waitingFor` reason. Untested here.
- The installed tmux already parses OSC 9;4 into `pane_pb_state` and `pane_pb_progress`. V does not mention them. They report work, not a wait.

**To the events map (v0.3).**
- The four states are not a partition. A question can be outstanding while a worker computes. F2 proposes eight dimensions, each with its own subject and lifetime (§5).
- Row 11's PTY-only fallback says a stall "cannot distinguish approval from slow tool". The harder pair is approval versus idle.
- Add: a status is "unknown since attach" until evidence arrives. Silence means something only over an interval with proven continuity.
- Row 2: on Linux 6.15 or later an observer holding a pidfd can read the exit status after the parent reaped. Check the host's kernel.

**To N (Symmetry's own note).**
- "A live child means a tool runs" is wrong. Agent CLIs keep long-lived helpers. Usable: a newly appeared child, or a child's CPU delta, and even then a link to the request is missing.
- Codex's approval notification by OSC 9 or BEL is conditional: gated by focus, coalesced, absent in a headless PTY. It gives no open/close pair.
- Idea 3, "pull instead of push", survives only in a narrower form (§7).

**To AR.**
- It treats the terminal as carrying no state contract. F2 shows Codex now writes a typed one into it.

# 5. The shape that falls out

**Two decisions, not one state.** Relay and Alert need different evidence. A relay never needs to tell a question from a hang; it needs a positive "free". An alert needs a declared reason.

**Dimensions (F2), with who gives each its meaning.**

| Dimension | Smallest witness | Meaning comes from |
|---|---|---|
| Process lifetime, exit cause | identity plus kernel record; pidfd on 6.15+ | kernel |
| Local execution, child presence | CPU delta; verified parent | kernel |
| Transport activity | per-socket counter deltas | kernel — if readable at all |
| Pane output and its quality | bytes over time, tap start, gaps, geometry | mux and kernel |
| Request lifecycle | correlated start and end of one turn | vendor |
| Outstanding human decision | declared reason, scope, how it ends | the declaring program |
| Relay availability | a still-valid, unspent receive for this seat incarnation | **our own seat convention** |
| Human control of input | attached clients; an explicit handoff | mux; convention |

The first four are the floor: vendor-neutral, coarse, and enough to check what the vendors
declare. The fifth and sixth need one adapter per vendor. The seventh is ours. This is
majkee's "one uniform core, one adapter per vendor", with the line drawn by evidence.

# 6. Where the "answer owed" bit is — pinned versions, all untested on the host

| Program | Surface | What it gives | Limit |
|---|---|---|---|
| Codex 0.172.0 | OSC 7501 in the raw pane bytes | `state=blocked` with `kind=permission`, `question` or `auth` | scope is the displayed thread; no thread, turn or request id; a late tap misses the only copy; unchanged status is not repeated |
| Codex 0.172.0 | app-server stream, if a copy already exists | typed requests with ids; `isBlocking`; a resolution event | a stock TUI may run an embedded server nobody else can read |
| Claude Code 2.1.332 | `claude agents --json`, read outside the pane | `status: waiting`, `waitingFor: permission prompt` or `input needed` | polling misses short waits; no request id; whether this read counts as passive is majkee's call |
| Claude Code 2.1.332 | OSC 7501 | — | Claude asks tmux for support; 3.7c has no handler; expect no report |
| either | session file on disk | closes history for a turn | Codex's rollout omits approval and input requests and records a tool call before dispatch; Claude writes transcripts asynchronously. Not a real-time alert source. |

`done` or `idle` from Codex does not settle whether the composer will take a new task (fix of
2026-11-09: a finished turn reports `done` with a background process still alive).

# 7. The parked receive — after attack

The idea: a seat that is free for mail does not go idle; its agent stays inside one known
blocking command until mail arrives. Symmetry proposed that a child with a known name and a
verified parent would then be a kernel-level witness of "free".

F2's verdict: **the convention is acceptable; the proof from process name and parentage is
refuted.** The same waiter process exists in a history where the tool wrapper already
returned a background handle and the operator is typing the next turn.

- **The invariant that makes it sound:** for seat incarnation S and receive R, a successful
  claim implies R is still outstanding for S, R may take that addressed item, and the item
  returns through R's own path. Claim and revocation are ordered so that only one wins.
- **What defeats it:** a tool time limit; an approval asked for the wait itself; compaction
  or reset; a wrapper shell; two senders.
- **A trap in tmux 3.7c** (from its source): one `wait-for -S` wakes every waiter on the
  channel; with no waiter one signal is kept; a second early signal can remove the channel
  and leave a later waiter asleep with both messages on disk. So the signal is a doorbell
  and the file with its claim is the delivery record — which is D2.

# 8. Tests — proposals only; each needs majkee's release

Cheapest first. All read-only toward the target seat; the operator's own account of what was
pending is the independent truth.

1. **Bind the subjects.** tmux version of the *running server*; per pane: id, pid, tty, pipe state, `pane_pb_state`, `pane_pb_progress`. An occupied pipe is left alone.
2. **Claude's status surface.** Read `kind, pid, startedAt, sessionId, status, waitingFor` from `claude agents --json` during a real approval and a real question. Does the reason appear and clear?
3. **Codex's OSC 7501 on the raw tap.** One real permission or question episode, start to resolution. A `blocked` record that matches the operator's account admits a positive Alert for the displayed thread.
4. **Break it cheaply.** A picker, a question asked while work continues, a thread switch, a phone reattach at another size, a tap started in the middle of a wait.
5. **Session files.** Event type, ids and arrival time around one answer, one interruption, one reset. No message text.
6. **Transport control.** `ss -Hntie` on a disposable same-user connection first. Asymmetry's own host answered EPERM. Until this passes, traffic deltas are "unavailable", not "quiet".
7. **The parked receive**, on a disposable seat: requested · registered · claimed · read. Any double claim, claim after revocation, or loss between wake and claim rejects the convention.

More consumers of one pane without displacing the tap: a read-only control client
(`tmux -C attach-session -E -r -t SESSION`), or followers of an append-only log the existing
pipe already writes. Attaching still adds a client and can fire hooks.

Carried from N, for `relay-X3-pty` if it ever opens: at which gap and which way of writing
does Codex 0.172.0 submit a one-line pointer, read from the rollout and not from the screen?

# 9. Decisions owed by majkee — none is made here

1. **What Relay promises:** the pointer is durably posted · the current receive claimed it · the agent read the file and acknowledged its exchange id. Only the second needs the parked receive.
2. **Which waits ring the phone:** a non-blocking question, or only one that stops the work; and whether auth, sandbox and generic dialogs count.
3. **The unit of attention:** the displayed thread, every thread in a pane, or a named seat across restart and compaction.
4. **What counts as passive:** reading the vendor's status listing; reading an existing app-server stream.
5. **L4 and code that owns the PTY.**
6. **The carrier** (V §7): the running bridge with its vendor door, or D1 held strictly.
7. **D3:** whether screen reconstruction is comprehension (assumption 6).
8. **U2:** whether the earlier Wave review is the answer to the brief of 2026-09-30.

# 10. What this does not show

- That any surface in §6 behaves as its source says on the host.
- That the floor's first four dimensions are readable there without privilege; one external read already failed elsewhere.
- That REFUSE should change. Nothing here is a failure of routine use; V's falsifier still decides.
- Anything about Antigravity CLI, Gemini CLI or Cursor CLI.
- That hcom fails or works; nobody ran it.
