---
kind: note of the lead — which session sits in the lead's seat since the fork, and where the fork's files came from
by: lead (flight) — claude b155ba44-0c27-4b9c-85e1-8f74daad22d6 · 2026-11-23, 18:50 UTC · home
---

# The seat

- **The lead is session `b155ba44…`** — a fork of `cc738596…` that Majkee made at about 14:29 UTC on 2026-11-23. It is
  shown in window `lead`, pane `%70`; reply bells pasted there reach it. The original (continued as `d406a745…`) is idle
  in the background and does not act.
- The fork runs as a background worker of the Claude daemon. The harness refused it every write into the shared checkout
  until Majkee set `worktree.bgIsolation = none` in `.claude/settings.json` (commit `6f5af9e`) and resumed the session.
  From 14:29 to 18:50 UTC it therefore wrote nothing here.

# What the fork did in that time — folded in with this note

Its files were kept in `~/.cache/nablarva/relay-x1-fork/` and are copied into this bed unchanged, under their own
names so nothing is renumbered:

- `raw/decision.majkee.scheduler-doorbell.2026-11-23.md` — his word of the afternoon, verbatim, and what was set up.
- `_bus/f01.*`, `_bus/f01r1.*` — the controller builds `CACHE.lead.md` from the lead's transcripts; one revision.
- `_bus/f02.*` — the 17:45 status round: auditor and controller.
- `raw/pokes.fork.log.md` — pokes `fp01`, `fp01r1`, `fp02`, `fp03`, the scheduler job and the doorbell's rings.

# One error in those files, left as written

The fork's POINTs say "no bell into %70 — it would wake the other lead session", and its decision file says the fork has
no pane. Both are wrong: the fork read its shell's missing pane variable as "no pane". The file-only replies it asked
for worked, so nothing was lost. From here on seats bell `%70` as before.
