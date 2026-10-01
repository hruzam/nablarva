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
