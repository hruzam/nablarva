---
title: Sources and evidence — dated verification ledger
date: '2026-10-23'
author: Wave
language: en
type: evidence register
scope: cross-scope evidence
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# Sources and evidence register

## Scope of verification

Primary project documentation, repository READMEs, release notes, published licence text and generated API documentation were consulted on **23 October 2026**. Public pages may be cached, may change after this date, and may describe features absent from an installed distribution package. No claim is made that a particular version is the latest release.

Each scope document has its own footnotes. This register supplies the cross-pack reference map; public source pages are not copied into the archive.

## Reference map

| ID | Primary source | Used to check |
|---|---|---|
| R1 | [RustDesk repository and architecture map](https://github.com/rustdesk/rustdesk) | Product identity, UI/core distinction and repository component map. |
| R2 | [RustDesk Linux documentation](https://rustdesk.com/docs/en/client/linux/) | Published Linux/Wayland and login-screen qualifications. |
| R3 | [RustDesk release notes](https://github.com/rustdesk/rustdesk/releases) | Existence of terminal functionality and reconnect-related work, not local compatibility. |
| R4 | [RustDesk main repository licence](https://github.com/rustdesk/rustdesk/blob/master/LICENCE) | Main repository licence; not a per-component audit. |
| K1 | [KDE KRdp repository and README](https://github.com/KDE/krdp) | RDP server role, settings, session-login autostart and listener defaults. |
| V1 | [TigerVNC project](https://tigervnc.org/) | VNC product scope. |
| V2 | [TigerVNC Xvnc manual](https://tigervnc.org/doc/Xvnc.html) | Virtual X desktop model. |
| V3 | [TigerVNC w0vncserver manual](https://tigervnc.org/doc/w0vncserver.html) | Existing Wayland display model and compositor/portal conditions. |
| T1 | [tmux getting-started guide](https://github.com/tmux/tmux/wiki/Getting-Started) | Attachment/detachment and session continuity model. |
| T2 | [tmux control-mode protocol](https://github.com/tmux/tmux/wiki/Control-Mode) | Machine protocol, terminal output and observation caveats. |
| T3 | [tmux manual, OpenBSD publication](https://man.openbsd.org/tmux) | Command and attachment semantics; compare with installed version. |
| T4 | [OpenSSH client manual](https://man.openbsd.org/ssh) | SSH remote-command and pseudo-terminal options. |
| M1 | [tmate project](https://github.com/tmate-io/tmate) | Terminal-sharing purpose and tmux lineage. |
| M2 | [tmate self-hosted SSH server](https://github.com/tmate-io/tmate-ssh-server) | Availability of the self-hosted server implementation. |
| W1 | [WezTerm multiplexing and SSH domains](https://wezterm.org/multiplexing.html) | Ordinary SSH versus native remote multiplexing requirements. |
| S1 | [Slint language and application guide](https://docs.slint.dev/latest/docs/slint/) | Declarative UI building blocks. |
| S2 | [Slint language integrations](https://docs.slint.dev/latest/docs/slint/language-integrations/) | Rust and C++ integration. |
| S3 | [Slint backends and renderers](https://docs.slint.dev/latest/docs/slint/guide/backends-and-renderers/backends_and_renderers/) | Backend/renderer choices and trade-offs. |
| S4 | [Slint licence terms](https://slint.dev/terms-and-conditions) | Published licence routes and conditions. |
| Q1 | [QTermWidget README, licensing and API](https://github.com/lxqt/qtermwidget) | Embedded terminal role, API and project-level licence. |
| A1 | [alacritty_terminal generated API documentation](https://docs.rs/alacritty_terminal/latest/alacritty_terminal/) | Rust terminal-core API surface, not Slint integration. |


## Qualifications carried into the artifacts

| Earlier idea | Durable interpretation |
|---|---|
| “Rust/C++ solutions are light.” | Implementation language is not a benchmark. Compare the actual workload and full process/dependency costs. |
| “Flutter to Slint simplifies RustDesk.” | A plausible design motivation; no result from the friend's migration was available to verify. |
| “RustDesk has a terminal.” | Supported by release notes; does not establish existing tmux integration or universal client/server support. |
| “Control mode gives us agent messages.” | It gives a machine interface and terminal data. Semantic history and task results require separate sources. |
| “A read-only panel cannot disturb sessions.” | An intended property to test, including hooks, identity, resize, input and lifecycle effects. |
| “Tailscale makes a server private.” | A chosen route is not proof of exclusive reachability. Verify service exposure and enforcement. |
| “Copying a RustDesk library is easy reuse.” | No dependency or API audit was performed; extraction remains a separate investigation. |
| “The recommendations are now settled canon.” | They remain advisory until reconciled with the repository and explicitly adopted. |

These rows record corrections, reasoning and test obligations. They are not independent product specifications; the applicable source-backed details appear in the linked scope reports.

## Validation ledger

| Work | Status |
|---|---|
| Consult primary documentation for the material capability/licence claims | Performed. |
| Separate conversation context, source-backed facts and proposals | Performed in the scope documents. |
| Create UTF-8 Markdown files and a ZIP bundle | Performed. |
| Validate YAML metadata, Markdown structure, footnote definitions and relative links | Performed during packaging. |
| Verify ZIP integrity and byte-for-byte contents against the Markdown files | Performed during packaging. |
| Inspect majkee's current repository, local diffs or workstation | Not performed. |
| Execute the example SSH/tmux commands on a target host | Not performed. |
| Install, build or benchmark any candidate application | Not performed. |
| Audit component dependencies or issue a licence-compatibility determination | Not performed. |
| Validate the friend's Flutter-to-Slint migration | Not performed; no source or build evidence supplied. |

## Use after this date

Before implementation, pin actual package versions or repository revisions and recheck volatile behaviour. Replace assumptions with observed facts in the repository's own state/handoff files. Preserve these documents as the dated research/decision input, not as a substitute for that evidence.
