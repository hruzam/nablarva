---
kind: answer to two operator questions
question_source: Majkee's section "Can we have some vendor neutral" in decision.majkee.open-bed.2026-11-21.md
by: engineer · host home · checked 2026-11-21T21:00Z
---

# 1. A vendor-neutral "friendly reminder" with a timer

**Yes, and most of it is standard.** The pattern is a deadline, a watchdog, at most one harmless repeat, then a human is told.
The goal is drafted as `../goals/G10.friendly-reminder.md`, with the edge cases listed there.

- **Seeing who is silent** needs no script: tmux `monitor-silence <seconds>` flags a window that printed nothing for that long.
  It is off on home today (`monitor-silence 0`). Setting it is your hand.
- **Telling the one who waits** is a small finite script: a RETURN path, a deadline, a completeness check, one message to the
  waiting owner. I do this by hand today with a background wait.
- **Reminding the silent seat** is a second send. That is delivery (L21) and an exception to "poke once", so it needs your release.
- vistMini already had the idea: `vist-heartbeat.py`, one bounded wake under a lease with an expiry, a maximum number of wakes
  and a pending id, started only by an external timer. It is archived evidence. Its guards are the ones to copy; its code is tied
  to the trial's own resolver and should not be revived.

# 2. What is left from vistMini

**Nothing from vistMini is installed or running on home.** What remains is native doors, shared practice, an archive and some residue.

| What | State today | Where |
|---|---|---|
| `codex queue --thread` (Claude → Codex) | native CLI feature, in use by this bed | codex-cli 0.171.0 |
| Look-first tmux paste (into a Claude pane) | plain tmux, in use by this bed | — |
| Codex thread messaging, Claude `SendMessage` | native, not used here | — |
| POINT / RETURN / VERDICT | shared guide, in use | `~/reposoma/raw.guides/bus/GUIDE.md` |
| file-poke rhythm | shared, provisional, in use; retirement debt is G7 | `~/reposoma/raw.guides/bus/res/file-poke.md` |
| Fallback poke "like sudo" | your decision of 2026-11-14, in force | origin bed `raw/decision.majkee.fallback-poke.2026-11-14.md` |
| Lessons: four layers of "delivered", the scars | carried in the export §4 and §8 | `export.vist-x0.engineer.2026-11-21.md` |
| `bus-poke.sh` + `vist-signatures.conf` (keystroke adapter and its screen signatures) | archived, not deployed | `~/ia-sync/.dev/records/vist/2026-11-14/vistMini-01-tests/scripts/` |
| `vist-deliver.sh` (delivery wrapper) | archived, not deployed | same |
| `handoff-once.sh` (one bounded hand-off after a controller turn) | archived, not deployed | same |
| `vist-heartbeat.py` (bounded wake under a lease) | archived, not deployed | same |
| C04 inputs | still present, memory-backed, host up since 2026-09-29 | `/tmp/vc08r1.tkz50zbf`, `/tmp/vc08r2.kk50sqqh` |
| Old tmux sessions `vist`, `view-*`, `traj-home*`, `helper-utils-00-tmux*` | still open; every pane is a plain shell | tmux on home |

How I checked "not deployed": no file mentioning `vist` in the deploy sources `~/ia-sync/{zsh,claude,codex,germline}` nor in the
live targets `~/.config/zsh`, `~/.claude/hooks`, `~/.claude/settings.json`, `~/.codex/config.toml`, `~/.local/bin`; no user
systemd timer or unit named `vist`.

**Not checked:** office and monitor. The export mentions a home state file for the never-retry ids `t03` and `c08r1-05-ae3ee8e7`;
I did not look for it again today. Those two ids stay untouched either way.

**No door is qualified on today's versions.** That is what G3 and G8 are for.
