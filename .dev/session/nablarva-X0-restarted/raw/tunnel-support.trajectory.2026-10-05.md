# tunnel support — nablarva-X0-restarted · trajectory(support) · append-only

`2026-10-05 · office hruzam-120922 · codex-cli 0.160.0 · shim ia-sync/zsh/ai/tunnel-codex.{zsh,py} (live copy identical, selftest 96/96)`
`writer: trajectory (blessed by majkee 2026-10-05) · sibling of tunnel-issues.2026-10-05.md (carrier's log, not touched here)`
`contact: majkee relays problems to me, or I am reached as trajectory(support) (RUNBOOK call sign: trajectory(it))`

## T1 · approval requests behind the tunnel are silently declined — no alert exists

- **Observed (source, not a live run):** the shim answers every server→client request
  (approval prompts) with a JSON-RPC error — `_auto_decline`, `tunnel-codex.py:414`, called
  from `_await_response` (:409) and `drive_turn` (:487). The turn does not hang; the escalated
  command simply fails. No stderr line, no state counter, no exit code reflects it. Operator
  and carrier see it only if the Codex seat mentions it in its reply.
- **Bound thread `01a0f5a6-42f9-76e3-938e-c7d798a9dcc5`** (rollout 2026-10-01, last
  turn_context): `approval_policy: on-request` · `workspace-write`, network off ·
  `gpt-6-astra` / `xhigh`. In-sandbox commands run unasked; escalations (network, writes
  outside nablarva, likely `.git`) request approval → auto-declined behind the tunnel.
- **Open question (verify at first `tun resume`):** does a policy changed in the TUI
  (`/permissions`) persist into the app-server `thread/resume`? The shim sends only
  `threadId` on resume and `threadId+input` on turn/start. Check:
  `jq .runtime.approvalPolicy "$TUNNEL_CODEX_STATE"`.
- **Workarounds today, safest first:** (a) TUI: approvals → never / auto-review, keep
  workspace-write, before release · (b) `~/.codex/config.toml` `approvals_reviewer =
  "auto_review"` or `approval_policy = "never"` — GLOBAL to all Codex sessions on the host,
  deliberate and reverted after · (c) shim change, see below.

### For the next version — transport (ia-sync, surgical table; not built here)

1. Never decline silently: each declined request → one stderr line (method + command summary)
   and a counter/list in the state file (`declinedApprovals`), so `tn-st` shows it.
2. Optional open-time knob: `tun open --approval-policy … --approvals-reviewer …`, sent on
   `thread/resume` / `turn/start` (both params exist in the 0.160.0 schema:
   `ThreadResumeParams`, `TurnStartParams`). Open-time only, per Law 2.4 — same reasoning that
   kept the sandbox override out of `send`.
3. Alternative native alert: Codex 0.160.0 carries a `PermissionRequest` hook event — a
   hook could notify the operator without shim changes. Unverified; needs a probe.

### For the next version — protocol (coordination discipline)

An **approval slot**: when a tunnel turn hits a declined escalation, the carrier logs it in
`tunnel-issues…`, asks majkee, and carries the decision back as the next turn of the same
cycle. Until the transport reports declines (above), the carrier should ask the Codex seat
to name any refused command in its RETURN.

## T2 · small holds noticed at bring-up

- `.gitignore` `**/tunnel*.state.json` covers the vault but not `tunnel.state.json.lock` /
  `.tmp`. Both are transient (released / replaced), but a killed driver leaves a stale
  `.lock`. Suggest `**/tunnel*.state.json*`. Low priority.
- `tn-use <slug>` resolves under `$RB_ROOT` = `~/ia-sync/.dev/session`; nablarva beds need
  an absolute path.
- Known source findings (Cartan, confirmed by reading): lock only on send/ask/steer —
  `close` deletes `.lock` even mid-turn; O_EXCL-create-then-write-pid leaves a window where
  a second caller reads pid 0 and treats the lock as stale; `lastTurnId` advances only on
  success, so `steer` after a timeout targets the previous turn. Mitigation = carrier's
  strict turn order; repairs belong to the transport owner.
