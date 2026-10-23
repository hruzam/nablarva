---
doc: lock proposals r4 — X3 architecture sitting (supersedes raw/lock-proposals.r3.md after review cycle 03)
seat: houston · card: sitting · 2026-10-22
authority: PROPOSED TEXT ONLY. Only majkee's GO creates a lock (locked: L16.12). A GO on docs/ARCHITECTURE.md approves the document. It adopts a proposal below only if that GO names the proposal explicitly. Approving the document does not by itself append any placeholder L-line. Oraculum carries these to the docket. Houston never writes flag.md.
rules: G4 and G5 are said: majkee (gavel deck STEP 4 / STEP 5), with no L-id until gaveled. Leans per G7 b are inferred: houston and exclude docket 2. They appear here, and in the draft body only as the labelled working defaults that majkee's R9-1 C "c1" allows: dockets 3/4/5/6/8 and O3/O4, which are not gavels and can be overridden without ceremony. G7 option b, as printed, reads "Leans allowed, but only in `lock-proposals.md`, never in the draft body. Each is marked `inferred: houston` with the constraint that drives it. Docket 2 is excluded". Majkee's qualification stands: "ad hoc can gshift behind boundary … not … too tight cage" (said: majkee). Each proposal names what stays open, so a lock does not become a cage.
---

# Lock proposals (r4)

Append-only placement is the head's matter (locked: L15). Text inside each block is the proposed
flag wording. Notes outside the blocks are not lock text.

## P1 — Organ-body homes (from G4)

```text
- **L18 · Organ-body homes** (majkee, gavel deck G4 2026-10-21, own answer "Taking your team
  RESULT as GAVELED"; adopted only if majkee's GO names this proposal): an organ or toolbox that
  already has a documentation home keeps it (e.g. toolbox/termbrana/ with DECISIONS.md under
  L11; docs/organs/stridularium.md). A new body starts as a component folder whose thin README.md
  is the entry; chapters or resources are added only on need. This is the K5 growth law's folder
  stage entered early; line → chapter growth continues inside the entry. Existing bodies are not
  migrated for symmetry. The wrapper and docs/ARCHITECTURE.md point at whichever home applies.
  OPEN, not decided by this line: the parent directory for new folders, the organ/toolbox
  taxonomy, any metadata/frontmatter schema, and any reader/MCP adapter.
```

Note (`inferred: houston`): "L18" is a placeholder number, and the head assigns the real one. The
addendum §1 "proposed, not locked" row changes only after adoption. That addendum edit is
germline-forge work, not this sitting's.

## P2 — Decisions and task-bound reading (from G5)

```text
- **L19 · Decision homes and task-bound reading** (majkee, gavel deck G5 2026-10-21, own answer
  + "gaveled" on the reading schedule; adopted only if majkee's GO names this proposal): locks
  stay in flag.md; product-technical rationale lives in component ledgers, each entry citing its
  authorizing flag line or session brief (the L11 pattern, unchanged). No root ADR series is
  opened by this line. Context for a task is prepared before RUNBOOK authorship, read again by
  each recipient at entry, and refreshed on reassignment, scope/interface change, a changed
  governing source, a new constraint or a conflict; missing, ambiguous or oversized required
  context holds the affected action. The reusable procedure's survival as a controller/function
  is a promotion obligation. OPEN, not decided by this line: the reader schema, the program
  home/API, and the docs/decisions/README.md stub's correction versus retirement.
```

## P3 — VIST boundary (from majkee's Q3 answer)

```text
- **L20 · VIST as observation principle** (majkee, X3 arc answer Q3 2026-10-22; adopted only if
  majkee's GO names this proposal): VIST is a shared observation principle and an intended
  protocol. Its conceptual boundaries come first; its concrete contract is developed and
  qualified afterwards. VIST names observations; controller decisions and actuator actions remain
  separate components with separate authority. Antensor is an implementation candidate. The event
  envelope is proposed, not adopted. Overlaps with termpanum (observation) and stridulatrix
  (delivery) remain visible and unassigned. Observations authorize nothing (L17: discovery is not
  delivery authority).
```

Note (`inferred: houston`): this is proposed because a flag line would stop the "observation ≠
action" split from depending on a raw brief. If majkee prefers to keep it as architecture-doc text
only, drop P3. The draft states the same content as `said: majkee Q3` either way.

## P4 — Build/install coherence with independent clients (from majkee's Q5 answer)

```text
- **L21 · Coherent packages, independent clients** (majkee, X3 arc answers 2026-10-22, Q5;
  adopted only if majkee's GO names this proposal): the direction is coherent build/install
  packages for nabLarva and its toolboxes, while the existing independent client boundaries (L17)
  hold. Coherent packaging does not itself select one global router or a common runtime
  framework. OPEN: exact packaging, one versus several packages, and any shared runtime mechanism
  (which, if introduced, follows L17's narrow-integration-edge rule).
```

Note: majkee said "Record that direction now". It is recorded in the draft. The flag line is
offered, not required.

## P5 — L17 and the one-body direction: choose ONE alternative (from majkee's R9-1 N1 and answer A)

**Sources, verbatim** (said: majkee):

- R9-1 N1 (`answers.majkee.r9-1-notes.2026-10-22.md`):
  - "I will take in advance nablarva as body with architecture - bricks can share
    process|api|cli|subscription layers and call generic methods,... so there is no need keep them
    separately."
  - "Brick indepndence should buy me lightness and extendability over known pipes and flexible
    architecture."
  - "when particular tool is needed, than is no reason wake whole nablarva animal."
  - "UI should be coherent 'framework' not only group of worse findable bashes (-> aliases) and
    locked tmux-pane cages."
- R9-1 A (`answers.majkee.r9-1-abc.2026-10-22.md`): "No common framework - I meaned to use little
  original angle of sight: floating yes, chaotic not. -> most probably `a2`".

**Tension in the sources, shown and not resolved:** answer A begins "No common framework" (L17's
phrase), while N1 asks for a UI that is a "coherent 'framework'". The alternatives below differ
exactly on this point. P5-a keeps L17's words and reads them. P5-b replaces them.

**The L17 text concerned** (locked: L17, flag.md, verbatim): "Termbrana composition and ovitmugen
are independently useful clients; shared mechanisms belong at a narrow integration boundary." and
"Concrete shared-layer ownership/home/API and carrier qualification remain open; no common
framework or transport is authorized by the Phase 0 build."

A GO adopts P5 only if it names **P5-a** or **P5-b**. A GO that names "P5" alone has no single
meaning, so it adopts neither.

### P5-a — reading: L17's text stays; a clarifying clause is added

```text
- **L22 · Reading of L17's framework clause** (majkee, R9-1 note N1 and answer A, 2026-10-22;
  adopted only if majkee's GO names P5-a): L17's text is unchanged. Its clause "no common
  framework or transport is authorized by the Phase 0 build" is read as "floating yes, chaotic
  not" (majkee, R9-1 A). It does not forbid architecting nabLarva as one body in which bricks
  "can share process|api|cli|subscription layers and call generic methods" and the UI is a
  "coherent 'framework'" (majkee, R9-1 N1). It means that the Phase 0 build authorizes no such
  shared layer, framework or transport. Designing shared layers is architectural work and is
  permitted. Implementing, activating, delivering through or adopting a transport for any of them
  needs its own separate release. A particular tool still runs without waking the whole animal.
  All other L17 provisions remain in force, including "shared mechanisms belong at a narrow
  integration boundary"; this line releases no implementation, delivery, activation or
  transport.
```

Note (`inferred: houston`): under P5-a, the narrow-integration-boundary sentence stays as written.
The tension with N1's broader sharing stays open, and design work happens within that boundary
until majkee says otherwise.

### P5-b — replacement: two named L17 phrases are superseded

```text
- **L22 · L17 amendment — one body, floating not chaotic** (majkee, R9-1 note N1 and answer A
  "most probably `a2`", 2026-10-22; adopted only if majkee's GO names P5-b): in L17,
  (1) the phrase "shared mechanisms belong at a narrow integration boundary" is superseded by:
  "nabLarva is one body with an architecture; its bricks can share process, API, CLI and
  subscription layers and call generic methods, and its UI is a coherent framework — floating,
  not chaotic"; and
  (2) the phrase "no common framework or transport is authorized by the Phase 0 build" is
  superseded by: "the Phase 0 build authorizes no shared layer, framework or transport
  implementation; designing them is architectural work, and implementing, activating, delivering
  through or adopting a transport for any of them needs its own separate release".
  The sentence "Termbrana composition and ovitmugen are independently useful clients" stays, and
  a particular tool still runs without waking the whole animal. All other L17 provisions remain
  in force; this line releases no implementation, delivery, activation or transport.
```

Note (`inferred: houston`): under P5-b, the head appends the amendment and lists the two
superseded phrases under flag's `## Archived index` (locked: L15). The original L17 text stays in
place. Concrete shared-layer ownership/home/API and carrier qualification remain open under both
alternatives.

Further notes (`inferred: houston`):
- The head read answer A as a2 *as a proposal* (inferred: oraculum). Choosing between P5-a and
  P5-b, or adopting neither, is majkee's.
- P4 (packaging) and P5 (runtime body) are separate. Majkee may adopt either, both, or merge them.

## Leans on the docket and O-items (G7 b; `inferred: houston`; the items marked **working default (c1)** also appear in the draft §9, per said: majkee R9-1 C "c1")

| item | lean | driving constraint |
|---|---|---|
| 1 files-only control spike | none beyond flag's recorded lean (L14 D2) | — |
| 2 v1 language | **excluded** ("only majkee weighs") | — |
| 3 git residual seat | **working default (c1):** no lean | nothing in the seam ledger depends on it today |
| 4 broker lifecycle | **working default (c1):** **No lean between pane and service.** Either way, the broker's lifetime is independent of every viewer: a broker never runs as a pane inside the ovitmugen frame | L17 (protected process lifetime) · L14 D5 · said: PROJECT-DESIGN §3.2.x ("the broker gets a tab in the agents server, never a pane in the frame") |
| 5 journal store | **working default (c1):** **Confirm NDJSON now**, with a SQLite import path later, under L3 S1's single writer | nablarva.v0 (JSONL first, SQLite when cross-day questions arrive), X2's local ndjson records and the flag's own framing all point the same way; nothing measured argues otherwise (K8) |
| 6 V1 sweet-spot cut | **working default (c1):** no lean | a scope cut, not an architectural constraint |
| 8 discrete-state vocabulary | **working default (c1):** **Do not confirm yet.** First run a bounded comparison of the four candidate envelopes (nablarva.v0, VIST v0, EVENTS v0.3, jev convergence). It names fields, semantics and gaps without choosing one | four envelopes and no gavel (draft §4.5); X2 parked such a comparison as optional (said: cartan-x2 disposition heading 2) |
| O1 hosting machine | no lean; said: majkee R9-1 N9: "office\|in case home" | decide with docket 4 (flag) |
| O2 cross-host transport | none beyond flag's recorded lean; said: majkee R9-1 N9: "now using tailnet with SSH but openned to alternatives" | — |
| O3 room repo topology | **working default (c1):** no lean | — |
| O4 monitor brick-set | **working default (c1):** **No lean.** Sublime is the current working target (said: majkee G2), which is not an editor choice | the sitting must not manufacture an editor decision |

**Ad hoc beyond the docket** (G7's allowance, `inferred: houston`). X1, the doorbell mechanism, is
the collision most likely to be built around silently. Send-keys injection is a recorded death
(locked: L4), and qualification work alone cannot reopen it. If anyone claims an exception — for
example, that a pointer-only nudge carrying no content falls outside that death — the claim goes
to Majkee with its evidence, and only Majkee can grant it. Until he does, no gate or build may
presume the exception. This is offered as a future decision route, not as a lock or a gate
condition. Majkee welcomes alternatives to `tmux send-keys -l` (said: majkee R9-1 N3).

## Not proposed here

- L12's seal and qualifier lines (audit M3, C1 lock side) belong to X1 check 6, owned elsewhere.
- J2 (the AGENTS.md architect seat line and PROJECT.yaml `agents:`) is a saddle edit with its own writer.
- L14 D4/D7 are existing locks. The draft now carries them as relay-work constraints, so they need no proposal.
- Agents approving low-key things (said: majkee R9-1 N8). Per R9-1 B "b1", this is parked as its own governance question.
- Session naming and sub-organ numbering (said: majkee R9-1 N6). Parked by the head; not part of this document.
