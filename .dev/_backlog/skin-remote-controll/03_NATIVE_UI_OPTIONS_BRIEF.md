---
title: Native UI — Slint/Rust, Qt and terminal embedding
date: '2026-10-23'
author: Wave
language: en
type: technology brief
scope: native interface
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# Native UI — Slint/Rust, Qt and terminal embedding

## Recommendation

For a panel beside the existing terminal, evaluate **Slint + Rust**. When an embedded, fully interactive terminal is a core requirement, evaluate **Qt + QTermWidget** before committing to a custom Rust terminal integration.

Neither choice is approved or benchmarked. The first useful experiment may need no new GUI at all.

## Documented building blocks

**Slint** offers a declarative UI language with properties, callbacks, layouts, models and custom controls, and official Rust and C++ integrations.[^S1][^S2] Its documented backend/renderer choices include Winit and Qt, alongside software and GPU rendering options.[^S3]

**QTermWidget** is an embeddable Qt 6 terminal emulator derived from Konsole. Its documented API includes program/argument configuration, starting the terminal program, text input, selection and terminal events.[^Q1]

**alacritty_terminal** exposes terminal-state and parsing-related building blocks, including a grid, `Term`, selection, PTY-related modules and `vte`.[^A1] That is useful infrastructure to investigate, not a ready-made Slint widget or a tested integration in this project.

## Three options and their boundaries

| Option | What we would build | What remains outside | Main deciding constraint |
|---|---|---|---|
| Slint/Rust companion panel | Session navigation, note batches, file views, explicit handoff actions | Existing terminal handles full interactive CLI rendering | Is navigation/handoff the actual missing feature? |
| Qt/QTermWidget application | Native panel plus an embedded terminal running the existing SSH/tmux path | Host still owns the persistent sessions | Is one-window terminal interaction essential enough to justify the integration and licence choice? |
| Slint plus a Rust terminal core | Custom terminal presentation and event integration as well as the panel | Existing host/session ownership can remain unchanged | Is custom terminal behaviour a genuine product requirement, rather than incidental ambition? |

The estimated implementation burden rises substantially in the third option. That is an architectural judgment, not a time estimate or measured comparison.

## Proposed Termbrana companion panel

```text
Existing Sublime pins + note files
                |
      adapter into existing formats
                |
         optional native panel
       /          |           \
 navigation   observations   reviewed action
      |           |                |
 open native   files/tmux     existing relay
 terminal       views          contract
```

Preserve the current pin/anchor semantics. Do not replace Sublime with a new editor, copy all files into a UI database, or introduce a second queue solely for the panel.

Useful proposed views are host/session navigation, thematic notes, request/result inspection and clearly separated transport/activity/task states. A selected transcript view can be added only when its format and provenance are known.

Closing or crashing this panel must not terminate an agent, erase a queued intent, or prevent direct terminal access. A panel may own its own viewer/SSH child, but that child's exit must not become an instruction to kill the remote session.

## Why a text box is not a terminal

The tmux control-mode stream contains application terminal data, not pre-rendered assistant messages.[^T2] A custom interactive terminal therefore needs an explicit plan for cursor movement, alternate screens, resizing, scrolling, selection, Unicode, keyboard encoding and mouse behaviour. Treat those as requirements to validate, not automatic properties of the UI toolkit.

A bounded, escaped text preview is a legitimate feature. Label it as a preview and provide an action to open the real terminal; do not market it as complete terminal emulation.

## Performance: define “light” before selecting

Changing the language or toolkit does not establish a smaller process or faster application. Slint's renderer documentation itself distinguishes different implementation paths and notes a heavier disk footprint for its Skia renderer.[^S3]

Proposed comparison: use a representative session list, the same number of notes, a bounded high-output preview and a reconnect cycle. Record startup time, process-tree PSS/RSS, idle and active CPU, rendering responsiveness, dependency size and packaging effort. Include the existing terminal's cost consistently when comparing a companion panel against an embedded terminal.

Do not optimize by measuring an empty demo window against a feature-complete alternative.

## Licensing gates

Slint's published options include GPLv3, a royalty-free desktop/mobile/web licence with attribution conditions, and a paid licence route. The royalty-free terms also contain scope and API-exposure limitations; it is not an unrestricted permissive licence.[^S4]

QTermWidget states GPLv2-or-later at project level, with some files under other compatible licences.[^Q1] Record the exact selected version and files; do not infer that a subset's licence applies to the whole widget.

These are engineering screening notes, not a licence-compatibility determination for an unbuilt application. Recheck the exact dependency tree and intended distribution before commitment. The Alacritty-based option also requires its own version/API/licensing audit; none was performed here.

## Decision experiment

Use an existing shell-level adapter and mock/local data first. A Slint prototype should demonstrate navigation, pin preservation and non-destructive reconnect without implementing a terminal. A QTermWidget prototype should demonstrate the actual CLI's rendering, keyboard behaviour and safe viewer closure through SSH/tmux.

Choose from observed behaviour and maintenance cost. No frontend choice should require adoption of RustDesk's transport.

Related: [relay architecture](02_SSH_TMUX_RELAY_ARCHITECTURE.md) · [handoff](05_IMPLEMENTATION_HANDOFF.md).

## Primary sources

Checked on 2026-10-23. Documentation is evidence of documented capability, not a test of an installed build.

[^S1]: [Slint language and application guide](https://docs.slint.dev/latest/docs/slint/).
[^S2]: [Slint language integrations](https://docs.slint.dev/latest/docs/slint/language-integrations/).
[^S3]: [Slint backends and renderers](https://docs.slint.dev/latest/docs/slint/guide/backends-and-renderers/backends_and_renderers/).
[^Q1]: [QTermWidget README, licensing and API](https://github.com/lxqt/qtermwidget).
[^A1]: [alacritty_terminal generated API documentation](https://docs.rs/alacritty_terminal/latest/alacritty_terminal/).
[^T2]: [tmux control-mode protocol](https://github.com/tmux/tmux/wiki/Control-Mode).
[^S4]: [Slint licence terms](https://slint.dev/terms-and-conditions).
