# STATUS — ovitmugen-01-basement

```yaml
updated: "2026-10-02 03:45 CEST"
writer: trajectory · anthropic
host: office · hruzam-120922
worktree: |
  ia-sync main at 55aef22 (ovitmugen help fallback, ours, 1 ahead, not pushed). Other writers'
  dirty paths, not ours: pulse.md, .dev/session/jev-implementation-00-build/.
  nablarva core at 852ff08, 14 ahead of origin with other writers' commits interleaved
  (muticula, research, convergence) — push only with an explicit refspec to an own commit.
  This bed (RUNBOOK.md, STATUS.md) and the pulse.md router row are new and uncommitted.
gate: >-
  Majkee records GO or STOP after walking it live on office — ov-up with no name restores
  the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p
  jump agent tabs from either half; the halves swap left/right and up/down by key, and a
  preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the
  new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches
  AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
checkpoint: >-
  Bed authored 2026-10-02 by the ovitmugen-00-console head. Design and all majkee answers
  (D1–D5, layout + addendum) are in ovitmugen-00-console/raw/architecture.pipes-ui-keys.2026-09-29.md;
  § KEYS CODE is in AGENTS.PROJECT-DESIGN.md (committed by another writer in addbe07).
  Nothing of 01 is built. Baseline: ov-selftest OK, runbook selftest PASS at ia-sync 55aef22.
in_flight: none
recovery_probe: >-
  ls /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/ — RUNBOOK.md and
  STATUS.md present means the bed is authored; then python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py
  selftest — OK means the baseline is intact, FAIL names the check that broke before 01 began.
  git -C /home/hruzam/ia-sync log --oneline -1 shows whether anything landed after 55aef22.
holds:
  - ov-ls --json output shape stays as today (consumer contract of nablarva-00 and nablarva-03-app-architecture); the v1 map is added beside it.
  - D2 state dir is input to nablarva-03-app-architecture (data/runtime homes) — majkee relays it to Cartan before B1 writes ~/.local/state/ovitmugen/.
  - ovitmugen-00-console stays open only for the home selftests; its STATUS owns that.
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
