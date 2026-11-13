---
title: RustDesk reuse — relevance, extraction risk and gates
date: '2026-10-23'
author: Wave
language: en
type: reuse assessment
scope: RustDesk components
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# RustDesk reuse — relevance, extraction risk and gates

## Verdict

Use RustDesk as a complete remote-desktop application when that solves the problem. Consider component reuse only for a requirement that actually needs its capabilities. For the current SSH-reachable terminal workflow, extracting its networking stack is not the recommended starting point.

This assessment is based on documented architecture, not an audit of module APIs or transitive dependencies.

## Documented areas and proposed relevance

The first two columns summarize the repository's file-structure map.[^R1] The last column is Wave's assessment.

| Area | Documented role | Relevance to our work |
|---|---|---|
| `libs/scrap` | Screen capture | Candidate only for an actual screen-sharing feature. |
| `libs/enigo` | Platform-specific keyboard/mouse control | Relevant to desktop input, not needed for direct tmux addressing. |
| `libs/clipboard` | File copy/paste integration | Investigate for a richer remote workspace, not ordinary note delivery. |
| `libs/hbb_common` | Shared configuration, protocol, networking and other utilities | Broad coupling risk to investigate; not presumed to be a generic relay SDK. |
| `src/client.rs`, `src/rendezvous_mediator.rs` | Peer connection and rendezvous/direct-or-relayed connection handling | Relevant only if current connectivity is insufficient for a demonstrated requirement. |
| `src/server`, `src/platform` | Desktop services and platform integration | Potentially substantial dependencies and permission requirements. |

A repository directory is not evidence of a stable embeddable API. The extraction cost remains unknown until the chosen revision and dependency graph are inspected.

## What the Flutter-to-Slint claim does and does not establish

The friend's statement says that a Codex-assisted migration is progressing. No repository, diff, release, build result or platform test from that work was supplied here.

Do not treat the friend's project as an available upstream RustDesk feature, a maintained fork we can adopt, or proof of better performance. It may eventually be valuable reference work, but its scope and completeness remain unverified.

Replacing a UI also does not automatically create reusable terminal transport, solve session addressing, or eliminate the need to test capture, input, clipboard and platform behaviour.

## A more economical reuse order

1. **Product reuse:** run RustDesk separately for desktop access.
2. **Protocol/API reuse:** keep the existing SSH/tmux integration for terminal access.
3. **Component reuse:** evaluate one bounded library only after a missing capability has been demonstrated.
4. **Application fork:** consider it only when the product-level requirement and maintenance budget justify it.

This order is a proposal intended to avoid turning a small workflow integration into a new remote-desktop product.

## Extraction checklist

Before adopting any code, produce a short spike report containing:

| Gate | Required evidence |
|---|---|
| Exact input | Repository, commit/tag, selected paths, submodule revisions and applicable licences. |
| Dependency boundary | Cargo/CMake features, native libraries, codec/rendering dependencies, platform APIs and build requirements. |
| Minimal use case | A small program demonstrating the required operation without unrelated application state. |
| Runtime ownership | Clear process/thread lifecycle, permissions, configuration and shutdown semantics. |
| Security boundary | Authentication, input validation, exposed services and credential handling for the actual integration. |
| Maintenance | How upstream fixes are tracked and local modifications are kept reviewable. |
| Exit criterion | A measurable reason this beats using the complete application or an existing narrower component. |

Do not start by copying a directory and fixing compile errors until it works. First establish which surrounding behaviour that directory expects.

## Licensing boundary

The main RustDesk repository publishes AGPL-3.0.[^R4] Review the exact files and dependencies before reuse, and assess obligations for the intended modification, distribution and deployment. Do not assume all subcomponents have one uniform licence, or that moving code behind a process boundary settles the legal analysis.

Slint's terms apply to the UI toolkit, not as a replacement for obligations attached to any RustDesk code incorporated alongside it.[^S4]

This report makes no final legal compatibility determination. A shipping decision requires a scoped review of the actual combined work.

## Recommendation to carry forward

Do not put a RustDesk extraction on the critical path of Termbrana's first navigation/handoff experiment. Keep screen sharing as an independent future scope, with its own evidence and decision record.

Related: [desktop report](01_LINUX_REMOTE_DESKTOP_REPORT.md) · [native UI brief](03_NATIVE_UI_OPTIONS_BRIEF.md) · [implementation handoff](05_IMPLEMENTATION_HANDOFF.md).

## Primary sources

Checked on 2026-10-23. Documentation is evidence of documented capability, not a test of an installed build.

[^R1]: [RustDesk repository and architecture map](https://github.com/rustdesk/rustdesk).
[^R4]: [RustDesk main repository licence](https://github.com/rustdesk/rustdesk/blob/master/LICENCE).
[^S4]: [Slint licence terms](https://slint.dev/terms-and-conditions).
