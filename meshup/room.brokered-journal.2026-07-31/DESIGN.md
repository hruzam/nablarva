# DESIGN — room.brokered-journal.2026-07-31

`scope: the production room — broker + append-only journal + adapter-owned PTY sessions + cursor projections (stage 1 → stage 2).`
`status: live · S1–S8 locked (triad 2026-07-31) · hybrid Y+Z selected 2:1 · origin 2026-07-31`
`sources: raw.nablarva/ (prefix rule) — cite, never copy. Composed from cleanup-00-meshup/raw/card.A, card.D, card.E.`

## Shape

`larvad` broker + append-only NDJSON journal + adapter-owned PTY sessions + sparse cursor projections;
Unix socket same-host, SSH to one central broker cross-host (S7).
— `raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md:25` · `01_ARCHITECTURE_ROOM_AND_BROKER.md:28`

Journal has two projections: **braid** = raw interleaved audit trail, **book** = chapter-folded reasoning view;
book derived from braid, braid never destroyed.
— `raw.nablarva/nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md:161-163`

## Phases

| phase | origin | state | source |
|---|---|---|---|
| X — primary-larva file-ledger room, cooperative convention, fails soft | 2026-07-31 | superseded (2:1 vote) | `oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` · `_preflight/task.T3-T4.orchestration-fork.md:38` |
| Y — larvad CREATURE: static binary, PTY adoption, structural turn-quota, fails hard | 2026-07-31 | folded into hybrid | `oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` |
| Wave hybrid V1 — closer to Y, Python-stdlib candidate, NDJSON events, larva-agent-{claude,codex} adapters | 2026-08-05 | selected direction | `oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` · `03_COST_COMPLEXITY_AND_STAGED_DECISION.md` |
| Braid-and-Book journal projections | 2026-08-01 | live stone | `nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md` |
| Four-phase blind triangulation as consultation lease | 2026-07-31 | Z novel organ 2 | `oraculum-basic-triangulation/triad.comparison.2026-07-31.md` |
| Two-lane evidence channel (conversation vs machine events) | 2026-08-05 | fork A, open | `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md:226` |
| Adapter capability handshake | 2026-08-05 | post-V1 | `oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md:4.15` |

## Records, not design

`oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` (session close) ·
`nablarva.wave.full-report.2026-08-05.md` (concat of 01–07) · `brief.triangulation.2026-07-31.md` (sealed Z brief) ·
`06_ORACULUM_TRANSMISSION.md` · `07_AI_HANDOFF.md` (synthesis chapters).

## Boundaries

stage 1 · stage 2 (S7) · stage 3 stridularium (organ naming = gavel docket 7) · broker/room · naming.
Locks live in `.dev/session/flag.md`; this file does not re-litigate them.

## Sources (14)

- raw.nablarva/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/brief.triangulation.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/00_README.md
- raw.nablarva/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md
- raw.nablarva/oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md
- raw.nablarva/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md
- raw.nablarva/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md
- raw.nablarva/oraculum-basic-triangulation/07_AI_HANDOFF.md
- raw.nablarva/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md
- raw.nablarva/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md
- raw.nablarva/_preflight/task.T3-T4.orchestration-fork.md
- raw.nablarva/nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md
