# Terminal trial — implementation evidence and proposed seams

Astrobley, 2026-10-30; bounded prompt-1. This is a proposal and implementation
receipt, not a contract lock or physical qualification. No application home created.

Position before the cut: use a pinned external gateway, fixed command arguments,
private loopback access, and a dedicated tmux socket. First establish the terminal
loop. Do not build a composer against an assumed iframe API or reuse a live pane.

## Observed dependency and upstream boundary

[ttyd release 1.7.7](https://github.com/tsl0922/ttyd/releases/tag/1.7.7) is the
latest release returned by the upstream releases endpoint, published 2024-03-30.
Downloaded x86_64 binary reports `1.7.7-40e79c7`. Its SHA256 is
`8a217c968aba172e0dbf3f34447218dc015bc4d5e59bf51db2f2cd12b7be4f55`.
The source tarball hash is in the adjacent JSON receipt. These are locally observed
hashes, not a claim of signature verification. Downloaded files live only in
`/tmp/phone-console-ttyd-1.7.7/`. The release source is MIT; retain notices on
redistribution. [License](https://github.com/tsl0922/ttyd/blob/1.7.7/LICENSE).

Supported extension seams are CLI options, client preferences, and a custom HTML
entry with `-I`; `-b` mounts a reverse-proxy path. Commands are server-owned;
leave `-a` disabled. The bundled frontend is a Preact app around xterm.js 5.4.
Its `window.term` assignment is an implementation detail, with no documented
parent-to-iframe composer/key API. An iframe is adequate for a manual trial;
direct programmatic controls need an owned, pinned frontend module and explicit
adapter contract. `-I` serves an HTML entry, not an arbitrary application asset
server: upstream bundles its page and assets together. Source references:
[CLI](https://github.com/tsl0922/ttyd/blob/1.7.7/README.md),
[frontend](https://github.com/tsl0922/ttyd/blob/1.7.7/html/src/components/terminal/xterm/index.ts),
[HTTP server](https://github.com/tsl0922/ttyd/blob/1.7.7/src/http.c).

On each authenticated WebSocket initialization ttyd starts its configured command;
on socket closure it signals that process (SIGHUP default). A persistent tmux shell
survives through a disposable `tmux attach-session` client. The browser resets its
terminal on reconnect; it does not preserve a full conversation, acknowledge input,
or safely replay uncertain input. Auto reconnect differs for abnormal close versus
normal close (the latter offers Enter to reconnect). Source:
[protocol](https://github.com/tsl0922/ttyd/blob/1.7.7/src/protocol.c),
[client](https://github.com/tsl0922/ttyd/blob/1.7.7/html/src/components/terminal/xterm/index.ts).

`-c` gates HTTP and WebSocket upgrade with Basic credentials; authenticated `/token`
returns the encoded credential for the first WebSocket JSON `AuthToken` message.
Treat it as a credential, never durable evidence. `-H` merely trusts the presence of
the configured header: a production proxy must authenticate and replace that header,
and the backend must be unreachable directly. `-O` rejects missing and foreign
Origin but compares host/port without scheme. The local probe confirmed this
limitation. The eventual HTTPS ingress must bind exact Origin, preserve the trusted
external Host, and enforce authorization for both HTTP and upgrade. This loopback
USB trial does not prove a tailnet HTTPS deployment or authorize an ACL change.

## One bounded maintained alternative

[WeTTY v3.3.5](https://github.com/butlerx/wetty/releases/tag/v3.3.5), released
2026-09-29, is a vendor-neutral MIT terminal using xterm.js, Socket.IO and node-pty.
Its recent origin/security fixes show ongoing maintenance. It offers SSH/login,
custom command, mount path, iframe and allowed-origin controls; it brings a Node
runtime and native build dependencies. The reviewed README/package expose no
durable composer or shared prompt/file vault, so this bounded review gives no reason
to replace ttyd solely to gain those missing controls. WeTTY was not installed or
functionally qualified. Its tagged package.json still reports 3.0.0 despite the
v3.3.5 release label: use the actual release/commit if selected later. Sources:
[tagged README](https://github.com/butlerx/wetty/blob/v3.3.5/README.md),
[tagged package](https://github.com/butlerx/wetty/blob/v3.3.5/package.json).

## Proposed minimal contracts for Cartan review

- Target reference: host identity plus tmux server generation, window/pane ID and
  pane process identity. Session name alone is insufficient. Revalidate at attach
  and every control operation; a changed generation requires explicit reselection.
- View: a separate linked/grouped tmux session per independent browser view, sharing
  windows/panes but owning its active-window selection. A shared `phone` session
  proves phone-versus-desktop independence only; multiple phone tabs need separate
  view identities. Linked windows still share pane selection and dimensions.
- Terminal module: mount/unmount, focus, connection state with target identity,
  explicit `paste(text)` and explicit `key(allowlistedKey)`. It sends only while
  connected to the selected generation, has no background queue, and clears
  unsent transport state on disconnect. Paste does not imply Enter. Bracketed paste
  behavior needs qualification per shell/application; the trial proves only a
  single-line paste and separate Enter. Multiline shell paste can execute lines.
- Ownership: ovitmugen remains lifecycle/list owner. The host adapter translates
  validated target/view handles into fixed tmux attachments and owner APIs, never
  arbitrary URL commands, global tmux cleanup or another session manager.
- Delivery: sent-to-socket is distinct from accepted-by-process. No acknowledgement
  should claim delivery certainty; never auto replay after disconnect. Native CLI
  approvals remain live terminal interactions; no inferred approval state.
- Vault and drafts have independent revision/storage contracts; terminal transport
  does not claim their persistence or provide a room send API.

## Launch, checks and bounded rollback

From the repository root:

```sh
python3 .dev/session/phone-console-01-browser/raw/trial/gateway.py start --port 18789
python3 .dev/session/phone-console-01-browser/raw/trial/probe.py /tmp/pc-trial-j6j1id09
tmux -S /tmp/pc-trial-j6j1id09/tmux.sock attach-session -t desktop
python3 .dev/session/phone-console-01-browser/raw/trial/gateway.py stop /tmp/pc-trial-j6j1id09
```

The first command returns a fresh runtime directory; use that returned directory
for subsequent commands on a new run. Cartan launched the recorded runtime. The
launcher binds only 127.0.0.1, pins the binary hash, creates random credentials in a
0700 temporary directory, starts only two disposable shells on its explicit socket,
and never changes shell rc files, system services, package paths or live tmux panes.
The parent owns ADB reverse/browser state and must remove only its exact reverse
mapping on rollback. No device or USB operation belongs to these scripts.

Stop verifies the PID command before signaling it and kills only this private
socket's tmux server. It retains runtime files/evidence for review, including private
credentials; the head should retire those temporary files when finished. No global
installation was made. Do not copy runtime state.json or unredacted logs into git.

The probe passed HTTP/WS authorization, host/port Origin rejection, exact Czech UTF-8,
paste versus Enter, same shell PID after reconnect, and independent active-window
selection. Receipt: `terminal-trial.evidence.2026-10-30.json`. Syntax checks passed.
The initial sandbox run could not open sockets; the authorized escalated run exited 0.
Physical Redmi IME, keys, scrollback, clipboard, native CLI permission, long screen-off
and reconnect usability remain with Cartan/Majkee before surrounding UI investment.

Integration action: disposition the explicit frontend boundary and physical terminal
trial, then fix the owned transport interface before dispatching UI/storage writers.
