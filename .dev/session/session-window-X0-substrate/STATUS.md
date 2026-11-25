updated: 2026-11-25 16:28 UTC
writer: trajectory · claude · home (the bed's only writer; this is its closing snapshot)
host: home · hruzam (office not inspected)
worktree: /home/hruzam/unikuklatrix/nablarva · core · HEAD eb26f28 when written (the closing commit follows)
state: CLOSED 2026-11-25, for the record. No GO and no STOP was ever recorded on this gate.
gate: >-
  PROVISIONAL — Majkee to confirm or rewrite. Majkee records GO or STOP on a
  small personal session-window helper scope: what the first version does
  (smallest useful action set), where it lives, the per-CLI metadata display
  route (native status line vs. tmux metadata pane vs. second tmux status row),
  and independent views with usable scrollback as default behaviour.
checkpoint: >-
  Closed on Majkee's word. Sheet 1, E1: "confirming `session-window-X1-surface` in case if previous session can be
  considered as closed, or at least we have to close it 'FLR'"; his voice answer of 2026-11-25: "FLR means only for legal
  reason". Both are verbatim in /home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md,
  sections 7 and 8. The provisional gate above was never confirmed, so nothing was decided in this bed. It holds substrate
  only: no helper code, no scheme schema, no design lock. The line continues in
  /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/ under a gate he confirmed.
in_flight: none
recovery_probe: >-
  Read-only: `git -C /home/hruzam/unikuklatrix/nablarva log --oneline -3 -- .dev/session/session-window-X0-substrate/`.
  The newest commit is the closing one; a newer commit, or a dirty path here, means somebody wrote into a closed bed —
  ask before going on. The live position of the line is
  /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/STATUS.md.
carried_to_X1:
  - >-
    Observed on home, 2026-11-13 — the native Claude status line cuts its text with … at the pane width.
  - >-
    Unresolved conflict — the official docs promise multiline output, COLUMNS and the fields session_name and effort;
    never checked against the installed CLI. The first probe, one real status-line input record, was never run.
  - >-
    Candidate, untested — the status-line command also writes its input to a file that a metadata pane reads.
  - >-
    Candidate, untested — a second tmux status row (raw/handoff.senior-advice.trajectory.2026-11-14.md, section 1.3).
  - >-
    Open with Majkee — where the helper and its scheme files live; which part extends ovitmugen and which stays separate.
  - >-
    The chess clock deferred to this line (../session-window-X.ledger.md, section Open).
related_live_surfaces:
  - ~/ia-sync/claude/hooks/statusline.sh and statusLine in ~/ia-sync/claude/settings.json — the deployed Claude status
    line; stays in ia-sync; changes go through its compose-first rule and deploy.sh.
  - raw/tmux-comfort.conf was loaded by hand into home's tmux server only; not on office.
holds:
  - The bed stays in place and tracked; raw/ is the successor's substrate and is read there by path. It is not retired
    under the runbook guide (unregister from Git, ignore) — that step changes what other hosts receive and is Majkee's
    word, later.
  - Nothing in this file is an assignment. A reader who wants to act goes to the successor's STATUS.
next: none in this bed — read /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/STATUS.md
expected: no further change to this file.
