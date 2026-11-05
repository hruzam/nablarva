# Termbrana

Termbrana's initial observer is a planned independent semantic observation, navigation,
and replay layer for terminal sessions, Zellij-first and read-only by default. The
composition family below is separate from this observer under flag L17.

> **Status — pre-product, Milestone 0 truth spike.** This repository currently contains
> a compiling Zellij 0.44.3 probe harness, not an installable semantic-navigation MVP.
> `termbrana-core`, the review UI, JSONL persistence, and replay are not implemented yet.

## Why

Terminal scrollback is visually linear. It does not normally preserve durable units such
as a prompt and answer, a tool run, an approval, an error with its context, or a bookmarked
test result. Termbrana intends to retain inspectable observations and derive semantic
blocks without turning the shell, agent, or orchestrator into an editor.

The product earns existence only if a user can return to a meaningful event faster and at
least as reliably as with native Zellij search and scrollback editing.

## Current host contract

| Area | Current truth |
|---|---|
| Host pins | Zellij and `zellij-tile` 0.44.3, Rust/Cargo 1.95.0, `wasm32-wasip1` |
| Code on disk | `termbrana-zellij` 0.0.0: a read-only M0 probe harness |
| Capture ceiling | Zellij plugins receive host-rendered strings/events: `rendered_text` or `rendered_ansi`, never `raw_pty` |
| Chosen MVP view | A side/tiled review pane; the overlay experiment was dropped |
| Chosen capture shape | Render-report events signal changes; full scrollback is pulled on demand. Burst cadence measured 2026-09-02 (self-feeding storm when subscribing to own pane; dozens of PaneUpdates per resize); per-call cost of repeated get_pane_scrollback remains unmeasured — see ADR-0002 L-A1/L-A2 |
| Observer safety | No writes, signals, or global input interception in the default product mode |
| M0 gate | **FROZEN 2026-09-02** — operator pad sat (8/8 fences), evidence folded, @Assay fresh-eyes PASS, ADR-0002 gaveled by majkee. Re-verification loop (pad.2-m0-loop) is due before M2 adapter code — ADR-0002 §Loop |

Zellij owns the PTY master, parses terminal control sequences, and constructs its terminal
model before Termbrana can observe it:

```text
shell or agent
    -> Zellij PTY + parser
    -> rendered pane strings / render-report events
    -> future termbrana-zellij adapter
    -> future termbrana-core
    -> review projection + append-only JSONL
```

This boundary means a plugin cannot reconstruct original PTY bytes, erased intermediate
states, or a pre-parser security record. A future `termbrana-pty` would have to allocate and
own the PTY from process start; that is a separately gated system, not part of the MVP.

### Provenance grades

| Grade | Meaning | Available now? |
|---|---|---|
| `raw_pty` | Bytes read by the process that owns the PTY master | No; future PTY experiment only |
| `rendered_ansi` | Host-rendered pane representation retaining ANSI styling | Runtime-confirmed 2026-09-02: reachable ONLY via PaneRenderReportWithAnsi subscription; get_pane_scrollback strips ANSI (ADR-0002 fact 1) |
| `rendered_text` | Host-rendered plain text | API path verified |
| `derived` | Blocks, highlights, filters, or summaries referencing parent observations | Planned in `termbrana-core` |

“Replay” means planned deterministic replay of retained Termbrana observations and derived
records from append-only JSONL. It does not mean byte-perfect terminal emulation, command
re-execution, or retroactive recovery of raw history. The candidate JSONL envelope is not
yet frozen.

## Build and load the probe harness

Prerequisites must match the pinned host contract:

```text
zellij 0.44.3
rustc 1.95.0
cargo 1.95.0
wasm32-wasip1
```

Build:

```bash
cargo build --locked --release --target wasm32-wasip1 -p termbrana-zellij
```

From a terminal pane inside an attached Zellij client, load the probe:

```bash
zellij action launch-plugin --floating --skip-plugin-cache \
  "file:$PWD/target/wasm32-wasip1/release/termbrana-zellij.wasm"
```

Approve the read-only pane/application/CLI-pipe permissions when prompted. `ReadCliPipes`
and the probe command channel exist only to collect M0 evidence; they are not planned MVP
permissions.

tmux was useful during the automated spike only as a stable real-PTY carrier for an attached
Zellij client. It is not a Termbrana dependency, capture protocol, semantic source, or replay
store. `zellij action dump-screen` can inspect terminal panes but returned no content for
plugin panes in the tested host, so final plugin rendering still needs an operator check.

## Product direction

The read-only MVP is intended to provide:

- terminal-pane selection and safe retargeting;
- live-follow and frozen review states;
- explicit-marker and generic semantic blocks;
- next/previous navigation, search, bookmarks, filters, collapse, and copy;
- visible source grade, target identity, and capture freshness;
- safe recovery when the source pane closes; and
- standalone operation with nabLarva completely absent.

The MVP does not include raw capture, sanitization claims, a transparent overlay, autonomous
command injection, global interception, or provider-specific policy in the core.

## Composition and explicit input direction

**Said — Majkee, 2026-10-20:** a "more flexible surface above sessions", with
"need send keys to tmux or anothe similar push type also" and text editors
"like sublime or lite XL"; "needs pipes and and also should be accessible from
agent assistant to inject parts there." These source words are retained here from
Majkee's direct product-direction messages of that date.

**Inferred — Astrobley, connective design reading:** composition is reusable
independently of a RUNBOOK bed, vault or editor. Those may attach to its workspace.
Human edits, Sublime Text/Lite XL, pipes and assistant calls can contribute prepared
text or parts through shared composition interfaces. Contributing a draft and
transmitting prepared output are distinct operations. Output needs explicit input/
push adapters, including tmux keys/text or another suitable target. A shared write
and target-binding policy must govern all clients; editing or body
text never implies submission or authority. Concrete APIs, storage, daemon, picker,
writer arbitration and delivery qualification remain open.

The Phase 0 parser is a reusable, byte-preserving inert validator beneath
this direction: no editor orchestration, instruction discovery/loading or sending.
The existing Zellij observer, M0/M1/M2 gates and benchmark are unchanged. Its default
is read-only; sending requires the separately enabled operator capability already
defined in [product law §2.4](research/termbrana.project-definition.md#24-read-only-first).
No adapter, writer or transmission is implemented or activated by this direction.
Retained observations remain append-only and provenance grades are not inflated.

There is a carrier seam with [flag L3/L4/L14](../../.dev/session/flag.md): tmux is
never the room protocol or truth, and send-keys was rejected as the regulated
injection leg because rendered screens cannot distinguish noise/final/interrupt
([founding comparison](../../raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md)).
The new push request is broader product direction; later carrier qualification and
any necessary lock reconciliation remain explicit gates. It does not approve tmux
as regulated transport or reopen the whole relay. L17 places human-operated
editor/pipe/tmux push outside that regulated protocol until qualified; assistant
draft contribution grants no autonomous sending authority.

**Source direction — said: Majkee, 2026-10-20:** code home
`~/ia-sync/zsh/termbrana/composer.zsh` with family scripts; "python if fast enough."
**Locked — L17, Majkee GO, 2026-10-20:** the reusable composition family lives at
`~/ia-sync/zsh/termbrana/`, with a thin zsh entry and independent Python stdlib
parser, conditional on measured responsiveness. Its [source-family README](../../../../ia-sync/zsh/termbrana/README.md)
and [GRAMMAR.md](../../../../ia-sync/zsh/termbrana/GRAMMAR.md) describe the source-only Phase 0 interface. The existing
Rust/WASM observer remains at `toolbox/termbrana/`; its M2 benchmark/stop-rule binds
only that observer. This supplements L11/L12 rather than changing its host contract
([L17/L11/L12/L16/L8′](../../.dev/session/flag.md)). Approved v4 is released only for
Phase 0 parser implementation and independent verification; no deployment or
later-phase activation follows.

**Phase 0 qualification — 2026-10-21:** the [retained exit finding](../../.dev/session/composer-01-parse/evidence/phase0.exit.cartan.2026-10-21.md)
links independent verification and the exact source receipt. This retained,
uncommitted evidence qualifies the finite office-only parser checks (Python 3.14.7),
not sourcing, editor integration or delivery. A durable qualification commit pin
awaits an actual, separately authorized preservation commit.

**Layering B — L17, amended by L21:** Termbrana composition and ovitmugen are independently useful
clients. See [flag L21](../../.dev/session/flag.md), adopted P5-b 2026-10-23, for shared layers
and a coherent UI framework; implementing, activating, delivering through or adopting a transport
for them needs its own separate release. Composition
works without ovitmugen, a RUNBOOK bed, tmux, editor or interactive shell. Ovitmugen
keeps view/layout and protected process-lifetime ownership; discovery is not delivery
authority. Future sending needs complete checked target binding and explicit operator
authority through a common write/target policy. Control text and payload bytes stay
distinct; existing tmux helpers/probe pipes establish neither packet fidelity nor
raw-PTY provenance. Shared-layer owner/home/API and carrier qualification remain open.

**Future adjustable sources — L17; Majkee direction, 2026-10-21:** common
programs/controller tables, germline, actual vendor agent/roster/skill shapes and
SPECIAL, including germline/pipes, are first-class generation-X sourcing requirements.
Coverage may span additional sourcing gates; these capabilities are planned, not
implemented. Each source needs a configurable location and format reader, preserving
source/kind provenance. Selected text or references are prepared before composing
the opaque body. Native activation/launching stays explicit; definitions do not
activate themselves. No loader, picker or shared selection API is implemented here.

The five continuing integration constraints are independent core/optional edges;
observer, retained-record and provenance safety; contribution distinct from
transmission; qualified carriers with required lock reconciliation; and explicit
shared-layer/publication ownership. Python needs latency evidence. Locate temporary
acceptance work and current decisions through the standing [pulse router](../../.dev/session/pulse.md)
and its owning session's RUNBOOK/STATUS, not a durable dependency on a particular bed.

## Roadmap and gates

| Milestone | State | Exit gate |
|---|---|---|
| M0 — host truth spike | **Frozen 2026-09-02** (ADR-0002) | Done — see ADR-0002; loop pad.2-m0-loop due before M2 code |
| M1 — pure core | Not started | Deterministic model, block index, navigation, bookmarks, JSONL replay, and host-independent tests |
| M2 — read-only Zellij MVP | Not started | User workflow works without nabLarva and passes the pre-registered benchmark |
| M3 — beta hardening | Conditional | Opens only if the M2 benchmark passes |
| M4 — nabLarva adapter | Optional/later | Neutral boundary exists and M2 remains standalone when disconnected |
| M5 — PTY owner experiment | Parked | Separate ADR proves a raw-byte or pre-parser need that composition cannot meet |

The M2 benchmark is frozen at five real sessions and fifteen retrieval tasks. Median
time-to-locate must be at least 30% lower than native Zellij, with success rate at least
equal to native. Otherwise development stops at M2 and preserves the probe and core work.

## Repository map

- [`DECISIONS.md`](DECISIONS.md) — append-only product-technical ADRs.
- [`research/termbrana.project-definition.md`](research/termbrana.project-definition.md) — adopted product laws, boundary, domain model, and success criterion.
- [`research/termbrana.execution-plan.md`](research/termbrana.execution-plan.md) — adopted r0 milestone plan; current status is superseded by later evidence.
- [`research/termbrana.addendum-to-foil-theory.md`](research/termbrana.addendum-to-foil-theory.md) — corrected Zellij/PTY/security boundary.
- [`research/evidence/`](research/evidence/) — M0 API, build, runtime, fidelity, input, geometry, and performance evidence.
- [`research/foil_theory.md`](research/foil_theory.md) and [`research/foil_plugin.rs`](research/foil_plugin.rs) — research history, not production substrate.
- [`crates/termbrana-zellij/src/main.rs`](crates/termbrana-zellij/src/main.rs) — current probe harness.

## Development and governance

Structural, topology, ownership, and scope decisions live in nablarva
`.dev/session/flag.md` (L11). [`DECISIONS.md`](DECISIONS.md) holds product-technical ADRs
only, and every entry cites the authorizing flag line or central session brief.

Termbrana deliberately has no local `AGENTS.md`, Claude/Codex roster, harness, devenv twin,
or beacon. Development sessions run from the central nablarva harness under
`.dev/session/`, with one integration owner. Historical observer beds retain
`toolbox-termbrana-*`; operator-directed generation-X composition includes names
such as `termbrana-X1-composer-sourcing`, each requiring its own scope and launcher
authorization. Parallel agents may perform
bounded, preferably read-heavy work after the applicable gate; shared conclusions and domain
types flow through the owner or an ADR.

For Codex, Cartan remains the controller and routes bounded work to the global
`architect`, `challenger`, `researcher`, `implementer`, and `verifier` roles. Termbrana
adds its Zellij, terminal, and PTY context through the task brief and evidence files; it
does not clone or modify those global agent definitions.

For the observer's frozen host contract and remaining qualification limits, read
[ADR-0002](DECISIONS.md#adr-0002--m0-host-contract-frozen). Before the first M2
adapter code, complete its required re-verification loop. Locate active work through
the standing [pulse router](../../.dev/session/pulse.md) and the owning session's STATUS.
