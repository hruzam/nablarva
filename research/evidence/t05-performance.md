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
