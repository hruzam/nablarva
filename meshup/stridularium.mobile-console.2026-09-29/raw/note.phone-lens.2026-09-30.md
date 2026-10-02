---
note: phone lens for CLI sessions
date: 2026-09-30
status: NOTE · scope open — own program, or part of relay
related: seed.relay-research.2026-09-30.md · session-bed · presence-board
---

# Phone lens — note

## Shape (majkee)

- The session lives on the server: the workstation, in tmux. The phone never hosts it; closing the app changes nothing there.
- Compute and resources stay on the computer. The phone is a long keyboard and a display over the internet (Tailscale). Pipes clear: render out, keystrokes in, nothing stateful on the handset.
- The shape of the Claude and ChatGPT mobile apps — thin fronts over server-side sessions — but for your own CLIs, vendor-neutral.
- A dashboard with a buffer: carry a message from one session to the next, and open a session within a window.
- A wrapper over tmux, because tmux is the best of the bad options.

## Canon it rides on

- session-bed: the mobile device is a lens, not the execution host.
- presence-board: the phone attaching is an advisory attachment; detaching ends only that declaration — it never closes the bed or proves a gate.
- STATUS, `_bus/` and the buffer stay on the server. The pipe carries only render and keystrokes.

## The delta worth building

Vendor remote control exists on both sides (`codex remote-control`, Claude Code `/rc`) and may already cover keyboard and display. The cross-session buffer — a message carried from one seat to the next, driven from the phone — is what no vendor app gives you. The wheel check in `relay-00-research/` confirms or kills this.

## Extension — later, not first (majkee)

- A small app-owned vault, plus a few files scoped into it.
- A session may switch you to the markdown reader on a file inside the vault. That is a render instruction, not an action — the same class as a ring.
- The scope is yours, set once, like the tunnel enable. A session cannot widen the vault.

## Rejected — PROPOSED, confirm

Device-scoped access: a CLI reaching Android functions outside the app over Tailscale. The app is the membrane; a session knocks on it and never reaches past it.

## Open

- Own program with its own gate (candidate: "cross-session buffer usable from the phone"), or a lens inside relay's scope?
