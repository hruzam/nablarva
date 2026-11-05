---
title: Remote workspace — scope map and reading guide
date: '2026-10-23'
author: Wave
language: en
type: index / decision brief
scope: cross-scope
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# Remote workspace — scope map and reading guide

**Prepared for majkee · 23 October 2026 · Wave**

## Executive position

Keep the existing SSH/tmux route for living CLI sessions. Evaluate a complete remote-desktop application separately. Consider a native Termbrana panel only for the navigation, notes, pins and deliberate handoff operations that are currently missing.

This is a recommendation, not an instruction to replace the working environment or begin a migration.

```text
Desktop access               Terminal access              Optional interface
RustDesk / KRdp / TigerVNC    existing SSH + tmux          Slint + Rust, or Qt
          |                           |                          |
          +--- separate need          +--- existing sessions ---+
                                                |
                                    authoritative project files
```

## Documents by scope

| File | Type | Use it for |
|---|---|---|
| [01_LINUX_REMOTE_DESKTOP_REPORT.md](01_LINUX_REMOTE_DESKTOP_REPORT.md) | Research report | TeamViewer-style access on Linux; RustDesk, KRdp and TigerVNC; a practical evaluation checklist. |
| [02_SSH_TMUX_RELAY_ARCHITECTURE.md](02_SSH_TMUX_RELAY_ARCHITECTURE.md) | Architecture brief | Session ownership, addressing, observation, file-backed handoff and reconnect behaviour; tmate/WezTerm alternatives. |
| [03_NATIVE_UI_OPTIONS_BRIEF.md](03_NATIVE_UI_OPTIONS_BRIEF.md) | Technology brief | Slint/Rust versus Qt/QTermWidget; what an embedded terminal adds to the scope. |
| [04_RUSTDESK_REUSE_REPORT.md](04_RUSTDESK_REUSE_REPORT.md) | Reuse assessment | Which RustDesk areas are relevant, what remains unaudited, and licensing/dependency gates. |
| [05_IMPLEMENTATION_HANDOFF.md](05_IMPLEMENTATION_HANDOFF.md) | Agent handoff | Repository-first inspection, a bounded first experiment, acceptance tests and stop conditions. |
| [06_SOURCES_AND_EVIDENCE.md](06_SOURCES_AND_EVIDENCE.md) | Evidence register | Primary-source links, qualifications, and what was and was not validated. |

For a coding-agent continuation, start with **05**, then **02**. For choosing a desktop tool, **01** stands alone. Each scope document includes its own source links and can be handed off independently.

## Context to preserve

Conversation context—not a freshly inspected machine inventory:

- majkee uses Linux/KDE, zsh, Sublime and persistent CLI sessions, with a home/office connection through Tailscale/SSH.
- Existing Sublime pins and thematic note batches are assets to integrate, not features to discard and rebuild.
- Remote devices are interfaces to workstation-owned execution. Native CLI access must remain available.
- Files are the durable coordination record. Terminal observations and vendor transcripts have different roles.

Actual repository files, host configuration and current diffs take precedence over this summary. No repository or workstation was accessed for this pack.

## Proposed direction, not a locked-in stack

| Question | Recommendation | Revisit when |
|---|---|---|
| How should existing sessions be reached? | Reuse the current SSH/tmux path. | An observed requirement cannot be met through that path. |
| Must we build a GUI now? | No. Prove the missing integration first. | A concrete interaction benefits from a native panel. |
| Which GUI direction? | Slint/Rust for a companion panel; evaluate Qt/QTermWidget for an embedded terminal. | A representative prototype and distribution requirements favour another choice. |
| Should we extract RustDesk transport? | Not for the present terminal-only objective. | Screen sharing or a distinct connectivity requirement justifies the dependency. |

## Evidence and authority

**Documented** means supported by a linked primary source. **Proposed** means Wave's design judgment. **Untested** means it has not been exercised on the target host. Recommendations are not benchmarks, and packaging these notes does not approve their implementation.

The earlier discussion is qualified in the scope reports: no measured memory advantage is claimed; Slint is not a terminal emulator or transport; RustDesk's terminal feature does not establish compatibility with existing tmux sessions; and source availability does not make component extraction trivial.

The Markdown files use UTF-8, YAML front matter, relative links and local footnote definitions. No external renderer or private account is required to read the documents. Public sources are linked, not bundled.

## Phone continuation — 2026-10-30, Oraculum

For Majkee's fast phone-console task, start with
[08 — current direction and retained native architecture](08_PHONE_CONSOLE_DIRECTION_2026-10-30.md),
then [09 — v0 extension candidate](09_V0_PHONE_EXTENSION_2026-10-30.md).
These operator-requested notes preserve the browser-first direction, the earlier
Kotlin/Compose/Room table, and the required post-build Houston documentation check.
They remain uncanonical. The older 05 handoff is historical context for this task,
not its current execution order; apply 07's repository-fit corrections as well.
