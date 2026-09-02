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

> **Pointer (2026-09-02):** the T0.3 / T0.4 / T0.5 items above were exercised live in `pad.1-m0-runtime-confirm.md` and are recorded in ADR-0002 (facts 4–8); this section is retained as the historical statement and is superseded in part by ADR-0002. The decision above stands unchanged.

---

## ADR-0002 — M0 host contract FROZEN

**Date:** 2026-09-02
**Authority:** nablarva flag **L11** (majkee gavel 2026-08-15: "no parallel coding before M0 freezes the host contract"; pins locked same day) · session `toolbox-termbrana-02-m0-truthspike` (handoff.md §Gate; RUNBOOK.md §prompt-0 items 3–4)
**Gate evidence:** `pad.1-m0-runtime-confirm.md` (all fences filled 2026-09-02, operator majkee) · `research/evidence/{host-versions,t01-build-load,t02-pane-content-semantics,t03-input-behavior,t04-geometry-rendering,t05-performance,api-surface-0.44.3,pane-content-matrix}.md` · @Assay fresh-eyes pass 2026-09-02 (verdict: PASS — host matches both pin blocks; --locked build OK; 8/8 fences filled; fold additive only; all folded claims trace to fences; ADR-0001 uncontradicted; WARN: README rows 28/30/53 + ADR-0001 "what remains open" prose stale)
**Revision r2 (majkee direction 2026-09-02):** lock with a re-verification loop (§Loop) · home = parity target, not excluded (§Hosts)
**Gaveled by:** majkee, 2026-09-02 (session toolbox-termbrana-02-m0-truthspike; driver Oraculum; verbal gavel "I am agreeing with that" on r2)

### Decision: the host contract is frozen as below; all M1/M2 code targets exactly this

| pin | value | provenance (verified 2026-09-02, office) |
|---|---|---|
| zellij | **0.44.3** | pacman `zellij 0.44.3-1`, Arch build (packager alerque@archlinux.org, 2026-05-14) delivered via **Manjaro `stable`** branch |
| rustc / cargo | **1.95.0** | rustup toolchain `1.95.0-x86_64-unknown-linux-gnu` — distro-independent |
| target | **wasm32-wasip1** | rustup target installed |
| crate | **zellij-tile = 0.44.3** | Cargo.lock; build `--locked` |
| leading host | **office** (hruzam-120922) · `ID=manjaro`, `ID_LIKE=arch` | the host every fact below was verified on |

The pin is **empirical**, verified twice on the actual host (2026-08-15/16 PAD-01 + pad.1 STEP 0; 2026-09-02 STEP 0′). It is not a repo-tracking promise: Manjaro stable lags Arch by design, and the 2026-08-15 research note's "Arch extra in sync with upstream" reasoning is corrected in `host-versions.md` (right package origin, wrong delivery timing). Bumping any pin = a new ADR, not a drift.

### Hosts — leading host and parity hosts

- **Leading host = office.** All evidence in this ADR was produced there; it is the reference state.
- **Parity hosts (home, any common host)** are brought to the *same state as the leading host*, not excluded from the contract: packages through ia-sync where the package set allows (zellij 0.44.3-1 from Manjaro stable — note it must be the exact build; if the host's mirror branch has moved past it, pin from the package cache / Arch Linux Archive), rustup toolchain 1.95.0 + `wasm32-wasip1` target; where a package path is not possible, a **navigation MD** (ia-sync pattern — an operator-facing walk with an agent on the line) does it by hand.
- A parity host counts as *verified* only after `pad.1` **STEP 0′** is sat on it and a dated block is appended to `host-versions.md`. Until then, "termbrana builds/runs" is a statement about office only. Home is currently unverified (zellij absent as of 2026-09-02).

### Facts of the contract that M1/M2 design against (runtime-confirmed, not docs-trusted)

1. **Source grade ceiling = `rendered_ansi`, subscription-only.** `get_pane_scrollback` returns plain text (ANSI stripped; fence 2). `PaneRenderReportWithAnsi` carries SGR sequences (fence 2b — observed on the probe's own pane report; fixture-line codes not isolated). No plugin-API path reaches `raw_pty` (source-certain, ADR-0001).
2. **`get_pane_scrollback(full=0)` = viewport only** (`above=0 below=0`); `full=1` is bounded by zellij's scrollback cap **10 000 lines** (fence 5).
3. **Push events are layout/focus-driven, not content-driven.** An unsubscribed plugin received zero events during a 100 000-line burst; server ~0.6 % CPU (fence 5).
4. **Blind render-report subscription self-feeds.** Including the plugin's own pane loops report→render→report (~300K events/min), degrading the session past pane-close (fence 2b).
5. **Interception is real and reversible, but asynchronous.** `InterceptInput` is granted after a user prompt; intercepting before the grant is a silent no-op (fence 3, F1). While intercepting, the operator cannot type the release; `zellij --session <s> action pipe …` from outside the session works as the off-switch (F2, F3).
6. **`zellij action pipe` reaches the plugin reliably; the CLI echo (`cli_pipe_output`) does not land** under an interactive client (0/2). Evidence route = the plugin's own render, or a file sink (fence 2).
7. **Plugin-pane rendering is stable under resize and tile/float toggles** (SSH-mediated judgement); one resize drag emits dozens of `PaneUpdate`s (fence 4).
8. **A plugin on a non-active tab stopped advancing; a direct message woke it.** Cause not separated (starvation vs missed re-render, R1 — fence 5).

### Adapter laws derived (bind M1-core interfaces and the M2 zellij adapter)

- L-A1 · Subscribe to `PaneRenderReport(WithAnsi)` **only for the target pane(s)**; never the adapter's own pane; debounce bursts.
- L-A2 · Treat `get_pane_scrollback` as the on-demand "full pull" path (≤10 000 lines), never the steady-state path (ADR-0001 stands).
- L-A3 · Any interception feature: request → await the grant event → intercept; ship an out-of-band release; observer mode never requests `InterceptInput` (L11 constraint).
- L-A4 · Re-sync target state on tab/visibility return (R1).
- L-A5 · Label every observation `rendered_ansi` or `rendered_text`; never claim more (project-definition §2.6).
- L-A6 · Design the operator surface for a non-expert: focus and mode must be visible in the plugin's own render (operator-UX finding, fence 5).

### Loop — re-verification before M2 code (the "not built on sand" clause)

This freeze is a lock with a scheduled return, not a one-way door. **Before the first M2 (zellij-adapter) code lands**, a second operator pad (`pad.2-m0-loop`) is sat on the leading host and re-proves:
- the five pins (STEP 0′ shape) — drift = STOP, ADR-0003;
- the open items below, each with a declared verdict pair;
- STEP 2b with the fixture line *isolated* (subscribe with the probe's own pane excluded — requires the L-A1 fix in the harness first).
If any *fact* above is refuted, this ADR is superseded by ADR-0003 naming the refuted line; the pins and the unrefuted facts carry over. M1-core work (host-independent by definition, law 2.3) is not blocked by the loop.

### What remains open (does not block the freeze; owned by the Loop / M2 fixture set)

- Per-call cost of `get_pane_scrollback` under repeated polling — unmeasured (t05 gap).
- R1 (tab-return behaviour) — unresolved.
- Alternate-screen capture semantics; CJK/emoji fidelity — not exercised (matrix rows deferred).
- Fixture-line SGR codes through `PaneRenderReportWithAnsi` — not isolated (2b caveat).
- Home parity — unverified (§Hosts).

### Consequences

- flag L11's "no parallel coding before M0 freezes" clause is satisfied on gavel → session **03-tunnel** opens (RUNBOOK already authored); @Flight branch group eligible per flag deferral thresholds.
- M1 backlog receives: harness ordering fix (L-A3), own-pane exclusion + debounce (L-A1), tab re-sync (L-A4), and the `pad.2-m0-loop` authoring task.
- ia-sync receives the home-parity task (packages or navigation MD) — machine layer, out of termbrana's tree.
- Pre-registered M2 benchmark bar (L11) is re-tunable only BEFORE M2 begins — nothing here changes it.

Draft lineage: r1 → r2 (majkee direction 1A loop / 1B host parity, 2026-09-02); draft file retired to the session bed.
