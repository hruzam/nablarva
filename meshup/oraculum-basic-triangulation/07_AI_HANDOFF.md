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
