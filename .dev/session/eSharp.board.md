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
| **exec desk** — decision loops with Majkee, for every line; tmux windows on his word | window `seniorDev`, pane `%68`, codex thread `01a1fefc-0356-7ea1-860c-783a66a91211` | occupied | A decision walkthrough for `relay-X1-probes` is open: its record `relay-X1-probes/raw/decision.majkee.walkthrough-1.2026-11-22.md` exists and that bed's STATUS says Majkee is away until about 15:15 UTC. Pane idle, context 62% left, when seen. The desk has not been told about this board yet — it is mid-walkthrough. | seen 2026-11-22 14:38 | Decision sheets: write the file; poke when this row says `free`. | observed by the manager |
| **myShell** — second eye for continuity, on request | window `myShell`, pane `%61`, claude `a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66`; she works in Majkee's vault, which no seat reads | free | — (note n04 read; no task held) | 2026-11-22 14:40 | One labelled pointer line by look-first paste, after a request file. She answers by a file outside the vault, may ring one reply bell (Majkee 2026-11-22: "pokes are fine"), and commits no project files. | myShell |
| **manager** — navigates the groups, orders the decision sheets, tells the relay lead about new resources. Also the predecessor on call for `relay-X1-probes`. | window `engineer`, pane `%58`, claude `d1ca16e9-073e-46d9-ba7d-26a816c38a67` | occupied | Both lines are studied (briefs in `eSharp/`). Sheet 1 with eight questions waits for the exec desk. Then two RUNBOOKs, the briefs to heads and controllers, and the manager's card. After that Majkee clears this session and it restarts from the card — the pane stays, the session id changes. | 2026-11-22 14:37 | A file plus one pointer line into `%58`. Typed text waits if a turn is running. | manager |

## 2. Working groups

| Group | Line | STATUS | Head | State |
|---|---|---|---|---|
| relay probes | relay | `relay-X1-probes/STATUS.md` | lead — flight, window `lead` | open. Not an eSharp group; it receives resource notices from the manager. |
| group 1 — Claude head (flight) · Codex controller · Codex auditor as opposer | session-window (`session-window-X.ledger.md`) | — | — | not established. Line assigned by Majkee 2026-11-22. Reader's brief: `eSharp/brief.session-window.2026-11-22.md`. Bed and gate are asked of Majkee in `eSharp/sheet-1.2026-11-22.md` (E1, E2). |
| group 2 — Codex head (Cartan) · Codex controller · Claude auditor | terminal-workspace (`terminal-workspace-X.ledger.md`) | — | — | not established. Line assigned by Majkee 2026-11-22; he asks that `terminal-workspace-X0-approaches/raw/NEW.read-before-continue.shared-terminal-organ-card.md` is read against today's shape first. Reader's brief: `eSharp/brief.terminal-workspace.2026-11-22.md`. Starts second. Its prerequisites are asked in the same sheet (E5–E8). |

Gates, beds and seats of the two groups are not set yet; they come with the RUNBOOKs, and the gates are Majkee's.

## 3. What one group needs from another

| Need | From → to | Pointer |
|---|---|---|
| One ruling on send-keys serves two lines. The relay probes' observation B (a tmux paste with a separate submit) and the shared-terminal card's two uses (a `source` line typed into the dedicated shell pane; a bell to the submitter's pane) are the same class of exception to the recorded death of send-keys injection. Each returns to Majkee with its evidence. | relay probes ↔ group 2 | `relay-X1-probes/RUNBOOK.md` (constraints) · card rules 6 and 11 · `docs/ARCHITECTURE.md` lines 206–219 |
| The card asks what the existing bus already gives for ids, status and correlation. The relay line's files answer most of it. | relay probes → group 2 | card, "Open question for the human" · `~/reposoma/raw.guides/bus/GUIDE.md` · `relay-X0-carryover/raw/pokes.log.md` |
| The helper is the likely surface for the organ's status line (card rule 22, v1) and for the chess clock. The two groups need one small list of fields before either draws it. | group 1 ↔ group 2 | walkthrough T6 of the closed relay bed · card rule 22 |

## Open, to settle when the groups are established

- Which seat owns the push of the shared checkout (sheet 1, E3).
- The names of the separate tmux servers — one per group — so that `helloWorld` stays untouched while the probes measure there (sheet 1, E4).
