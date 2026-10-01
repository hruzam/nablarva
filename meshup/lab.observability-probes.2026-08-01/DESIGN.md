# DESIGN — lab.observability-probes.2026-08-01

`scope: the research laboratory — controlled scenario capture, extractor replay/comparison, cross-host read discipline, 7-gate promotion into production.`
`status: live · stage-6 write-back gated on majkee go · origin 2026-08-01`
`sources: raw.nablarva/ (prefix rule). Composed from cleanup-00-meshup/raw/card.A, card.D, card.E.`

## Shape

Laboratory explicitly separated from production; proven adapter rules promote through 7 gates.
— `raw.nablarva/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md:181,313` · `00_README.md:66`

Seam probe protocol: six-stage cross-host TUI read with [SEEN]/[INFERRED]/[BLIND] discipline; motion test via hash-diff over three frames.
— `raw.nablarva/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md`

## Phases

| phase | origin | state | source |
|---|---|---|---|
| Seam probe over Tailscale (stages 1–5 run) | 2026-08-01 | live | `nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` |
| Stage 6 write-back, closed-loop verification | 2026-08-01 | prepared, gated on majkee go | `nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` |
| Laboratory + 7-gate promotion path | 2026-08-05 | live | `oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md` |
| Shadow extractor deployment (shadow-mode before promotion) | 2026-08-05 | fork C | `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` |
| Epoch observability facts: codex hooks, PTY libs, eBPF, OSC-133 markers, Zed terminal threads | 2026-08-07/08 | 5 gaps → 3 closed, 1 sub-question open | `_preflight/research.web.epoch.2026-08-07.md` · `research.web.epoch.delta.2026-08-08.md` |

## Boundaries

LAB/observability · stage 2 cross-host · Claude↔Codex seam (multi-vendor read) · feeds room.brokered-journal only through the 7 gates.

## Sources (5)

- raw.nablarva/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md
- raw.nablarva/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md
- raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md
- raw.nablarva/_preflight/research.web.epoch.2026-08-07.md
- raw.nablarva/_preflight/research.web.epoch.delta.2026-08-08.md
