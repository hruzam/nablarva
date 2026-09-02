`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence`

# T0.5 — Performance limits

## Confirmed from this session

- **Cold WASM load/instantiate cost under Wasmi is small and consistent**: 8 loads of
  the harness across this session, all 24.86ms–28.09ms
  (`plugin_loader.rs:151` log line, see `t01-build-load.md` for the full list). This is
  the host-side "compile+instantiate a ~1.6MB wasm module" cost, not plugin logic cost
  — but it's a real, repeatable number, and it's small enough that reload-on-change
  during M2 development will not be a friction point.
- **The host runs plugins on the Wasmi interpreter, not wasmtime** (`Loading plugins
  using Wasmi interpreter`, logged on every session start). This is a genuinely useful
  fact the execution plan does not mention anywhere: an interpreter, not a JIT, is a
  meaningfully different performance regime than a naive "WASM is basically native
  speed" assumption would suggest, and should inform the T0.5 gate's "do not choose a
  fixed 4Hz poll until evidence supports it" instruction — a poll loop doing nontrivial
  per-tick work (e.g. re-parsing scrollback) pays interpreter overhead on every tick,
  not just at load.
- **`zellij action` CLI round trips have a hard 1-second server-side budget**
  (`ACTION_COMPLETION_TIMEOUT`, `route.rs:36`, confirmed by source and by 11
  reproduced timeouts this session). Any future tooling (including a possible
  termbrana CLI companion) that shells out to `zellij action pipe` synchronously
  should not assume sub-second turnaround is guaranteed under load.

## What is NOT confirmed — this is the largest gap of the five probes
→ large-scrollback + hidden-plugin scenarios confirmed 2026-09-02, see §Confirmed by pad.1 sitting (per-call polling cost remains unmeasured, see that section)

None of the actual T0.5 scenarios (rapid continuous output, 100k-line scrollback,
viewport-only vs full-scrollback capture cost, update-driven vs timer-polling capture,
hidden vs visible plugin state, target-pane-closure-during-observation) were run this
session. All of them require either:

1. A stable, held-open `zellij action pipe` or equivalent channel to pull timing data
   out of the plugin while it runs — blocked by the same round-trip unreliability
   documented in t02/t03, or
2. Direct human observation of CPU/responsiveness while interacting live.

This is the probe most dependent on a genuinely interactive session (a background
`tmux`/`script`-hosted client does not generate the kind of rapid, bursty, human-paced
interaction this probe needs to be meaningful) and is fully deferred to the operator
pad rather than approximated with a synthetic substitute that would misrepresent real
usage.

## Operator follow-up

`pad.1-m0-runtime-confirm.md` includes: `yes | head -100000` or similar into a fixture
pane to build a large scrollback, toggle the harness's `subscribe_render_reports` and
watch CPU (`top`/`htop` alongside the session), compare a `capture ... 1` (full
scrollback) request's latency against `capture ... 0` (viewport only), hide/show the
plugin pane and watch whether `render()` keeps firing while hidden, close a captured
target pane mid-observation and confirm the harness's `get_pane_scrollback` error path
(already implemented — see `src/main.rs`'s `capture` command, which logs `Err` results
same as `Ok`) behaves as expected rather than crashing.

## Confirmed by pad.1 sitting, 2026-09-02 (operator majkee over SSH from home; driver Oraculum)

Probe instance was NOT subscribed to render reports for this step (fresh session
after the 2b storm). Verdict: **`<SESSION STAYS RESPONSIVE, PLUGIN RESUMES CLEANLY>`**
— with one unresolved refinement (R1 below) (fence 5, plus the storm carried over
from fence 2b).

- **`yes "termbrana perf fixture line" | head -100000` → `cat`, 100,000-line
  fixture:** while unsubscribed, zero events were delivered to the probe pane —
  `PaneUpdate` is layout/focus-driven, not content-driven, so a `cat` flood in an
  unrelated pane produces no plugin traffic. Session stayed responsive throughout.
- **CPU:** `zellij --server` measured ~0.6% CPU after the cat (RES 107M); the
  operator additionally observed CPU wandering 0.6–1.9% with no correlation to the
  cat (background noise, not attributable to the fixture).
- **Host fact:** zellij's scrollback cap is 10,000 lines (`SCROLL: 0/10000` in the
  pane title) — so `get_pane_scrollback(full=1)` can never exceed that cap on this
  host contract, regardless of how much more a fixture writes.
- **Hidden-on-other-tab:** the probe's event counter froze at `[0519]` across a tab
  excursion (`Ctrl+t n`, hidden 30s+) and subsequent tab switches (`Alt+arrows`).
  Sending `clear` via pipe emptied the log and counting resumed from `[0001]`
  (`PaneUpdate: 9 pane(s) across 2 tab(s)`) with live `Event::Key` lines following —
  proving the plugin was alive throughout, not crashed.
- **R1 — UNRESOLVED:** whether the frozen counter during the tab excursion was
  event-starvation (no `PaneUpdate` delivered to a plugin on a non-active tab) or a
  missed re-render on return could not be separated, because the `clear` command used
  to prove liveness also wiped the evidence that would have distinguished the two.
  Either way, the derived adapter law for M2 is: re-sync state on tab return.
- **Subscribed-mode cost remains UNMEASURED.** The only subscribed-mode data point
  from this sitting is the runaway storm documented in t02's pad.1 section (fence
  2b) — a subscriber that includes its own pane self-feeds into an unbounded loop.
  The steady-state per-call cost of `get_pane_scrollback` under repeated/timed
  polling (as opposed to a self-feeding subscription) was not measured this sitting
  and is an explicit open gap for M2.
- **Operator-UX finding (product-relevant, not a performance number):** zellij's
  modal keyboard bindings, combined with the floating pane layer and SSH-mediated
  input, made "where do my keys go" the dominant difficulty for a non-expert
  operator (focus repeatedly landed on the probe or `htop` unintentionally).
  termbrana's real operator is this kind of user, not a zellij power-user, and this
  should inform M2 input-affordance design.
