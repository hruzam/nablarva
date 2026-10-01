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
