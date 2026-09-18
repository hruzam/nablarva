---
kind: candidate route evidence
revision: r1
author: cartan
date: 2026-09-13
point: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/02.oraculum.point.md
point_sha256: 981fd4881441e122e9f09b7707724800c504e00cef736b20b6c875bb105248e1
disposition: "PARTIAL — offline validation built; live observer unwired, STOP_ROUTE_UNKNOWN"
authority: "evidence for Oraculum's audit; no PAD release, arming, native qualification, or gavel"
---

# Route r1 — do not connect from this revision

The installed CLI is `0.154.0`; the attached daemon's version, existence, concrete
default socket path and target membership are **unknown**. Help is not a daemon probe.
No connection, thread read, daemon operation, target launch or send ran in POINT 02.

The requested live `inspect` is **not implemented**: it refuses before any transport
action. This is a partial engineering return, not successful completion of the requested
bounded live reader. Its offline semantic parser and static validator are testable.
`QUALIFIED_READ_ROUTE` is reserved and never emitted by this revision.

## 1. What the permitted sources establish

The App Server wire omits `jsonrpc`. Stdio uses JSONL; Unix sockets use WebSocket plus
HTTP Upgrade. Initialization uses client metadata, then `initialized`. Summary
`thread/read` neither resumes, subscribes, loads the thread nor emits
`thread/started`. [Protocol, initialization and thread read](https://learn.chatgpt.com/docs/app-server).

The CLI documentation names symbolic `unix://` for the default socket and
`unix://PATH` for an explicit one. It does not supply hruzam's concrete Linux pathname
in the consulted sections. [Developer commands — App Server](https://learn.chatgpt.com/docs/developer-commands#codex-app-server).

The local `proxy --help` below accepts `--sock <SOCKET_PATH>` and describes a proxy
of stdio bytes to a **running** control socket. It does not document whether those
bytes are raw WebSocket traffic, JSONL translated into frames, or another client
convention. Consequently, piping plain JSON lines to the proxy is **not established
as valid**. No pathname has been guessed from another socket, user, platform or session.

### Exact semantic messages, not a transport command

Offline example only. The UUID below is synthetic, not an armed target. A future reader
must wait for the matching successful initialization response before emitting the
notification and read request; constructing this list does not establish that ordering
on a live transport.

```json
{"id":1,"method":"initialize","params":{"clientInfo":{"name":"nablarva_qualification_probe","version":"0.1.0"}}}
{"method":"initialized","params":{}}
{"id":2,"method":"thread/read","params":{"threadId":"12345678-1234-1234-1234-123456789abc","includeTurns":false}}
```

The client version is this disposable probe's metadata, **not** a measured server
version. These payloads follow the [App Server initialization/read contract](https://learn.chatgpt.com/docs/app-server#initialization);
none was sent.

| Returned field | Documented meaning / handling in this candidate |
|---|---|
| `result.thread.id` | Exact correlation key; mismatches stop. |
| `thread.sessionId` | Session-tree root, not an incarnation fence. Never substitute it for the requested ID. |
| `thread.status.type` | `notLoaded`, `idle`, `systemError`, `active`. |
| `thread.status.activeFlags` | Nested under active status; missing is not fabricated as an observed empty list. |
| `thread.updatedAt` | Numeric in examples; resume alone does not update it. Missing remains unknown, not a liveness clock. |
| Initialization result | Describes user agent/platform, not a guaranteed structured daemon-version field. |

Field evidence: [App Server threads and initialization](https://learn.chatgpt.com/docs/app-server).
The parser is a narrow offline candidate, not a generated complete vendor schema.
Unexpected envelopes, correlation or status shapes stop. It does not print conversation
previews, messages, turns or other arbitrary response content.

## 2. Unknowns that block STEP 0c

| Question | This cycle's result | Consequence |
|---|---|---|
| Concrete default socket for this user | **Not documented in the consulted sources; not discovered locally.** | No materialized `--sock` value. A symbolic URL is not a filesystem pathname. |
| Proxy stdin framing and handshake responsibility | **Not documented by installed help.** | No JSONL-to-proxy recipe. The known socket transport alone does not prove proxy translation. |
| Missing/stopped daemon | **Not observed; error text, exit code, timeout and autostart behavior unknown.** | A generic connection failure cannot be labeled “daemon absent.” No start/restart fallback. |
| Existing daemon or CLI version correspondence | **Not observed.** | Local CLI version cannot attest a running server. |
| Whole-client noninterference | **Not observed.** | Method-level documentation is not proof that connecting/disconnecting this client leaves other native UIs/subscriptions intact. |
| Live target identity, idle state, permissions or instance | **No target armed or inspected.** | A UUID-shaped string and mock idle status do not qualify identity. |
| Native bounded-read behavior | **Not implemented or exercised.** | Future timeout/byte/frame bounds need real transport implementation and tests; offline parser bounds alone do not supply it. |
| Native submission/acknowledgement/incarnation guard | **Not documented here or exercised.** | No operational send release, even if a later read succeeds. |

Inference: a summary-only method is the appropriate candidate observation, but the broader
“cannot disturb either working session” claim is **unverified**, not guaranteed. Both working
UUIDs are denied by the probe. It must never connect to them as a characterization shortcut.

**Exact executable STEP 0c command: none releasable from this revision.**
The CLI shape `inspect --sock <path> --thread <uuid>` exists, but all invocations stop
without connecting. Supplying a plausible path does not unlock it. Do not put this shape
into a live PAD as if a successful read were possible.

Current executable verification is offline only:

```sh
python3 -B /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/test_qualify.py
```

Future work needs a separately scoped POINT resolving the version-pinned route/proxy contract
and completing the bounded reader, followed by audit. Connection approval remains separate.
No schema generation, socket search, runtime listing, credential lookup, source download or
fresh app-server launch is implied by this recommendation.

## 3. Queue: local help is the available CLI contract

Search scope on 2026-09-13: the official
[CLI reference](https://learn.chatgpt.com/docs/cli/reference),
[Developer commands](https://learn.chatgpt.com/docs/developer-commands) and
[App Server reference](https://learn.chatgpt.com/docs/app-server).
There is no `codex queue` contract in those consulted pages. This is a bounded search
result, not proof that no documentation exists anywhere.

The documented **interactive** behavior is different evidence: Tab defers a follow-up,
slash command or shell command until the next turn; Enter injects into active work.
Queued slash commands are parsed when run. These statements do **not** establish the
CLI subcommand's behavior. [Developer commands — interactive shortcuts](https://learn.chatgpt.com/docs/developer-commands#interactive-shortcuts).

For `codex queue`, the following are **not documented** by the consulted evidence:
route selection/default daemon, no-daemon behavior/autostart, target ambiguity resolution,
delivery versus acceptance acknowledgement, native turn correlation, busy/approval rejection,
atomic incarnation matching, duplicate suppression, restart recovery, cancellation, timeout,
UI/subscription effects and usage attribution. The advertised UUID-or-exact-name interface
does not solve those questions. This bed permits UUIDs only.

A documentation/help mismatch also remains open: the general developer-command reference's
remote-mode supported-subcommand list excludes queue, while local queue help advertises
`--remote`. Neither text proves that this installed subcommand honors that option.
[General remote option](https://learn.chatgpt.com/docs/developer-commands).

Other uses of “queue” in API prose (such as queued MCP refresh work or transport overload)
are not a message-delivery contract for `codex queue`. No timing, rejection or acknowledgement
property is imported from those unrelated mechanisms.

### Verbatim installed queue help

Command: `codex queue --help`. Exit: `0`. Combined tool output, warning included;
stdout/stderr were not separately captured by Cartan. This was the **only** queue
invocation; no assignment was supplied.

```text
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
Queue a message for an existing session

Usage: codex queue [OPTIONS] --thread <THREAD> --message <TEXT>

Options:
      --thread <THREAD>
          Session UUID or exact session name

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --message <TEXT>
          Message text to queue

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

      --remote <ADDR>
          Connect the TUI to a remote app server endpoint.
          
          Accepted forms: `ws://host:port`, `wss://host:port`, `unix://`, or `unix://PATH`.

      --remote-auth-token-env <ENV_VAR>
          Name of the environment variable containing the bearer token to send to a remote app
          server websocket

  -i, --image <FILE>...
          Optional image(s) to attach to the initial prompt

  -m, --model <MODEL>
          Model the agent should use

      --oss
          Use open-source provider

      --local-provider <OSS_PROVIDER>
          Specify which local provider to use (lmstudio or ollama). If not specified with --oss,
          will use config default or show selection

  -p, --profile <CONFIG_PROFILE_V2>
          Layer $CODEX_HOME/<name>.config.toml on top of the base user config

  -s, --sandbox <SANDBOX_MODE>
          Select the sandbox policy to use when executing model-generated shell commands
          
          [possible values: read-only, workspace-write, danger-full-access]

      --approve-for-me
          Route approval requests through automatic review using the workspace-write sandbox

      --dangerously-bypass-approvals-and-sandbox
          Skip all confirmation prompts and execute commands without sandboxing. EXTREMELY
          DANGEROUS. Intended solely for running in environments that are externally sandboxed

      --dangerously-bypass-hook-trust
          Run enabled hooks without requiring persisted hook trust for this invocation. DANGEROUS.
          Intended only for automation that already vets hook sources

  -C, --cd <DIR>
          Tell the agent to use the specified directory as its working root

      --worktree
          Run the session in a new managed Git worktree

      --add-dir <DIR>
          Additional directories that should be writable alongside the primary workspace

      --strict-config
          Error out when config.toml contains fields that are not recognized by this version of
          Codex

  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

  -h, --help
          Print help (see a summary with '-h')
```

## 4. Other installed command evidence

Observed by Cartan on host `hruzam-120922`, current Codex sandbox frame,
at the CLI-help batch clock `2026-09-13 21:38:44 UTC` (23:38:44 CEST).
All three commands below exited `0`. No daemon subcommand was executed.

`codex --version`:

```text
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
codex-cli 0.154.0
```

`codex app-server proxy --help`:

```text
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
Proxy stdio bytes to the running app-server control socket

Usage: codex app-server proxy [OPTIONS]

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

      --sock <SOCKET_PATH>
          Path to the app-server Unix domain socket to connect to

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

  -h, --help
          Print help (see a summary with '-h')
```

`codex app-server daemon --help`:

```text
WARNING: proceeding, even though we could not create PATH aliases: Read-only file system (os error 30)
Manage the local app-server daemon

Usage: codex app-server daemon [OPTIONS] <COMMAND>

Commands:
  bootstrap               Install durable local app-server management for SSH-driven use
  start                   Start the local app server daemon if it is not already running
  restart                 Restart the local app server daemon
  enable-remote-control   Enable remote control for future starts and a currently running managed
                          daemon
  disable-remote-control  Disable remote control for future starts and a currently running managed
                          daemon
  stop                    Stop the local app server daemon
  version                 Print local CLI and running app-server versions as JSON
  help                    Print this message or the help of the given subcommand(s)

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

  -h, --help
          Print help (see a summary with '-h')
```

The PATH-alias warning is an observed property of these help invocations in this frame,
not evidence about a daemon, queue delivery, or another seat's environment. Oraculum's
Assay rerun with empty stderr remains separately attributed evidence; neither observation
erases the other.

