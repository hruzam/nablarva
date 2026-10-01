# DESIGN — extraction.driller-onion.2026-06

`scope: raw PTY stream → reversible tokenization → sparse transforms → clean provenance-tagged events; and the tap-point map it reads from.`
`status: V1 small stateful driller selected · generalized driller + larvanizer tensor drill parked · origin 2026-06 (month only; onion studies undated by day)`
`sources: raw.nablarva/ (prefix rule). Composed from cleanup-00-meshup/raw/card.A, card.B, card.E.`

## Shape

Driller / Output Extraction Engine: raw PTY → reversible tokenization → sparse temporal/spatial transforms →
mathematical reconstruction + provenance-tagged clean room events.
— `raw.nablarva/oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md:614`

Terminal onion: structural tap-point map, rings 1–8; disk/JSONL at ring 7 is the clean read layer, PTY pair at ring 4 is the wire.
— `raw.nablarva/old-but-good-onion/terminal-onion-study.md:106`

PTY file-loop / file-skin: wrap vendor CLI in tmux PTY, feed via tail -F, tee via pipe-pane; files as invariant spine,
one thin adapter per vendor, canary tripwire.
— `raw.nablarva/old-but-good-onion/interposition-study.md:131,134,145`

## Phases

| phase | origin | state | source |
|---|---|---|---|
| Terminal onion ring map | 2026-06 | live | `old-but-good-onion/terminal-onion-study.md` |
| PTY file-loop interposition (policy §self-marked volatile) | 2026-06 | live | `old-but-good-onion/interposition-study.md` |
| Parallel-finger daemon: inotifywait on JSONL, read-only disk fingers | 2026-06 | extension, open | `old-but-good-onion/interposition-study.md` §7 |
| Driller V1 — small stateful, recommended stack | 2026-08-05 | selected | `oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md:3.6` |
| Generalized driller | 2026-08-05 | parked, not rejected | `oraculum-basic-triangulation/02_DRILLER…md:614` · `05_DECISION…md:84` |
| Larvanizer tensor drill, tiers T0–T4, wake conditions recorded | 2026-08-04 | parked | `symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/parked.larvanizer-tensor-drill.2026-08-04.md` |

## Boundaries

LAB/observability (feeds lab.observability-probes) · broker/room (emits events into room.brokered-journal) · Claude↔Codex seam (one adapter per vendor).

## Sources (4)

- raw.nablarva/oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md
- raw.nablarva/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/parked.larvanizer-tensor-drill.2026-08-04.md
- raw.nablarva/old-but-good-onion/interposition-study.md
- raw.nablarva/old-but-good-onion/terminal-onion-study.md
