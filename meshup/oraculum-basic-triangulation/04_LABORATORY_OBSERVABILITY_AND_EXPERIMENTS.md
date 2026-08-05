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
