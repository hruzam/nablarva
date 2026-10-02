---
what: experience transfer — ovitmugen-00-console cSharp head → next head (ovitmugen-01-basement)
date: 2026-10-02
from: trajectory (ff-sync.trajectory.cSharp-oStar-ovitmugen)
gate: closed GO — office walk 2026-09-29, selftests green on office + home 2026-10-02
---

# What this run learned (short, testable)

1. **Test where the operator lives, not where you build.** Every walk found a bug the isolated
   selftest could not: dead fixed pane on quit, frame runbook on the wrong root, home shells busy
   for >8 s. Run the selftest on HOME too (scp to a throwaway dir, isolated sockets) before
   asking majkee to walk.
2. **zsh runs every pane command.** `=word` is equals expansion — quote it. shlex.join does not.
3. **tmux refuses `/dev/tty` as a terminal name.** Keep a real tty fd when exec-ing attach.
4. **`$RB_ROOT` beats the cwd** in runbook's root order: pass `--root` explicitly, always.
5. **`=` works on session/window targets, fails on pane targets** (3.7c). Use ids for panes.
6. **"Idle" is a judgement over time, not a snapshot.** Prompt redraws and startup commands fork
   briefly; read several times and act right after an idle read. Display ≠ safety: `fg` for
   counting agents, `busy` (fg OR shell children) for refusing a close.
7. **Push with an explicit refspec to your own commit, always.** A plain `git push` once carried
   another session's commit (publish-gate 7075b61) that landed seconds after the check.
8. **Never commit a shared file with someone else's pending edits.** Append, leave it
   uncommitted, tell majkee (AGENTS.PROJECT-DESIGN.md § KEYS CODE went in via another writer).
9. **Check consumers before changing an output.** `ov-ls --json` became a contract for two other
   sessions without anyone announcing it — grep the beds before reshaping any output.
10. **One question per turn** worked for design decisions with majkee (D1–D5): record each answer
    in the design file the same turn.

Open and handed on: everything in ../../ovitmugen-01-basement/ (RUNBOOK fixed facts + holds).
