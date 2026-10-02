# RUNBOOK: ovitmugen-01-basement

```yaml
goal: >-
  ovitmugen grows its basement: a neutral session map and remembered state other organs can
  read, fast agent-tab jumps, a bed that comes back as you left it, swappable halves in both
  monitor orientations with a small preset manager, and the shared key grammar honoured.
gate: >-
  Majkee records GO or STOP after walking it live on office — ov-up with no name restores
  the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p
  jump agent tabs from either half; the halves swap left/right and up/down by key, and a
  preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the
  new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches
  AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
participant_0: [trajectory, {brand: anthropic, model: operator-selected, effort: operator-selected}, {host: office, role: cSharp head, sole writer of ovitmugen source in scope, status_owner}]
participant_1: [delta, {brand: anthropic, model: agent-default, effort: agent-default}, {host: office, role: zero-judgment pieces spawned by trajectory, reviewed before report}]
participant_2: [majkee, {brand: human, model: none, effort: none}, {host: office + home, role: deploy hands, live walk, gavel}]
status_owner: trajectory
head_note: >-
  cSharp (res/csharp-head-protocol.md): a FRESH Trajectory incarnation sits as head, builds,
  spawns Delta for zero-judgment pieces, never self-confirms the gate. Predecessor: the
  ovitmugen-00-console head (ff-sync.trajectory.cSharp-oStar-ovitmugen).
schema_note: >-
  runbook/GUIDE.md Manifest read 2026-10-02 · status/GUIDE.md fixed fields · no _bus
  (one writer + in-window spawns). Wake choice: @Trajectory — the build needs senior
  judgment and an evidence-bearing return.
```

## Why this session exists

ovitmugen v1 works (00: office walk GO). Daily use showed the gaps: switching agent tabs
takes three moves, a rebuilt bed starts from scratch, layout is fixed, keys differ between
organs. Other organs (nablarva bus, termbrana) will need to read the sessions. Majkee
answered the basement design D1–D5 and the layout one question per turn; this builds it.

## Fixed facts (settled — do not re-litigate)

- Design + every answer: `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/raw/architecture.pipes-ui-keys.2026-09-29.md`
  (§1 layers · §2 map · §3 pipes · §6 keys · §8 D1–D5 · §9 majkee input · §10–10.1 layout · §11 reports · §12 D5).
- D1 events.jsonl yes · D2 `~/.local/state/ovitmugen/` (machine-local, never synced) ·
  D3 shared key grammar ACCEPTED, DRY: it lives ONLY in
  `/home/hruzam/unikuklatrix/nablarva/.dev/session/AGENTS.PROJECT-DESIGN.md` § KEYS CODE; helps point, never copy ·
  D4 tmux now, zellij possible behind the L0 adapter · D5 this sibling.
- Layout default: agents ~½ (or one clean terminal) + organs ~½ (runbook…, swappable);
  horizontal agents left / organs right; vertical organs up / agents down; user swaps live by
  key and saves / deletes presets in the console.
- Code lives in `/home/hruzam/ia-sync/zsh/session/` (ovitmugen.{py,zsh,tmux.conf,presets.json},
  runbook.py T bridge, help/ovitmugen/HELP.md ≤ 40 columns). Live only via majkee's `bash deploy.sh`.
- UI backlog + friction log: `.../ovitmugen-00-console/raw/ui-operability.2026-09-29.md`.

## Engineering laws (each one cost a bug)

- Views only: never send-keys / paste-buffer into a pane (nablarva L4). Never close a ● tab.
- Every tmux call names its server (`-L default` / `-L ovitmugen`); runbook runs inside the frame.
- After creation address by id (`@N %N`); no `=` on pane targets (3.7c: "can't find pane").
- Pane commands run through zsh: single-quote any `=word` (equals expansion kills it).
- Frame runbook always gets `--root <bed>/.dev/session`; `$RB_ROOT` beats the cwd otherwise.
- Handing the terminal to tmux: keep a real tty fd; tmux refuses the `/dev/tty` alias.
- Tests only on isolated sockets (`-L ovt<pid>-…`, agents conf `/dev/null`), unlink the socket
  files after; `list-keys -T prefix <key>` prints nothing on 3.7c — grep the full table.
- Display counts `fg` (program not a shell); kill-safety uses `busy` (fg OR shell children).

## prompt-0 — trajectory (fresh cSharp head, persistent)

```text
You are Trajectory, cSharp head of /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/.
Read RUNBOOK.md and STATUS.md there, then /home/hruzam/reposoma/raw.guides/runbook/res/csharp-head-protocol.md,
then the design file named in Fixed facts (§8–§12 first) and § KEYS CODE in
/home/hruzam/unikuklatrix/nablarva/.dev/session/AGENTS.PROJECT-DESIGN.md.
Build in order B1 → B2 → B3 → layout (see STATUS next). Before each step: one notice of the exact
files you will write. After each step: python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py selftest
and runbook.py selftest green, then commit only your own paths and update STATUS.
Push only with an explicit refspec up to your own commit (other writers stack commits here).
Never deploy. Spawn @Delta only for zero-judgment pieces; review its diff before reporting.
```

## prompt-1 — delta (spawned by trajectory only)

```text
Execute exactly the task and file scope trajectory names. Report the diff and the command
output that proves it. No opinions, no scope growth.
```

## Known constraints + destructive holds

- **Do not change today's `ov-ls --json` shape** (list of beds with `tabs[].busy/fg/left`): it is
  the consumer contract cited by nablarva-00 (Oraculum build description) and
  nablarva-03-app-architecture (Cartan blueprint). The v1 map comes BESIDE it (new flag/verb).
- nablarva-03-app-architecture's gate covers "code/config/data/runtime homes": D2's state dir
  is input to that blueprint — send it there (via majkee) before B1 writes the state dir.
- ia-sync `journal.host-cleanup.md` is another writer's: propose, never edit.
- `AGENTS.PROJECT-DESIGN.md` is maintained by the convergence seat (Cartan): append-only, never
  rewrite other chapters; commit only when no other writer's edits are pending in it.
- No deploy, ever, by this session. Never bare `rb-unmark`; detach by exact id.

## Acceptance evidence

- ov-selftest + rb-selftest output from office and home (home run by majkee).
- Majkee's live walk of the gate sequence and his recorded GO or STOP.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/` — predecessor bed (RUNBOOK, STATUS, raw/).
- `/home/hruzam/ia-sync/zsh/guides/claviature.global.spec.md` — shell keys: derive, don't register.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-03-app-architecture/RUNBOOK.md` — live blueprint gate.

## What this session deliberately does not do

- U5 mosaic (B4), U6 badges `!`, U7 scrolling policy (Cartan feedback), U8 idle-frame tick,
  remote attach from home (`ov-up --host`), Alt-key bindings, t41 convergence, termbrana work.
