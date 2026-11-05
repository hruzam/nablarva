# tmux source fidelity — attributed researcher consultation

Recorded by Cartan X2 from native researcher `/root/tmux_source_research` on 2026-10-22.
Assignment: `question.tmux-source-fidelity.cartan.2026-10-22.md`. Text-only role; no files,
fixtures, living-session probes or transports were assigned. This is source research, not
runtime qualification or the missing L14 D4 relay verdict.

The returned text below is preserved verbatim. Head verification/addenda follow separately.

---

**Question.** For the first disposable source-qualification slice, what can tmux 3.7c’s `pipe-pane`, `capture-pane`, and control mode establish about a pane, and what still needs a fixture?

**OBSERVED (2026-10-22, no server/pane contact):** `tmux -V` reports **tmux 3.7c**. The installed local manual agrees with the upstream 3.7c tag. The [3.7c release](https://github.com/tmux/tmux/releases/tag/3.7c) identifies tag `e476c12` as a tmux 3.7 bug-fix release; the exact source/manpage used below is [tagged `tmux.1`](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1) and [tagged control implementation](https://raw.githubusercontent.com/tmux/tmux/3.7c/control.c).

**SOURCE — representations and direction.**

- A tmux pane is a PTY, not an adapter-owned PTY. tmux describes a session as a collection of PTYs and each pane as a separate PTY ([3.7c manual](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). At the kernel boundary, bytes written by the application to the slave become readable at the master; bytes written to the master are terminal input to the slave, and both directions are asynchronous ([Linux `pty(7)`](https://man7.org/linux/man-pages/man7/pty.7.html)). This supports the layer distinction, but does not establish ownership, semantic event boundaries, or durable delivery.
- `pipe-pane -O command` (the default when neither flag is set) connects **pane output** to the command’s stdin. `-I` reverses direction: command stdout is written into the pane “as if it were typed”; `-I` is injection and is outside this observer slice. One pane has at most one command pipe; installing another closes the prior pipe; no command closes the current pipe ([3.7c manual, `pipe-pane`](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). Thus `-O` is a prospective observation stream from tmux’s pane-output path, not terminal input, not a screen snapshot, and not a documented durable journal.
- `capture-pane` captures **contents of tmux’s pane screen/history representation** to stdout or a paste buffer. It can choose the alternate screen (`-a`), a mode screen (`-M`), attributes (`-e`), escaped nonprintables (`-C`), and whitespace/wrap treatment (`-N`, `-J`); `-P` exposes only an incomplete incoming escape sequence ([3.7c manual, `capture-pane`](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). It is therefore a rendered/state-derived snapshot, with options that materially alter its textual projection. It is not evidence of original application byte boundaries, input, or a time-ordered event log.
- Control mode is a separate text protocol. Commands receive `%begin…%end/%error` blocks, and notifications never occur inside such a command-output block ([3.7c manual, Control Mode](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). `%output pane-id value` says a pane produced output; nonprintables and backslash are octal-escaped. With `pause-after`, `%extended-output` includes a tmux buffering age in milliseconds, not source-production time or end-to-end freshness ([notification definitions](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). It carries pane output plus tmux lifecycle/layout notifications; it does not observe pane terminal input, nor supply an adapter’s independent PTY.

**Identity, ordering, loss, reconnect, and freshness.**

- **SOURCE:** Control notifications identify output with a tmux pane ID. The tagged implementation stores per-control-client offsets keyed by `wp->id`; its comment says output blocks hold later client-queue lines to enforce ordering while an output block is partially written ([control queues](https://raw.githubusercontent.com/tmux/tmux/3.7c/control.c)). This is an implementation fact for an attached client/server instance, not a durable cross-restart identity contract.
- **INFERENCE:** A usable identity binding needs the observed tmux server/socket identity, control-client attachment/session, pane ID, and a metadata snapshot from the same qualification interval. Names, indexes, and a bare `%N` must not be treated as durable identity. No reviewed source promises ID persistence through server restart, destruction/recreation, or reconnect; test it.
- **SOURCE:** With `pause-after`, tmux may send `%pause`, discard queued pane blocks, and later resume at the pane’s current offset; the code shows the discard and offset reset ([discard/off](https://raw.githubusercontent.com/tmux/tmux/3.7c/control.c), [age/pause path](https://raw.githubusercontent.com/tmux/tmux/3.7c/control.c)). Without pause mode, 3.7c’s tagged code exits a too-far-behind control client after its internal maximum age. These are explicit loss/discontinuity conditions, so control output cannot be claimed lossless. The public interface documents pause/continue and says a client may need `capture-pane` to refresh state; it does not offer replay.
- **SOURCE:** `refresh-client -A off` can stop output to the client and, if every client turns a pane off, tmux may stop reading that pane ([manual](https://raw.githubusercontent.com/tmux/tmux/3.7c/tmux.1)). This is backpressure behavior, not a completeness guarantee.
- **INFERENCE/untested:** `pipe-pane` order, write atomicity, buffering, error visibility, sink child exit, and retention after sink failure have no reviewed API guarantee here. Treat the sink as fallible and add wrapper-owned receipt timestamps/sequence numbers; those prove only receipt order at the wrapper, not source time.
- **INFERENCE/untested:** Control output is scoped to the client’s attached session (the tagged source gates output on the pane window being linked into that session); attachment changes, disconnect/reconnect windows, and multi-pane interleaving need a fixture. No freshness SLA exists: PTY is asynchronous, `%output` has no timestamp, and `%extended-output` age measures tmux buffering only.

**Smallest falsifying disposable fixture (planned; do not run now).** Create a new private tmux socket and one disposable pane with a deterministic helper that (a) writes a pre-hashed byte fixture containing markers, ANSI cursor/erase sequences, a split escape sequence, nonprintables, and alternate-screen transitions; and (b) separately records received stdin, so output and input have independent oracles. Start `pipe-pane -O` before marker 1 into a disposable sink and one control client before the same marker; retain their raw outputs. Compare: decoded control `%output` and the pipe sink against the independently pre-hashed application-output oracle; compare `capture-pane` only to a separately specified final-screen oracle, never to raw bytes.

Use the same fixture to: slow/stop the control reader until `%pause` or exit, then continue and capture state; terminate the pipe sink midstream; detach/reconnect the control client; and recreate a pane with the same name/index. Require explicit gap, restart, sink-failure, and identity-reuse markers. A single unexplained byte mismatch, missing/duplicated ordered marker, control gap without an emitted discontinuity record, sink failure masquerading as clean completion, or reused identity accepted as continuous falsifies the proposed “clean PTY source” claim. The fixture can qualify version-scoped observation provenance; it cannot discharge L14 D4’s missing relay verdict or establish an end-to-end relay.

---

## Head verification and bounded follow-up

Cartan independently observed `tmux -V` = 3.7c and `zellij --version` = 0.45.1 without server
contact. Opened the tagged tmux manual, tagged control implementation and Linux pty(7)
on 2026-10-22. The control source's queue comment supports its attached-client ordering
statement; pty(7) describes asynchronous directions. No fixture result is claimed.

Correction identified, inferred: Cartan — comparing application-write bytes to pane-output bytes
requires an explicit PTY termios boundary. Output processing such as ONLCR could transform
bytes before tmux sees them. A bounded text-only clarification was requested from the same
researcher; the raw response above remains unchanged. The reply below resolves the design
detail for P2, while all fixture execution remains planned.

### Researcher's clarification (verbatim)

**Correction:** no—comparing the helper’s pre-hashed `write(2)` payload directly to `pipe-pane` or decoded control `%output` is invalid unless the fixture pins and records the slave PTY’s output termios state.

**SOURCE:** Linux `termios` defines `OPOST` as output post-processing and `ONLCR` as NL→CR-NL translation ([termios(3)](https://man7.org/linux/man-pages/man3/termios.3.html)). A PTY slave write reaches its master asynchronously through the terminal line discipline ([pty(7)](https://man7.org/linux/man-pages/man7/pty.7.html)). Therefore the application-write boundary can differ from the tmux-observed master-byte boundary before tmux’s own control escaping/rendering. `capture-pane` remains a screen-state oracle only.

**Planned fixture correction:** make the independently oracled comparison boundary the bytes expected **at the PTY master after line discipline**, not merely the helper’s source payload. The fixture helper must set a known slave configuration before emitting markers—preferably disable `OPOST` for the byte-fidelity subcase—then emit a machine-readable `tcgetattr` record/hash immediately before and after emission. Retain the exact `c_iflag`, `c_oflag`, `c_lflag`, `c_cflag`, control characters, terminal size, tmux version/tag, and helper binary/payload hashes.

Then compare (1) pipe sink bytes and (2) decoded control payload bytes to that recorded post-termios oracle. A separate subcase with `OPOST|ONLCR` intentionally enabled should expect transformed wire bytes, proving the fixture detects the boundary rather than accidentally assuming it. The fixture must treat any termios-state mismatch/change as invalid evidence, not a failed tmux fidelity assertion.
