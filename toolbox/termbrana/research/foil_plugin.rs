// source: ~/.remote/harvest · author: nabla · adopted: flag L11 2026-08-15 · role: research history

// foil_plugin.rs — a Zellij "semi-transparent foil" plugin skeleton.
//
// Design law this code enforces:
//   captured grid  = IMMUTABLE MODEL   (replaced wholesale, never mutated in place)
//   opacity `t`    = PROJECTION PARAM  (∈ [0,1], moved only by a hotkey)
//   rendered cells = render(model, t)  (a pure function; recomputed every frame)
//
// Because Zellij clears the plugin's screen before every render() call, we re-emit
// the whole foil each frame anyway — which makes render() literally a pure function
// of (model, t). Nothing in the model is ever written by the render path.
//
// ---------------------------------------------------------------------------
// BUILD (verify against your installed Zellij with get_zellij_version()):
//   Cargo.toml:
//     [dependencies]
//     zellij-tile = "0.42"          # match your Zellij; this API surface is recent
//   target: wasm32-wasi   (or wasm32-wasip1 on newer toolchains)
//     rustup target add wasm32-wasi
//     cargo build --release --target wasm32-wasi
//   load it:  zellij action new-pane --plugin file:/abs/path/foil_plugin.wasm
// ---------------------------------------------------------------------------

use std::collections::BTreeMap;
use zellij_tile::prelude::*;

// ===================================================================
// @section: model  (the invariant)
// ===================================================================

/// A wholesale snapshot of an underlying pane. Treated as immutable:
/// on each capture we build a NEW one and swap it in — we never edit fields.
#[derive(Default, Clone)]
struct CapturedGrid {
    /// Lines as returned by get_pane_scrollback. NOTE: these arrive as ANSI
    /// strings (already styled), not as a fg/bg-per-cell matrix. That is the
    /// crux of the transparency limitation — see blend_line() below.
    viewport: Vec<String>,
    /// Monotonic marker so we can tell stale captures apart in logs / replay.
    captured_at_ms: u64,
}

#[derive(Default)]
struct Foil {
    // --- projection parameter (the ONLY thing the hotkey mutates) ---
    opacity: f32, // t ∈ [0.0 = fully see-through, 1.0 = fully opaque foil]

    // --- immutable model ---
    captured: Option<CapturedGrid>,

    // --- which pane we are foiling / injecting into ---
    target_pane: Option<PaneId>,

    // --- lifecycle flags ---
    permissions_granted: bool,
    intercepting: bool,
}

register_plugin!(Foil);

// The theme background we blend TOWARD as opacity drops. In a full build,
// read this from the user's theme; hardcoded here for clarity.
const THEME_BG: Rgb = Rgb { r: 0x00, g: 0x1a, b: 0x3a };
const OPACITY_STEP: f32 = 0.05;

// ===================================================================
// @section: lifecycle
// ===================================================================

impl ZellijPlugin for Foil {
    fn load(&mut self, config: BTreeMap<String, String>) {
        self.opacity = config
            .get("opacity")
            .and_then(|s| s.parse().ok())
            .unwrap_or(0.85);

        // Optional: caller pins the target pane id via config, e.g. "target_terminal=1".
        self.target_pane = config
            .get("target_terminal")
            .and_then(|s| s.parse::<u32>().ok())
            .map(PaneId::Terminal);

        // Request EXACTLY the capabilities the foil's role needs — each is
        // user-prompted, which is the human-visible grant your approval-gate wants.
        request_permission(&[
            PermissionType::ReadPaneContents,      // get_pane_scrollback  (capture)
            PermissionType::WriteToStdin,          // write_chars_to_pane_id (inject)
            PermissionType::InterceptInput,        // intercept_key_presses (hotkey)
            PermissionType::ChangeApplicationState, // send_sigint_to_pane_id (Ctrl-C gate)
        ]);

        subscribe(&[
            EventType::PermissionRequestResult,
            EventType::InterceptedKeyPress,
            EventType::Timer, // drives the periodic capture loop
        ]);

        // A foil should not steal normal pane selection; intercept still works globally.
        set_selectable(false);
    }

    fn update(&mut self, event: Event) -> bool {
        match event {
            // ---- permissions resolved: arm intercept + kick off capture loop ----
            Event::PermissionRequestResult(result) => {
                self.permissions_granted = matches!(result, PermissionStatus::Granted);
                if self.permissions_granted && !self.intercepting {
                    intercept_key_presses(); // hotkeys now arrive as InterceptedKeyPress
                    self.intercepting = true;
                    set_timeout(0.0); // immediate first capture; handler re-arms
                }
                false
            }

            // ---- the capture loop tick ----
            Event::Timer(_elapsed) => {
                self.capture();          // build a NEW immutable model, swap it in
                set_timeout(0.25);       // re-arm ~4 Hz; tune to taste
                true                     // model changed -> re-render
            }

            // ---- the ONLY place opacity changes: the hotkey handler ----
            Event::InterceptedKeyPress(key) => self.on_intercepted_key(key),

            _ => false,
        }
    }

    // Zellij clears our screen before this runs; we emit a full frame.
    fn render(&mut self, rows: usize, cols: usize) {
        let Some(model) = &self.captured else {
            // Nothing captured yet: emit a faint status line, nothing else.
            print!("\u{1b}[2m foil: awaiting capture… \u{1b}[0m");
            return;
        };

        // render(model, t): pure. We only READ model + self.opacity here.
        for (row, line) in model.viewport.iter().take(rows).enumerate() {
            let projected = blend_line(line, self.opacity, THEME_BG, cols);
            // position cursor at (row, 0) then print the projected line
            print!("\u{1b}[{};1H{}", row + 1, projected);
        }
        // tiny HUD so you can see t while tuning
        print!(
            "\u{1b}[{};1H\u{1b}[7m t={:.2} \u{1b}[0m",
            rows.max(1),
            self.opacity
        );
    }
}

// ===================================================================
// @section: behaviour  (capture / hotkey / inject)
// ===================================================================

impl Foil {
    /// Build a fresh immutable snapshot and swap it in. Never mutates an
    /// existing CapturedGrid — replacement only, so the model stays a value.
    fn capture(&mut self) {
        let Some(pane) = self.target_pane else { return };
        match get_pane_scrollback(pane, /* full = */ false) {
            Ok(contents) => {
                self.captured = Some(CapturedGrid {
                    viewport: contents.viewport, // ANSI strings (see blend_line note)
                    captured_at_ms: now_ms(),
                });
            }
            Err(e) => eprintln!("foil capture failed: {e}"),
        }
    }

    /// The projection mutator. Returns true iff a re-render is needed.
    fn on_intercepted_key(&mut self, key: KeyWithModifier) -> bool {
        // NOTE: the key enum has churned across Zellij versions. Verify BareKey
        // variants against your zellij-tile. This matches the recent model.
        match key.bare_key {
            BareKey::Char('+') | BareKey::Char('=') => {
                self.opacity = (self.opacity + OPACITY_STEP).min(1.0);
                true
            }
            BareKey::Char('-') => {
                self.opacity = (self.opacity - OPACITY_STEP).max(0.0);
                true
            }
            // number keys 0..9 -> preset opacities (0 => 0.0, 9 => 0.9)
            BareKey::Char(c @ '0'..='9') => {
                self.opacity = (c as u8 - b'0') as f32 / 10.0;
                true
            }
            // Enter -> push a command into the target pane, grid-native.
            BareKey::Enter => {
                self.inject("echo pushed-by-foil\n");
                false
            }
            // Ctrl-C -> gated interrupt of the target process.
            BareKey::Char('c') if key.key_modifiers.contains(&KeyModifier::Ctrl) => {
                if let Some(pane) = self.target_pane {
                    send_sigint_to_pane_id(pane);
                }
                false
            }
            // Esc -> release the intercept so keys flow normally again.
            BareKey::Esc => {
                clear_key_presses_intercepts();
                self.intercepting = false;
                false
            }
            _ => false,
        }
    }

    /// Grid-native command injection: bytes land on the target pane's STDIN,
    /// rendered by Zellij — no synthetic keystrokes.
    fn inject(&self, chars: &str) {
        if let Some(pane) = self.target_pane {
            write_chars_to_pane_id(chars, pane);
        }
    }
}

// ===================================================================
// @section: blending  (the SIMULATED alpha — Zellij has no native cell alpha)
// ===================================================================

#[derive(Clone, Copy)]
struct Rgb { r: u8, g: u8, b: u8 }

fn blend_channel(top: u8, bottom: u8, t: f32) -> u8 {
    (top as f32 * t + bottom as f32 * (1.0 - t)).round().clamp(0.0, 255.0) as u8
}

fn blend_rgb(top: Rgb, bottom: Rgb, t: f32) -> Rgb {
    Rgb {
        r: blend_channel(top.r, bottom.r, t),
        g: blend_channel(top.g, bottom.g, t),
        b: blend_channel(top.b, bottom.b, t),
    }
}

/// Fade a captured line toward `bg` by factor `t`, emitting 24-bit ANSI.
///
/// *** THE HONEST LIMITATION ***
/// `line` arrives as an ANSI-styled STRING, not a fg/bg-per-cell matrix. To blend
/// each cell's TRUE colour toward the background you must first PARSE the SGR
/// sequences back into per-cell (glyph, fg, bg) — i.e. run a VT parser (`vte`
/// crate) to reconstruct screen state. That parser is the piece Zellij's API does
/// NOT hand you, and it's the real work behind "continuous transparency."
///
/// This skeleton ships the pragmatic v1: strip existing SGR, then re-wrap the
/// plain text in a single blended fg over the theme bg. It reads as a uniform
/// translucent wash rather than true per-cell alpha. Swap in the vte path when
/// per-cell fidelity matters.
fn blend_line(line: &str, t: f32, bg: Rgb, cols: usize) -> String {
    let plain: String = strip_sgr(line).chars().take(cols).collect();
    // Foil text colour = white faded toward the theme bg as t drops.
    let fg = blend_rgb(Rgb { r: 0xe0, g: 0xe0, b: 0xe0 }, bg, t);
    format!(
        "\u{1b}[38;2;{};{};{}m\u{1b}[48;2;{};{};{}m{}\u{1b}[0m",
        fg.r, fg.g, fg.b, bg.r, bg.g, bg.b, plain
    )
}

/// Minimal CSI/SGR stripper. Good enough for v1; a real build lets the VT
/// parser own this instead of hand-rolling escape handling.
fn strip_sgr(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut chars = s.chars().peekable();
    while let Some(c) = chars.next() {
        if c == '\u{1b}' {
            if chars.peek() == Some(&'[') {
                chars.next();
                while let Some(&nc) = chars.peek() {
                    chars.next();
                    if ('@'..='~').contains(&nc) { break; } // final byte ends CSI
                }
            }
        } else {
            out.push(c);
        }
    }
    out
}

fn now_ms() -> u64 {
    // Plugins run in wasm; wire this to a host time source or a monotonic
    // counter you bump each Timer tick. Placeholder to keep the model shape honest.
    0
}
