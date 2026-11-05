# Architecture Coherence Layer — Consolidated Proposal

status: working architecture proposal
scope: project architecture · sessions · architect role
purpose: consolidate the proposed model for challenge and later gavel
authoring context: Wave + Majkee discussion
canon status: NOT LOCKED

## 1. Problem

The existing session mechanism already handles local work well:

- Majkee initiates a session and places source material into session-local `raw/`;
- a cSharp / session head can organize the work;
- implementers execute;
- verifiers check acceptance;
- session artifacts preserve evidence and handoff.

The missing function is not another executor or another generic planner.

The gap is **cross-session architectural coherence**.

A project can accumulate many locally successful sessions while gradually violating its original intent, subsystem boundaries, state ownership, dependency direction, documentation model, or other project-wide invariants.

The architect exists to answer:

> **Does this local design still belong to the same coherent system?**

This is a different responsibility from:

- session lifecycle ownership;
- implementation;
- functional verification;
- canon acceptance.

## 2. Authority split

Recommended authority model:

```text
Majkee
  owns: initiative · business intent · gavel / canon acceptance

Architect
  owns: architectural interpretation · project-wide coherence analysis
  proposes: architecture decisions · architecture gates · documentation changes
  does not own: final canon lock · implementation · session lifecycle

cSharp / session head
  owns: session lifecycle · navigation · RUNBOOK/STATUS · delegation · integration

Implementer
  owns: bounded implementation

Verifier
  owns: independent functional/acceptance verification

Files
  hold: durable project truth
```

Compact form:

```text
raw intent                   Majkee owns
     ↓
problem interpretation       Architect owns
     ↓
architectural proposal       Architect owns
     ↓
accept / reject / redirect   Majkee gavel
     ↓
execution navigation         cSharp owns
```

## 3. Preserve `raw/` as source substrate

`raw/` remains session-bound.

Example:

```text
.dev/session/<slug>/
├── raw/
│   ├── majkee/
│   ├── client/
│   ├── research/
│   └── captures/
└── ...
```

The architect may read and cite raw material, but source and interpretation must remain distinguishable.

Desired provenance:

```text
Majkee actually said:
    X

Architect inferred:
    Y

Project later locked:
    Z
```

Do not rewrite X into Y and lose the source boundary.

## 4. Architect as a vertical coherence plane

The architect is not simply another box in the execution pipeline.

The architect crosses sessions vertically:

```text
                         PROJECT WORLD
        PROJECT.yaml ─ flag.md ─ architecture docs
                    \      |      /
                     \     |     /
                      ▼    ▼    ▼
                    ARCHITECT
               coherence custodian
                  ▲           ▲
                  │           │
          ingress │           │ egress
                  │           │
                  │           │
Majkee ──► session/raw        │
   │              │           │
   │              ▼           │
   │          session plan    │
   │              │           │
   │           [gavel]        │
   │              │           │
   │              ▼           │
   │           cSharp         │
   │      lifecycle/status    │
   │              │           │
   │              ▼           │
   │         implementers     │
   │              │           │
   │              ▼           │
   │           evidence ──────┘
   │
   └──────── owns intent + canon decision
```

The central function is **semantic correspondence**:

```text
intent
  ≈
architecture
  ≈
plan
  ≈
implementation
  ≈
documentation
```

A broken `≈` is an architectural finding.

## 5. One architect identity, multiple bounded protocols

Do not create separate permanent agents such as:

```text
architect-check
architect-review
architect-session
architect-documentation
```

Prefer:

```text
one ARCHITECT identity
        +
invocation protocol
```

Stable role:

> Protect project-wide architectural coherence and make consequential boundaries, invariants, ownership, data flow, failure modes, transitions, and documentation implications explicit.

Protocols alter the immediate task, not the architect's identity.

Recommended modes:

```text
                    one ARCHITECT identity
                             │
          ┌──────────────────┼─────────────────┐
          ▼                  ▼                 ▼
       CONSULT           CONFORMANCE         SITTING
     "look at this"      "did we drift?"    "design this"
```

### 5.1 `consult`

Purpose:

- inspect a proposed local design;
- compare it with project architecture;
- identify conflicts;
- recommend whether an architecture gate is needed.

Typical caller:

- cSharp / session head;
- Majkee directly;
- possibly another bounded parent role.

Input:

- session question / proposed design;
- relevant `raw/`;
- `PROJECT.yaml`;
- relevant `flag.md`;
- relevant architecture docs;
- relevant live project state.

Output:

```yaml
architecture_check:
  fit: compatible | conflict | unclear
  touched_boundaries: []
  conflicts: []
  recommendation: ...
  architecture_gate: required | optional | none
  documentation_impact: []
  project_contract_change: true | false
```

Authority:

- advisory;
- no canon lock;
- no implementation;
- preferably read-only.

### 5.2 `conformance`

Purpose:

> Check whether the resulting implementation still agrees with the intended architecture.

Input:

```text
frozen implementation
+
original plan / architecture recommendation
+
tests/evidence
+
PROJECT.yaml
+
flag
+
architecture docs
```

Output:

```yaml
architecture_verdict: PASS | DEVIATION | ESCALATE

matches: []
deviations: []
documentation:
  update_required: []
project_contract_change: false
```

Important distinction:

```text
Verifier:
    "Does it work?"

Architect:
    "Is it still the right shape?"
```

The architect is not a replacement for the verifier.

For consequential work, avoid self-confirmation when practical:

- use a fresh architect context;
- or use an independent challenger / second architecture pass;
- especially when the original architect authored the design.

### 5.3 `sitting`

Purpose:

- full architecture session for consequential structural change;
- buffer directly with Majkee when needed;
- explore alternatives;
- define boundaries, ownership, data flow, migration, rollback, gates, and documentation impact;
- prepare proposed canon changes.

Flow:

```text
Majkee + architect
       │
       ├── buffer
       ├── alternatives
       ├── boundaries
       ├── architecture
       ├── migration
       └── proposed canon changes
               │
             GAVEL
               │
               ▼
          session head
               │
               ▼
          execution arc
```

The architect may prepare the design boundary; cSharp then owns the execution lifecycle.

## 6. Architect should be spawnable

Recommended:

- Majkee may invoke architect directly.
- cSharp/session head may spawn architect in bounded modes.
- other agents may request escalation through the head unless project rules explicitly permit direct invocation.
- the parent owns synthesis/integration.
- architect returns evidence/recommendation, not canon authority.

However, architecture review should not depend entirely on head discretion.

For certain classes of change, project contract should require an architecture gate.

Example:

```yaml
architecture_gate:
  required_when:
    - component_boundary_changes
    - state_ownership_changes
    - dependency_direction_changes
    - persistent_schema_strategy_changes
    - public_contract_changes
    - trust_boundary_changes

  optional_when:
    - local_implementation
    - internal_refactor
```

This makes the project enforce architectural attention without making every task architectural.

## 7. When to escalate from consult to sitting

Use an architectural sitting when an initiative may alter a project-wide invariant.

Likely triggers:

- new subsystem or major component;
- state ownership changes;
- dependency direction changes;
- public/internal API boundary changes;
- cross-session or cross-project mechanism;
- persistent storage strategy;
- migration with structural consequences;
- security/trust boundary;
- architecture documentation conflict indicating uncertain truth;
- changes requiring `PROJECT.yaml` modification;
- major changes to responsibility or ownership.

Do not inflate local implementation choices into architecture.

## 8. Session topology

Recommended principle:

> **One session universe. Separate durable architecture corpus.**

Use:

```text
.dev/
├── PROJECT.yaml
├── flag.md
├── pulse.md
│
├── architecture/            ← durable project architecture
│   ├── MASTER.md
│   ├── toolbox.md
│   ├── engine.md
│   └── adr/
│
└── session/                 ← ALL temporary work
    ├── feature-x/
    ├── bug-y/
    └── toolbox-boundary/
```

Do not create a second live process universe by default:

```text
.dev/session/
.dev/architecture-sessions/
```

because that creates ambiguity around:

- STATUS ownership;
- live state;
- pulse;
- closure;
- raw material;
- runbook conventions;
- promotion.

Architectural work is still work and therefore belongs under `.dev/session/`.

Durable architectural truth belongs under `.dev/architecture/`.

## 9. Architectural session example

```text
.dev/session/toolbox-boundary/
├── SESSION.yaml
├── raw/
│   ├── majkee/
│   ├── research/
│   └── captures/
│
├── architecture/
│   ├── problem.md
│   ├── options.md
│   └── recommendation.md
│
├── plan/
│   └── session.plan.md
│
├── RUNBOOK.md
├── STATUS.md
├── evidence/
│
└── proposed/
    ├── flag.diff.md
    ├── architecture.diff.md
    └── project-yaml.diff.yaml
```

Example session metadata:

```yaml
kind: architecture
scope: project
architect: architect
status_owner: csharp
```

At closure:

```text
session/toolbox-boundary/architecture/recommendation.md
                         │
                         │ promote after gavel
                         ▼
.dev/architecture/toolbox.md

proposed lock
     │
     ▼
flag.md

contract topology changed?
     │
     └── yes → PROJECT.yaml
```

## 10. cSharp and architect remain structurally separate

cSharp:

- first in, last out;
- opens the table;
- owns lifecycle and status;
- delegates work;
- integrates evidence;
- closes the session.

Architect:

- may enter inside that lifecycle;
- may be invoked early, mid-session, or at egress;
- does not become lifecycle owner merely because architecture is involved.

This allows:

```text
cSharp opens
   ↓
architect designs/checks
   ↓
Majkee gavels
   ↓
cSharp executes/navigates
   ↓
architect optionally checks conformance
   ↓
cSharp closes
```

The architect has high semantic authority over architecture without replacing the head.

## 11. PROJECT.yaml versus architecture documentation

`PROJECT.yaml` should not become the architecture encyclopedia.

Recommended role:

> machine-readable project constitution + topology skeleton + hard invariants + canonical pointers

Example:

```yaml
project:
  id: example
  type: application

architecture:
  canonical: .dev/architecture/MASTER.md

  components:
    toolbox:
      root: toolbox/
      architecture: .dev/architecture/toolbox.md
      responsibility: reusable_project_primitives

    engine:
      root: src/
      architecture: .dev/architecture/engine.md
      responsibility: application_runtime

  invariants:
    - toolbox_must_not_depend_on_engine
    - engine_may_depend_on_toolbox
    - persistent_state_has_one_owner

standards:
  code: docs/standards/code.md
  testing: docs/standards/testing.md
  ui: docs/design/ui.md
  ux: docs/design/ux.md

continuity:
  decisions: .dev/flag.md
  live_state: .dev/pulse.md

session:
  root: .dev/session/
```

Boundary:

```text
PROJECT.yaml
    topology + laws + pointers

architecture/*.md
    explanation + diagrams + rationale

flag.md
    settled decisions

pulse.md
    current live state

session/
    temporary work and evidence
```

## 12. Full state flow

```text
                   PROJECT.yaml
              topology + laws + pointers
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     architecture   standards     UX/UI
       documents     documents    documents
          │
          │ decisions become settled
          ▼
        flag.md
          │
          │ project is currently here
          ▼
        pulse.md
          │
          │ instantiate current work
          ▼
      session/raw
          │
          ▼
       ARCHITECT
    consult / sitting
          │
          ▼
    session.plan.md
          │
          ▼
       RUNBOOK/PAD
          │
          ▼
      implementation
          │
          ├──────────────► verifier
          │                  │
          │                  ▼
          │            functional verdict
          │
          ▼
        evidence
          │
          ▼
       ARCHITECT
      conformance
          │
          ▼
        verdict
          │
          ├── current state changes → pulse.md
          │
          ├── durable decision → flag.md
          │
          ├── durable design → architecture/
          │
          └── standing contract changed → PROJECT.yaml
```

## 13. Ingress + egress responsibility

Architect should have two possible observation points.

### Ingress

Before consequential execution:

> Does the proposed change fit the architecture?

### Egress

After implementation:

> Does the built result still fit the architecture?

Diagram:

```text
                         ARCHITECT
                       /           \
                      /             \
             INGRESS CHECK        EGRESS CHECK
                  │                   │
                  ▼                   ▼
           proposed design      resulting system
                  │                   │
                  │                   ├── code reality
                  │                   ├── architecture docs
                  │                   ├── flag
                  │                   └── PROJECT.yaml
                  │
                  ▼
              execution
```

This makes the architect a coherence function rather than merely a planning function.

## 14. Promotion and canon

Architect may prepare:

- recommendation;
- ADR-ready decision;
- proposed documentation change;
- proposed `flag.md` entry;
- proposed `PROJECT.yaml` diff.

Architect should not silently lock canon.

Preferred flow:

```text
architect proposal
      │
      ▼
reviewable diff / session artifact
      │
      ▼
Majkee gavel
      │
      ▼
durable project truth
```

This preserves human authorship-by-approval and prevents architecture automation from quietly rewriting the project constitution.

## 15. Protocol cards / skills

Recommended:

```text
architect identity
    +
protocol card / skill / bounded invocation brief
```

Not multiple architect personas.

Possible protocol definitions:

```yaml
role: architect
mode: consult
```

```yaml
role: architect
mode: conformance
```

```yaml
role: architect
mode: sitting
```

The stable architect contract defines:

- purpose;
- authority;
- exclusions;
- project-read discipline;
- required output classes.

The mode protocol defines:

- trigger;
- exact input;
- scope;
- whether session-local writing is permitted;
- output envelope;
- return edge.

This follows the principle:

> stable role, variable procedure.

## 16. Distinct gates

Keep these gates separate:

```text
implementation gate:
    did the assigned work get built?

verification gate:
    does it satisfy acceptance criteria?

architecture gate:
    does it preserve the intended system shape?

canon gate:
    does Majkee accept this as durable project truth?
```

Do not collapse them into one PASS.

## 17. Fresh-eyes rule

Potential rule:

- ordinary `consult`: same architect context is acceptable;
- routine `conformance`: fresh context preferred but not mandatory;
- consequential architectural lock:
  - fresh architect context or challenger;
  - independent read of the evidence;
  - no self-confirmed gate where practical;
  - Majkee remains tie-break / canon gate.

This preserves crossed witnesses without making every session expensive.

## 18. Minimal implementation path

Do not build a large architecture bureaucracy first.

### Phase 1 — define role

Create one stable architect role contract.

It should state:

- cross-session coherence purpose;
- read project contract / locks / relevant docs before advising;
- no implementation;
- no direct canon lock;
- explicit recommendation and escalation output.

### Phase 2 — define three protocols

Small cards/skills:

- `architect-consult`;
- `architect-conformance`;
- `architect-sitting`.

These should be procedures, not new identities.

### Phase 3 — add architecture gate hints to PROJECT.yaml

Only for high-value triggers.

### Phase 4 — establish durable architecture home

If absent:

```text
.dev/architecture/
```

Start small:

```text
MASTER.md
```

Add subsystem documents only when needed.

### Phase 5 — pilot

Run on a real consequential session.

Measure:

- architecture conflict found before implementation;
- post-build drift found;
- unnecessary escalations;
- human interventions;
- documentation corrections;
- time/token overhead;
- whether the role changed the outcome.

Only then expand the mechanism.

## 19. Main risks

### Architect becomes shadow project manager

Correction:

- architecture authority only;
- cSharp keeps lifecycle;
- Majkee keeps gavel.

### Every task becomes architectural

Correction:

- explicit threshold;
- architect must be allowed to say:
  `NO_ARCH_GATE — implementer may proceed`.

### Duplicate session universes

Correction:

- all temporary work under `.dev/session/`;
- `.dev/architecture/` is durable architecture, not another execution engine.

### Architect self-confirms

Correction:

- fresh-eyes rule for consequential gates.

### Documentation bureaucracy

Correction:

- architect checks meaningful semantic drift, not formatting completeness.

### PROJECT.yaml becomes huge

Correction:

- keep topology, laws, gate triggers, and canonical pointers there;
- detailed architecture remains Markdown.

## 20. Open questions before gavel

The proposal is coherent but not yet canon. Questions worth testing:

1. Should `architect-sitting` permit writes only inside the session bed, or remain read-only and return content to the head?
2. Should cSharp always exist during an architecture sitting, or may Majkee + architect prepare the bed first and wake cSharp only at execution handoff?
3. Which architecture-gate triggers are truly universal enough for `PROJECT.yaml`?
4. Should architecture gate configuration name only semantic classes, or actual repository paths/components?
5. Is egress conformance mandatory for every architecture-gated change or only selected ones?
6. What exact fresh-eyes threshold justifies a second context/agent?
7. Should architectural recommendations use a standard machine-readable envelope?
8. What minimum durable architecture corpus is needed before the architect can judge coherence reliably?
9. How should conflicting evidence between docs, code, runtime, and locked decisions be surfaced?
10. When architecture reality changes but docs lag, is the implementation wrong, the docs stale, or the lock reopened?
11. Should `pulse.md` track architecture-gate state explicitly?
12. How are rejected architectural alternatives retained without polluting canon?
13. What architecture metrics are actually useful enough to record?
14. When does a session-local architectural conclusion deserve promotion into `flag.md` versus only architecture docs?
15. Should `PROJECT.yaml` point to architectural docs by component and responsibility?
16. Should the architecture role remain vendor-neutral while runtime-specific cards render it differently?
17. How much context may an architect load before consultation becomes too expensive for routine sessions?

## 21. Proposed compact constitution

If this design survives challenge, its core can be reduced to:

> **Majkee owns intent and canon.**
>
> **cSharp owns session lifecycle and integration.**
>
> **Architect owns cross-session architectural coherence analysis.**
>
> **Implementers build.**
>
> **Verifiers prove acceptance.**
>
> **Architect may be invoked as consult, conformance, or full sitting.**
>
> **Consequential architecture gates may be required by the project contract.**
>
> **All temporary architectural work remains session work.**
>
> **Durable architecture lives in the project architecture corpus.**
>
> **Architect proposes canon changes; Majkee gavels them.**

That is the current proposal to challenge, not yet the lock.
