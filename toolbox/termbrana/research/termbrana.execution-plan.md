`source: ~/.remote/harvest · author: Wave r0 2026-08-15 · adopted: flag L11 2026-08-15 · role: founding canon`

# Termbrana — Execution Plan for Coding Agents

**Status:** Draft r0  
**Date:** 2026-08-15  
**Target:** independent Zellij-first MVP  
**Estimated size:** medium; approximately 3–6 weeks for one strong Rust systems developer to reach a hardened independent beta  

---

## 1. Execution rule

Do not begin by renaming `foil_plugin.rs` and filling its placeholders.

Begin by proving the host boundary. The original skeleton contains useful intent but no Cargo project, compatibility matrix, compile result, runtime evidence, or tests. Every implementation claim must be established against the actually installed Zellij version.

### Repository authority order

1. current Termbrana definition and decisions;
2. probe evidence from the pinned host version;
3. compiling code and tests;
4. original Foil theory and skeleton as research history;
5. agent recollection.

---

## 2. Proposed repository shape

Start with one workspace and two crates:

```text
termbrana/
├── Cargo.toml
├── README.md
├── ARCHITECTURE.md
├── DECISIONS.md
├── crates/
│   ├── termbrana-core/
│   └── termbrana-zellij/
├── profiles/
├── fixtures/
├── research/
│   └── evidence/
└── docs/
```

Add an adapter or PTY crate only when its milestone begins. Do not pre-create empty architecture.

---

## 3. Milestone 0 — Host truth spike

**Effort:** 1–3 coder-days  
**Goal:** replace assumptions with reproducible evidence.

### T0.1 Establish versions

- record `zellij --version`;
- record `rustc --version`, `cargo --version`, and installed WASM targets;
- select the exact matching `zellij-tile` version;
- prefer `wasm32-wasip1` for the current toolchain unless the pinned host documentation proves otherwise;
- record Arch package provenance or binary provenance.

**Done when:** a minimal plugin compiles, loads, renders its version information, and its build commands are committed.

### T0.2 Prove pane-content semantics

Create fixtures containing:

- plain text;
- 8-color, 256-color, and true-color SGR;
- cursor movement and erased text;
- OSC title and OSC 52 attempts;
- alternate-screen content;
- wide CJK glyphs, emoji, and combining marks;
- wrapped long lines.

Observe and save results from:

- `get_pane_scrollback(..., false)`;
- `get_pane_scrollback(..., true)`;
- `PaneRenderReport`;
- `PaneRenderReportWithAnsi`, if available in the pinned version.

For every result, label whether it is raw, rendered ANSI, or rendered text. Never infer raw-byte fidelity from visual similarity.

**Done when:** `research/evidence/pane-content-matrix.md` states what survives, what is normalized, and what is lost.

### T0.3 Prove input behavior

- demonstrate ordinary `Event::Key` behavior in a focused plugin pane;
- demonstrate what global interception consumes;
- determine whether an intercepted unhandled key can be faithfully forwarded;
- demonstrate explicit Zellij keybinding or plugin-message activation;
- verify `Esc` recovery.

**Gate:** observer mode must not need global interception.

### T0.4 Prove geometry and rendering

- test tiled review pane;
- test floating review pane;
- test resize and rapid updates;
- test whether a copied-pane visual can remain aligned without flicker;
- compare direct native regex highlights with re-rendering a copied pane.

**Gate:** if overlay alignment or responsiveness is weak, delete overlay from the MVP and keep the review-pane design.

### T0.5 Prove performance limits

Test:

- rapid continuous output;
- large full scrollback;
- viewport-only observation;
- update-driven capture versus timer polling;
- hidden and visible plugin states;
- target pane closure during observation.

Record CPU, responsiveness, capture latency, and any host-query stalls. Do not choose a fixed 4 Hz poll until evidence supports it.

### Milestone 0 deliverables

- compiling minimal plugin;
- exact build and load instructions;
- compatibility/version note;
- five probe reports;
- decision: side review pane, floating review pane, or both;
- decision: capture/event mechanism;
- corrected implementation backlog.

---

## 4. Milestone 1 — Pure core

**Effort:** 3–5 coder-days  
**Goal:** build deterministic semantic navigation without a terminal host.

### T1.1 Domain types

Implement:

- `ObservationId` and monotonic sequence;
- session and pane identity;
- `SourceGrade`;
- observation payloads;
- semantic blocks;
- bookmarks;
- view/navigation state.

Use newtypes where accidental ID mixing is plausible. Avoid time as the primary key.

### T1.2 Block indexing

Implement two lanes:

1. explicit `@@termbrana:block` and `@@termbrana:end` markers;
2. generic heuristic rules from fixture text.

The core returns derived blocks and never mutates observation text.

Minimum kinds: prompt, answer, command, tool, output, error, approval, test, note, unknown.

### T1.3 Navigation reducer

Implement pure transitions for:

- next/previous block;
- next/previous block of kind;
- search result navigation;
- bookmark create/jump/delete;
- live/frozen mode;
- filter changes;
- collapse state;
- unread cursor.

### T1.4 JSONL

Implement candidate v0 serialization and strict decoding.

Requirements:

- one record per line;
- unknown event kinds can be retained or rejected explicitly, never silently misread;
- derived records reference parent sequences;
- source grade cannot be upgraded by conversion;
- truncated final line is handled as recoverable append interruption.

### T1.5 Core tests

Required tests:

- stable block IDs across replay;
- deterministic navigation;
- malformed and nested markers;
- marker without end;
- empty and huge blocks;
- Unicode titles and content;
- bookmark target absent after partial import;
- JSONL round-trip;
- provenance preservation.

**Done when:** all core behavior runs under ordinary host tests without Zellij or WASM.

---

## 5. Milestone 2 — Read-only Zellij MVP

**Effort:** 4–7 coder-days  
**Goal:** deliver independent daily user value.

### T2.1 Pane selection and lifecycle

- choose focused terminal pane on activation;
- display target identity;
- allow explicit retargeting;
- handle target closure and tab movement;
- never target the Termbrana plugin itself as terminal content;
- restore a safe no-target state.

### T2.2 Capture adapter

- translate pinned Zellij pane contents into `termbrana-core` observations;
- attach correct source grade;
- use sequence ordering;
- capture viewport live and full scrollback only when required;
- bound memory and define eviction versus retained-log behavior;
- never block render on heavy indexing or file work.

### T2.3 Review view

Implement:

- status line with target, source grade, freshness, and live/frozen state;
- text viewport owned by Termbrana;
- block headers and active-block indication;
- `]b`, `[b`, `]e`, `[e`, `]t`, `[t`;
- search;
- bookmark create and jump;
- collapse/expand;
- copy active block;
- all/errors/tool-command filters.

### T2.4 Native host enhancements

Where supported by the pinned version:

- use regex highlights for errors, URLs, paths, and explicit markers;
- consume highlight-click events;
- use native scrollback editing for full editor fallback;
- open `path:line` only after explicit user action.

### T2.5 Permission tiers

Observer MVP requests only the capabilities it actually exercises. `WriteToStdin`, signals, host commands, and interception remain absent unless a feature and test require them.

### Milestone 2 acceptance

From an ordinary shell or agent pane, a user can:

1. open Termbrana;
2. inspect the selected pane's retained history;
3. jump among meaningful blocks;
4. freeze, search, bookmark, filter, collapse, and copy;
5. close or retarget the source pane without losing control of Zellij;
6. use the tool with NablaRava completely absent.

---

## 6. Milestone 3 — Independent beta hardening

**Effort:** 1–3 weeks  
**Goal:** make the MVP installable and trustworthy.

### Required work

- adaptive capture cadence or event-driven updates;
- terminal display-width correctness;
- scrollback and memory limits;
- crash-safe append-only logs;
- configuration parsing and validation;
- user-defined generic regex rules;
- host-version compatibility checks;
- reproducible release build;
- Arch-oriented installation instructions without assuming only Arch;
- threat model for observer mode;
- fuzz or property tests for marker and JSONL parsing;
- fixtures for Codex, Claude, Gemini, and generic shell output;
- manual acceptance matrix across supported Zellij versions;
- clear statement of what is not raw capture.

### Beta release gate

- no swallowed input in observer mode;
- no writes to target panes;
- deterministic replay from a retained log;
- source grades visible and preserved;
- target lifecycle recovery proven;
- documented resource behavior under large scrollback;
- install and uninstall instructions tested on a clean user configuration.

---

## 7. Milestone 4 — NablaRava adapter

**Effort:** 3–5 coder-days after the neutral contract stabilizes  
**Goal:** make Termbrana a sensor without making it a subsystem.

### Adapter responsibilities

- consume Termbrana JSONL or explicit plugin messages;
- map selected blocks into NablaRava's current boundary contract;
- retain Termbrana sequence and source grade;
- include adapter provenance;
- support a read-only notification path first;
- remain one-directional until reverse control demonstrates value.

### Forbidden coupling

- no NablaRava imports in `termbrana-core`;
- no NablaRava availability check during Termbrana startup;
- no silent history mutation;
- no conversion of `rendered_text` into a stronger evidence label;
- no vendor-agent classifier embedded as universal truth.

### Gate

Disconnect NablaRava. All Milestone 2 acceptance tests must still pass.

---

## 8. Milestone 5 — Optional PTY experiment

**Estimated effort:** 6–12 additional weeks  
**Start only if:** a demonstrated requirement needs raw bytes, pre-parser policy, or authoritative session capture.

### Before approval

Write an ADR answering:

- which concrete threat or evidence requirement cannot be met by rendered observations;
- whether an existing recorder/proxy can be composed instead;
- whether Termbrana must render or can remain a transport and log layer;
- acceptable latency and compatibility cost;
- how secrets, clipboard controls, and terminal queries are treated.

### Required substrate work

- allocate and continuously drain PTY master;
- child process lifecycle;
- correct `EIO` handling on Linux;
- signal and process-group forwarding;
- `TIOCSWINSZ` and `SIGWINCH` propagation;
- bounded buffering and backpressure tests;
- raw append-only capture;
- tested terminal-control allow/deny/normalize policy;
- explicit downstream `$TERM` and terminfo contract;
- failure recovery without orphaned children.

Do not implement a terminal parser from scratch unless a narrower maintained library cannot meet the established contract.

---

## 9. Work packages for parallel coding agents

Parallel work begins only after Milestone 0 freezes the host contract.

| Package | Scope | Inputs | Output | Must not do |
| --- | --- | --- | --- | --- |
| Core model | types, reducer, provenance | project definition | tested `termbrana-core` | import Zellij |
| Block index | markers and generic rules | fixtures, core types | derived blocks and tests | encode vendor policy in core |
| Zellij adapter | pane capture and lifecycle | truth-spike evidence | observation adapter | invent raw fidelity |
| Review UI | rendering and keymap | reducer API | usable plugin view | globally intercept by default |
| Persistence | JSONL and recovery | record envelope | append/replay tests | silently rewrite records |
| Profiles | Codex/Claude/Gemini rules | captured fixtures | optional profile data | become core truth |

Integration ownership remains with one agent. Parallel agents do not independently change shared domain types; they propose changes through the owner or an ADR.

---

## 10. Validation matrix

### Functional

- explicit markers;
- heuristic blocks;
- no recognized blocks;
- multiple panes and tabs;
- source closes;
- source enters alternate screen;
- resize while frozen and live;
- copy and open actions;
- plugin reload.

### Text correctness

- ASCII;
- combining characters;
- double-width glyphs;
- emoji sequences;
- invalid UTF-8 boundary from an adapter;
- very long unwrapped line;
- ANSI retained and ANSI stripped sources.

### Safety

- OSC 52 fixture;
- title-change fixture;
- cursor rewrite fixture;
- malformed CSI/OSC/DCS;
- hostile marker-looking text;
- untrusted path and URL;
- denied permissions;
- host-version mismatch;
- incomplete JSONL tail.

### Performance

- continuous fast output;
- 100,000-line retained history;
- repeated freeze/live transitions;
- rapid target changes;
- hidden plugin for an extended period;
- replay without a running Zellij session.

---

## 11. Size and decision gates

| Stage | Cumulative size | Decision |
| --- | ---: | --- |
| Truth spike | 1–3 days | Is the Zellij boundary sufficient? |
| Useful MVP | 8–15 days | Does semantic navigation beat ordinary search? |
| Independent beta | 3–6 weeks | Is Termbrana reliable enough for daily use? |
| NablaRava adapter | +3–5 days | Does integration remain optional and neutral? |
| PTY/security product | +6–12 weeks | Is raw ownership worth a second system? |

If the MVP does not beat native search and scrollback editing for real sessions, stop. Preserve the probe and core work; do not justify the project through visual opacity.

---

## 12. First coding-agent assignment

```text
Goal: Establish the Termbrana Zellij host contract; do not implement the product yet.

Read first:
- termbrana.project-definition.md
- termbrana.addendum-to-foil-theory.md
- foil_theory.md
- foil_plugin.rs

Tasks:
1. Record installed Zellij/Rust/WASM versions.
2. Create the smallest compiling Zellij plugin for that exact version.
3. Run and record the five Milestone 0 probes.
4. Preserve fixtures and raw probe observations.
5. Write pane-content-matrix.md and a short ADR choosing the MVP view/capture path.

Constraints:
- no NablaRava coupling;
- no global interception for observer mode;
- no raw-capture or sanitization claims;
- no full VT parser;
- no production rewrite of the Foil skeleton.

Return:
- files changed;
- exact commands and outcomes;
- evidence paths;
- discovered API mismatches;
- recommended next task;
- remaining uncertainty.
```

---

## AI HANDOFF

**Goal:** Convert Nabla's Foil exploration into an independently executable Termbrana project.  
**Current state:** Architecture, provenance boundary, MVP surface, and phased execution plan are defined; no production code has been claimed.  
**Decisions made:** Standalone core; Zellij-first observer; read-only MVP; semantic navigation before opacity; optional NablaRava adapter; PTY security work parked behind evidence.  
**Files changed:** New Termbrana definition, theory addendum, and execution plan. Original Foil files preserved.  
**Validation performed:** Source files reviewed; volatile Zellij API claims checked against current official documentation during architecture review. No Rust compilation or runtime test performed.  
**Open questions / risks:** Installed host version; pane-content fidelity; ANSI report behavior; update cadence; floating geometry; large-scrollback performance.  
**Recommended next move:** Execute Milestone 0 as a bounded evidence-producing spike.  
**Agent:** Wave
