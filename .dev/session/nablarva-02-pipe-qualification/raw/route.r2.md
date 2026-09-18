---
kind: private-server read-route candidate
revision: r2
author: cartan
date: 2026-09-14
cycle: "03"
corrects: "02"
status: "Engineering for audit; UNVERIFIED-native; not opening, arming, or send authority"
point: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/03.oraculum.point.md
point_sha256: 2585464c53444a466b26994968db72fc77ee5cc944fe1e484b122d97b5a5bcc5
handoff_rule: "Immutable after RETURN; corrections need a new cycle/revision"
---

# Own a disposable endpoint; do not discover a working session's endpoint

The candidate is one private Unix WebSocket app-server and one native TUI attached to it.
The reader implements a bounded summary-only exchange. Neither a successful fake-server
test nor a successful future summary read qualifies the native delivery route. The owning
STATUS decision_rule remains default STOP until the separate live requirements are met.

No command under a **FUTURE** heading below was executed in cycle 03. No server or TUI was
started, no live interlock was minted or supplied, and no Codex socket was contacted. The
only socket activity permitted this cycle is POINT 03 §4's test-owned fake loopback.

## 1. Evidence and limits

Local, this cycle: `codex-cli 0.154.0`; version, root help, app-server help and queue help
all exit 0. Their full outputs, including the read-only-filesystem PATH-alias warning, are
in `../_bus/03.cartan.return.md` §2. Help is syntax evidence, not execution evidence.

Official sources checked 2026-09-14:

- `--remote` connects a TUI to an app-server. Unix transport uses a WebSocket HTTP Upgrade;
  its text messages carry JSON-RPC objects, whereas stdio uses JSONL. `thread/list` covers
  stored threads: `cwd` filters exactly and `useStateDbOnly: true` avoids scan/repair.
  `thread/read` with `includeTurns: false` does not resume or subscribe to a thread.
  `sessionId` denotes a tree root, not a running incarnation. These facts support the
  bounded protocol below, not proof of this particular target's visibility.
  [OpenAI App Server reference](https://learn.chatgpt.com/docs/app-server).
- `/status` documents settings and usage information; a remote TUI also shows remote
  address and server version. The current command reference's `--remote` supported-command
  list excludes `queue`, while this installed `queue --help` advertises `--remote`.
  This is an unresolved documentation/help mismatch, not permission to test a send now.
  [OpenAI developer command reference](https://learn.chatgpt.com/docs/developer-commands).
- ChatGPT login uses subscription access; API-key login uses usage-based access. Therefore
  the same user's Codex home implies, at most, an expectation of reused authentication:
  it does **not** establish subscriber usage. No credentials or configuration were read.
  [OpenAI authentication reference](https://learn.chatgpt.com/docs/auth).
- The wire implementation checks HTTP 101 and the accept digest, masks client frames,
  rejects masked server frames, and validates lengths/opcodes/UTF-8. This is a deliberately
  narrow client, not a claim of complete WebSocket conformance: fragmented/binary messages
  and unsolicited extensions are refused.
  [RFC 6455 §§4–5](https://www.rfc-editor.org/rfc/rfc6455.html).

Design inference: a dedicated server separates this transport and its in-memory clients
from working TUIs. It is **not** a separate user, configuration, authentication store or
persisted-thread database. Thus `thread/list` must not be an unfiltered discovery query.
Whether a newly opened remote TUI is immediately indexed under the expected source kind,
remains visible without a model turn, and is addressable by this build's remote queue are
all native observations still owed. Zero/multiple/mismatched results stop; no wider retry.

## 2. Exact binding and opening ladder — FUTURE, head-authored PAD only

| Item | Exact candidate |
|---|---|
| Host | `hruzam-120922` |
| Workspace | `/tmp/nablarva-b-entry-20260913-01` |
| Private socket | `/run/user/1000/nablarva-b-entry-20260913-01.sock` |
| Remote URI | `unix:///run/user/1000/nablarva-b-entry-20260913-01.sock` |
| Native display name | `nablarva-b-entry-20260913-01` (operator sets it; never used for resolution) |
| Test-only receiver | `probe_codex`; not a real BUS seat |

The pocket endpoint `/run/user/1000/codex-pocket-test.sock` is excluded, regardless of
whether it is listening. No adoption, inspection, connection, unlink or stop of it.
Working UUIDs `01a092ed-f422-7051-ba69-f6c1d47c57d8` and
`0a27e884-b106-48e6-b56a-71dcb271ab6f` are refused; the ia-sync TUI is additionally excluded
by STATUS's supplied suffix `9cea3c`. Its complete ID is unknown here, not discovered.

Oraculum first audits RETURN 03 and authors `pad.2-sitting-1.md`. The proposal for its
HANDS steps is sequential; each report and branch belongs in the PAD before release:

1. Reconcile prior work and approvals. Verify the existing scratch is still the exact
   empty, nonsymlink, user-owned mode-700 directory created in cycle 02. Do not recreate
   or clean it. Head checks the exact private path is absent and has no listening entry;
   an existing path, even a stale socket, stops this setup. No guessed replacement name.
2. Ask majkee for **open_approval only**: this sitting, this private endpoint, this workspace,
   one server and one attached TUI, default settings, with expiry/disarm conditions.
   Without it, no opening. Each terminal's actual cwd must be the scratch, not the repo.
3. In the designated server terminal, release exactly this foreground command:

   ```sh
   codex app-server --listen unix:///run/user/1000/nablarva-b-entry-20260913-01.sock
   ```

   Head's read-only check, before and after as separately released steps:

   ```sh
   ss -xl | rg -F -- '/run/user/1000/nablarva-b-entry-20260913-01.sock'
   ```

   The head must inspect the full address field for an **exact** match; `rg -F` alone is
   a substring filter, not an identity check. Expected: absent before, one listening entry
   after, plus an actual user-owned nonsymlink socket. An `ss` line is not incarnation proof.
4. In a separate designated native terminal, release exactly one fresh TUI:

   ```sh
   codex --remote unix:///run/user/1000/nablarva-b-entry-20260913-01.sock -C /tmp/nablarva-b-entry-20260913-01
   ```

   Majkee uses native `/rename` to set the display name, then `/status`. Record the actual
   UUID, cwd, host, opening time, remote endpoint/version, available effective settings,
   usage/login-path observation and current instance evidence. Observe whether the TUI
   remains usable. Do not copy account identifiers or credentials into the bed. No task,
   model turn, permission bypass, changed profile or login repair is part of opening.
5. Resolve **armed_target** from observation, never placeholders. UUID must be available
   **before** the first reader connection; if native `/status` cannot supply it, stop for
   a separately approved identity source. Do not use a tokenless `thread/list` or select
   its sole result to bootstrap identity. Missing settings/instance evidence remains
   unknown. Do not promote a PID, socket inode, `sessionId` or display name into a proven
   native incarnation fence. An incomplete required tuple is not an armed target.
6. Only when the head can record the required observed tuple, ask separately for
   **armed_approval: inspect**, scoped to one bounded read and expiring on any target or
   server change. Record actual launch evidence (§3); materialize the interlock only
   after that approval. Release the reader once (§4). Log the observed label and metadata;
   STOP on an uncertainty. No send is a branch of this first read-only sitting.

Expected subscriber route: reuse an existing **ChatGPT** login, if that is actually the
server's login mode. `/status` must be observed for the available plan/usage indicators;
if they do not establish the mode, subscriber usage is **unknown**, not inferred from the
home directory, lack of a key flag, or CLI exit. The reader makes no account/config RPC.

## 3. Launch evidence and connection interlock

Both `inspect` and `validate` require `--launch-evidence` containing **inline JSON**, not a
filename. The exact three-key record is:

```json
{
  "server_argv": ["codex", "app-server", "--listen", "unix:///run/user/1000/nablarva-b-entry-20260913-01.sock"],
  "target_argv": ["codex", "--remote", "unix:///run/user/1000/nablarva-b-entry-20260913-01.sock", "-C", "/tmp/nablarva-b-entry-20260913-01"],
  "inherited_profile": null
}
```

Only the executable spelling `codex` or `/home/hruzam/.local/bin/codex` is accepted; all
other tokens and their order are exact. No shell/env wrapper, unknown key or extra token.
This rejects `--dangerously-*`, `--approve-for-me`, `-a/--ask-for-approval never`, model,
profile, config, provider, sandbox, permission, feature and writable-root overrides,
including equals/joined forms. Required `-C` is case-sensitive and is not `-c`.

`inherited_profile: null` is a **supplied claim of absence**, not a discovered effective
default. Missing/non-null profile evidence is BLOCKED. A clean record cannot exclude a
misreported shell function, environment override or inherited setting. Observe native
effective settings where exposed and stop on any override signal or missing required
evidence. The reader does not read configuration, auth, environment dumps or histories
to turn unknown into absent. `validate` binds the canonical record's SHA-256 in its static
preview; it does not extend the unchanged fixture/tuple schema or authorize an action.

The `--allow-connect` format is defined in the probe header:

```text
nablarva-inspect-v1:<lowercase sha256 of socket-path UTF-8 bytes + one NUL byte + canonical lowercase UUID bytes>
```

This deterministic, public-data token is an intentional-action interlock, **not** a
secret, authentication, approval record, expiry or instance fence. There is no mint verb.
No valid token is materialized for invocation or supplied in cycle 03; the positive
loopback test calls the lower-level transport, not an armed CLI invocation.
Future approval still lives in the head-owned STATUS/PAD. Withholding a token prevents the
CLI connection, but changing/reusing the same path is not a valid rearming procedure.

Before any socket construction/connect: validate launch evidence, the canonical allowed
path, canonical nonworking UUID and interlock. Then check host and a real nonsymlink socket
with safe ancestors and expected ownership. Compare its filesystem identity around the
connection/read. These local checks reduce accidents; they do not atomically fence server
replacement or native target takeover. Any change stops without retry.

## 4. Reader commands and protocol — FUTURE inspection only

Exact shell shape, with deliberately invalid placeholders for the observed UUID/token:

```sh
python3 -B /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/qualify.py inspect --sock /run/user/1000/nablarva-b-entry-20260913-01.sock --thread '<observed UUID>' --allow-connect '<approved interlock>' --launch-evidence '{"server_argv":["codex","app-server","--listen","unix:///run/user/1000/nablarva-b-entry-20260913-01.sock"],"target_argv":["codex","--remote","unix:///run/user/1000/nablarva-b-entry-20260913-01.sock","-C","/tmp/nablarva-b-entry-20260913-01"],"inherited_profile":null}'
```

Each following object is one WebSocket text message. The client first waits for a valid
correlated initialize result, then notifies initialized, then waits for each read result.
This corrects POINT 03's loose “JSONL per frame” wording: no JSONL batch, newline-dependent
stream parser, extra `jsonrpc` field, second route, proxy or protocol fallback.

```json
{"id":1,"method":"initialize","params":{"clientInfo":{"name":"nablarva_qualification_probe","version":"0.2.0"}}}
{"method":"initialized","params":{}}
{"id":2,"method":"thread/list","params":{"cwd":"/tmp/nablarva-b-entry-20260913-01","useStateDbOnly":true,"limit":2,"sourceKinds":["cli","vscode","appServer"]}}
{"id":3,"method":"thread/read","params":{"threadId":"<observed UUID>","includeTurns":false}}
```

The first, filtered list must return exactly one entry, matching the supplied UUID and
workspace, with `nextCursor: null`. This is an acceptance constraint, not a prediction of
all server contents. No pagination, unfiltered retry, scan/repair, name resolution or
implicit thread creation. The read result's identity/workspace/status shape must agree.
An initialize response/version is transport evidence only; it is not an approval or login
proof. No `thread/start`, `thread/resume`, turn method, config/account read or subscription.

The stdlib transport has a five-second total deadline, 8-KiB HTTP header bound, 64-KiB
frame bound, 256-KiB cumulative received-frame byte bound and 32-received-frame bound. It validates the handshake,
handles partial reads and buffered bytes, uses fresh client masks and bounded ping/pong,
and closes on unsupported/malformed input. Notifications are bounded and discarded;
server-initiated requests (including approvals) are never answered. Raw errors, previews,
turns, message text and notification bodies are not emitted. Close is cleanup, not a task
send or a completion receipt.

Allowlisted summary: route/version if available, `id`, optional `sessionId`, `cwd`, status
type, `activeFlags`, optional `updatedAt`, plus fixed gate/uncertainty metadata. Version
missing means unknown. `sessionId` does not establish incarnation. Effective override
hints, if supplied by the response, are checked; absence of those fields proves nothing.

| CLI exit | Label | Meaning |
|---|---|---|
| 0 | `PREPARED` | `validate` only: static fixture/tuple/launch preview; not arming |
| 2 | `BLOCKED` | Missing interlock/evidence, unsafe launch, identity/path/protocol refusal |
| 2 | `STOP_NOT_IDLE` | Summary reports active, including approval activity |
| 2 | `STOP_ROUTE_UNKNOWN` | Thread state unavailable/not loaded/system error |
| 2 | `STOP_IDENTITY_UNKNOWN` | Idle summary read, but living incarnation/effective defaults remain unproved |
| 2 | argparse usage error | Invalid CLI grammar; no connection |

`read_route_observed: true` means a wire read succeeded, including against the fake server;
it never means native qualification. Every result remains `UNVERIFIED-native`.
`QUALIFIED_READ_ROUTE` from plan r1 §0c is reserved and **not emitted** by this revision.
Transport exceptions can be BLOCKED; a failure label never selects an alternate route.

Future static-validation shape (only after separately authorized fixture materialization):

```sh
python3 -B /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/qualify.py validate --fixture /tmp/nablarva-b-entry-20260913-01/qualification.point.md --tuple '<frozen tuple JSON>' --launch-evidence '<observed canonical launch JSON>'
```

Fixture placement/schema are unchanged. `raw/probe/fixtures/README.md` remains pinned
cycle-02 history; its unwired-reader/testing description is superseded here, not rewritten
under POINT 03's placement-only conditional permission. The scratch remains empty now.

## 5. What this replaces; what is still not qualified

Plan r1 §0c's **existing control socket** candidate is replaced by the explicitly approved
private server above. Its identity, permission, UI and noninterference requirements remain.
The server/TUI opening allowance is the three-stage STATUS ladder, not a daemon discovery
exception. Plan r1 §0d remains wholly native work: acknowledgement, boundary-time busy and
approval rejection, incarnation fence, recovery lookup and one carrier's serialization.
No fixture callback test or idle snapshot establishes any of them.

Later, only under a separate audited **armed_approval: send-once**, the installed-help
candidate for the actuator is (NOT RUN; placeholders are not an armed invocation):

```sh
codex queue --remote unix:///run/user/1000/nablarva-b-entry-20260913-01.sock --thread '<observed UUID>' --message 'Read and act on /tmp/nablarva-b-entry-20260913-01/qualification.point.md — you are test fixture probe_codex; resolve your fixture identity first.'
```

The future sitting must settle the doc/help mismatch on **this private server**, capture
the actual acknowledgement/correlation, observe the same native TUI and exact worked
RETURN, and independently establish native admission/instance guards before claiming GO.
If a scoped characterization is needed first, it needs its own approval/fixtures and must
not be mislabeled the successful operational send. An error, timeout or missing ack after
possible submission means reconcile; never retry or switch carrier automatically.

Current unknowns: target UUID/instance; live indexing/source-kind behavior; actual remote
queue support and semantics; effective settings/profile absence; actual subscriber usage;
native UI noninterference; atomic admission and incarnation protection; correlated receipt
and worked RETURN. No proxy, terminal injection, hook or automatic delivery was added.
