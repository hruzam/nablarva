`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence · answers execution-plan.md §12 / handoff.md epoch open item`

# zellij-tile / zellij-utils 0.44.3 — actual plugin-API surface

**Method:** not docs-trust. `cargo add zellij-tile@0.44.3` + `cargo build` in a scratch
crate pulled the exact vendored source into
`~/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/{zellij-tile,zellij-utils}-0.44.3/`,
which was then read directly (`shim.rs`, `data.rs`, `plugin_api/event.rs`,
`plugin_api/event.proto`). Server-side loader behavior was additionally cross-checked
against the real `zellij-server` source at git tag `v0.44.3` (raw.githubusercontent.com)
since that crate is not published to crates.io. This is source evidence, one level more
authoritative than either the public docs site or runtime probing through a
Wasmi-interpreted plugin (see t05/t02 for why the CLI round-trip channel was
unreliable in this headless harness).

## Epoch open item, answered directly

**`PaneRenderReportWithAnsi` availability in 0.44.3: CONFIRMED PRESENT.**

Both `Event::PaneRenderReport(HashMap<PaneId, PaneContents>)` and
`Event::PaneRenderReportWithAnsi(HashMap<PaneId, PaneContents>)` exist as `Event`
variants (`zellij-utils/src/data.rs:1012-1013`) and as `EventType` discriminants you can
`subscribe(&[...])` to. They are **push events**, not request/response calls — nothing
in `zellij-tile::shim` lets you ask for one on demand; you subscribe once and the host
pushes a `HashMap<PaneId, PaneContents>` snapshot whenever it renders, for every pane
visible to your client. `PaneRenderReport` vs `PaneRenderReportWithAnsi` is a **second,
independent** subscription — the host maintains two separate side caches internally
(`all_pane_contents` vs `all_pane_contents_with_ansi`, `zellij-utils/src/data.rs:2390-
2423`, `add_pane_contents` / `add_pane_contents_with_ansi`), which is the strongest
structural evidence that the "no-ansi" variant really does normalize away styling
rather than just being an alias.

## get_pane_scrollback — corrects a misreading in the execution plan

Execution-plan §3/T0.2 reads `get_pane_scrollback(..., false)` /
`get_pane_scrollback(..., true)` as if the second boolean toggles between raw and
ANSI-rendered output. **That is not the actual signature.** From
`zellij-tile-0.44.3/src/shim.rs:1812`:

```rust
pub fn get_pane_scrollback(
    pane_id: PaneId,
    get_full_scrollback: bool,
) -> Result<PaneContents, String>
```

The boolean is `get_full_scrollback` — viewport-only vs viewport-plus-full-scrollback
(`PaneContents.lines_above_viewport` / `lines_below_viewport` are populated only when
`true`, per the doc comment at `zellij-utils/src/data.rs:2428-2430`, explicitly "for
performance reasons"). There is **no ANSI-vs-plain parameter on this call at all**. The
raw/rendered-ANSI/rendered-text axis the plan wants for T0.2 is answered by a **different
mechanism** — the `PaneRenderReport` vs `PaneRenderReportWithAnsi` push-event pair above,
not by `get_pane_scrollback`. `pane-content-matrix.md` reflects this corrected mapping.

`PaneContents` shape (`zellij-utils/src/data.rs:2427`):

```rust
pub struct PaneContents {
    pub lines_above_viewport: Vec<String>,
    pub lines_below_viewport: Vec<String>,
    pub viewport: Vec<String>,
    pub selected_text: Option<SelectedText>,
}
```

Every line is a `String` — i.e. whatever content it holds (plain text or ANSI-styled
text) is already host-rendered and serialized to a string over the WASM boundary before
your plugin ever sees it. There is no cell matrix (`(glyph, fg, bg, attrs)`) handed to
the plugin anywhere in this API — confirms foil_theory.md §2's claim still holds in
0.44.3: the plugin gets strings, not a grid.

## Permission surface (actual enum, `zellij-utils/src/data.rs:1063-1080`)

```rust
pub enum Permission {
    ReadApplicationState, ChangeApplicationState, OpenFiles, RunCommands,
    OpenTerminalsOrPlugins, WriteToStdin, WebAccess, ReadCliPipes,
    MessageAndLaunchOtherPlugins, Reconfigure, FullHdAccess, StartWebServer,
    InterceptInput, ReadPaneContents, RunActionsAsUser, WriteToClipboard,
    ReadSessionEnvironmentVariables,
}
```

(`PermissionType` is the `strum`-generated discriminant of this enum — same names, used
in `request_permission(&[PermissionType::...])`.) The plan's assumption of a
`WriteToStdin` name is correct and present. One name this spike needed that isn't
mentioned anywhere in project-definition/addendum/execution-plan: **`ReadCliPipes`** —
required to call `cli_pipe_output()` at all. Confirmed empirically: without it, the host
logs `permission 'ReadCliPipes' denied - Command 'CliPipeOutput' denied`
(zellij-session.log). This is a harness-only need (driving probes over `zellij action
pipe`), not a product-observer need — the eventual `termbrana-zellij` adapter has no
reason to call `cli_pipe_output`.

## Event enum — full relevant slice (`zellij-utils/src/data.rs:945-1030`)

Confirms plan assumptions and adds detail: `Event::Key(KeyWithModifier)` fires "while
the user is focused on this plugin's pane" (doc comment, in-source); separate
`Event::InterceptedKeyPress(KeyWithModifier)` only fires after
`intercept_key_presses()` is called (requires `InterceptInput` permission — confirmed
present, not renamed); `Event::PermissionRequestResult(PermissionStatus)`;
`Event::PaneUpdate(PaneManifest)`. `PipeMessage` (`zellij-utils/src/data.rs:3000`) is
delivered through a **separate trait method**, not through `update(event: Event)`:

```rust
fn pipe(&mut self, pipe_message: PipeMessage) -> bool   // zellij-tile/src/lib.rs:43
```

with `PipeMessage { source: PipeSource, name: String, payload: Option<String>, args:
BTreeMap<String,String>, is_private: bool }` and `PipeSource::{Cli(String),
Plugin(u32), Keybind}`. This was not obvious from the execution plan and would have
cost real time in M2 if discovered only then.

## Server-side constant worth carrying into M2 design

`zellij-server/src/route.rs:36` (git tag v0.44.3, not published to crates.io so quoted
from source, not vendored): `const ACTION_COMPLETION_TIMEOUT: Duration =
Duration::from_secs(1);` — every `zellij action ...` CLI invocation gets a **hard 1-
second** server-side completion budget before the CLI reports `did not complete within
1s timeout` (it does not necessarily mean the action failed, but the CLI's own
observable round-trip is capped there). Relevant to any future tooling that shells out
to `zellij action` synchronously expecting a fast reply from a plugin running under the
Wasmi interpreter.

## Confirmed present, not renamed (things the plan worried might have moved)

`BareKey`, `KeyWithModifier`, `intercept_key_presses()`, `clear_key_presses_intercepts()`,
`write_chars_to_pane_id`, `send_sigint_to_pane_id`, `get_zellij_version()`,
`get_plugin_ids()` all exist in 0.44.3 exactly as `foil_plugin.rs` used them
(`zellij-tile-0.44.3/src/shim.rs`). The one **build-shape** thing that has moved and
that `foil_plugin.rs`'s own build comment does not mention: `wasm32-wasi` is not the
right target anymore (T0.1 already pins `wasm32-wasip1`, confirmed working); and the
crate must be a `[[bin]]`, not the `cdylib` a first-glance skim of the skeleton could
suggest (see t01-build-load.md, Bug 1).
