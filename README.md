# Termbrana

Termbrana is a planned independent semantic observation, navigation, and replay layer
for terminal sessions. It is Zellij-first and read-only by default.

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
| Chosen capture shape | Render-report events signal changes; full scrollback is pulled on demand. Burst cadence, debounce, and repeated-call cost remain unmeasured |
| Observer safety | No writes, signals, or global input interception in the default product mode |
| M0 gate | Not frozen: operator pad steps 1–5, evidence folding, and an independent fresh-eyes pass remain |

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
| `rendered_ansi` | Host-rendered pane representation retaining ANSI styling | API path verified; exact runtime semantics still partly operator-pending |
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

## Roadmap and gates

| Milestone | State | Exit gate |
|---|---|---|
| M0 — host truth spike | **In progress** | Finish the operator pad, fold T0.2–T0.5 evidence, independent review, then freeze the host contract |
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
`.dev/session/toolbox-termbrana-*`, with one integration owner. Parallel agents may perform
bounded, preferably read-heavy work after the applicable gate; shared conclusions and domain
types flow through the owner or an ADR.

For Codex, Cartan remains the controller and routes bounded work to the global
`architect`, `challenger`, `researcher`, `implementer`, and `verifier` roles. Termbrana
adds its Zellij, terminal, and PTY context through the task brief and evidence files; it
does not clone or modify those global agent definitions.

The next concrete step is the operator pad at:

```text
~/unikuklatrix/nablarva/.dev/session/
  toolbox-termbrana-02-m0-truthspike/pad.1-m0-runtime-confirm.md
```
