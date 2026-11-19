---
kind: witness continuity note (host move home → office)
from: witness (oraculum, Claude Fable, session c266d10a-ecda-4f89-9f18-f29b59e3130e, renamed `witness|spawn:houston`)
date: 2026-11-19
authority: majkee, typed in the witness session 2026-11-19: move the whole work to office; keep the briefed witness by carrying
  its exact session transcript (.jsonl) to the same place on office; alternative was a cold-start card.
status: note only; no sweep, no verdict
---

# Witness moves with its transcript

Choice: carry the transcript (majkee's first option). This note is the fallback if resume on office fails:
a fresh Oraculum reads it plus the files below and is briefed without the chat.

## What I am (decided, on disk)
- Outside `witness` for vist-X0: `raw/decision.majkee.witness.2026-11-14.md`, `raw/brief.witness.trajectory.2026-11-14.md`,
  my read-back `raw/readback.witness.2026-11-14.md`. Plan row "Outside witness": `raw/plan.runbook-and-team.cartan-trajectory.2026-11-14.md`.
- Job: at a gate or majkee's call, sweep the process checklist, write `raw/witness.<date>.md`. No pen on STATUS, RUNBOOK, verdicts, push;
  no dispatch, `/clear`, pane input. No sweep has been called or written yet.
- Carried cases U01–U06 are UNRUN/UNQUALIFIED (`raw/preregister.vistmini-carryover.cartan.2026-11-14.md`). Keys t03 and
  c08r1-05-ae3ee8e7 are kept, never retried.
- Fallback poke decision: `raw/decision.majkee.fallback-poke.2026-11-14.md`. Open: whether it applies to the witness (brief says no pane input;
  hook denies `send-keys`).

## Hook (ia-sync)
- `claude/hooks/oraculum-bash-whitelist.sh` has a read-only `tmux)` case: ia-sync 23f15e0, journal 6bccbca. Live on home only.
- Beyond the brief's proposal it also accepts `-L <name>` and short aliases, and denies arguments ending in `_`. Majkee was told; not yet ruled on.
- **Office needs `git pull` + deploy in ia-sync before the witness can read panes there.**

## Stale after the move (do not trust from the transcript)
- Every tmux window/pane id, seat session id and context % seen on home.
- Host facts: the transcript's work happened on home; resolve the host again on office (`machines.json`, tailscale node id).
- The ia-sync dirty paths seen on home (`claude/agents/trajectory.md`, `claude/settings.json`, `claude/hooks/statusline.sh`).

## Transcript handling
- Private, host-to-host only over the operator's own SSH. Never into Git (ia-sync is a public repo; the preregistration keeps raw histories out of packets).
- Copy, do not delete: the home original stays.
- The file keeps growing until this session stops; the last copy must be taken after the session is idle or closed.
