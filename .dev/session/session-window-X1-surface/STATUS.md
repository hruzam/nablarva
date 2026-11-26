updated: 2026-11-26 02:52 UTC
writer: lead.seswin · claude · flight build, claude-opus-5-5, effort xhigh — the first snapshot the lead wrote itself
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · HEAD 796d306 when written (the bind commit follows) · dirty, not this bed's:
  .dev/session/eSharp/answers.sheet-2.majkee.2026-11-25.md and .dev/session/eSharp/roster-proposal.eSharp.md (Majkee's
  edits); untracked, not this bed's: eSharp/_bus/10.*, two side-quest files in relay-X1-probes/raw/, nano.2280604.save
gate: >
  Majkee records GO or STOP on a witnessed status-surface packet — what the installed Claude status line really receives and
  shows; the same fields for one Codex session by reading only; the three display routes (native status line · second tmux
  status row · metadata pane) tried side by side on a separate tmux server, each checked for whether inspection and one
  pointer line still reach the intended pane; one recommended smallest first version, with the place for the chess clock.
  No helper is built yet.
checkpoint: >-
  Bound. Majkee gave lead.seswin the pen at about 02:43 UTC; his words are in raw/decision.majkee.pen.2026-11-26.md. The party
  matches live tmux: `$44 | 0 lead @78 | %80` claude (this seat) and `$44 | 1 audit @79 | %81` codex (audit.seswin,
  gpt-6.2-astra, effort high by her own record). RUNBOOK.md carries the lead's changes from its first read (roster and real
  models, the sandbox server as it now stands, read-only queries, versions, the Claude sample's settings, the pointer text) and
  stays open to change until the read-back at step 2. Step 1 has started.
in_flight:
  - s01 · epoch · Claude status-line input by the documentation · _bus/01.epoch-claude.point.md → _bus/01.epoch-claude.return.md
  - s02 · epoch · Codex session data by the documentation · _bus/02.epoch-codex.point.md → _bus/02.epoch-codex.return.md
  - s03 · field · statusline.sh, the X0 substrate and G10, by reading · _bus/03.field-local.point.md → _bus/03.field-local.return.md
recovery_probe: >-
  Read-only, three looks.
  (1) `ls /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/_bus/` — a `.point.md` without its
  `.return.md` is a child task still open or lost; children are in-process and die with the lead's session, so a lost one is
  issued again, not waited for.
  (2) `ls /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/raw/` — `decision.majkee.pen.*` present
  and no `decision.majkee.*release*` file means bound and not released.
  (3) `tmux -L sandbox-server list-panes -s -t '=sandbox' -F '#{window_name} #{pane_id} #{pane_current_command}'` shows
  `codex-sample %0`, `claude-sample %1`, `session %2`, each `zsh`, while nothing is released. Anything else there without a
  release file in raw/ means something was started without leave: touch nothing and tell Majkee.
holds:
  - The sandbox release is not given. Nothing is run or typed on `tmux -L sandbox-server`, no sample CLI is started, nothing
    is captured there, until Majkee's yes is in a decision file in this bed's raw/. Read-only queries are allowed
    (RUNBOOK, "What needs no release").
  - The session `sandbox` serves this group only; group 2 has `sandbox-terwor` on the same server. Only options of
    `sandbox` and its windows are set there, nothing global; every command names the server and checks its target first.
  - No seat's pane and no pane on the usual tmux server is ever a target of a try. The deployed status line, ia-sync and the
    live Claude settings are not changed; no deploy.
  - The GitHub remote is public. No cache, capture, transcript or raw status-line record goes into Git.
  - Majkee's own files in eSharp/ (his sheet answers, his roster) are never staged by a seat.
  - L12 — plain pull and push on `core`; supervisorCli is the only pusher; commits by file name.
asked_of_majkee:
  - Pen word, point 3, names `$45 | 1 audit @81 | %83` — live tmux gives those coordinates to audit.terwor (group 2). The
    lead reads it as audit.seswin (`$44 | 1 audit @79 | %81`) until he says otherwise.
  - That the session `sandbox` is now group 1's alone. His act (the session `sandbox-terwor`) says so; his words do not yet.
next: >-
  When s01–s03 have returned, the lead issues the field list (raw/fields.2026-11-26.md) to a child that writes it from the
  three returns, and has @assay check it against them; every row stays provisional until a sample shows it. Then step 2:
  the read-back sheet with the release and the start script, read once by audit.seswin before it goes to the exec desk.
expected: >-
  Three return files in _bus/, then raw/fields.2026-11-26.md with source and date on every row and an assay verdict.
