# pad.1-m0-runtime-confirm — Milestone 0 truth-spike, human-in-the-loop probes

> Operator test surface. Sequential — one step, report back, next step.
> Driver: whoever sits this pad (human or a driver seat helping a human).
> Re-pathed 2026-09-02 (flag L12 unification): project now lives at toolbox/termbrana inside nablarva. Build artefacts did not travel — STEP 0′ below re-sits the state check at the new path before STEP 1.
> Sitting 2026-09-02: driver = Oraculum (office session); operator = majkee, hands over SSH (`oc`) from home. STEP 4/5 judgements are SSH/Tailscale-mediated — stamp that in their reports.

## Driver rules

1. One step, one concept, then wait. Never run ahead.
2. Every command is copy-pasteable as written — full paths, no assumed `cd`.
3. Nothing here is destructive; STEP 0 only reads state.
4. Every step's outcome is one of the branch verdicts listed under it — don't guess.
5. If a step's output doesn't match either verdict, stop and flag @Trajectory (or
   whoever is driving session `toolbox-termbrana-02-m0-truthspike`) rather than
   improvising past it.

## Why this pad exists

The automated half of the M0 truth spike (Trajectory, 2026-08-15) got further than
expected — it fixed two real plugin bugs, confirmed the exact 0.44.3 plugin-API
surface from crate source, and proved `dump-screen` cannot read plugin panes and that
`zellij action pipe`'s one-shot round trip is unreliable against a headless/scripted
client. What it could not do without a genuine human hand: watch a plugin pane render,
judge visual alignment, and feel the input/interception experience live. That is what
this pad collects. See `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t02
through t05` for exactly which claims are pending confirmation here.

## Shared constant

```
Project path used in all commands:
/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana
```
```
Zellij session name used in all commands:
termbrana-spike
```
```
Plugin wasm path used in all commands:
/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm
```

## Precondition

A real terminal you are typing into (not a scripted/backgrounded shell) — that's the
whole point of this pad.

## STEP 0 — state check

```bash
cd /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana
zellij --version && rustc --version
cargo build --locked --release --target wasm32-wasip1 -p termbrana-zellij
zellij list-sessions
```

Expected: version lines match `research/evidence/host-versions.md` exactly, the build
finishes with no errors (it should already be a no-op rebuild), and `list-sessions`
either shows nothing or shows a leftover `termbrana-spike [EXITED - attach to
resurrect]` from the automated half of this spike (harmless either way).

- `<MATCH>` → proceed to STEP 1.
- `<VERSION MISMATCH or BUILD ERROR>` → STOP, flag @Trajectory — the host contract may
  have drifted since this pad was written.

>MAJKEE report 0
```zsh
# sat 2026-08-16, driver: Houston · verdict: <MATCH>
zellij 0.44.3
rustc 1.95.0 (59807616e 2026-04-14)
Finished `release` profile [optimized] target(s) in 0.22s
No active zellij sessions found.
```

### STEP 0′ — re-sit state check at the new path (2026-09-02, post-L12)

The 2026-08-16 <MATCH> was sat at a path that no longer exists. Re-prove the environment at the
new one. Cold build expected (target/ was untracked and did not travel). `delete-session` removes
only the 16-day-old EXITED leftover — no evidence lives in it.

```bash
cd /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana
zellij --version && rustc --version && cargo --version
cargo build --locked --release --target wasm32-wasip1 -p termbrana-zellij
ls -la target/wasm32-wasip1/release/termbrana-zellij.wasm
zellij delete-session termbrana-spike
zellij list-sessions
```

Expected: `zellij 0.44.3` · `rustc 1.95.0` · `cargo 1.95.0`; build finishes without error (minutes,
not seconds); the `.wasm` is listed; `list-sessions` reports no sessions.

- `<MATCH>` → proceed to STEP 1.
- `<VERSION MISMATCH or BUILD ERROR>` → STOP, paste the full output, flag the driver.

>MAJKEE report 0′
```zsh
# sat 2026-09-02 01:38, driver: Oraculum · operator: majkee over SSH from home · verdict: <MATCH>
# (cargo build output not pasted by operator; artefact timestamp below is the build proof)
zellij 0.44.3
rustc 1.95.0 (59807616e 2026-04-14)
cargo 1.95.0 (f2d3ce0bd 2026-03-21)
❯ ls -la target/wasm32-wasip1/release/termbrana-zellij.wasm
-rwxr-xr-x 2 hruzam hruzam 1577266  2. zář 01.38 target/wasm32-wasip1/release/termbrana-zellij.wasm
❯ zellij delete-session termbrana-spike
Session: "termbrana-spike" successfully deleted.
❯ zellij list-sessions
No active zellij sessions found.
```

### STEP 1 — attach for real, load the plugin, confirm it renders

```bash
zellij attach -c termbrana-spike
```

This drops you into an interactive zellij session (creating it fresh if the leftover
one is gone). Once inside, run:

```
Ctrl+p n
```
(open a new pane) then in that new pane:
```bash
cd /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana
WASM="$(pwd)/target/wasm32-wasip1/release/termbrana-zellij.wasm"
zellij action launch-plugin --floating --skip-plugin-cache "file:$WASM"
```

A floating pane should appear. If a permission-request prompt appears first, approve
it (it will ask to read pane contents / application state / CLI pipes — all read-only,
matches `crates/termbrana-zellij/src/main.rs`'s `load()` comment).

Expected: the floating pane's first line reads something like `termbrana-zellij probe
harness | zellij=0.44.3 plugin_id=N perms_granted=Some(Granted) intercepting=false`.

- `<VERSION LINE VISIBLE, perms_granted=Some(Granted)>` → T0.1's "renders its version
  information" done-check is now visually confirmed. Proceed to STEP 2.
- `<PANE BLANK or PERMS DENIED>` → note whether a permission prompt ever appeared and
  what you answered; STOP, flag @Trajectory with that detail.

>MAJKEE report 1
```zsh
# sat 2026-09-02, driver: Oraculum · operator: majkee over SSH from home · verdict: <VERSION LINE VISIBLE, perms_granted=Some(Granted)>
# operator report (typed, not pasted): permission prompt appeared → approved.
# floating pane shows: perms_granted=Some(Granted) plugin_id=4
# then a growing [00N] event-log counter (harness event log — expected).
```

### STEP 2 — T0.2: capture a colored fixture

In a plain terminal pane in the same session:

```bash
printf '\033[31mred\033[0m \033[1;32mbold-green\033[0m \033[38;5;208morange256\033[0m \033[38;2;10;200;250mtruecolor\033[0m\n' > /tmp/t02-fixture.txt
cat /tmp/t02-fixture.txt
```

Note that pane's ID (`zellij action list-panes -a -j` or just check the pane's border
label), then from any pane in the session:

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "capture terminal <ID> 0"
```

(replace `<ID>` with the actual pane id number)

Expected: output lines showing the captured viewport content, escaped (`<ESC>` visible
literally instead of real color codes) so you can see whether SGR codes are present in
the string or not.

- `<OUTPUT SHOWS <ESC>[31m etc. literally>` → `get_pane_scrollback` embeds ANSI by
  default. Record this in the report.
- `<OUTPUT SHOWS PLAIN "red bold-green..." with no <ESC> tokens>` → `get_pane_scrollback`
  strips ANSI by default. Record this instead.
- `<NO OUTPUT / TIMEOUT>` → same round-trip issue as the automated session; STOP, flag
  @Trajectory — this specific point needs a different approach, not more retries.

>MAJKEE report 2
```zsh
# sat 2026-09-02 ~02:10, driver: Oraculum · operator: majkee over SSH from home
# verdict: <OUTPUT SHOWS PLAIN "red bold-green..." with no <ESC> tokens> → get_pane_scrollback STRIPS ANSI by default
# route: CLI echo of `zellij action pipe` produced NOTHING (both runs) — the pipe DID reach the plugin;
#        evidence read from the plugin's own log pane (ejected + fullscreen). Photos: ~/.claude/uploads/…/42df8c24-image.jpg, c294c9b8-image.jpg
# pane id via: zellij action list-clients → "1  terminal_0  zellij action list-clients"
❯ printf '\033[31mred\033[0m \033[1;32mbold-green\033[0m \033[38;5;208morange256\033[0m \033[38;2;10;200;250mtruecolor\033[0m\n' > /tmp/t02-fixture.txt; cat /tmp/t02-fixture.txt
red bold-green orange256 truecolor          # rendered in colour in the terminal
❯ zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "capture terminal 0 0"
                                             # (no CLI output)
# plugin pane log (transcribed from photo):
[0072] T0.2 get_pane_scrollback(Terminal(0), full=false) OK viewport_lines=39 above=0 below=0
[0097]   viewport[24]: ❯ printf '\033[31mred\033[0m \033[1;32mbold-green\033[0m ...   # shell echo of typed text, not ESC bytes
[0099]   viewport[26]: red bold-green orange256 truecolor                                  # PLAIN — no <ESC> tokens
[0102]   viewport[29]: red bold-green orange256 truecolor                                  # second run, same
[0105]   viewport[32]: 1          terminal_0      zellij action list-clients
# NEW FACT vs 2026-08-15: pipe → plugin works under an interactive client; cli_pipe_output → CLI stdout does NOT land (0/2).
# STEP 2b (added by driver, same concept): PaneRenderReportWithAnsi push path — see fence 2b.
```

### STEP 2b — T0.2: does the PUSH path keep colours? (added 2026-09-02, same concept as STEP 2)

`get_pane_scrollback` strips ANSI (STEP 2). The only other content path is the host-push
subscription `PaneRenderReport` / `PaneRenderReportWithAnsi`, which the harness can subscribe
to on command. `clear` first, so the flood of report lines starts from an empty log.

From your shell pane (each pipe prints nothing to the CLI — expected):

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "clear"
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "subscribe_render_reports"
cat /tmp/t02-fixture.txt
```

Then focus the plugin pane, fullscreen it, and read the log. Expected: lines labelled
`T0.2 PaneRenderReportWithAnsi: N pane(s)` and `T0.2 PaneRenderReport (no-ansi): N pane(s)`,
each followed by `[<label>][i]: <line>` lines for every pane reported.

- `<WithAnsi lines show <ESC>[31m … tokens around the fixture words; no-ansi lines plain>` →
  the push path carries ANSI; `rendered_ansi` grade is reachable via subscription only.
- `<BOTH variants plain>` → no ANSI path exists in 0.44.3 plugin API; `rendered_ansi` grade
  is unreachable on this host contract (record as structural ceiling).
- `<NO report lines at all after cat>` → subscription did not fire; STOP, report the last
  [NNNN] line.

Also note: how many pane(s) each report covers, and whether the plugin pane felt sluggish
after subscribing (log flood) — that is T0.5 evidence.

>MAJKEE report 2b
```zsh
# sat 2026-09-02 ~02:20, driver: Oraculum · operator: majkee over SSH from home
# verdict: <WithAnsi lines show <ESC> tokens> → PaneRenderReportWithAnsi CARRIES ANSI; rendered_ansi grade reachable by SUBSCRIPTION ONLY
# (fixture line for terminal_0 not isolated in the photo — the storm below buried it; ESC tokens seen are SGR resets in the plugin's own pane report)
❯ zellij action pipe … -- "clear"                       # no CLI output (expected)
❯ zellij action pipe … -- "subscribe_render_reports"    # no CLI output; operator reports the command "started, unfinished"
❯ cat /tmp/t02-fixture.txt
# plugin pane log (transcribed from photo ~/.claude/uploads/…/013d0a9c-image.jpg):
[528133]        [T0.2 PaneRenderReportWithAnsi][33]: <ESC>[m[528009<ESC>[m…
[528136]        [T0.2 PaneRenderReportWithAnsi][34]: <ESC>[m …
[528142]        [T0.2 PaneRenderReportWithAnsi][48]: <ESC>[mrReportWithAnsi][64]:<ESC>[m<ESC>[m<ESC>[m<ESC>[m
# RUNAWAY (T0.5 evidence): subscribing reports EVERY pane incl. the plugin's OWN pane → each report re-renders the plugin
# → new report → loop. seq counter ~300K within ~1 min, ~528K at photo time. Reported content = the plugin's own log lines.
# Product law derived: a subscriber MUST exclude its own pane and debounce; never subscribe blindly to all panes.
# Session responsiveness during storm: degraded past recovery — Ctrl+p x (close pane) was NOT reachable;
# operator had to QUIT THE WHOLE SESSION (Ctrl+q). Lag-vs-freeze detail: <operator to report>. Session recreated fresh for STEP 3.
# No `unsubscribe` in harness; kill-by-pane-close was not possible under the storm → whole session quit (see above).
```

### STEP 3 — T0.3: interception cycle

From any pane:

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "intercept_on"
```

Then click/focus the harness's floating pane and press a few ordinary keys (letters,
arrows). Then:

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "intercept_off"
```

Press `Esc` once more afterward regardless of outcome (recovery check).

Expected: while intercepting, keys should NOT reach whatever pane was previously
focused (they're being swallowed/logged by the harness instead); after `intercept_off`,
normal typing in other panes resumes immediately.

- `<KEYS SWALLOWED DURING INTERCEPT, NORMAL AFTER intercept_off>` → T0.3 gate
  confirmed live: interception works as designed and Esc/intercept_off cleanly restores
  normal input.
- `<KEYS STILL REACH OTHER PANES DURING INTERCEPT, or NORMAL INPUT DOESN'T RESUME>` →
  STOP, flag @Trajectory — this would mean the harness's intercept_on/off pair has a
  real bug, not just an evidence gap.

>MAJKEE report 3
```zsh
# sat 2026-09-02 02:30–02:45, driver: Oraculum · operator: majkee over SSH from home · fresh session after 2b storm (Ctrl+q)
# verdict: <KEYS SWALLOWED DURING INTERCEPT, NORMAL AFTER intercept_off>  — with three findings:
# F1 ORDERING BUG (harness): 1st intercept_on → [0049] "requested InterceptInput + intercept_key_presses()" fired BEFORE
#    the grant [0062]; operator typed `abc` → reached the shell (zsh: command not found: abc), no Event::Key logged.
#    2nd intercept_on (permission already granted) → [0069], then [0077] T0.3 Event::InterceptedKeyPress = Enter,
#    thereafter every key incl. arrows logged as InterceptedKeyPress; nothing reached the shell.
# F2 OPERATOR LOCK-OUT: while intercepting, operator could NOT type the intercept_off pipe (keys swallowed) — as designed, but
#    it means the product needs an out-of-band off-switch.
# F3 OUT-OF-BAND SWITCH WORKS: from a separate office shell (Delta):
#    zellij --session termbrana-spike action pipe --plugin "file:…/termbrana-zellij.wasm" --name termbrana-probe -- "intercept_off"
#    → exit 0, no output; plugin header flipped to intercepting=false.
# recovery: Ctrl+u · Esc · `echo ok` → "ok" printed, shell normal.
# permission prompt at intercept_on listed: 1. Access Zellij state 2. Intercept Input (keyboard & mouse) 3. Read pane contents — approved (y).
# photos: ~/.claude/uploads/…/f5a512e2-image.jpg (prompt), 339c2c87-image.jpg (abc reached shell), 7242b95e-image.jpg ([0077] intercepted Enter)
```

### STEP 4 — T0.4: visual alignment

Resize the terminal window a few times and watch the floating plugin pane. Toggle it
tiled vs floating (`zellij action toggle-pane-embed-or-eject` while it's focused).
Watch for flicker, stale content, or misaligned borders during resize.

- `<STABLE, NO FLICKER/MISALIGNMENT>` → overlay-vs-review-pane concern is not a
  blocker; ADR-0001's review-pane choice stands and this removes the last open
  reservation about it.
- `<FLICKER OR MISALIGNMENT OBSERVED>` → note what specifically (describe it), record
  in report — this may inform an M2 rendering-cadence adjustment but does not reopen
  ADR-0001 (that decision rests on the structural findings, not this visual check
  alone).

>MAJKEE report 4
```zsh
# sat 2026-09-02 ~02:50, driver: Oraculum · operator: majkee over SSH (Konsole on home → office) — SSH/Tailscale-mediated judgement
# verdict: <STABLE, NO FLICKER/MISALIGNMENT> in the PLUGIN pane
# operator: resized the Konsole window manually several times; Ctrl+p e (tiled↔floating) ×2 — pane slot order changed (normal re-embed)
# photo ~/.claude/uploads/…/7a7baeb7-image.jpg: plugin pane (now left, tiled) — borders aligned, log continuous [0358]..[0420], no stale lines.
# CONTROL: the SHELL pane (right) showed heavy artefacts — zsh powerline prompt re-drawn/smeared ~40× on resize (SIGWINCH redraw).
#          → transport/zsh-side artefact; plugin pane behaved BETTER than a terminal pane under identical resizes.
# cadence datum (T0.5): one resize drag ≈ dozens of PaneUpdate events (seq 0193 → 0420 across the resizes).
# ADR-0001 review-pane reservation: closed.
```

### STEP 5 — T0.5: large scrollback + hidden-plugin behavior

```bash
yes "termbrana perf fixture line" | head -100000 > /tmp/big-fixture.txt
cat /tmp/big-fixture.txt   # run this in a plain terminal pane, let it scroll through
```

While that's running/just after, hide the plugin pane (minimize/switch tab away from
it) for ~30s, then bring it back. Watch overall session responsiveness throughout with
`htop`/`top` in another pane if convenient.

- `<SESSION STAYS RESPONSIVE, PLUGIN RESUMES CLEANLY>` → no performance red flag found;
  record any CPU numbers you noticed.
- `<SESSION LAGS OR PLUGIN PANE BREAKS>` → note when (during the big cat, during
  hide, during show) and record in report; this is real T0.5 evidence either way.

>MAJKEE report 5
```zsh

```

## Trailing sink

After this sitting, distilled results (not the raw pad) belong in one of:
- `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t02-pane-content-semantics.md` (STEP 2),
- `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t03-input-behavior.md` (STEP 3),
- `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t04-geometry-rendering.md` (STEP 4),
- `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t05-performance.md` (STEP 5),
- `~/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/pane-content-matrix.md` (fixture rows
  marked `PENDING-OPERATOR`).

Whoever folds these in should update each file's "Status"/gap section to say
"confirmed by pad.1 sitting, <date>" rather than deleting the automated-session
context — the two halves of this evidence trail should stay legible together.

## parked

(space for off-pad questions raised during the sitting)
