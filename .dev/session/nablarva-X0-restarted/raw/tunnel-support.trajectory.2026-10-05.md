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

## T3 · 2026-10-06 · exit 13 from a second terminal — operator wiring, not a defect

- **Reported (majkee, relayed):** `tun ask` works in the terminal where `tn-on` ran; a
  second terminal gets `refused — no state path given … (exit 13)`. Nothing was sent.
- **Cause:** `TUNNEL_CODEX_STATE` is a per-shell env var; `tn-on`/`tn-use` export it only in
  the shell that ran them. The shim never infers the vault from `$PWD` (by design, no
  default — exit 13 creates nothing). Reproduced 12:41 from inside the bed folder with the
  var unset → exit 13. **Running from the bed folder does NOT fix it.**
- **Fix per new terminal (one of):**
  `tn-use /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted` ·
  `cd …/nablarva-X0-restarted && tn-use .` · or `tun ask --state <vault path> "…"`.
  Agent Bash calls: `export TUNNEL_CODEX_STATE=<vault path>;` in every call.
- **Live check 12:41:15 → 12:41:24 (+02:00):** `tun ask` with explicit export → exit 0,
  reply `pong — cartan(coordinator)`, `ctx=77724/258400 (30.1%)`. Line healthy on 0.160.0
  (this also serves as the L8 live-turn proof). Pre-check: no `.lock`, no TUI holding the
  rollout of `01a0f5a6…`.
- Repair candidate (transport owner): exit-13 message could add "per-shell — run
  `tn-use <bed>` in this terminal".

## T4 · 2026-10-06 · approvalPolicy still on-request after bring-up

`state.runtime` stamped 10:33:09Z: `approvalPolicy: on-request`, `workspaceWrite`, network
off, `writableRoots: []`. Either the TUI change (T1 workaround a) was not made, or it does
not survive into app-server `thread/resume`. Escalations behind the tunnel are therefore
still auto-declined silently (T1). Open until majkee says which.

## T5 · 2026-10-06 · answer to oraculum(cSharp) note (raw/note.oraculum-to-trajectory.2026-10-06.md)

### 1 · carrier trace shape (turns 10-11 · 12 · 13) — sound, three adjustments

Read `raw/tunnel-turns/*` at ~16:10. All three: exit 0, `.err` empty (no writer-lock NOTE →
no TUI residue), usage line present, no `.lock` left → lock released. Turn 12 = atlas via
yielded slot, recorded in `.meta`. Keep the pattern. Adjust:

- **Timeout is a kill, not a give-up — correction to my earlier advice.** On timeout the shim
  raises (`tunnel-codex.py:483`) and its `finally` closes the app-server (`:844-845`), which
  **interrupts the server turn** (guide §Long turns). Durations: 10-11 = 269 s, 12 = 36 s,
  13 = **362 s = 60 % of 600**. A heavier round will hit the wall and lose the turn. Use
  `TUNNEL_CODEX_TIMEOUT=1800` for design turns (still backgrounded); 600 only for short acks.
  After exit 30: `read` → expect `interrupted` → one-line nudge, same cycle.
- **Context is climbing fast:** 43.1 % → 44.7 % → 59.6 % (turn 13 alone +38.6k). ~80 % is the
  reset trigger (user-run §Clearing) — roughly two more rounds of this size. Tell majkee before
  it is reached; a reset = new thread, Cartan rebriefed from files.
- **`.meta` — add the turn id** for correlation with `read`: after the ask,
  `jq -r .lastTurnId "$TUNNEL_CODEX_STATE" >> <meta>` (on exit 0 only; on failure it still
  holds the previous id — record that fact, not the value).

### 2 · effective runtime policy — as of now, unchanged

`state.runtime` observedAt **2026-10-06T13:59:38Z**: `approvalPolicy: on-request` ·
`sandbox: workspaceWrite, networkAccess: false, writableRoots: []` · cwd
`/home/hruzam/unikuklatrix/nablarva` · `gpt-6-astra` / `xhigh` · instructions
`~/.codex/AGENTS.md` + `nablarva/AGENTS.md`. No change has been made; STATUS `holds:` can
carry exactly this line.

**Technical note on Atlas's §C8 (mechanism only, no design position):**
- `writable_roots` **adds** writable paths outside the workspace root; it never narrows. The
  bed and `_provisional/` are already inside the root (`nablarva/`) and already writable —
  proven: Cartan wrote `_bus/10.cartan.return.md` and `_bus/13.cartan.return.md`. So
  writable_roots = bed + `_provisional/` changes **nothing**.
- `approvalPolicy` is **thread-wide**, not per path. "never inside it" cannot be expressed.
  `never` = every escalation (network, outside-root write, protected path) is refused back to
  the model instead of asked — the same outcome as today's silent decline, but by policy and
  visible to the model as a refusal.
- To *restrict* Cartan to the bed, no sandbox knob exists; that stays an instruction-contract
  rule (POINT "permitted writes").
- Any change can only be made from the TUI owning the thread (the shim sends no policy on
  resume). Then: TUI `/exit` → carrier `tun resume` → I read `jq .runtime` and append it here.
  Whether a TUI change survives into app-server resume is still unverified (T4).

### 3 · exit-13 wording

Agreed as a candidate. The shim's source is `~/ia-sync/zsh/ai/tunnel-codex.zsh` (surgical
table; deploy via ia-sync) — outside this bed, so it waits for majkee's word. Not done.

### 4 · U3 fixture — noted. No action until majkee rules U1 and oraculum's RUNBOOK exists.
