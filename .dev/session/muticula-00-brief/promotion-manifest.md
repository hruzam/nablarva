---
session: muticula-00-brief
author: "trajectory-dashboard · Claude · office (cSharp head, status_owner)"
date: "2026-09-27"
gate_result: "GO — majkee, 2026-09-27, on brief r3 (sha256 eca377815bb1…) after the witness's PROCEED"
preservation: "the commit that adds this file on nablarva core — git -C /home/hruzam/unikuklatrix/nablarva log --diff-filter=A --format=%H -1 -- .dev/session/muticula-00-brief/promotion-manifest.md"
---

# Promotion manifest and cleanup record — muticula-00-brief

Every file in this bed is a keeper. All of them are preserved by the commit that adds this
manifest, and the next commit prunes the directory (GUIDE, "On gate closure"). The table lists
15 keepers plus this manifest.

## Keepers

| path | sha256 (12) | bytes | role | where it goes |
|---|---|---|---|---|
| `RUNBOOK.md` | `7188bcab7307` | 6045 | session RUNBOOK | stays in this commit |
| `STATUS.md` | `e1f0001761d5` | 2043 | final STATUS — gate met | stays in this commit |
| `_bus/01.cartan-muticula.verdict.md` | `56fb31fb6978` | 8307 | witness verdict — PROCEED on r3 | stays in this commit |
| `_bus/01.trajectory-dashboard.point.md` | `22116af6a0ab` | 3788 | fold-check POINT to the witness | stays in this commit |
| `raw/gate-fixture.2026-09-26.md` | `2480f150c476` | 2261 | gate receipt, Trajectory-reported | stays; input to muticula-01's gate fixtures |
| `raw/muticula.master.2026-09-26.md` | `eca377815bb1` | 38177 | the brief, r3 — GO | design baseline: muticula-01 copies it from this commit |
| `raw/muticula.master.2026-09-26.reviewed-17a2641e.md` | `17a2641ec6f7` | 21325 | reviewed r1 — hash pin | stays in this commit |
| `raw/muticula.master.2026-09-26.reviewed-6db74151.md` | `6db7415110ae` | 36463 | reviewed r2 — hash pin | stays in this commit |
| `raw/muticula.master.2026-09-26.reviewed-7c41b520.md` | `7c41b520c245` | 17852 | reviewed r0 — hash pin | stays in this commit |
| `raw/relays/TRAJECTORY-CARTAN-addendum.muticula-identity-tokens.2026-09-26.md` | `7515a02e6764` | 7014 | Trajectory → Cartan relay, consumed | stays in this commit |
| `raw/relays/TRAJECTORY-CARTAN-challenge.muticula-master.2026-09-26.md` | `719e862b9793` | 6929 | Trajectory → Cartan relay, consumed | stays in this commit |
| `raw/relays/TRAJECTORY-CARTAN-challenge.muticula-scope.2026-09-26.md` | `e78dca08e9b1` | 5478 | Trajectory → Cartan relay, consumed | stays in this commit |
| `raw/relays/TRAJECTORY-CARTAN-point.muticula-r2-closure.2026-09-26.md` | `446b58d6fb72` | 7737 | Trajectory → Cartan relay, consumed | stays in this commit |
| `raw/relays/move-map.2026-09-27.json` | `b245228de17d` | 2151 | move map of the four relays | stays in this commit |
| `raw/trajectory.experience-transfer.2026-09-27.md` | `bba380bee680` | 2550 | cSharp experience transfer | stays; majkee carries it to the next head |

## Clean house — every action, 2026-09-26/27

| action | what | evidence |
|---|---|---|
| renamed | nablarva `.dev/session/toolbox-muticula-00-` → `muticula-00-brief` | untracked folder, plain `mv`; frozen records keep the old path; sha256 pins the content |
| kept | r0, r1 and r2, byte-identical, as `reviewed-<sha8>` copies | the witness re-verified all three hashes (verdict 01) |
| moved | 4 Trajectory relays, from the ia-sync meeting room `rellays-claude-codex/` to `raw/relays/` | `raw/relays/move-map.2026-09-27.json`: sha256 equal at both ends (done by Delta, verified by the head) |
| removed | duplicate r0 at nablarva `.dev/session/recovery/muticula-00-/`, and its empty folder | full sha256 equal to `reviewed-7c41b520` before removal; `recovery/` keeps its other file |
| closed — old bed | ia-sync `runbook-upgrade-02-app`: Cartan's uncommitted STATUS receipt committed as `c819b6e`; bed pruned and router row dropped in `143914c` | evidence at `9bb608b` (182 paths). The 35 ignored JSONL logs were archived host-local, and each original was re-hashed equal to its copy before deletion. The router row was removed hunk-precisely; a neighbouring uncommitted row stayed |
| closed — this bed | preserved by this manifest's commit, then pruned; its router row removed from nablarva `pulse.md` before commit | this manifest; STATUS `recovery_probe` |

## Locators after prune

- **This bed:** `git -C ~/unikuklatrix/nablarva show <preserving commit>:.dev/session/muticula-00-brief/<path>`
- **Old-bed paths the brief and RUNBOOK cite:** `git -C ~/ia-sync show 9bb608b:.dev/session/runbook-upgrade-02-app/<path>`. The old bed's final STATUS is at `c819b6e`.
- **B0 JSONL logs:** `~/.local/state/muticula-evidence/runbook-upgrade-02-app/2026-09-27/` (office only, no second-host copy).
