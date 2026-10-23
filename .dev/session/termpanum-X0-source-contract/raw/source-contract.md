# Termpanum X0 — source contract

2026-10-22 · documentary packet · **all qualification below is planned**.

## Scope and source identity

| Subject | Identity / dated source | What it establishes here |
|---|---|---|
| Target subject | local `tmux -V` observed 2026-10-22: `tmux 3.7c`; pinned target, not a claim about the latest release | The first question is version-scoped to tmux 3.7c. A Q run must record its actual binary, tag and hash again. |
| tmux primary manual | [tmux 3.7c `tmux.1`](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1), checked 2026-10-22 | A tmux session is a collection of PTYs and each pane is a separate PTY. `pipe-pane -O` connects pane output to the command stdin; `-I` writes into the pane and is excluded. `capture-pane` emits the pane screen/history representation, with options that alter that projection. |
| PTY primary reference | [Linux `pty(7)`](https://man7.org/linux/man-pages/man7/pty.7.html), checked 2026-10-22 | Master/slave directions are bidirectional and asynchronous: slave writes become readable at the master, while master writes are terminal input. |
| termios primary reference | [Linux `termios(3)`](https://man7.org/linux/man-pages/man3/termios.3.html), checked 2026-10-22 | `tcgetattr` exposes terminal flags and control characters; `OPOST` controls output processing and `ONLCR` transforms NL to CR-NL. |
| Accepted local source finding | `.dev/session/nablarva-X2-builder-narative/raw/research.tmux-source-fidelity.2026-10-22.md`, SHA-256 `3abd43ac5b8f4b22cc5236f6e836c5503969356cde935482d35a7e50699075f7` | Dated source research and the corrected post-termios oracle; no server or fixture result. |
| Approved assignment | `.dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md`, SHA-256 `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145` | The proposed Q workloads, measurements, ownership and release boundary. |

The candidate source is prospective `pipe-pane -O` pane output. It is not an
adapter-owned PTY, terminal input, an inherently durable journal, or a completed runtime
qualification. `capture-pane` is a separately specified rendered-state cross-check at fixed
80×24 and fixed options; it never substitutes for the byte oracle. Control-mode `%output`
is a distinct escaped text protocol and remains an alternative/cross-check, not the source
contract for this first qualification.

## Observation contract and limits

For a released Q, source provenance must bind the tmux server/socket incarnation, pane ID,
process-start identity, actual tmux binary/tag/hash, terminal dimensions and the declared
start/end interval. Pane names, indexes and a bare pane ID are insufficient through
reconnect, destruction or server restart. Attach late and record coverage before attachment
as absent. A reconnect is a discontinuity until a new binding succeeds.

`pipe-pane -O` is expected to preserve an observed pane-output sequence only within the
declared interval. Wrapper sequence numbers prove receipt ordering after observation, not
loss before observation. The qualification must retain chunking without treating writes or
chunks as messages. Sink-child exit, buffering, write atomicity, loss under pressure and
retention after failure have no claimed guarantee here. A sink failure, capture discontinuity,
unexplained byte mismatch, duplicate/reordered frame, unknown identity or stale observer
must remain a gap/error/unknown or narrowed coverage; none may become clean success.

Freshness is not inferred from output silence. A quiet source can be known alive when an
independent fixture control and direct child wait status prove it. EOF/close and text such as
`Done` are neither helper exit nor task completion. The PTY reference describes asynchronous
flow, so the proposed visibility bound below is not a power-loss durability, source-time or
vendor-computation guarantee.

## Corrected independent oracle and planned measurements

The oracle author and collector author are different, sequential assignments. Before
collector work, a head/fresh verifier checks and pins expected corpus, schedule and
hand-calculation/reference-generation specification hashes. Byte equality is against the
**expected PTY-master stream after declared slave line discipline**, never directly against a
helper `write()` payload across an unrecorded terminal boundary. The fixture records
`tcgetattr` flags/control characters immediately before and after emission, terminal size,
helper and payload hashes, and actual tmux binary/tag. Any unexpected termios change
invalidates that run; it does not indict tmux.

The planned corpus has one `OPOST`-off byte-fidelity configuration and a separate deliberate
`OPOST|ONLCR` case whose independent expectation contains NL→CR-NL. It includes frozen
CR/LF, NUL, backslash, ANSI and split-escape subcases. Fixture-control acknowledgements,
monotonic emission times and direct child wait status remain independent of captured text;
the fixture requires no typing or injection.

| Planned workload or case | Exact proposed measurement / acceptance bound |
|---|---|
| Normal | One pane and one private socket/server on office: 256 numbered 1,024-byte frames every 10 ms (256 KiB). Thirty fresh process invocations; sort each metric and take sample 29/30 as p95; retain maximum and every run. |
| Burst | 4,096 numbered 1,024-byte frames (4 MiB), no deliberate pacing; thirty fresh invocations. Rendered testing is a separate short frozen screen sequence, never this binary burst. |
| Healthy fidelity | Across all 30 normal and 30 burst runs, exact bytes within the declared interval and zero missing, duplicate or reordered numbered frames. |
| Visibility and invocation | Helper marker release to completed reader-visible file append: p95 ≤500 ms, max ≤1,000 ms on normal. `zsh -f` start through exit plus readable complete `inspect`/`replay`/`report` result: p95 ≤1,500 ms, max ≤3,000 ms for 256 KiB, 30 each. Capture start to bound source/ready metadata ≤1,500 ms; normal whole capture ≤6 s; burst ≤10 s; watchdog 15 s. |
| False completion | Fake `Done` and prompt-looking paint, then alive and quiet for 5 s before separately timed exit: all 30 report quiet/known-alive where independently proven, never `task_completed`, `accepted`, or `turn ended`. |
| Observer health | Planned collector heartbeat every 250 ms. If age exceeds 1 s, a view marks stale/unknown by its next 250 ms refresh (≤1.25 s from last healthy heartbeat). A new reader cannot renew old timestamps. Inject 3 s delayed/out-of-order records and retain receipt and observation times. |
| Sink, pressure and loss | Kill only the owned sink halfway through burst; pause the owned reader 3 s; disconnect/reconnect capture; delete/duplicate/reorder a replay frame. Ten runs per failure mode. Each ends incomplete/gap/error or measured narrowed coverage, never clean success. Directly observed supervised failure is detected ≤1 s; hard stop 15 s if progress/exit is not established, retaining timeout/unknown. |
| Identity reuse | Ten destroy/recreate cycles with repeated pane names/indexes and ten fresh-server cycles. Zero inherited fresh state or silent cross-incarnation continuation. Failure to bind is unknown. |
| Replay/rejection | For every retained case, replay twice with pinned code/config and compare exact normalized observations/report data to independent files; report-generation timestamps are outside normalization. Ten stale/malformed/reuse cases each: metadata/capture/sequence mutation, truncation or unsupported version must reject nonzero and retain a reason. |
| Later view lifecycle | Planned source→file→projection update p95 ≤750 ms, max ≤1.25 s under normal workload; 250 ms refresh. Ten close/reopen cycles leave source/collector running; two readers cannot refresh collector health. This is L work, not released by D. |

Record host/kernel, binary versions/hashes, source boundary, dimensions, entry argv and an
environment allowlist plus load context; do not dump the environment or secrets. Retain every
failing, invalid and timed-out unique run with expected hashes, exact argv, stderr and original
criteria. A retry never overwrites a failure. All corpora are synthetic and nonsecret.

## Local proposed evidence shape

This is prose for a local test/product data shape, not an API or animal-wide event schema:

- immutable `manifest.json`: identities, versions, clocks, termios, expected hashes and coverage;
- `capture.bin`; collector-owned `records.ndjson`; independent `fixture-control.ndjson`;
  atomic `health.json`; `comparison.json`; and `report.md`;
- records carry run/source/incarnation, sequence, observed and received times, kind,
  provenance, certainty and evidence references; unsupported and ambiguous facts are explicit
  unknowns.

Raw bytes and records remain distinct, with one owner per file. This creates no `vist.*`
event, approved four-state vocabulary, producer topology, collector-lifetime owner or shared
consumer contract. Local C/R/L paths and their homes/language remain later releases.

## Distinct legacy constraints and scoped Termbrana evidence

All local links in this section resolve from this file under repository root
`/home/hruzam/unikuklatrix/nablarva`.

- **SOURCE — struck hooks stop rule:** the [original Termpanum brief](../../toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md)
  FALSIFICATION GATE says to stop building the PTY tap when hooks/records cover every state.
  The [lab DESIGN](../../../../meshup/lab.observability-probes.2026-08-01/DESIGN.md) records
  that `#gate` as struck on 2026-10-02 because it made the PTY floor conditional on vendor
  features; the [registry](../../../../meshup/REGISTRY.md) agrees. This old stop rule is stale
  and inoperative.
- **SOURCE — D4 remains binding:** [flag L14](../../flag.md) retains research before dependent
  build, mapped to the `relay-00-research` verdict before `relay-01-pty` and
  `relay-02-tracker`. The older lab header's phrase “research gate precedes any RUNBOOK” is a
  different historical wording. **INFERENCE — X2's approved documentary authorization:** it
  permits this finite preparation, but neither it nor the struck hooks rule waives D4 for Q/C.
- **SOURCE — Termbrana ceiling is version-scoped:** [ADR-0002](../../../../toolbox/termbrana/DECISIONS.md)
  freezes its M1/M2 host contract to Zellij 0.44.3, rustc 1.95.0, `wasm32-wasip1`, and
  `zellij-tile = 0.44.3`. Its plugin source ceiling is `rendered_ansi`/`rendered_text`, never
  `raw_pty`; target-only subscription, own-pane exclusion, debounce and tab re-sync are adapter
  laws. These are Termbrana observer facts, not a tmux qualification or a source-grade transfer.
- **SOURCE — Termbrana M2 limit:** ADR-0002 requires its re-verification loop before first M2
  adapter code: re-prove pins on the leading host, STOP and issue ADR-0003 on pin drift, then
  address explicitly unexercised fidelity/visibility cases. Its L11 M2 time-to-locate bar is
  scoped to that observer. **INFERENCE:** no parity, raw-PTY capability or qualification is
  inferred for a newer installed Zellij, nor for the tmux candidate here.

## Method choice and releases owed

**Recommendation: ADOPT the narrow lab method**—capture, retain, replay and compare one
prospective version-scoped `pipe-pane -O` source, with independent post-termios byte and
rendered-screen expectations. It reuses tmux's own pane PTY without claiming ownership or
durability. `capture-pane`-only is rejected for Q because a snapshot cannot establish original
output completeness; control mode is deferred because its escaping, pause/reconnect and
client-scoped discontinuities add a second contract; a new PTY owner or Zellij adapter is
deferred because it changes ownership/effects before the small source question is answered.

The distinct struck hooks stop rule, the older “before any RUNBOOK” wording, and L14 D4 are
recorded above rather than merged. L13 only names the observation lab Termpanum.

Runtime qualification, source behaviour, coverage, sink-failure reporting and every threshold
above are planned. Q needs a recorded applicable D4 verdict **or** Majkee's explicit recorded
exception naming the exact Q effects, plus a separate Q assignment and the fixed independent
oracle. Relative to repository root `/home/hruzam/unikuklatrix/nablarva`,
`Q = .dev/session/termpanum-X1-source-fixture/`; it is proposed only and this packet does not
create it. The Q oracle author owns exactly
`Q/expected/{wire.bin,screen.txt,observations.ndjson,schedule.md,manifest.json}` and freezes
its hashes before collector work; a different implementer owns
`Q/src/{fixture,collect,compare}` and `Q/runs/<run-id>/`. Before any Q execution, the
experimental helper's language and dependencies must be separately and explicitly released
for Q, without deciding animal docket 2. That release is not selected here, installs nothing,
and cannot release C. C later also needs its own product-build disposition,
home/language/local-record-contract authority. No execution release is supplied here.
