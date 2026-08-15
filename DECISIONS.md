# DECISIONS — Termbrana ADR Ledger

Append-only record of product-technical architecture decisions. Every entry cites the flag line or session brief that authorized it.

---

## ADR-0000 — Adoption record

**Date:** 2026-08-15  
**Authority:** nablarva flag L11 (majkee gavel 2026-08-15)  
**Session:** toolbox-termbrana-01-brief/brief.md  

### Adoption

Five founding files from `~/.remote/harvest/` adopted as substrate:

- `termbrana.project-definition.md` (Wave r0, role: founding canon)
- `termbrana.execution-plan.md` (Wave r0, role: founding canon)
- `termbrana.addendum-to-foil-theory.md` (Wave r0, role: founding canon)
- `foil_theory.md` (Nabla, role: research history)
- `foil_plugin.rs` (Nabla, role: research history)

### Host pins (M0)

Established at founding to freeze the host contract for all milestone work:

- **zellij:** 0.44.3
- **rustc:** 1.95.0
- **WASM target:** wasm32-wasip1
- **zellij-tile crate:** 0.44.3

### Decision: Independent core, Zellij-first observer

Termbrana is an independent semantic observation and navigation layer. NablaRava is one optional consumer of its neutral outputs, never a dependency.

The MVP delivers read-only navigation (no input injection or signal sending in the observer default). Semantic blocks, bookmarks, filters, search, and replay precede visual opacity.

---

## ADR-0001 — M0 view/capture path for the MVP

**Date:** 2026-08-15
**Authority:** nablarva session `toolbox-termbrana-02-m0-truthspike/handoff.md` (Part 2 assignment, execution-plan.md §12)
**Owner:** Trajectory (integration owner, M0 truth spike)
**Evidence:** `research/evidence/{t01-build-load,t02-pane-content-semantics,t03-input-behavior,t04-geometry-rendering,t05-performance,api-surface-0.44.3,pane-content-matrix}.md`

### Decision: side/tiled review pane, not an overlay; event-and-command-driven capture, not a fixed-cadence poll

**Review surface — review pane, overlay dropped from the MVP.**

The plan's T0.4 gate is: if overlay alignment or responsiveness is weak, delete overlay
and keep the review-pane design. This spike could not run the specific visual-alignment
check live (`t04-geometry-rendering.md`), but three independent, source-certain findings
already point the same direction and are sufficient to decide now rather than wait:

1. `zellij action dump-screen` — the one mechanism that could make an overlay's own
   rendered output externally verifiable — does not work on plugin panes at all
   (confirmed 3/3 on real built-in plugins). An overlay's correctness would be
   unverifiable by anything except a human's eyes, every time, forever — a maintenance
   cost a review pane (which reads and re-renders *terminal* pane content, where
   `dump-screen` works and is diffable) does not carry.
2. There is no per-cell grid anywhere in the plugin API (`pane-content-matrix.md`) —
   only host-rendered `Vec<String>` lines. True compositing (foil_theory.md §5's Porter-
   Duff "over") was already known to be simulated, not real, per the addendum; this
   spike adds that even the *simulation's* verification path is closed off headlessly.
3. Zellij's own native highlight/search/scrollback facilities operate on the terminal
   pane directly (project-definition.md §2.5: native facilities outrank replicas) — a
   side review pane composes with those for free; an overlay competes with them for the
   same screen space.

**Capture mechanism — subscribe to push events + on-demand pull, no fixed-cadence
timer.**

`get_pane_scrollback` is a pull call with real, measured cost only at the *load*
boundary so far (WASM instantiate ~25ms cold, `t01-build-load.md`); its per-call cost
under repeated polling was not measured this session (`t05-performance.md` gap).
`PaneRenderReport`/`PaneRenderReportWithAnsi` are host-push subscriptions — the host
already knows when a pane's content changed and tells you, which is strictly cheaper
than guessing a poll interval and strictly more honest about the plan's own instruction
("do not choose a fixed 4Hz poll until evidence supports it," execution-plan.md §3
T0.5). M2's capture adapter should subscribe to these events as the primary signal and
treat `get_pane_scrollback` as the on-demand "user asked for full scrollback" path, not
the steady-state one. Final cadence numbers (does the push rate need debouncing under
rapid output) remain open pending the operator pad's T0.5 sitting.

**Source grade — `rendered_ansi` ceiling, stated plainly.**

No plugin-API path in 0.44.3 reaches `raw_pty` (`pane-content-matrix.md`, governing
conclusion). `termbrana-zellij`'s M2 adapter must label every observation
`rendered_ansi` or `rendered_text` and never claim stronger fidelity
(project-definition.md §2.6). This is a structural ceiling, not a testing gap — a
future `termbrana-pty` component (addendum §3.1/§4, execution-plan.md §8) is the only
path to `raw_pty`, and remains explicitly parked.

### What remains open

Visual alignment/flicker judgment (T0.4), the interception felt-experience (T0.3), and
the full T0.5 performance envelope were not exercised live this session — headless
automation hit two independent, root-caused blockers (`dump-screen` is terminal-pane-
only; `zellij action pipe`'s round trip is unreliable against a Wasmi-interpreted
plugin within a 1s server-side completion budget). `pad.1-m0-runtime-confirm.md` hands
these to an operator sitting. None of the open items change this ADR's decision — they
would only add precision to it.
