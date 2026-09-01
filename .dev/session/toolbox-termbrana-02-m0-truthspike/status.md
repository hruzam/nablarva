# status — session 02 (M0 truth spike) · live position

`updated: 2026-08-15 (Houston) · gate: M0 host contract — NOT YET FROZEN`

## Done (Trajectory, 5 commits 3b6deab..e319ed4, pushed)

- Probe harness: smallest compiling plugin for zellij 0.44.3 (`crates/termbrana-zellij`,
  `[[bin]]` not cdylib — loader needs `_start`+`load`; real bug found+fixed).
- Evidence in `termbrana/research/evidence/`: t01-build-load · api-surface-0.44.3 ·
  t02-pane-content-semantics · t03-input-behavior · t04-geometry-rendering ·
  t05-performance · pane-content-matrix · m1-m2-backlog-corrections (+ raw session log).
- ADR-0001 appended to DECISIONS.md (view/capture path) — load-bearing now, does not
  wait on the pad.
- API mismatches vs docs recorded: scrollback bool = full-scrollback (no ansi/raw
  param) · PaneRenderReport(+WithAnsi) exist but push-subscribe only · undocumented
  ReadCliPipes permission · 1s ACTION_COMPLETION_TIMEOUT on action CLI · bin-not-cdylib.
- Structural verdicts complete: no `raw_pty` grade reachable from a plugin (source-
  certain) · observer mode needs no global interception.

## Pending → gate closure sequence

1. **OPERATOR: sit `pad.1-m0-runtime-confirm.md`** (this dir) — settles: ANSI embed/strip
   default of scrollback (STEP 2) · live interception feel (STEP 3) · visual
   alignment/flicker (STEP 4) · performance envelope (STEP 5 — largest gap).
2. Trajectory (or Delta) folds pad results into the t02–t05 PENDING-OPERATOR rows.
3. **@Assay-class fresh-eyes pass** over the full M0 evidence set (handoff gate law).
4. Houston freezes the host contract → session 03 (m1-core) opens, @Flight branch
   group eligible.
