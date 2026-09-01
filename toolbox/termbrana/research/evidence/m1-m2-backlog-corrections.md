`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 deliverable (execution-plan.md §3 "corrected implementation backlog")`

# Corrections to Milestone 1 / Milestone 2, from M0 truth-spike evidence

This does not replace `termbrana.execution-plan.md` §4/§5 — it lists the specific
places evidence from this spike should change how those milestones are read or
sequenced, each citing the evidence file that forced the correction.

## Milestone 1 (pure core) corrections

- **T1.1 `SourceGrade`**: implement the type with exactly the four grades already in
  project-definition.md §4 (`raw_pty`/`rendered_ansi`/`rendered_text`/`derived`), but
  the core's own doc comments/tests should assert that `raw_pty` is *unreachable* from
  the Zellij adapter path — a compile-time or at least a strongly-documented invariant,
  not just a convention. `pane-content-matrix.md`'s governing conclusion is the reason:
  nothing in `termbrana-zellij` can ever legitimately construct a `raw_pty` observation,
  and a future `termbrana-pty` component is a different crate entirely. Encoding this
  as "the Zellij adapter's observation constructor only offers
  rendered_ansi/rendered_text/derived" prevents a future contributor from plausibly
  mislabeling a capture out of convenience.
- **T1.2 block indexing, generic heuristic lane**: plan for line-wrap awareness up
  front. `pane-content-matrix.md`'s "wrapped long lines" row confirms
  `get_pane_scrollback`/`PaneRenderReport*` hand you already-host-wrapped lines with no
  "this was one logical line" marker — a heuristic block detector that assumes one
  scrollback line == one logical line will misclassify wrapped output (e.g. a long
  command line wrapped across three viewport rows) unless it re-joins using terminal
  width, which the core does not currently have as an input. Flag this as a design
  input needed before T1.2 starts, not something to discover mid-implementation.
- **T1.4 JSONL, "derived records reference parent sequences"**: this requirement was
  already correct and is now empirically reinforced — since `PaneRenderReport`/
  `PaneRenderReportWithAnsi` are two *independently* pushed views of what may be the
  same underlying render tick (`api-surface-0.44.3.md`), the adapter will sometimes
  have two observations for what is conceptually one moment. The JSONL schema/parent-
  sequence design should be able to express "these two observations share a render
  tick" without inventing a new concept — likely just two records with adjacent
  sequence numbers and a shared (optional) correlation field, not a new relationship
  type.

## Milestone 2 (read-only Zellij MVP) corrections

- **T2.2 capture adapter — mechanism choice is now decided, not open.** ADR-0001: the
  adapter's steady-state capture should subscribe to `PaneRenderReport`/
  `PaneRenderReportWithAnsi` (push) as primary, and call `get_pane_scrollback(pane_id,
  true)` only for the explicit "load full scrollback" user action, not on a timer. This
  changes T2.2's "capture viewport live and full scrollback only when required" from a
  vague instruction into a concrete design: *live = subscribe*, *full scrollback =
  on-demand pull*.
- **T2.2 "attach correct source grade"** — the adapter's default grade should be
  whichever of `rendered_text`/`rendered_ansi` the *no-ansi* `PaneRenderReport`
  subscription yields by default, with `rendered_ansi` available as an explicit
  higher-detail subscription for consumers (e.g. a future syntax-aware block classifier)
  that opt in. Do not default to the ansi-carrying variant just because it is "more
  data" — project-definition.md §2.1 wants provenance to be honest, and ansi payloads
  need `strip_sgr`-equivalent handling wherever plain text is assumed (foil_theory.md
  §3's warning about naive CSI skipping still applies to any code path that touches
  `rendered_ansi` strings).
- **T2.4 native host enhancements — new item to add: `ReadCliPipes` is NOT needed.**
  `api-surface-0.44.3.md` found this permission only because the M0 probe *harness*
  needed it to answer CLI queries about itself; the actual observer-mode product has no
  reason to call `cli_pipe_output`. T2.5's permission-tier discipline ("Observer MVP
  requests only the capabilities it actually exercises") should explicitly exclude
  `ReadCliPipes` from the M2 permission request list — it is easy to accidentally carry
  it forward by copying the M0 harness's `load()` verbatim, since the harness's own
  code comments explain why it needs it but a future implementer skimming the file
  might not notice the distinction.
- **T2.4 "use regex highlights ... consume highlight-click events"** — no contradicting
  evidence found this session; not blocked, not newly informed. Left as-is.
- **New pre-T2.1 item worth adding: bootstrap dependency on an attached client.** This
  spike found that a Zellij session with **no attached client cannot load or focus any
  plugin** (`Loaded plugin '...'` never followed by success; `No connected clients
  found - cannot load or focus plugin` in `zellij-session.log`). This is obvious for a
  human-run session (a human is always attached) but matters for any future automated
  test harness for `termbrana-zellij` (e.g. CI): a bare `zellij attach -b` session is
  not enough to exercise plugin-loading code paths; a real or tmux-hosted client attach
  is required. Worth one line in a future CONTRIBUTING/testing doc so the next person
  doesn't lose the hour this session did rediscovering it.
