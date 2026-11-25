updated: 2026-11-25 23:50 UTC
writer: lead.seswin · claude
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · HEAD 5f22248 when written (the commit with this snapshot follows) · dirty, not
  this bed's: .dev/session/eSharp/answers.sheet-2.majkee.2026-11-25.md and .dev/session/eSharp/roster-proposal.eSharp.md
  (Majkee's edits), nano.2280604.save (untracked, his)
gate: >
  Majkee records GO or STOP on a witnessed status-surface packet — what the installed Claude status line really receives and
  shows; the same fields for one Codex session by reading only; the three display routes (native status line · second tmux
  status row · metadata pane) tried side by side on a separate tmux server, each checked for whether inspection and one
  pointer line still reach the intended pane; one recommended smallest first version, with the place for the chess clock.
  No helper is built yet.
checkpoint: >-
  The frame exists; no seat of this bed holds the pen. RUNBOOK.md and this snapshot were written by the eSharp manager
  (trajectory · claude; session `helloWorld`, window `eSharp`), not by the lead. Majkee built the tmux session `seswin` on
  2026-11-26: window `lead` (pane %80) and window `audit` (pane %81) hold a shell each and no CLI yet. The shared
  `supervisorCli` runs in `helloWorld` (pane %75) and has its brief. The predecessor bed is closed for the record
  (/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/STATUS.md). Where things are tried, and the
  release for it, are asked of Majkee and not given
  (/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md, section 11).
in_flight: none
recovery_probe: >-
  Read-only, three looks.
  (1) `ls /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/raw/` — no such folder, or no
  `decision.majkee.*` file in it, means the lead is not bound and no release exists.
  (2) `tmux list-panes -s -t seswin -F '#{window_name} #{pane_id} #{pane_current_command}'` — `zsh` in a window means its
  CLI is not started; `claude` in `lead` and `codex` in `audit` mean the seats run.
  (3) `tmux -L session-window list-sessions` answers "no server running", and
  `tmux list-panes -s -t sandbox -F '#{window_name} #{pane_current_command}'` shows only `zsh`, while nothing is released.
  Anything else without a release file in raw/ means something was started without leave: touch nothing and tell Majkee.
holds:
  - Where things are tried is not settled and its release is not given. No `tmux -L session-window` server, nothing run or
    typed in the tmux session `sandbox`, no sample CLI, no capture, until Majkee's yes is in a decision file in this bed's raw/.
  - No seat's pane and no pane on the usual tmux server is ever a target of a try. The deployed status line, ia-sync and the
    live Claude settings are not changed; no deploy.
  - The GitHub remote is public. No cache, capture, transcript or raw status-line record goes into Git.
  - Majkee's own files in eSharp/ (his sheet answers, his roster) are never staged by a seat.
  - L12 — plain pull and push on `core`; supervisorCli is the only pusher; commits by file name.
next: >-
  Majkee starts the two CLIs of this group, on the manager's request of 2026-11-26 — in the tmux session `seswin`: window
  `lead` (pane %80), Claude in the flight build, nick lead.seswin; window `audit` (pane %81), Codex with the Oraculum
  profile, nick audit.seswin — and tells the eSharp manager.
expected: >-
  Both panes run their CLI and each footer shows its posture. The manager has sent each seat one pointer line to its prompt in
  /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/RUNBOOK.md. A decision file in raw/ holds
  Majkee's words giving lead.seswin the pen, and the lead has replaced this snapshot with its own.
