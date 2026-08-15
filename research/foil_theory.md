`source: ~/.remote/harvest · author: nabla · adopted: flag L11 2026-08-15 · role: research history`

# Foil Plugin — Theory Companion

Background for the concepts the plugin skeleton relies on. Each section maps to a
`@section:` in `foil_plugin.rs`.

---

## 1. The terminal stack: why a plugin is a *peer* emulator

A "terminal" today is three layers that people conflate:

- **The device pair.** A TTY (real hardware/serial: `/dev/ttyS0`, or a kernel
  virtual console `/dev/tty1`) or a **PTY** (pseudoterminal). A PTY is two linked
  character devices: a *master* fd held by whoever controls the terminal, and a
  *slave* (`/dev/pts/N`) handed to the child process. The child calls `isatty()`,
  gets `true`, and enables terminal behaviour: colour, progress bars, raw mode.
- **The line discipline.** A kernel layer between master and slave that handles
  echo, canonical (line-buffered) vs raw input, and signal generation
  (Ctrl-C → SIGINT, Ctrl-Z → SIGTSTP). It is why Ctrl-C "just works" without the
  program polling for it.
- **The emulator.** A userspace program that (a) allocates the PTY and (b)
  interprets the byte stream from the master into a drawn character grid. Alacritty,
  kitty, konsole, xterm.js, VTE — all just holders of a master fd plus a renderer.

The consequence for the plugin: **holding a master fd is the whole job of "being a
terminal."** A standalone emulator and an editor's embedded terminal are peers, not
original-vs-copy. When your foil sits on the byte stream, it is architecturally a
terminal emulator that happens to log/gate/blend instead of draw pixels. Nothing
about that role is second-class.

The quality gap between emulators is not in the PTY (identical for all) but in
everything *above* the master fd: escape-sequence coverage, render speed, and
`$TERM`/terminfo honesty (advertising capabilities you actually implement).

---

## 2. The terminal as a grid, and why scrollback arrives as strings

The screen a program "sees" is a **cell grid**: `rows × cols`, each cell holding a
grapheme plus attributes (fg colour, bg colour, bold/italic/underline, etc.). The
program never sends you this grid. It sends a **byte stream** — printable characters
interleaved with **control sequences** that mutate an implicit cursor and cell
attributes. The emulator runs a state machine over that stream to *reconstruct* the
grid. There is no API in the ANSI/VT world for "give me your grid"; the grid exists
only inside whoever parsed the stream.

This is the root of the plugin's central limitation. `get_pane_scrollback` returns
lines that are **already-styled ANSI strings** (SGR sequences embedded), because
that is Zellij's serialization of its internal grid back out. To recover the *true
fg/bg of each cell* — which you need for genuine per-cell blending — you must parse
those strings back into cells. The API hands you the stream, not the matrix.

---

## 3. VT/ANSI parsing: the state machine behind the `vte` crate

Escape sequences are not a regular language you can strip with a regex reliably; they
are a small state machine. The canonical model is **Paul Williams' DEC-compatible
parser** (a formalization of how real VT100/VT220 hardware behaved). Core states:

- **GROUND** — printable bytes go straight to the grid as glyphs.
- **ESCAPE** — entered on `0x1B` (ESC). The next byte selects a sub-machine.
- **CSI** (Control Sequence Introducer, `ESC [`) — the big one. Collects numeric
  **parameters** (separated by `;`), optional **intermediates**, and a **final byte**
  in `0x40..=0x7E` that names the action. `ESC [ 3 1 m` = SGR set-foreground-red;
  `ESC [ 2 J` = erase display; `ESC [ H` = cursor home.
- **OSC** (Operating System Command, `ESC ]`) — string commands like set-window-title
  (`ESC ] 0 ; title BEL`) or clipboard writes (OSC 52).
- **DCS** (Device Control String, `ESC P`) — device-specific payloads. Zellij's own
  private UI-component protocol rides on DCS (`ESC P z ribbon ; …`).

**SGR** (Select Graphic Rendition, final byte `m`) is the attribute language you care
about. Relevant codes: `0` reset, `1` bold, `38;2;r;g;b` set 24-bit fg, `48;2;r;g;b`
set 24-bit bg, `38;5;n`/`48;5;n` the 256-colour palette, `30–37`/`40–47` the 8-colour
base.

Why this matters: the `strip_sgr()` in the skeleton is a deliberately naive CSI
skipper. It works for a wash but it is *not* a correct parser — it ignores OSC/DCS
string termination rules, cursor motion, and the difference between "this cell is red"
and "the cursor moved then wrote red." A real per-cell foil replaces it with a proper
parser (the `vte` crate implements exactly the Williams machine) that emits a
`(glyph, fg, bg, attrs)` for every cell. Once you have that matrix, blending is
trivial; getting the matrix is the work.

---

## 4. Immutable model + pure projection (this is MVU / the Elm Architecture)

The plugin's design law — *model is immutable, opacity is a projection parameter,
render is a pure function* — is not ad-hoc. Zellij's plugin trait (`load` / `update`
/ `render`) **is** the Model-View-Update pattern (a.k.a. the Elm Architecture):

- **Model** = your `Foil` struct (captured grid + `opacity`).
- **Update** = `update(event) -> bool`: the only place state changes, driven by
  events (a keypress, a timer). It returns whether a re-render is needed.
- **View** = `render(rows, cols)`: a *pure function of the model*. Zellij clears the
  screen before each call, so you re-emit a full frame; there is no hidden retained
  state to drift out of sync.

Two properties fall out of keeping `render` pure (referentially transparent):

- **Replay / audit.** If the model is an immutable value and the view never mutates
  it, you can re-render *any past captured model* at *any opacity*, days later, and
  get a faithful picture. The view logic provably cannot have corrupted the logged
  truth — because it only reads. For a supervised orchestrator this is the whole game:
  the monitoring layer can dim, highlight, or fade without risk of editing history.
- **Testability.** `render(model, t)` and `blend_rgb(top, bottom, t)` are pure, so
  they test with plain input→output assertions, no terminal in the loop.

The discipline to preserve: `update` mutates; `render` and the blend helpers only
read. Capture does **replacement** (`self.captured = Some(new)`), never in-place
mutation, so the model stays a value rather than a shared mutable thing.

---

## 5. Alpha compositing, and why a text cell has none

Real transparency is the **Porter–Duff "over" operator** (Porter & Duff, 1984). For a
source pixel over a destination, the "over" blend of colour channels is:

```
out = src·α + dst·(1 − α)
```

which is a linear interpolation (`lerp`) between destination and source by α. The
skeleton's `blend_channel(top, bottom, t)` is exactly this with `t = α`. So the *math*
of transparency is present and correct.

The problem is the substrate. A framebuffer pixel has an alpha channel; **a terminal
character cell does not.** A cell is `(glyph, fg, bg, attrs)` and its background is
opaque — there is no per-cell α for a compositor to blend. Zellij confirms this at the
protocol level: a rendered UI component is either **opaque** (uses the theme
background) or **transparent** meaning *"use no background,"* i.e. a binary on/off, not
a continuous α. There is no float opacity in the cell model.

Therefore continuous transparency inside the grid must be **simulated**: you compute
the blended colour yourself and emit a cell whose *fg/bg already equals the blend*.
That is what `blend_line` does. `t` is a real α; the cell just stores the result of the
lerp instead of asking a compositor to perform it.

Two honest caveats on the math:

- **Colour space.** Correct alpha blending is done in *linear* light, but terminal
  colours are sRGB (gamma-encoded). Lerping raw sRGB bytes (what the skeleton does) is
  the near-universal shortcut and looks fine for a UI wash; for photometric accuracy
  you would linearize → blend → re-encode. Not worth it here.
- **Window α is the other, real transparency.** Compositor/emulator
  `background_opacity` (Hyprland, picom, kitty) *is* true see-through, because it
  operates a layer below the grid where pixels do have α. That path is trivially
  continuous — but it makes the whole window translucent to the desktop behind it, not
  the foil translucent to the pane beneath it. Different axis, often useful in combo.

---

## 6. Escape-sequence injection: the security reason to normalize

Because the terminal executes control sequences from its byte stream, **any process
that can write to your terminal can drive it.** A malicious subprocess (or hostile file
you `cat`) can emit sequences that:

- rewrite the window/tab title (OSC 0/2) — cosmetic, but also a spoofing vector;
- move the cursor and overwrite already-printed output, so what you *see* differs from
  what was *logged* — dangerous for an audit trail;
- request a **clipboard read/write** (OSC 52) or a device-status **query** whose reply
  the terminal *types back on your input* — turning display into input injection;
- abuse historical parser bugs (a recurring CVE class in terminal emulators) to
  escalate from "printed bytes" to executed effects.

This is precisely why the foil's true value is as a **normalization / sanitization
choke point**, not as decoration. Because it sits on the byte stream (or reads pane
contents and re-emits), it is the natural place to strip or canonicalize dangerous
sequences before they reach the one parser that will act on them — and to guarantee
that the *logged* stream equals the *displayed* stream. "Send only normalized data"
does not delete the parser; it routes everything through one trusted parser with clean
input.

---

## 7. The drain-or-deadlock rule (backpressure)

If you ever hold a PTY master directly (outside Zellij), the load-bearing rule is:
**read the master continuously.** A PTY has a finite kernel buffer. If you stop
reading, the child blocks on `write()` once that buffer fills — a silent deadlock, not
an error. Two related quirks:

- On Linux, after the slave closes, `read()` on the master returns **`EIO`**, not a
  clean `0`/EOF. Treat `EIO` as normal child exit.
- Propagate window size (`TIOCSWINSZ` ioctl + forward SIGWINCH) or full-screen TUIs
  render at the wrong dimensions.

Inside Zellij you are insulated from this — Zellij owns the master and drains it — but
the same shape recurs: your `Timer`-driven capture must not block the plugin's own
`render`. Long or heavy work belongs in a **worker** (Zellij's async offload) so the
render path stays responsive.

---

## 8. WASM capability sandbox: why permissions are granular (and time isn't free)

Zellij plugins are WebAssembly modules. Two properties of that sandbox show up in the
code:

- **Capability-based security.** A WASM module has *no ambient authority* — it cannot
  touch stdin, panes, the network, or the host command line unless a capability is
  explicitly granted. Hence `request_permission(&[ReadPaneContents, WriteToStdin,
  InterceptInput, ChangeApplicationState])`, each **user-prompted at load**. This is a
  gift for a supervised orchestrator: the foil asks for exactly the powers its role
  needs, no more, and the human *sees* the grant. It maps directly onto a
  "least-privilege, human-in-the-loop" posture.
- **No ambient clock.** The sandbox denies wall-clock time by default, which is why
  `now_ms()` is a placeholder. You get time either from a host-provided source or by
  maintaining a monotonic counter you bump each `Timer` tick. Determinism-by-default is
  a feature, not an obstacle — it also makes replay reproducible.

A practical corollary: the plugin API surface (key enums like `BareKey`, the
`wasm32-wasi` vs `wasm32-wasip1` target, newer calls like intercept and
pane-content reads) has been moving. Gate assumptions on `get_zellij_version()` and
pin your `zellij-tile` version.

---

## 9. One-paragraph synthesis

A terminal is a byte stream reconstructed into an opaque cell grid by whoever holds the
PTY master; your foil is a legitimate peer in that role. The grid has no alpha, so
continuous transparency is a *simulated* lerp (Porter–Duff "over") whose result you
bake into each cell's colour — the α math is real, the compositor is you. Keeping the
captured grid an immutable value and `render` a pure projection (Zellij's MVU loop) buys
you audit and replay for free, which is the actual point for a monitored orchestrator.
The genuinely hard, deferred piece is a correct VT parser (`vte`) to turn styled
scrollback strings back into per-cell colours; everything else in the skeleton is a
direct, permissioned API call.

---

### References worth reading (by name)

- Porter, T. & Duff, T. (1984), *Compositing Digital Images* — the "over" operator.
- Paul Williams, *A parser for DEC's ANSI-compatible video terminals* — the VT state
  machine the `vte` crate implements.
- ECMA-48 / ISO 6429 — the control-sequence standard (CSI, SGR, OSC, DCS).
- The Elm Architecture (MVU) — the model/update/view pattern Zellij plugins follow.
- Your own OpenClaw risk-assessment framing — terminal-escape and clipboard (OSC 52)
  handling belong on the same threat map.
