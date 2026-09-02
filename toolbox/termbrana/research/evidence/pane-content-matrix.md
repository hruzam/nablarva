`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 deliverable (execution-plan.md §3 T0.2 done-when) · cites t02-pane-content-semantics.md`

# Pane-content matrix — what survives, what is normalized, what is lost

Source-grade vocabulary is project-definition.md §2/4's, verbatim:
`raw_pty` / `rendered_ansi` / `rendered_text` / `derived`.

**Never infer raw-byte fidelity from visual similarity** (execution-plan.md §3 T0.2,
project-definition.md §2.1/§2.6). Every row below is either a direct source-level fact
(cited) or explicitly marked pending live confirmation — nothing here is an assumption
dressed as an observation.

## Capture mechanisms, by grade they can ever produce

| Mechanism | Max grade obtainable | Why (evidence) |
| --- | --- | --- |
| `get_pane_scrollback(pane_id, get_full_scrollback)` | `rendered_ansi` or `rendered_text` (host-determined, no per-call choice) | Signature has no ansi/raw parameter — returns `PaneContents { viewport: Vec<String>, ... }`, strings only. `api-surface-0.44.3.md`. |
| `Event::PaneRenderReport` (subscribe) | `rendered_text` (normalized, no ansi) | Separate internal cache (`all_pane_contents`) from the ansi variant — structural evidence it strips styling. `api-surface-0.44.3.md`. |
| `Event::PaneRenderReportWithAnsi` (subscribe) | `rendered_ansi` | Separate internal cache (`all_pane_contents_with_ansi`). `api-surface-0.44.3.md`. |
| `zellij action dump-screen` (host CLI, not plugin API) | `rendered_ansi` (with `--ansi`) or `rendered_text` (without) — **terminal panes only** | Confirmed working for terminal panes, confirmed **non-functional for plugin panes** (3/3 tested: tab-bar, status-bar, about). `t04-geometry-rendering.md`. Not a plugin-facing mechanism at all — belongs to the host CLI, useful only for capturing what a *target* terminal pane shows, never what Termbrana's own review pane shows. |
| any plugin API in 0.44.3 | never `raw_pty` | No call anywhere in `zellij-tile`/`zellij-utils` returns per-cell `(glyph,fg,bg,attrs)` or original PTY bytes; every content-bearing return type is `Vec<String>`. `api-surface-0.44.3.md`. Confirms addendum-to-foil-theory.md §3.3: `raw_pty` is future-`termbrana-pty`-only, never available to a Zellij plugin. |

## Per-fixture survives/normalized/lost

Fixture list per execution-plan.md §3 T0.2. Status column: `SOURCE-CONFIRMED` (settled
by the table above, applies regardless of fixture content) or `PENDING-OPERATOR`
(needs the actual byte-for-byte capture from `pad.1-m0-runtime-confirm.md`).

| Fixture | Grade ceiling | Status | Note |
| --- | --- | --- | --- |
| Plain text | `rendered_text` / `rendered_ansi` | SOURCE-CONFIRMED | No transformation expected beyond whatever line-wrapping the host already applied before your plugin sees it. |
| 8-color / 256-color / true-color SGR | `rendered_ansi` only via `PaneRenderReportWithAnsi` or (if the host embeds it) `get_pane_scrollback` strings; **lost** entirely from `PaneRenderReport` (no-ansi) and from `rendered_text` grade by definition | SOURCE-CONFIRMED (grade ceiling) / OPERATOR-CONFIRMED 2026-09-02 | Whether `get_pane_scrollback`'s plain `get_pane_scrollback` call embeds ANSI in its strings or always strips it is not fixed by the signature — needs one live capture to settle definitively for the M2 adapter's default path. Live capture 2026-09-02: `get_pane_scrollback` STRIPS ANSI (plain "red bold-green orange256 truecolor", no `<ESC>`); `PaneRenderReportWithAnsi` carries `<ESC>[…m` → `rendered_ansi` is subscription-only for the M2 adapter. (pad.1 fences 2, 2b) |
| Cursor movement / erased text | `rendered_*` (post-erase state only) | SOURCE-CONFIRMED | The API hands you the host's *reconstructed* current grid, serialized to lines — there is no event stream of intermediate cursor motions, only the settled result. Anything erased before capture is unrecoverable by definition (matches foil_theory.md §2: no cell-level history, only current state). |
| OSC title / OSC 52 attempts | not exposed as pane *content* at all | SOURCE-CONFIRMED | `Event` has no OSC-title/clipboard-attempt variant surfaced to plugins in the enums read this session; a title change surfaces only via host UI (tab/pane title fields in `list-panes`), not as scrollback text. An OSC 52 clipboard write is a host-level security concern (project-definition.md §2.6 / addendum §3.2), not something the plugin API echoes back for inspection. |
| Alternate-screen content | `rendered_*`, whichever screen is currently active | PENDING-OPERATOR | Whether `get_pane_scrollback` transparently follows the active screen or exposes any indicator of alt-screen state was not verified live this session. Not exercised by the 2026-09-02 sitting — deferred to pad.2-m0-loop (ADR-0002 §Loop, majkee decision 2026-09-02: "loop"). |
| Wide CJK glyphs, emoji, combining marks | `rendered_*`, width-aware per source | SOURCE-CONFIRMED (mechanism) / PENDING-OPERATOR (fidelity) | `zellij-utils/src/data.rs` implements its own `extract_text_by_columns`/`extract_text_from_column` helpers using `.width()` (unicode-width) specifically to handle wide characters correctly for *selection* extraction — evidence the host is width-aware internally, not blind-byte-column slicing. Whether an emoji ZWJ sequence or combining mark survives as one grapheme through the `String` boundary needs a live capture. Fidelity half not exercised by the 2026-09-02 sitting — deferred to pad.2-m0-loop (ADR-0002 §Loop, majkee decision 2026-09-02: "loop"). |
| Wrapped long lines | host-determined wrap, not plugin-controlled | SOURCE-CONFIRMED | `viewport: Vec<String>` is one entry per **rendered** line, i.e. already wrapped by the host's terminal-width model before the plugin ever sees it — Termbrana cannot recover "this was originally one long line" from `get_pane_scrollback` alone without also tracking terminal width and re-joining heuristically. |

## Governing conclusion for ADR-0001

No mechanism in the 0.44.3 plugin API — `get_pane_scrollback` in either mode, or either
`PaneRenderReport*` subscription — can produce a `raw_pty`-grade observation. The
strongest grade obtainable is `rendered_ansi` (via `PaneRenderReportWithAnsi`, a push
subscription — confirmed 2026-09-02; `get_pane_scrollback` strips ANSI on this host,
so the pull path yields `rendered_text` only). This is not a shortfall of this
spike's testing depth; it is a structural ceiling of the API surface itself, confirmed
from the vendored crate source. Any Termbrana capability description must say so
plainly (project-definition.md §2.6) and any future push toward stronger fidelity
requires the parked `termbrana-pty` component (addendum §3.1/§4), not a deeper dig into
this plugin API.
