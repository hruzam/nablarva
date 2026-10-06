# Blind Architecture Challenge Brief

status: challenge input
purpose: independent architectural read
method: blind triangulation
instruction: derive an independent model before comparing against any existing proposal

## Context

A project uses durable project state plus temporary work sessions.

Typical durable surfaces include:

- `PROJECT.yaml` — standing project contract / machine-readable project map;
- `flag.md` — settled decisions and locked architectural state;
- `pulse.md` — live project heartbeat / current doing-state;
- durable architecture documentation;
- ordinary work sessions under `.dev/session/`.

A typical work session may contain:

- session-local `raw/` material with human briefs, observations, captures, research, consultant input, and other source material;
- a session head / cSharp-like role that opens the work, maintains navigation and status, delegates bodies of work, collects evidence, and closes the session;
- implementers;
- verifiers;
- runbooks, status, evidence, verdicts, and handoff material.

The operator often begins a new initiative by creating a session folder and placing source material into `raw/`. The session head can later organize execution.

The unresolved problem is the role, authority, lifecycle, and storage model of an **architect**.

Do not assume that the architect must resemble the current session head, planner, reviewer, controller, or documentation owner.

## Questions to derive independently

### 1. What problem would the architect solve?

Ask:

- What failure exists today that is not already solved by the session head?
- Can multiple sessions each be locally correct while the application as a whole drifts?
- Who currently checks whether one session's design remains compatible with the project's main intentions, architecture, boundaries, and documentation?
- Is the missing function planning, cross-session coherence, design authority, documentation integrity, or something else?
- If no architect existed, what concrete failure modes would remain?

### 2. What should the architect own?

Consider separately:

- original human initiative / business intent;
- interpretation of the initiative;
- project-wide architectural coherence;
- local session design;
- session plan;
- architectural documentation;
- architecture gates;
- proposed changes to project canon;
- final canon acceptance;
- implementation;
- verification.

For every responsibility, decide whether the architect should:

- own it;
- advise on it;
- inspect it;
- be explicitly excluded from it.

### 3. Where should the epistemic boundary sit?

Assume `raw/` remains bound to the session and preserves source material.

Ask:

- Who may interpret raw material?
- Who may summarize or transform it?
- Who may turn interpretation into a proposed design?
- Who may write a proposed architectural decision?
- Who may promote that proposal into durable canon?
- How is provenance preserved so that:
  - "Majkee said X,"
  - "architect inferred Y,"
  - "project later locked Z"
  remain distinguishable?

### 4. Passive or active architect?

Compare possible models:

- passive architecture reviewer;
- recommendation-only consultant;
- active cross-session coherence custodian;
- phase/session planner;
- temporary design authority during architectural work;
- permanent project-level authority;
- other model.

Determine which model creates the least duplicated authority while still solving the actual problem.

### 5. Spawnable architect?

Should the architect exist as a reusable sub-agent / delegated role that a session head can invoke?

If yes:

- who may spawn it?
- may an implementer invoke it?
- may a verifier invoke it?
- may the operator invoke it directly?
- when is invocation optional?
- when should invocation be mandatory?
- should mandatory architecture gates be encoded in `PROJECT.yaml` or elsewhere?
- may the session head override or skip such a gate?
- what does the architect return to its parent?

### 6. Invocation modes

Determine whether one architect identity should support multiple bounded protocols, for example:

- early consultation;
- architecture conformance check during or after implementation;
- full architectural sitting / design session;
- documentation consistency review;
- migration review;
- other.

Questions:

- Are these truly modes of one stable role?
- Or are they different roles that should not be collapsed?
- Which differences belong in the role identity and which belong in protocol cards / skills / invocation briefs?
- Should mode alter write authority?
- Should mode alter output format?
- Should mode alter who owns the session?

### 7. Full architectural sessions

When a change is sufficiently consequential, should architecture become a full session rather than a bounded consultation?

If yes:

- what triggers that escalation?
- what does the architect prepare?
- does the architect own the session plan?
- does the architect own the session lifecycle?
- does a cSharp/session head still exist?
- when does control pass back to the session head?
- what is the operator's gavel point?
- how are rejected alternatives preserved?

### 8. Where should architectural sessions live?

Compare at least these shapes:

#### A — one session universe

```text
.dev/
├── session/
│   ├── feature-x/
│   ├── bug-y/
│   └── architecture-boundary-z/
└── architecture/
    └── durable project architecture
```

#### B — separate architectural work universe

```text
.dev/
├── session/
└── architecture-session/
```

#### C — another structure

Ask:

- Does separating architectural sessions create a second lifecycle, second status system, or second pulse?
- Does keeping them together blur durable architecture and temporary design work?
- What belongs to session state versus architecture canon?
- What should be promoted at closure?
- Can one architecture vault be durable canon while architectural work remains ordinary session work?

### 9. Ingress and egress architecture responsibility

Should the architect see only proposals before implementation, or also inspect the resulting system?

Possible two-sided responsibility:

- ingress: "Does this proposed change fit the system?"
- egress: "Did the resulting implementation remain faithful to the intended architecture?"

Ask:

- Is this useful or redundant with verification?
- What is the distinction between:
  - functional verification,
  - architectural conformance,
  - documentation consistency?
- Should the architect who designed the change also confirm it?
- When are fresh eyes or an adversarial second architect required?

### 10. Relation to project continuity

Determine how architect output interacts with:

- `PROJECT.yaml`;
- `flag.md`;
- `pulse.md`;
- architecture documentation;
- session plan;
- RUNBOOK / PAD;
- STATUS;
- evidence;
- verdict / handoff.

Which surfaces may the architect edit directly?
Which may receive only proposed diffs?
Which remain owned by the session head or operator?

### 11. Project contract versus architecture documentation

Clarify the boundary between:

- machine-readable topology / hard invariants / canonical pointers in `PROJECT.yaml`;
- full architectural explanation in durable Markdown documentation;
- settled decisions in `flag.md`;
- current work in `pulse.md`.

Should the architect police that separation?
If documentation, runtime reality, and `PROJECT.yaml` disagree, what is the correct response?

## Open questions / evidence to gather during triangulation

Do not force answers where evidence is missing. Classify unknowns as:

- **design question** — can be reasoned from first principles;
- **repository fact** — must be checked from current files;
- **workflow fact** — should be observed in real sessions;
- **runtime capability** — must be verified against current agent/runtime behavior;
- **human preference / gavel** — requires operator decision.

Possible open questions to investigate:

1. How often do current sessions produce architectural drift that is discovered only later?
2. Which types of sessions have historically required a later architecture correction?
3. How often does cSharp/session head already perform architectural work implicitly?
4. Is that implicit architecture work reliable enough to formalize, or precisely the coupling that should be removed?
5. Does `PROJECT.yaml` currently contain enough information to recognize an architecture-sensitive change?
6. Can architecture-gate triggers be machine-readable without becoming bureaucracy?
7. Which changes are clearly below the architecture threshold?
8. Which changes have repeatedly crossed subsystem boundaries?
9. Does the repository already have a durable architecture home, or would one need to be defined?
10. Are architecture documents currently authoritative, descriptive, or mixed?
11. Who currently updates architecture docs after implementation?
12. How often do architecture docs disagree with code or runtime reality?
13. Should the architect be read-only in all bounded invocations?
14. During a full architectural sitting, is session-local write authority necessary?
15. Should the architect write the session plan, or only architecture inputs that the head compiles into the runbook?
16. If architect and session head disagree, what exactly is the escalation/gavel boundary?
17. If architect and verifier disagree, are they judging the same criterion or different criteria?
18. When should fresh-eyes architectural review be mandatory?
19. Should a major architecture sitting automatically require a challenger / blind second opinion?
20. What evidence should be carried forward so a later session can understand why an architectural decision was made?
21. What minimum output is required from an architecture consult so the cost remains low?
22. What is the acceptable token/context cost of loading full project architecture for routine checks?
23. Can smaller scoped architecture indexes or pointers reduce that cost safely?
24. Should architectural sessions remain reopenable history, or should only promoted decisions matter after closure?
25. What metrics would show that the architect role is useful rather than ceremonial?

## Requested output from the challenger

Produce an independent recommendation containing:

1. **Problem statement** — what gap actually needs solving.
2. **Role contract** — stable purpose, authority, exclusions.
3. **Invocation topology** — who calls the architect and under what conditions.
4. **Mode model** — one role with protocols vs multiple roles.
5. **Session topology** — where architectural work lives.
6. **State/data-flow diagram**.
7. **Promotion model** — how session-local architectural work becomes durable project truth.
8. **Gate model** — optional vs mandatory architecture review.
9. **Fresh-eyes / challenge rule**.
10. **Documentation responsibility**.
11. **Failure modes and over-engineering risks**.
12. **Open questions still requiring evidence or operator gavel**.
13. **Smallest viable implementation** — what to add first before building a larger architecture framework.

Do not optimize for agreement with another architect. Prefer a coherent independent model, even when it contradicts the current system.
