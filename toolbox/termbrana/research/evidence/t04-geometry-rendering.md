`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence`

# T0.4 — Geometry and rendering

## Confirmed from this session

- **Floating plugin pane geometry is queryable numerically and precisely**, without
  needing eyes on a screen: `zellij action list-panes -a -j` (or `-g` for geometry
  alone) returns exact `pane_x/y`, `pane_content_x/y`, `pane_rows/columns`,
  `pane_content_rows/columns` for every pane including floating plugin panes. Observed
  for the harness's own floating pane: `pane_x=20 pane_y=7 pane_rows=11
  pane_columns=40` (content area `21,8` `9x38` after the border). This means geometry
  *correctness* (does a floating pane land where requested, does resize change the
  reported numbers) is fully automatable and does not need a human — only *visual*
  alignment/flicker judgment does (see gap below).
- **`zellij action dump-screen` works reliably for terminal panes** (`-p terminal_N`),
  confirmed multiple times with real multi-line content (shell prompt, ~15 lines of
  substrates config-loader banner text) captured byte-correct to a file. This is the
  proven, working half of the "compare direct native regex highlights with re-rendering
  a copied pane" T0.4 probe — a terminal pane's content is trivially diffable
  programmatically.
- **`zellij action dump-screen` does NOT work for plugin panes**, confirmed on three
  distinct built-in plugins (`tab-bar`, `status-bar`, `about`), every attempt returning
  zero bytes regardless of `--ansi`/`--path`/stdout. This is a hard, reproducible
  finding, not a one-off: it means the review-pane-vs-overlay comparison this probe
  wants ("compare direct native regex highlights with re-rendering a copied pane") can
  only be done by capturing the *terminal* side (works) and inspecting the plugin's
  rendered result *visually*, live — there is no headless capture path for a plugin's
  own screen in 0.44.3.

## Load-bearing consequence for the T0.4 gate

The plan's T0.4 gate is: *"if overlay alignment or responsiveness is weak, delete
overlay from the MVP and keep the review-pane design."* Because plugin-pane content
cannot be captured headlessly at all, **this specific gate question cannot be answered
from this session alone** — "is the overlay's alignment weak" is a visual judgment this
harness has no way to make without a human watching a real terminal. Everything else
this spike found (dump-screen terminal-only, PaneRenderReport push-only,
get_pane_scrollback string-only, no per-cell grid anywhere) already independently
argues for the review-pane design over a compositing overlay — see ADR-0001 for the
full reasoning — but the *specific* "does it flicker/misalign" empirical check is
deferred to the operator pad, honestly, rather than assumed.

## What is NOT confirmed
→ visual alignment under resize confirmed 2026-09-02, see §Confirmed by pad.1 sitting

- Visual alignment of a floating pane's re-rendered content against the pane it copies
  from, under resize and rapid updates — needs eyes.
- Whether resize events reliably trigger a fresh `render()` call with correctly updated
  `rows`/`cols` (the numeric geometry query confirms the *pane's* size changes; it does
  not confirm the plugin's `render(rows, cols)` callback fires with matching values in
  a timely way, since that can only be observed via the same broken dump-screen/pipe
  paths).

## Operator follow-up

`pad.1-m0-runtime-confirm.md` includes: open the harness plugin tiled, then floating;
resize the terminal/window; watch for flicker or stale content; visually compare a
`dump-screen`-captured terminal pane's regex-highlighted content (native) against the
plugin's re-rendered echo of the same content (copied-pane path) side by side.

## Confirmed by pad.1 sitting, 2026-09-02 (operator majkee over SSH from home; driver Oraculum)

Judgement is SSH/Tailscale-mediated: operator on Konsole at home, session running on
office, over Tailscale (fence 4).

- **Verdict: `<STABLE, NO FLICKER/MISALIGNMENT>` in the plugin pane.** The operator
  manually resized the Konsole window several times, and toggled tiled↔floating
  (`Ctrl+p e`) twice — pane slot order changed (normal re-embed behavior). Photo shows
  the plugin pane (now left, tiled) with aligned borders and a continuous log,
  `[0358]..[0420]`, no stale lines.
- **Control datum:** the terminal (shell) pane on the same screen showed heavy
  artefacts under identical resizes — its zsh powerline prompt was redrawn/smeared
  roughly 40 times (SIGWINCH redraw). This is judged a transport/zsh-side artefact,
  not a termbrana finding, but it means the plugin pane behaved *better* than an
  ordinary terminal pane under the same resize stress, not merely "as good."
- **Cadence datum (T0.5-relevant):** one resize drag produced dozens of `PaneUpdate`
  events (sequence counter moved 0193 → 0420 across the resizes).
- **ADR-0001 review-pane reservation: closed.** This removes the last open
  reservation the T0.4 gate above left pending on visual alignment.
