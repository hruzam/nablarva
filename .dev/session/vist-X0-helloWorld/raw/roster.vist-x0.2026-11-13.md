---
kind: roster
bed: ~/unikuklatrix/nablarva/.dev/session/vist-X0-helloWorld/
owner: majkee (fills ids and addresses). Seats read it. Only the head proposes changes.
status: DRAFT. Seating is majkee's decision. See handoff.vistmini-00-index for the reasoning.
---

# Roster — vist-X0

One row per seat. Fill `<…>` when the seat is launched. Leave a field empty rather than guess.
This is the **data** for the resolver (`handoff.vistmini-03` §2). Keep it data, not prose.

## Which address does each vendor need? (from vistMini evidence)

| vendor | delivery address (inbound) | state probe | tmux pane needed? |
|---|---|---|---|
| **Codex** | thread UUID → `codex queue --thread <uuid> --message …` (1/1, q01). Codex↔Codex: same UUID via native `send_message_to_thread` | `read_thread` (Codex side) | **No** for delivery. Optional, as a read-only sensor |
| **Claude** | **tmux pane** (Codex→Claude adapter 3/3). Claude↔Claude: session id via `SendMessage` (documented, untested here) | `claude agents --json` (session id) | **Yes, today.** It's the only proven inbound door from Codex |

So majkee's assumption is right: **Claude needs the pane**, plus its session id for the state probe. Codex needs the thread UUID.

Pane rule: record `session:window.pane` (stable name) **and** the `%N` pane id (changes when the pane is recreated or the tmux
server restarts). Launch agents as the pane's root process, never under a shell:
`tmux new -d -s <session> -c <cwd> 'exec <agent command>'`.

## Seats

```yaml
- seat: cartan|astrobley
  vendor: codex
  model: Sol
  role: head            # issues POINT/VERDICT, owns STATUS; delegates the building
  host: home
  cwd: ~/ia-sync
  add_dirs: [~/unikuklatrix/nablarva]
  thread: <uuid>        # FRESH session recommended; not 01a1ce98-… (vistMini thread)
  tmux: <session>:0.0   # optional (sensor)
  pane_id: <%N>
  inbound: [codex-queue, codex-native]
  push: <yes|no>        # exactly one seat says yes, per repo
  launch: <exact command>

- seat: oraculum|crawlers
  vendor: codex
  model: Astra
  role: strategist      # outside the build; consulted by brief at gates only, never gets cycle pointers
  host: home
  cwd: ~/unikuklatrix/nablarva
  thread: <uuid>        # vistMini knew 01a1ceb4-452c-76e0-954a-3160ceadc2ed; native send hit "active writer" (-32600)
  tmux: none
  inbound: [codex-native, codex-queue]
  push: no
  launch: <exact command>

- seat: trajectory|delta
  vendor: claude
  model: Opus
  role: senior-dev (Claude-side builder)
  host: home
  cwd: ~/unikuklatrix/nablarva
  session: <claude session id>
  tmux: <session>:0.0   # REQUIRED today
  pane_id: <%N>
  permission_mode: <default|auto>   # default if the gate wants a witnessed permission boundary
  inbound: [tmux-adapter, claude-msg]
  push: <yes|no>
  launch: <exact command>

- seat: flight
  vendor: claude
  model: Fable
  role: auditor         # read-only verifier: no execution, no fixes; NOK goes back through the head
  host: home
  cwd: ~/unikuklatrix/nablarva
  session: <claude session id>
  tmux: <session>:0.0   # REQUIRED today
  pane_id: <%N>
  permission_mode: <default|auto>
  inbound: [tmux-adapter, claude-msg]
  push: no
  launch: <exact command>

- seat: sample-claude
  vendor: claude
  model: <cheap, e.g. haiku>
  role: test receiver   # receive, write nonce receipt, stop. All disruptive cases run here
  host: home
  cwd: <scratch dir>
  session: <id>
  tmux: <session>:0.0
  pane_id: <%N>
  inbound: [tmux-adapter, claude-msg]
  push: no

- seat: sample-codex
  vendor: codex
  model: <cheap>
  role: test receiver
  host: home
  cwd: <scratch dir>
  thread: <uuid>
  tmux: <session>:0.0   # optional (sensor)
  pane_id: <%N>
  inbound: [codex-queue, codex-native]
  push: no
```

## Operator views

Never attach two terminals to the same tmux session: the current window is per session, so they mirror. Use
`tmux new -t <session> -s <session>-<viewer>`.
