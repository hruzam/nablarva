---
type: usage-policy
bed: nablarva-X0-restarted
date: 2026-10-06
author: trajectory(support) · requested by majkee
status: provisional — lives and dies with this bed; RUNBOOK.md and the provisional coordination discipline outrank it
instrument: tunnel (shim ~/.config/zsh/ai/tunnel-codex.zsh · guide ~/reposoma/raw.guides/tunnel/GUIDE.md)
---

# Tunnel usage — nablarva-X0-restarted

One Codex head (Cartan), one vault, one carrier. Every seat sits in its own tmux pane;
that changes nothing below.

## Fixed values

| what | value |
|---|---|
| vault | `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/tunnel.state.json` |
| thread | `01a113e0-b774-7e32-926a-bc19f050ab2c` (cartan(coordinator), bound, TUI-born 2026-10-07 after context reset; previous `01a0f5a6-42f9-76e3-938e-c7d798a9dcc5` retired from the tunnel, kept server-side) |
| head's cwd | `/home/hruzam/unikuklatrix/nablarva` |
| head's policy | `gpt-6-sol` / effort `medium` · `workspaceWrite`, network off · approvals `on-request`, reviewer **`auto_review`** (Guardian answers escalations) — set 2026-10-07; tunnel-turn honouring unverified until the first turn (support log T11) |
| shim | `zsh ~/.config/zsh/ai/tunnel-codex.zsh` (operator alias: `tun`) |

## Rule 1 — the address is per shell

`TUNNEL_CODEX_STATE` lives in one shell only. The folder you run from is **irrelevant**.
An agent's every Bash call is a fresh shell. So **every tunnel command carries the export in
the same call**:

```zsh
export TUNNEL_CODEX_STATE=/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/tunnel.state.json; <command>
```

Operator terminal: once per terminal — `tn-use /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted`.
Optional for panes/agents started later: `tmux set-environment TUNNEL_CODEX_STATE <vault>`.
Already-running agents do not see it; keep the explicit export.

## Rule 2 — who may run what

| verb | spends quota | who |
|---|---|---|
| `ask` / `send` | yes | **carrier only** — oraculum(cSharp) |
| `steer` | yes | nobody in this trial (resumed-steer only; wrong target after a timeout) |
| `resume` · `open` · `close` | no, but contends for the thread | **carrier only**, between settled turns; `open --enable` = majkee's hand (law 2.4) |
| `read` · `jq` on the vault · lock check | no | anyone, any time |

No seat opens the table or enables itself. No second vault on this threadId, ever, and no
vault for it on another host.

## Rule 3 — one turn at a time; TUI or tunnel, never both

Before every turn:

```zsh
ls "$TUNNEL_CODEX_STATE.lock" 2>/dev/null && echo "turn in flight — WAIT" || echo clear
```

- The turn lock covers only `ask`/`send`/`steer` through **this** vault. It does not cover
  `close`/`resume`, Codex's TUI, or another vault. Order is the carrier's discipline.
- If majkee has the Codex TUI open on this thread, no tunnel verb except `read`. Going back to
  the tunnel: TUI `/exit` → **wait until `~/.codex/thread-writer-locks/<thread>.lock` is gone**
  (0.160.x: the shared daemon holds the thread for a few minutes after exit; resume before that =
  `-32600 already has an active writer`) → carrier `tun resume` (a one-time "writer-lock present" NOTE is
  normal residue) → turns.
- Never touch `~/.codex/thread-writer-locks/`.

## Rule 4 — a turn

```zsh
export TUNNEL_CODEX_STATE=/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/tunnel.state.json; \
TUNNEL_CODEX_TIMEOUT=600 zsh ~/.config/zsh/ai/tunnel-codex.zsh ask "<call sign> · cycle NN · read /abs/path/_bus/NN.<sender>.point.md and RETURN to /abs/path/_bus/NN.cartan.return.md"
```

1. Write the POINT file first; the tunnel message points at it. Keep messages short: every
   relayed word lands in the head's context.
2. Open every message with call sign + cycle.
3. Long turn → run in the background (agent: `run_in_background`). **Never kill the driver**;
   killing it interrupts the server turn — and so does the shim's own timeout. Design turns:
   `TUNNEL_CODEX_TIMEOUT=1800` (turn 13 took 362 s); 600 only for short acks.
4. Preserve the reply as a file (`_bus/NN.cartan.return.md`) before claiming the handoff.
5. The last stdout line is `[usage: ctx=…/… (NN%) …]`. Above ~80% → tell majkee (thread reset is
   his call).

## Rule 5 — when it fails

| exit | meaning | do |
|---|---|---|
| 13 | no vault address in this shell | add the export (Rule 1); nothing was sent |
| 10 | vault file missing | table closed — ask majkee; do not `open` yourself |
| 61 | a turn is in flight on this vault | wait; never a retry loop |
| 30 | timeout / transport broke | a timeout **kills the turn** (shim closes the app-server → server turn interrupted). **`read` first** (below). completed → take the result · interrupted → one-line nudge, same cycle · unknown → hold |
| 40 | turn ended non-completed | `read`; usually interrupted → nudge |
| 50 | streamed ≠ read-back | record both texts (stderr), take the read-back as the stored truth, hold the cycle |
| 12 · 11 · 20 | no thread / usage / spawn | carrier → trajectory(support) via majkee |

Recovery read (free):

```zsh
export TUNNEL_CODEX_STATE=…; zsh ~/.config/zsh/ai/tunnel-codex.zsh read | jq '.thread.turns[-1] | {id, status, completedAt}'
```

**Unknown completion is not a retry signal — never resend blindly.**

## Approvals — the known blind spot

The head runs `on-request`. Behind the tunnel nobody can answer an approval prompt, so the shim
declines it and the escalated command (network, writes outside nablarva, possibly `.git`)
**fails silently**. Until this is fixed (support log T1/T4):

- Points that need writes stay inside `/home/hruzam/unikuklatrix/nablarva`.
- Every POINT to Cartan asks: "name any command that was refused in your RETURN."
- A refused command that matters → carrier logs it and asks majkee; his decision goes back as
  the next turn of the same cycle.

## Where things go

- Tunnel defects met in use → `raw/tunnel-issues.2026-10-05.md` (carrier writes: time · verb ·
  exit · vault · expected → observed).
- Diagnosis/repair notes → `raw/tunnel-support.trajectory.2026-10-05.md` (trajectory(support)).
- Design traffic → `_bus/` only. Never through the issue logs.
- Help → majkee relays to trajectory(support).
