---
kind: eSharp board — noncanonical and provisional. Availability and pointers only. A group's STATUS owns its doing-state and wins on conflict; pulse.md stays the router.
what: (1) whether a shared seat can be contacted now · (2) where each working group's STATUS is · (3) what one group needs from another
not: no gate, no next action, no narrative, no script, no watcher. Plain markdown, read by eye or with `git diff` / `git log -p` on this file.
authority: Majkee 2026-11-22 — eSharp.decisions.majkee.2026-11-22.md ("we need small helper dashboard … Just markdown … Maybe we will not need that")
kept_by: the eSharp manager (today the engineer session d1ca16e9, window `engineer`). Each shared seat writes its own row.
---

# eSharp board

## How to use it

1. **One row per shared seat, written by that seat** — when it takes a task and when it is free again. Nobody edits another seat's
   row. A row the manager filled in from outside says `observed`.
2. **A row is a courtesy, not a lock.** Look at the pane before every poke all the same. A row that looks old is "unknown".
3. **Seat occupied?** Write your request file anyway and send the pointer line when the row says `free`. If it cannot wait, it is
   Majkee's call.
4. **The file on disk is the live truth** — every seat on home shares this checkout. The manager commits it at natural points, so
   the history is in the diffs.
5. This is not the presence board. `rb-board` says who is attached to which workspace; this says whether three shared seats can
   take a request.

## 1. Shared seats

| Seat | Where | State | With | Since (UTC) | Reach now | Row by |
|---|---|---|---|---|---|---|
| **exec desk** — decision loops with Majkee, for every line; tmux windows on his word | window `exec`, pane `%68`, codex thread `01a1fefc-0356-7ea1-860c-783a66a91211` | free | Idle at its prompt, context 45% left, when seen. Not asked for anything by the manager: Majkee answered sheets 1 and 2 himself. The desk has not been told about this board yet. | seen 2026-11-25 16:28 | Decision sheets: write the file; look at the pane; poke when it is idle at its prompt. | observed by the manager |
| **myShell** — second eye for continuity, on request | window `myShell`, pane `%61`, claude `a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66`; she works in Majkee's vault, which no seat reads | free | — (note n04 read; no task held) | 2026-11-22 14:40 | One labelled pointer line by look-first paste, after a request file. She answers by a file outside the vault, may ring one reply bell (Majkee 2026-11-22: "pokes are fine"), and commits no project files. | myShell |
| **manager** — navigates the groups, orders the decision sheets, tells the relay lead about new resources. Also the predecessor on call for `relay-X1-probes`. | session `helloWorld`, window `eSharp`, pane `%77` — the old pane `%58` is gone. Claude, attached job `4f923bb7`; older records name this seat by the session `d1ca16e9…`. | free | Group 1 is established and its lead holds the pen. Owed next: the manager's own card for a clear; group 2's frame when group 1 has closed a cycle. A side-quest from Majkee's roster runs beside it: `eSharp/side-quest.2026-11-26.md`. | 2026-11-26 02:47 | A file plus one pointer line into `%77`. Typed text waits if a turn is running. | manager |
| **supervisorCli** — the one pusher of the shared checkout; bounded work on a POINT; caches on request. Shared by the relay line and both groups (sheet 1, E3; sheet 2, B1). | session `helloWorld`, window `supervisorCli`, pane `%75`, codex thread `01a214df-7fd9-7952-9987-1750c56ef877` | free | Briefed, and its first push is done: `eSharp/_bus/02.supervisorCli.return.md` (three commits, `70aa917..3a9b91b`). Brief: `eSharp/brief.supervisorCli.2026-11-25.md`. The relay controller (window `supervisor-relay`, pane `%59`) keeps the relay line's push until the relay lead names the new seat. | 2026-11-25 23:50 | A POINT file, then `codex queue --thread <id>` with one pointer line. | the manager, until the seat writes its own row |
| **seniorDev** — the manager's thinking partner of the other brand: honest critique of what the manager is about to hand on (Majkee's roster, section 4.2). Not a group's auditor. | session `helloWorld`, window `seniorDev`, pane `%60`, codex thread `01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1`, Oraculum profile | free | Briefed; her first opposing read is in: `eSharp/_bus/03.seniorDev.return.md` (group 1's frame holds with changes; she holds for the separate test server). Brief: `eSharp/brief.seniorDev.2026-11-26.md`. | 2026-11-25 23:50 | A POINT from the manager only. | the manager, until the seat writes its own row |

## 2. Working groups

| Group | Line | STATUS | Head | State |
|---|---|---|---|---|
| relay probes | relay | `relay-X1-probes/STATUS.md` | lead — flight, window `lead` | open. Not an eSharp group; it receives resource notices from the manager. |
| group 1 — `lead.seswin` (Claude, flight on Opus 5.5) · `audit.seswin` (Codex, Oraculum profile) · `supervisorCli` (shared) | session-window (`session-window-X.ledger.md`) | `session-window-X1-surface/STATUS.md` | `lead.seswin` — tmux session `seswin`, window `lead`, pane `%80`; the auditor in window `audit`, pane `%81`, codex thread `01a21585-ca9f-74e1-af4c-6018f2c4c324` | established 2026-11-26: the lead holds the pen (`session-window-X1-surface/raw/decision.majkee.pen.2026-11-26.md`). From here its STATUS speaks; the manager writes nothing in that bed. |
| group 2 — `lead.terwor` (Codex, the Cartan build on gpt-6.1-sol) · `audit.terwor` (Claude, the flight build on Fable) · `supervisorCli` (shared) | terminal-workspace (`terminal-workspace-X.ledger.md`) | — | `lead.terwor` — tmux session `terwor`, window `lead`, pane `%82`; the auditor in window `audit`, pane `%83` | not established; starts when group 1 has closed a cycle. The tmux session exists with shells only. Bed to come: `terminal-workspace-X1-v0`; the old bed `terminal-workspace-X0-approaches` is closed by the new lead. The NEW card is the master (sheet 1, E5). Reader's brief: `eSharp/brief.terminal-workspace.2026-11-22.md`. Majkee's wishes for it: `eSharp.decisions.majkee.2026-11-22.md`, section 8. |

Group 1's gate is Majkee's own confirmation (sheet 1, E2). Group 2's gate is proposed in sheet 2 (A4) and accepted for now; it is fixed when its RUNBOOK is written.

Where things are tried: Majkee's separate tmux server, `tmux -L sandbox-server` (his map: chapter 6 of his roster). Since 2026-11-26 each group has a session of its own there: `sandbox` for group 1 — windows `codex-sample` (`%0`), `claude-sample` (`%1`), `session` (`%2`) — and `sandbox-terwor` for group 2 — window `terminal` (`%4`). Ids there are local to that server.

## 3. What one group needs from another

| Need | From → to | Pointer |
|---|---|---|
| One ruling on send-keys serves two lines. The relay probes' observation B (a tmux paste with a separate submit) and the shared-terminal card's two uses (a `source` line typed into the dedicated shell pane; a bell to the submitter's pane) are the same class of exception to the recorded death of send-keys injection. Each returns to Majkee with its evidence. | relay probes ↔ group 2 | `relay-X1-probes/RUNBOOK.md` (constraints) · card rules 6 and 11 · `docs/ARCHITECTURE.md` lines 206–219 |
| The card asks what the existing bus already gives for ids, status and correlation. The relay line's files answer most of it. | relay probes → group 2 | card, "Open question for the human" · `~/reposoma/raw.guides/bus/GUIDE.md` · `relay-X0-carryover/raw/pokes.log.md` |
| The helper is the likely surface for the organ's status line (card rule 22, v1) and for the chess clock. One small list of status fields serves both: group 1 writes it (`session-window-X1-surface/raw/fields.<date>.md`), group 2 reads it. | group 1 → group 2 | walkthrough T6 of the closed relay bed · card rule 22 · `session-window-X1-surface/RUNBOOK.md`, step 1 |
| Majkee wants to be told when somebody tries to send a command to a shared terminal that is closed, or not expected to be open for that sender. Group 2 owns the gate that refuses; group 1's surface is where he would see it. Group 1's packet names the place and builds nothing. | group 2 → group 1 | `eSharp.decisions.majkee.2026-11-22.md`, section 8 · `session-window-X1-surface/RUNBOOK.md`, step 5 |
| One test server serves both groups, each in a session of its own (`sandbox`, `sandbox-terwor`). A status row is an option of the session, so the groups no longer touch each other there; an option of the server itself still reaches both, and neither sets one. A change the other must know about goes through the manager. | group 1 ↔ group 2 | `eSharp/roster-proposal.eSharp.md`, chapter 6 · `eSharp/_bus/07.lead.seswin.return.md`, point 1 |

## Open

- The sandbox release for group 1 (sheet 2, A3): worded, not given. The lead asks Majkee for it at its read-back.
- The exec desk has not been told about this board.
- myShell is not asked for her part of the side-quest yet (`eSharp/request.myShell.side-quest.2026-11-26.md`): her input row was in use each time the manager looked.
- The relay group hears about the shared `supervisorCli` and the two projects from Majkee himself (sheet 1, E3; decisions, section 10).
- The relay bed stays open for a few experiments of his; he retires it himself.

Settled since 2026-11-22: one shared seat pushes (E3, B1). Every seat lives on the usual tmux server — the shared seats in
`helloWorld`, each group in a session of its own (`seswin`, `terwor`); Majkee built the tree on 2026-11-26 and accepted its
four rules. The tree: `eSharp.decisions.majkee.2026-11-22.md`, section 10. His map: `eSharp/roster-proposal.eSharp.md`.
