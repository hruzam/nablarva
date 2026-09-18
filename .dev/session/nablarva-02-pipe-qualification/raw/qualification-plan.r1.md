---
kind: qualification plan
revision: r1
author: cartan
date: 2026-09-13
status: "Proposal for P1 audit; not a PAD, not arming, not send authority"
point: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/01.oraculum.point.md
point_sha256: daf69ae2cd8834a2b2d2c30aa977ee7121cecb01128c51b615e4109981792919
preflight: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/preflight.r1.md
handoff_rule: "Immutable after RETURN; corrections need a new cycle/revision"
---

# B-entry: one disposable native exchange

**Recommended first sitting: open/identify one disposable target and qualify its read-only
route; stop before any send unless the missing instance, admission and acknowledgement
contracts have been established.** Successful preflight is not successful delivery.
Oraculum audits this plan, branches on its VERDICT, and authors/drives the PAD; Cartan builds
any approved probe in a later POINT. No probe code or target fixture is created in P0.

Two proposed clarifications must be resolved by the head before it releases a PAD: file
presence is attention/availability, not consumption; and terminal completion plus missing
RETURN does not authorize another activation. These preserve the owning RUNBOOK and gaveled
r1 against the weaker language in the fold note. No L4 exception or new identity scheme.

## Target definition

Proposed workspace for the first sitting: **`/tmp/nablarva-b-entry-20260913-01`**.
This exact path is a candidate, not an existing/approved target. Cartan must first verify
absence, including a dangling symlink; an existing path stops setup, never reuse or delete it.
If another path is needed, the head names the new absolute path in a revised PAD before use.
Cartan creates the approved scratch with `mkdir -m 700 --` in a later cycle, not here.

Majkee opens one fresh interactive Codex there, with **no model/permission/provider/profile
overrides**, and names it `nablarva-b-entry-20260913-01` through the native UI. No `exec`, no
resume of a working conversation, no second hidden session. The directory is outside the
Nablarva instruction tree to avoid an accidental competing Cartan controller.

Oraculum records in STATUS `holds:` the exact **thread UUID · display name · workspace · host ·
opened_at**, plus the qualified route and observed incarnation discriminator. Record separate
**operator approval**, permitted actions, sitting identifier and expiry/disarm conditions.
A `target:` record is not that approval. Initially the permitted action is a **bounded read-only
inspection**; a send requires a later explicit confirmation of the fully resolved preview.

The scratch receiver is a **test fixture**, label `probe_codex`, not a new coordination seat.
The head must declare this test-only identity and its write scope in the audited PAD before
opening/arming it. Real `_bus/` seats remain `oraculum` and `cartan`; only Cartan writes this
cycle's real RETURN. Never point the scratch target at `01.oraculum.point.md` or let it claim
the existing Cartan identity. Working exclusions, checked as full IDs:

- `01a092ed-f422-7051-ba69-f6c1d47c57d8` — Cartan.
- `0a27e884-b106-48e6-b56a-71dcb271ab6f` — Oraculum's declared transcript/session.

Future fixture POINT and RETURN live **inside the scratch workspace**, so the test need not
add writable roots. Their exact paths are declared in §Positive case; approved fixture/probe
source, if needed, lives under this bed's `raw/probe/`. No binding-record implementation.

## Preconditions / STEP 0

Oraculum supplies the PAD's STEP 0 and its GLOSS note before the operator sits it. This plan
uses [PAD law, PAD → log](/home/hruzam/reposoma/raw.guides/PAD/GUIDE.md): expected results and
branches precede action; each actual outcome and count lands in that step's report fence.

**0a — audit gate, no runtime contact (Cartan; head verifies).** Check the exact P0 hashes,
an ACCEPT disposition covering the clarified plan, later probe authorization if needed,
and absence of an earlier unresolved attempt. Validate all future paths and the sole writer
of each. Existing raw/PAD/target files alone do not advance a phase. Any mismatch → stop for
the head; do not edit these r1 artifacts or retry a previous assignment.

**0b — operator-opened target and inspection approval ([HANDS]).** Observe native `/status`
and record the tuple/defaults/usage-path evidence. Confirm this is the one scratch TUI,
not either working seat. Human observation verifies native usability; it is not a screen
parser used by the probe. Trust/auth/permission obstacles → stop, not an override.

**0c — qualify the native read route (Cartan, only after inspection approval).** Read-only
inspection must tie the exact thread ID to the already-running target's actual server/route
and incarnation. Candidate: existing native control socket plus summary `thread/read`.
Do not guess a socket, start a daemon, invoke a resume/start method, or connect to a working
session to discover what happens. A socket file alone is not proof of ownership. Inspect
only explicit non-secret target metadata; no all-environment dumps or whole-server content
capture. Establish that the observer does not steal approvals or disrupt either native UI.

**Required output:** `QUALIFIED_READ_ROUTE` with the observed route/version, exact native
thread ID, workspace, current instance evidence, status and noninterference observations;
otherwise `STOP_ROUTE_UNKNOWN`, `STOP_IDENTITY_UNKNOWN` or `STOP_NOT_IDLE`. These are proposed
probe report labels, not claims that an existing tool emits them.

**0d — admission contract (Cartan; independent audit).** Prove what will reject a stale
instance and a transition from idle to active/approval at the submission boundary. Record
the native acknowledgement schema and recovery lookup. No status-snapshot-only check, no
assumed queue behavior, no manufactured “ack” from exit 0. A single designated carrier and
operator serialization are also required: no parallel sender, manual target input, resume,
or takeover while an attempt is being prepared/submitted. If an adequate guard cannot be
demonstrated without live characterization, return a scoped test proposal for fresh approval;
the positive dispatch stays blocked. Do not quietly substitute a one-shot wrapper for a
server-side guarantee it cannot provide.

**0e — final guard, immediately before the permitted send.** Recheck exact tuple/incarnation,
idle state, unchanged fixture hash, destination absent, unused attempt, no pending approvals
and no takeover. Any change invalidates the preview and arming. Disconnect/replacement is a
new arming after reconciliation, not a refresh-and-send loop.

Before submission these checks are reversible: disarm and leave the scratch/evidence intact.
After possible submission, reversibility is **not** assumed; use the interruption branch.

## Positive case

**Preconditions:** all of STEP 0 passed, the exact final native command/probe bytes are
audited, and majkee confirms **one** send. If any is unresolved, record `NOT RUN` with the
failed precondition. P0 supplies no live command with invented UUID/socket placeholders.

Future immutable fixture paths:

- Assignment: `/tmp/nablarva-b-entry-20260913-01/qualification.point.md`.
- Only receiver write: `/tmp/nablarva-b-entry-20260913-01/qualification.return.md`.

Cartan authors the fixture only under a later POINT and pins it in the PAD before arming.
It is POINT-shaped (`from`, `to: probe_codex`, scope, exact read/write paths, `done_when`,
`return_to`) but **not** live BUS cycle 01. Scope: read this fixture and one small synthetic
input, perform a deterministic transform/checksum specified there, and write the exact
RETURN once. Include a fresh per-attempt challenge in the fixture, not in the carrier line;
the RETURN must identify the fixture/hash/challenge, exact observed conversation ID,
performed calculation, commands/results and its own destination. No network, helpers,
background work, rollout access, repo writes or other effects. If identity/scope mismatches
or the destination already exists, report refusal in the native UI and do not overwrite.

The permitted message contains **one path pointer**, not the task body. Prefer queue only
after its route, acknowledgement and admission behavior are qualified; another native route
requires the same audit, not automatic fallback. Use the exact UUID, never name resolution
or “last session.” The carrier invocation must omit model/permission/provider overrides.
Opening this short-lived carrier client is allowed at the send step; starting a new target
conversation/server in place of the living TUI is not.

| Observation | Required evidence, recorded separately in the PAD |
|---|---|
| Prepared | Immutable POINT/input hashes, destination absent, resolved preview/tuple, unused one-shot attempt, final guard |
| Submitted / uncertain | One carrier invocation with timestamp, exit and its actual acknowledgement fields; failed/missing ack after possible handoff remains uncertain |
| Consumed | Native target/turn correlation plus the fixture's fresh challenge and correctly worked result; not a filename or UI echo alone |
| RETURN present | Exact path/type/hash and content check; no substitution, partial file or old receipt |
| Terminal | Same native thread/turn, terminal status and bounded public result; early/late events reconciled without resending |
| Accepted / advanced | Oraculum independently reruns the deterministic check and writes VERDICT; Oraculum alone advances STATUS; majkee's final GO/STOP stays separate |

Record permissions, subscriber-path evidence and native UI usability again afterward. A
successful delivery has no receiver-window paste and no context re-explanation in its routine
carriage; setup/verification window visits are counted separately, not hidden.

**Signal option:** default first sitting uses a qualified native completion/read-back route
and installs no hook. A project-local Stop attention probe is an optional later approval at
arming, with exact source hash, `.codex/hooks.json` path under this scratch, trust action and
allowed output specified beforehand. It can test the exact RETURN path at turn end, but may
not send/continue/nudge or authorize acceptance. Workspace-local notify is not proposed;
see [preflight, Turn-complete signal](preflight.r1.md). A missing signal/file triggers inspection,
not another activation. Mtime-only observation cannot pass this test.

## Negative cases

All mutation-bearing negative cases need their own named PAD step and explicit permission;
one-sitting approval is not an unbounded failure-injection license. Pure refusal fixtures
run first. The independent auditor distinguishes a local mock pass from real native behavior.
Each live test input needs a distinct immutable fixture, challenge, hash and RETURN path,
materialized in its PAD step before approval. Never reuse the positive fixture for another
live attempt, and never start a new case while an earlier attempt may still act.

| Case | Safe exercise | Predeclared required result |
|---|---|---|
| Wrong UUID/bed/seat/destination | Feed invalid synthetic identities or paths into the disarmed validator; include the two working IDs as deny fixtures, with carrier replaced by a call-count stub | `BLOCKED`; **zero carrier calls**, zero target work; no fallback or overwrite |
| Closed/stale thread | After explicit operator closure of the disposable target at an approved step, try to prepare with its old tuple; do not actually queue to that closed UUID | Stale/unloaded refused before submission; no implicit resume, no server start |
| Exact-name collision | Supply two synthetic candidates with the same name to the selector; no second live session required | Ambiguous name never selects a target; only an explicitly armed exact UUID may proceed |
| Same conversation, replacement instance | After closing/reconciling the prior attempt, majkee may resume **this disposable UUID only**, with fresh arming for observation, not send. Present the old preview to the guard | Old instance/preview rejected even if name/UUID/path/mtime match. A mock-only result leaves native replacement detection **unverified** |
| Duplicate attempt | In the same one-shot controller, request the same dispatch a second time with carrier-call instrumentation; after restart separately test the unresolved-state path | Second invocation blocked before queue; live send count for that fixture remains one. After controller restart: unreconciled/STOP, not “unused” |
| Interrupt after possible submission | Predeclared inert fixture only; majkee interrupts the **exact owned carrier client or disposable TUI** at the named boundary. Never kill the shared daemon/working seats | Attempt stays submitted-or-unknown; read-only reconciliation may find a late valid RETURN. No replay, new cycle, retarget or fallback paste while the old attempt may act |
| Busy / awaiting approval / unknown | First use injected state fixtures. A real naturally busy/approval target is observed only; do not manufacture a dangerous approval task | No carrier call; operator resolves native state if appropriate, then fresh guard. Snapshot-to-submit state-change fixture must also block |

Do not test “duplicate” by deliberately invoking queue twice and hoping the model deduplicates.
Do not count a validator's refusal as proof that native queue itself rejects that condition.
If required live failure behavior cannot be demonstrated safely under the named authority,
mark it `NOT RUN`/`UNVERIFIED`; the qualification VERDICT must not report a complete pass.

The interruption case must identify which component was interrupted and whether the target
could continue. Lost client acknowledgement is not target cancellation. If the exact turn or
its effects cannot be reconciled, leave the attempt unresolved and stop; an empty destination
does not clear it. No cleanup/removal of that evidence is part of this gate.

## Characterization

**Optional; separate explicit majkee approval for each sitting/case. NOT RUN by default.**
After the safe route and exact target are known, the head may offer a labeled active-turn
experiment using only the inert synthetic fixture. It must declare the extra input, permissible
effects and expected classifications before approval: refused; held until turn boundary;
joined/injected into an existing turn; unexpected/unknown. Record actual native thread/turn
IDs, order, acknowledgements and final content, not terminal impressions.

The observed queue policy is **not** permission for operational busy delivery. Injected or
unintended activation stops the experiment immediately. Any discovery that weakens the idle-only
guard returns to architecture review; do not silently adopt the characterization as the carrier.
Skipping this optional experiment is not a fabricated observation of next-turn queueing.

## Counts

Use r1's granularity: **one deliberate operator action**, including repeated selection,
preview inspection, copy/send invocation, window switch, paste, submit, explanation, or return
notice inspection. A macro does not erase confirmations. Count model/tool reads as engineering,
not human labor. Do not put setup work into “free” routine work or turn model tokens into savings.

| Category | Count here |
|---|---|
| Setup | Opening/naming target, recording/confirming identity, initial permission/usage inspection, read-route approval, optional hook/trust review |
| Routine carriage | Selecting/inspecting the assignment preview, operator-triggered send, any repeated carry/context repair, noticing and waking the head to read the RETURN |
| Recovery | Interrupted/ambiguous attempt reconciliation, disarm/re-arm, operator state resolution and any separately authorized retry |
| Audit/gavel | Reviewing results, approving a distinct experiment, independent audit interactions and final GO/STOP |

Majkee reports his actual actions; Oraculum records them in each PAD report fence; Cartan
supplies timestamps/invocation counts and checks consistency. Record per-step actual counts,
four-category totals and the sum. Use `unknown`, not zero, for missing human evidence. P0 has
no live-sitting measurements. Bed 01's sender-side baseline remains owed; no savings claim here.

**Nudges:** additionally tag/count any second activation of the same pointer. This is a
cross-cutting counter, not a fifth category to double-add to the total. Default: `NOT RUN`.
Human initiation is necessary but **not sufficient**: completed turn + absent RETURN does
not clear uncertainty. This plan permits no nudge until exact-target/effect reconciliation,
proof the old attempt cannot still publish/act, and a separately approved retry step. If that
cannot be established, stop. No automatic hook nudge or new BUS file kind.

## Operator-hands steps

**These are candidate PAD blocks, not a multi-command instruction to run now.** Oraculum
releases one at a time after the preceding branch passes, writes the GLOSS note first, and
materializes all future IDs/paths/hashes. Cartan does the engineering; majkee is not asked to
write scripts, chase sockets or repair configuration. Expected labels below are test outcomes,
not evidence already observed.

**[HANDS 0 — state inspection before setup].** Head points to the current PAD/STATUS and
confirms no armed/unresolved prior attempt. Native-free inspection in an office shell:

```sh
hostname
sed -n '1,180p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/STATUS.md
```

Expected: host `hruzam-120922`; the head's current checkpoint and explicit approval state agree
with the PAD. Mismatch → stop. Merely seeing the text `target:` is not a pass.

**[HANDS 1 — open only after audited setup].** Cartan has prepared the absent-checked scratch
under a later authorized cycle. In the selected new office terminal, launch:

```sh
/home/hruzam/.local/bin/codex -C /tmp/nablarva-b-entry-20260913-01
```

Expected: one native interactive TUI in that exact workspace, inherited defaults, no automatic
assignment. If trust/login/default-policy behavior blocks the approved setup, stop and report;
do not select broader permissions or change the account to continue.

**[HANDS 2 — name; then a separate inspection step].** In that disposable TUI:

```text
/rename nablarva-b-entry-20260913-01
```

Expected: native saved display name changes. Unsupported command → stop, no guessed `-n`.
When the head releases the next step, inspect:

```text
/status
```

Expected: record the actual non-secret identity/workspace/model/permission/usage and route
fields available. Do not assert a field is present if it is not. Missing native UUID or
subscriber-path evidence returns to Cartan for safe investigation, not an environment/auth dump.

**[HANDS 3 — inspection authority, then send authority separately].** Oraculum presents the
resolved target tuple and the exact limited read operation. Majkee approves/refuses that
operation; Cartan performs STEP 0c/0d. Only after they pass, the head presents the frozen
assignment preview and the exact one-shot native command. That block is composed after route
qualification; this r1 intentionally contains **no runnable send with placeholder IDs**.
Majkee approves one send; Cartan executes it, or majkee invokes the audited one-shot entrypoint
if the PAD selects that form. Expected: exactly one attempt; no receiver-window paste. Count
the confirmation and any invocation as actual distinct actions.

**[HANDS 4 — named failure action only].** For replacement/interruption cases the later PAD
must print the exact disposable UUID/client identity and native close/resume or Ctrl-C action
after resolving it. No broad kill command, guessed PID, `--last`, or command against either
working seat is provided here. Expected: test branch from §Negative cases; changing target or
instance disarms the earlier send authorization.

**[HANDS 5 — inspect usability/usage, alert the head, then gavel].** Return to the disposable
native UI for the same `/status` inspection; report actual values and usability without
parsing the screen automatically. Signal the head to inspect the exact fixture RETURN and PAD
evidence. After its qualification VERDICT, majkee records GO or STOP against that artifact.
These are distinct observations/decisions, released separately and counted, not one “done.”

## Stop conditions

Stop immediately for unintended activation, replacement, retarget or replay; loss of either
native working UI; uncertain admission/acknowledgement; inherited permissions or usage path
that cannot satisfy the gate; any proposed override; credential exposure/access request;
screen-parser dependency; transcript mutation; cross-host access; an observer that loads a
thread or takes over approvals; a new daemon claiming working sessions; duplicate/late effects;
or an existing/mismatched RETURN. If the native route fails, this bed STOPs: no tmux, manual
fallback paste, stored-thread tunnel or headless API substitution.

Stop means **cease new submissions**, preserve the exact attempt/evidence and use only the
approved bounded read-back to reconcile. It does not mean kill shared processes, remove locks,
delete scratch/history, revoke unrelated sessions or edit another writer's artifact. Unclear
recovery authority returns to Oraculum/majkee. A timeout or restart never resets “possibly sent.”

## Probe code

No code authored in P0. A later POINT may authorize these **proposed, currently absent** paths:

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/qualify.py`
  — bounded, foreground observer/validator and audited one-shot carrier, only after the
  native route/guard contracts are known. Read-only mode must have no send capability invoked;
  explicit send mode needs the approved exact tuple/fixture and an unused attempt. Fail closed
  on restart/uncertainty. No daemon management, auto-resume, search-by-name, retry, watcher,
  credential access, screen/rollout parsing, billing/config overrides or binding registry.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/test_qualify.py`
  — offline refusal/race/correlation fixtures with carrier-call counters; must not import a
  module that connects or submits at import time. Clearly label mocks versus native evidence.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/stop_attention.py`
  — optional later, approved Stop helper; bounded ID/path/availability output only. Never
  forwards the last message, reads a transcript, returns a continuation decision or sends.

The head's later POINT must also name authorized scratch fixture files and any probe output
sink before creation. All per-step reports stay in the PAD; no file-per-step mini-ledger.
One-shot attempt state is test control, not the excluded production binding-record build.
No deployment, repository cleanup, commit, push, pruning or surgical-table promotion.
