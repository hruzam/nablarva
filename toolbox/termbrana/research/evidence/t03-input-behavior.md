`source: termbrana session 02 (toolbox-termbrana-02-m0-truthspike) · author: Trajectory 2026-08-15`
`role: Milestone 0 probe evidence`

# T0.3 — Input behavior

## Confirmed from this session (runtime, not just source)

- **`zellij action send-keys -p <pane_id> <key>` reliably delivers ordinary input to a
  specific pane's normal input path**, independent of that pane's current focus state,
  for at least the two host-drawn plugin overlays this session actually needed to
  dismiss: the "First Run Setup Wizard" and the "Release Notes 0.44.3" `about` plugin
  pane both closed cleanly on `send-keys -p plugin_N Enter` /
  `send-keys -p plugin_N Esc`. This is genuine evidence that ordinary, non-intercepted
  key delivery to a plugin pane works exactly as project-definition.md §7's observer
  mode expects — no interception needed for a plugin to receive and act on keys.
- **`Esc` recovery**: confirmed for the wizard/about overlays (both pads dismissed
  cleanly via `Esc` or `Enter` sent this way). Not yet confirmed for the harness's own
  `intercept_on`/`intercept_off` cycle (see gap below).
- The harness's own `Event::Key` handling is implemented and compiles/loads correctly
  (`update()` logs every `Event::Key` it receives, escaped, with a `T0.3` prefix) —
  but whether a real keystroke reached it while genuinely focused could not be
  independently confirmed this session, for the same dump-screen/pipe-round-trip
  reasons as T0.2 (see t02).

## What the source surface confirms about global interception (design question, not a runtime probe)

From `api-surface-0.44.3.md`: `Event::InterceptedKeyPress(KeyWithModifier)` only ever
fires after the plugin calls `intercept_key_presses()`, which requires the
`InterceptInput` permission — a separate, explicitly-granted capability, not something
that leaks into ordinary `Event::Key` delivery. The harness deliberately requests
`InterceptInput` only inside a pipe-triggered `intercept_on` command
(`src/main.rs`), never at `load()`, so the default probe-harness permission set matches
what the eventual observer-mode product should request: `ReadPaneContents` +
`ReadApplicationState` only (plus the harness-only `ReadCliPipes`, see
api-surface-0.44.3.md).

This directly supports the plan's T0.3 gate — **"observer mode must not need global
interception"** — at the design level: nothing about receiving and reacting to
`Event::Key` while focused requires `InterceptInput`. The gate is satisfied by
construction, not by having exercised interception live and watched it consume input.

## What is NOT confirmed and is the honest gap

- Live exercise of `intercept_on` → `Event::InterceptedKeyPress` → confirm an
  unhandled key is genuinely swallowed → `intercept_off` → confirm keys flow normally
  again. The harness command exists (`intercept_on`/`intercept_off` pipe commands) but
  could not be driven to completion for the same `zellij action pipe` round-trip
  unreliability documented in t02 — sending the command is one thing, confirming its
  effect (whether a subsequent key really was or wasn't consumed) needs to either watch
  the plugin's own log output (pipe, unreliable here) or feel the actual input
  experience (needs a human).
- Explicit plugin-message activation (`zellij action pipe` used as the *legitimate*
  activation mechanism project-definition.md §3.5 recommends instead of global
  interception) is architecturally sound and is exactly what this harness's whole
  command surface already uses — but the same round-trip issue means its *reply* path
  couldn't be watched live this session, only its *delivery* (confirmed: `handle_command`
  runs, permission-denial and panic-fix cycles above prove pipe messages do reach
  `pipe()`).

## Operator follow-up

`pad.1-m0-runtime-confirm.md` includes an interception cycle step: attach for real,
send `intercept_on`, press a key that should be swallowed, confirm normal `Event::Key`
does not also fire for it, send `intercept_off`, confirm normal keys resume. This is
exactly the class of probe the handoff brief anticipated needing a live human for
("input behavior... may need a live human at the terminal").
