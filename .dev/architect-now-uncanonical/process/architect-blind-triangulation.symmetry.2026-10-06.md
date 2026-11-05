---
doc: architect-blind-triangulation
seat: Symmetry (claude.ai · Opus) — blind challenger
answers: architect-blind-triangulation-brief.wave.2026-10-06.md
date: 2026-10-06
status: SEALED · blind read · pre-comparison · un-gaveled
blind: derived before wave's results; architect body, PROJECT-DESIGN and any architect proposal left unread
read_at: nablarva@6dbe97b (core, pushed 2026-10-01 — local likely ahead) · reposoma@d5badad (pushed 2026-10-05)
golden_rule: no bureaucracy, no over-engineering (operator, 2026-10-06)
---

# Architect — blind triangulation read

`Sealed before wave. Score against it axiom by axiom (hold / strike), not prose against prose.`

## Thesis

The gap is promotion, not authority. nablarva already designs (head or design seat), audits (Oraculum, Janus) and gavels (majkee's GO/STOP). The runbook's closure law already says "promote what survives." Nobody owns the architecture part of that sentence.

The smallest honest architect is a named owner for that clause plus an optional consult. It has no lifecycle of its own, no new universe and no new file kinds. A mandatory gate comes only when it is earned by count.

## Axioms — strike any

- **A1** · The gap is durable residue, not design authority.
- **A2** · Design authority works. `nablarva-01-design` was a full architectural session in all but name.
- **A3** · The closure law exists ("promote what survives"). The architect owns one clause of it, not a new process.
- **A4** · Locks keep one home: `flag.md`. L9′: two files are allowed, two authorities are not.
- **A5** · The architect has no pulse row, no STATUS and no standing session. Consult and harbour are postures: runbook law names protocols for the posture, never the seat.
- **A6** · Much visible drift is mechanical (dead pointers, router creep). That is lint territory, not architect territory.
- **A7** · The judgement remainder is real but unmeasured: each session is right while the whole drifts.
- **A8** · Every session already ends at majkee's GO/STOP, so no new gavel point is needed.
- **A9** · A separate architecture universe would recreate the pulse fork that L9's survey says orphans a branch.
- **A10** · Commit-pinned citations (`repo@sha:path`, already used in L9′) survive pruning; relative ones don't. `docs/ARCHITECTURE.md`'s `../triad.comparison…` and `../vision.oraculum.Y…` don't resolve in the pushed tree.
- **A11** · A mandatory gate is earned, not declared — same shape as flag's named deferral thresholds.

## 1 · Problem statement

Architecture evaporates between sessions. A session dies at its gate, and its accepted design stays in the pruned folder.

- `docs/ARCHITECTURE.md` still says "pre-architecture, no build yet," while a first-brick design with GO, termbrana's passing tunnel, ovitmugen v1 and muticula all exist.
- Live instance in pulse: `nablarva-01-design (CLOSED — GO; awaiting preservation + prune)`. Promotion has stalled and has no owner.
- The head's implicit design work is fine. The coupling to remove is the head consolidating its own design into durable truth.
- Second, unmeasured: cross-session incompatibility (A7).

Not the gap: planning, verification, design authority. All three have owners.

## 2 · Role contract

**Purpose.** Keep one current, cited answer to "what shape is the system, and why," and test designs against it when they near a boundary.

**Stance.** Event-driven custodian. Between calls, its only state is `ARCHITECTURE.md`.

| relation | scope |
|---|---|
| Owns | cross-session coherence · `ARCHITECTURE.md` content |
| Advises | interpretation of raw · local design · flag-line drafts · `PROJECT.yaml` diffs |
| Inspects | a session's result against the constraints from its own consult |
| Excluded | business intent (majkee) · RUNBOOK / PAD / STATUS / pulse (head) · canon acceptance (gavel) · implementation · functional verification |

## 3 · Invocation topology

Two scales — the golden rule's own shape: a check inside authoring when small, a gate of its own when big (`res/research.md`).

- **Small** — the head checks inline against `ARCHITECTURE.md` while authoring the RUNBOOK. No spawn.
- **Big** — the design crosses a subsystem or shared interface, or touches a lock. The architect is spawned.
- **Who spawns** — the head or majkee only. Implementer and verifier raise "boundary?" to the head; no side channel.
- **Returns** — a one-page RETURN: `fits | stretches | breaks` + ≤5 constraints + said and inferred kept separate.
  - `fits` — inside the current architecture.
  - `stretches` — extends it; needs a delta.
  - `breaks` — contradicts a lock; flag law then requires new evidence.
- **Constraints land in existing slots** — RUNBOOK "known constraints" at authoring time, STATUS `holds:` mid-session.

## 4 · Mode model

One seat, two postures.

- `consult` — ingress, read-only, answered with a RETURN.
- `harbour` — at closure: conformance + consolidation, written as a VERDICT with drafts in the session folder.

The seat's body carries purpose and exclusions; the cards carry inputs, output shape and budget. A fresh seat may fill harbour. Doc consistency → lint. Migration review → a consult. Full sitting → a session, not a mode (§5). Posture changes output and write scope, never who owns the session.

## 5 · Session topology

Shape A. Durable material stays in `docs/`, where `PROJECT.yaml` already points — no `.dev/architecture/` vault.

An architecture session is an ordinary sibling `<program>-<NN>-<phase>/` with its own gate. The head keeps the cSharp posture, the architect holds the design pen, a challenger reads blind at the gate, majkee gavels. A consult escalates to a full session on `breaks`, or when the question outgrows the consult budget.

## 6 · State / data flow

```
majkee ─brief─▶ raw/                      said · append-only
                  │ read (any seat)
head ◀────────────┘   small: inline check vs ARCHITECTURE.md
 ├─ consult ──▶ architect ─▶ RETURN  fits | stretches | breaks
 │  (big · mandatory once earned)    → RUNBOOK constraints / STATUS holds
 ▼
RUNBOOK ─▶ implementers ─▶ evidence ─▶ verifier ─▶ VERDICT (function)
 │
 close · STATUS arch: touch
 ├─ harbour ──▶ architect ─▶ VERDICT (shape) + ARCHITECTURE delta + flag drafts
 │                           cites L-id · repo@sha:path
 ▼
majkee GO/STOP ─▶ flag.md (locks) · docs/ARCHITECTURE.md (explains)
                  pulse row out · dir pruned · git = archive
```

## 7 · Promotion model

Three provenance tags, never merged:

- `said:` — locator into raw (append-only).
- `inferred:` — the seat that inferred it.
- `locked:` — the L-id.

Anyone may read raw; interpretation lives outside it. Only majkee's GO turns a draft into a lock. Nothing enters `ARCHITECTURE.md` except through a GO'd session, each section citing its lock or commit-pinned evidence.

At close, three things are promoted: flag-line drafts, the ARCHITECTURE delta, and only those rejected alternatives someone could plausibly re-propose (as L4-style deaths). The rest is pruned; git is the archive.

## 8 · Gate model

Optional for now. A mandatory consult for boundary-crossing designs is earned at ≥2 recorded cross-session corrections, written as one line under flag's named deferral thresholds. `PROJECT.yaml` needs nothing — it already points at flag.

- **Trigger** — the head's declaration, not path rules in `PROJECT.yaml`. A rule engine would be premature.
- **Below threshold** — stays inside one subsystem; touches no lock and no shared interface.
- **Waiver** — allowed but visible: `arch: waived — <reason>` in STATUS, seen at the existing GO/STOP. (`waived` joins the key's vocabulary only once the gate is earned.)
- **Head vs architect** — the head may proceed against `stretches`, recorded in STATUS. `breaks` touches a lock; only majkee's gavel settles it.

## 9 · Fresh-eyes / challenge rule

A blind challenger is mandatory in only two cases:

1. a `breaks` verdict;
2. the architect confirming what it designed itself — then a fresh instance given flag + ARCHITECTURE + diff, no transcript, or Janus.

Everything else is optional; triangulation is already cultural here.

## 10 · Documentation responsibility

One writer per surface:

| surface | writer |
|---|---|
| `flag.md` | majkee gavels · head writes · architect drafts |
| pulse · STATUS · RUNBOOK / PAD · handoff | head |
| `PROJECT.yaml` | proposals only → gavel |
| `ARCHITECTURE.md` | architect authors; lands only with a GO |
| evidence | implementers / verifier; architect reads |

Boundary: `PROJECT.yaml` maps (pointers + hard facts, no prose) · flag decides · ARCHITECTURE explains · pulse routes. ARCHITECTURE cites locks and never restates them (L11 already makes termbrana's `DECISIONS.md` cite its authorizing flag line).

Three criteria, three owners: function (verifier) · shape (architect) · consistency (lint). Architect and verifier can't contradict each other; they judge different things.

On disagreement, classify before fixing:

- code ≠ lock → implementation drift → fix the code;
- reality moved on legitimately → unpromoted change → promote via gavel (reality is the new evidence);
- dead pointer → mechanical fix.

## 11 · Failure modes and over-engineering risks

- **Second authority** — ARCHITECTURE paraphrasing locks → cite, never restate.
- **Rubber stamp** — fits-rate near 100% → kill the consult.
- **Shadow head** — architect drifting into planning → exclusion list.
- **Self-grading** → §9.
- **Context tax** → `ARCHITECTURE.md` as lighthouse: small index, sections loaded by scope, size cap.
- **Ontology creep** → no new file kinds; two small vocabularies (verdict, provenance) + one STATUS key; pilot tags die with the pilot; the whole role is deletable if its residue costs less than its upkeep.
- **Name collision** — `architect` seat (`PROJECT.yaml`), `convergence` maintaining `AGENTS.PROJECT-DESIGN.md`, Houston's reconcile pass (L5). Three claimants = three authorities in waiting.

## 12 · Open questions — evidence or gavel

- **[repo] Load-bearing.** Are `convergence` + `AGENTS.PROJECT-DESIGN.md` already this function and the de facto architecture doc? It is labelled "draft, not canon," yet it holds the naming/design chapter — authority is already mixed.
- **[repo]** `.shared/agents/convergence.md` isn't in the pushed tree (scope-group path?). ARCHITECTURE.md pointers are dead (A10). pulse carries two non-router rows — L9′ creep in miniature.
- **[workflow]** How many designs were later corrected? Candidates: `nablarva-X0-restarted`, `recovery`, and four sessions on one seam (relay-contract · communication-protocole · 02-pipe · voice-relay).
- **[workflow]** Worktree branch per session? Yes → promotion = merge; no → head applies the delta.
- **[runtime]** A read-only consult stays a cooperative rule until proven on the installs; muticula-01's evidence is the natural source.
- **[gavel]** Verdict vocabulary · threshold N · L10 placement split (§13).
- **[parked]** Cross-project altitude (Houston's reconcile, Hypatia) — a different function; don't merge.

## 13 · Smallest viable implementation

1. **Build nothing.** One manual harbour pass on `nablarva-01-design` (stalled in pulse). Fresh seat: not Cartan (designed), not Oraculum (audited).
   - In: flag · ARCHITECTURE stub · accepted design · audit.
   - Out: `ARCHITECTURE.md` v0 (cited, commit-pinned) · flag-line drafts · findings tagged `mech | judge | cross` · cost as a spend record (`res/token-economy.md`).
   - majkee's GO → head applies → prune.
2. **Only if step 1 finds `judge` / `cross` value:**
   - one clause in the runbook GUIDE's closure law: the architecture delta is part of what survives;
   - one STATUS key `arch: none | touch`; `touch` requires a harbour VERDICT before prune — checkable.
3. **Mandatory consult** only through a flag threshold line (§8).

- **Kill switch** — pilot + next two passes yield zero `judge` / `cross` → the role collapses into a head closure clause + lint; delete the seat.
- **Golden-rule check** — native surface: closure law · research gate · Janus/Oraculum audits. Delta: one clause + one key. Retirement: the kill switch.
- **Placement (L10)** — the residue is nablarva's own architecture → lands in nablarva; history stays pure animal. Convention edits live in reposoma's guides. Role telemetry travels by mail.
- **Metrics** — `judge` / `cross` findings per pass · non-`fits` verdicts that changed a RUNBOOK · fits-rate · close → residue latency · tokens per pass.

## Adversarial pass

- **Strongest counter:** this is just the head's closure duty plus a lint. Maybe — the `cross` count decides; it can't be won by argument.
- **The brief:** 11 question groups, 25 open questions and 13 output sections for what may be one closure clause. Its density is the over-engineering vector; most answers here are "don't decide; count."
- **This read's lens:** lighthouse (ARCHITECTURE.md) · anchor (consult) · harbour (closure) is the homeostat seed lifted to project scale. The seed is unvalidated and its brake is on — used to name, not to justify. Strike it wherever it does argumentative work.

## Underlined — open at release

- wave: scored axiom by axiom (hold / strike), not prose against prose.
- `AGENTS.PROJECT-DESIGN.md` and reposoma's architect body: read at comparison, after wave.
- Load-bearing question, unanswered: is `convergence` already this role under another name? If yes, step 1 becomes "merge two docs and two names into one," not "activate an architect."

## Receipts

Read (pinned):

- `nablarva@6dbe97b:PROJECT.yaml`
- `nablarva@6dbe97b:.dev/session/flag.md` — L1–L13, named deferral thresholds, docket
- `nablarva@6dbe97b:.dev/session/pulse.md`
- `nablarva@6dbe97b:docs/ARCHITECTURE.md`
- `nablarva@6dbe97b:.gitignore` — checked whether `.shared/` is ignored (it isn't)
- `nablarva@6dbe97b:` listings of `/`, `docs/`, `docs/decisions/`, `.dev/session/`
- `reposoma@d5badad:raw.guides/runbook/GUIDE.md`
- `reposoma@d5badad:` root listing

Unread by design: reposoma's architect body · `AGENTS.PROJECT-DESIGN.md` · any architect proposal · `.hlm/` (sealed operator vault, L12).

Staleness: nablarva's pushed head is 2026-10-01; pulse-row evidence may be five days old.

Release delta vs the inline seal: §8 waiver reconciled with §13's key vocabulary (`waived` joins only once the gate is earned); `read_at` pins and receipts added. Consistency only — no new decision.
