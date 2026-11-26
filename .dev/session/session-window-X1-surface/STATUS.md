updated: 2026-11-26 02:04 UTC
writer: lead.seswin · claude
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · HEAD 9e393d4 when written (the commit with this snapshot follows) · dirty, not
  this bed's: .dev/session/eSharp/answers.sheet-2.majkee.2026-11-25.md and .dev/session/eSharp/roster-proposal.eSharp.md
  (Majkee's edits); untracked, not this bed's: two side-quest files in .dev/session/relay-X1-probes/raw/ and nano.2280604.save
gate: >
  Majkee records GO or STOP on a witnessed status-surface packet — what the installed Claude status line really receives and
  shows; the same fields for one Codex session by reading only; the three display routes (native status line · second tmux
  status row · metadata pane) tried side by side on a separate tmux server, each checked for whether inspection and one
  pointer line still reach the intended pane; one recommended smallest first version, with the place for the chess clock.
  No helper is built yet.
checkpoint: >-
  Both seats of the group run and have their briefs; nobody holds the pen yet. `seswin:lead` (pane %80, Claude, the flight
  build on Opus 5.5) and `seswin:audit` (pane %81, Codex, Oraculum profile) each got one pointer line from the eSharp manager
  on 2026-11-26 at 02:03 UTC (/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/_bus/07.manager.point.md and
  08.manager.point.md) and were seen working on it. RUNBOOK.md and this snapshot are still the manager's (trajectory · claude;
  session `helloWorld`, window `eSharp`). The frame had one opposing read
  (/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/_bus/03.seniorDev.return.md). The shared `supervisorCli` runs in
  `helloWorld` (pane %75) and has pushed on a poke. Majkee made the test server himself: `tmux -L sandbox-server`, session
  `sandbox`, four shell windows. The sandbox release is not given.
in_flight: none
recovery_probe: >-
  Read-only, three looks.
  (1) `ls /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/raw/` — no such folder, or no
  `decision.majkee.*` file in it, means the lead is not bound and no release exists.
  (2) `ls /home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/_bus/07.lead.seswin.return.md
  /home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/_bus/08.audit.seswin.return.md` — a missing file means that seat has
  not finished its first read; `tmux list-panes -s -t seswin -F '#{window_name} #{pane_id} #{pane_current_command}'` shows
  whether its CLI still runs (`claude` in `lead`, `codex` in `audit`).
  (3) `tmux -L sandbox-server list-panes -a -F '#{window_name} #{pane_id} #{pane_current_command}'` shows four windows with
  `zsh` while nothing is released. Anything else there without a release file in raw/ means something was started without
  leave: touch nothing and tell Majkee.
holds:
  - The sandbox release is not given. Nothing is run or typed on `tmux -L sandbox-server`, no sample CLI is started, nothing
    is captured, until Majkee's yes is in a decision file in this bed's raw/.
  - The sandbox server is shared with group 2 (its window `terminal`). Only options of the session `sandbox` and its windows
    are set there, nothing global; every command names the server and checks its target before it changes anything.
  - No seat's pane and no pane on the usual tmux server is ever a target of a try. The deployed status line, ia-sync and the
    live Claude settings are not changed; no deploy.
  - The GitHub remote is public. No cache, capture, transcript or raw status-line record goes into Git.
  - Majkee's own files in eSharp/ (his sheet answers, his roster) are never staged by a seat.
  - L12 — plain pull and push on `core`; supervisorCli is the only pusher; commits by file name.
next: >-
  Majkee gives lead.seswin the pen, in his own words, in the lead's pane (tmux session `seswin`, window `lead`); the lead
  writes them into a decision file in /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/raw/.
expected: >-
  A file `decision.majkee.*` in raw/ holds his words; lead.seswin has replaced this snapshot with its own and has written its
  roster; /home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/_bus/07.lead.seswin.return.md holds the lead's first read of
  the frame.
