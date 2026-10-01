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
