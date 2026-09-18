---
kind: native preflight
revision: r1
author: cartan
date: 2026-09-13
status: "P0 evidence only; no native route qualified or activated"
point: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/01.oraculum.point.md
point_sha256: daf69ae2cd8834a2b2d2c30aa977ee7121cecb01128c51b615e4109981792919
founding_sha256: b43d10ae13535e053547523044fb6c22e6448cc00f503457a60e48da3ab6814a
observed_frame: "hruzam-120922 · core · b99701f4b04735a16cb51257d070ba91b01a96b6 · thread 01a092ed-f422-7051-ba69-f6c1d47c57d8 · pane %50"
handoff_rule: "Immutable after RETURN; corrections need a new cycle/revision"
---

# B-entry native preflight

The installed CLI offers plausible native entry points. P0 does **not** establish that any
of them addresses an already-living TUI with the required incarnation and idle-state fence.
The next plan therefore has a read-only route/identity gate before its conditional send.
`Observed` below means this seat's local check; `documented` means the linked current page;
`proposal` and `unknown` are deliberately not qualification results. Exact command outcomes
are in [RETURN §2](../_bus/01.cartan.return.md).

## Route

**Observed, 2026-09-13 21:46 CEST:** `codex-cli 0.154.0`. Root help advertises `queue` for an
existing session and `agents` as a browser on the shared local app-server daemon. Help also
offers `--remote` with Unix-socket and WebSocket address forms. This is an interface inventory,
not evidence that the intended TUI is registered with a particular daemon.

| Local help checked | What it establishes | What it does not establish |
|---|---|---|
| `codex agents --help` | Interactive browser; `--remote` and `-C` exposed | No `--json` option advertised; listing is not documented as an inert read. No listing run. |
| `codex app-server --help` | `daemon`, `proxy`, schema generators; stdio/Unix/WebSocket listeners | Starting a fresh server is not attaching to the target's running server. |
| `codex app-server daemon --help` | Lifecycle verbs; `version` would report CLI and running-server versions | No `status` verb advertised. No lifecycle or running-server query run. |
| `codex app-server proxy --help` | Stdio proxy to a running control socket; explicit `--sock` | Socket location, target ownership, connection side effects, and missing-server behavior remain unproved. |

The earlier `--thread <UUID or exact name> --message` / optional `--remote` evidence is pinned
in [bed 01 VERDICT, Claim verification and Curvature 9](../../nablarva-01-design/_bus/01.oraculum.verdict.md).
It was **not refreshed by invoking queue**, even with `--help`: POINT 01 prohibits any such
invocation. The fetched [CLI reference](https://learn.chatgpt.com/docs/cli/reference) did not
contain `codex queue` or `codex agents`; this is a scoped documentation gap, not proof of absence
from all vendor material.

**Unknown:** whether default queue bootstraps a daemon; whether an unloaded thread is resumed;
which local socket reaches this TUI; whether a queue acknowledgement names the accepted
thread, turn and running instance; how name ambiguity is handled. Do not discover these by
trying queue against a working or unbound session.

**Proposal:** qualify an explicit same-host route to the operator-opened disposable TUI.
Do not start/bootstrap/restart the shared daemon, guess its socket, connect to the working
Cartan route, or use a fresh stdio server as a substitute. If the target is not already
reachable through a safe native route, the sitting stops at this gate.

## Identity vs incarnation

**Observed:** this process's `CODEX_THREAD_ID` is
`01a092ed-f422-7051-ba69-f6c1d47c57d8`; `TMUX_PANE=%50`; host `hruzam-120922`. These resolve
the POINT's Cartan seat, not a future target. `resume --help` accepts a UUID or session name
(UUID takes precedence); `fork --help` accepts a conversation UUID. Root help advertises no
startup `-n` name option. Use the documented native `/rename` interaction if available in the
disposable TUI; do not invent `codex -n`. [Developer commands](https://learn.chatgpt.com/docs/developer-commands)

**Documented:** resume uses `thread.id`; fork creates another thread ID. `thread.sessionId`
denotes a session-tree root, not an incarnation token. The fork examples themselves differ
for ephemeral forks; read returned fields, never derive equivalence. [App Server](https://learn.chatgpt.com/docs/app-server#start-or-resume-a-thread)

**Proposal:** map r1's generic conversation identity to the exact native `thread.id`, not a
display title or an assumed synonym named `sessionId`. Keep the operator's name as a label.
Record the exact route and whatever native registration/instance discriminator is actually
available, plus a corroborating target process PID/start time and host identity. A PID alone
is reusable; a TUI PID alone may say nothing about the server-side conversation instance.
The target's own declared UUID/environment is corroboration, not a transport ownership fence.

**Unknown:** a dependable native running-instance discriminator and its relation to the TUI
and daemon. Same-thread resume/restart can preserve the conversation identifier while replacing
the process. Unchanged name, path, UUID or file timestamp cannot clear that case. Before send,
the route must reject the former instance or provide evidence sufficient for the approved
single-carrier guard to do so. Replacement invalidates arming and every prepared preview.
This bed records observations in the existing PAD/STATUS; it does not build a binding registry.

## State

**Documented:** `thread/read` can return a summary without resume/subscription. Runtime states
are `notLoaded`, `idle`, `systemError`, or `active` with `activeFlags`; approval waiting is an
active flag. Reading does not load the thread. [App Server](https://learn.chatgpt.com/docs/app-server#read-a-stored-thread-without-resuming)

**Observed locally:** no RPC connection or state query was made. The future target does not
exist in the authorized state. Installed help does not settle queue behavior for any state.

| State seen through the qualified target route | This gate's action |
|---|---|
| Exact bound incarnation, `idle`, no unresolved attempt | Candidate for a fresh final guard; not yet permission to send |
| `active`, including approval/input waiting | No submission; operator may resolve it in the native UI; invalidate preview and recheck |
| `notLoaded`, `systemError`, missing/unknown status | Stop; never load/resume merely to make the check pass |
| Disconnect, replacement, or conflicting observers | Disarm; reconcile without replay |

An idle snapshot is not an atomic admission guard. Neither observed help nor the fetched
material establishes a queue compare-and-swap against both idle state and incarnation.
`turn/steer` is explicitly for active turns, so it is not the idle-only alternative.
The plan requires a proved native guard plus designated-carrier/operator serialization;
otherwise the send step remains blocked. Human visual inspection may confirm native UI
usability, but screen parsing never becomes the state check.

## Permissions and usage path

**Observed:** CLI help exposes override options; none was used. No disposable session was
opened, so its effective model, sandbox, approval policy and account mode are **unknown**.
“Defaults only” is an instruction to inherit and inspect effective settings, not a claim
that the fresh target necessarily defaults to `workspace-write` or a particular approval mode.

**Documented observation surface:** native `/status` reports model, approval policy, writable
roots and usage; remote connections also report route/server information. `codex login status`
reports authentication mode, not a per-turn billing receipt. [Developer commands](https://learn.chatgpt.com/docs/developer-commands#inspect-the-session-with-status)

**Proposal:** majkee records a redacted before/after native UI observation: account/plan or
usage-path label, model, effective permissions, allowed workspace, route/version where shown,
and usage counters. The success claim is only **operator-observed subscriber usage**, at the
strength r1 requires; token counts alone cannot distinguish subscription from API billing.
If the UI cannot establish the required usage path, report it unverified and stop qualification.

API-key/provider indicators, a changed account/usage path, a newly required billing credential,
or changed effective permissions/model are drift, not setup tasks to repair silently. No
environment dump, token/auth-file read, login operation, credential experiment or provider
override. Login-status help was read; login status itself was not run. Do not change a read-only
or otherwise incompatible default simply to make the target produce a file.

## Read-back

**Documented:** `turn/completed` distinguishes completed, interrupted and failed turns.
Saved read-back can include turns without resuming. [App Server](https://learn.chatgpt.com/docs/app-server#events)

**Observed precedent, not a qualified carrier:**
`/home/hruzam/ia-sync/zsh/ai/tunnel-codex.py:340` correlates completion and supports later
read-back. But it starts a fresh stdio server (`:168`), sets `approvalPolicy: never` for
thread start (`:325`), and its `item/completed` text collection (`:380`) is not filtered by
thread/turn. Do **not** run or transplant it. Borrow only the independently checked
completion/read-back reconciliation principle from the [tunnel guide](/home/hruzam/reposoma/raw.guides/tunnel/GUIDE.md).

**Proposed acceptance chain:** freeze the synthetic POINT bytes/hash and exact `return_to`;
preview the target tuple; record the one carrier attempt and acknowledgement; bind the actual
native turn to that attempt; obtain terminal evidence; read the exact RETURN; independently
check its work and correlation. Store only the exact target's allowlisted public result and
thread/turn/status fields, not unfiltered event streams or other conversations.

`test -f return_to` at turn end is an **availability/attention test**, not proof of consumption.
The file may be partial, stale, wrongly bound or authored by the wrong actor. A fresh challenge
inside the immutable fixture, the correct response to it, exact destination, and native
thread/turn evidence make the inference testable. Acceptance still belongs to Oraculum.
No file, no acknowledgement, or a completed turn without the required artifact means
**unreconciled**, not “safe to nudge.” Completion does not by itself prove that no side effect
or delayed publication can occur. See [r1, Uncertainty after submission](../../nablarva-01-design/raw/design.r1.md).

Rollout public-item pickup is a different, operator-signalled evidence operation. None occurred
in P0. It must not be hidden inside metadata-only `observe()` or used as a carrier/readiness
parser. Native target read-back is the preferred qualification evidence; if it needs forbidden
resume, hidden content, or a screen parser, stop.

## Vendor facts refreshed

Installed help/version were rechecked on **2026-09-13 21:46:15 CEST**. The executable resolves
from `/home/hruzam/.local/bin/codex` to
`/home/hruzam/.codex/packages/standalone/releases/0.154.0-x86_64-unknown-linux-musl/bin/codex`
(static, stripped x86-64 ELF). All nine version/help commands exited 0; the read-only PATH-alias
warning did not prevent help. It was not repaired.

Current official pages opened and checked on **2026-09-13**: the CLI reference, App Server,
Developer commands, Advanced Configuration, Configuration Reference, Hooks, and changelog
(links adjacent to claims). These are live documentation, not a guarantee that every described
feature is active in this installed account/build.

The [changelog](https://learn.chatgpt.com/docs/changelog) dates CLI 0.154.0 to **September 9**
and its Python SDK entry to September 10. The fetched September list begins September 11;
no post-September-12 release changing this question was established. Today's newly read hook
and history details are **new evidence here**, not claimed new vendor releases. No update,
schema generation, SDK install or native behavior probe was performed.

## Turn-complete signal

**Documented:** `notify` runs a program with one JSON argument for `agent-turn-complete`;
fields include `type`, `thread-id`, `turn-id`, `cwd`, `input-messages`, and
`last-assistant-message`. [Advanced Configuration](https://learn.chatgpt.com/docs/config-file/config-advanced#notifications)
But project `.codex/config.toml` cannot set `notify`: that key is ignored there.
[Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference#configtoml)
Thus workspace-local **notify is not an eligible plan**; no global-config or command-line
override workaround is proposed.

**Documented alternative:** project `.codex/hooks.json` supports `Stop`, subject to project
trust and review of the exact hook definition. Input includes `session_id`, `cwd`,
`hook_event_name`, `turn_id`, `stop_hook_active`, and nullable `last_assistant_message`.
Subagent hooks may use a parent session ID. `decision: block` creates a continuation prompt.
Interrupt is separate. Asynchronous hooks can finish out of order or be cancelled at session
end. [Hooks](https://learn.chatgpt.com/docs/hooks#stop)

**Not observed:** installed Stop firing, reload timing, identifier mapping, trust behavior,
or delivery guarantees. Help/version alone cannot qualify a hook. No hook was installed.

**Ranked plan:** (1) an explicitly approved, successfully tested workspace-local Stop can
provide a turn-end attention hint; (2) otherwise use a qualified app-server terminal signal
with exact-turn read-back; (3) rollout mtime can only prompt a bounded inspection, never pass
the completion/consumption test. Prefer the native event/read-back route for the first sitting
if it is already available, avoiding an extra configuration/trust change.

An optional future Stop probe may retain only whitelisted IDs, event name, workspace and a
present/absent result for the one approved path. It must not read the transcript, return a
continuation decision, submit a prompt, approve tools, or send a nudge. Error/missing signal
leaves attention outstanding. Actual helper bytes, hook scope/trust and any host-local trust
write need explicit approval at arming; this plan does not authorize their installation.

## Rollout semantics and observe() metadata

**Observed metadata only, 2026-09-13 21:45 CEST:**

```text
path: /home/hruzam/.codex/sessions/2026/09/12/rollout-2026-09-12T02-04-23-01a092ed-f422-7051-ba69-f6c1d47c57d8.jsonl
type: regular file
bytes: 20240734
inode: 8677692
mtime/ctime: 2026-09-13 21:45:55.811988267 +0200
resolved path: unchanged by readlink -f
```

This proves a file was available then. Its date-bearing filename is not the current run's
start time. There was no record-type scan, content read or transcript edit in this preflight.
Size/inode were one-off diagnostic corroboration, not additions to the approved `observe()` API.

**Documented:** resume alone does not advance rollout modified time; starting a turn does.
Archive moves logs, rollback persists a marker, and history modes can differ in read/resume
support. [App Server](https://learn.chatgpt.com/docs/app-server#start-or-resume-a-thread)
Installed root help also advertises `migrate-rollouts`; it was not invoked.

**Unknown:** a released filesystem contract guaranteeing live append-only writes, no rollover,
stable filenames, atomic publication, or “read only on resume/fork.” Logical conversation
continuation is not proof of those storage properties. Do not import the consult's Claude
storage claims as Codex facts. We did not exercise resume, fork, migration or compaction.

| Allowed metadata | Defensible use | Cannot establish |
|---|---|---|
| Existence and resolved path | Locate bounded evidence; detect disappearance/path changes | Receipt, live process, or addressable native route |
| Session ID supplied externally / in filename | Candidate conversation locator | Running incarnation, fork identity mapping, or verified ownership |
| mtime | File modification hint | Turn completion; resume/restart absence; idle/approval state |
| Observed path rollover | Invalidate the old evidence locator pending reconciliation | Automatic “new session” or a verified reincarnation event |

**Editing hazard:** persisted history participates in continuation; it is not inert chat
decoration. Manual edits could alter reconstructed context or corrupt resume (**inference**;
the exact manual-edit behavior was not tested or guaranteed by the sources). Therefore the
answer to “could edits alter resumed belief?” is **yes, treat that as a real risk; never edit**.
No guarantee is made about whether a particular edit is noticed by an already-running model.
The prohibition follows [HANDSHAKE, Delivery rule](/home/hruzam/ia-sync/HANDSHAKE.md) and this
RUNBOOK's transcript boundary, not a promise about internal storage mechanics.
