---
doc: architecture-process
seat: Symmetry (claude.ai · Opus) — final fold
date: 2026-10-06
version: final (supersedes this file's earlier draft of the same day)
status: FINAL · gaveled in conversation (majkee, 2026-10-06) · becomes a lock when L16 lands in flag
read_at: nablarva@3547e3c · reposoma@d5badad
triad: architecture-process · project-documentation · houston (.symmetry.2026-10-06)
folds:
  - architect-blind-triangulation.symmetry.2026-10-06.md (blind read, @6dbe97b)
  - architect-coherence-plan.wave.2026-10-06.md
  - wave-contrast-addendum_symmetry-fold_2026-10-06.md
  - contrast-return-addendum.symmetry.2026-10-06.md
  - architecture-contract_final_2026-10-06.md (wave) — provenance once this triad lands
---

# Architecture process: how a move travels

This is the hub of the triad. It covers the workflow: who owns what, how a move travels from idea to closure, when Houston is spawned, the gate and its checks, promotion, and the L16 landing text. The shelf lives in `project-documentation`; Houston himself lives in `houston`. Each file points at the others and copies nothing.

The lock lives in flag, and this triad explains it. Every axiom below names the L16 clause that decides it.

## 0. The job

Nablarva doesn't lack local design intelligence. What it lacks is **whole-animal coherence across sessions that each succeed on their own**: a session can be locally right and still bend the animal. The maintained overview is the instrument of that job, not the job itself.

```text
intent ≈ architecture ≈ RUNBOOK ≈ implementation ≈ documentation

a broken ≈ anywhere in the chain is an architecture finding
```

## 1. Axioms

| id | axiom | decided in |
|---|---|---|
| P1 | The gap is whole-animal coherence across sessions, plus an owner for checking it. The overview is that job's instrument. Local design authority already works. | the why |
| P2 | Majkee is the moving gavel. There's no central seat: the seats stay put and he moves between them. | L16.1 |
| P3 | Architecture work is ordinary session work. One session has one gate, and there's no parallel architecture lifecycle. | L16.2 |
| P4 | A gate may require several checks: implementation, verification, architecture and canon. They are never one undifferentiated PASS, and never four gates. | L16.3 |
| P5 | Oraculum diverges, Houston grounds. Neither seat absorbs the other. | L16.1 · L16.5 |
| P6 | The head keeps the closure pen and promotes what survives. Only Majkee's GO makes a lock, and locks live in flag. | L16.12 |
| P7 | Routine ceremony is earned by evidence. Consequential moves carry an intrinsic architecture check from their first occurrence. | L16.6 · L16.7 |
| P8 | No autonomous loops. Every invocation is bounded: read → finding → return. A correction may trigger a new, explicit invocation. | L16.8 |
| P9 | `said`, `inferred` and `locked` never collapse into one another. | L16.11 |
| P10 | No deflection: no seat stops at "Houston must judge". | L16.15 (proposed) |

In the contrast, wave bent P1, P7 and P8. The return pass added R1–R3: how intrinsic classes get declared, Houston naming the hole rather than designing the fix, and gate → checks. The full trail is in the provenance files listed in the frontmatter.

## 2. Seats and authority

| seat | owns | doesn't own |
|---|---|---|
| Majkee | intent, canon, the gavel | delegated execution |
| Oraculum | divergence: forms a move with Majkee, releases the brief | the whole-animal verdict |
| cSharp (head) | lifecycle, RUNBOOK, STATUS, integration, the closure pen; spawns consult | the gavel |
| Houston | whole-animal grounding and coherence checks | lifecycle, gavel, build, functional verification |
| implementers | bounded build work | architecture authority, canon |
| verifier | whether the work meets acceptance | whether the shape still holds |

```text
Majkee ────────────────── intent · canon · gavel
  │
  ├── buffers with ─► Oraculum ────── divergence · forms the move · the brief
  │
  ├── GO ───────────► cSharp (head) ─ lifecycle · RUNBOOK · STATUS · closure pen
  │                   │
  │                   ├── spawns ──► Houston consult
  │                   └── runs ────► implementers · verifier
  │
  └── spawns ───────► Houston ─────── consult · audit · sitting
```

The gavel doesn't go to whoever reasons best. It stays with whoever carries the consequences. Majkee asks, the seats advise, and the gavel stays with him.

## 3. The path of a move

```text
idea (Majkee)
  │
  ▼
Oraculum buffer ──────── diverge · form the move
  │
  ▼
brief ──► Majkee GO
  │
  ▼
ordinary session ─────── head · RUNBOOK · STATUS · one gate
  │
  ├── architecture trigger? ──► Houston consult
  │                             verdict: fits · stretches · breaks · unclear
  │                             known before the build ───► RUNBOOK known constraints
  │                             found during the build ───► STATUS holds:
  ▼
build
  │
  ▼
the gate ─┬── implementation check
  │       ├── verification check
  │       ├── architecture check   [intrinsic or earned]
  │       └── canon check          [if promotion needs GO]
  ▼
closure ── the head promotes what survives (routes: §7)

out of band:   Majkee ──► Houston audit     the whole animal, ad hoc
               Majkee ──► Houston sitting   rare: a move that reshapes the animal
```

In homeostat terms (names only; the seed is still unvalidated): the wrapper is the lighthouse, consult on drift is the anchor, and closure is the harbour.

## 4. When Houston is spawned

| card | spawned by | fires when | not for |
|---|---|---|---|
| consult | the head, or Majkee | a trigger class is hit, an organ boundary is crossed, a lock is touched, drift shows, or closure needs a check | a local choice inside one organ, which the head checks inline |
| audit | Majkee, ad hoc | before a sitting, after meaningful closures, when the animal smells wrong, when the wrapper goes stale, or on suspected cross-organ drift | a schedule |
| sitting | Majkee, rarely | a move that reshapes the animal | one organ's design, which is an ordinary session with a consult |

The trigger classes are the head's checklist; turning them into PROJECT.yaml text has to be earned first. The classes are component boundary, state ownership, dependency direction, persistent schema strategy, public contract and trust boundary.

The first candidate for a sitting already exists: PROJECT-DESIGN §2.1 asks whether nablarva's UI stays in the terminal, gets a terminal wrapper with a process window, or becomes a real app.

Workers don't spawn Houston themselves:

```text
implementer / verifier ──► finding ──► head or Majkee ──► Houston, if needed
```

## 5. One gate, several checks

In nablarva's vocabulary, a **gate** is the single closing condition of one session. The runbook GUIDE puts it this way: one `gate:`, and if you need two, you have two sessions. A gate may require several independent **checks**.

```text
SESSION GATE ── the one closing condition: one `gate:` per session
  │
  ├── implementation check ─── was the assigned work built?
  ├── verification check ───── does it meet acceptance?
  ├── architecture check ───── does it keep the animal's shape?   [intrinsic or earned]
  └── canon check ──────────── does Majkee accept it as truth?    [if promotion needs GO]
```

## 6. Intrinsic checks, earned ceremony

Some architecture checks are required from the first occurrence because of consequence, reversibility or authority. Anything routine waits for evidence.

```text
a move arrives
  │
  ▼
consequential class?   lock · irreversible · trust · ownership ·
  │                    architect-authored design · breaks
  │
  ├── yes ──► intrinsic architecture check, from the first occurrence
  │             known at authoring ───► RUNBOOK known constraints
  │             found mid-session ────► STATUS holds:
  │             a `breaks` verdict ───► intrinsic on occurrence
  │             missed by the head ───► a process finding
  │
  └── no ───► routine: the head's ordinary judgement;
                machinery only once evidence earns it (§9)

new permanent class:  proposal ──► Majkee GO ──► flag line
```

The initial intrinsic classes:

- **lock:** a new or reopened architectural lock.
- **irreversible:** rolling back would be costly or unsafe.
- **trust:** a trust or security boundary changes.
- **ownership:** a fundamental change in who owns state or responsibility.
- **architect-authored design:** the architecture seat materially designed what's now being accepted.
- **breaks:** any Houston `breaks` verdict, on occurrence.

## 7. Promotion and provenance

```text
closure: the head promotes what survives
  │
  ├── organ-local delta ──────────► organ body
  ├── cross-organ delta ──────────► docs/ARCHITECTURE.md
  ├── wrapper meaning changed ────► PROJECT-DESIGN.md
  ├── machine skeleton changed ───► PROJECT.yaml
  └── lock candidate ─────────────► flag docket ──► Majkee GO ──► locked: L<n>
```

Three tags, never merged:

```text
said: <source words>  ≠  inferred: <seat> <reading>  ≠  locked: L<n> (after GO, in flag)
```

Durable docs never cite a prunable session folder except by commit pin: `repo@sha:path`.

## 8. Bounded invocations, no deflection

Every invocation is bounded, and nothing loops between Houston and the head on its own:

```text
Houston ──► breaks ──► return
                         │
         head or Majkee changes the design
                         │
              explicit new invocation
                         ▼
                   fresh Houston ──► fits ──► return
```

"Not on me, Houston must judge" is never a reason to stop. Houston's existence doesn't suspend anyone's local reasoning:

```text
architecture-shaped question
  ├── do what you can
  ├── record `inferred: <seat>`
  ├── name the pending architecture check, if one is needed
  └── return useful work
```

Write permission travels with the task, not with one seat. `said:` 2026-10-06: pulse and flag writes were opened beyond Houston for specific cases, starting with Atlas. The voice transcript said "pools", which I read as pulse. I didn't verify the canon line itself in this read.

## 9. Earned mechanisms (proposed thresholds, not locked)

The rule is locked (L16.7); the numbers below are proposals. Each one becomes a line under flag's *Named deferral thresholds* only on GO.

| mechanism | proposed: earned when |
|---|---|
| routine architecture check on ordinary closures | ≥2 recorded `cross` findings |
| lint / pointer checker | the same `mech` finding repeats across two audits |
| PROJECT.yaml trigger machinery | a skipped consult is later found to have been needed, twice |
| machine-readable Houston envelopes | something parses them |
| audit cadence | ad hoc audits keep arriving after the drift they should have caught |
| the sitting card's full body | the first real sitting |
| dormancy | three audits in a row return only `mech`: scripts absorb that layer and Houston goes quiet again |

Houston exists for judgement, not ceremony.

## 10. Landing: the L16 payload

This is wave's draft with its meaning unchanged; only the house style and the record pointer are adapted. Paste it under `## Locked` in `flag.md`. Once it has landed, shrink this section to `locked: L16`.

```md
- **L16 · Whole-animal architecture coherence** (majkee 2026-10-06; gaveled in
  conversation after blind triangulation and the Wave↔Symmetry contrast; full record:
  the triad `architecture-process` · `project-documentation` · `houston`,
  `.symmetry.2026-10-06`):
  · 1 Authority. Majkee owns intent, canon and the gavel. Oraculum owns divergence and
    move formation. cSharp owns session lifecycle, RUNBOOK, STATUS, integration and
    closure. Houston is the grounding architect: whole-animal coherence, never
    lifecycle, gavel, implementation or functional verification.
  · 2 One session universe. Architecture work is ordinary session work. One session has
    one `gate:`. No parallel architecture-session lifecycle.
  · 3 Checks. A session gate may require independent implementation, verification,
    architecture and canon checks. Architecture and canon checks are conditional; the
    four are not four session gates.
  · 4 Houston. One identity, three cards: `consult` (in-session grounding check, spawned
    by head or Majkee), `audit` (whole-animal audit, spawned by Majkee), `sitting` (rare
    whole-animal design session, spawned by Majkee).
  · 5 Divergence boundary. Houston does not own divergence. If consult finds the
    presented frame cannot preserve coherence, Houston names the hole and its
    constraints; Oraculum or a sitting designs the alternative.
  · 6 Intrinsic architecture classes. New/reopened locks, irreversible changes,
    trust-boundary changes, fundamental ownership changes, architect-authored
    consequential design, and any Houston `breaks` verdict require architecture
    attention from first occurrence. Known classes land in RUNBOOK constraints; classes
    discovered mid-session land in STATUS `holds:`. New permanent classes require
    Majkee GO and flag.
  · 7 Earned ceremony. Routine mandatory architecture checks, lint, PROJECT.yaml trigger
    machinery, machine-readable envelopes, audit cadence and similar mechanisms are
    added only after evidence earns them.
  · 8 No autonomous loops, no self-confirmation. Every Houston invocation is bounded:
    read → finding → return. A correction may trigger a new explicit invocation.
    Consequential locks and architect-authored consequential design receive fresh
    architecture eyes.
  · 9 Documentation homes. PROJECT.yaml = machine skeleton and pointers;
    PROJECT-DESIGN.md = thin animal wrapper and index; docs/ARCHITECTURE.md =
    whole-animal cross-organ architecture; organ body = local contract, detail, key
    files; flag.md = locks; pulse.md = live-session router; session = temporary work.
  · 10 Documentation law. One home per fact. The wrapper stays thin. Organs are born
    thin and grow only on need. Staleness is declared; age is not a finding. Mechanical
    claims are tested mechanically; architectural claims cite locks or evidence;
    unknowns remain unknown.
  · 11 Epistemic provenance. `said:` = source words; `inferred: <seat>` =
    interpretation; `locked: L<n>` = gaveled durable decision. Never merged.
  · 12 Promotion. The head keeps the closure pen and promotes surviving deltas to the
    correct durable home. Houston may check; Houston does not own promotion. Only
    Majkee's GO creates a lock.
  · 13 Houston re-forge. Houston's body is rebuilt in its own small session. Acceptance:
    the body matches this lock and its full record, one real audit has run, its output
    is classified useful / overreaching / missing, and no authority boundary was
    crossed.
  · 14 (proposed) Houston's pen and keeper. Read-only by default; a card carries any
    write authority explicitly. The audit card may maintain wrapper mechanics only
    (pointers, `checked:` stamps, one-liners whose meaning is unchanged) as a diff
    majkee commits. When convergence retires, the audit card keeps PROJECT-DESIGN.md.
  · 15 (proposed) No deflection. No seat stops at "Houston must judge": it does what it
    can, records `inferred: <seat>`, names the pending check, and returns useful work.
```

Clauses 14–15 are a proposed completion. Both are already in the gaveled contract body (wave's H4, §10 and §19), but neither made it into wave's L16 draft. The keeper is an ownership change, and under L11's governance clause ownership belongs in flag. Confirm or strike both at landing.

## 11. Adversarial pass on the final fold

1. **Two operational homes during the transition.** Wave's final contract calls itself the operational shape, and so does this triad. Fix: once the triad lands, wave's contract becomes provenance (`said:` majkee 2026-10-06, "rather … whole final file triad"). L16's full-record pointer names the triad.
2. **Intrinsic classes creeping into routine.** In an animal this early, "ownership" and "trust" could fire on most sessions, which would sneak ceremony in through the back door. Fix: watch the telemetry. If intrinsic checks fire on most closures, that's evidence the class wording is too broad, and it reopens under GO.
3. **A check nobody can run yet.** L16.6 requires intrinsic checks from the first occurrence, but Houston's body stays stale until the re-forge closes. A proposed interim rule lives in `houston`, under *Re-forge*.
4. **Self-report at closure.** The head whose session drifted is the one who writes the delta. A fresh Houston checks it whenever the architecture check applies.

## 12. Next moves

```text
1. land L16 in flag (confirm or strike clauses 14–15)
2. move wave's contract to provenance; this triad becomes the record
3. open the Houston re-forge session (gate: see `houston`)
4. run one real audit inside it, starting from the first-audit seed
5. judge the seat by that evidence
```

Open for Majkee: clauses 14–15, the interim rule (`houston`), and where organ bodies live before structure earns them (`project-documentation`).
