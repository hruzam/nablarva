---
note: stridularium — nablarva's phone organ
date: 2026-10-01
status: NOTE · input for the architecture session (nablarva-03-app-architecture) · DECIDED = majkee said it; the rest is proposal
canon: flag.md L2 · L3 · L4 · L13 · O2 · session-bed · presence-board · KEYS CODE
supersedes: note.phone-lens.2026-09-30.md (never committed)
home: .dev/session/nablarva-X0-restarted/raw/ until a stridularium bed exists
---

# stridularium — note

L2 stage 3: the human's door into the room (L13). It calls you for gavels; it hosts nothing.

## Shape — DECIDED (majkee)

- The session lives on the host (workstation, tmux). The phone attaches and never hosts; closing
  the app changes nothing there.
- Compute, state and sessions stay on the computer. The phone renders and sends input: a thin lens.
- Attaching is advisory (presence-board class); detaching never closes a bed.
- Reach is app-scoped: an app-owned vault you scope. A session may ask the app to switch you to a
  view inside it (a render instruction, not an action) and can't widen it.
  Rejected: device-scoped access, a CLI reaching Android functions outside the app. That is agent
  reach on a personal device.

## Bridge — O2 · majkee's pick: harden what exists

The bridge is the session-bed: Tailscale + Termux + SSH into tmux. On a Redmi, the system battery
manager is the usual killer. In order:

1. Tailscale and Termux: unrestricted battery use, autostart on, both locked in recents;
   Always-on VPN for Tailscale; `termux-wake-lock`.
2. mosh instead of plain SSH: roams between Wi-Fi and mobile data, survives the phone sleeping.
3. Trajectory's tips: the phone attaches to its own view session `<slug>--phone`, and windows use
   `window-size latest`, so the phone neither steals the desk's tab nor shrinks its windows.

Fallback, not chosen: an outbound tunnel from the PC to a small VPS relay; the phone needs only a
browser. Cost: one public endpoint to secure, one more machine to keep.

Rejected: a vendor-hosted page. It moves the page, not the route, which still needs a way to your
PC. claude.ai's published pages block outside network calls by design, and the control surface
would sit on someone else's host.

Worth one test (weather, re-verify): Zellij's web client (0.43+: token login, mobile browsers
supported; 0.44: read-only follow).

## Navigation — carousel + breadcrumbs (majkee)

- Cards swiped sideways, small breadcrumbs for position (host › room › seat › session). No window
  loader.
- The host renders text, the phone shows cards. No terminal emulator on the phone.
- Proposal: gestures carry KEYS CODE meanings (swipe = move, tap = Enter, back = q), so the phone
  doesn't become a second grammar.

## Voice mode (majkee's shape, mapped)

- Voice is the app's own pipe, not the phone's system voice input.
- You pick a target: the agent that maintains the app (limited to the app), or a mirrored CLI
  session on the host.
- Each voiced text lands in that target's buffer. Buffers live on the host, one per target.
  Release is the only way into a CLI: through stridulatrix and the adapter's own PTY (L3), never
  send-keys (L4).
- This is Ptyra's voice-to-CLI pipeline with release checks, moved onto the phone.
- Speech-to-text runs on the PC, so audio stays off vendor servers.
- Inherited gap (Ptyra): no rule for secrets spoken aloud. On a phone, in public, it turns urgent.

## What reaches the phone — carried from the bus-fork thread, unstruck

stridularium buzzes only for:

1. gavel — promote, deploy, canon change
2. gate change or sibling opening
3. STOP or BLOCKED verdict
4. loop budget spent (~10 cycles) or fork width > 3–4
5. irreversible op outside RUNBOOK holds
6. seats still disagreeing after one pushback each
7. curvature the head can't resolve

## The delta worth building

Vendor remote control (`codex remote-control`, Claude Code `/rc`; weather, 09-30) may already
cover keyboard and display for one session. No vendor app gives the cross-session buffer driven
from the phone, or one gavel feed across vendors. Build only that.

## Open

- build order: notifier first (majkee) or buffer first (symmetry) — open since 09-30
- `voice-relay-00-probe` in nablarva — unread
- the rule for secrets spoken aloud
