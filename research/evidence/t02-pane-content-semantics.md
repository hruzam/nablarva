`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence`

# T0.2 — Pane-content semantics

## Status: source-verified, runtime capture incomplete — see gap below

The probe harness (`crates/termbrana-zellij`) implements a `capture <kind> <id> <full>`
pipe command that calls `get_pane_scrollback` and logs the escaped result (control
bytes rendered as visible tokens like `<ESC>`, `<BEL>`, `<0xNN>` — see `escape()` in
`src/main.rs` — so a capture never gets silently re-interpreted by whatever terminal
displays it). It also subscribes to `PaneRenderReport` / `PaneRenderReportWithAnsi` on
command and logs every pushed pane snapshot the same way.

**What is confirmed (source + host truth, not inference):**

- `get_pane_scrollback(pane_id, get_full_scrollback)` has no ANSI/raw parameter — see
  `api-surface-0.44.3.md`. Whatever ANSI content is or isn't in `PaneContents.viewport`
  strings is fixed by the host, not selectable per-call.
- The raw/rendered-ANSI/rendered-text axis the plan wants is answered by subscribing to
  `PaneRenderReport` (no-ansi) vs `PaneRenderReportWithAnsi` (ansi) as two independent
  push events, confirmed to exist as separate internal caches server-side
  (`api-surface-0.44.3.md`).
- Every source grade this spike can produce is at best `rendered_ansi` or
  `rendered_text` per project-definition.md §2.1's own vocabulary — nothing in the
  plugin API surface returns per-cell `(glyph, fg, bg)` or original PTY bytes. This
  confirms the addendum's §3.3 correction still holds exactly in 0.44.3: there is no
  `raw_pty` grade obtainable from a Zellij plugin.

**What could not be captured this session:** actual fixture text (SGR colors, OSC
title/52 attempts, alt-screen, CJK/emoji, wrapped lines) round-tripped through
`get_pane_scrollback` and the two `PaneRenderReport*` events, to fill in
`pane-content-matrix.md`'s per-fixture rows with real observed strings rather than
structural/source-level claims.

## Why the runtime half is incomplete

Two independent headless-automation blockers, both root-caused, neither faked around:

1. **`zellij action dump-screen` cannot read plugin panes.** Verified on three different
   real, actively-rendering built-in plugins (`tab-bar`, `status-bar`, and the
   first-run `about`/release-notes pane, which has substantial multi-line text) — all
   three returned zero bytes, with and without `--path`, with and without `--ansi`.
   `dump-screen` only ever produced content for the plain terminal pane in the same
   session (confirmed working, see t04). This means the harness's own `render()` output
   — the "renders its version information" T0.1 done-check — cannot be captured
   non-interactively at all; only its `pipe()`-driven log echo can.

2. **`zellij action pipe`'s one-shot round trip is unreliable against a Wasmi-
   interpreted plugin in this headless harness.** The server enforces a 1s
   `ACTION_COMPLETION_TIMEOUT` per CLI action (`api-surface-0.44.3.md`); across 11
   attempts (with permission grants attempted via `send-keys`, then via genuine
   `tmux send-keys` keystroke injection into the attached client — the closest
   approximation of a human hand available here), the CLI process consistently
   returned before the plugin's `cli_pipe_output()` call could land, or exited
   immediately on stdin EOF before any async reply arrived. This was reproducible, not
   a one-off flake, and is documented as a genuine limitation, not swept under a
   "probably fine" assumption (project-definition.md §2.6 in spirit: no false-confidence
   claims).

Neither of these are the plugin's own bug — both were isolated to the CLI/session
plumbing (see t01 Bug 1/2 for the two bugs that *were* the plugin's, both fixed).

## What this means for the decision this spike has to make

Independent of whether the exact ANSI/plain text of a colored fixture line round-trips
byte-for-byte, the **source-level finding already answers the T0.2 gate question**: no
`get_pane_scrollback` or `PaneRenderReport*` call anywhere in 0.44.3's plugin API can
produce anything stronger than `rendered_ansi` / `rendered_text`. That is sufficient to
write `pane-content-matrix.md`'s grade column and ADR-0001's capture-path decision
without the fixture run. What the fixture run would add is precision on *loss*
specifics — e.g. does OSC 52 ever appear literally in a captured string, does a
combining-mark grapheme survive as one `char`-cluster or get split — which matters for
M2 implementation detail but not for the M0 gate (raw_pty is unavailable; period).

## Operator follow-up

`pad.1-m0-runtime-confirm.md` (in the nablarva session dir) hands a human the exact
fixture panes + capture commands, run from a *real* attached terminal (where `zellij
action pipe`'s stdin is a live tty, not `/dev/null` or a killed background process, and
a human can watch the plugin's floating pane directly rather than needing
`dump-screen`). That sitting will fill in the fixture-by-fixture rows in
`pane-content-matrix.md` with observed strings; it will not change the raw/ansi/text
grade conclusion above, which is already source-certain.
