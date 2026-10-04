# DESIGN — extraction.driller-onion.2026-06

`scope: raw PTY stream → reversible tokenization → sparse transforms → clean provenance-tagged events; and the tap-point map it reads from.`
`status (rescoped 2026-10-02): PTY stays the base stone (L14 D1). Meaning-from-PTY (the driller) is the FALLBACK for a CLI whose hooks/records do not yield a needed state — today agy's approval gap; NOT the primary path for Claude Code or Codex (Epoch 10-01/10-02). Discrete states (termpanum, L14 D3) are the minimal PTY reading; the driller is the maximal one, parked until a hook-less CLI needs it. Larvanizer tensor drill parked. Origin 2026-06 (month only; onion studies undated by day).`
`sources: raw.nablarva/ (prefix rule). Composed from cards A, B, E + Epoch 10-01/10-02.`

## Shape

Driller / Output Extraction Engine: raw PTY → reversible tokenization → sparse temporal/spatial transforms → mathematical reconstruction + provenance-tagged clean room events.
— `raw.nablarva/oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md:614`

Terminal onion (June reference, 183 lines — the "old onion", distinct from Nabla's 09-17 study owned by `lab`): structural tap-point map, rings 1–8; disk/JSONL at ring 7 is the clean read layer, PTY pair at ring 4 is the wire.
— `raw.nablarva/old-but-good-onion/terminal-onion-study.md:106`

PTY file-loop / file-skin: wrap vendor CLI in tmux PTY, feed via tail -F, tee via pipe-pane; files as invariant spine, one thin adapter per vendor, canary tripwire.
— `raw.nablarva/old-but-good-onion/interposition-study.md:131,134,145`

## Where the driller stands after 2026-10-02

| CLI | states without screen (Epoch) | content without screen | driller needed? |
|---|---|---|---|
| Claude Code | all 4 | yes (Stop payload, PostToolUse, sessions/<pid>.json) | no |
| Codex | working · waiting · idle; exited via L0 | yes (Stop, PostToolUse; rollout JSONL drifts) | no |
| Gemini CLI | all 4 on paper (M, no fixture) | ? | unknown |
| agy | working · idle only | transcript only (fragile) | **yes — waiting (approval) is the gap** |

Majkee 2026-10-01: "trying to escape PTY as base stone was not a good idea" — the escape was making the PTY *tap* conditional on hooks (termpanum `#gate`, struck). The driller is a different question: how much *meaning* to pull from the bytes. Answer today: as little as the vendor forces.

## Phases

| phase | origin | state | source |
|---|---|---|---|
| Terminal onion ring map (June) | 2026-06 | live reference | `old-but-good-onion/terminal-onion-study.md` |
| PTY file-loop interposition (policy §self-marked volatile) | 2026-06 | live | `old-but-good-onion/interposition-study.md` |
| Parallel-finger daemon: inotifywait on JSONL, read-only disk fingers | 2026-06 | extension, open | `old-but-good-onion/interposition-study.md` §7 |
| Driller V1 — small stateful, recommended stack | 2026-08-05 | **rescoped: fallback for hook-less CLIs** | `oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md:3.6` |
| Generalized driller | 2026-08-05 | parked, not rejected | `oraculum-basic-triangulation/02_DRILLER…md:614` · `05_DECISION…md:84` |
| Larvanizer tensor drill, tiers T0–T4, wake conditions recorded | 2026-08-04 | parked | `symetry…entity/parked.larvanizer-tensor-drill.2026-08-04.md` |
| Discrete-state parser (idle · working · waiting · exited) — the minimal PTY reading | 2026-09-30 → 10-02 | lives in `lab` (termpanum, EVENTS map) | `.dev/research/termpanum-events/events-map.v0.2026-10-02.md` |

## Boundaries

LAB/observability (lab measures; extraction is what lab would promote if a CLI needs it) · broker/room (emits events into room.brokered-journal) · Claude↔Codex seam (one adapter per vendor) · stridularium app counts with agy as optional vendor → the driller's one live customer today.

## Sources (4)

- raw.nablarva/oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md
- raw.nablarva/symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/parked.larvanizer-tensor-drill.2026-08-04.md
- raw.nablarva/old-but-good-onion/interposition-study.md
- raw.nablarva/old-but-good-onion/terminal-onion-study.md

Pointers (not copied): .dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md · .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md · meshup/lab.observability-probes.2026-08-01/raw/terminal-onion.study.2026-09-17.md (the September study)
