---
title: Linux remote desktop — candidates and evaluation
date: '2026-10-23'
author: Wave
language: en
type: research report
scope: desktop access
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# Linux remote desktop — candidates and evaluation

## Verdict

For the previous TeamViewer use case, evaluate **RustDesk as a complete application**. On the existing KDE workstation, also evaluate **KRdp** before building anything. Keep **TigerVNC** as a candidate when a conventional VNC or virtual-desktop arrangement better matches the requirement.

This is a suitability shortlist, not a ranking of memory use, responsiveness or reliability. No candidate was installed or benchmarked during this work.

## Documented capabilities

| Candidate | Documented capability | Interpretation for this workflow |
|---|---|---|
| RustDesk | An open-source remote-desktop application supporting self-hosting; its repository maps a Rust core and Flutter desktop/mobile code.[^R1] | Closest conceptual match to the former TeamViewer workflow. Use it as a product before considering a fork. |
| KDE KRdp | RDP server infrastructure with a Plasma settings interface, session-login autostart, authentication settings, certificates and quality controls.[^K1] | A natural candidate to test on the existing KDE host. It is the server side; an RDP client is still needed. |
| TigerVNC | A VNC client/server implementation with authentication and TLS-related features.[^V1] | A candidate for an explicitly assembled remote-display setup, not an assumption of TeamViewer-equivalent onboarding. |

### RustDesk: Wayland and terminal qualifications

The Linux guide inspected for this report still describes Wayland support as experimental and says remote login-screen access requires X11.[^R2] Treat that as the documented limitation to test against the selected package and desktop, not a promise that every newer release behaves identically.

Its release notes also contain a dedicated terminal feature and persistent-session reconnect fixes.[^R3] Therefore, RustDesk is not limited to showing a graphical terminal. However, the notes do **not** establish that this feature attaches to majkee's existing tmux sessions, implements our file-handoff contract, or works identically across all client/server combinations. Those are separate tests.

Do not change the desktop session type merely to follow a generic installation recipe. First establish whether access is needed to an already logged-in session, the lock screen, or the pre-login screen.

### KRdp: session access and network exposure

The inspected README describes autostart **at session login**, not a demonstrated pre-login/headless solution for this workstation. It also documents listening on `0.0.0.0`, including all-interface listening for the example server.[^K1]

**Deployment gate:** verify listening addresses and enforce the intended network boundary before enabling unattended access. The existence of a Tailscale route is not evidence that another route is blocked. Do not copy example passwords into shell commands or logs.

### TigerVNC: choose the correct display model

`Xvnc` supplies an X desktop backed by a virtual framebuffer.[^V2] By contrast, `w0vncserver` shares an existing Wayland display and documents a requirement for a wlroots-based compositor or an implemented RemoteDesktop portal.[^V3]

That is a meaningful compatibility condition. Check the actual compositor, portal implementation and packaged server; do not translate “Wayland supported” into “works on every Wayland desktop.”

## Proposed evaluation procedure

Record the exact application versions, package source, compositor/session type, host hardware, encoding configuration and network path. Evaluate the same task and display resolution for each candidate.

| Test | Record | Pass criterion to agree before selection |
|---|---|---|
| Existing logged-in desktop | Connection steps, prompts, capture and input behaviour | Required access succeeds without changing the local workflow. |
| Lock and logout | Behaviour in each state; whether local intervention is required | Actual unattended-access requirement is met. |
| Disconnect and reconnect | Surviving applications, required reauthentication, display recovery | No unexpected loss of the existing work session. |
| Keyboard and clipboard | Czech layout, modifiers, multiline text, non-ASCII characters | Relevant combinations behave correctly. |
| Displays and scaling | Monitor choice, mixed DPI, resize and reconnect | Usable on the actual workstation and viewing device. |
| Idle and active resources | Process-tree memory, CPU, GPU use, bandwidth and startup time | A documented budget is met; no inferred winner from language alone. |
| Network boundary | Listener addresses and allowed/denied connection attempts | Only intended peers can reach the service. |

These are proposed tests, not reported outcomes. Measure both ends where relevant, and distinguish RSS from PSS rather than comparing unlike memory numbers.

## Decision boundaries

Choose a remote-desktop product for graphical interaction. Do not make it a mandatory dependency of a terminal relay that already has a working connection.

Keep authentication and endpoint recovery understandable. Enabling unattended access, opening ports, installing services or changing firewall rules requires an explicit execution task; this report authorizes none of those changes.

**Next useful action:** run a bounded comparison of RustDesk and KRdp on the actual KDE machine, preserving the existing SSH/tmux route as an independent fallback.

Related: [terminal relay architecture](02_SSH_TMUX_RELAY_ARCHITECTURE.md) · [component reuse](04_RUSTDESK_REUSE_REPORT.md).

## Primary sources

Checked on 2026-10-23. Documentation is evidence of documented capability, not a test of an installed build.

[^R1]: [RustDesk repository and architecture map](https://github.com/rustdesk/rustdesk).
[^R2]: [RustDesk Linux documentation](https://rustdesk.com/docs/en/client/linux/).
[^R3]: [RustDesk release notes](https://github.com/rustdesk/rustdesk/releases).
[^K1]: [KDE KRdp repository and README](https://github.com/KDE/krdp).
[^V1]: [TigerVNC project](https://tigervnc.org/).
[^V2]: [TigerVNC Xvnc manual](https://tigervnc.org/doc/Xvnc.html).
[^V3]: [TigerVNC w0vncserver manual](https://tigervnc.org/doc/w0vncserver.html).
