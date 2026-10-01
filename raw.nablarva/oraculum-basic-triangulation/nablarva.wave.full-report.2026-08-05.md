# nabLarva — Wave full synthesized report

**Generated:** 2026-08-05

---

# nabLarva — Wave conversation export

**Date:** 2026-08-05  
**Status:** architecture and research synthesis; not an implementation specification  
**Source basis:** the shared triangulation brief and the subsequent Wave–majkee discussion  
**Purpose:** preserve the full conceptual current, including pushback, parked branches, and later-testable forks

## What this export contains

This report set preserves the evolution of the design rather than presenting only the last answer.

1. `01_ARCHITECTURE_ROOM_AND_BROKER.md`  
   The original clean-room architecture: peer sessions, brokered room, append-only journal, directed projections, private lines, anti-drift control, failure recovery, and V1 cut.

2. `02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md`  
   The output-cleaning discussion: hard prefilters, reversible tokenization, sparse vector/tensor representation, synchronization, transforms, and mathematical reconstruction.

3. `03_COST_COMPLEXITY_AND_STAGED_DECISION.md`  
   Practical resource cost, where the real complexity lies, and why the full generalized tokenizer engine is parked rather than discarded.

4. `04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md`  
   The “hacker” current: legitimate instrumentation, observable layers, skill/tool activation signals, controlled experiments, replay, and promotion of proven findings into production.

5. `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`  
   A durable ledger of decisions, objections, rejected shortcuts, parked ideas, unresolved questions, and possible later branches.

6. `06_ORACULUM_TRANSMISSION.md`  
   Message-ready text intended for transmission to Oraculum after the initial architecture proposal already sent.

7. `07_AI_HANDOFF.md`  
   A concise state handoff for another agent or a later development thread.

8. `nablarva.wave.full-report.2026-08-05.md`  
   A combined report containing all substantive chapters.

## Central synthesis

nabLarva should be understood as two related but distinct systems:

```text
PRODUCTION ROOM
    Independent agent sessions
          ↓
    thin session adapters
          ↓
    clean normalized events
          ↓
    brokered append-only room journal
          ↓
    sparse participant-specific views

RESEARCH LABORATORY
    controlled CLI scenarios
          ↓
    native events + PTY + OS observations
          ↓
    synchronized evidence bundle
          ↓
    replay and extractor comparison
          ↓
    proven versioned adapter rules
```

The production system should remain conservative and lightweight. The laboratory is where broad observation, experimental tokenization, statistical transforms, and alternative reconstruction strategies can be explored safely.

## Current design posture

The following are provisionally selected for V1:

- one central room broker per active room or host;
- independent live CLI sessions rooted in their own repositories;
- adapter-owned PTYs;
- append-only room journal;
- explicit addressing and recipient-filtered delivery;
- versioned goal and bounded consultation leases;
- immutable raw terminal capture;
- terminal-state normalization;
- narrow vendor profiles;
- a small stateful extraction layer;
- an experimental laboratory kept outside the production path.

The following are deliberately parked:

- dense tensor infrastructure;
- neural or embedding-based token classification;
- LLM-based output cleaning;
- a central `drillerd` service;
- a universal transformation language;
- full machine-level tracing during ordinary production use;
- automatic inference presented as certainty;
- interception of encrypted provider traffic.

## Governing principle

> Observe first. Preserve raw truth. Prefer declared semantic events. Infer conservatively. Promote only repeatable findings. Keep production smaller than the laboratory.


---

# 1. Core architecture — brokered rooms for independent terminal agents

## 1.1 Problem restatement

The required topology is not a parent agent spawning child agents. It is a room containing independent peers:

- one or more humans;
- two or more live terminal AI sessions;
- each session rooted in its own project directory;
- each session retaining its own repository context;
- all participants able to communicate without surrendering their independence.

The pilot case is an OpenCart-to-Laravel migration:

```text
OpenCart repository              Laravel repository
Claude/Codex session A           Claude/Codex session B
deep legacy knowledge            deep target-system knowledge
             \                    /
              \                  /
               human-supervised room
```

The room must support directed messages, private lines, read economy, anti-drift regulation, durable audit, clean text, cheap recovery, and later remote participants.

## 1.2 Foundational choice

The primary object should be an **append-only room event journal**, not a shared terminal transcript.

Every participant receives a filtered projection of that journal.

```text
OpenCart agent adapter ─┐
Laravel agent adapter ──┼── Unix socket ── larvad ── journal.ndjson
Human CLI ──────────────┘                      │
                                              ├── recipient projections
                                              ├── checkpoints
                                              ├── delivery cursors
                                              └── audit views
```

This architecture separates three concerns:

1. **Agent cognition and project context** stay inside each independent CLI session.
2. **Transport, addressing, ordering, and regulation** belong to the room broker.
3. **Terminal-specific interpretation** belongs to edge adapters.

nabLarva is therefore a communication substrate with regulation, not a meta-agent that decides what participants should think.

## 1.3 Components

### `larvad`: room broker

A small process owns ordering and room state.

Responsibilities:

- accept participant connections;
- identify participants;
- validate recipient sets;
- assign monotonic room sequence numbers;
- append accepted events;
- deliver events only to eligible recipients;
- track participant delivery cursors;
- enforce room and consultation state;
- render derived views.

Non-responsibilities:

- repository understanding;
- model prompting strategy;
- summarizing project code;
- deciding architectural truth;
- vendor-specific terminal parsing;
- semantic replacement of participant messages.

For same-machine V1, `larvad` listens on a Unix domain socket:

```text
$XDG_RUNTIME_DIR/nablarva/nablarva.sock
```

It can run in a `tmux` pane or foreground shell. A system daemon is not required.

### `larva`: human CLI

The human reads and writes through a small command-line client.

Illustrative commands:

```sh
larva send @all "Compare migration boundaries."
larva send @opencart --private "Check hidden order-status side effects."
larva tail
larva audit --all
larva consult open MIG-004 --blind --budget 8
larva consult extend MIG-004 4
larva checkpoint accept MIG-004
```

The room directory remains directly inspectable with ordinary text tools and Sublime Text.

### Agent adapters

One adapter owns one agent session:

```text
larva-agent-claude
larva-agent-codex
```

The adapter:

1. starts the CLI in a configured project directory;
2. owns its pseudo-terminal;
3. receives framed room messages;
4. injects those messages into the interactive session;
5. observes native events and terminal output;
6. extracts the meaningful result;
7. submits normalized events back to `larvad`.

The adapter is vendor-specific. The room protocol is not.

### Optional `tmux`

`tmux` is useful as:

- a process host;
- an emergency visual surface;
- a manual recovery tool;
- a familiar operator workspace.

It should not become the message protocol. `send-keys` and `capture-pane` are too tied to screen rendering to provide robust structured transport.

## 1.4 Durable state

A room may live under:

```text
$XDG_STATE_HOME/nablarva/rooms/<room-id>/
├── room.toml
├── participants.toml
├── goal.md
├── state.md
├── journal.ndjson
├── transcript.md
├── cursors/
│   ├── human-majkee.json
│   ├── agent-opencart.json
│   └── agent-laravel.json
├── adapters/
│   ├── agent-opencart.json
│   └── agent-laravel.json
└── raw/
    ├── agent-opencart/
    └── agent-laravel/
```

### Authoritative state

`journal.ndjson` is the room source of truth.

Properties:

- append-only;
- one writer;
- stable event IDs;
- monotonic sequence;
- replayable;
- diffable and inspectable;
- exportable into other stores later.

### Derived state

The following may be rebuilt:

- `transcript.md`;
- current `state.md`;
- catch-up summaries;
- participant views;
- delivery indexes;
- metrics.

### Repository relationship

Shared room state should not live by default inside either participant repository. Otherwise one project accidentally becomes the owner of the shared communication.

Accepted outcomes can later be exported deliberately to:

```text
ARCHITECTURE.md
DECISIONS.md
MIGRATION_PLAN.md
AI_HANDOFF.md
```

## 1.5 Event model

A message event might be:

```json
{
  "seq": 184,
  "id": "01K1E6MZ4Y6J9TM38W7V21QF9R",
  "time": "2026-07-31T19:42:11+02:00",
  "room": "opencart-laravel-migration",
  "kind": "message",
  "from": "agent:opencart",
  "to": ["agent:laravel"],
  "scope": "private",
  "goal_rev": 3,
  "consultation": "MIG-004",
  "reply_to": 181,
  "body": "The current admin writes stock history inside the order-status transition."
}
```

Useful kinds include:

```text
message
goal_changed
consultation_opened
consultation_phase_changed
consultation_paused
consultation_extended
checkpoint_draft
checkpoint_accepted
decision
participant_online
participant_offline
delivery_attempt
delivery_ack
extraction_warning
```

Control and conversational events share one order.

## 1.6 End-to-end message travel

Example: human privately asks the OpenCart agent a question.

```sh
larva send @opencart --private \
  "Does the old admin have side effects outside the order transaction?"
```

Flow:

1. `larva` creates a client event ID and sends the framed request.
2. `larvad` validates sender, recipient, scope, goal revision, and consultation.
3. The broker appends the event and assigns a sequence.
4. The eligibility projection includes only the OpenCart participant and audit-authorized views.
5. The OpenCart adapter receives a clean envelope.
6. The adapter injects a bounded prompt into its live session.
7. The adapter correlates the resulting output with the triggering event.
8. The extracted response returns to the broker with provenance.
9. The broker appends and routes the response according to explicit or inherited addressing.

Example injected envelope:

```text
[nabLarva · private from human:majkee · MIG-004 · message 185]

Does the old admin have side effects outside the order transaction?

Reply to the sender. Remain inside MIG-004.
```

The agent should not receive:

- its own prior output;
- unrelated messages;
- private lines addressed elsewhere;
- the entire room history.

## 1.7 Addressing and visibility

### Recipient forms

```text
@all
@human
@agents
@opencart
@opencart,@laravel
```

Named groups are expanded at append time. Historical recipient sets therefore remain stable if group membership changes later.

### Scope

```text
shared
private
```

A private event has exactly one recipient.

“Private” means absent from non-recipient live context and ordinary views. It does not mean hidden forever from the room owner, because full auditability is a requirement.

This is a context-visibility boundary in same-user V1, not a hostile-security boundary.

### Projection rule

Participant `P` receives event `E` when:

```text
E.seq > P.cursor
AND P ∈ E.to
AND E.from != P
AND E is not administratively held
```

Benefits:

- no self-replay;
- no irrelevant traffic;
- no accidental private-line leakage;
- cheap cursor-based continuation;
- sparse context delivery.

## 1.8 Anti-drift regulation

The system should regulate drift structurally rather than relying primarily on semantic policing.

### Versioned room goal

A room goal contains:

- objective;
- non-goals;
- constraints;
- required output;
- completion criteria.

Every consultation and agent message references a goal revision.

Changing the goal pauses active consultations until they are explicitly carried forward or reframed.

### Consultation lease

Agent-to-agent dialogue is bounded.

```sh
larva consult open MIG-004 \
  --question "Where should the transaction boundary move?" \
  --participants @opencart,@laravel \
  --budget 8 \
  --blind
```

A consultation has:

- one question;
- a participant set;
- a message budget;
- a goal revision;
- a phase;
- an owner.

When the budget is exhausted, further agent traffic is held. The human chooses:

```text
extend
reframe
decide
close
```

This creates real control points.

### Blind triangulation phases

#### Phase 1: independent positions

Each participant receives the same question without seeing the others’ answers.

Required structure:

- proposal;
- assumptions;
- project-specific evidence;
- principal risk.

#### Phase 2: simultaneous reveal

Held positions are released after all responses arrive or the human ends the phase.

#### Phase 3: bounded challenge

Participants may challenge evidence and assumptions within the remaining budget.

#### Phase 4: position closure

Each agent states:

- final recommendation;
- what changed;
- strongest unresolved disagreement;
- evidence needed to settle it.

The consultation pauses.

### Human-accepted checkpoint

A checkpoint records:

- goal revision;
- consultation question;
- accepted decisions;
- rejected alternatives;
- unresolved disputes;
- next action;
- journal sequence range.

It becomes authoritative only after human acceptance or edit. The raw history remains intact.

## 1.9 Failure and restart

### Agent session failure

Messages remain journaled.

On restart:

1. adapter resumes its identity;
2. broker reads the durable cursor;
3. latest visible checkpoint is delivered if context cannot be resumed;
4. only eligible events after that checkpoint are sent;
5. normal delivery continues.

### Delivery ambiguity

Exactly-once injection into an interactive terminal cannot be proved across crashes.

Use at-least-once delivery with stable message IDs and explicit states:

```text
queued
injected
responded
```

An unanswered injected message may be replayed with a clear marker.

### Broker failure

Because the broker is the only journal writer:

- adapters spool unsent outbound events;
- clients reconnect;
- broker truncates only an incomplete final NDJSON record;
- highest sequence is recovered;
- client IDs deduplicate submissions;
- derived files are rebuilt.

### Human observer absence

Observation is not ownership. `larva tail` resumes from a cursor.

### Remote extension

Keep one authoritative broker and transport framed events over SSH.

```text
remote adapter ── SSH channel ── central larvad
```

SSH supplies authentication, encryption, and familiar operations. No distributed consensus is required while one broker owns room order.

## 1.10 Version 1 cut

Recommended technology:

- Python 3 standard library;
- Unix domain sockets;
- `asyncio` or `selectors`;
- `pty`, `termios`, `subprocess`;
- framed JSON;
- append-only NDJSON;
- atomic cursor replacement;
- optional `tmux`;
- golden transcript tests.

Initial topology:

```text
one machine
one room
one human owner
two agent sessions
one Claude adapter
one Codex adapter
one active consultation at a time
```

Data structures should allow N participants even if the first interface is optimized for two agents.

Deferred:

- browser or Electron UI;
- autonomous workflow graph;
- vector database;
- automatic best-answer selection;
- hostile multi-user permissions;
- distributed broker replication;
- general plugin ecosystem;
- semantic drift model;
- full generalized driller infrastructure.

## 1.11 Contestable decisions

### Broker versus files/FIFOs only

**Choice:** one small broker.

**Reason:** addressing, ordering, fan-out, cursor replay, backpressure, and future remote sessions need a stateful coordinator.

**Strong objection:** the daemon adds lifecycle and a failure point.

**Response:** the complexity already exists; a broker makes it explicit rather than spreading it across locks, mailbox files, watchers, and races.

### Adapter-owned PTY versus attaching to arbitrary sessions

**Choice:** adapter owns the CLI session.

**Reason:** deterministic input correlation, clean extraction, and idle-state knowledge.

**Strong objection:** users lose some freedom and adapters become sensitive to CLI changes.

**Response:** keep adapters thin, versioned, fixture-tested, and capable of preferring native structured interfaces.

### NDJSON versus SQLite

**Choice:** NDJSON journal for V1.

**Reason:** direct inspection, streaming, replay, simple single-writer recovery.

**Strong objection:** SQLite gives transactions, indexes, and queryability cheaply.

**Response:** migration to an append-only SQLite event table remains possible if room size or query complexity earns it.

## 1.12 Architectural invariant

> One immutable room history, many sparse participant views, and human-owned control over when agent exchange continues.


---

# 2. Driller, tokenization, synchronization, and reconstruction

## 2.1 Evolution of the idea

The output-cleaning discussion moved through three formulations.

### Initial formulation

The CLI emits volatile decorative and process output. Hard prefilters can remove known UI patterns. A further “driller” would tokenize the remaining stream and produce clean output through mathematical filtering.

### First Wave pushback

The term “tokenizer” appeared too narrow if understood as ordinary linguistic tokenization. A tokenizer that merely splits words cannot distinguish a spinner rewritten forty times from stable answer text.

The proposed correction was:

> The driller is a stateful temporal segmenter and classifier that may use tokenization as one instrument.

### Majkee’s clarification

The intended tokenizer was not merely lexical. The complete agent-output stream would be encoded into structured tokens, forming a vector or tensor-like representation. That representation would pass through filtering and synchronization transforms, producing another representation from which clean output would be rebuilt mathematically.

With that clarification, the stronger formulation became:

> The driller is an analysis–transform–synthesis engine whose substrate is a reversible structured token space.

The pushback therefore refined the idea; it did not invalidate it.

## 2.2 The observed object

A terminal agent does not emit a simple list of final text lines.

It emits a time-varying terminal field:

```text
bytes × time × screen position × interaction phase
```

A status line may repeatedly overwrite one row:

```text
⠋ Thinking
⠙ Thinking
⠹ Reading file
⠸ Reading file
```

A final answer may grow monotonically:

```text
"The old"
"The old system"
"The old system writes"
"The old system writes stock history..."
```

These trajectories differ in:

- persistence;
- rewrite rate;
- prefix continuity;
- spatial behavior;
- structural coherence;
- relation to the injected prompt;
- interaction phase.

The driller should preserve those dimensions long enough to distinguish them.

## 2.3 Analysis–transform–synthesis model

```text
raw terminal stream
        │
        ▼
reversible tokenizer / encoder
        │
        ▼
structured token sequence
        │
        ▼
filtering + synchronization transforms
        │
        ▼
transformed token sequence or graph
        │
        ▼
decoder / reconstructor
        │
        ▼
clean logical output
```

Notation:

\[
x \xrightarrow{E} T_x \xrightarrow{F} T_y \xrightarrow{D} y
\]

Where:

- \(x\): raw or normalized terminal stream;
- \(E\): encoder/tokenizer;
- \(T_x\): structured source representation;
- \(F\): filtering, contraction, synchronization, and grouping;
- \(T_y\): transformed representation;
- \(D\): reconstruction;
- \(y\): clean message.

A critical invariant before filtering is:

\[
D(E(x)) \approx x
\]

For a normalized terminal representation, the ideal is:

\[
D(E(x)) = x
\]

Then intentional transformation is explicit:

\[
D(F(E(x))) = y
\]

This separates information accidentally lost during encoding from information deliberately suppressed or reorganized.

## 2.4 Token definition

A useful token is not necessarily a word. It is an observed event or span with metadata.

Conceptually:

\[
t_i =
(
content,
type,
time,
position,
mutation,
phase,
source,
confidence
)
\]

Example:

```json
{
  "value": "Thinking",
  "lexical_type": "word",
  "terminal_row": 23,
  "terminal_column": 4,
  "first_seen": 1842.14,
  "last_seen": 1842.31,
  "mutation_count": 7,
  "operation": "replace",
  "session_phase": "processing",
  "vendor_marks": ["status-line"]
}
```

Stable answer span:

```json
{
  "value": "The legacy controller commits before updating stock.",
  "lexical_type": "prose-span",
  "terminal_row": 14,
  "first_seen": 1844.02,
  "last_seen": 1848.11,
  "mutation_count": 0,
  "operation": "append",
  "session_phase": "answer",
  "vendor_marks": []
}
```

## 2.5 Vector and tensor interpretation

A token feature vector may be:

\[
v_i =
[
e_{text},
e_{type},
\Delta t,
x,
y,
rewrite,
persistence,
phase,
confidence
]
\]

A sequence is:

\[
V = [v_1, v_2, \dots, v_n]
\]

With multiple axes:

\[
T[time, position, token, feature]
\]

The tensor language is conceptually valid, but implementation should remain sparse. Terminal mutations are sparse events, not a reason to allocate a dense multidimensional array.

Practical representation:

```text
Token {
    text
    operation
    row
    column
    first_seen
    last_changed
    rewrite_count
    persistence
    phase
    annotations
    source_range
}
```

Tensor-like transforms can operate over event sequences without PyTorch or dense matrices.

## 2.6 Multiple token resolutions

One tokenization layer is unlikely to be sufficient.

```text
Layer 1: terminal operations
Layer 2: visible character spans
Layer 3: lexical tokens
Layer 4: structural blocks
Layer 5: conversational units
```

Example:

```text
terminal replace event
      ↓
visible span
      ↓
status-line token group
      ↓
processing-state block
      ↓
non-answer conversational unit
```

Each layer answers a different question:

- terminal token: how the screen changed;
- lexical token: what the text contains;
- structural token: whether it belongs to prose, code, diff, table, or error;
- conversational token: which nabLarva input it answers.

## 2.7 Proposed pipeline boundaries

```text
PTY byte stream
      │
      ▼
1. Terminal decoder
      │
      ▼
2. Vendor prefilter annotations
      │
      ▼
3. Driller transforms
      │
      ▼
4. Output gate
      │
      ▼
CleanMessage + provenance
```

### Terminal decoder

Responsibilities:

- UTF-8 boundaries;
- ANSI control sequences;
- carriage-return replacement;
- cursor movement;
- erase operations;
- alternate screen handling;
- terminal resize;
- partial lines;
- scroll history.

It should reconstruct terminal state rather than merely strip escape bytes.

### Vendor prefilters

Hard-coded rules belong in versioned adapter profiles.

Examples:

- known status region;
- spinner class;
- prompt marker;
- command echo;
- token counter;
- permission prompt;
- tool-call heading.

Important design choice:

> Prefilters annotate first; they do not immediately delete.

A changed UI may cause a rule to misclassify meaningful text. Annotation preserves later review and multi-signal correction.

### Driller

The driller turns normalized observations into stable groups:

```text
terminal mutations
    → persistent spans
    → atoms
    → blocks
    → conversational output groups
```

Possible group classes:

```text
assistant_answer
code_block
tool_command
tool_result
progress
prompt
input_echo
warning
error
status
unknown
```

### Output gate

The final policy decides:

```text
PASS
SUPPRESS
HOLD_UNKNOWN
PASS_WITH_WARNING
```

The gate should be more conservative for errors and warnings than for visual decoration.

## 2.8 Mathematical transforms

### Temporal persistence

\[
persistence = \frac{stable\ duration}{observed\ duration}
\]

Stable prose gains weight. Rapidly rewritten status text loses weight.

### Rewrite rate

\[
rewriteRate = \frac{changes}{second}
\]

High rewrite rate at a fixed position suggests UI state, but should not alone suppress content.

### Prefix continuity

For partial answer growth:

\[
continuity(t_i,t_{i+1}) =
\frac{LCP(t_i,t_{i+1})}{\max(|t_i|,|t_{i+1}|)}
\]

High continuity plus increasing length suggests progressive construction.

Contraction:

\[
[t_1,t_2,t_3,t_4] \rightarrow [t_4]
\]

### Spatial stability

Fixed bottom-row or right-aligned regions are likely UI surfaces. Normal answer text usually advances through scroll flow.

This is a feature, not an absolute rule.

### Structural coherence

Protect:

- code fences;
- diffs;
- stack traces;
- JSON;
- Markdown lists;
- tables;
- errors.

A broad repetition filter must not destroy repeated code lines or tabular data.

### Interaction phase

The adapter can track:

```text
idle
message injected
agent processing
tool active
answer emerging
prompt returned
```

Tokens are synchronized to a nabLarva message epoch.

```text
room message 185
      ↓
terminal output epoch 185
      ↓
clean response event 186
```

This synchronization is often stronger than text-only inference.

## 2.9 Soft mask model

A simple score may combine features:

\[
q_i =
w_pP_i +
w_mM_i +
w_sS_i +
w_lL_i +
w_cC_i -
w_rR_i -
w_uU_i
\]

Where:

- \(P_i\): persistence;
- \(M_i\): monotonic growth;
- \(S_i\): structural coherence;
- \(L_i\): relation to latest input;
- \(C_i\): continuity with neighbors;
- \(R_i\): rewrite frequency;
- \(U_i\): UI likelihood.

A sigmoid or bounded mapping gives:

\[
m_i = \sigma(q_i)
\]

Conceptually:

\[
T_y = M \odot T_x
\]

But low score should not automatically mean deletion. The practical output classes remain:

```text
pass
suppress
merge
hold
unknown
```

## 2.10 Reconstruction graph

Some transforms are many-to-one or one-to-many. A graph is safer than pretending every result is a flat vector.

Example instructions:

```text
BEGIN_PARAGRAPH
TEXT("The transaction boundary...")
SPACE
TEXT("must remain...")
END_PARAGRAPH

BEGIN_CODE_BLOCK(language="php")
TEXT("$db->commit();")
NEWLINE
TEXT("$this->updateStock();")
END_CODE_BLOCK
```

The decoder linearizes typed structure instead of guessing formatting after destructive cleaning.

## 2.11 Provenance and dual truth

The driller must produce two truths:

```text
raw capture       — what the terminal emitted
clean projection  — what enters the room
```

Never overwrite raw capture.

A clean event should include provenance:

```json
{
  "text": "The migration should preserve the existing status transition.",
  "extractor": {
    "profile": "claude-code-2026.08-a",
    "driller": "0.3",
    "raw_start": 8127,
    "raw_end": 8459,
    "confidence": 0.94
  }
}
```

This enables:

- deterministic replay;
- new-filter comparison;
- debugging missing text;
- re-drilling old captures;
- version regression analysis;
- human inspection.

## 2.12 `unknown` as a first-class state

A binary model is unsafe:

```text
content | noise
```

Use:

```text
content | noise | unknown
```

Illustrative thresholds:

```text
confidence ≥ 0.90  → pass automatically
0.60–0.90         → pass with uncertainty or hold by policy
< 0.60            → retain as unknown
```

Thresholds should be empirical and class-sensitive. Errors deserve a stronger preservation bias than progress indicators.

## 2.13 Architectural placement

The driller belongs close to the PTY, inside or adjacent to the adapter.

```text
Agent CLI
   │
   ▼
Adapter
   ├── PTY capture
   ├── terminal decoder
   ├── vendor profile
   ├── driller
   └── clean event emitter
             │
             ▼
           larvad
```

Reasons:

- access to raw timing and cursor mutations;
- session-local phase state;
- failure isolation;
- lower traffic;
- no vendor knowledge in the broker.

Possible placements:

### V1: embedded in adapter

Simplest and preferred initially.

### Later: worker per agent

Useful if extraction can crash or stall independently. Raw capture remains alive while the worker restarts.

### Only if earned: host-level `drillerd`

Potentially useful if a substantial shared model must be loaded once. Otherwise it adds a daemon, multiplexing, raw-output transport, backpressure, and shared failure.

## 2.14 Corrected final formulation

> The driller encodes terminal reality into a reversible structured token space, transforms that space through temporal, spatial, structural, and conversational operators, and reconstructs a cleaner output sequence with retained provenance.

This is the complete concept. Its full generalized implementation is parked for later evidence, not rejected as incoherent.


---

# 3. Practical cost, complexity, and staged implementation decision

## 3.1 Direct judgment

The concept contains a valuable kernel, but the maximal generalized form is premature for nabLarva V1.

The likely runtime cost is trivial.

The likely engineering and validation cost is not trivial.

Therefore:

> Keep the stateful extraction concept. Implement only the smallest proven subset. Use experiments to decide whether a richer tokenizer-transform-reconstructor has earned its place.

## 3.2 Runtime cost

Agent terminal output is small compared with media processing, database analytics, compilation, or model inference.

A deterministic pass over bytes or terminal mutations is approximately:

\[
O(n)
\]

where \(n\) is the captured byte or event count.

For a typical turn containing tens or hundreds of kilobytes of raw PTY traffic, rough unbenchmarked orders of magnitude are:

| Processing layer | Expected latency | Memory tendency |
|---|---:|---:|
| UTF-8 and ANSI decoding | sub-ms to a few ms | small |
| terminal-state reconstruction | sub-ms to a few ms | screen-sized |
| exact vendor rules | negligible | negligible |
| rewrite contraction | low milliseconds | bounded recent history |
| simple statistical scoring | low milliseconds | small |
| local embedding model | tens to hundreds of ms | hundreds of MB |
| local LLM cleaner | much higher | model-dependent |
| remote LLM cleaner | network/model latency | external cost |

These are not measurements. They define the likely scale.

For two or ten deterministic adapters, a normal development machine should barely notice the processing. The agent CLIs and their tools will dominate CPU, memory, and latency.

## 3.3 What is not needed for V1

The implementation does not need:

- GPU;
- CUDA;
- TensorFlow;
- PyTorch;
- dense tensor allocation;
- central inference server;
- SIMD optimization;
- model embeddings;
- another LLM pass.

A sparse event sequence with ordinary structs is sufficient.

The mathematical model can be tensor-like without forcing a machine-learning stack.

## 3.4 Where the true cost lives

### Ground-truth creation

You need captured sessions paired with approved clean outputs.

Without this, there is no evidence that a sophisticated system improves on narrow rules.

### Vendor volatility

CLI versions may change:

- cursor strategy;
- status placement;
- prompt shape;
- tool rendering;
- alternate-screen use;
- permission dialogs;
- final-answer boundaries.

### False-negative risk

Retained noise is annoying.

Lost meaningful text is dangerous.

A sophisticated filter may become less trustworthy precisely because its decisions are harder to explain.

### Structural ambiguity

Legitimate answers may contain:

- ANSI demonstrations;
- prompts;
- progress output;
- repeated lines;
- terminal traces;
- diffs;
- stack traces;
- tables;
- raw tool chatter being discussed as evidence.

A general heuristic can delete valid content.

### Reconstruction validation

Every split, merge, reorder, contraction, and suppression rule expands the regression surface.

Runtime remains cheap while correctness work grows.

## 3.5 Appropriate senior-programmer response

Two simplistic reactions should both be rejected.

### Too narrow

> Use only a few regexes. Everything else is unnecessary.

This ignores terminal state, cursor rewrites, turn synchronization, and future vendor variation.

### Too expansive

> Build a universal tensor-driven semantic reconstruction engine first.

This commits the project to a research subsystem before observing actual failures.

### Better response

> Preserve the raw stream, reconstruct real terminal semantics, apply narrow deterministic rules, measure residual failures, and add stateful or statistical mechanisms only where recorded evidence justifies them.

Hard-coded rules are not primitive when they encode a real protocol boundary.

A rule based on:

```text
rapidly rewritten fixed terminal region during active turn
```

is more durable than:

```regex
/^Thinking/
```

## 3.6 Recommended V1 extraction stack

```text
Raw PTY capture
      │
      ▼
Terminal normalization
      │
      ▼
Exact adapter profile
      │
      ▼
Small stateful driller
      │
      ▼
Conservative output gate
```

### Raw capture

Immutable, timestamped, replayable.

### Terminal normalization

Understand terminal operations rather than treating output as plain lines.

### Exact profile

Known prompt, status, spinner, echo, and tool patterns. Rules annotate before suppression.

### Small stateful driller

Implement only:

- collapse repeated replacements;
- retain final stable state;
- remove confirmed input echo;
- bind output to injected message epoch;
- detect prompt return;
- preserve code blocks and errors;
- route uncertainty to `unknown`.

### Conservative gate

Prefer some retained noise over silent loss.

## 3.7 Process and memory model

Per agent:

- one adapter process;
- one PTY;
- one virtual terminal state;
- one bounded event ring;
- one append-only raw spool;
- one small extraction state machine.

Likely footprint: a few to tens of megabytes depending on buffers and parser implementation.

CPU: effectively negligible relative to the agent session.

The PTY reader should not block on extraction.

```text
PTY reader
  ├── append raw event
  └── enqueue bounded work
             │
             ▼
          driller
```

If the driller falls behind:

1. continue raw capture;
2. spill to local spool;
3. delay clean delivery;
4. emit extractor health state;
5. never discard silently.

## 3.8 The experiment that decides further investment

Build a corpus covering:

```text
ordinary prose answer
code-heavy answer
tool-heavy answer
permission prompt
warning and error
interrupted response
terminal resize
CLI restart
long-running command
nested shell output
skill invocation
MCP tool
CLI version change
```

For each case:

```text
raw capture
expected clean output
actual output
extractor version
profile version
human notes
```

Compare:

### Baseline A

Terminal normalization only.

### Baseline B

Normalization plus hard rules.

### Candidate C

Normalization, hard rules, and small stateful/statistical driller.

### Later Candidate D

Full reversible tokenizer-transform-reconstructor.

Metrics:

- meaningful text lost;
- noise retained;
- incorrect turn boundaries;
- manual correction count;
- processing latency;
- profile breakage after CLI update;
- unexplained suppression;
- replay determinism.

Primary metric:

> How often did the extractor lose meaningful content?

If Baseline B or C solves almost all real cases safely, stop.

## 3.9 Promotion criteria for the richer tokenizer

The fuller engine is justified when evidence shows at least one of:

- multiple adapters duplicate the same stateful logic;
- vendor hard rules break frequently;
- line-based processing cannot represent the terminal trajectories;
- residual failures have repeatable statistical structure;
- replaying historical captures produces operational value;
- human correction volume becomes material;
- clean-output errors affect architectural decisions.

Until then, keep the conceptual design and defer the generalized implementation.

## 3.10 Parked, not rejected

Parked for later:

```text
dense tensor representation
embedding each token
neural classification
LLM cleaning pass
general transform DSL
central drillerd
automatic semantic reconstruction
```

They remain valid research branches if the corpus proves a need.

## 3.11 Decision

The selected direction is:

```text
hard facts first
terminal semantics second
small stateful statistics third
semantic intelligence only after evidence
```

The idea is not a dead alley. The dead alley would be allowing the cleaning subsystem to become the main project before the room itself exists.


---

# 4. Testing laboratory, legitimate hacker method, and observability

## 4.1 Meaning of “hacker” in this project

The intended hacker stance is not intrusion or policy bypass.

It is:

> Treat the CLI as an unknown machine. Stimulate it with controlled inputs. Observe every boundary legitimately available on the owned system. Correlate independent signals. Infer only what the evidence supports.

The laboratory exists to discover the machine’s real behavior before production architecture hardens around terminal guesses.

## 4.2 Why the laboratory changes the design

A terminal screen is the outermost and often least semantic layer.

The system should prefer higher-quality signals when available:

```text
native lifecycle event
        ↓ unavailable
structured vendor event stream
        ↓ unavailable
local process/file/tool observation
        ↓ unavailable
PTY reconstruction
        ↓
statistical inference
```

This leads to a key architectural refinement:

> The driller is not the universal first interpreter. It is the fallback and correlation engine after native and structured signals have been considered.

## 4.3 Observable layers

```text
┌──────────────────────────────────────────────┐
│ Provider internals                          │ mostly opaque
├──────────────────────────────────────────────┤
│ Server-side model/context assembly          │ partly or not observable
├──────────────────────────────────────────────┤
│ Agent lifecycle: turns, tools, skills       │ sometimes natively observable
├──────────────────────────────────────────────┤
│ Child processes, files, MCP, sockets        │ locally observable
├──────────────────────────────────────────────┤
│ Structured JSON/event interfaces            │ strongly observable if offered
├──────────────────────────────────────────────┤
│ PTY rendering                               │ observable but noisy
└──────────────────────────────────────────────┘
```

The exact available signals depend on CLI version and invocation mode. They must be verified experimentally and documented in a capability profile.

## 4.4 Skill activation and tool behavior

A laboratory question might be:

> When a CLI automatically consumes a skill, what machine events occur and which of them reliably prove activation?

Possible evidence:

- native skill lifecycle event;
- structured input item naming a skill;
- `SKILL.md` read;
- bundled script execution;
- characteristic tool sequence;
- prompt expansion;
- process creation;
- final answer structure.

Important distinction:

```text
observed:  SKILL.md was opened
inferred:  the skill was probably activated
known:     a native semantic event declared activation
unknown:   the model's private reason for selecting it
```

A file read alone does not prove semantic activation. The CLI may be scanning, caching, listing, validating, or loading metadata.

## 4.5 Machine-level observations

On a machine controlled by the user, the laboratory may observe the scoped process tree.

### Process topology

Capture:

- CLI process;
- child shells;
- tool subprocesses;
- MCP servers;
- executable paths;
- working directories;
- arguments;
- start and exit times.

Example:

```text
claude
 ├─ bash -lc "php artisan test"
 │   └─ php artisan test
 └─ node mcp-server-filesystem
```

This proves local execution, not the model’s hidden rationale.

### File activity

Observe:

- skill instruction reads;
- rule/config loading;
- bundled script access;
- temporary files;
- patch writes;
- repository changes;
- transcript output.

Attribution matters. A filesystem watcher may show that a path changed but not which process caused it.

### System calls

For controlled experiments, scoped tracing may observe:

```text
execve
openat
read
write
connect
clone
wait
exit
```

This is useful for mapping behavior but too noisy and intrusive for normal production.

### Network metadata

Potentially observable:

- destination;
- connection timing;
- duration;
- byte counts;
- MCP endpoints.

The laboratory should not depend on intercepting encrypted provider traffic. That is brittle, risky, and unnecessary when legitimate structured boundaries exist.

## 4.6 Opaque or unknowable layers

Do not promise visibility into:

- hidden system prompts;
- server-side routing;
- provider classifiers;
- speculative model branches;
- private chain-of-thought;
- server-side context assembly not exposed by the vendor;
- internal cache behavior;
- the private reason a model selected one skill;
- hidden telemetry.

The observation system must encode epistemic status:

```text
confirmed
observed
correlated
inferred
unknown
```

## 4.7 Separation of laboratory and production

```text
LABORATORY                         PRODUCTION
──────────                         ──────────
broad observation                  minimal proven instrumentation
optional syscall tracing           no routine syscall tracing
multiple extractors                one selected conservative path
experimental features              stable normalized events
hypothesis generation              deterministic behavior
raw research data                  bounded operational state
```

The laboratory may be large. Production should remain small.

## 4.8 Laboratory components

Suggested conceptual subsystem:

```text
nabLarva laboratory
├── probe       capture observable signals
├── fixture     define controlled scenarios
├── replay      run extractors over immutable captures
├── compare     calculate diffs and metrics
├── annotate    add human ground truth
└── promote     export proven adapter profiles/rules
```

Possible command surface:

```sh
larva-lab run experiments/skill-implicit.toml
larva-lab replay captures/<id> --extractor hard-v1
larva-lab replay captures/<id> --extractor driller-v2
larva-lab compare captures/<id> expected.md
larva-lab promote captures/<set> codex-2026.08
```

## 4.9 Experiment bundle

One run should produce a synchronized, reproducible bundle:

```text
experiment/
├── manifest.toml
├── prompt.txt
├── environment.json
├── versions.json
├── pty.raw
├── terminal-events.ndjson
├── native-events.ndjson
├── processes.ndjson
├── files.ndjson
├── network.ndjson
├── syscalls/
├── expected.md
├── observations.md
└── conclusion.md
```

The manifest should identify:

- CLI name and exact version;
- command-line mode;
- adapter version;
- repository fixture commit;
- terminal dimensions;
- enabled skills;
- MCP configuration;
- environment allowlist;
- experiment question;
- expected signal;
- redaction policy.

## 4.10 Example skill experiment matrix

Hypothesis:

> Reading `SKILL.md` after the user prompt indicates skill activation.

Experiments:

1. start CLI with skill installed but do not mention it;
2. list available skills without using one;
3. invoke skill explicitly;
4. request a task that should trigger implicit selection;
5. request a near-match that should not trigger it;
6. invoke another skill with similar description;
7. repeat after warm cache;
8. repeat after process restart;
9. repeat under different CLI version.

Possible conclusion:

```text
startup read                     → discovery
menu/list read                   → enumeration
post-prompt read + native event  → confirmed activation
post-prompt read + bundled tool  → strongly correlated activation
cached run without read          → file observation alone insufficient
```

## 4.11 Behaviour mapping versus extractor evaluation

### Behaviour mapping

Discover:

- turn start and end;
- skill discovery;
- explicit and implicit activation;
- instruction loading;
- tool request and completion;
- child-process lifecycle;
- file reads/writes;
- context compaction;
- interruption and retry;
- prompt boundaries;
- agent answer boundaries.

### Extractor evaluation

Run identical captures through:

```text
terminal normalization only
hard filters
stateful driller
statistical scorer
full tokenizer/reconstructor
experimental semantic classifier
```

Compare against approved output.

## 4.12 Promotion rule

A discovery enters production only when it has:

1. repeatable fixture;
2. precise signal definition;
3. supported CLI/version scope;
4. known failure case;
5. conservative fallback;
6. regression test;
7. provenance and redaction review.

Weak finding:

```text
The last terminal row is usually a status bar.
```

Promotable rule:

```text
For CLI version family X, while a turn is active, a fixed-width
alternate-screen bottom row is repeatedly replaced and disappears
before prompt return. Mark as status. Preserve as unknown when it
contains an error-class signal.
```

## 4.13 Normalized event vocabulary

Multiple sources should converge into a vendor-neutral vocabulary:

```text
turn_started
turn_completed
skill_discovered
skill_activated
instruction_loaded
tool_requested
tool_started
tool_completed
file_read
file_changed
subprocess_started
subprocess_completed
assistant_text
prompt_returned
unknown_activity
```

Each event records source and confidence.

Example:

```json
{
  "time": 1785872462.117,
  "session": "codex-17",
  "source": "syscall",
  "kind": "file_read",
  "path": "/project/.agents/skills/migration-review/SKILL.md",
  "pid": 28413,
  "certainty": "observed"
}
```

Derived inference:

```json
{
  "time": 1785872462.121,
  "session": "codex-17",
  "source": "correlator",
  "kind": "skill_activated",
  "skill": "migration-review",
  "confidence": 0.91,
  "certainty": "inferred",
  "evidence": [812, 813, 814]
}
```

## 4.14 Security and privacy boundary

The probe must be scoped to:

- processes launched by the adapter;
- repositories owned by the user;
- explicitly configured tools and MCP servers;
- experiment-specific sandboxes.

Redact by default:

```text
API keys
authorization headers
environment secrets
auth files
cookies
SSH agent material
private tokens
full provider request payloads
```

The laboratory should record an environment allowlist rather than dump the entire process environment.

## 4.15 New impulses worth testing later

### Capability handshake

Each adapter could publish:

```json
{
  "native_turn_events": true,
  "native_skill_events": false,
  "structured_output": true,
  "pty_required": true,
  "process_observation": "lab-only"
}
```

The production pipeline then chooses the strongest available signal rather than assuming one universal path.

### Shadow extraction

A candidate extractor runs beside production but cannot affect delivered messages.

```text
raw capture
   ├── production extractor → room
   └── shadow extractor     → metrics only
```

After sufficient comparison, it may be promoted.

### Differential mutation tests

Take real captures and mutate:

- terminal width;
- timing;
- spinner text;
- prompt wording;
- chunk boundaries;
- ANSI ordering;
- Unicode width.

The rule should survive irrelevant mutations and fail visibly on unsupported ones.

### Error bypass lane

Warnings, permission prompts, failures, and stack traces should bypass aggressive suppression. Losing an error is more damaging than forwarding some noise.

### Semantic checksum

A later research metric could compare the clean output with stable raw spans to detect unexplained disappearance. This should remain advisory, not authoritative.

### Version drift alarm

When an adapter observes unknown UI structure or a CLI version outside its tested profile, it should downgrade confidence and produce a laboratory capture request rather than silently adapting.

## 4.16 Laboratory invariant

> The laboratory may infer broadly, but production may act only on evidence that is versioned, replayable, conservative, and reversible.


---

# 5. Decision ledger, pushback alleys, parked branches, and forks

## 5.1 Purpose

This ledger prevents useful rejected or deferred ideas from disappearing.

Status vocabulary:

- **Selected:** current preferred direction.
- **Provisional:** selected pending experiments.
- **Parked:** coherent but not justified for V1.
- **Rejected for V1:** actively excluded from the first implementation.
- **Open:** unresolved.
- **Laboratory only:** valid for experiments, not ordinary runtime.

## 5.2 Core room architecture

| Topic | Status | Decision | Why | Strong counterargument |
|---|---|---|---|---|
| Room authority | Selected | Append-only room journal | durable ordering, audit, replay | SQLite may be simpler for queries |
| Coordinator | Selected | Small broker (`larvad`) | explicit routing, cursors, backpressure | adds daemon/process lifecycle |
| Agent topology | Selected | Independent peer sessions | preserves project-rooted contexts | harder than subagents |
| Session control | Provisional | Adapter owns PTY | correlation and extraction | brittle across CLI updates |
| Human UI | Selected | CLI + files + optional `tmux` | Unix-native, inspectable | less polished than web UI |
| Remote extension | Provisional | SSH transport to one broker | avoids new security protocol | central broker remains bottleneck |
| Privacy | Selected for V1 | recipient context boundary + full owner audit | satisfies private lines and audit | not hostile-user secrecy |
| Read economy | Selected | sparse recipient projections and cursors | saves context | checkpoint quality becomes important |

## 5.3 Anti-drift

| Topic | Status | Decision | Why | Counterargument |
|---|---|---|---|---|
| Goal anchor | Selected | versioned human-owned goal | explicit authority | administrative overhead |
| Agent dialogue | Selected | consultation message budgets | creates real stop points | may interrupt useful flow |
| Blind triangulation | Selected for important questions | independent answer then reveal | reduces anchoring | slower interaction |
| Closure | Selected | final position + unresolved evidence | durable convergence | agents may still frame strategically |
| Checkpoint authority | Selected | human acceptance required | avoids silent AI truth mutation | human becomes throughput bottleneck |
| Semantic drift detector | Parked | embeddings/LLM classifier | may detect subtle drift | probabilistic control over clear structural problem |

## 5.4 Output extraction evolution

### Original hard-filter-only alley

**Status:** insufficient as a complete doctrine.

Value:

- simple;
- deterministic;
- cheap;
- easy to inspect.

Weakness:

- vendor wording changes;
- terminal rewrite semantics are lost;
- prompt boundaries may be ambiguous;
- regexes can delete legitimate examples.

Preserved as:

- first adapter profile layer;
- baseline in laboratory comparisons.

### Driller as ordinary linguistic tokenizer

**Status:** rejected interpretation.

Reason:

- word/subword tokenization alone does not model cursor movement, time, persistence, or turn phase.

### Driller as temporal segmenter/classifier

**Status:** preserved but superseded by richer clarification.

Value:

- recognizes state and trajectories;
- avoids line-only model.

### Reversible structured tokenizer and mathematical reconstruction

**Status:** conceptually accepted; generalized implementation parked.

Value:

- supports multi-resolution representation;
- separates encoding loss from intentional filtering;
- makes replay and transformation explicit;
- can combine time, position, structure, and phase.

Why parked:

- no corpus yet;
- unclear residual failure rate;
- larger validation surface;
- likely unnecessary for V1.

### Small stateful driller

**Status:** provisional V1.

Allowed scope:

- rewrite contraction;
- stable final-state selection;
- input-echo removal;
- turn/epoch correlation;
- prompt-return detection;
- structural preservation;
- unknown lane.

## 5.5 Representation choices

| Idea | Status | Notes |
|---|---|---|
| sparse event sequence | Selected | practical implementation substrate |
| dense tensor | Rejected for V1 | conceptual model does not require dense memory |
| feature vectors | Provisional | simple numerical scoring may be useful |
| reconstruction graph | Parked/partial | useful if structure becomes complex |
| hard deletion by regex | Rejected as default | annotate first, suppress later |
| unknown classification | Selected | protects against destructive certainty |
| provenance ranges | Selected | enables replay and debugging |
| raw capture as authority | Selected | clean transcript remains derived |

## 5.6 Resource choices

| Idea | Status | Reason |
|---|---|---|
| embedded deterministic extraction | Selected | low latency, no extra service |
| worker per adapter | Parked | useful if isolation becomes necessary |
| central `drillerd` | Rejected for V1 | shared failure and moving parts |
| GPU/model inference | Rejected for V1 | no demonstrated need |
| LLM cleaner | Rejected for V1 | cost, latency, non-determinism, possible semantic mutation |
| embeddings | Parked | only if residual patterns justify |
| Python standard library | Provisional V1 | rapid experiment and PTY support |
| Rust rewrite | Parked | only after real reliability/performance pressure |

## 5.7 Hacker/observability alleys

### Terminal-only observation

**Status:** rejected as exclusive strategy.

Reason:

- throws away stronger semantic signals;
- forces inference where native events may exist.

### Native and structured events first

**Status:** selected principle.

Order:

```text
native semantic event
structured event stream
OS-local observation
PTY reconstruction
statistical inference
```

### System-call tracing

**Status:** laboratory only.

Value:

- process/file/network behavior mapping;
- version characterization;
- skill/tool activation experiments.

Reason not production:

- volume;
- overhead;
- permissions;
- secrets;
- fragile interpretation.

### Network interception

**Status:** rejected.

Reason:

- credential and privacy risk;
- encrypted private protocol;
- likely policy/compatibility issues;
- unnecessary for room objective.

### Skill activation inference

**Status:** provisional.

Rule:

- native declaration = confirmed;
- correlated file/tool events = inferred;
- file read alone = observed but ambiguous.

## 5.8 Laboratory decision

| Topic | Status | Decision |
|---|---|---|
| Separate lab | Selected | prevent research complexity entering production |
| Immutable captures | Selected | enable replay and comparison |
| Ground-truth expected output | Selected | required for extractor evaluation |
| Promotion gate | Selected | fixture + scope + failure + fallback + test |
| Shadow mode | Valuable later fork | compare without affecting room |
| Mutation testing | Valuable later fork | test resilience to irrelevant UI changes |
| Version capability profile | Valuable later fork | choose strongest signal per CLI |

## 5.9 Open questions

### Session attachment

Must adapters always launch sessions, or may a later version attach to already-running sessions through official APIs?

### Native structured modes

Can normal interactive UX be preserved while obtaining reliable structured lifecycle events, or will adapters need to run a different headless/app-server mode?

### Tool chatter visibility

Should the room transport only final answers, or also normalized evidence events such as:

```text
tool_started
tests_failed
file_changed
permission_required
```

A likely answer is two lanes:

```text
conversation lane
evidence/status lane
```

The human may subscribe to both; agents receive only what the consultation requires.

### Private-line audit timing

Should the owner see private traffic only on explicit audit, or receive a discreet existence indicator in real time without content?

### Checkpoint generation

Should checkpoints be manually written, mechanically templated from final positions, or drafted by a dedicated summarizer and then human-approved?

### Raw-capture retention

How long should raw PTY and laboratory captures remain? The answer affects disk use, privacy, and reproducibility.

### Failure policy

When extraction confidence is low, should the room:

- delay delivery;
- deliver with warning;
- include a raw fallback;
- ask the sender/owner for review?

## 5.10 Later forks worth preserving

### Fork A: evidence lane

Separate final conversational prose from machine evidence:

```text
assistant message:
"The transaction should include stock history."

evidence events:
- file `order.php` read
- test `OrderTransitionTest` failed
- command exited 1
```

This may improve auditability without polluting agent context.

### Fork B: adapter capability negotiation

At session start, adapters declare supported signals and tested versions. The broker records the capability snapshot with every room run.

### Fork C: extractor shadow deployment

Run candidate transformations over the same raw stream, compare against production, and promote only after stable improvement.

### Fork D: room-level replay simulator

Replay a historical room with alternate:

- extraction profiles;
- checkpoint policies;
- consultation budgets;
- addressing rules.

This could evaluate architecture decisions without involving live agents.

### Fork E: decision provenance graph

Accepted decisions may reference:

- consultation;
- participant positions;
- repository evidence;
- test outputs;
- unresolved assumptions.

This provides richer audit than a flat transcript, but should not replace the journal.

### Fork F: adversarial extraction fixtures

Generate outputs designed to resemble UI noise:

- an answer explaining spinner sequences;
- code printing ANSI control bytes;
- a stack trace on the last terminal row;
- repeated table entries;
- nested shell prompts.

These cases test false-negative risk.

### Fork G: self-description probes

Ask the CLI to describe what it believes it loaded or invoked, then compare self-report with machine observation. Self-report is evidence, not authority.

## 5.11 Current compact decision

Build the room first.

Build raw capture and deterministic normalization with it.

Build the laboratory early enough to characterize adapters.

Do not build the universal driller until evidence from the laboratory shows that narrow extraction is materially insufficient.


---

# 6. Transmission to Oraculum

The following text is written as message-ready sections. It assumes Oraculum has already received Wave’s initial architecture proposal for the brokered append-only room.

---

## Message 1 — Added current: output interpretation

After the first architecture proposal, majkee introduced a second subsystem: a hard prefilter layer followed by a “driller.” His intended driller is not merely a regex cleaner and not merely a linguistic tokenizer.

The intended mechanism is:

```text
raw agent output
      ↓
structured reversible tokenization
      ↓
vector/tensor-like representation
      ↓
filtering and synchronization transforms
      ↓
transformed representation
      ↓
mathematical reconstruction
      ↓
clean room output
```

My first pushback was that ordinary tokenization does not understand terminal time, cursor rewrites, persistence, or turn boundaries. Majkee clarified that “tokenizer” means encoding the full output process, including those dimensions. Under that definition, I accept the concept as coherent.

The strongest formulation is:

> The driller encodes terminal reality into a reversible structured token space, applies temporal, spatial, structural, and conversational transforms, and reconstructs a cleaner output sequence while retaining provenance.

The representation should be sparse events rather than a dense machine-learning tensor. A token may include text, terminal operation, row/column, timestamps, rewrite count, persistence, interaction phase, annotations, and source ranges.

---

## Message 2 — Pushback and current practical decision

The runtime cost is probably negligible. Agent output is small, and deterministic terminal processing is linear. ANSI decoding, terminal reconstruction, exact rules, rewrite contraction, and simple scoring should take milliseconds and modest memory.

The real cost is engineering correctness:

- obtaining ground truth;
- surviving CLI version changes;
- avoiding deletion of meaningful text;
- preserving code, diffs, tables, stack traces, and examples that resemble UI noise;
- testing every merge, split, contraction, and reconstruction rule.

Therefore I push back against implementing the generalized tensor engine in V1.

I do not reject the idea. I park its maximal form.

Current staged choice:

```text
immutable raw PTY capture
      ↓
real terminal-state normalization
      ↓
versioned narrow vendor annotations
      ↓
small stateful driller
      ↓
conservative output gate with UNKNOWN
```

The small driller may collapse repeated replacements, select stable final forms, remove confirmed input echo, correlate output with the injected room message, detect prompt return, and preserve structural blocks and errors.

No GPU, neural model, embeddings, LLM cleaner, central drillerd, or general transform DSL should be introduced until captured failures prove a need.

---

## Message 3 — The hacker current

Majkee’s “hacker” idea is legitimate instrumentation, not intrusion:

> Treat each CLI as an unknown machine. Stimulate it with controlled inputs, observe every permitted boundary, correlate the signals, and discover the actual protocol.

This creates an important hierarchy:

```text
native semantic events
      ↓
structured vendor events
      ↓
local process/file/tool observations
      ↓
PTY reconstruction
      ↓
statistical inference
```

We should not guess from terminal pixels when the CLI already exposes a turn event, tool event, skill event, structured JSON stream, or app-server protocol.

At the machine layer, controlled experiments may observe child processes, file reads, MCP activity, working directories, command execution, system calls, and network metadata. But we must distinguish evidence levels:

```text
confirmed: native event names skill activation
observed: SKILL.md was read
inferred: correlated read + bundled script probably means activation
unknown: the model's private reason for choosing the skill
```

System-call tracing belongs in experiments, not ordinary production. TLS interception and attempts to recover hidden provider internals are rejected.

---

## Message 4 — Laboratory resolution

The testing laboratory is the correct home for the broad hacker method and the fuller driller research.

Production and laboratory should be separated:

```text
LABORATORY                         PRODUCTION
broad instrumentation              minimal proven signals
multiple extractor candidates      one conservative extractor
optional syscall tracing           no routine tracing
hypotheses and inference            deterministic normalized events
large evidence bundles             bounded operational state
```

Suggested laboratory components:

```text
probe
fixture
replay
compare
annotate
promote
```

Each controlled run should preserve:

```text
manifest and versions
prompt
raw PTY
terminal events
native events
process events
file events
optional system-call traces
approved clean output
observations
conclusion
```

A laboratory finding may enter production only with:

1. repeatable fixture;
2. precise observable signal;
3. explicit CLI/version scope;
4. known failure case;
5. conservative fallback;
6. regression test;
7. provenance and redaction review.

This laboratory decides whether the final production extractor remains five narrow rules, grows into a small statistical driller, or eventually earns the full reversible tokenizer-transform-reconstructor.

---

## Message 5 — Important architecture refinement

The original room architecture remains intact:

- independent project-rooted sessions;
- adapter-owned terminal sessions;
- append-only room journal;
- explicit directed recipients;
- private context lines with later owner audit;
- sparse per-participant projections;
- versioned human-owned goals;
- bounded consultation leases;
- blind triangulation phases;
- human-accepted checkpoints.

The new refinement is at the adapter edge:

```text
Agent CLI
   │
   ├── native/structured events
   ├── raw PTY
   └── scoped local observations
           │
           ▼
       adapter correlator
           │
           ├── versioned profile
           ├── small production driller
           └── immutable raw provenance
                   │
                   ▼
              normalized room events
                   │
                   ▼
                 larvad
```

The broker should remain ignorant of Claude/Codex UI details. Vendor volatility stays in adapter profiles and laboratory fixtures.

---

## Message 6 — Current decision and open forks

Current decision:

> Build the room first, raw capture with it, and a laboratory early. Keep production extraction narrow and conservative. Promote complexity only when replayable evidence demonstrates a repeated failure.

Selected now:

- raw append-only capture;
- terminal semantics rather than line regex alone;
- exact versioned profiles;
- small stateful extraction;
- `unknown` as first-class;
- provenance ranges;
- replay;
- native events before inference.

Parked:

- dense tensors;
- embeddings;
- neural classification;
- LLM cleaning;
- universal transform language;
- central drillerd;
- production syscall tracing.

Valuable later forks:

- shadow extractor running without affecting delivery;
- adapter capability handshake;
- separate conversational and machine-evidence lanes;
- mutation testing of terminal width, timing, ANSI chunks, and UI wording;
- version-drift alarm;
- room replay with alternate extraction and consultation policies;
- decision provenance graph;
- adversarial fixtures where legitimate answer content resembles UI noise.

My own strongest caution is that output cleaning can become an attractive research project that delays the actual room. The laboratory is justified only if it feeds small, tested rules back into production.

---

## Compact one-paragraph transmission

The post-architecture discussion converged on a two-plane design. Production nabLarva remains a small brokered append-only room with independent repository-rooted agent sessions, sparse recipient views, bounded consultations, and adapter-local cleaning. A separate testing laboratory treats each CLI as an unknown machine: it captures native lifecycle events, structured streams, PTY state, and scoped process/file observations under controlled scenarios; replays competing extractors; and promotes only repeatable, version-scoped findings. Majkee’s driller concept is retained as a reversible tokenization–transform–reconstruction model over sparse temporal terminal events, but its generalized tensor/semantic form is parked. V1 should use immutable raw capture, terminal normalization, narrow vendor profiles, a small stateful driller, provenance, and an `unknown` lane. The laboratory—not intuition—will determine whether more mathematical or learned reconstruction is ever worth adding.


---

# AI HANDOFF

**Goal:**  
Design nabLarva: a lightweight, auditable communication room for humans and independent live terminal AI sessions rooted in different project directories. Preserve the complete architectural and research discussion, including deferred branches.

**Current state:**  
A clean-room architecture has been proposed. The system centers on a small broker (`larvad`), an append-only room journal, human CLI, adapter-owned agent sessions, explicit recipient projections, private context lines, bounded consultations, blind triangulation, accepted checkpoints, and cursor-based recovery.

A second design current has been integrated: output extraction through immutable raw capture, terminal-state normalization, versioned vendor annotations, a small stateful “driller,” and conservative reconstruction.

A separate testing laboratory has been identified as the proper place for broad instrumentation, controlled CLI experiments, replay, alternative extractors, skill/tool activation research, and machine-level observation.

**Decisions made:**

- Keep agents as independent peer sessions.
- Use one authoritative ordered room journal.
- Use a small broker rather than files/FIFOs alone.
- Keep vendor-specific interpretation inside adapters.
- Prefer native semantic and structured events over PTY inference.
- Preserve raw terminal evidence.
- Treat clean text as a derived projection with provenance.
- Use structural anti-drift controls: versioned goals, consultation budgets, blind phases, and human-accepted checkpoints.
- Implement only a small stateful driller in V1.
- Keep `unknown` as a first-class extraction result.
- Separate laboratory complexity from production.
- Promote rules only through repeatable, version-scoped fixtures and tests.

**Parked decisions:**

- generalized reversible tokenizer-transform-reconstructor;
- dense tensor representation;
- embeddings or neural classification;
- LLM-based cleaning;
- central `drillerd`;
- production system-call tracing;
- network interception;
- semantic drift classifier;
- general transformation DSL.

**Files changed / produced:**

- `00_README.md`
- `01_ARCHITECTURE_ROOM_AND_BROKER.md`
- `02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md`
- `03_COST_COMPLEXITY_AND_STAGED_DECISION.md`
- `04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md`
- `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`
- `06_ORACULUM_TRANSMISSION.md`
- `07_AI_HANDOFF.md`
- combined report and ZIP archive

**Validation performed:**  
Conceptual consistency check across the triangulation brief and discussion. No software implementation or runtime benchmarks were performed. Resource estimates remain order-of-magnitude expectations and must be measured against captured CLI sessions.

**Open questions / risks:**

- exact structured interfaces available in each target CLI/version;
- whether adapters must own sessions or can later attach through supported APIs;
- appropriate separation between conversation events and machine evidence events;
- checkpoint creation workflow;
- raw-capture retention and redaction;
- low-confidence extraction policy;
- impact of CLI alternate-screen behavior;
- whether NDJSON remains sufficient after real usage;
- actual rate of meaningful extraction failures after terminal normalization and hard profiles.

**Recommended next move:**  
Create the smallest laboratory fixture before implementing the generalized driller. Capture one ordinary and one tool-heavy run from each target CLI, including raw PTY, exact versions, injected prompt boundaries, and manually approved clean output. Compare terminal-normalization-only against narrow-profile extraction. Use the result to define the first adapter contract and V1 event vocabulary.

**Agent:** Wave


---
