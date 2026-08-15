// termbrana-zellij — Milestone 0 truth-spike PROBE HARNESS.
//
// This is intentionally NOT the product. It is the smallest compiling Zellij
// plugin (T0.1) instrumented just enough to drive probes T0.2-T0.5 and log
// their evidence onto its own screen, where `zellij action dump-screen` can
// capture it non-interactively.
//
// Design rule carried over from the honest parts of foil_theory.md: this
// harness only READS (get_pane_scrollback, PaneRenderReport events, Key
// events). It never writes to a target pane and only requests InterceptInput
// when a probe explicitly asks for it via a pipe command - never at load.
//
// Driven from outside via:
//   zellij action pipe --plugin file:/abs/path/termbrana_zellij.wasm \
//       --name termbrana-probe -- '<command>'
//
// Commands (see `handle_command` below):
//   capture <terminal|plugin> <id> <full:0|1>   - call get_pane_scrollback
//   subscribe_render_reports                    - subscribe to PaneRenderReport(WithAnsi)
//   intercept_on / intercept_off                - probe-only, never default-on
//   clear                                        - clear the on-screen log
//
// Evidence written to the log is ESCAPED (control bytes rendered as visible
// tokens like <ESC> and <0x07>) so the dump-screen capture shows literal
// bytes/structure, not a re-interpreted terminal. Never infer raw-byte
// fidelity from visual similarity (project-definition.md 2.1 / 2.6).

use std::collections::BTreeMap;
use std::fmt::Write as _;
use zellij_tile::prelude::*;

const LOG_CAPACITY: usize = 400;

#[derive(Default)]
struct Probe {
    seq: u64,
    log: Vec<String>,
    permissions_granted: bool,
    intercepting: bool,
    zellij_version: String,
    plugin_id: u32,
}

register_plugin!(Probe);

impl ZellijPlugin for Probe {
    fn load(&mut self, _configuration: BTreeMap<String, String>) {
        // Observer-only capability set (project-definition.md 7: observer mode
        // needs only ReadPaneContents + normal input). ReadApplicationState is
        // requested too so PaneUpdate/ModeUpdate arrive for free diagnostics.
        // InterceptInput is deliberately ABSENT here - see intercept_on/off.
        //
        // ReadCliPipes is a HARNESS-ONLY addition, not part of the observer
        // product surface: it is required to call cli_pipe_output() at all
        // (confirmed empirically - CliPipeOutput is denied without it), which
        // is how this spike answers `zellij action pipe` probes since
        // dump-screen cannot read plugin panes in 0.44.3 (verified: T0.2/T0.4
        // evidence). The eventual termbrana-zellij product does not need this.
        request_permission(&[
            PermissionType::ReadPaneContents,
            PermissionType::ReadApplicationState,
            PermissionType::ReadCliPipes,
        ]);

        subscribe(&[
            EventType::PermissionRequestResult,
            EventType::Key,
            EventType::InterceptedKeyPress,
            EventType::PaneUpdate,
            EventType::Timer,
        ]);
    }

    fn update(&mut self, event: Event) -> bool {
        match event {
            Event::PermissionRequestResult(status) => {
                self.permissions_granted = matches!(status, PermissionStatus::Granted);
                self.zellij_version = get_zellij_version();
                self.plugin_id = get_plugin_ids().plugin_id;
                self.push(format!(
                    "T0.1 permissions_granted={:?} zellij_version={} plugin_id={}",
                    self.permissions_granted, self.zellij_version, self.plugin_id
                ));
                true
            }
            Event::Key(key) => {
                self.push(format!("T0.3 Event::Key (focused) = {:?}", key));
                true
            }
            Event::InterceptedKeyPress(key) => {
                self.push(format!("T0.3 Event::InterceptedKeyPress = {:?}", key));
                true
            }
            Event::PaneUpdate(manifest) => {
                let n: usize = manifest.panes.values().map(|v| v.len()).sum();
                self.push(format!("PaneUpdate: {} pane(s) across {} tab(s)", n, manifest.panes.len()));
                false
            }
            Event::PaneRenderReport(map) => {
                self.log_pane_report("T0.2 PaneRenderReport (no-ansi)", &map);
                true
            }
            Event::PaneRenderReportWithAnsi(map) => {
                self.log_pane_report("T0.2 PaneRenderReportWithAnsi", &map);
                true
            }
            Event::Timer(_) => false,
            _ => false,
        }
    }

    fn pipe(&mut self, pipe_message: PipeMessage) -> bool {
        // Release the CLI's ACTION_COMPLETION_TIMEOUT (1s, zellij-server route.rs)
        // immediately. Empirically, `zellij action pipe` reports "did not complete
        // within 1s timeout" if this is not called promptly - the pipe still works
        // afterwards, but the CLI's own stdout window can close before a slower
        // cli_pipe_output() call lands. Unblock first, compute second.
        unblock_cli_pipe_input(&pipe_message.name);
        let before = self.log.len();
        let payload = pipe_message.payload.clone().unwrap_or_default();
        self.handle_command(&payload);
        // Evidence channel: echo every log line this command produced straight
        // back to `zellij action pipe`'s STDOUT. dump-screen cannot read plugin
        // panes in 0.44.3 (verified empirically), so this is the probe harness's
        // real capture path - not the plugin's own render().
        if matches!(pipe_message.source, PipeSource::Cli(_)) {
            let mut out = String::new();
            let start = before.min(self.log.len());
            for line in &self.log[start..] {
                out.push_str(line);
                out.push('\n');
            }
            if out.is_empty() {
                out.push_str("(no new log lines)\n");
            }
            cli_pipe_output(&pipe_message.name, &out);
        }
        true
    }

    fn render(&mut self, rows: usize, _cols: usize) {
        println!(
            "termbrana-zellij probe harness | zellij={} plugin_id={} perms_granted={:?} intercepting={}",
            self.zellij_version, self.plugin_id, self.permissions_granted, self.intercepting
        );
        let take = rows.saturating_sub(2);
        let start = self.log.len().saturating_sub(take);
        for line in &self.log[start..] {
            println!("{}", line);
        }
    }
}

impl Probe {
    fn push(&mut self, line: String) {
        self.seq += 1;
        self.log.push(format!("[{:04}] {}", self.seq, line));
        if self.log.len() > LOG_CAPACITY {
            let overflow = self.log.len() - LOG_CAPACITY;
            self.log.drain(0..overflow);
        }
    }

    fn handle_command(&mut self, payload: &str) {
        let mut parts = payload.split_whitespace();
        match parts.next() {
            Some("capture") => {
                let kind = parts.next().unwrap_or("");
                let id: u32 = parts.next().and_then(|s| s.parse().ok()).unwrap_or(0);
                let full = parts.next().unwrap_or("0") == "1";
                let pane_id = match kind {
                    "terminal" => PaneId::Terminal(id),
                    "plugin" => PaneId::Plugin(id),
                    other => {
                        self.push(format!("capture: unknown pane kind {:?}", other));
                        return;
                    }
                };
                match get_pane_scrollback(pane_id, full) {
                    Ok(contents) => {
                        self.push(format!(
                            "T0.2 get_pane_scrollback({:?}, full={}) OK viewport_lines={} above={} below={}",
                            pane_id, full, contents.viewport.len(),
                            contents.lines_above_viewport.len(),
                            contents.lines_below_viewport.len(),
                        ));
                        for (i, line) in contents.viewport.iter().enumerate() {
                            self.push(format!("  viewport[{}]: {}", i, escape(line)));
                        }
                        for (i, line) in contents.lines_above_viewport.iter().enumerate() {
                            self.push(format!("  above[{}]: {}", i, escape(line)));
                        }
                    }
                    Err(e) => self.push(format!(
                        "T0.2 get_pane_scrollback({:?}, full={}) ERR {}",
                        pane_id, full, e
                    )),
                }
            }
            Some("subscribe_render_reports") => {
                subscribe(&[EventType::PaneRenderReport, EventType::PaneRenderReportWithAnsi]);
                self.push("subscribed to PaneRenderReport + PaneRenderReportWithAnsi".to_string());
            }
            Some("intercept_on") => {
                // Probe-only path: InterceptInput is requested ONLY here, never
                // at load, so the default observer permission set stays minimal.
                request_permission(&[
                    PermissionType::ReadPaneContents,
                    PermissionType::ReadApplicationState,
                    PermissionType::InterceptInput,
                ]);
                intercept_key_presses();
                self.intercepting = true;
                self.push("T0.3 intercept_on: requested InterceptInput + intercept_key_presses()".to_string());
            }
            Some("intercept_off") => {
                clear_key_presses_intercepts();
                self.intercepting = false;
                self.push("T0.3 intercept_off: clear_key_presses_intercepts()".to_string());
            }
            Some("clear") => {
                self.log.clear();
                self.seq = 0;
            }
            Some(other) => self.push(format!("unknown command: {:?}", other)),
            None => {}
        }
    }

    fn log_pane_report(&mut self, label: &str, map: &std::collections::HashMap<PaneId, PaneContents>) {
        self.push(format!("{}: {} pane(s)", label, map.len()));
        for (pane_id, contents) in map.iter() {
            self.push(format!("  {:?} viewport_lines={}", pane_id, contents.viewport.len()));
            for (i, line) in contents.viewport.iter().enumerate() {
                self.push(format!("    [{}][{}]: {}", label, i, escape(line)));
            }
        }
    }
}

/// Render control bytes as visible tokens instead of letting the terminal
/// interpret them. This is the harness's core evidence law: what you see in
/// the dump IS the string content, not a re-rendering of it.
fn escape(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '\u{1b}' => out.push_str("<ESC>"),
            '\u{07}' => out.push_str("<BEL>"),
            '\r' => out.push_str("<CR>"),
            '\n' => out.push_str("<LF>"),
            c if (c as u32) < 0x20 => {
                let _ = write!(out, "<0x{:02X}>", c as u32);
            }
            c => out.push(c),
        }
    }
    out
}
