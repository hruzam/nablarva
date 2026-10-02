# STATUS — ovitmugen-01-basement

```yaml
updated: "2026-10-02 (00 closed GO and pruned; keepers moved here)"
writer: trajectory · anthropic
host: office · hruzam-120922
worktree: |
  ia-sync main at b435af5, on origin (all ovitmugen work through the home fix is pushed).
  nablarva core: own commits (00 closure, this bed) sit above other writers' unpushed commits —
  push only with an explicit refspec to an own commit, after those writers push.
gate: >-
  Majkee records GO or STOP after walking it live on office — ov-up with no name restores
  the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p
  jump agent tabs from either half; the halves swap left/right and up/down by key, and a
  preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the
  new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches
  AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
checkpoint: >-
  Bed authored 2026-10-02 by the ovitmugen-00-console head. Design and all majkee answers
  (D1–D5, layout + addendum) are in this bed's raw/architecture.pipes-ui-keys.2026-09-29.md (moved from 00);
  § KEYS CODE is in AGENTS.PROJECT-DESIGN.md (committed by another writer in addbe07).
  Nothing of 01 is built. Baseline: ov-selftest OK (office + home), runbook selftest PASS at ia-sync b435af5.
in_flight: none
recovery_probe: >-
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/ — RUNBOOK.md and
  STATUS.md present means the bed is authored; then python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py
  selftest — OK means the baseline is intact, FAIL names the check that broke before 01 began.
  git -C /home/hruzam/ia-sync log --oneline -1 shows whether anything landed after b435af5.
holds:
  - ov-ls --json output shape stays as today (consumer contract of nablarva-00 and nablarva-03-app-architecture); the v1 map is added beside it.
  - D2 state dir is input to nablarva-03-app-architecture (data/runtime homes) — majkee relays it to Cartan before B1 writes ~/.local/state/ovitmugen/.
  - "Carried tasks OUTSIDE this gate (from the closed 00 bed) — session-browser GUIDE res/examples.md
    (/home/hruzam/reposoma/raw.guides/session-browser/res/examples.md, teach the final TUI) ·
    pad.1-remote-cli-walk.md in this bed (majkee's PAD) · receipt navigation idea (display-only)."
  - No deploy by this session; ia-sync journal is another writer's; AGENTS.PROJECT-DESIGN.md append-only.
  - Tests only on isolated tmux sockets; never send-keys into agent panes; never close a busy tab.
next: >-
  majkee wakes a fresh Trajectory with prompt-0 of
  /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md
  (optionally via the cold-start card that points here). Its first build step is B1.
expected: >-
  The fresh head reports the B1 file-scope notice and the D2 relay status before writing
  code, then rewrites this STATUS with B1 in_flight.
```
