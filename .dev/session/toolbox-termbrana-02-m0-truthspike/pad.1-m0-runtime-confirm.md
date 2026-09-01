# pad.1-m0-runtime-confirm — Milestone 0 truth-spike, human-in-the-loop probes

> Operator test surface. Sequential — one step, report back, next step.
> Driver: whoever sits this pad (human or a driver seat helping a human).

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
this pad collects. See `~/unikuklatrix/termbrana/research/evidence/t02
through t05` for exactly which claims are pending confirmation here.

## Shared constant

```
Project path used in all commands:
/home/hruzam/unikuklatrix/termbrana
```
```
Zellij session name used in all commands:
termbrana-spike
```
```
Plugin wasm path used in all commands:
/home/hruzam/unikuklatrix/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm
```

## Precondition

A real terminal you are typing into (not a scripted/backgrounded shell) — that's the
whole point of this pad.

## STEP 0 — state check

```bash
cd /home/hruzam/unikuklatrix/termbrana
zellij --version && rustc --version
cargo build --release --target wasm32-wasip1 -p termbrana-zellij
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
cd /home/hruzam/unikuklatrix/termbrana
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
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "capture terminal <ID> 0"
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

```

### STEP 3 — T0.3: interception cycle

From any pane:

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "intercept_on"
```

Then click/focus the harness's floating pane and press a few ordinary keys (letters,
arrows). Then:

```bash
zellij action pipe --plugin "file:/home/hruzam/unikuklatrix/termbrana/target/wasm32-wasip1/release/termbrana-zellij.wasm" --name termbrana-probe -- "intercept_off"
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
- `~/unikuklatrix/termbrana/research/evidence/t02-pane-content-semantics.md` (STEP 2),
- `~/unikuklatrix/termbrana/research/evidence/t03-input-behavior.md` (STEP 3),
- `~/unikuklatrix/termbrana/research/evidence/t04-geometry-rendering.md` (STEP 4),
- `~/unikuklatrix/termbrana/research/evidence/t05-performance.md` (STEP 5),
- `~/unikuklatrix/termbrana/research/evidence/pane-content-matrix.md` (fixture rows
  marked `PENDING-OPERATOR`).

Whoever folds these in should update each file's "Status"/gap section to say
"confirmed by pad.1 sitting, <date>" rather than deleting the automated-session
context — the two halves of this evidence trail should stay legible together.

## parked

(space for off-pad questions raised during the sitting)
