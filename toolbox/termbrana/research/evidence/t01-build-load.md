`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence · cites: nablarva .dev/session/toolbox-termbrana-02-m0-truthspike/handoff.md`

# T0.1 — Build and load evidence

Raw session log backing every claim below: `research/evidence/zellij-session.log`
(copied verbatim from `/tmp/zellij-1000/zellij-log/zellij.log` for this spike run).

## Versions (verify pass)

Re-verified against the live host, matches the already-locked
`research/evidence/host-versions.md` (PAD-01 green) exactly:

```
zellij 0.44.3
rustc 1.95.0 (59807616e 2026-04-14)
cargo 1.95.0 (f2d3ce0bd 2026-03-21)
wasm32-wasip1 (rustup target, only wasm target installed besides host)
zellij-tile = 0.44.3 (confirmed resolvable on crates.io index via `cargo add`/`cargo build`)
```

No changes needed to `host-versions.md` — T0.1 is a verify-and-record step against an
already-locked pin, not a re-decision.

Additional host fact not previously recorded: the server logs
`Loading plugins using Wasmi interpreter` on every session start (zellij-session.log:9,
40, etc.) — this build of zellij 0.44.3 runs plugin WASM through **Wasmi** (a pure-Rust
interpreter), not `wasmtime`. This matters for T0.5 (interpreted, not JIT-compiled,
execution) and for any future assumption about WASM feature support.

## The smallest compiling plugin

Workspace: `~/unikuklatrix/nablarva/toolbox/termbrana/` (Cargo.toml `[workspace] members =
["crates/termbrana-zellij"]`). `termbrana-core` is intentionally not created — execution
plan §2: "do not pre-create empty architecture."

`crates/termbrana-zellij/Cargo.toml`:

```toml
[package]
name = "termbrana-zellij"
version = "0.0.0"
edition = "2021"
publish = false

[dependencies]
zellij-tile = "=0.44.3"
```

`crates/termbrana-zellij/src/main.rs` — a `[[bin]]` crate (see "API mismatch #1" below
for why this must be a bin, not a `cdylib` lib), ~230 lines, the Milestone-0 **probe
harness**, not the product. It implements `ZellijPlugin::load/update/pipe/render` and
exposes pipe-driven commands (`capture`, `subscribe_render_reports`, `intercept_on`,
`intercept_off`, `clear`) so probes T0.2–T0.5 can be driven externally instead of by
editing and recompiling the plugin per probe.

### Exact build command

```bash
cd ~/unikuklatrix/nablarva/toolbox/termbrana
cargo build --release --target wasm32-wasip1 -p termbrana-zellij
```

Output: `target/wasm32-wasip1/release/termbrana-zellij.wasm` (~1.58 MB, unstripped).
Verified clean build, zero warnings, `Finished release profile [optimized] target(s) in
~1.2s` on incremental rebuilds (~45s cold, pulling zellij-utils/zellij-tile and their
full dependency tree from crates.io).

### Exact load commands (headless, scriptable — no interactive human required)

```bash
# 1. Create a detached session (server only, no client yet)
zellij attach -b termbrana-spike

# 2. Attach a real client so the server has somewhere to route plugin/pane actions.
#    A session with NO attached client cannot load or focus a plugin at all — see
#    "API mismatch #3" below. tmux hosts a proper pty for this; `script` also works
#    but was observed to occasionally desync the client protocol (zellij-session.log
#    "Client sent over 1000 consecutive unknown messages" — not reproduced under tmux).
tmux new-session -d -s zc -x 220 -y 50 "zellij attach termbrana-spike"

# 3. Load the plugin as a floating pane
WASM="$(pwd)/target/wasm32-wasip1/release/termbrana-zellij.wasm"
zellij --session termbrana-spike action launch-plugin --floating --skip-plugin-cache "file:$WASM"
# -> prints the created pane id, e.g. "plugin_7"
```

Confirmed via `zellij --session termbrana-spike action list-panes -a -j`: the plugin
pane appears with `plugin_url` set to the `file:` URL, floating, selectable, with real
geometry (observed 11 rows x 40 cols for a floating default; see T0.4 for geometry
detail). Confirmed via the session log: `Loaded plugin
'/home/.../termbrana-zellij.wasm' in ~25ms` on every one of 8 successive loads during
this spike (24.86ms–28.09ms, zellij-session.log lines 29/60/91/97/455/628/637/658) —
tight and consistent, first useful T0.5 data point (cold WASM instantiate cost under
Wasmi).

**Done-when check (execution-plan §3 T0.1):** "a minimal plugin compiles, loads, renders
its version information, and its build commands are committed." Compiles: yes. Loads:
yes (see above). Renders version information: the harness's `render()` prints
`get_zellij_version()` and `get_plugin_ids().plugin_id` on its first line — this is
implemented and the plugin does not crash after the fix below, but visual confirmation
of the rendered frame could not be captured headlessly (see "dump-screen cannot read
plugin panes" below) and is deferred to the operator pad
(`pad.1-m0-runtime-confirm.md`).

## Bugs found and fixed during the spike

### Bug 1 — crate must be a `[[bin]]`, not a `cdylib` lib

First attempt used `[lib] crate-type = ["cdylib"]` (a common pattern for other wasm
targets). Zellij's plugin loader requires **both** a `_start` export and a `load`
export (`zellij-server/src/plugins/plugin_loader.rs:175-180`, fetched from the
`v0.44.3` tag to confirm against the actual release, not assumption). A `cdylib` built
for `wasm32-wasip1` does not produce a WASI `_start` command entry point, so loading
failed every time with:

```
ERROR failed to load plugin from instance ... Caused by: could not find exported function
```

Fix: make the crate a plain `[[bin]]` (`src/main.rs`, no `[lib]` section). Rust's
`wasm32-wasip1` target then emits `_start` automatically, and `register_plugin!`'s
`#[no_mangle] fn load()` (and the rest) are exported normally. Confirmed fixed — this
exact error stopped appearing in the log after the switch, across 8 subsequent loads.

### Bug 2 — slice panic in the probe harness's own `pipe()` handler

Own bug, not a zellij one: `pipe()` computed `before = self.log.len()` and later sliced
`self.log[before..]`, but the `clear` command runs in between and can shrink `log`
below `before`, panicking with an out-of-bounds slice (`wasm \`unreachable\`
instruction executed`, `PANIC IN PLUGIN`, zellij-session.log around lines 100-360).
Fixed by clamping: `let start = before.min(self.log.len());`. Confirmed fixed — no
further panics for this plugin across 4 subsequent reloads and pipe attempts.
