# task.T3-T4 — orchestration fork: CREATURE ⟷ primary-larva

_Navigation layer folded by @folder from two maps · 2026-08-07_
_This is a POINTER index, not a digest. Raw files are authoritative; descriptors are copied verbatim from the source maps. Forks are preserved AS FORKS — no branch collapsed._
_Roots — MESHUP: `/home/hruzam/unikuklatrix/nablarva/meshup/` · REPOSOMA: `/home/hruzam/reposoma/`_
_Source maps — Field: `/home/hruzam/unikuklatrix/nablarva/meshup/_preflight/map.meshup.field.2026-08-07.md` · Epoch: `/home/hruzam/unikuklatrix/nablarva/meshup/_preflight/map.reposoma.epoch.2026-08-07.md`_

- **Theme:** T3/T4 — the orchestration-concept fork: living process (Y / stridulator / CREATURE) vs file-only (X / primary-larva), plus related orchestration forks.
- **Scope:** meshup T3/T4 cluster + the fork records F1, F2, F5 (all touching room/broker orchestration).
- **What tyler does with it:** enters an UNRESOLVED fork. Both branches are located and preserved. Tyler reads BOTH before any decision; the gavel is not closed in the corpus.

---

## SOURCES

### T3 — CREATURE / room-is-a-process (Y position) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` · the canonical Y document: stridulator as one small static binary; PTY adoption; in-memory socket routing; structural regulation (turn quotas enforced by router, not agents); failure story (hard failure). · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "Y — room-is-a-process" · Y described for fresh reader; the bus-mediated, structure-enforced alternative. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.11 · hybrid that substantially adopts Y (broker process = larvad; adapter-owned PTY); broker vs files/FIFOs contestable decision resolved in favour of broker. · Field map

### T4 — primary-larva / room-is-a-file (X position) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` · the X formulation (pre-triangulation); "COMPOSER = most hardcoding"; roller; "dialogue-room repo?"; no daemon posited. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "X — room-is-a-file" · X described: roller, git-diff wire, cooperative anchors, fails soft; position that died (git-as-wire reversed mid-session). · Field map

### Fork record files (both positions present) — from Field's meshup map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` · convergence record; deaths of X-specific elements; gavel item 1 (files-only spike: yes or no?). · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` · decision ledger holding both alternatives with status. · Field map
- `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md` · transmission that resolves toward hybrid. · Field map

_(No reposoma SCOPE candidate is assigned to this fork by Epoch's map; the orchestration-fork material is meshup-side. Epoch's scope-2 multi-agent/orchestration research is folded in task.T2.composites.md.)_

---

## FORKS

### F1 — CREATURE vs primary-larva — the archetype fork (per brief) · UNRESOLVED
- **Question:** Should the nabLarva room be regulated by a living process (structural enforcement) or by file conventions alone (cooperative enforcement)?
- **Branch A (CREATURE / room-is-a-process / Y):** the stridulator: one small static binary; PTY adoption; in-memory socket routing over Unix domain sockets; turn quotas and drift gates enforced by the router, not requested of agents; an agent cannot drift on traffic it never receives. Fails hard (dead router = dead room).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` (entire document, Oraculum's sealed position)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "Y — room-is-a-process"
- **Branch B (primary-larva / room-is-a-file / X):** ledger-mediated; roller as append-only markdown; regulation by cooperative convention; agents obey anchors because they're told to; git-as-wire (reversed mid-session, but position held by majkee). Fails soft (a file is always readable).
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` (majkee's original position; Cluster A + B)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "X — room-is-a-file"
- **Field status (verbatim intent):** The Wave conversation (`01_ARCHITECTURE_ROOM_AND_BROKER.md`) proposes a hybrid broker (larvad) substantially closer to Y/CREATURE; the triad voted 2:1 against X. Gavel item 1 remains open: "files-only control spike — build X-pure as one-day control experiment, or accept 2:1 vote and skip." **Not resolved; gavel pending.** → DECISIONS FOR MAJKEE.

### F2 — v1 language: Python stdlib vs C++ · UNRESOLVED
- **Question:** What implementation language for the nabLarva broker (larvad) and adapters?
- **Branch A (Python stdlib first):** delivery speed, zero deps, rapid experiment and PTY support (`asyncio`, `pty`, `subprocess`); Rust rewrite only after real reliability/performance pressure demonstrated.
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.10 (V1 recommended technology)
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.6 ("Python standard library: Provisional V1")
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` deaths section ("C++/Go static binary as Y language: outvoted by Python-stdlib-first")
- **Branch B (C++):** majkee's stated learning appetite; "smallest safe solution" implies writing C++ to learn it on this project; explicitly not overridden — only majkee weighs this decision.
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §8 gavel item 2 ("Python-stdlib-first (Z's argument) vs majkee's appetite to learn C++ on this. These optimize different goods: delivery speed vs growth. Only majkee weighs.")
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` gavel item 2
- **Field status:** Technical recommendation = Python. Personal call = C++. Majkee's gavel not recorded in corpus. → DECISIONS FOR MAJKEE.

### F5 — Adapter session ownership: adapter-launches vs adapter-attaches · UNRESOLVED (tracked)
- **Question:** Must adapters always launch their own PTY-owned CLI sessions, or can a later version attach to already-running sessions through official APIs?
- **Branch A (adapter owns and launches):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.3 and §1.11; `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.2.
- **Branch B (adapter may attach to running sessions):** `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.9 "Session attachment"; `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/07_AI_HANDOFF.md` open questions.
- **Field status:** A = V1 choice, provisional; B = future-path open question. Not a resolved fork — a tracked fork. _(Also cross-referenced in task.T1.)_

---

## DOUBLES

- **D3 — Promotion criteria — 7-item list for a finding to enter production** touches this theme (staged-decision / lab-to-production, part of the room's anti-drift regulation). Two locations:
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md` §4.12 (lines ~315–324): "1. repeatable fixture; 2. precise signal definition; 3. supported CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."
  - `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md` Message 4: "1. repeatable fixture; 2. precise observable signal; 3. explicit CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."
  - Field note: items 2 and 3 differ in one word each; items 1, 4–7 verbatim. **Raw preserved, not merged.**
- **D5 — nablarva.wave.full-report.2026-08-05.md contains verbatim doubles of all chapter content** touches this theme (the fork records 01/05/06 are chapters inside the aggregate). `/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md` opens identically to `00_README.md` and reproduces chapters 01–07 verbatim. Field note: systematic (derived aggregate, not authored separately), not flagged individually. **Raw preserved, not merged.**

---

## GAPS

### Field gaps touching orchestration
- **G1. Conflict resolution for shared writes (load-bearing gap).** Flagged "unresolved, load-bearing" in `seed.entity.full-idea.2026-08-02.md` (§open), raised to "LOAD-BEARING PRECONDITION" in `triangulation.entity.symmetry-x-asymmetry.2026-08-03.md` (#conflict-is-ontology: "no multi-host write topology before the conflict rule exists"), and listed as an open question in `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`. No file proposes a concrete mechanism. _(Also surfaces in STYLE-SUPPORT via the entity files.)_
- **G2. Math engine research.** Referred to repeatedly as "untabled, blocks final forge" (`handoff.applications-in-common.2026-07-31.FINAL.md` §11 thread 1; `triad.comparison.2026-07-31.md` "Untabled (blocks final forge)"). No file in the corpus contains this material.
- **G4. Cluster B (product/strategy) elaboration.** `seed.oraculum.2026-07-31.md` splits material into Cluster A (mechanism) and Cluster B (product/strategy); Cluster A heavily documented, Cluster B (nabLarva identity, multi-vendor onboarding, human-team hub / stridularium as product) has almost no corpus presence beyond the seed's sketch. The provisorium content referenced in the handoff is not present.
- **G6. Gavel outcomes.** 7-item gavel docket (`triad.comparison.2026-07-31.md`) and associated decisions (language, git residual seat, component naming, V1 sweet-spot, journal store, broker lifecycle) have no resolution document in the corpus. Gavel process announced as starting on "nabla-lab side" at session close; outcomes absent.
- **G3. V1 implementation code** (shared with T1/T2) — no code for larvad, larva CLI, adapters, room protocol.

---

## DECISIONS FOR MAJKEE

- **F1 gavel item 1 — files-only control spike: yes or no?** Build X-pure as a one-day control experiment, or accept the 2:1 vote against X and skip. Gavel pending; not resolved in corpus. Branches/locations under F1 above. **BOTH branches preserved — do not collapse to the hybrid.**
- **F2 — v1 language: Python stdlib vs C++.** Technical recommendation = Python; personal call = C++ ("only majkee weighs" — delivery speed vs growth appetite). Majkee's gavel not recorded in corpus. Locations under F2 above.
- **G6 — the wider 7-item gavel docket** (`triad.comparison.2026-07-31.md`) has no resolution document; its outcomes are a standing human/gavel obligation flagged by Field as absent from the corpus.
