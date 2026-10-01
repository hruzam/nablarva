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
