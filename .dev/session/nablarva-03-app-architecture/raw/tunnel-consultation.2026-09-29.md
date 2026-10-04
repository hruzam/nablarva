# Existing consultation carriers — fresh opinion or continued conversation

Cartan · 2026-09-29 · source inspection and dated evidence, no live invocation.
Revised after [Flight's RETURN 01](../_bus/01.flight-executioner.return.md), verified in
[Cartan's separate VERDICT](../_bus/01.cartan.verdict.md). The earlier mapping of all
second-opinion work to the tunnel was too broad.

Majkee supplied the [tunnel-upgrade card](/home/hruzam/reposoma/_cold-start/card/CS.tunnel-upgrade.2026-09-21.md)
for a **Claude-initiated consultation ticket with a Codex reply**. The use can be a
flat Claude bus or a planner seeking another view. Preserve that useful one-way
initiation while selecting the carrier according to the context the reply needs.

## Route by the kind of consultation

| Need | Existing carrier | Context and boundary |
|---|---|---|
| Fresh, position-free second opinion | Vega relay → `codex-run.zsh` | New `codex exec --ephemeral` invocation; the Vega brief excludes the caller's preferred answer. |
| Fresh adversarial review of a plan | Mirror relay → `codex-run.zsh` | New invocation; Mirror deliberately receives the plan and reasoning to challenge. |
| Follow-up needing earlier turns | `tunnel-codex.zsh` | Explicitly selected stored thread, created on first send or resumed later; conversation continuity is intentional. |

This follows the [tunnel guide's routing](/home/hruzam/reposoma/raw.guides/tunnel/GUIDE.md:17),
[Vega](/home/hruzam/ia-sync/claude/agents/vega.md),
[Mirror](/home/hruzam/ia-sync/claude/agents/mirror.md) and their
[shared relay contract](/home/hruzam/ia-sync/zsh/guides/codex-relay.contract.md).
These are existing Claude-side roles, not a new roster for the animal.
Fresh invocation avoids reusing earlier thread turns; it does not by itself establish
independent judgment. The supplied brief, shared files and role instructions still matter.

Both carriers return through the waiting caller's tool invocation. Neither needs a
second wake merely to return that call's result. An interrupted caller still needs
recovery. Neither carrier is delivery into an already-running interactive Codex seat,
which remains the separate **living-peer exchange** qualification track.

## What the implementations actually provide

| Property | Fresh relay: `codex-run.zsh` | Continuity tunnel: `tunnel-codex.{zsh,py}` |
|---|---|---|
| Codex entry | `exec --json --ephemeral`, no resume | One app-server subprocess per verb; start or resume the stored thread |
| Default sandbox | `workspace-write` | `read-only`; thread start sets `approvalPolicy: never` and unsolicited approvals receive an error |
| Opening | Caller permissions and assigned relay scope; no tunnel enable step | Explicit state selection and operator `open --enable`; absent selection exits 13 |
| Wait | `CODEX_TIMEOUT`, default 300 seconds per attempt | `TUNNEL_CODEX_TIMEOUT`, default 120 seconds for individual response waits and the drive-turn deadline |
| Reply handling | Requires a `turn.completed` event and extracts final message/usage | `ask` checks the completed turn by read-back and compares final text; mismatch exits 50 |
| Input | Accepts argv or stdin, then passes the collected prompt as one argv string | Only the first positional prompt string; no stdin/file option |
| Retry | One retry when the raw output is empty | No automatic retry in the inspected ask path |

Source: [fresh relay](/home/hruzam/ia-sync/zsh/ai/codex-run.zsh),
[tunnel transport](/home/hruzam/ia-sync/zsh/ai/tunnel-codex.py:168),
[approval and thread start](/home/hruzam/ia-sync/zsh/ai/tunnel-codex.py:306),
[ask](/home/hruzam/ia-sync/zsh/ai/tunnel-codex.py:619),
[state selection/gate](/home/hruzam/ia-sync/zsh/ai/tunnel-codex.zsh:194).
These are inspected implementation facts, not a new current-version behavior certificate.

The fresh relay's writable sandbox and empty-output retry are material differences,
not properties inherited from the tunnel. A read-only architecture consultation must
retain its assigned scope. Before adopting either wrapper as a general ticket carrier,
account for its actual permissions, failure handling and retries; do not infer an
exactly-once guarantee. This study invokes neither wrapper.

Both append a usage line to the result. A file-backed ticket consumer must preserve
and distinguish that metadata. Raw stdout is not already a POINT/RETURN envelope;
transport agreement and a usage tail do not prove that the answer is correct.

## Tunnel limits that the architecture must retain

- **Wait and interruption.** The default is configurable, not a fixed two-minute
  maximum for every call. Each response wait and the turn-driving phase have their
  own deadlines, so whole-call duration can differ. On an exception, `finally`
  closes the transport and terminates its subprocess. The September 4/10 field notes
  report interrupted turns after driver loss; stored history does not guarantee an
  in-flight turn survives. An outer tool timeout is a separate limit. Backgrounding
  alone does not remove the shim's own deadline.
- **Cold-thread handle loss.** A newly allocated thread ID is held in memory until
  after drive/reconcile succeeds. An earlier exception can leave the old state with
  `threadId: null` although a thread was allocated. On resume the thread ID is already
  stored, but the latest turn ID can remain stale. A text mismatch saves state before
  raising exit 50. The September 10 cold failure fits the new-thread failure window;
  an orphaned thread is an inference, not something inspected or reproduced here.
- **Timeout exit disagreement.** Current source maps `ProtocolError` to exit 30;
  the September 10 observation records exit 0 twice. Which layer produced that zero
  remains unresolved. Do not accept exit 0 or a usage tail alone as delivery proof;
  require the expected completed, correlated answer and preserve uncertainty on error.
- **Input boundary.** `tun ask hello world` is parsed as the prompt `hello`; later
  words are silently ignored by the inspected zsh code. A caller must pass exactly
  one literal prompt string safely. Neither route avoids the per-string exec limit:
  even the fresh relay's stdin mode becomes argv internally. The local Linux UAPI
  header defines `MAX_ARG_STRLEN` as 32 pages; this host reports 4096-byte pages,
  corresponding to 128 KiB including the terminating NUL. No size-limit execution
  probe was run. Shell text is not an arbitrary-byte file transport.
- **Concurrent use.** State replacement uses a fixed sibling `.tmp` and has no
  per-handle writer arbitration. Keep one caller and one in-flight request per handle
  for the bounded proposed use; atomic replacement alone is not a concurrency guard.
- **Ownership-aware close.** The shim removes only its selected handle file. It does
  not delete Codex writer locks or retire the thread. The planned close-time handle
  printout is absent; closing can discard the convenient reference to that conversation.

The [September 10 observation](/home/hruzam/reposoma/raw.guides/tunnel/src/observation.app-server-wait.2026-09-10.md)
and [field journal](/home/hruzam/reposoma/raw.guides/tunnel/dev-journal.tunnel.md)
are dated reports, not substitutes for the current source. In particular, reported
6/27-second waits must not be equated to the entire turn budget: the current driver
passes its remaining deadline to the wait function.

## What is proven, installed and still pending

The [September 3 PASS receipt](../../../../toolbox/termbrana/research/evidence/t06-tunnel-v0-roundtrip.md:154)
proves **send plus read-back**, on codex-cli 0.152.1, including independent checking
of the returned claim. It does **not** prove the later `ask` implementation:
ia-sync commit `5a0a59f` added `ask` on September 3 at 15:24, after that receipt.
The failed completed-turn steer remains part of the evidence. Later journal reports
mention `ask`; they are not the same controlled PASS receipt.

The office launcher `/home/hruzam/.local/bin/codex` resolves into the standalone
`0.158.0-x86_64-unknown-linux-musl` release directory. This is install-path evidence;
the binary was not executed. The shim's observed pin is 0.152.1 and the upgrade card
addresses 0.154.0. Compatibility with the resolved installation remains unverified.

Source and live office copies match byte-for-byte, checked 2026-09-29:

| File under ia-sync/zsh/ai and ~/.config/zsh/ai | SHA-256 |
|---|---|
| `tunnel-codex.py` | `75226a2c10eb932bb3716c8f2f804250b38f201969b2aacb64cbe6b8cbfef163` |
| `tunnel-codex.zsh` | `0863bc467221c184ff3b581d197616fa7f48b7369c2ebcd0529b267549bd40eb` |
| `codex-run.zsh` | `6f5156fb7fdabe6f36d0853580805eda5e46c5075c8ef297e2ea7c5f0c03da65` |

Installed bytes do not prove current alias resolution, an enabled vault or behavior.
The old shim “not deployed” comment conflicts with those observed live files.

The [upgrade STATUS](/home/hruzam/ia-sync/.dev/session/tunnel-upgrade-01-parametrization/STATUS.md)
owns its separate gate. Its T1 progress wording conflicts internally and with the
newer card. T2's `-c` passthrough, `--vault`, occupancy percentage and close-time handle
printout are absent from current source. Report those discrepancies to that owner
when the work is resumed; do not silently repair its STATUS or widen T2 from this bed.

Likewise, [HANDSHAKE §TABLE](/home/hruzam/ia-sync/HANDSHAKE.md:95) still says countersign
pending, but the later [Cartan amendment](/home/hruzam/ia-sync/HANDSHAKE.md:166) is
present in that same file. That is stale routing prose, not an absent countersign.
The relay contract's old retry-description prose also differs from current code;
inspect the actual wrapper rather than carrying that implementation detail forward.

## Place in the animal and next boundary

**Consultation** has two candidate carriers: fresh relay for a planner's new opinion;
continuity tunnel for a conversation that needs its earlier turns. **Living-peer
exchange** remains a separate capability with its existing native-activation gate.
A common roller may present all three experiences while keeping their actual context,
permissions, endpoints and evidence distinct. No additional daemon or routing schema
is required merely to make this distinction.

This is a documentation amendment. Mechanical work belongs with the existing ia-sync
owner or a successor that owner scopes; no implementation is opened here.
A successful future `ask "ping"` could provide a narrow current-version smoke test.
It cannot settle a timeout-exit disagreement because it does not exercise timeout.
That needs a separate direct-exit observation on a controlled timeout path; local
fixtures may establish source/wrapper behavior without quota, while claims about live
cancellation or thread recovery require their own authorized evidence. No probe is
requested or run by this note, and no operator enable is inferred from the review.
