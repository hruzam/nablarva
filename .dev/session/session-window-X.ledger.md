---
line: session-window
generation: X
kind: uncanonical line ledger — points only; STATUS.md wins on conflict
read: stop at "## Solved" unless something strategic seems lost
update: at session open and session close only
attach: ovitmugen organ (session helper / tmux beds) — majkee 2026-11-19; not yet a named sub-organ
naming: session-window-X{0,1,…}-<slug of the particular work>
updated: 2026-11-25 (X0 closed for the record, X1 opened) · 2026-11-22 (pointer row for the deferred friendly reminder, from relay-X0-carryover) · 2026-11-19 (line opened with X0 bed moved from ia-sync)
by: trajectory (claude, home) · majkee request 2026-11-19
---
# session-window · line X · ledger

Personal, operator-facing session-window helper: independent tmux views per CLI, usable
scrollback, per-CLI metadata (model/effort · CWD · context left · session name · session ID ·
transcript path), saved launch recipes. User ↔ CLI windows — not agent ↔ agent delivery.

## Open
- [ ] X1 `session-window-X1-surface` — group 1 of eSharp; gate confirmed by majkee (sheet 1, E2): GO or STOP on a witnessed status-surface packet; no helper built · STATUS: `.dev/session/session-window-X1-surface/STATUS.md`
- [ ] Owed by majkee: the sandbox release for X1 (sheet 2, A3) — worded, not given
- [ ] First probe, carried into X1: installed Claude statusLine stdin payload (docs promise multiline + session_name/effort; observed truncation on home)
- [ ] Organ seam with ovitmugen: which part extends ovitmugen (`~/ia-sync/zsh/session/ovitmugen.*`, bed `ovitmugen-01-basement`) and which stays a separate helper — the X0 substrate names ovitmugen's fixed panes as the "cage" complaint
- [ ] Home of the helper and its `scheme-*.json` files — `.majkee/` path not settled
- [ ] Other hosts: office/monitor not probed; home tmux comfort profile never loaded on office
- [ ] Deferred here from the relay line (Majkee 2026-11-21 and 2026-11-22): the friendly reminder — a chess clock the operator can inspect, extend, pause and reset, with the helper window as its surface and workflow state shown apart from terminal output. Not built, not released, no owner until this line's group has its own lead. Definition and his words: `relay-X0-carryover/goals/G10.friendly-reminder.md` · `relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md` (T6, T11) · `relay-X0-carryover/raw/decision.majkee.walkthrough-2.2026-11-22.md` (S5)
- [ ] Parked: zero-pane read mode (transcripts + `capture-pane`) · vendor adapters for Codex metadata. (The second tmux status row is no longer parked: it is one of the three routes X1 tries.)
- [ ] Seam to the terminal-workspace line, files only: X1 writes the one list of status fields; the shared terminal's "somebody tried while it was closed" notice may be shown on this line's surface (majkee 2026-11-25, `eSharp.decisions.majkee.2026-11-22.md` §8)
- [ ] Not retired: X0 stays tracked and in place while X1 reads its `raw/`; retirement under the runbook guide is majkee's word, later

## Shared principles, separate organ
- Sibling line [terminal-workspace](terminal-workspace-X.ledger.md) — shared human-and-agent task terminal. Shares tmux ground and principles (bind to the real session not the newest file, mark stale/estimated values, never `kill-server`, trust dialogs by hand). Different organ: do not merge beds or gates without majkee.
- Agent delivery stays VIST's (L21); this line meets it only at data (window labels, session IDs).

## Solved
- [x] X0 `session-window-X0-substrate` closed for the record 2026-11-25 ("FLR" — for legal reason, majkee E1); its provisional gate was never confirmed, no GO and no STOP · closing STATUS: `.dev/session/session-window-X0-substrate/STATUS.md`
- [x] Bed moved verbatim from `~/ia-sync/.dev/session/helper-utils-00-tmux/` (sha256 checked; ia-sync MOVED.md tombstone) — nablarva@f5ca6a1, 2026-11-19
- [x] Cold-start card for office: `~/reposoma/_cold-start/card/CS.session-window-X0.office.2026-11-19.md`
- [x] Deployed Claude status line stays in ia-sync (`claude/hooks/statusline.sh`) — deploy surface, not moved
