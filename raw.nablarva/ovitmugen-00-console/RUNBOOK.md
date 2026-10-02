# RUNBOOK: ovitmugen-00-console

```yaml
goal: >-
  ovitmugen v1 is live on both hosts: one terminal shows agents switchable like tabs on the
  left and runbook fixed on the right, rebuildable from a JSON preset, driven from runbook
  and from a console popup, never owning agent lifetime.
gate: >-
  Majkee records GO or STOP after walking ovitmugen v1 live on office: frame built from a
  preset, left tab switched from the runbook T modal and from the C-a t popup, split moved,
  and ov-down --idle keeping a tab with a running agent, with ov-selftest and runbook
  selftest green on office and home.
participant_0: [trajectory, {brand: anthropic, model: operator-selected, effort: operator-selected}, {host: office, role: cSharp head, sole writer of source in scope, status_owner}]
participant_1: [delta, {brand: anthropic, model: agent-default, effort: agent-default}, {host: office, role: surgical subtasks spawned by trajectory only, reviewed before report}]
participant_2: [majkee, {brand: human, model: none, effort: none}, {host: office + home, role: deploy hands, live walk, gavel}]
status_owner: trajectory
head_note: >-
  cSharp (res/csharp-head-protocol.md): this seat authored the RUNBOOK and stays through the
  arc; it builds, spawns Delta for zero-judgment pieces, and never self-confirms the gate.
schema_note: >-
  runbook/GUIDE.md (Manifest read 2026-09-25) · status/GUIDE.md fixed fields · no _bus:
  one writer plus in-window spawns. Session name ff-sync.trajectory.cSharp-oStar-ovitmugen.
```

## Why this session exists

tmux twins and hand-built beds cost the operator every session. ovitmugen turns the
hand recipe into a brick of the session layer. P1 (core, frame, presets, console, help)
is built and self-tested in the ia-sync deploy layer; P2 (runbook `T` modal + overview
line) remains, then the live walk on both hosts.

## Fixed facts

- Design: `raw/draft.trajectory.ovitmugen-architecture.2026-09-23.md` (layout C, §5.7 console hosting, §9 answers).
- Placement (majkee 2026-09-23): docs in this bed; code in `/home/hruzam/ia-sync/zsh/session/`; live only via `bash deploy.sh`, run by majkee.
- Decided: split 60/40 (`C-a <`/`>`), tabs = empty shells, frame prefix `C-a`, aliases `ov-*` (no bare `ov`: keyboard grammar `<family>-<action>`).
- Write scope + coordination notice: `raw/notice.ovitmugen-p1-zsh-session.2026-09-25.md`.

## prompt-0 — trajectory (cSharp head, persistent)

```text
You are Trajectory, cSharp head of /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/.
Read RUNBOOK.md and STATUS.md there, then /home/hruzam/reposoma/raw.guides/runbook/res/csharp-head-protocol.md.
Build only inside the write scope of raw/notice.ovitmugen-p1-zsh-session.2026-09-25.md; P2 touches
/home/hruzam/ia-sync/zsh/session/runbook.py and needs majkee's coordination word first (muticula B4).
Verify with: python3 /home/hruzam/ia-sync/zsh/session/ovitmugen.py selftest and runbook.py selftest.
Spawn @Delta only for zero-judgment pieces; review its diff before reporting. Keep STATUS current.
Commit only own paths; no push while another writer's local commit is ahead; never deploy.
```

## prompt-1 — delta (spawned by trajectory only)

```text
Execute exactly the task and file scope trajectory names. Report the diff and the command
output that proves it. No opinions, no scope growth.
```

## Known constraints + destructive holds

- Never `send-keys`/`paste-buffer` into agent panes (nablarva L4); never kill a busy pane.
- Tests only on isolated tmux sockets; the real `default` server is read-only to tests.
- ia-sync journal (`journal.host-cleanup.md`) belongs to other writers: propose, never edit.
- `raw/brief.ovitmugen-sentinel.2026-09-04.md` (@kukla) is not ours; untouched until majkee rules.
- runbook-upgrade-02-app holds: no `deploy.sh` during its B0/germline; do not push its local commit.

## Acceptance evidence

- ov-selftest + runbook selftest PASS output on office and home (majkee runs home).
- Majkee's live walk of the gate sequence, and his recorded GO or STOP.

## References

- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `status/GUIDE.md`
- `/home/hruzam/ia-sync/zsh/session/help/ovitmugen/HELP.md` — user surface
- `/home/hruzam/ia-sync/.dev/session/runbook-upgrade-02-app/STATUS.md` — neighbour holds

## What this session deliberately does not do

- t41 convergence (P3), termbrana consumer (P4), phone view, cross-host frame.
- Registering `ov-` in `ai/keys.zsh` / `guides/keyboard.md`, a temple guide, muticula work.
