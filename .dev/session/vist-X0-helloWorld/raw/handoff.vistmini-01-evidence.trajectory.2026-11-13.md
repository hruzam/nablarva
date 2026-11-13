---
kind: handoff
date: 2026-11-13
seat: trajectory|engineer (Claude Opus, home)
part: 01 of 4 (evidence)
evidence_root: ~/ia-sync/.dev/session/vistMini-01-tests/
---

# 01 · Evidence: what was tested and what was observed

Home only (hostname `hruzam`), tmux 3.7c, bash 5.3.15, codex-cli 0.167.2, Claude Code 2.1.286. Seats: `traj-home` pane
`%3` (Claude, trajectory, head) and `cartan-home` pane `%2` (Codex, cartan|astrobley, Sol).

## 1. Cycle log

| cycle | aim | outcome | lesson |
|---|---|---|---|
| 01 | pre-register refusal/recovery matrix | ACCEPT. C01–C18 on stand-ins | stand-ins model *pre-typing* screens only |
| 02 | first live send | BLOCKED. Both agents ran as children of an interactive zsh (C11) | a pointer could land in a shell. Launch with `exec` |
| 03 | 3+3 ordinary messages | Codex→Claude 3/3. Claude→Codex 0/3 (t01, t02 clean refusal 29; t03 uncertain 27) | stop rule fired correctly; adapter safe but unusable |
| 04 | research Codex inbound + ask Astra | research ACCEPT; Astra blocked by `active writer (-32600)`, later answered via operator | native doors exist |
| 05 | one `codex queue` probe | q01 delivered and consumed, nonce matched | first Claude→Codex without relay |

Plus, out of band: Oraculum (Codex) reached the Claude seat through **Claude cross-session messaging** via a "Codex delivery
worker" (marker VIST-READING-20261112-01). Mechanism not inspected.

## 2. The keystroke adapter (`scripts/bus-poke.sh`, by cartan)

Checks before sending: pane exists, agent is the pane's root process (not under a shell), composer empty, not busy, renderer
recognised, no duplicate. Exit codes: `2` usage · `20` unknown target · `21` dead · `22` not an agent · `23` composer occupied ·
`24` busy · `25` duplicate/uncertain prior · `26` lifetime/enclosing shell · `27` text not visible after typing, no Enter sent
(uncertain) · `28` state/injection failure · `29` unrecognised composer · `30` invalid pointer. Reservation keys per message live
in a state dir. An uncertain key is never retried. `scripts/handoff-once.sh`: wait 8 s at turn end, check both panes, send once.

Observed: Codex→Claude worked 3/3. Claude→Codex failed three different ways (29, 29, 27). **The safety property held and
usability did not.** The likely cause of 27 and of one manual failure (hypothesis, never controlled): Codex treats a fast burst
of typed text as a paste, and an Enter arriving inside that window becomes a newline, not a submit. `sleep 1` between text and
Enter worked. Separate tool calls without it did not.

## 3. Carrier matrix (directions × doors)

| direction | door | status here | notes |
|---|---|---|---|
| Codex→Claude | tmux adapter | **3/3** | needs Claude footer signatures per version |
| Codex→Claude | Claude cross-session messaging (via delivery worker) | observed once | how the worker got the session socket: unknown |
| Claude→Codex | `codex queue --thread <id> --message <text>` (no `--resume`) | **1/1 (q01)** | exit 0 + queue id. Started a turn in the live TUI within the same second. No keys |
| Claude→Codex | tmux keystrokes | 0/3 | paste-window hypothesis |
| Codex→Codex | `mcp__codex_tui__send_message_to_thread` | stable on office (Jev, cycles 09–11) | fails `-32600 active writer` when the target thread is held elsewhere. Runtime adds sender context to the message |
| Claude→Claude | `SendMessage` / `ListAgents` | documented, untested here | |
| any→Claude (state) | `claude agents --json` | documented | busy/idle without a TTY. Replaces footer parsing |
| any→Codex (state) | `read_thread` (Codex native) | used by cartan | gave turn ids and start time for q01 |

Untested for queue: busy receiver, duplicate, wake from long idle, `--resume` (may create a second writer: avoid until tested),
`ssh <host> codex queue …` cross-host.

## 4. How q01 was proven (the pattern worth keeping)

1. POINT with `msg`, random `nonce`, `bell:` committed and pushed **before** sending.
2. One carrier call, logged with UTC before/after and exit code.
3. Read-only pane capture: idle → Working within ~4 s, no input.
4. Receiver writes a receipt: msg id, nonce copied from the file, receiving turn id, turn start time, idle-before, how it arrived.
5. Head compares nonce + time + log. Operator states no input.

This is VIST's sense → act → receipt loop in miniature (vist-01 "Where VIST sits"). The sensor (tmux/read_thread) and actuator
(queue) were different tools.

## 5. What is NOT established

Cross-host anything · permission boundaries · busy/duplicate behaviour of native doors · whether any door survives a CLI
upgrade · the delivery worker's mechanism · reliability (3 successes are a smoke test, not statistics).
