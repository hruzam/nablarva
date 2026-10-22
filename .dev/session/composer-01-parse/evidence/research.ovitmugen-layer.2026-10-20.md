---
kind: consultation-capture
captured_by: Cartan · Codex
source: /root/ovitmugen_layer_research · native researcher · fresh context
cycle: '21'
date: 2026-10-20
verbatim: true
---

Relative source paths in this native reply are relative to the Nablarva root,
as in its assignment; the reply itself is preserved without link rewriting.

## Verbatim reply

Question: should Termbrana consume ovitmugen “resources/pipes” (A), or should both use a lower layer (B)?

**Raw local-source evidence**

- **OBSERVED — ovitmugen is a tmux view/layout manager, not a transport.** It addresses two named tmux servers: the default agent server and the `ovitmugen` frame server; the frame’s left pane attaches to a grouped agent-session view and its right pane runs a fixed app. [ovitmugen.py:10](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:10), [ovitmugen.py:95](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:95), [ovitmugen.py:222](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:222).

- **OBSERVED — resources it controls are tmux sessions/windows/views and a frame, with guarded lifecycle operations.** `plan_up` creates a base session, windows, a grouped `--left` view, and a frame session; `plan_down` removes the frame, views, or only idle windows. It refuses busy-tab closure. [ovitmugen.py:239](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:239), [ovitmugen.py:252](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:252), [ovitmugen.py:264](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:264), [ovitmugen.py:590](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:590).

- **SOURCE — its stated boundary is viewer-only.** The local source laws prohibit `send-keys` and `paste-buffer`, and say closing a viewer/view never kills an agent. [ovitmugen.py:16](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:16). The generated plan selftest also asserts that neither injection command appears. [ovitmugen.py:821](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:821).

- **OBSERVED — ovitmugen owns no registry, retained record store, payload pipe, or input API.** Its only local data file is a read-only preset JSON file; `bed_report()` synthesizes bed/tab/view/frame metadata on demand and `ls --json` prints it. [ovitmugen.py:177](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:177), [ovitmugen.py:552](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:552), [ovitmugen.py:566](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:566). The bounded source search found no `pipe-pane`, FIFO, socket client/server, `send-keys`, or buffer-paste mechanism. The named `-L` sockets are tmux server control endpoints invoked through `subprocess.run`, not an application message protocol. [ovitmugen.py:59](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:59).

- **OBSERVED — its observable reusable primitives are coupled helpers, not a declared shared library.** `Tmux`, `servers()`, `tabs()`, `bed_report()`, and `switch_tab()` can respectively issue scoped tmux calls, enumerate/display tab metadata, and select the left view. [ovitmugen.py:59](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:59), [ovitmugen.py:95](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:95), [ovitmugen.py:147](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:147), [ovitmugen.py:535](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:535), [ovitmugen.py:552](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:552). There is no stable module/API contract beyond its CLI.

- **OBSERVED — Termbrana is not yet a core, replay, or transport implementation.** Its workspace contains only the Zellij M0 probe crate; `termbrana-core`, JSONL persistence, review UI, and replay are explicitly absent. [Cargo.toml:3](toolbox/termbrana/Cargo.toml:3), [README.md:7](toolbox/termbrana/README.md:7).

- **OBSERVED — Termbrana does contain a pipe, but only a Zellij M0 probe-control/evidence channel.** The harness accepts `zellij action pipe` commands to capture rendered pane data, subscribe to render reports, and test interception; `ReadCliPipes` is explicitly harness-only and not planned observer-product permission. [main.rs:8](toolbox/termbrana/crates/termbrana-zellij/src/main.rs:8), [main.rs:53](toolbox/termbrana/crates/termbrana-zellij/src/main.rs:53), [main.rs:112](toolbox/termbrana/crates/termbrana-zellij/src/main.rs:112), [README.md:87](toolbox/termbrana/README.md:87). It is neither a tmux pipe nor a reusable composition/input transport.

- **SOURCE — byte/render boundary differs materially.** Ovitmugen observes tmux metadata plus process-state clues from `/proc`, never pane bytes or semantic blocks. [ovitmugen.py:123](/home/hruzam/ia-sync/zsh/session/ovitmugen.py:123). Termbrana’s host sees Zellij-rendered text/ANSI, never raw PTY bytes; raw PTY requires a future separately owned component. [README.md:33](toolbox/termbrana/README.md:33), [README.md:45](toolbox/termbrana/README.md:45). The repository’s transport locks also say adapter-owned PTY, tmux is never the protocol, and reject tmux `send-keys` injection. [.dev/session/flag.md:14](.dev/session/flag.md:14), [.dev/session/flag.md:20](.dev/session/flag.md:20).

**Implications**

- **INFERENCE — A has no present pipe resource to consume.** A Termbrana dependency on ovitmugen today could consume only view-management metadata/actions. It would inherit tmux/session-bed assumptions and a dashboard lifecycle boundary, while yielding neither semantic observations nor a safe input carrier.

- **INFERENCE — B matches the facts only if “lower layer” means a future, separately specified contract.** No shared lower layer exists in the inspected source. The nearest reusable read-only datum is ovitmugen’s computed bed report; it is not a transport and carries no rendered terminal content. A prospective shared input carrier cannot be inferred from either current implementation.

- **INFERENCE — do not merge observation and transmission.** Termbrana’s M0 pipe controls a probe and its observer is read-only; ovitmugen is expressly views-only. Treating either as a generic write pipe would cross both established boundaries.

**Unresolved gaps**

- No evidence identifies the intended target identity, payload lifetime, writer arbitration, or acknowledgement/replay semantics for Majkee’s requested pipes.
- No source-level compatibility contract exists for consuming ovitmugen metadata outside its CLI/module.
- No live probe was run, as directed.

**Smallest next decision**

Decide whether the immediate need is only read-only session/view discovery. If yes, `bed_report` / `ov-ls --json` is the sole existing narrow candidate to qualify. If the need includes prepared-text delivery, neither A nor existing B is implemented; it requires a separate carrier qualification before any dependency or API decision.

No files were changed.
