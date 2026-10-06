---
doc: architecture-process
seat: Symmetry (claude.ai · Opus) — fold author
date: 2026-10-06
status: DRAFT · folded · un-gaveled · contrast-signature pending (wave)
read_at: nablarva@3547e3c · reposoma@d5badad
folds: architect-blind-triangulation.symmetry.2026-10-06.md (blind, @6dbe97b) · architect-coherence-plan.wave.2026-10-06.md · Majkee's voice loop, 2026-10-06
siblings: project-documentation.symmetry.2026-10-06.md · houston.symmetry.2026-10-06.md
lands: beside wave's files in .dev/architect-now-uncanonical/ until gaveled (suggestion)
---

# Architecture process: how a move travels

This is one of three files and owns the workflow: the seats, the path of a move, when each Houston card fires, the gates, and promotion. The shelf is in `project-documentation`; the seat itself is in `houston`. Each file points at the others and copies nothing.

## Axioms (strike what's misread)

wave signs in the last column with `hold`, `bend` or `strike`, plus one line why. One pass, no re-litigation.

| id | axiom | wave |
|---|---|---|
| P1 | The gap is the missing whole-animal overview and an owner for its upkeep. Design authority already works. | |
| P2 | Majkee is the moving gavel. There's no central seat; the seats stay put and he moves between them. | |
| P3 | Architecture work is session work. A design sitting is an ordinary session: one session, one gate. | |
| P4 | Divergence and convergence are separate seats. Oraculum opens a move with Majkee; Houston grounds it against the animal. | |
| P5 | The pen at closure stays with the head. The runbook's closure law already puts promotion at the gate the head runs. | |
| P6 | Locks keep one home, flag (L11's governance clause). Only Majkee's GO makes one. | |
| P7 | Nothing is mandatory until a count earns it. No fixed ceremony (L15). | |
| P8 | No loops. Every check is a straight read that returns a finding. | |

## Seats

| seat | owns | doesn't own |
|---|---|---|
| Majkee | intent, canon, the gavel | — |
| Oraculum | the buffer: forms a move with Majkee, releases the brief | verdicts on the animal |
| cSharp (head) | lifecycle, RUNBOOK, STATUS, the pen at closure; spawns consult | the gavel |
| Houston | grounding: checks a move against the animal (three cards → `houston`) | lifecycle, the gavel, the build |
| implementers · verifier | the build; whether it works | the shape |

The gavel doesn't go to whoever reasons best. It sits with whoever carries the consequences. Majkee asks, the seats advise, and the gavel stays with him.

## The path of a move

```text
idea ─► Oraculum buffer ─► brief ─► GO ─► session (head · RUNBOOK · one gate)
(Majkee)   diverge                              │
                                    trigger? ───┼──► consult: head spawns Houston
                                                │      fits · stretches · breaks · unclear
                                              build      constraints → RUNBOOK / STATUS holds:
                                                │
                gates: implementation → verification → architecture* → canon
                                                │
                closure: head promotes what survives
                         design delta → organ body · wrapper line only if it changed

out of band, Majkee spawns:
  audit    walk the whole animal, report mismatches, keep the wrapper
  sitting  rare: a move that reshapes the animal; research-backed

* optional until earned (see "Earned by count")
```

In homeostat terms (names only; the seed is unvalidated), the wrapper is the lighthouse, consult on drift is the anchor, and closure is the harbour.

## When each card fires

| card | spawned by | fires when | not for |
|---|---|---|---|
| consult | the head (or Majkee) | the move hits a trigger class, crosses an organ boundary, or touches a lock | a local choice inside one organ; the head checks that inline |
| audit | Majkee | his call: before a sitting, after a run of closures, when something smells, when the wrapper's staleness floor looks old | a schedule |
| sitting | Majkee | a move that reshapes the animal: layer model, UI vs terminal, organ dependencies, adopting an outside approach | one organ's design, which is an ordinary session with a consult |

The trigger classes are wave's six, kept as the head's checklist rather than as PROJECT.yaml text: component boundary, state ownership, dependency direction, persistent schema strategy, public contract, and trust boundary.

The first sitting candidate already exists. PROJECT-DESIGN §2.1 asks whether nablarva's UI stays in the terminal, gets a terminal wrapper with a process window, or becomes a real app.

## Four gates, never one PASS (wave §16)

- **implementation:** was the assigned work built? (head)
- **verification:** does it meet acceptance? (verifier)
- **architecture:** does it keep the animal's shape? (fresh Houston, read-only; optional until earned)
- **canon:** does Majkee accept it as durable truth? (gavel)

## Promotion

Three tags, never merged:

- `said:` is Majkee's words, into append-only raw.
- `inferred: <seat>` is a seat's reading, and it names the seat.
- `locked: L<n>` exists only after GO, in flag.

At closure the head promotes what survives. The design delta goes into the organ's body. The wrapper line changes only if the organ's one-liner changed. Lock drafts go to flag's docket for GO. A fresh Houston checks the delta at the architecture gate.

Durable docs never cite into a prunable session folder except by commit pin: `nablarva@<sha>:path`.

## No deflection

"Not on me, Houston must judge" never stops the work. A seat that meets a Houston-shaped question does what it can, tags it `inferred: <seat>`, and names the check as pending. Writing nothing is the failure.

Write permission travels with the task, not with one seat. `said:` 2026-10-06: pulse and flag writes in specific cases were opened beyond Houston, Atlas first. The voice transcript said "pools", read here as pulse. The canon line itself wasn't verified in this read.

## Earned by count (proposed thresholds)

Each becomes a line under flag's *Named deferral thresholds* only on GO.

- **Architecture gate becomes mandatory** at ≥2 recorded `cross` findings.
- **Lint script** when the same `mech` finding repeats across two audits.
- **PROJECT.yaml gate triggers** when a skipped consult is later found needed, twice.
- **Machine-readable envelopes** when something parses them.
- **Sitting card body** at the first real sitting.
- **Dormancy:** if three audits in a row return only `mech`, Houston goes quiet again, as he has been on the personal projects for months, and scripts carry the mechanical part.

## Fold provenance

**Converged blind, on both sides:**
- the architect never owns lifecycle
- one identity with protocol cards
- one session universe
- said, inferred and locked kept apart
- only the head or Majkee spawns
- ingress and egress both covered
- the architect judges shape, the verifier judges function
- no self-confirmation on locks
- the architect proposes, Majkee gavels
- PROJECT.yaml stays a skeleton
- a pilot before expansion

**Majkee's, folded in:**
- Houston as a spawn that checks a developing session against the design
- Oraculum as creative, Houston as grounding
- audit and sitting as separate jobs
- PROJECT-DESIGN as a thin wrapper that grows sub-chapters
- re-forge, not invent

**Wave scorecard:**

| wave element | verdict | note | home |
|---|---|---|---|
| one identity, protocol cards | keep | | houston |
| consult · conformance · sitting | keep, reshaped | conformance becomes consult at the gate; audit added | houston |
| four distinct gates | keep | | process |
| six trigger classes | keep as checklist | PROJECT.yaml text is earned | process |
| `unclear` | keep | | houston |
| a broken ≈ is a finding | keep | "plan" reads as RUNBOOK (L9: no plan.md) | houston |
| fresh eyes on consequential locks | keep | | houston |
| PROJECT.yaml gate triggers | earn | see thresholds | process |
| components / invariants in PROJECT.yaml | earn | invariants only as L-id cites (L11's governance clause) | documentation |
| per-component docs | earn | these are organ bodies, born thin | documentation |
| YAML envelopes | earn | when something parses them | houston |
| `.dev/architecture/` | drop | a third home beside PROJECT-DESIGN and `docs/` | documentation |
| `SESSION.yaml` | drop | duplicates RUNBOOK frontmatter | — |
| `plan/session.plan.md` | drop | plan.md had zero survivors (L9) | — |
| phases 1–4 before the pilot | drop | definitions before any measurement | — |

## Adversarial pass on this fold

1. **Overlap breeds deflection.** Oraculum already runs independent audits in sessions (`nablarva-01-design`). Next to Houston's audit card, that is where "not on me" grows. Proposed boundary (`inferred: symmetry`): Houston checks accordance with the animal (wrapper, organ bodies, flag), and Oraculum challenges the move itself. The no-deflection rule is the backstop.
2. **The moving gavel has a blind spot.** Only Majkee spawns audits, so if he doesn't, the wrapper rots quietly. Staleness stamps make the rot visible at a glance (→ documentation, K6), so no cadence is needed.
3. **The audit holds a pen.** Keeping the wrapper means one seat both checks and writes. That pen is bounded to pointers, stamps and one-liners, as a diff Majkee commits. Substance goes to its owner.
4. **Self-report at closure.** The head whose session drifted writes the delta. A fresh Houston checks it at the architecture gate.
5. **Too thin to orient.** A wrapper that only reaches the right organ makes every agent grep for the same files. Key-files blocks in organ bodies fix that (→ documentation, rule 4).

## Open

- **Gavel:** re-forge Houston's body as its own session, or let it ride along with this contract (→ `houston`).
- **Gavel:** `docs/ARCHITECTURE.md` as the whole-animal body (→ `project-documentation`).
- Repo items seen @3547e3c go to Houston's first-audit seed (→ `houston`).
