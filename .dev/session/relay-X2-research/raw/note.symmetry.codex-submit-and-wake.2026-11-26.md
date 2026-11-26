---
kind: side note — a small web research and four ideas, beside the verdict of relay-X2-research
by: Symmetry (claude.ai, Fable 5.2) · 2026-11-26 · at Majkee's spoken request during his reading of research-verdict.md
status: NOT evidence of the bed. Web sources only. Nothing was tested: no session started, no door tried.
reading: some pages were read through a summarising fetch, not raw bytes. Versions and dates are the sources' own.
repo_state_read: github.com/hruzam/nablarva at 81f5e6f (shallow clone); .majkee/ and .hlm/ not opened.
does_not: change the ranking REFUSE · ADOPT · REINVENT, open any bed, or decide the carrier (verdict §7).
---

# 1. What was found

## 1.1 Codex composer: why an Enter after a fast send does not submit

Codex's TUI has a paste-burst detector. A fast stream of characters is treated as a paste.
While the burst is active, and for a short suppression window after it, Enter is taken as a
newline inside the paste, not as "submit".

- Source: `codex-rs/tui/src/bottom_pane/paste_burst.rs` and `docs/tui-chat-composer.md`
  (mirrors read: https://docs.rs/crate/koda-cli/0.2.27/source/src/composer/paste_burst.rs —
  a verbatim port, upstream commit of 2026-05-01;
  https://forge.lthn.ai/core/core-agent-ide/raw/commit/58e8f75b276bbc6bae5bde633137ceee399db6d9/docs/tui-chat-composer.md).
  The upstream files themselves were not read on github.com/openai/codex.
- What it would explain: "sent but left in the composer" (W rows 42, 43) and the 0/3 into Codex
  recorded in relay-X0-carryover. That it is the cause on this host is a hypothesis, not a finding.
- Not found in W, R or A; they hold the symptoms, not this mechanism.
- Community practice disagrees on the remedy:
  - netsky-core 0.1.2 sends plain keystrokes, avoids bracketed paste, and waits 500 ms before
    `C-m` (https://docs.rs/crate/netsky-core/0.1.2/source/src/runtime/codex.rs). Its comment says
    bracketed input can stop Enter from submitting. The 500 ms is not explained in the source.
  - The verdict (§2) cites the opposite remedy — one bracketed paste, then a single Enter — and
    already calls it proposed, not validated.
  - A sibling case in another CLI: Enter lost when it arrives in the same PTY write as the end
    of a bracketed paste (Cursor CLI,
    https://forum.cursor.com/t/cursor-cli-does-not-submit-a-bracketed-pasted-prompt-when-enter-arrives-in-the-same-pty-input-chunk/166674).
- Unknown: the exact window on Codex 0.172.0 on Linux inside tmux 3.7c.

## 1.2 Claude Code: an idle session woken by a file write, no typing

A published recipe: a `FileChanged` hook on a per-session watch path, run with `asyncRewake`,
wakes an idle session. It is a doorbell only — the injected prefix is fixed, so the agent
fetches the message body from the file itself. A `SessionStart` hook arms the watch.

- Source: pi-shell-acp 0.11.1, `scripts/raw-async-delivery/README.md`
  (https://cdn.jsdelivr.net/npm/@junghanacs/pi-shell-acp@0.11.1/scripts/raw-async-delivery/README.md).
- Measured by its author on Claude Code 2.1.163. This host runs 2.1.332.
- In this repository the door exists on paper only
  (`relay-X0-carryover/raw/doors.inventory.2026-11-21.md`, row D, `asyncRewake`).
- Standing: a vendor hook, so weather under D1. It needs a hook installed and kept trusted.

## 1.3 Codex: whether a session can be addressed depends on how it was launched

Same source as 1.2:

- An embedded standalone TUI binds no external socket and has no file-watch hook. Not
  addressable from outside; fixed at launch.
- If an app-server listens at the default socket path
  (`$HOME/.codex/app-server-control/app-server-control.sock`) before launch, plain `codex`
  attaches to it. `turn/start` on that socket then wakes an idle thread with no typing, and
  `thread/status/changed` reports the end of the turn.
- Caveats it names: socket directory owned and 0700; any `-c` override disables the
  auto-attach; `turn/steer` needs an active turn and is not a wake.
- Measured on Codex 0.136.0, 2026-06-05. This host runs 0.172.0.
- Bears on W's open point (line 129: whether a plain TUI exposes thread status to a second
  client). It would give the receipt `codex queue` lacks. Still a vendor door.

## 1.4 hcom: a wrapper that owns the PTY, idle taken from Codex's own hook

Codex's `notify` hook fires at turn completion; hcom's hook marks the instance listening,
writes `idle_since`, and sends a TCP wake to a wrapper that owns the PTY and injects the
message (https://www.mintlify.com/aannoo/hcom/integration/codex; hcom is in A's table, this
mechanism is not spelled out there).

- Idle comes from an emitted signal, not from the screen.
- Blind spots: before the first turn completes, and while an approval waits — no notify fires.
- The page does not say how the text is submitted.

# 2. Ideas — Symmetry's own, none tested, none a build request

1. **Do not look for the reply in the PTY.** A TUI emits cursor-addressed repaints, not a
   linear text stream. Recovering the answer from it means emulating the terminal — a screen
   classifier by another door. The answer is already on disk (rollout, transcript, RETURN).
   Keep the PTY for the impulse and for discrete signals.
2. **Closed loop instead of a fixed pause.** An adapter that owns the PTY also sees its output.
   Write the pointer; wait until its echo appears in the output stream; then send Enter. Confirm
   submission on the file plane (a new rollout entry, or the submit hook); if it is missing
   after a deadline, repeat the Enter only. This turns "500 ms and hope" into something with a
   pass/fail record.
3. **Pull instead of push.** The recipient ends its turn by running a blocking command —
   `tmux wait-for <channel>` or `inotifywait` on its mailbox — that returns when mail arrives.
   The session never goes idle, so nothing has to wake it; no vendor door, no typing into a
   pane. To be measured before believed: tool-call time limits on both CLIs, what a held turn
   costs, and how a human's own input interleaves with it.
4. **State from the lab's tap.** termpanum's tap already carries the pane's bytes; the status
   sequence OSC 7501 is in them where the CLI emits it. A relay core could read state from
   that record instead of a sensor of its own. Unverified: that either CLI emits it inside
   tmux on this host (verdict §9).

# 3. If relay-X3-pty is ever opened — the one small question this suggests

On Codex 0.172.0 in tmux 3.7c on this host: for which way of writing (plain keystrokes,
bracketed paste) and which gap before Enter does a one-line pointer submit, counted over a
named number of tries, with submission read from the rollout and not from the screen?

# 4. What this note does not show

- That any of 1.1 to 1.4 holds on the installed versions.
- That idea 3 survives real tool timeouts.
- Anything about Antigravity CLI, Gemini CLI or Cursor CLI beyond the one forum report.
- L4: whether a write by an adapter that owns the PTY counts as the recorded death
  "send-keys injection" is Majkee's reading to give, not this note's.
