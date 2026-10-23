flag-append: R10 step 4 candidate · writer: oraculum(cSharp) X3 head · 2026-10-23 · status: CANDIDATE, shown to Majkee before any flag.md write
sources: raw/lock-proposals.r4.md (sha256 12ed0669…) P1, P3, P5-b · raw/answers.majkee.r9-5.2026-10-23.md (P2 short text) · adoption: raw/answers.majkee.r9-2.2026-10-23.md
placement: block A is appended at the end of `## Locked`, after L17 and before `## Named deferral thresholds` (L15 append-only). Block B is appended at the end of `## Archived index`.
the ONLY changes from the adopted texts: (1) real L-numbers in order after L17 — P1 → L18, P2-short → L19, P3 → L20, P5-b → L21 (P5-b's placeholder said L22; P4 was not adopted); (2) in each attribution, "adopted only if majkee's GO names this proposal / P5-b" becomes "adopted by majkee, R9-2<x> answer, 2026-10-23", which records the act instead of the condition. Every other byte of each lock body is copied unchanged.

## Block A — appended to `## Locked`

```text

- **L18 · Organ-body homes** (majkee, gavel deck G4 2026-10-21, own answer "Taking your team
  RESULT as GAVELED"; adopted by majkee, R9-2a answer "a", 2026-10-23): an organ or toolbox that
  already has a documentation home keeps it (e.g. toolbox/termbrana/ with DECISIONS.md under
  L11; docs/organs/stridularium.md). A new body starts as a component folder whose thin README.md
  is the entry; chapters or resources are added only on need. This is the K5 growth law's folder
  stage entered early; line → chapter growth continues inside the entry. Existing bodies are not
  migrated for symmetry. The wrapper and docs/ARCHITECTURE.md point at whichever home applies.
  OPEN, not decided by this line: the parent directory for new folders, the organ/toolbox
  taxonomy, any metadata/frontmatter schema, and any reader/MCP adapter.

- **L19 · Decision homes** (majkee, gavel deck G5 2026-10-21, own answer; adopted as the
  decision-homes half of proposal P2 by majkee's R9-2b answer "b", 2026-10-23): locks
  stay in flag.md; product-technical rationale lives in component ledgers, each entry citing its
  authorizing flag line or session brief (the L11 pattern, unchanged). No root ADR series is
  opened by this line. OPEN, not decided by this line: the docs/decisions/README.md stub's
  correction versus retirement.

- **L20 · VIST as observation principle** (majkee, X3 arc answer Q3 2026-10-22; adopted by
  majkee, R9-2c answer "a", 2026-10-23): VIST is a shared observation principle and an intended
  protocol. Its conceptual boundaries come first; its concrete contract is developed and
  qualified afterwards. VIST names observations; controller decisions and actuator actions remain
  separate components with separate authority. Antensor is an implementation candidate. The event
  envelope is proposed, not adopted. Overlaps with termpanum (observation) and stridulatrix
  (delivery) remain visible and unassigned. Observations authorize nothing (L17: discovery is not
  delivery authority).

- **L21 · L17 amendment — one body, floating not chaotic** (majkee, R9-1 note N1 and answer A
  "most probably `a2`", 2026-10-22; adopted by majkee, R9-2 answer "P5-b", 2026-10-23): in L17,
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
  Record: docs/ARCHITECTURE.md (X3 sitting, promoted at nablarva@f20dda5); sitting bed nablarva@519a211.
```

The last line of L21 ("Record: …") is the only text added beyond the attribution change. It is a pointer, not lock content, and Majkee may strike it.

## Block B — appended to `## Archived index`

```text
- L17's phrase "shared mechanisms belong at a narrow integration boundary" and its phrase "no common framework or transport is authorized by the Phase 0 build" → superseded by L21 (majkee, 2026-10-23); all other L17 provisions live.
```
