---
shape: "proposal — for the owner of /home/hruzam/ia-sync/journal.host-cleanup.md"
from: trajectory (ovitmugen-00-console)
date: 2026-09-25
status: NOT applied. The journal has another writer's uncommitted edits; this seat does not touch it.
---

Suggested entry (paste or rephrase at your discretion, newest-first per journal convention):

```markdown
## 2026-09-25 · office · ovitmugen P1 landed on the table (not deployed)

- New session-layer organ in `zsh/session/`: `ovitmugen.{py,zsh,tmux.conf,presets.json}` +
  `help/ovitmugen/`; `base.zsh` P5, `keyboard.zsh` P6 (`ov-up/tab/ls/down/console/selftest`).
  Commit `0b95adf` (ia-sync, local; not pushed while `b2b7901` awaits its own authorization).
- Runtime footprint only when `ov-*` is called: a second tmux server `tmux -L ovitmugen` for the
  frame; agents stay on the default server. Never send-keys; never closes a busy pane.
- Goes live with the next `bash deploy.sh` on each host (majkee), after runbook-upgrade-02-app
  lifts its B0/germline no-deploy hold. Home: run `ov-selftest` after deploy.
- Bed + design: `~/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/`.
```
