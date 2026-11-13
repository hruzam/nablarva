---
kind: handoff
date: 2026-11-13
seat: trajectory|engineer (Claude Opus, home)
part: 03 of 4 (runbook substrate)
status: PROPOSED. Raw material for the head's RUNBOOK. Every item needs the head's adoption. Transport needs majkee's release (L21).
---

# 03 · Runbook substrate

## 1. A candidate gate (stricter than vistMini's, smaller in scope)

> On one host, each of the four directions (C→C, C→X, X→C, X→X; C = Claude, X = Codex) delivers **3 ordinary bus pointers**
> through a **declared carrier**, each consumed with a nonce-matched receipt, with no operator input to the receiver; every
> pre-registered refusal case run live; carriers and their failure modes recorded per CLI version; limits for cross-host stated.

Cross-host is a separate, later gate. vistMini's RUNBOOK made the same split.

## 2. Hardcoded resolver (majkee's idea; I back it)

The bus frontmatter already has `to:` and `from:`. A fixed script resolves the target and calls a carrier. Agents never pick
transport.

```yaml
# seats.yaml (data, not code; one row per seat)
oraculum|crawlers: {host: home, vendor: codex,  thread: <uuid>, tmux: <session>:0.0, carriers: [codex-queue, tmux]}
trajectory|delta:  {host: home, vendor: claude, session: <id>,  tmux: <session>:0.0, carriers: [claude-msg, tmux]}
```

`deliver <bus-file>` reads `to:`, looks up the row, tries carriers in order, stops at the first definite result, writes one
receipt line. Code is stable. Seats, carriers and signatures are data (vist-01 "Registries").

## 3. Result ladder (majkee's null/false/true, made explicit)

| level | meaning | next |
|---|---|---|
| `null` | host or tmux unreachable | stop, report |
| `absent` | no pane, thread or session for the seat | stop, report |
| `dead` | pane exists, agent gone | **operator** decides resume. Never automatic |
| `held` | alive but busy or composer occupied | one later retry, then report |
| `uncertain` | carrier may or may not have submitted | preserve the key, **never retry**, report |
| `delivered` | carrier confirms submission (exit 0 + id, or turn started) | wait for receipt |
| `consumed` | receipt with matching nonce | done |

## 4. Receipts without agent cost (proposal, untested)

A receiver-side hook writes a "copy" line at turn start: Claude `UserPromptSubmit`, Codex `notify`. That proves the turn
started at zero agent context. Consumption still needs the agent's correlated return. A bash auto-reply proves only that bash ran.

## 5. Pre-registered cases to run live (from vistMini, not yet run live)

Busy receiver per native door · duplicate send (same msg id twice) · expired envelope · wrong recipient · dead pane · receiver
under a shell · uncertain submit (keystroke carrier) · CLI version bump (canary) · `--resume` on queue (second writer?) · writer
conflict (`-32600`) · self-echo (sensor sees the actuator's own string, must tag `caused_by`).

## 6. Do not rebuild

`bus-poke.sh` guards (lifetime, root process, composer, duplicate keys) already encode the safety rules. Reuse them as the
**tmux carrier and sensor** and drop their role as the only door. The POINT/RETURN/VERDICT bus, six-field RETURN, single writer
per file and STATUS-as-sole-doing-state worked. Keep them.

## 7. Questions for the head to settle first

1. Seat ids unique across vendors? (two `oraculum`)
2. Who owns push and Git windows in nablarva?
3. Claude permission mode for the trial (auto hides the boundary)?
4. Is the delivery worker that reached Claude a reusable carrier, and what does it need?
5. Does VIST adopt "receipt = truth, screen = evidence", or does the team want the screen to carry more (S9 in file 02)?
