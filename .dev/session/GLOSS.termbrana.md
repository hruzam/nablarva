# GLOSS.termbrana — majkee's learning file across all termbrana sessions

`what: explanatory notes running alongside the termbrana PADs — the "what are we doing and why"`
`for the human sitting them. UNCANONICAL (like dock.md): never cite as truth; commands live in`
`the PADs only, verdicts live in the fences and research/evidence/ only.`
`scope: all toolbox-termbrana-* sessions. One gloss per nablarva part: GLOSS.<part>.md, here.`
`written by: the driver of each sitting, before the step is run. Opened 2026-09-02 (Oraculum).`
`guide: ~/reposoma/raw.guides/gloss/GUIDE.md (DRAFT 2026-09-02)`

## The big picture (read once)

Termbrana wants to be a zellij plugin that watches a terminal pane and lets you navigate
what happened in it *semantically* — jump to the last error, the last tool run, the answer
to a prompt — instead of scrolling linearly. It is read-only by default: it observes, it never
types into your shell.

A zellij plugin is not a program in a pane. It is a small WebAssembly file that the zellij
*server* loads and runs inside itself. Zellij owns the terminal (the PTY), parses everything
the shell prints, and only then hands the plugin already-rendered text. That is the ceiling:
a plugin can see what zellij rendered, never the raw bytes. Termbrana's whole design rests on
knowing exactly where that ceiling is on the real machine.

**M0** ("milestone zero", the truth spike) asks one question: *what can a zellij 0.44.3 plugin
actually see and do on this exact box?* Trajectory answered most of it headlessly in August
(build works, API surface confirmed from source, several docs-vs-reality mismatches found).
Five things could not be answered without a human looking at a screen — those are the PAD's
STEPs 1–5. When they are answered, the **host contract** is frozen: zellij 0.44.3 · rustc 1.95.0
· wasm32-wasip1 · this Manjaro box. "Frozen" means every later line of code is written against
exactly that, and versions are never argued again. The freeze is the gate; majkee owns it
(nablarva flag L11).

Why so much ceremony for one plugin: a plugin API is a moving target, and building on a guess
about it is how projects die at month three. The spike converts guesses into evidence files
(`toolbox/termbrana/research/evidence/`) *before* real code exists.

## Zellij keyboard you will use (pane mode = `Ctrl+p`, then one letter)

| keys | does | why you need it |
|---|---|---|
| `Ctrl+p n` | new tiled pane | a plain shell next to the plugin |
| `Ctrl+p w` | hide/show all floating panes | get your shell back when the floating plugin has focus |
| `Ctrl+p e` | eject floating → tiled (and back) | a tiled pane can be fullscreened |
| `Ctrl+p f` | fullscreen focused pane | the plugin renders only its last N log lines — taller pane = more history |
| `Alt+←/→` (or `Alt+h/l`) | move focus between tiled panes | switch shell ↔ plugin without the mouse |

A **focused** pane receives your keystrokes. The yellow border shows which one has focus. The
plugin logs every key it receives (`Event::Key (focused) = …`) — that is not interception,
just normal focus; interception is STEP 3.

---

## session 02 · pad.1-m0-runtime-confirm

### STEP 0 / STEP 0′ — state check

*Proves the environment before anything real happens.* STEP 0 was sat 16 Aug in the old repo
path; the repo was then unified into nablarva (flag L12) and the old path deleted, so STEP 0′
re-proves it at the new one.

- `--version` ×3 — has the host drifted since the pin? (No: exact match.)
- `cargo build --locked …` — the compiled plugin (`.wasm`) did not travel with the repo move
  (build output is never tracked in git), so it is rebuilt in place. `--locked` = use exactly
  the dependency versions in `Cargo.lock`; a silent upgrade here would quietly break the
  contract we are about to freeze.
- `ls … .wasm` — the artefact exists where STEPs 1–2 will point at it.
- `delete-session termbrana-spike` — zellij remembers dead sessions and can "resurrect" them;
  the 16-day-old ghost pointed at a deleted path. Clean slate for STEP 1.

Sat 2026-09-02 over SSH from home: MATCH.

### STEP 1 — attach, load the plugin, see it render

*Proves the first thing everything else depends on: the plugin loads, is granted its
permissions, and can draw.* (T0.1's done-check, seen with human eyes.)

- `zellij attach -c termbrana-spike` — `-c` creates the session if it does not exist. You are
  now inside a real zellij client; the server process is what will load the plugin.
- `Ctrl+p n` — a separate plain pane for typing commands so the plugin can float over it.
- `zellij action launch-plugin --floating --skip-plugin-cache "file:…wasm"` — asks the server
  to load the wasm as a floating pane. `--skip-plugin-cache` matters: zellij caches compiled
  plugins by path, and we just rebuilt — the cache could otherwise hand you August's build.
- **The permission prompt** — a plugin declares what it wants (read pane contents, read
  application state, read CLI pipes); zellij asks the human once per plugin path. All three
  are read-only. The `ReadCliPipes` one exists only so the probe can receive commands in
  STEPs 2–3; it is not a permission the real product will ask for.
- The first line the plugin draws (`… plugin_id=N perms_granted=… intercepting=false`) is the
  plugin reporting its own view of the world back to you. If it says granted, the trust
  boundary is passable; if the pane stays blank, nothing downstream in termbrana is possible
  on this host and we stop here.
- The growing `[00NN]` lines under it are the probe's **event log**: zellij pushes events to a
  subscribed plugin (key presses, pane changes, timers) and the harness counts and prints each
  one. `PaneUpdate: 7 pane(s)` = zellij telling the plugin the layout changed (7 = your two
  terminals + the plugin + zellij's own bar plugins). That log is the evidence surface for
  every later step.

Why this is a *human* step: `zellij action dump-screen` — the tool that lets scripts read a
pane — returns nothing for plugin panes (proved in August). A plugin's own rendering can only
be verified by eyes. That is also why the product chose a review *pane* (whose source is a
terminal pane, script-readable) over an overlay (ADR-0001).

Sat 2026-09-02: granted, plugin_id=4.

### STEP 2 — capture a coloured fixture (does the API keep colours?)

*Proves the single most product-shaping fact left open: when a plugin asks zellij for a pane's
content (`get_pane_scrollback`), does the text arrive with its colour codes embedded, or
stripped?* Termbrana promises a `rendered_ansi` grade (colours preserved). If the default call
strips them, the product must take a different path for colour — a real architectural fork,
decided by this one step.

- The `printf` line prints four words in four **different colour systems**: classic 16-colour
  red, bold 16-colour green, 256-colour orange, and 24-bit truecolour. If any survive the
  capture we see exactly which layers zellij preserves. The *pane* is what gets captured, not
  the file.
- **Pane ID** — zellij numbers terminal panes and plugin panes separately. `zellij action
  list-clients` shows the focused pane's id (`terminal_0`); that is the number the capture
  command needs.
- `zellij action pipe … -- "capture terminal 0 0"` — a **pipe** is zellij's message channel
  from the command line into a running plugin (that is what `ReadCliPipes` was for). The
  message tells the probe: "read terminal pane 0, viewport only (`0`), and log what you got,
  escaped". *Escaped* = the probe prints an ESC byte as the visible token `<ESC>` — so the eye
  can see whether colour codes are inside the string. Your typed `\033[31m` on the command
  line is *source text* the shell echoed, not an ESC byte; only `<ESC>` tokens count.
- **Why the CLI printed nothing:** the probe answers the pipe in two places — into its own
  log pane *and* back to the CLI's stdout. The CLI half has a 1 s window and did not land
  (twice). The log-pane half is durable. Reading the plugin pane is therefore the evidence
  route, not a fallback. New fact for t02: the pipe reaches the plugin fine under an
  interactive client; only the echo back is broken.

**Result 2026-09-02:** `viewport[26]: red bold-green orange256 truecolor` — plain, no `<ESC>`.
`get_pane_scrollback` **strips ANSI by default.** `above=0 below=0` also confirms `full=0`
returns the viewport only. The `rendered_ansi` grade cannot come from the pull call.

### STEP 2b — the push path (added this sitting, same question, other door)

*Proves whether ANY path in the 0.44.3 plugin API delivers colours.* Zellij can *push*
pane content to a subscribed plugin whenever a pane changes — two event flavours,
`PaneRenderReport` (plain) and `PaneRenderReportWithAnsi` (supposedly with colours). The
harness subscribes on command.

- `clear` — empties the probe's log so the flood of report lines starts from zero (each report
  logs every line of every reported pane; without `clear` STEP 2's evidence would be pushed out
  of view — it is already photographed, but a clean log reads better).
- `subscribe_render_reports` — the probe subscribes to both flavours at once, so we compare
  them side by side on the same content.
- `cat /tmp/t02-fixture.txt` — makes pane 0 change, which triggers the push.

Verdicts: WithAnsi lines carry `<ESC>` tokens → colours reachable, but only by subscription
(the product's capture adapter must be event-driven — ADR-0001 already leans that way). Both
flavours plain → no colour path exists in this API; `rendered_ansi` becomes a documented
ceiling, not a promise. Also watch whether the plugin pane feels sluggish after subscribing:
a report per pane per change is the cost model of the real product (T0.5).

### STEP 3 — interception cycle (can the plugin take the keyboard, and give it back?)

*Proves the product's "safe" story in the only direction that matters: not that termbrana can
grab input — that it can release it.* An observer that could ever trap your keyboard is not
read-only.

- `intercept_on` — the probe asks zellij for one more permission, `InterceptInput` (never at
  load — only here, on purpose), and calls `intercept_key_presses()`. From then on every key
  pressed anywhere in the session is delivered to the plugin instead of the focused pane.
  Expect a second permission prompt.
- Type a few letters/arrows in the *shell* pane — they should not appear there; the plugin
  log should show them as `Event::Key` lines instead.
- `intercept_off` — `clear_key_presses_intercepts()`; keys must flow to the shell again
  immediately. Press `Esc` once more afterwards as a recovery check.

Verdicts: swallowed during / normal after → the on/off pair is sound. Keys still reach the
shell during, or do not come back after → a real harness bug, stop. (`intercept_on` is
probe-only; the product's observer mode never requests it — L11 constraint "no global
interception for observer mode".)

**Result 2026-09-02:** the on/off pair is sound — but only from the *second* `intercept_on`. The
harness asks for `InterceptInput` and calls `intercept_key_presses()` in the same breath; zellij
grants permissions asynchronously, so the first call ran without the right and did nothing
(your `abc` reached the shell). Second call: every key, arrows included, went to the plugin and
none to the shell. You could not type `intercept_off` yourself — the driver fired it from a
separate shell with `zellij --session termbrana-spike action pipe …`, which works from outside
the session. Lesson for the product: request → *wait for the grant* → intercept; and any
intercepting feature needs an off-switch that does not depend on the keyboard it just took.

### STEP 4 — visual alignment under resize (does the plugin pane behave like a real pane?)

*Proves the last open reservation about ADR-0001: that a plugin-rendered pane stays visually
sane when the layout changes.* The plugin is re-asked to `render(rows, cols)` on every
resize; zellij composites the result. The old worry was an *overlay* drifting off its target;
we dropped the overlay, so this step only has to show the review-pane path is clean.

- Resize the terminal window a few times — each resize travels home → SSH → zellij, which
  re-lays-out every pane and asks the plugin to redraw. Watch for flicker, stale lines,
  misaligned borders.
- `Ctrl+p e` toggles the plugin between tiled and floating; `Ctrl+p f` toggles fullscreen.
  Each is a geometry change with a fresh render.
- **Judge relatively, not absolutely:** you are looking through SSH and your home terminal.
  Anything that flickers in the *shell* pane too is the transport; only what misbehaves in
  the plugin pane *alone* is the plugin's. Say which.

Verdicts: stable → ADR-0001's review-pane choice loses its last reservation. Flicker or
misalignment in the plugin pane only → describe it; it tunes M2's render cadence, it does not
reopen the ADR (that decision rests on the structural findings, not on this look).

**Result 2026-09-02:** stable. The plugin pane stayed aligned and continuous through window
resizes and two tiled↔floating toggles; it was the *shell* pane that smeared (zsh redrawing its
prompt on every resize signal). The control worked in our favour: whatever the SSH transport
did, it did to both panes, and only the terminal pane showed it. One number to keep: a single
resize drag produced dozens of `PaneUpdate` events — the product must treat "layout changed"
as a burst, not a tick.

### STEP 5 — big scrollback + hidden plugin (what does watching cost?)

*Proves the last gap: the performance envelope.* Everything so far was small. The product
will sit next to panes that print thousands of lines per second, and it will often be hidden
(other tab, minimised). Does it stay cheap, and does it come back sane?

- `yes … | head -100000 > /tmp/big-fixture.txt` — a 100 000-line file, made in a blink.
- `cat /tmp/big-fixture.txt` — the pane scrolls it as fast as zellij can render; zellij's
  parser and renderer work hard, and every screen change is a `PaneUpdate` to the plugin.
  The current probe instance is *not* subscribed to render reports (that was the 2b storm
  instance, since quit), so the plugin receives only lightweight layout events — this
  measures the *observer-idle* cost, which is what the product's default mode pays.
- **Hide the plugin for ~30 s** (`Ctrl+p e` to float it, `Ctrl+p w` to hide; `Ctrl+p w` to
  show) — a hidden plugin still runs; the question is whether it accumulates work while unseen
  and stutters when shown, or resumes cleanly.
- `htop` in a spare pane (`Ctrl+p n`, then `htop`; `q` to leave) shows whether the zellij
  server process spikes; the number to note is its CPU % during the `cat`.

Verdicts: session stays responsive, plugin resumes cleanly → no red flag; note any CPU %.
Session lags or the plugin pane breaks → note *when* (during the cat, during hide, on show).
Remember 2b: a *subscribed* plugin would have paid far more here — that is the number M2
must measure before choosing a capture cadence.
