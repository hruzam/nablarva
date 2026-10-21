# .dev/observations/ — the session-process record (first instance 2026-10-07; law GAVELED majkee 2026-10-07 → runbook GUIDE §On gate closure)

**If you just arrived:** this folder holds what closed sessions learned about *running* sessions — not their work results. Read a file by the session slug in its name; write your own only for a session you are in. Pointed from `AGENTS.md` §Read order (session surfaces).

`what: what a SESSION taught about running sessions — regime facts, carriage faults, support logs, watcher/latency incidents, what broke and how it was caught. Not work evidence (that promotes to canon/commits), not the seat's inner record (that is reposoma raw.therapy/<seat>/), not the operator's journal.`
`why: beds die with the gate (runbook law). Process observations written inside a bed die with it or orphan in a preservation commit nobody opens. "Forgetting is one of the strongest human harnesses" (majkee, S10). This folder is outside every bed and never pruned.`

## Law of the folder (gaveled 2026-10-07; authority = runbook GUIDE §On gate closure, this README mirrors it)

- Flat. One file per `<session-slug>.<seat>.<YYYY-MM-DD>.md`; append-only; any seat writes its own file at any time **during** the session — not only at close.
- Origin header on every file: source path + preservation commit + promoter. Verbatim moves; summarising happens in receipts and therapy, which **point here**.
- Harvest, not replace: closing receipts, therapy arcs, gavels and guide chapters cite these files; the file stays the only full-grain copy.
- Project-local by design. A cross-project harvest in reposoma is NOT built until repeated pain earns it (global CLAUDE.md: no registries before maintenance pain).

## Closure step — GAVELED 2026-10-07, folded into runbook GUIDE §On gate closure (text kept here as the mirror)

> **Observations promote before prune.** Session-process files in the bed (`raw/observations.*`, `raw/*issues*`, `raw/*support*`, `raw/note.*`, the receipt's carriage facts) move to `<project>/.dev/observations/<slug>.<seat>.<date>.md` with an origin header. **The prune refuses** while any such file is still in the bed un-promoted — the head runs the check, and a FAIL holds the `git rm`. This completes `csharp-head-protocol.md` §4 (promotion manifest of every `raw/` keeper): that manifest classifies by work-value; this step names the class it lets fall through.

Rationale: G-27 extension (2026-10-07) — a check whose verdict cannot reach the act stops nothing; the refusal wires it to the act. First instance: X0 — three files below, promoted from `d1c4b1e` after the prune (out of order, hence the law).

## Readers — three reads, by what they produce (gaveled majkee 2026-10-07 "all three"; authority = runbook GUIDE `observations_read` + §On gate closure)

| read | reader | trigger | output |
|---|---|---|---|
| **lineage** | next head on the same program line (`/runbook` seat) | authoring; `ls .dev/observations/<program>*` | `observations_read:` line in the RUNBOOK — not parkable without it |
| **coherence** | Houston, audit card | majkee invokes the audit | mech findings: does RUNBOOK/guide describe how sessions actually ran? pointers · `checked:` stamps. Observations = the process-reality half of `RUNBOOK ≈ implementation`. Grounding only — no ideas (L16.1). Clause lands in the audit card at the NEXT forge bed (homes are canonical; no in-place edit) |
| **synthesis / improvement** | **@agol**, spawned once by the closing head (or by majkee in a sitting) | the folder GREW at a closure (≥1 file promoted) | `harvest.<date>.agol.md` here: patterns across sessions, candidate amendments to guides / skills / regimes — proposals, no verdict shape; candidates become U-rows in the next RUNBOOK on any line |

Why not the head herself for synthesis: the one who ran the session is the wrong synthesizer of it — the author is not the witness. Why a growth trigger, not a schedule: a schedule is nobody's; a closure is somebody's. Cross-project incentive is welcome — observations from any practitioner line may be harvested here.

Open, named: whether harvests get read is the same orphan risk one level up; the U-row landing is the current answer.

## Event-triggered reading (majkee 2026-10-22; applies the G5 reading schedule)

Closure-only reading never fires for beds that stay open (X1). These rows fire on an event; the named reader reads at that moment.

| when (event) | who reads | what |
|---|---|---|
| a new head opens work on Houston or the germline | that head, at entry | ia-sync `.dev/session/germline-06-full-audit/raw/feedback.houston-install.oraculum.2026-10-21.md` · `nablarva-X1-to-X3-arc.agol.2026-10-22.md` · ia-sync `.dev/session/germline-01-builds-and-deploy/raw/witness.install-test.assay.2026-10-13.md` |
| before a Houston sitting or audit is launched | the umbrella head (preparation, before dispatch) | `nablarva-X1-to-X3-arc.agol.2026-10-22.md` §4 · `nablarva-X1-architecture.oraculum.2026-10-22.md` · the sitting bed's STATUS `holds:` |
| any brief touching agent config, a deploy or the tunnel | the head writing the brief, before dispatch | `nablarva-X1-architecture.oraculum.2026-10-22.md` §Structural notes · reposoma `_cold-start/card/CS.nablarva-x1-architecture.cartan.2026-10-17.md` (Codex facts) |
| a bed closes | the closer | every observation for that bed, then promote per the closure step |
| material change to a source above | the head that notices | refresh the affected row's files, note it in the bed's STATUS |

## Index (by filename date; no other index by design)

- `nablarva-X0-restarted.trajectory.2026-10-05.md` — tunnel support + issues log (T1–T11), carrier→IT note
- `nablarva-X0-restarted.atlas-ui.2026-10-07.md` — 30 harness observations (watcher baseline, manifest-over-POINT, numbering gap, what broke) + note to carrier
- `nablarva-X0-restarted.oraculum.2026-10-07.md` — carriage facts (11 turns, 0 refusals, 1 recovery, 1 reset), carrier faults, bought/cost, the skipped §4 manifest
- `nablarva-X1-architecture.trajectory.2026-10-08.md` — tunnel support log, written live (T12→); handshake + state at X1 entry
- `codex-houston-held-seat.cartan.2026-10-13.md` — Cartan (Codex) held-subagent release probe
- `nablarva-X1-architecture.oraculum.2026-10-22.md` — oraculum carrier observations, X1 checks 4–6 handoff
- `nablarva-X1-to-X3-arc.agol.2026-10-22.md` — Agol harvest #1, X1→X3 arc (synthesis, not verdict)
