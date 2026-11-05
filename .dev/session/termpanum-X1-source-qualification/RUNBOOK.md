# RUNBOOK: termpanum-X1-source-qualification

```yaml
goal: >-
  Establish the supported behavior and limits of one output-only tmux source through
  independent expectations, retained captures and reproducible comparisons.
gate: >-
  Majkee records GO or STOP on an independently witnessed qualification packet for one isolated synthetic tmux output source, comparing capture with frozen post-termios byte expectations and separate rendered-state expectations, with the approved failure, freshness, identity and timing cases accounted for.
participant_1: {seat: cartan-termpanum-x1, brand: codex, model: gpt-6.1-terra, effort: high, host: office, role: working head and sole STATUS owner}
participant_2: {seat: oracle, brand: codex, model: gpt-6.1-terra, effort: high, host: office, role: independent expected-corpus author}
participant_3: {seat: builder, brand: codex, model: gpt-6.1-sol, effort: high, host: office, role: Astrobley fixture and capture implementer}
participant_4: {seat: witness, brand: codex, model: gpt-6.1-sol, effort: high, host: office, role: fresh independent verifier; never fixes}
participant_5: {seat: majkee, brand: human, host: office, role: exact runtime release and final GO or STOP}
status_owner: cartan-termpanum-x1
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/termpanum-X0-source-contract.cartan.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X2-builder-narative.cartan.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-10-23.agol.md
```

## Why this session exists

X2 delivered the approved build plan; Termpanum X0 delivered its accepted documentary
source contract. This is Q, the first source-qualification experiment. Its result is an
inspectable evidence packet, including a meaningful failure if the proposed source cannot
meet the declared requirements. It is not the collector product, live view or delivery system.

The selected source is tmux `pipe-pane -O` on a synthetic pane, with `capture-pane` used
only for a separate rendered-state comparison. Source bytes, rendered paint and inferred
meaning remain distinct. The accepted source contract owns the detailed test requirements.

## Authority, numbering and wake

Said: Majkee, 2026-10-30: “I am authorizing RUNBOOK.” After the numbering clarification
and proposed rename to `termpanum-X1-source-qualification`, he said: “I agree, you have my
blessing.” This authorizes the rename and launcher preparation. The completed X0 bed is
`/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/`.

The dated entry brief in this bed remains verbatim historical input: its X0 qualification
name and old self-path are superseded by this header. The old proposed Q path ending
`termpanum-X1-source-fixture` also resolves operationally to this X1 assignment; behavioral
acceptance and original approved artifacts remain unchanged.

The recommended next seat is Cartan in Medusa posture on GPT-6.1-Terra/high: it maintains
one STATUS and coordinates the bounded bodies. Oracle and witness are independent of the
capture builder. Astrobley/Sol is justified for the PTY/termios and process-lifetime work.
Model tuples are requested carriage, not claims about an observed runtime. Record actual
role/route/model/effort at dispatch; return a mismatch rather than editing the harness.
Use native bounded worker/verifier routes for those roles, and native Astrobley for builder.
This authoring turn starts no executor. No multi-session cSharp arc is newly invoked here.

## P0 through P4 — one session, one final gate

| Phase | Work and exit evidence |
|---|---|
| P0 — entry and exact release | Head resolves current frame, frozen inputs and Q prerequisites. Write `raw/entry-and-release.md`: current paths/hashes, bounded decision lookup, acceptance mapping, proposed language/dependencies/effects and actual operator receipt. Documentary work only until the release is complete. |
| P1 — independent expectations | Oracle authors the expected corpus and generation specification. Fresh witness checks the post-termios calculations, rendered case, controls, measurement schedule and hashes in `raw/review.oracle.md`. Head ACCEPT freezes it before any capture implementation. |
| P2 — fixture and capture | Builder implements only the released Q helpers and isolated runner; records commands, ownership, cleanup and pilot evidence. A pilot cannot replace the fixed acceptance corpus. Expected files are read-only to the builder. |
| P3 — witnessed qualification | Witness inspects source/oracle independence and runs the declared matrix on the owned private fixture, recording actual results, failures, invalid runs and limits in `raw/review.qualification.md`. Builder repairs through a new bounded cycle; old runs and findings remain. |
| P4 — decision and transfer | Head checks evidence and writes `raw/qualification-summary.md`; Majkee records GO or STOP in `raw/decision.majkee.md`. Then preserve the packet, transfer any remaining work, promote process observations and close the router entry under the shared closure rules. |

These are work phases, not additional session gates. A valid STOP can close the gate with
an honest independently checked packet; missing execution authority alone is not a runtime
qualification result. If P0 remains unresolved, keep the gate open and hand Majkee the exact
missing decision. Do not restart the completed X0 research pass indefinitely.

## P0 release boundary — concrete scope to present

P0 may read public project documents, inspect files/git, hash accepted artifacts, check
installed executable paths/versions and author the bounded release packet. It must not
start or contact a tmux server, execute a fixture, implement Q code or launch vendor CLIs.

Before P1, the head must verify a recorded applicable L14 D4 verdict **or** Majkee's explicit
Q-only exception naming the effects below. It must also verify a release of the helper
language/dependencies. Reuse an already applicable receipt; do not ask twice. The authoring
blessing above is not an explicit D4 exception. No broad product or delivery release follows.

Recommended request, pending that decision:

- Q-only helpers use the installed Python 3 standard library, with zsh only for explicit
  command entry where needed, and the existing tmux 3.7c binary. No package installation,
  dependency download, vendor SDK, daemon or global configuration change. Record actual
  paths/versions/binary hashes at entry; version drift returns a concrete disposition before
  executing. This local choice decides neither animal language docket 2 nor C's product stack.
- Code and retained evidence are restricted to this bed's `expected/`, `src/`, `runs/`,
  `raw/` and `_bus/` assignments below. Only the head writes STATUS and its router row.
- Runtime uses one newly allocated private directory per run, matching
  `/tmp/tq-<uid>-<unique-id>/`, containing `tmux.sock` and temporary control files. The
  runner records its exact directory/socket before spawn, checks the socket path fits the
  platform limit, and refuses an existing socket/directory or any unbound identity.
- Every tmux command uses that exact `-S` socket. Start with `-f /dev/null`, fixed 80x24
  dimensions and a controlled environment. Never use the default server, a foreign socket,
  user's tmux config, login startup, selection-following, hooks or a living agent pane.
- Launch the synthetic fixture as the pane's command. It emits only synthetic nonsecret
  data and waits for an out-of-band owned control signal until capture is ready. No
  `send-keys`, `pipe-pane -I`, terminal-input injection or live CLI/session contact.
- Allowed failure actions affect only that run's owned reader/sink/source/server processes:
  pause/resume, terminate, disconnect/rebind and recreate on the private socket. Record
  process starts and identities before acting. A 15-second watchdog bounds each run;
  verify cleanup of all owned processes, retaining evidence even after failure.
- Temporary socket/control cleanup is restricted to exact proven-owned paths after process
  exit; never delete retained run bundles. No kill-all/pkill pattern, global tmux shutdown,
  commit, push, deploy, shared-record write or foreign-session edit is released.

The packet must quote the actual permission/exception, identify its author/date/scope and
show which of these effects it covers. A candidate request is not a receipt. The witness
checks this release before any qualification run. Any wider effect returns to the head.

## Ownership and expected artifacts

All relative paths below are relative to `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/`; the head's POINT uses absolute paths.

| Owner | Exclusive writing scope |
|---|---|
| Head | `STATUS.md`, own numbered `_bus/NN.cartan-termpanum-x1.point.md` and `.verdict.md`, `raw/entry-and-release.md`, `raw/qualification-summary.md`, `raw/decision.majkee.md`, closure/experience records and only this session's pulse row |
| Oracle | `expected/` and own `_bus/NN.oracle.return.md` |
| Builder | `src/fixture/`, `src/collect/`, `src/compare/`, builder's uniquely allocated `runs/<run-id>/` and own `_bus/NN.builder.return.md` |
| Witness | `raw/review.oracle.md`, `raw/review.qualification.md`, uniquely allocated witness `runs/<run-id>/` and own `_bus/NN.witness.return.md`; corrections use new review filenames/cycles |

`expected/` contains `wire.bin`, `screen.txt`, `observations.ndjson`, `schedule.md` and
`manifest.json`; distinct variants may live in `expected/cases/<case-id>/` with every file
and schedule pinned by the manifest. The oracle's specification explains calculations and
hand-checked examples independently of collector output. Do not derive expected bytes by
capturing the system under test. Builder fixes never silently regenerate expected results.

Each run retains immutable input/criteria hashes, versions, identities, termios before/after,
argv, clock basis, source coverage, `capture.bin`, independent `fixture-control.ndjson`,
comparison/report output, stderr, exit and cleanup evidence. The oracle defines the local
expected observation vocabulary; it is not an adopted shared schema or task-state vocabulary.
Tests use direct child exit/control evidence, not prompt text, to distinguish quiet from gone.

No directory is pre-created merely to fill this table. `_bus/` begins at the first actual
delegated cycle. A POINT gives one owner, exact write paths, release receipts, done-when and
an absolute RETURN path. A RETURN alone is not acceptance: the head checks its artifacts
and records a VERDICT before advancing STATUS. Workers are not alone in the repository;
preserve unrelated changes and one another's owned files.

## Acceptance mapping — scope Q, retain later-package boundaries

The normative input is
`/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/source-contract.md`
(§Corrected independent oracle and planned measurements), read with the package labels in
approved plan §4. P0 freezes a row-by-row Q mapping; it may not relax a threshold after a run.

| Q evidence | Required check |
|---|---|
| Provenance and byte oracle | tmux 3.7c binary/tag/hash; server/socket and process incarnation; exact interval; OPOST-off and separate OPOST+ONLCR case; independent post-termios expected bytes; before/after termios; unexpected change invalidates run |
| Rendered cross-check | Independently frozen short 80x24 screen sequence and exact capture options; separate from binary burst and never a replacement for byte fidelity |
| Healthy capture | 30 normal runs of 256 x 1024-byte frames every 10 ms; 30 burst runs of 4096 x 1024-byte frames; exact bytes and zero missing/duplicate/reordered frames; retain chunking without calling it message boundaries |
| Timing | Sorted sample 29/30 is p95; normal reader visibility p95 <=500 ms/max <=1000 ms; ready <=1500 ms; normal capture <=6 s, burst <=10 s, per-run watchdog 15 s; use independently timed markers and actual reader-visible append |
| Quiet/false completion | 30 fake-Done/prompt-looking cases, alive and quiet for 5 s before independently timed exit; no semantic completion or acceptance inferred from paint or EOF |
| Failure/coverage | Ten cases per applicable failure mode: owned sink loss, reader paused 3 s, disconnect/reconnect, deliberately deleted/duplicated/reordered replay frames; explicit gap/error/incomplete or measured narrowed coverage; directly supervised detection <=1 s, watchdog 15 s |
| Identity/freshness | Ten pane recreate and ten fresh-server cases; late attach marks earlier coverage absent; reconnect requires rebind; old run/receipt timestamps cannot become fresh through a new reader |
| Independence and repeatability | Frozen expectations predate capture implementation; witness reruns actual cases and verifies nonzero rejection/reason for mismatched or incomplete Q bundles; retain every failed/invalid run and original criteria |

The fixture comparator is Q-local verification. Product C heartbeat/health, R's public
inspect/replay/report invocation benchmarks, L's view refresh/lifetime cases, E packaging
and V shared admission remain later packages. Mark them deferred with their package owner;
do not implement those products to make this Q packet look complete. A failure or version
mismatch is reported honestly; narrowed qualification needs an explicit reason and operator
decision, with the original failed bar preserved.

## prompt-0 — working head

```text
Enter /home/hruzam/unikuklatrix/nablarva as cartan-termpanum-x1.
Read AGENTS.md, .dev/session/flag.md, .dev/session/pulse.md and PROJECT.yaml in that order,
then /home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/RUNBOOK.md
and /home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/STATUS.md.
Adopt the sole STATUS pen; inspect actual files and preserve all foreign changes.
Start P0 only: verify the accepted input hashes and current Q release evidence; produce
/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/raw/entry-and-release.md
with the exact scope, criteria mapping and concrete decision still needed, if any.
Do not infer a D4 exception from RUNBOOK authorization or start runtime work without its receipt.
Once released, assign oracle first, have a fresh witness accept and freeze expected hashes,
then assign the separate builder. Keep bodies delegated and inspect returned evidence.
Use the phase and ownership tables above. Before every spawn/action, record the current
in_flight and an exact recovery probe; update it after checking the result. On material
ownership/API/authority change, return the bounded question to Majkee; never absorb X5.
Give Majkee a short next move with its practical consequence. Stop at the final GO/STOP,
retain evidence and close only your router row under the referenced closure rules.
```

## prompt-1 — oracle

```text
Work only on the absolute paths assigned in Cartan's POINT under
/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/expected/.
Read that bed's RUNBOOK, actual release receipt and the accepted X0 source contract.
Author independent expected bytes, screen and observation cases, schedule and hash manifest.
Specify post-termios transformations, control/exit evidence, workload and measurement bounds.
Use the released helper language only; never generate expectations from capture-under-test.
You do not implement the collector or edit another seat's files. You are not alone; preserve
others' work. Return evidence and uncertainty at the absolute RETURN path in your POINT.
```

## prompt-2 — builder

```text
Act as Astrobley on the exact Q fixture/collect/compare and unique run paths assigned by
Cartan under /home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/.
Read its RUNBOOK, actual release receipt and witness-accepted frozen expected manifest.
Do not start capture implementation before that acceptance. Keep expected/ read-only.
Implement the minimal isolated Q helpers, immutable bundles, failure reporting and owned cleanup.
Every tmux call names the proven-owned private socket; no living session, default server,
input injection or shared substrate write. Return source/evidence hashes, commands and limits.
You are not alone in the codebase; preserve other writers. Consequential changes go to Cartan.
```

## prompt-3 — witness

```text
Act independently of oracle/capture author for the specific stage assigned by Cartan in
/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/.
Read the RUNBOOK, original acceptance criteria, actual release receipt and current POINT.
At P1, check independent calculations/coverage and freeze expected hashes before builder work.
At P3, inspect the actual code and run the released fixture matrix on your own unique run paths.
Check isolation, observations, metrics, retained failures and cleanup; record each unknown.
Never repair source or expected files. Return PASS/REVISE/STOP with paths, counts and limits
in your assigned review and RETURN. Test the head's STATUS claims against actual artifacts.
```

## Recovery and holds

Before runtime, STATUS recovery is documentary: inspect the receipt's actual wording and the
oracle acceptance, reconcile POINT/RETURN/VERDICT contents, and verify manifests against bytes.
An absent receipt means no runtime release; directory presence alone never proves execution.

Before each runtime action the head records the exact run directory, socket and PID/start
identities in STATUS or a cited run manifest. Recovery first inspects those records and OS
process identity. If ownership is proven, query only that recorded private socket for pane
identity and `pane_pipe`, and compare with independent child/control/exit evidence. A capture
file alone cannot prove the pipe lives. Unknown/reused identity forbids signaling and capture
continuation. After interruption preserve the partial run as incomplete; restart under a new
run ID only after reviewing and cleaning proven-owned survivors. No generic default-socket probe.

No `.hlm/`, `.majkee/`, private histories, secrets or environment dumps. No product code outside
this bed, live provider experiments, package installation, transport, deployment, canon edit,
foreign STATUS edit, automatic prune or commit. Explicit scoped later authority is recorded,
not inferred. Keep source generation, observation, controller decisions and actuation distinct.

X5 owns its read-only spine contract, registry and shared-record work. Its RUNBOOK explicitly
leaves Q to this line. Coordinate a possible later producer use through Majkee with exact
paths and evidence; this qualification assigns no shared producer or lifetime ownership.
X4's recorded startup HELLO experiment is separate evidence; it does not qualify this capture.
Current architecture r8 replaces older handoff descriptions of documentary lag. No X5
completion is imposed as a prerequisite for this isolated Q test.

## Process lessons carried into this launcher

- U1: each approval names its subject/effects; no naming lock becomes producer ownership.
- U2: absolute roots, explicit corpus membership, pinned reviewed bytes and checked RETURNs.
- U3: revise from disk, declare every change and retain older generations. Rebrief a lost child
  from its actual POINT/RETURN/VERDICT; no promise that an old handle survives.
- U4: verify source bytes at any claimed preservation commit. Uncommitted X2 evidence remains
  retained; publication/preservation debt does not authorize silently committing it here.

These apply the 2026-10-23 harvest to this work; they create no global rule or new gavel.
At closure classify every raw keeper, transfer surviving findings, promote process observations
before any separately authorized prune, and perform the guide's triggered harvest. Keep the
next head's practical handoff distinct from Cartan's global therapy record.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/raw/brief.entry.cartan.2026-10-25.md` — historical entry brief; numbering superseded above.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md` — approved sequence and package-scoped bars; SHA-256 `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/decision.majkee.plan-go.2026-10-22.md` — exact plan GO.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/source-contract.md` — accepted source packet; SHA-256 `7086e59527c77040be9d41ee94966f661dd751c009e5eb636590db103dd32694`.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/research-disposition.md` — dated bounded D4 search and proposed Q; SHA-256 `b2cad9dabcaa62a47440c4e235548e42f8812c0b1183febecda8d05659aebc80`.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-contract/raw/decision.majkee.packet-acceptance.2026-10-22.md` — documentary acceptance, no execution release.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/handoff.csharp-method.cartan.2026-10-24.md` — technical intent and cooperation hints, advisory.
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md` — current seams and owners; read with current flag.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X5-spine-slice/RUNBOOK.md` — Q boundary and potential later producer coordination.
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` — launcher and closure law.
- `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` — sole doing-state and recovery.
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` — verified delegated exchange.
