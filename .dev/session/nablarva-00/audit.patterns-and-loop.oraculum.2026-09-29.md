# Audit 1 of 3 — building philosophies, the loop, and patterns

*Oraculum · Claude · 2026-09-29 · session `nablarva-00` · office (`hruzam-120922`).*
*Status: audit report. Uncanonical. Nothing here is a lock, a plan, or a build
authorization. Majkee gavels; `flag.md` keeps authority over locks.*

Companions: [wrapper rewrites](audit.wrapper-rewrites.oraculum.2026-09-29.md) ·
[session progress](audit.session-progress.oraculum.2026-09-29.md) · [STATUS](STATUS.md).

## 0. How to read the evidence marks

| Mark | Meaning |
|---|---|
| `[R]` | Read directly by Oraculum in this session, at the cited lines |
| `[S]` | Reported by a sub-reader; not re-checked by Oraculum. Treat as a lead |
| `[W]` | Web research by Epoch on 2026-09-29. A dated claim, not verified on this host |
| `[W-Aug]` | Web research of 2026-08-07/08 kept in `meshup/_preflight/` |
| `[I]` | Oraculum's inference |

About half of the sub-readers made at least one material error that a check against the
source exposed (list in audit 3, §5). Every `[S]` item should be checked at its quoted
lines before it supports a gavel.

Not read, by instruction: `.hlm/` and `.dev/session/skill-report-test`.

## 1. Governing insight

**The deciding unknown is attraction, and it has never been measured.** A message file
and a reply file already travel between vendors every day. What does not exist is a
native way to tell a living session "there is something for you". Majkee performs that
step by hand, in both directions.

Everything else in the loop either works today or is ordinary engineering. Ten separate
steps were prepared to measure attraction or its neighbours, and none was run (audit 3,
§4.3).

## 2. The loop

Majkee, 2026-09-29: *"sender: mailing → attracting → own process on receiver side →
releasing reply (file, this is important and only one trust sphere but big — keep file
style at least on bus level) → reply → attract sender"*.

| # | Step | What marks it done | Exists today | State |
|---|---|---|---|---|
| 1 | Mailing | Message file written once, at an agreed path | `_bus/NN.seat.point.md` | In daily use `[R]` |
| 2 | Attract receiver | Receiver's living session holds a pointer to the file | Majkee carries the path | **Unmeasured** |
| 3 | Own process | Receiver works in its native session, under its own permissions | Yes, by construction | In daily use |
| 4 | Release reply | Reply file written once and complete, at the destination the message named | `_bus/NN.seat.return.md`, written by the receiver | In use; no completeness marker |
| 5 | Reply available | File present and tied to its message | `cycle` and `return_to` fields `[R]` | In use |
| 6 | Attract sender | Sender's living session holds a pointer to the reply | Majkee notices and carries | **Unmeasured** |

Steps 2 and 6 are one problem in two directions.

**One recorded carry** (2026-09-14) was segmented as 5 actions outward, about 19 actions
on the return leg, and a 16-minute notice lag `[R: nablarva-02 STATUS line 26]`. The
figures come from one mixed workflow. Use them as a baseline for comparison, never as a
promise of savings.

**Working assumption on trust.** All participants (Majkee, his agent sessions, his two
hosts) sit inside one trust sphere. The first loop therefore needs no authentication or
privacy machinery between participants. The released file is what counts as said; a
session's memory or its terminal output does not. *This is Oraculum's reading of
Majkee's phrase and needs his confirmation.*

**Every attraction step needs a named brake.** The entity study states it as a rule:
"Every trigger has escalation potential; every trigger therefore needs a named damping"
`[R: seed.entity.full-idea line 92]`. A loop that attracts automatically in both
directions is two model sessions feeding each other. The brake belongs in the mechanism
(round limit, budget, stop condition), outside model prose.

## 3. Strata — where each idea and each brick lives

The layer chain is Cartan's `[R: workflow-reading lines 103–107]`. The assignment of
bricks and philosophies to layers is Oraculum's `[I]`.

| Layer | Owns | Bricks there today | State |
|---|---|---|---|
| 5 · Human view and device | What Majkee sees and where he sits | ovitmugen frames, runbook browser, editor as monitor, phone console (k0k0nV3R idea), termbrana review pane | ovitmugen and runbook in use |
| 4 · Process and terminal | Running programs, PTY, multiplexer | tmux, Zellij; the sensing family: laboratory, termbrana, ommatermia, onion observer; the driller | termbrana M0 probe frozen; the rest are plans |
| 3 · Runtime connection | Reaching a session: attraction, adapters | Consultation carriers (`tun`, `codex-run.zsh`); vendor hooks; native messaging | Consultation works; attraction of a living peer unmeasured |
| 2 · Exchange | Message, reply, correlation, release, brakes | `_bus/` files; muticula beside it for shared writes | Files in use; no code |
| 1 · Durable work | The store: repos, locks, status, roles | `flag.md`, `pulse.md`, `STATUS.md`, `.germline/`, reposoma | In daily use |

Two rules hold the strata apart:

- **No layer's signal becomes another layer's truth.** Cartan: "A layer's display or
  process signal must not silently become the truth for another layer" `[R]`. A pane
  that looks idle is a layer-4 observation. It is not a layer-2 delivery receipt.
- **Toolboxes exist without the engine.** Majkee, 2026-09-29: the toolboxes were made to
  stand alone as practical helpers; they may be parts of the bigger animal, like
  plugins, but they must not need the nabLarva engine to exist. The engine may consume
  what a toolbox publishes (for example `ov ls --json`). A toolbox never imports the
  engine.

## 4. The building philosophies

Ten distinct ideas appear in the corpus. They are not rivals at one level; most answer
different layers.

| # | Philosophy | Core claim | Layer | Source | Status |
|---|---|---|---|---|---|
| 1 | **X — room is a file** | The room is an append-only file; readers come and go; regulation is cooperative; it fails soft | 2 | Majkee's position, founding handoff lines 59–63 `[R]` | Outvoted 2-to-1; docket 1 keeps a control spike open |
| 2 | **Y — room is a process** | A router owns each agent's terminal and delivers in memory; regulation is structural; it fails hard | 2 + 4 | Same file, lines 65–78 `[R]` | Partly locked through S4, S5 |
| 3 | **Z — brokered hybrid** | Small broker, single-writer journal, per-participant cursors, consultation leases, blind protocol | 2 | Triad comparison; Wave chapter 01 | S1–S8 locked (`flag.md` L3) |
| 4 | **Interposition** | Wrap the vendor CLI; keep a file skin; spine, seam, canary | 4 | `old-but-good-onion/interposition-study.md` `[S]` | Read side measured 2026-08-01; write side never run `[R]` |
| 5 | **Relay seam** | Three planes: activation, observation, authoritative files. Only a pointer rides the transport | 3 | `brief.relay-seam.v2.2026-09-13.md` `[R: lines 21, 29, 45, 56]` | Substrate, not law; folded into session 02 |
| 6 | **Consultation call** | The caller runs a command that blocks until the colleague's reply returns | 3 | Costa seed `[S]`; tunnel card `[R]` | Works today for headless and stored threads |
| 7 | **Entity** | What persists is the disciplined store; model motion is rented; identity is what survives session death | 1 | Entity triangulation `[R]` | Study only; a recorded ceiling forbids middleware before scored evidence |
| 8 | **Laboratory** | Prefer native events over terminal inference; promote a rule only through fixtures and tests | 4 | Wave chapter 04 `[S]`, chapter 07 `[R]` | Design only |
| 9 | **Bricks on the shell layer** | Useful independent tools, delivered through the surgical table | cross-cutting | Wrapper, VOLATILE section `[R]` | In daily use |
| 10 | **Fold** | Research the machine in plain systems vocabulary, then decode | method | Program brief in `meshup/` `[R]` | Preparation complete 2026-08-08; not continued in this repository |

**Where they agree.** These hold across all of them and can be treated as invariants:

- Files are the durable truth; history is appended, never rewritten.
- Each agent keeps its own cognition and its own session.
- The human is inside the system as the slow, highest authority.
- Brakes are structural.
- A native signal beats an inference from terminal output.
- "Unknown" is a valid state and is reported as such.

**Where they truly differ.** Four questions, each needing evidence more than argument:

| Question | Poles | What would settle it |
|---|---|---|
| Who starts the agent's process? | The bus launches it (Y, Z) · the bus attaches to a living one (relay seam, Majkee's loop) | The return-wake probe. Tracked since August as fork F5 `[R]` |
| Is there a running process in the middle? | Yes, a broker (Y, Z) · no, files and hooks (X) | The first loop run as the files-only spike |
| How is regulation enforced? | Structurally by a router · by limits in hooks and scripts | Observed loop behaviour over several runs |
| Which multiplexer? | tmux (ovitmugen, phones) · Zellij (termbrana, onion plan) | The loop should depend on neither `[I]` |

## 5. Patterns, scored against the loop

Key for the step columns: **F** file · **H** human · **N** native vendor surface ·
**P** process owned by the bus · **C** the caller itself waits · **–** not covered.

| Pattern | 1 mail | 2 attract | 3 work | 4 release | 5 reply | 6 attract | Evidence today |
|---|---|---|---|---|---|---|---|
| A · Operator workbench | F | H | native | F | F | H | In use |
| B · Exchange core + native adapters | F | N | native | F | F | N | Reasoned; adapters unqualified |
| C · Room host owning processes | journal | P | owned PTY | extracted | journal | P | Reasoned |
| D · Blocking consultation call | F or arg | C | headless or stored thread | stdout | C | C | Measured; works |
| E · Hook-signalled file loop | F | N at next event | native | F | F | N at next event | Hooks documented; nothing run here |
| F · Native push wake | – | N | – | – | – | N | Documented for Claude; unconfirmed for Codex |
| G · Local HTTP mailbox | F behind a service | N via hook or tool | native | F | F | N via hook or tool | None local |
| H · Observer first | – | – | – | – | – | – | Nothing run |
| I · Protocol adapters (ACP, A2A) | protocol | own session | adapter's session | protocol | protocol | – | Snippets only |

### A · Operator workbench
**Mechanism.** The existing browser shows which reply files have arrived. Majkee
initiates every handoff.
**Gives.** Less locating and copying. Useful before any wake exists.
**Leaves.** Majkee stays in the relay. It does not satisfy the ladder alone.
**Sources.** Workflow reading, candidate 1 `[R]`; blueprint §9 `[R]`.
**Smallest test.** Replay one recorded episode with today's browser and count the
remaining human actions.

### B · Exchange core with native adapters
**Mechanism.** One small program owns addressing, correlation, the release record and
delivery uncertainty. One adapter per vendor performs attraction through a qualified
native surface. Clients are thin.
**Gives.** One owner for exchange behaviour; records survive view and device changes.
**Leaves.** It cannot manufacture a wake the vendor does not offer.
**Sources.** Blueprint §1 and §3 `[R]`; relay seam v2 `[R]`.
**Smallest test.** The return-wake probe.

### C · Room host that owns agent processes
**Mechanism.** A broker launches each CLI under a terminal it owns, appends every event
to one journal, injects prompts, and extracts replies from the terminal stream.
**Gives.** Identity is established at launch; regulation is physical.
**Leaves.** Launch, attach, permissions, restart and recovery all become the bus's job.
Reply extraction needs the driller. It does not reach sessions that already live.
**Sources.** Wave chapter 01, lines 239–258 `[R]`; founding handoff `[R]`; `flag.md` L3.
**Smallest test.** None cheap. Wave's own next move was a capture fixture `[R: chapter
07 line 68]`.

### D · Blocking consultation call
**Mechanism.** The caller runs one command. It blocks until the other vendor's reply
returns on standard output.
**Gives.** A complete round trip today, with no reverse wake needed.
**Leaves.** It reaches a headless process or a stored thread, never the living peer.
It changes which conversation does the work.
**Sources.** Tunnel card `[R]`; blueprint §10 `[R]`; Costa seed `[S]`.
**Evidence.** Tunnel round trip recorded as PASS `[R: pulse.md, last row]`; fixture
selftests `[S]`.

### E · Hook-signalled file loop
**Mechanism.** Files carry the message and the reply. The receiver writes its reply
file itself. When its turn ends, its Stop hook checks whether the expected reply file
exists and, if so, emits the signal. A session picks up waiting mail at its next hook
event.
**Gives.** No terminal reading. The same shape on both vendors. Needs only hooks and
short scripts, so no language decision.
**Leaves.** A hook cannot wake an idle session. It fires only when the session itself
produces an event.
**Sources.** Pre-consultation file, lines 488–530 `[S]`, proposed code, never run;
August research delta, lines 49–136 `[R]`; Epoch items 3 and 10 `[W]`.
**Smallest test.** On a disposable session of each vendor: does a Stop hook fire, and
does it receive a session identifier?

### F · Native push wake
**Mechanism.** The vendor's own channel into a running session.

| Vendor | Surface | Reaches a running session | Maturity |
|---|---|---|---|
| Claude Code | Cross-session messaging over a per-session Unix socket | Yes, same host | Shipped `[W]` |
| Claude Code | Channels: an MCP server pushes a notification | Yes, if launched with the channel flag | Research preview `[W]` |
| Codex CLI | `app-server` thread and turn methods | Only if the TUI runs on an app-server | Documented as experimental `[W]` |
| Codex CLI | Plain running TUI | **Unconfirmed** | — |

**Gives.** The missing piece of patterns B and E: waking an idle session.
**Leaves.** Asymmetric between vendors. Tied to vendor versions.
**Sources.** Epoch items 1, 4, 9 `[W]`.
**Note.** This pattern is a component. It completes B or E; it is not a bus.

### G · Local HTTP mailbox
**Mechanism.** A small local web service holds the mailbox and routes. Sessions reach
it through hook handlers or tools. Files remain the record.
**Gives.** A stack Majkee knows. The mailbox is inspectable in a browser. It reaches
across hosts over the tailnet.
**Leaves.** A process that must stay alive, so it fails hard. Tools are pull only: the
model must call them. It still needs pattern F to wake an idle session.
**Sources.** Majkee's voice note, 2026-09-29; Epoch items 3 and 15 `[W]`.
**Smallest test.** None needed before the wake is measured.

### H · Observer first
**Mechanism.** Sensors (hooks, process tree, viewport) produce samples about one
session. No delivery.
**Gives.** Evidence to tell "waiting for permission" from "working" from "reply ready".
**Leaves.** It is an instrument, not a bus. The onion plan's phase 3 is a
communication policy and should not ride inside an observer `[R: workflow-reading
lines 149–153]`.
**Sources.** Onion build plan `[R]`; workflow reading, lines 128–207 `[R]`.

### I · Protocol adapters
**Mechanism.** Wrap each CLI behind a standard protocol.
**Leaves.** The known adapters start their own sessions, and the Claude adapter is
built on the Agent SDK, which Anthropic's terms tie to API keys `[W, snippet]`. Likely
outside the subscription constraint. Listed for completeness.

### Not a pattern
Keystroke injection through a multiplexer stays dead (`flag.md` L4). The September
proposals that named it as a doorbell are fenced as proposals in Cartan's fold and
blueprint `[R: workflow-reading lines 63–65; blueprint lines 484–486]`.

### One reading of the table `[I]`
Patterns E and F together cover all six steps with files as the carrier and no process
in the middle. B adds an owner once several exchanges must share state. C and G add a
running process. The order of cost is E+F, then B, then G, then C. That ordering is a
reading of the evidence, and the choice is Majkee's.

## 6. Pipes between the bricks

What each brick reads and what it emits. Blank cells are unknown to this audit.

| Brick | Reads | Emits | Consumed by |
|---|---|---|---|
| runbook browser (`runbook.py`) | Session `RUNBOOK.md`, `STATUS.md`, `_bus/` files | Terminal view; advisory board state | Majkee `[R: blueprint §4, §9]` |
| ovitmugen (`ovitmugen.py`) | `presets.json`; tmux server state | tmux views; `ov ls --json` | Majkee; runbook (optional import) `[S]` |
| tunnel (`tunnel-codex.py`, `tun`) | Vault state file; Codex stored threads over JSON-RPC | Reply on standard output | The calling Claude session `[R: card]` |
| `codex-run.zsh` | Prompt | Headless Codex reply on standard output | Vega, Mirror relays `[S]` |
| temple mail and doorbell | Mail files by path | Log; notice | Seats across vendors `[S]` |
| Vendor hooks | JSON on standard input at each event | Exit code; optional context | The vendor runtime `[W]` |
| termbrana probe | Zellij render events | Future JSONL | Nothing yet `[R: README]` |
| muticula | Claim files | Commit gate decision | Under qualification `[R: wrapper]` |
| `qualify.py` | Probe fixtures | Offline test results | Session 02 `[R]` |

**The missing pipes.** Nothing consumes the arrival of a `_bus/` file as an event.
Nothing emits toward a living session. Those two gaps are steps 2 and 6.

## 7. Small ideas that transfer to the loop

| Idea | Source | Use |
|---|---|---|
| Message epoch | Driller chapter, lines 434–442 `[R]` | The reply is bound to the message that caused it |
| Unknown as a first-class state | Cost chapter, line 186 `[R]` | An uncertain delivery is reported, never guessed |
| "Never discard silently" | Cost chapter, lines 218–224 `[R]` | Rule for a loop that falls behind or times out |
| Signal hierarchy | Laboratory chapter `[S]`; chapter 07 line 19 `[R]` | Attraction and reply detection use native events first |
| Two lanes | Ledger, lines 226–244 `[R]` | The reply file is the conversation lane; tool chatter stays out |
| Capability declaration | Ledger, fork B `[R]` | Each adapter states which wake surface it has, for which version |
| "NO faster than YES" | Entity seed, line 83 `[R]` | Stopping the loop is cheaper than continuing it |
| Identity address | Entity round one, lines 57–60 `[R]` | A woken session knows which lineage it continues |
| Cache suggests, provenance binds | Entity round two, lines 56–59 `[R]` | A reply is trusted because of the released file |
| Two scopes of confidence | Program brief, lines 387–406 `[R]` | Hook facts are instrumented; loop behaviour is only characterized |
| Atomic release | Pre-consultation file, lines 444–451 `[S]` | Write to a temporary name, then rename. A half-written reply never counts |
| Canary | Interposition study §6 `[S]` | A smoke test that fails loudly when a vendor changes a surface |

The driller itself is not needed for a file loop. It cleans replies out of terminal
output, and in this loop the reply arrives as a file. Its own verdict: "The dead alley
would be allowing the cleaning subsystem to become the main project before the room
itself exists" `[R: cost chapter line 333]`.

## 8. Tensions that need Majkee's gavel

These are proposals to table. None is decided here.

| # | Tension | Proposal |
|---|---|---|
| T1 | S5 "adapter-owned PTY" (L3) against a receiver that works in its own native process, woken natively | If the probe shows a native wake, scope S5 to the room-host pattern or amend it. New evidence exists: the native surfaces documented 2026-09-29 |
| T2 | Docket 1, the files-only spike, pending since 2026-07-31 | Declare the first loop to be the spike. Watch for the four failure modes Z predicted: locking, fan-out, cursor races, restart `[R: handoff line 116]` |
| T3 | S4 "structural regulation" against a loop regulated by limits in hooks and scripts | Open. Decide after loop behaviour is observed |
| T4 | L4 stays | Keystroke doorbells remain dead. A native wake is a different category and does not reopen L4 |
| T5 | tmux and Zellij both assumed by different bricks | Keep the loop independent of both. Record the split as an open choice |

## 9. What this audit does not know

- Whether a plain running Codex TUI can be addressed at all `[W: unconfirmed]`.
- Whether the Codex Stop hook payload carries the final message and a session identifier.
- Codex method names and version on this host. A local note says `thread/setName` and
  0.154.0; Epoch found `thread/name/set` and 0.159.0 `[W]`. The installed binary's
  generated schema answers this at zero quota `[R: tunnel card]`.
- Whether Z's four failure modes have ever occurred in the `_bus/` practice. No reader
  searched for them.
- Anything in Cartan's independent read. It had not arrived when this was written.
- The driller and cost chapters were read by a sub-reader in full and by Oraculum in
  part. Wave chapter 04 was read only by a sub-reader.
