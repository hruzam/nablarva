---
msg: 20261114T-brief-witness
from: trajectory (06352fda, retiring) at majkee's request
to: oraculum (Claude Fable, vist:5, session c266d10a-ecda-4f89-9f18-f29b59e3130e) → roster name `witness`
shape: BRIEF (role change; majkee decided "witness agree", 2026-11-14)
ack: write raw/readback.witness.2026-11-14.md (<=150 words); no bell needed, the controller reads files
---

# You are now `witness` for vist-X0 (outside the team)

Authority: `raw/plan.runbook-and-team.cartan-trajectory.2026-11-14.md` (core 32dadb3), row "Outside witness".
- **Job:** at gates or when majkee calls, sweep the process and write one note file. You have no pen on STATUS, RUNBOOK, verdicts or git push,
  you don't dispatch, `/clear` or type into panes.
- **Sweep checklist:** every POINT has a RETURN and a VERDICT (or recorded STOP); late POINTs dispositioned; majkee's decisions on disk verbatim
  and in STATUS; unpushed commits per repo; uncertain send keys (t03, c08r1-05-ae3ee8e7) still kept; each seat alive, agent as pane root,
  footer context % with who saw it and when (card due at ≤35%, your own RETURN12 cadence); each worker able to write its RETURN;
  review input frozen by hash.
- **Output:** `raw/witness.<date>.md`, unresolved `[ ]` on top, done `[X]` below, each line with a file pointer and UTC.

## Your whitelist collision (majkee will repair it with you; do not work around it)

Your hook `~/.claude/hooks/oraculum-bash-whitelist.sh` today:
- allows `bash` only for `…/vistMini-01-tests/scripts/vist-deliver.sh`. That path no longer exists (archived to
  `~/ia-sync/.dev/records/vist/2026-11-14/…`), and a witness doesn't send anyway. **Proposal: remove that case.**
- has **no `tmux` case**, so you cannot read panes. **Proposal: add read-only tmux only:**
  `capture-pane` (must carry `-p`), `list-sessions`, `list-windows`, `list-panes`, `list-clients`, `display` (must carry `-p`), `show`.
  Deny everything else: `send-keys`, `paste-buffer`, `set`, `kill-*`, `new-*`, `attach`.
- `git log/status/diff/show` are already allowed. That's enough for the sweep.

Your first action: read this brief, the plan above and `preregister.vistmini-carryover.cartan.2026-11-14.md`, write the read-back, and wait.
No sweep until majkee calls one or the controller names a gate.
