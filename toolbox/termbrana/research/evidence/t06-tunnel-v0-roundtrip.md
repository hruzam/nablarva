---
what: tunnel v0 round-trip evidence — FAIL receipts + fix + PASS receipts (both attempts are the proof)
state: EVIDENCE — gate t3 CLOSED on re-run 2 (2026-09-03)
verified: 2026-09-03 (independent grep vs DECISIONS.md:109)
next: ["v1 candidate: resident process (mid-stream steer)", "Cartan: writer-lock residue advice", "04-visible session when majkee opens it"]
---

# t3 receipts — termbrana 03-tunnel live round-trip

```yaml
verdict: FAIL — round-trip did not complete; tunnel returned no result to verify
gate: One full round-trip (Claude→Codex task, Codex→Claude result) through the v0
  tunnel, live on office, receipts on disk in this session folder.
seat: Claude · Opus 4.8 · office (hruzam-120922)
codex_cli: 0.152.1 (matches shim protocol pin)
tunnel_model_enabled: gpt-5.6-sol (from tunnel.state.json, majkee enable 2026-09-02T22:45:16Z)
run_window_utc: 2026-09-02T22:48:18Z … 2026-09-02T22:49:37Z
```

## Host verification (step 1)

```
$ ls /usr/bin/php74        -> /usr/bin/php74            (present)
$ command -v valet         -> /home/hruzam/.config/composer/vendor/bin/valet (present)
=> office. Gate host requirement satisfied.
```

## Precondition (step 3)

`tunnel.state.json` present — majkee ran `open --enable` (Claude seat did NOT enable).

```
$ ls -la .../toolbox-termbrana-03-tunnel/tunnel.state.json
-rw-r--r-- 1 hruzam hruzam 213  3. zář 00.45 tunnel.state.json     (PRECOND_EXIT=0)

$ zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh status        (STATUS_EXIT=0, local verb)
{
  "created": "2026-09-02T22:45:16Z",
  "lastTurnId": null,
  "model": "gpt-5.6-sol",
  "sandbox": { "networkAccess": false, "type": "readOnly" },
  "threadId": "01a0644c-4888-77d0-be9c-0032d31a4e0b"
}
```

Note at this point already: `lastTurnId: null` — the enabled thread had taken **zero turns**.

## The round-trip (step 4)

### send — turn/start on stored thread

```
SEND_START=2026-09-02T22:48:18Z
$ zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh send \
    'Read /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md and return the
     ADR-0002 heading line verbatim, plus one sentence stating what it froze.'
SEND_EXIT=30                       # 30 = protocol-error (shim exit-code contract)
SEND_END=2026-09-02T22:48:18Z
stdout: (empty)
stderr: tunnel-codex.py: app-server returned a JSON-RPC error for id=2:
        {'code': -32600, 'message': 'no rollout found for thread id
         01a0644c-4888-77d0-be9c-0032d31a4e0b'}
```

### read — reconcile (thread/read includeTurns)

```
READ_START=2026-09-02T22:49:11Z
$ zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh read
READ_EXIT=30
stdout: (empty)
stderr: tunnel-codex.py: app-server returned a JSON-RPC error for id=2:
        {'code': -32600, 'message': 'thread not loaded:
         01a0644c-4888-77d0-be9c-0032d31a4e0b'}
```

### Streamed vs reconciled comparison

- **Streamed (send):** nothing — send errored at transport (exit 30) before any turn ran.
- **Reconciled (read):** nothing — read errored at transport (exit 30).
- This is **NOT** a reconcile-mismatch (exit 50). Both legs failed identically at the
  JSON-RPC transport: the stored thread is not resumable. There is no Codex-side claim
  to compare, and nothing to verify against the real file *via the tunnel*.

## Bonus probe (step 5) — resume then steer

Cannot be executed. `resume` (the liveness probe the steer would follow) fails on the
same dead thread, so resumed-steer semantics are **untested this run**:

```
RESUME_START=2026-09-02T22:49:37Z
$ zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh resume
RESUME_EXIT=30
stderr: tunnel-codex.py: app-server returned a JSON-RPC error for id=2:
        {'code': -32600, 'message': 'no rollout found for thread id
         01a0644c-4888-77d0-be9c-0032d31a4e0b'}
```

## Mechanism evidence — why it failed

```
$ codex --version                     -> codex-cli 0.152.1
$ ls ~/.codex/sessions/**/*01a0644c*  -> no matches   (NO rollout file for the thread)
$ find ~/.codex -iname '*01a0644c*'   -> /home/hruzam/.codex/thread-writer-locks/
                                         01a0644c-4888-77d0-be9c-0032d31a4e0b.lock
```

**Root cause (reproducible, v0 shim design finding):**
`open --enable` runs a zero-turn preflight (`initialize → account/read → model/list →
thread/start`). On codex-cli 0.152.1 `thread/start` allocates a thread id and a
**writer-lock** but does **not** materialize a **rollout** — the rollout is written on
the first *turn*. The stored `threadId` therefore points at a thread with no rollout.
Every subsequent verb runs in its own fresh `codex app-server --stdio` subprocess (no
daemon, per RUNBOOK constraint) and begins with `thread/resume`, which looks up the
(nonexistent) rollout → `-32600 no rollout found` / `thread not loaded`.

The v0 open→send handoff cannot bridge a zero-turn thread across process boundaries.
`lastTurnId: null` in the state file was the early signal. This is precisely the class
of behavior-proof failure t3 exists to surface before promotion (Sella L8: unchanged
files != unchanged behavior on an experimental protocol).

## Ground-truth verification of ADR-0002 (step 7 — done independently of the tunnel)

The tunnel returned no claim, so there is nothing of the tunnel's to trust-check. Recorded
here as the ground truth a working tunnel would have had to match:

```
$ grep -n "0002" toolbox/termbrana/DECISIONS.md
109:## ADR-0002 — M0 host contract FROZEN
```

- **ADR-0002 heading line (verbatim):** `## ADR-0002 — M0 host contract FROZEN`
- **What it froze (one sentence):** it froze termbrana's **M0 host contract** — the
  office-pinned host/version baseline — under nablarva flag **L11** (dated 2026-09-02),
  closing M0 so downstream work may proceed against a fixed host contract.

## Disposition

- Gate **t3 = FAIL**. Round-trip incomplete; no result streamed or reconciled.
- No Codex quota was spent on a completed turn (both `send` attempts died at transport
  before a turn ran).
- Claude seat did **not** re-enable and did **not** silently retry the send.
- Shim remains **NOT deployed** to `~/.config/zsh` (hold stands — behavior proof failed).
- Fix belongs to the shim (owner/@Cartan): `open --enable` must leave a **resumable**
  thread — e.g. drive one no-op committed turn at enable so a rollout exists, or have
  `send` fall back to `thread/start` when `resume` reports no-rollout, or move to a
  resident process (v1/daemon) so the thread lives in one process across verbs.
- Codex-side residue: a stale writer-lock at
  `~/.codex/thread-writer-locks/01a0644c-4888-77d0-be9c-0032d31a4e0b.lock` (not cleaned
  by the shim's `close`, which is local-only).

---

# t3 RE-RUN 2 — 2026-09-03 (fix f32eb9a applied) — GATE PASS

```yaml
run: re-run 2 (appended, prior FAIL receipts above preserved verbatim)
writer: Claude · Opus 4.8 · office (t3 gate seat)
host: office (hruzam-120922) — verified this run: `ls /usr/bin/php74`=/usr/bin/php74,
  `command -v valet`=/home/hruzam/.config/composer/vendor/bin/valet (both present, exit 0)
fix_commit: f32eb9a ("tunnel v0 fix: thread birth on first send (zero-turn thread/start
  leaves no rollout on 0.152.1 — t3 FAIL evidence); exit 12 no-thread; regression
  fixtures") · authored 2026-09-03 01:00:59 +0200 · repo ~/ia-sync, checked out on the
  live shim's branch (read-back gitInfo.sha == f32eb9a, branch main)
model: gpt-5.6-sol (from post-send tunnel.state.json; read-back modelProvider=openai)
codex_cli: 0.152.1 (read-back thread.cliVersion)
result: GATE PASS — full round-trip completed, streamed == reconciled, ADR line verified
  independently against the real file.
```

## Precondition (step 3)

- `tunnel.state.json` PRESENT before this run — majkee ran `open --enable`; Claude seat
  did NOT enable. Pre-send content: `{created:2026-09-02T23:23:41Z, enabled:true,
  lastTurnId:null, model:null, sandbox:read-only, threadId:null}`. threadId:null is the
  EXPECTED post-fix shape — under f32eb9a `open --enable` persists threadId:null and the
  thread is born on first `send` (THREAD BIRTH note in the shim header).

## The round-trip (step 4)

### send — exit 0
- start 2026-09-02T23:26:14Z · end 2026-09-02T23:26:26Z (UTC; = 01:26 CEST 2026-09-03)
- cmd: `zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh send 'Read /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md and return the ADR-0002 heading line verbatim, plus one sentence stating what it froze.'`
- stdout (streamed result):
  ```
  ## ADR-0002 — M0 host contract FROZEN

  It froze the exact office-host runtime/toolchain pins and runtime-confirmed behavior that all M1/M2 code must target.
  ```
- stderr: (empty)
- Thread born WITH a rollout this time — the exact failure class the prior run caught is
  gone. Post-send `tunnel.state.json`: threadId=01a06471-cf85-72a1-9fa8-3526d15ad4b8,
  lastTurnId=01a06471-cfd9-71c0-b8a7-8d9ce4ab9da2, model=gpt-5.6-sol,
  sandbox={type:readOnly, networkAccess:false}.

### read (reconcile) — exit 0
- start/end 2026-09-02T23:26:38Z
- cmd: `zsh ~/ia-sync/zsh/ai/tunnel-codex.zsh read`
- thread/read(includeTurns=true) returned the full thread. Key fields:
  - thread.id / sessionId = 01a06471-cf85-72a1-9fa8-3526d15ad4b8
  - rollout path = `~/.codex/sessions/2026/09/03/rollout-2026-09-03T01-26-15-01a06471-cf85-72a1-9fa8-3526d15ad4b8.jsonl` (ON DISK, 107682 bytes — verified `ls -l`)
  - gitInfo.sha = f32eb9ac7d37… branch main (fix commit is what drove it)
  - turn status=completed, durationMs=10692, exitCode 0 on Codex's own `rg` command
  - final_answer agentMessage text == the streamed send stdout
- Codex reached the answer by running `rg -n -A50 -B2 '^#* ADR-0002|ADR-0002' DECISIONS.md`
  in its read-only sandbox (cwd /home/hruzam/ia-sync) — i.e. it read the real file.

### streamed vs reconciled
- Compared programmatically (json final_answer vs send stdout): **MATCH = True**.
- NOT a reconcile-mismatch (exit 50 did not occur).

## Bonus probe (step 5, not gate-fatal) — resumed-steer semantics

- `resume` — exit 0 · `thread 01a06471-… status={'type':'idle'}`. (Prior run this verb
  died exit 30 "no rollout found"; now it resumes cleanly — direct evidence the fix made
  the thread resumable across process boundaries.)
- `steer 'Also state the ADR-0002 Date field value verbatim.'` — exit 30 · app-server
  JSON-RPC error `-32600 'no active turn to steer'`.
- Loop evidence: after a fresh `resume`, the thread is idle (its one turn already
  completed), and the no-daemon v0 spawns a new subprocess per verb — so there is no
  live streaming turn for `steer` to target. Resumed-steer against a COMPLETED turn is
  not possible in v0; true mid-stream steering still needs a resident process (v1). NB:
  the shim's header maps "steer had no turn" to exit 40, but here the app-server itself
  rejected first (-32600), which the shim surfaces as exit 30 protocol-error — the shim
  does not pre-guard a completed-turn steer. Recorded as loop evidence, not a gate fail.

## Independent verification (step 7) — truth over the tunnel's claim

- `grep -n 'ADR-0002' ~/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md`:
  - line 109: `## ADR-0002 — M0 host contract FROZEN`  ← heading, matches tunnel verbatim
  - line 105: a pointer reference (not the heading)
- The tunnel's returned heading line is byte-for-byte the real DECISIONS.md:109 heading.
  ADR-0002's own body (Date 2026-09-02; "the host contract is frozen as below; all M1/M2
  code targets exactly this"; the five pins) confirms the tunnel's one-sentence summary
  is faithful. Gate closes on verified truth, not the tunnel's claim.

## Disposition — RE-RUN 2

- Gate **t3 = PASS**. One full round-trip (Claude→Codex task, Codex→Claude result) on
  office, live, receipts on disk, streamed==reconciled, ADR line independently verified.
- The prior FAIL's root cause (zero-turn `thread/start` → no rollout → every later
  `thread/resume` fails -32600) is FIXED by f32eb9a: thread birth deferred to first
  `send` (thread/start + turn/start in one connection), so a rollout exists before any
  resume. Confirmed by: rollout file on disk + `resume` now exit 0.
- Tunnel CLOSED by the Claude seat after the passing gate (see close receipt below).
- HOLD unchanged: shim still NOT deployed to `~/.config/zsh` — deployment/promotion is
  the owner seat's (t4) call, not this gate's. t3 passing only unblocks t4.

## Close (step 9) + residue note

- `close` — exit 0 · 2026-09-02T23:28:45Z · `tunnel.state.json removed — Law 2.4
  re-arms; next 'open' requires --enable again`. State file confirmed absent after.
- WRITER-LOCK RESIDUE (honest loop evidence — contradicts a shim-header claim):
  - prior FAIL lock `01a0644c-…lock` = GONE.
  - BUT this run left `~/.codex/thread-writer-locks/01a06471-cf85-72a1-9fa8-3526d15ad4b8.lock`
    (created 01:27, by `send`'s thread/start). The shim header states the fix removed the
    stale-writer-lock residue class because "`open` no longer creates any codex-side
    artifact (no thread/start)". That is only half true: the thread/start (and its
    writer-lock) simply MOVED from `open` to `send`. `close` is still local-only and does
    NOT clean this codex-side lock. The residue class persists — relocated, not
    eliminated. Flag for the owner seat / @Cartan (not gate-fatal; t3 still PASS).
  - (Unrelated older locks 01a06223-*.lock from 2026-09-02 14:41 also present; not this
    session's.)
