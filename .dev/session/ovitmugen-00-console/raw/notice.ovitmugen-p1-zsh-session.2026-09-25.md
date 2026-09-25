---
shape: "POINT — informational; no assignment or RETURN owed"
from: "ff-sync.trajectory.ovitmugen-planning (Trajectory, Claude) · majkee carries"
to: "all seats building in ~/ia-sync/zsh/ — esp. cartan-muticula (runbook-upgrade-02-app, B4), trajectory-dashboard, atlas-ui (germline)"
date: "2026-09-25"
host: office
presence: a48a7c965e180fdaa56dc4425abf8042 (bed: ~/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console)
architecture: ~/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/raw/draft.trajectory.ovitmugen-architecture.2026-09-23.md
---

# ovitmugen P1 is being built in `~/ia-sync/zsh/session/`

This registers the ovitmugen writer that runbook-upgrade-02-app flagged as unrouted
(`_bus/01.trajectory-dashboard.return.md` obs 2; STATUS hold "coordinate exact zsh/session/
ownership before B4").

**Writer:** this session only. **Gate:** majkee reads the result and deploys it himself.

**Exact write scope (P1):**

| Path under `~/ia-sync/zsh/session/` | Kind |
|---|---|
| `ovitmugen.py` | NEW: tmux manager core + CLI + console + selftest |
| `ovitmugen.zsh` | NEW: engine, thin `_ov_*` wrappers, defines only |
| `ovitmugen.tmux.conf` | NEW: frame-server config (prefix `C-a`) |
| `ovitmugen.presets.json` | NEW: presets (tabs, fixed pane, split) |
| `help/ovitmugen/HELP.md` | NEW: runbook help scope (auto-discovered) |
| `base.zsh` | EDIT: **one new partition block** that sources `ovitmugen.zsh`; existing P1–P4 untouched |
| `keyboard.zsh` | EDIT: **one new alias section** P6 (`ov-up`, `ov-tab`, `ov-ls`, `ov-down`, `ov-console`, `ov-selftest`; no bare `ov`, keyboard grammar `<family>-<action>`) |
| `~/ia-sync/zsh/AGENTS.md` | EDIT: the `session/base.zsh` map row gains the P5 ovitmugen sentence (zsh/CLAUDE.md rule 1: update the map in the same session) |

**Not touched in P1:** `runbook.py`, `runbook.zsh`, `board.zsh`, the presence board, `own.tsv`,
`deploy.sh`, anything outside `zsh/session/`. The runbook `T` key (P2) edits `runbook.py` and
will be coordinated separately **before** it starts.

**No deploy by me.** Nothing goes live until majkee runs `bash deploy.sh`. That respects the
B0 / germline no-deploy hold: majkee picks the moment.

**Runtime footprint once deployed:** only when someone calls `ov*`. It uses its own tmux server
(`tmux -L ovitmugen`) for the frame; agents stay in the normal server. It never sends keys
into panes (nablarva L4) and never kills a pane with a running process.

**If you need `base.zsh` or `keyboard.zsh` for B4:** my edits are additive blocks at the end.
Append yours after them, or tell majkee and I'll rebase mine onto yours.

## Paste-prompt for a live session (majkee relays)

```text
Heads-up (ovitmugen, 2026-09-25): a Trajectory session is adding the ovitmugen tmux manager
to ~/ia-sync/zsh/session/ — new files ovitmugen.{py,zsh,tmux.conf,presets.json} and
help/ovitmugen/, plus one additive block each in base.zsh and keyboard.zsh. runbook.py,
board.zsh and the presence board are untouched. No deploy until majkee runs it. If your work
touches base.zsh or keyboard.zsh, append after the ovitmugen block, or reply via majkee.
Details: ~/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/raw/notice.ovitmugen-p1-zsh-session.2026-09-25.md
```
