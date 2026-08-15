`source: ~/.remote/harvest · author: Wave r0 2026-08-15 · adopted: flag L11 2026-08-15 · role: founding canon`

# Termbrana — Addendum to the Foil Theory

**Status:** Draft r0  
**Date:** 2026-08-15  
**Purpose:** Preserve Nabla's original Foil exploration while correcting the product boundary before implementation.  
**Working name adopted:** **Termbrana**

---

## 1. Why this is an addendum rather than a rewrite

The original `foil_theory.md` and `foil_plugin.rs` are useful research artifacts. They expose the terminal substrate, distinguish byte streams from rendered cells, and identify projection, permissions, backpressure, and escape-sequence risk as important concerns.

They also combine several systems that have different trust boundaries and implementation sizes. Rewriting those files in place would erase how the idea developed. This addendum keeps them as evidence and establishes the corrected interpretation under the name **Termbrana**.

Termbrana is not merely a renamed Foil. The rename marks a boundary decision:

> **Termbrana is an independent semantic observation and navigation layer for terminal sessions. NablaRava is one optional consumer of Termbrana's outputs.**

---

## 2. What remains valid

The following ideas from the Foil exploration remain load-bearing:

- terminal programs emit byte streams, while users see a reconstructed cell grid;
- projections must not silently mutate their source observations;
- capture provenance must be explicit;
- blocking or heavy work must remain outside the render path;
- permissions should be narrow and visible to the operator;
- plain-text and append-only interfaces are valuable for replay and interoperation;
- semantic structure can be derived from terminal output without coupling it to one agent vendor;
- a live view, a filtered view, and the durable record are different objects.

The immutable-model discipline remains useful, but it should be stated precisely:

> Immutability prevents a renderer from corrupting an observation. It does not create history by itself. Replay requires retained observations or retained source events.

---

## 3. Corrections to the original model

### 3.1 A Zellij plugin is not the PTY owner

Zellij owns the PTY master, parses the process byte stream, and constructs the terminal grid. A plugin that calls `get_pane_scrollback` or receives a pane-render report observes a representation produced after that parsing.

Therefore `termbrana-zellij` is an **observer, projector, indexer, and controller**. It is not a peer terminal emulator and cannot claim possession of the original byte stream.

A future native process that allocates the PTY and sits between the child and Zellij could own that stronger role. This possible component is named `termbrana-pty` and is explicitly outside the first product slice.

### 3.2 A post-render observer is not a sanitizer choke point

Terminal escape sequences may already have affected Zellij before the plugin receives pane contents. A plugin can normalize what it stores or re-renders, but it cannot guarantee that hostile control sequences were harmless to the upstream parser.

Consequences:

- `termbrana-zellij` may provide safe derived text and semantic indexing;
- it must not describe its output as authoritative raw capture;
- it must not claim that displayed output equals original emitted bytes;
- pre-parser sanitization belongs only in a future PTY-owning process.

### 3.3 Rendered ANSI is not raw PTY history

Termbrana distinguishes four source grades:

| Source grade | Meaning | Audit strength |
| --- | --- | --- |
| `raw_pty` | Bytes read by a process that owns the PTY master | Strongest; future component only |
| `rendered_ansi` | Host-rendered pane representation with ANSI styling retained | Visual reconstruction, not original bytes |
| `rendered_text` | Host-rendered pane representation without ANSI styling | Semantic and navigation source |
| `derived` | Blocks, highlights, summaries, filters, or classifications | Must reference its parent observation |

The source grade travels with every persisted event. A downstream NablaRava adapter must not upgrade the grade.

### 3.4 The current opacity is a projection, not transparency

The Rust skeleton fades a uniform foreground toward a fixed background. Its background remains opaque. This can create a wash, clone, dimming, or focus effect, but not continuous compositing between terminal panes.

For Termbrana:

- visual wash is an optional projection experiment;
- semantic navigation is the first user value;
- native Zellij highlights should be preferred when they solve the visual need directly;
- full per-cell reconstruction is parked until a demonstrated use requires it.

### 3.5 Global interception is not a normal hotkey mechanism

Zellij input interception consumes intercepted keys. An always-on interceptor would have to forward every unhandled key correctly, including modifiers and terminal keyboard protocols. That is a large and unnecessary risk.

Termbrana therefore uses:

- explicit Zellij keybindings or plugin messages to open/focus Termbrana;
- ordinary `Event::Key` handling while the Termbrana pane is focused;
- a temporary intercept mode only for a separately justified operator action;
- `Esc` as an unconditional exit from any temporary control mode.

Read-only navigation must not require `WriteToStdin` or `InterceptInput`.

### 3.6 Replay requires a log

The original skeleton retains only the newest `CapturedGrid`; `captured_at_ms` is also a placeholder. Termbrana replay is instead based on:

- monotonic sequence numbers as the primary ordering mechanism;
- append-only JSONL records;
- explicit session and pane identity;
- optional wall-clock time when a trustworthy source exists;
- derived block records that reference the observation sequence from which they were produced.

---

## 4. Product decomposition

### `termbrana-core`

Pure Rust domain logic:

- observations and provenance;
- semantic block index;
- bookmarks;
- filters and projections;
- navigation state;
- replay from retained records.

It has no Zellij, NablaRava, Claude, Codex, or Gemini dependency.

### `termbrana-zellij`

Zellij WASM adapter:

- pane discovery and selection;
- viewport observation and on-demand scrollback retrieval;
- native highlights;
- Termbrana review pane;
- explicit command handling;
- pane lifecycle and compatibility handling.

### `termbrana-nablarava`

Optional boundary adapter:

- consumes neutral Termbrana JSONL or messages;
- maps selected observations and blocks into NablaRava concepts;
- never changes provenance grades;
- may be absent without reducing standalone Termbrana functionality.

### `termbrana-pty` — parked

Possible later host process:

- owns the PTY master;
- drains it continuously;
- propagates window size and signals;
- records raw bytes;
- applies an explicit terminal-control policy before downstream parsing.

It is not required to validate Termbrana's first product.

---

## 5. User-facing correction: editor-like navigation in a terminal

The smallest useful Termbrana is not an overlay. It is a semantic review surface over terminal history.

Inside its own review pane, Termbrana can jump to an absolute indexed block because it owns the projection offset. In the original terminal pane, the stable fallback is native search over a unique visible marker; the currently documented Zellij API provides line, page, top, and bottom scrolling, but not an arbitrary absolute line jump.

Candidate navigation vocabulary:

| Key | Meaning |
| --- | --- |
| `]b` / `[b` | next / previous semantic block |
| `]e` / `[e` | next / previous error block |
| `]t` / `[t` | next / previous tool or command block |
| `m<char>` | bookmark the current block |
| `'<char>` | jump to a bookmark |
| `/` | search retained text |
| `Space` | collapse or expand a block |
| `f` | freeze or resume live following |
| `y` | copy the current block |
| `o` | open a detected `path:line` target |
| `Esc` | leave Termbrana mode |

Termbrana should reuse native Zellij search, scrollback editing, regex highlighting, and clicks instead of duplicating them. Its independent value begins with semantic blocks, persistent bookmarks, filters, unread state, and replay.

---

## 6. Effect on the original Rust skeleton

`foil_plugin.rs` remains a research sketch. It should not be promoted by only renaming identifiers.

Its successor must be generated after the execution plan's truth spike establishes:

- the installed Zellij host version;
- the matching `zellij-tile` version;
- actual pane-content semantics;
- ANSI-report behavior;
- input and plugin-message behavior;
- performance under rapid output and large scrollback;
- whether a floating visual projection aligns without flicker.

Until then, the skeleton is evidence of intent rather than build evidence.

---

## 7. Current decision

Proceed with Termbrana as an independent, Zellij-first semantic terminal lens.

Do not make NablaRava a dependency of the core. Do not promise raw audit or sanitization from the plugin. Do not make continuous opacity the MVP. Preserve the PTY-owning security direction as a separately gated later experiment.

### Primary references

- [Zellij plugin commands](https://zellij.dev/documentation/plugin-api-commands.html)
- [Zellij plugin events](https://zellij.dev/documentation/plugin-api-events.html)
- [Zellij plugin API types](https://zellij.dev/documentation/plugin-api-types.html)
- [Zellij v0.44.3 release](https://github.com/zellij-org/zellij/releases/tag/v0.44.3)
