# STATUS: session-window-X0-substrate

```yaml
updated: 2026-11-19
writer: trajectory · claude · home (bed move ia-sync → nablarva)
host: home · hruzam (office not inspected)
origin: >-
  Moved verbatim from ~/ia-sync/.dev/session/helper-utils-00-tmux/raw/ (sha256 identical,
  ia-sync tombstone MOVED.md left there). The ia-sync bed never had a STATUS; this is the first.
gate: >-
  PROVISIONAL — Majkee to confirm or rewrite. Majkee records GO or STOP on a
  small personal session-window helper scope: what the first version does
  (smallest useful action set), where it lives, the per-CLI metadata display
  route (native status line vs. tmux metadata pane vs. second tmux status row),
  and independent views with usable scrollback as default behaviour.
checkpoint: >-
  Substrate only. Raw inputs gathered 2026-11-13/14 on home: Cartan goal substrate,
  Claude probe export, Cartan live tmux setup + comfort profile, retiring-Trajectory
  senior advice. No helper code written; no scheme schema; no design lock.
in_flight: none
evidence_state:
  - observed (home 2026-11-13): native Claude statusLine line truncates with … at width.
  - conflict (unresolved): official docs claim multiline output + COLUMNS + session_name/effort
    fields; not verified against the installed CLI (now 2.1.328 on home). First probe = dump one
    real statusLine stdin payload.
  - candidate: statusLine callback tees its JSON to a file a metadata pane reads (exact data,
    refreshes only on CLI events) — untested.
  - candidate: second tmux status row (handoff.senior-advice §1.3) — untested here.
related_live_surfaces:
  - ~/ia-sync/claude/hooks/statusline.sh + statusLine in ~/ia-sync/claude/settings.json —
    deployed Claude status line authored in this work; stays in ia-sync (deploy surface).
    Changes go through ia-sync compose-first + deploy.sh.
  - raw/tmux-comfort.conf was manually loaded into home's tmux server only; not on office.
  - sibling matter: terminal-workspace-X0-approaches (shared task terminal) — overlapping
    ground (tmux, panes, views); keep scopes separate unless Majkee merges them.
holds:
  - No build, no deploy, no canon. Gate text above is provisional until Majkee confirms.
  - Claude ↔ Cartan cooperation rhythm: Majkee explains; not invented here.
  - Home tmux session helper-utils-00-tmux (+ --claude/--codex views) is home-local, not transported.
next: >-
  On office: Majkee confirms/rewrites the gate; then the first probe — capture the installed
  Claude statusLine stdin payload and record which fields exist (effort, session_name,
  context_window, multiline behaviour), with CLI version.
expected: >-
  A confirmed gate and one version-stamped payload record, resolving the truncation-vs-docs conflict.
```
