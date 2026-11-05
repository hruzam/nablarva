# Termpanum X1 — entry and release

Recorder: Cartan · 2026-10-30 18:07 CET.
Initial state at first recording: decision sitting in P0. See the dated P0 completion below for the subsequent verified transition.

## Gavel 1 — Q-only D4 exception: accepted

Majkee's actual answer in this session, 2026-10-30:

> gavel: A

This selects option A of the immediately preceding decision presentation. The
accepted proposal was:

> I authorize a Q-only exception to L14 D4 for constructing and running the isolated synthetic source-qualification experiment described in this RUNBOOK. The broader research obligation remains. This grants no living-session input, shared-substrate integration, product build or deployment. Helper language/dependencies remain a separate decision; independent expectations must be accepted before capture implementation.

The longer quotation is Cartan's proposed wording accepted by that selection,
not a verbatim longer message from Majkee. The governing experiment and effects
are in [RUNBOOK.md](../RUNBOOK.md), “P0 release boundary — concrete scope to present”.
The exception covers the following bounded effects once the remaining release
and phase conditions are met:

- Synthetic source qualification and retained evidence only in this bed's assigned
  `expected/`, `src/`, `runs/`, `raw/` and `_bus/` scopes.
- Fresh per-run `/tmp/tq-<uid>-<unique-id>/` controls and private `tmux.sock`, with
  exact paths recorded before spawn, path-length checks and refusal of existing
  paths or unbound ownership. Every tmux invocation names that socket explicitly;
  startup uses `-f /dev/null`, 80x24 and a controlled environment.
- Synthetic nonsecret pane output, started by owned out-of-band control after
  capture readiness. No default or foreign server, user config, login startup,
  hooks, living agent pane, provider CLI or terminal-input injection.
- Run-owned failure cases: reader pause/resume, termination, disconnect/rebind
  and recreation, with process incarnation evidence before action, a 15-second
  watchdog per run and verified process cleanup.
- Cleanup only of exact proven-owned temporary controls/socket after process
  exit. Retain run bundles, including failures. No global shutdown or patterned
  process killing, shared-record write, foreign-session edit, commit, push or deploy.

The broader relay-research obligation remains open. This operational exception
does not amend canon or select the animal/product language. RUNBOOK remains the
reviewed plan; this receipt records its subsequent release decision separately.

## Gavel 2 — C++ helpers: accepted

Recorded by Cartan, 2026-10-30 18:32 CET. Majkee's actual answer:

> B

This selects option B after the cost discussion, narrowed in that discussion to
small C++ helpers using the existing compiler, C++ standard library and Linux/POSIX
interfaces, a simple build command, and no framework or downloaded dependencies.
Thin explicit zsh command entry and existing tmux remain within the proposed Q
tooling scope. No package installation or global configuration change is released.
This is a Q-only helper choice, not the animal language or C product-stack decision.

Disposition against the reviewed plan: the RUNBOOK expressly left helper language
for a separate operator decision and labelled Python a recommendation. Gavel 2
resolves that open choice in favor of C++; the Python recommendation is superseded
for Q helpers. Gate, ownership, source contract, acceptance thresholds, isolation
and oracle-before-builder sequence are unchanged. No material architectural plan
amendment is identified. Preserve the reviewed RUNBOOK as written and carry this
receipt into each POINT and witness review. A future dependency or wider effect
outside this scope requires its own disposition.

Read-only executable probes on office / hruzam-120922, HEAD
`74f4501ea101f66eddb64f884c70f510cf949754`:

| Executable | Observed version | SHA-256 |
|---|---|---|
| `/usr/bin/c++` | GCC 16.2.1 20260810 | `f04191f6a7b2cd7d9a62e1745872b8a6088791e5af6955488c69c9b2c4668bc9` |
| `/usr/bin/zsh` | 5.9.2 (x86_64-pc-linux-gnu) | `76e36b725f80c3b57a19b3747da0ad75fbfe4d5ae19d8b5c259fe52ac8891099` |
| `/usr/bin/tmux` | 3.7c | `e79f47015e65b128767ae0d12d0804b088a2d5fb9f6e04194f9abdc1388c435f` |

Compiler availability is observed; successful compilation/linking and full toolchain
identity are not yet tested. No tmux server was contacted. The unchanged RUNBOOK
SHA-256 at this decision is
`5cbd0c0f33597fdbedf387f6b3fe0812414017840c825af9b23a1df8a8ddc5e3`.

## Remaining P0 work

Both operator release decisions are now recorded. They need no repeat approval.

Technical entry must still recheck accepted input hashes and freeze the row-by-row
Q acceptance mapping before completing P0; carry the executable evidence above
forward and disposition any drift. Independent
expectations and their witness review/head ACCEPT precede capture implementation.
No worker has been dispatched and no Q code, expected corpus, fixture or runtime
has been started by this decision sitting.

## P0 completion — 2026-10-30 18:36 CET

Majkee's next instruction after both gavels: “ok, go to next.” Cartan adopts the
working-head/Medusa role and sole STATUS pen. MANNED: both actual operator gavels
are recorded above. No model switch is inferred from this posture. Child carriage
is selected explicitly at dispatch and actual tool-returned handles are recorded.

### Frozen inputs and executable drift check

| Input | SHA-256 | Result |
|---|---|---|
| `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md` | `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145` | MATCH |
| `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/source-contract.md` | `7086e59527c77040be9d41ee94966f661dd751c009e5eb636590db103dd32694` | MATCH |
| `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/research-disposition.md` | `b2cad9dabcaa62a47440c4e235548e42f8812c0b1183febecda8d05659aebc80` | MATCH |

All three executable hashes above were reread and matched. RUNBOOK remains
`5cbd0c0f33597fdbedf387f6b3fe0812414017840c825af9b23a1df8a8ddc5e3`.
The original Q source-fixture name is resolved to this bed by RUNBOOK authority.
The X0 packet acceptance and X2 package table were inspected; they do not themselves
release runtime. The applicable release is the two actual gavels above. The dated
X0 bounded D4 search is retained as dated evidence, not repeated or upgraded to a
current universal absence claim. No broader D4 verdict is claimed or needed for
this exact Q exception. No artifact/hash or executable drift was observed.

### Frozen row-by-row Q mapping

This mapping carries the accepted source contract and approved plan §4 package
labels into Q. It freezes requirements before corpus generation or capture.

| ID | Required Q evidence and bar | Later-package boundary |
|---|---|---|
| Q01 | Bind host/boot, exact socket/server incarnation, pane/process-start identity, tmux 3.7c binary/tag/hash, 80x24, interval, argv, environment allowlist and load context. Unknown identity stays unknown. | No shared registry/producer assignment. |
| Q02 | Independent post-termios bytes: OPOST off and separate OPOST+ONLCR with NL→CR-NL; CR/LF, NUL, backslash, ANSI and split-escape cases. Record before/after flags and control chars, payload/helper hashes. Unexpected termios change invalidates. | No claim about adapter-owned PTYs. |
| Q03 | Separate short frozen 80x24 screen with exact capture options and screen expectation. Never use binary burst rendering as the byte oracle. | No view product. |
| Q04 | 30 normal fresh invocations, each 256 numbered 1024-byte frames every 10 ms; 30 burst fresh invocations, each 4096 numbered 1024-byte frames without deliberate pacing. Exact bytes, zero missing/duplicate/reordered frames; retain chunks without message claims. | Repeat through C later. |
| Q05 | Independent monotonic marker release→reader-visible completed append; normal p95 ≤500 ms/max ≤1000 ms. Across 30 sorted samples p95 is sample 29. Ready metadata ≤1500 ms; whole normal ≤6 s/burst ≤10 s; per-run watchdog 15 s. Freeze metric population/clock definitions in oracle schedule, report all samples and maxima. | R inspect/replay/report public invocation and E packaged entry timing deferred. |
| Q06 | 30 fake-Done/prompt-looking cases, then independently proven alive/quiet 5 s before separately timed exit. No task_completed, accepted or turn-ended inference. Control/wait status separate from captured text. | C/L repeat; product semantic vocabulary remains open. |
| Q07 | Ten each: owned sink loss halfway through burst, reader pause 3 s, capture disconnect/reconnect, replay-frame deletion, duplication and reordering. Each retains explicit incomplete/gap/error or measured narrowed coverage, never clean success. Directly supervised failure detection ≤1 s; hard stop 15 s. | No universal losslessness under pressure. |
| Q08 | Ten pane recreation and ten fresh-server cases, repeated names/indexes without inherited fresh state. Late attachment marks earlier coverage absent; reconnect is discontinuity until rebound. No renewed timestamp for old observations. | Shared ownership and C/L health/view are deferred. |
| Q09 | Fresh witness checks actual sources and runs matrix. Q comparator rejects invalid/incomplete/mismatched bundles nonzero with reason. Preserve all failed/invalid/timed-out bundles and original criteria. | Full R twice-replay/report and ten-per-class product rejection matrix deferred; Q fault replay remains required by Q07. |
| Q10 | Every run binds immutable expected/criteria/source/config hashes, identities, clocks, coverage, termios, capture/control/compare/report, stderr, exit and exact owned cleanup evidence. | C health.json/250 ms heartbeat, L refresh/lifetime, E publication and V shared admission remain their owners' later packages. |

P0 disposition: ACCEPT entry for P1 independent expectations only. Oracle generation
and its local C++ build may now proceed in the assigned expected scope. No fixture,
capture code, tmux server or source qualification run precedes oracle review and
head ACCEPT. Compilation success remains to be observed in that work.

### P1 dispatch receipt

Native worker dispatch returned `/root/oracle_termpanum_x1`; requested model
`gpt-6.1-terra`, effort `high`, fresh context (`fork_turns: none`). Cycle 01 POINT
is the exact authority. This is an observed handle and dispatch configuration,
not an independent attestation of the serving model. Recovery queries that handle
and reconciles its actual RETURN/artifacts before resuming; no automatic duplicate.

P1 fresh witness dispatch returned `/root/witness_termpanum_x1_p1`; native worker
restricted to verification, requested `gpt-6.1-sol/high`, fresh context. Cycle 02
POINT defines the exact read-only artifact scope and two finding/RETURN outputs.

### P1 review disposition — 2026-10-30 18:45 CET

Cycle 02 REVISE is accepted as a finding. Candidate manifest
`fe981fa2f53d49279b276f59d487cb282ba6ec8d7f093bdffd6a32cc90cc9692`
is not accepted for capture. Head inference/operationalization of Q05: independently
measure release→completed append for every frame in each of 30 normal runs; retain
all 7680 samples, use each run's maximum as the 30-sample p95 population, and report
the global maximum. Fixed ≤500 ms p95 and ≤1000 ms max remain. This conservative
measurement exposes startup/tail delay without narrowing qualification; it is not
claimed as verbatim original wording or a new operator gavel. Remove universal
twice-replay and eight-class invalid-bundle count from mandatory Q; R owns those.
Q07 ten-per-mode mutations and Q09 nonzero rejection remain. No gate, ownership,
runtime effect or dependency amendment is needed for these specification repairs.

During verification, pulse.md changed concurrently: a phone-console-01-browser
router row was added. Termpanum's row/gate remains exact. This thread did not write
pulse in this window; preserve the concurrent row. The earlier blanket preservation
assertion failed for that file, so no all-files-unchanged claim is made.

### P1 accepted — 2026-10-30 18:49 CET

After independently witnessed correction, head ACCEPT freezes manifest
`627e2e30e1434b8e27c277ffc2a21d8f6120ba92a9aca12d863459a65f9fcf7c` (14 active members).
Cycle 03/04 VERDICTs record verification; raw/review.oracle.r2.md is the independent
PASS. Capture implementation may now begin within Gavel 1/2 and the exact builder
POINT. Runtime outcomes remain untested. Expected files are read-only to builder.

P2 dispatch returned `/root/builder_termpanum_x1`, native Astrobley configured
`gpt-6.1-sol/high`, fresh context. Cycle 05 POINT is the exact authority; expected
is read-only. Runtime recovery is runs/builder-05/runtime-index.json and the exact
per-run ownership manifests it cites. No serving-model attestation beyond route
configuration is claimed.

### P2 frame correction — 2026-10-30 19:01 CET

Head inspected first preflight manifest: runner PID 2, no tmux commands, no process
or generation entries. Independent tools reported different PID namespace inodes
(pid:[4026533271] versus pid:[4026533268]); PID/start alone cannot cross these
frames. Builder stopped suite (reported native exec exit 130) before source runtime.
Retain attempts and verify manifests. Head dispositions: record PID namespace in
identity, reject cross-namespace signaling/recovery, and use narrowly escalated
host-frame runtime if approved by execution sandbox. Existing Q effects remain;
this is no broader runtime or architecture release. No namespace mapping is inferred.

Narrow head read-only `require_escalated` probe returned exit 0: namespace
`pid:[4026531836]`, observed probe PID/NSpid `1768160`. Command only read
`/proc/self/ns/pid` and PID fields from `/proc/self/status`; no tmux operation.
This demonstrates host-frame access; each runtime still records and validates its
actual identities. Sandbox execution approvals are not inferred from another command.

### P2 partial return — 2026-10-30 23:43 CET

Cycle 05 returned partial and is BLOCKED at the execution boundary. Head directly
compared all three captured streams with their frozen cases: normal 262144 bytes,
burst 4194304, ONLCR 262656, all exact. Normal has 256 recorded timing samples and
a 1696445 ns maximum. These are pilot observations, not full qualification.
ONLCR cleanup remains unproven; v4 recovery command had no execution receipt after
an interrupted 618.4-second escalation wait. No approval rejection was reported.
The exact command, process identities, source hashes and unrun modes are retained
in 05.builder.return.md; the head VERDICT records limits and recovery order.
Both gavels remain effective; only the execution sandbox boundary is unresolved.
