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
