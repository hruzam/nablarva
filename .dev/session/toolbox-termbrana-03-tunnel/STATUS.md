```yaml
updated: 2026-09-02 13:20 CEST
writer: Trajectory (Claude · Sonnet 5 · office)
host: office (hruzam-120922) — verified: `ls /usr/bin/php74 && command -v valet` both present
worktree: /home/hruzam/unikuklatrix/nablarva · branch core · HEAD 1fbc539 ("03-tunnel
  opened: STATUS + router; t1 folded") · clean · pushed to origin/core
gate: One full round-trip (Claude→Codex task, Codex→Claude result) through the v0
  tunnel, live on office, receipts on disk in this session folder.
checkpoint: v0 shim built + fixture selftest 30/30 green + zsh -n / py_compile clean.
  ia-sync main @ 24d39d7dd5d788bfe34398b22064d2363f025282 ("termbrana tunnel v0 shim:
  app-server stored-thread supervisor per Cartan verdict; fixture selftest green; NOT
  deployed — behavior proof (t3) before promotion") — pushed. nablarva core @ 1fbc539
  ("03-tunnel opened: STATUS + router; t1 folded") — pushed. t1 mechanics verdict is
  folded into the ia-sync build (Cartan RETURN, app-server live-proven on codex-cli
  0.152.1 — see meeting-room file
  session/rellays-calude-codex/CARTAN-ORACULUM-tunnel-verdict.2026-09-02.md in ia-sync).
  Files: ~/ia-sync/zsh/ai/tunnel-codex.zsh (operator entry, Law 2.4 gate, exit-code
  contract), tunnel-codex.py (JSON-RPC mechanics, stdlib-only, method/field names
  cross-checked against a local zero-quota `codex app-server generate-json-schema
  --experimental` run on codex-cli 0.152.1 — not docs prose), tunnel-codex.selftest.zsh
  (fixture-only, fake app-server, 30/30 green, no live Codex call, no quota spent).
in_flight: none — both commits above are pushed to their origins; nothing uncommitted
  in either worktree at the time of this snapshot.
recovery_probe: `git -C ~/ia-sync log --oneline -1` should show 24d39d7 (or a
  descendant) on main. `git -C ~/unikuklatrix/nablarva log --oneline -1` should show
  1fbc539 (or a descendant) on core. `zsh ~/ia-sync/zsh/ai/tunnel-codex.selftest.zsh`
  is read-only/fixture-only and safe to re-run at any time to re-confirm 30/30 green —
  it spends no Codex quota and touches no live state file
  (`$HOME/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-03-tunnel/tunnel.state.json`,
  which does not yet exist — the shim has never been live-enabled).
holds: no live Codex quota spent before t3 (selftest is fixture-only; majkee owns t3
  enable) · shim NOT deployed to ~/.config/zsh until t3 passes (behavior proof before
  promotion, Sella L8) · known v0 limit recorded in tunnel-codex.zsh's own header: each
  verb is a separate process (no daemon), so `steer` can only target a turn id this
  same shim already recorded in its own state file — it cannot inject into a turn
  concurrently streaming inside a still-running separate `send` in another terminal;
  true mid-stream steering from a second process needs a resident process (v1/daemon),
  not attempted here · nablarva is plain `git pull`/`push` only on `core` — NEVER
  `git pull --rebase` (subtree history, flag L12, near-miss 2026-09-02).
next: t3 live round-trip — majkee enables (`zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh open
  --enable`), Claude seat sends one scoped task via `send <text>`, receipts (transcripts
  + the exchange) land as new files in this session folder
  (.dev/session/toolbox-termbrana-03-tunnel/).
expected: observable round-trip receipts on disk in this folder — a Codex-side result
  returned through `send`/`steer`/`read` output, reconciled via
  thread/read(includeTurns=true), with the exit code contract (0 on success) holding on
  the real app-server, not just the fixture.
```
