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

## T6 · 2026-10-07 · exit-13 message reworded (majkee "yes") — source only, NOT deployed

- File: `~/ia-sync/zsh/ai/tunnel-codex.zsh` (STATE PATH block), +1 stderr line after the
  unchanged refusal line:
  `tunnel-codex: the vault address is per shell — the folder you run from does not matter; in THIS terminal run 'tn-use <bed>' (absolute path outside $RB_ROOT), or prefix every agent Bash call with 'export TUNNEL_CODEX_STATE=<vault path>;'`
- Exit code, stdout purity, creates-nothing behaviour unchanged. Selftest on the source copy
  96/96 (the asserts on `--state` / `TUNNEL_CODEX_STATE` still hold — original line kept).
- **Live `~/.config/zsh/ai/` copy is still the old text** until an ia-sync dry-run deploy +
  deploy (ia-sync AGENTS.md §SYNC). Not committed. Both wait for majkee.

## T7 · 2026-10-07 · context reset at 81 % (turn 15: ctx=209287/258400)

Pre-state: no `.lock`, no TUI on `01a0f5a6…`, lastTurnId `01a111c7-bb01-75e2-b744-623f7d547af5`.

- **`/compact` keeps the thread id** → vault stays valid, no rebind. Summary loses detail; Codex
  itself warns repeated compactions degrade accuracy.
- **`/clear` (or `/new`) starts a NEW thread id** → the vault still points at the old 81 % thread.
  Must rebind (`tn-off` → `tn-on … --thread <new id>`) and rebrief from files. Check in the TUI
  with `/status` (shows the session id) before and after.
- The new thread takes the TUI's current approval/sandbox settings at birth — a chance to fix
  T1/T4 at the same time. After rebind, carrier `tun resume` and `jq .runtime` → append here.

### T6 · closed 2026-10-07 02:4x — committed, pushed, deployed (majkee "yes")

ia-sync `ffee9f6` on main (pushed `d7e4751..ffee9f6`; fast-forwarded over d7e4751 first, no
overlap). Only `zsh/ai/tunnel-codex.zsh` staged — foreign dirty files (`claude/agents/oraculum.md`,
`pulse.md`) left untouched. Dry-run showed the deploy would change only this file (+ its pycache).
After deploy: live `~/.config/zsh/ai/tunnel-codex.zsh` == source; live exit-13 prints the new
hint; live selftest 96/96.

## T8 · 2026-10-07 ~02:56 · rebind after `/clear` → `resume` exit 30 "no rollout found"

- **Error 1 — `zsh: no such file or directory`:** my T7 recipe wrote `--thread <NEW_ID>`; the
  operator pasted the id inside the brackets and zsh read `<…>` as an input redirect. Nothing
  ran. Cause = my placeholder in a paste-ready block. Rule for my recipes: no `<…>` in
  copy-paste lines; use `NEW_ID` plus an explicit "replace" note.
- **Error 2 — `-32600 no rollout found for thread id 01a113d8-c5b0-7343-a927-cb960dd641f7`:**
  `/clear` allocated a new id but the TUI was exited before any turn, so Codex never wrote a
  rollout (same fact as the shim's THREAD BIRTH note, 0.152.1 t3: a zero-turn thread has no
  rollout). Verified: no `rollout-*01a113d8*` file, no writer-lock for it, no TUI process on
  nablarva. The id is unusable from anywhere; the vault is bound to a dead address.
- Side observation: `rollout-…01a113d3-8bb0…` (02:46, cwd nablarva, `source: subagent guardian`,
  3 lines, 0 turns) — a Guardian auto-review subagent thread from the TUI. Suggests approvals
  were routed to auto-review in the TUI — relevant to T1/T4, verify on the next `resume`.
- Old thread `01a0f5a6…` untouched server-side (re-bind line printed by `tn-off`).
- Repair: give the new thread one real turn before binding (TUI route), or let the tunnel
  birth a fresh thread. See chat 2026-10-07 for both recipes.

## T9 · 2026-10-07 ~03:10 · new head bound — effective runtime policy (for STATUS `holds:`)

Thread **`01a113e0-b774-7e32-926a-bc19f050ab2c`** (TUI-born 03:00:56, rebrief as first turn,
3 turns, rollout 1.5 MB). `tun resume` exit 0, status idle. `state.runtime`:

- model **`gpt-6-sol`** · reasoningEffort **`medium`** (previous head: `gpt-6-astra` / `xhigh`;
  vault intent at open said `gpt-6.1-sol` — intent only, runtime wins)
- sandbox `workspaceWrite`, networkAccess false, writableRoots `[]` · cwd `/home/hruzam/unikuklatrix/nablarva`
- approvalPolicy **`on-request`**; rollout turn_context `approvals_reviewer: "user"` (the shim
  does not stamp the reviewer — read from the rollout) → **auto-review is NOT active on this
  head; T1 silent-decline still applies.** The 02:46 Guardian thread (T8) did not carry over.
- instructions `~/.codex/AGENTS.md` + `nablarva/AGENTS.md`
- `tunnel-using-protocole.md` §Fixed values updated (thread + policy rows).

STATUS line for the carrier, verbatim:
`tunnel head 01a113e0-b774-7e32-926a-bc19f050ab2c · gpt-6-sol/medium · workspaceWrite, net off, writableRoots [] · approvals on-request, reviewer user (escalations silently declined behind tunnel) · runtime observed 2026-10-07 ~03:10 · prior head 01a0f5a6… retired from tunnel at 81 % ctx`

Shim gap for the transport owner: `_stamp_runtime` keys omit `approvalsReviewer` — add it so
`tn-st` shows the reviewer without reading the rollout.

## T10 · 2026-10-07 03:1x–03:22 · TUI settings change → "already has an active writer"; settings check misread

**A · my verification command was wrong (my error).** T9 and the T10 recipe read the last
`turn_context`. That entry is written only when a turn runs. TUI settings changes land as
`event_msg / thread_settings_applied` entries in the rollout. The operator's "settings
check" message did not become a turn (turn_context count stayed 3), so the grep showed the
old state twice. The settings did change. Correct check:
`grep '"thread_settings_applied"' "$F" | tail -1 | jq -c '.payload.thread_settings | {model, approval_policy, approvals_reviewer, reasoning_effort, profile: (.active_permission_profile.id // .permission_profile.type)}'`
Settings trail (UTC): 01:03–01:16:02 on-request/user/workspace · **01:16:21 auto_review** ·
01:18:56 auto_review · **01:19:09 approval `never` + `:danger-full-access`** (permission
profile disabled), effort `medium`.

**B · `-32600 thread … already has an active writer` — new on 0.160.x.** codex-cli is now
**0.160.1**. The TUI now runs as a client of a shared, managed app-server daemon
(`codex app-server --listen unix:// --managed-daemon`, pid 988415, up since 10-05 20:58).
On `/exit` the TUI says "Disconnected from this task. Any running work continues". The
daemon keeps the thread loaded as its writer, so the shim's own `app-server --stdio`
cannot resume it. **"TUI /exit = release" no longer holds right away.**
Observed: the writer-lock file was present at the operator's `tun resume` (~03:20); it was
gone at 03:21:50; my `tun resume` at 03:22:21 → exit 0. The daemon released the writer
within ~3 min of disconnect. The release interval is not characterised.
Operator recipe until fixed: after TUI `/exit`, wait until
`~/.codex/thread-writer-locks/<id>.lock` is gone, then `tun resume`. Never delete the lock.

**C · effective runtime now (stamped 01:22:21Z), for STATUS `holds:`:**
`tunnel head 01a113e0-b774-7e32-926a-bc19f050ab2c · gpt-6-sol/medium · dangerFullAccess (no sandbox) · approvals never · runtime observed 2026-10-07 03:22 · prior head 01a0f5a6… retired at 81 % ctx`
⚠ No sandbox and no approvals: Cartan can write anywhere and use the network with no
check (guide: "never a habit"). It conflicts with the RUNBOOK's "existing sources
read-only" unless the instruction contract holds. Majkee to confirm whether this is
intended. The less broad option is `auto_review` + workspace-write, which was briefly
active at 01:16:21.

**Next-version notes, transport owner:**
- the shim should connect to the shared daemon (`--remote unix://` exists on 0.160.1)
  instead of spawning its own stdio server → no writer conflict, and the TUI would see
  tunnel turns live.
- otherwise: a `tun resume` wait-for-writer mode that polls the lock, never touches it,
  and has a bounded timeout.
- `_stamp_runtime` should add `approvalsReviewer`.
- L8: re-run the selftest and one live turn on 0.160.1 (this resume is a partial proof only).

## T11 · 2026-10-07 · auto-review set — effective policy (supersedes T10 C)

Operator: TUI `/permissions` → auto-review; `/exit`; `tun resume` exit 0 (no writer conflict this
time). Last `thread_settings_applied`: `gpt-6-sol` · approval `on-request` · reviewer
**`auto_review`** · effort `medium` · profile `:workspace`. Vault runtime: `on-request`,
`workspaceWrite`, network off. Full access (T10) is gone.

STATUS line for the carrier, verbatim:
`tunnel head 01a113e0-b774-7e32-926a-bc19f050ab2c · gpt-6-sol/medium · workspaceWrite, net off · approvals on-request, reviewer auto_review (Guardian answers escalations) · set 2026-10-07 ~03:3x · tunnel-turn honouring UNVERIFIED until first turn · prior head 01a0f5a6… retired at 81 % ctx`

**Open — verify on the first tunnel turn:** the shim sends no reviewer on resume/turn, so check
that the tunnel turn ran with the thread's stored reviewer:
`grep '"type":"turn_context"' "$F" | tail -1 | jq -c '.payload | {approval_policy, approvals_reviewer, effort}'`
→ `auto_review` = T1 closed for this head · `user` = the setting does not reach tunnel turns;
fallback is the config.toml line (global).
If a Guardian review ever comes back to the shim as a request, it is still auto-declined. A
Guardian subagent thread appearing (as at 02:46) is the sign that review ran.
