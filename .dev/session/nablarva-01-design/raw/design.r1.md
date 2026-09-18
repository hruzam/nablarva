---
kind: design-candidate
revision: r1
date: 2026-09-12
author: cartan
cycle: "01"
point: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-01-design/_bus/01.oraculum.point.md
status: proposed — no build, trial, deployment, or canon lock authorized
---

# Nablarva — attach first, qualify one pipe next

## Boundary

**Recommendation (proposal):** one same-host, one-bed attachment/preparation increment,
only if a static rehearsal beats the existing carry; then a separately authorized native
dispatch trial. Keep the independent full sessions; do not build a replacement IDE or a
third BUS-writing agent. The operator-signalled transcript pickup now in use is also a
zero-build comparator: it reduces carriage without automating attention.

| Step | Delivers | Does not claim |
|---|---|---|
| A — first build | Explicit local bindings for the head and one worker; selected POINT preview and deterministic context-copy; existing RETURN navigation | Activation, liveness, delivery, or an automated pipe |
| B — first pipe qualification | Operator-triggered dispatch to the bound living Codex session, worked RETURN at the POINT's exact path, head reads/audits it | Automatic wake of the Claude head; bidirectional or unattended operation |
| C — only if B earns it | Qualify native activation of the head, then additional pairings and recovery policy | A commitment to those builds or to cross-host scope |

In A, reuse the existing Python browser's bed/node selection, reader, clipboard helper,
and BUS navigation. Keep its current y/Y/R behavior. Add a separate prepared-handoff
preview/copy action; no generated command is executed. Binding mutation and strict
validation belong in one small sibling module, proposed `runbook_bindings.py`, not in
the display parsers. A has **no sender implementation**; B may add a bounded activation
function to that module after qualification. No daemon, registry service, plugin framework,
model call, automatic discovery sweep, or background watcher is needed for A.

For this existing-tool extension, propose source `/home/hruzam/ia-sync/zsh/session/`,
reviewed deployment to `~/.config/zsh/session/`, with Trajectory's timing agreement.
This follows the [session-browser source contract](/home/hruzam/reposoma/raw.guides/session-browser/GUIDE.md).
It is **not** a ruling that all future Nablarva organs must be authored in ia-sync:
[flag L6](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:27) explicitly distinguishes
experimental shapes here from structural builds on the surgical table. The operator's
public September 12 clarification reaffirms ia-sync for deployment to zsh/harness layers;
this extension fits that route. The launcher's blanket attribution to L6 is broader than
the flag, and must not silently settle the home of unrelated future organs. A's proposed
module and local filename had no collision in the scoped September 12 name sweep;
they remain candidate names, not a public namespace or global identity scheme.

## Binding record

**Proposal:** one `runbook-bindings.local.json` beside the owning RUNBOOK, explicitly
gitignored before first creation. JSON avoids silently reusing display-grade YAML parsing.
One operator-owned writer; atomic replacement with old-generation comparison and exclusive
write arbitration. A competing writer loses visibly. Seats do not self-attach by emitting
a file. Permission scope is local-user only; reject symlinked/foreign-owned binding files.

Minimal shape, not a populated attachment for this sitting:

```text
schema: runbook-bindings/v1
bed: canonical absolute bed path
host: exact local host
head: RUNBOOK seat key
generation: locally increasing binding revision
seats[seat]:
  workspace: canonical absolute working root
  runtime: codex-cli | claude-code-cli
  session_id: exact full-session identifier, or null when not established
  endpoint: {kind, value, route} | null
  incarnation: observed runtime-instance discriminator | null
  bound_at: ISO-8601 timestamp with zone
  bound_by: majkee
  evidence_locator: optional host-local public transcript path (read-only, never a send address)
```

The operator selects a seat from this RUNBOOK and supplies/confirms the full session's
own identifier. `endpoint` is adapter-specific: a Codex thread UUID plus its verified
local daemon route is not the same thing as a Claude runtime peer address. No guessed
socket path, display-name fallback, wildcard, `--last`, or credentials in the record.
An optional terminal locator may help the operator find the native UI but never enables
an action. Model labels are allocation, not endpoint identity.

The bed identifies the assignment namespace; workspace identifies where tools act;
seat identifies responsibility; session ID identifies conversation continuity;
incarnation identifies the currently attached runtime instance. A resumed conversation
may keep its session ID while its incarnation changes. `bound_at` is an observation,
not a lease or proof of readiness. Null/unknown incarnation or route means **manual only**.
Freshness requires revalidation, not a wall-clock TTL. On restart, replacement, changed
host/workspace/route, ambiguity, or loss of runtime evidence, require explicit rebinding
and invalidate every prepared preview. Rebinding never resends a POINT.

Today Cartan's own ID is observed as `01a092ed-f422-7051-ba69-f6c1d47c57d8`; `%50`
is only its environment-reported pane locator. STATUS now supplies Oraculum's public
transcript locator (file UUID `0a27e884-b106-48e6-b56a-71dcb271ab6f`), and one bounded
public-text read succeeded after majkee's signal. This resolves the earlier title-only
pointer `ff-nabl.oraculum-oStar.nablarva-flat`, not a live sending endpoint or verified
incarnation. No operational binding file is created by this design.

An evidence locator can support operator-signalled pull: allowlisted public user/assistant
text only, one bounded read per signal, no private reasoning, log-command replay, copied
transcript archive or background poll. Unknown vendor log schema stops extraction. It is
read-side attachment evidence, not a delivery binding; filename counts establish mentions
only. Missing attention or access stays visible instead of being inferred from file growth.

The handle borrows the bed's lifecycle, following the **DRAFT**
[cross-vendor-seat precedent](/home/hruzam/reposoma/raw.guides/runbook/res/cross-vendor-seat.md),
not its instrument taxonomy as new law. Detach removes only this tool's local binding;
it never stops, archives, or deletes the vendor session. Another host starts unbound.
The gaveled presence board remains unchanged and advisory; its `attachment_id` is not
this endpoint and provides no delivery authority.

## Correlation

**Proposal:** one outstanding assignment per bound worker in this first increment.
The exchange key is the canonical POINT path plus its declared cycle and exact
`return_to:`. No new exchange ledger, ACK file, fourth BUS kind, or purpose composer.
The mission reference is the owning RUNBOOK path, not generated motivational context.

Before preparation, strictly validate the selected POINT's frontmatter, `to:`, cycle,
read/write scope, and `return_to:` against this bed and selected binding. Reject duplicate
keys, malformed values, ambiguous seats, cross-bed return paths, symlink escapes, and an
existing RETURN. Do not infer these fields from the filename or STATUS display parser.
Failing validation does not change ordinary browsing/copying, but produces no validated
handoff. Bound the input size; use strict UTF-8, not replacement decoding, for this action.

The preview shows bed, sender, receiver, full-session ID, binding generation, POINT,
RUNBOOK, STATUS and exact RETURN path. The copied text is a fixed template containing
those pointers and the seat guard: read the POINT, resolve the expected full seat before
acting, obey its limits, return only at its declared path. It adds no authority to the
POINT. Recheck the selected inputs' bytes and binding generation immediately before copy
or later dispatch; changed inputs require a new preview. Hashes detect change, not authorship.

Receiver proves consumption through its worked RETURN: bind it to the POINT/cycle/seat,
state actual session identity and work evidence, and stop on mismatch. The head checks
content and cited artifacts, not just this declaration. RETURN publication should be
complete and exclusive; an existing/partial/unbound file is an attention condition, not
something the carrier repairs. No transcript copying or automatic RETURN manufacture.

## Native/reuse evidence

**Observed 2026-09-12, office; exact commands/outcomes in RETURN §2.**

| Interface | Evidence and limit |
|---|---|
| Codex CLI 0.154.0 | Installed `codex queue --help` exposes `--thread` and `--message`, with optional remote route. This is a native candidate, not an executed delivery. The fetched official CLI reference did not document this subcommand; do not invent its acknowledgement, retry, busy-state, or billing semantics. |
| Claude Code 2.1.269 | Installed version/help observed. Official [cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging) documents independent-session ListAgents/SendMessage, live peer discovery and inbound hold/refusal. This is not child-only. Its socket section does not supply a complete foreign-client message/ack contract. Oraculum's live reachability, policy and usage path were not tested. |
| Claude completion | Official [Stop hook input](https://code.claude.com/docs/en/hooks#stop) includes `last_assistant_message`, with common `session_id` and `transcript_path`. Stop excludes user interrupts; transcript writes can lag. A turn-final notification is not a correlated RETURN or acceptance. No hook installed or exercised. |
| Codex completion/read-back | Official [app-server](https://learn.chatgpt.com/docs/app-server) documents thread status, approval flags, `turn/completed` terminal status and `thread/read` without resuming. Events must match the bound thread and turn; `turn/steer` changes active work, not an idle-only dispatch. No live connection was made. |
| Headless alternatives | Installed `codex exec --help` exposes JSONL; [non-interactive docs](https://learn.chatgpt.com/docs/non-interactive-mode) describe its turn/item events. `codex exec` and `claude -p` are not delivery into the already-running interactive seat. Mode alone does not prove billing; neither is a silent fallback. |
| Existing browser | Source and office deployed bytes match SHA-256 `266dcb0d3e23c9b381a20c0970dd7a6f47b642ded1e07a67c08d07244138c9c9`. `render_bus_group` and y/Y/R are navigation/copy, never readiness or acceptance. No new selftest/TUI run claimed. |
| Existing tunnel | [tunnel guide](/home/hruzam/reposoma/raw.guides/tunnel/GUIDE.md) and [t06 evidence](/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/research/evidence/t06-tunnel-v0-roundtrip.md) prove a bounded stored-thread workflow on 0.152.1, not attachment to today's living TUI. Reuse reconciliation principles; do not transplant the per-verb server or unfiltered message collector. |

**Inference/recommendation:** qualify Codex queue first; if it cannot fence the selected
incarnation and reject unsafe state, investigate an existing local app-server's supported
attachment path. Do not start another server and assume it owns this TUI's living thread.
Do not promote an idle observation into an atomic send guarantee: an idle-to-busy race
must be rejected by the qualified mechanism or that mechanism remains manual-only.

For external activation of Claude, [Channels](https://code.claude.com/docs/en/channels)
is a documented MCP-based option, but entails a configured component; it is not an already
qualified arbitrary-peer socket client. Compare that incremental cost only after B.
Do not add another Claude session merely to relay into Oraculum.

Both external activations are **not** established here. A and the native-only B proposal
leave L4 untouched. Contingent exception request, **not selected**: if native activation
fails qualification, would majkee permit one operator-confirmed, path-only terminal
doorbell into one named endpoint in a separate disposable trial, with no payload injection,
UI parsing, approval response, interrupt, automatic retry or fallback? Path-only describes
content, not safety: send-keys still submits terminal input. Flag L4 has no explicit
doorbell carve-out. If readiness cannot be established without fragile screen heuristics,
do not conduct that trial. A rejected exception leaves manual carriage available.

Historical [Costa Probe A](/home/hruzam/unikuklatrix/nablarva/meshup/grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md:97)
was a designed one-shot/fresh-session experiment, not evidence this living-session pipe ran.

## Uncertainty after submission

**Proposal:** retain these separate observations; they need not arrive in this order.

| Observation | Sufficient evidence | Never implies |
|---|---|---|
| Prepared | Validated pointers/binding preview | Clipboard success or send |
| Submitted | Qualified carrier's positive acknowledgement for this exact target/input | Receiver consumed it |
| Consumed | Bound receiver's worked response or correlated runtime input observation | Work succeeded |
| RETURN present | Exact path contains a file | Complete, authentic, accepted, or even current work |
| Accepted | Independent head audit/VERDICT names the checked revision and result | Operator GO or updated STATUS |
| STATUS advanced | Sole owner's snapshot agrees with audited evidence and human gavel where required | Permission for an extra send |

Before a future sender touches the transport it marks the POINT attempted in memory and
disables that action. Timeout/disconnect is **unknown-after-possible-submission**, including
when no acknowledgement arrived. No blind retry, automatic retargeting or fallback paste.
After process restart all unresolved POINTs begin **unreconciled**, even if they might never
have been sent. Read available exact-target/runtime/RETURN evidence; absence proves nothing.
The head and operator resolve the uncertainty in existing BUS/STATUS surfaces. If they
cannot, stop that attempt; do not send a replacement cycle while the old one may still act.

This deliberately trades automatic recovery for a smaller first build: no durable transport
ledger and no exactly-once promise. A volatile fence cannot protect against another independent
sender; B therefore has one designated carrier and operator serialization. Native/manual
takeover during a possible send suspends the trial until reconciliation. A disconnect never
authorizes clearing a vendor lock. Later unattended operation requires a separately approved
durable dispatch/recovery policy, not a hidden expansion of this binding file.

## Layer map

| Layer | Authority / responsibility |
|---|---|
| Majkee | Bind/enable decisions, source-home/timing resolution, gavels and stop |
| Oraculum cSharp | RUNBOOK/POINT, one STATUS, independent audit/VERDICT; first in, last out |
| Cartan full session | Technical design/build integration and worked RETURN; helpers remain inside this seat |
| Runbook browser | Read model, selected-context preview/copy, advisory file-presence display |
| Binding/activation adapter | Local exact-endpoint validation and, only after qualification, operator-confirmed carrier call |
| Vendor runtime | Conversation, native subagents, permissions, turn processing, billing/usage path |
| Task files | Durable POINT/RETURN/VERDICT evidence; not L3's room journal |

Here **adapter** means an endpoint-binding/carrier boundary, not a terminal emulator,
Claude persona translator, or replacement for L3's future regulated room machinery.
The operator has un-parked [§5.9 Session attachment](/home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md:218).
This does not settle docket 1/5/6, journal storage, whole-product language, or broker design.
Borrow the lightest substrate's independent sessions, native escape hatch and attention
boundary, not its ungaveled actuator. HANDSHAKE's ack-free courtesy POINT is not a BUS
assignment POINT; human pull through a browser is not agent consumption. No mathematics
or general swarm research is a prerequisite.

## Acceptance test

**Predeclared proposal; none run.** Oraculum audits this design; majkee's GO authorizes
only the design. A build and B's live trial need named sibling gates, exact write/endpoint
scope and tool-owner timing agreement. Their operator count categories are fixed below
before testing, not tuned after observing results.

**Baseline:** finish the count of this manual cycle before comparing a build. RETURN §3
records the recipient side; majkee supplies sender-side notice/locate/copy/switch/paste/
explain/notice-return actions. Do not count model tool reads as human interventions.
Record setup/binding, routine carriage, recovery, and necessary audit/gavel work separately.
One intervention is one deliberate operator action: select a target, inspect a preview,
invoke copy/send, switch a window, paste, submit, supply missing context, or inspect a
return notice. Count repetitions; a compound macro does not erase its confirmations.
Report each named category with the same granularity in both workflows, plus their sum.
Before implementing A, rehearse its static preview against ordinary path-copy and the
now-observed operator-signalled transcript pickup, using a non-executing fixture and
counting bounded transcript retrieval as model work, not human labor. If no routine action
disappears relative to the better existing carry, skip A as a standalone utility
build and consider attachment only as B's prerequisite, with its cost visible.
Current sender count and told-to-read latency are unknown; the old 90/16 figures are not
measurements to substitute. One exchange can demonstrate utility, not generalized savings.

**A pass:** in an authorized representative exchange, bind both operator-opened full
sessions once; select the POINT; inspect and copy the deterministic handoff; paste once
into the selected worker. The receiver proceeds without another human context explanation
and produces a correctly bound RETURN; the head locates and audits it using the existing
view. Show setup count separately. Routine carriage must use fewer counted interventions
than the completed baseline, with no loss of audit/gavel steps. For a one-exchange net-saving
claim, the total including setup must also fall. Otherwise report only the narrower routine
benefit and the observed setup cost: no assumed amortization or fabricated net saving.
If routine carriage does not improve, REVISE/STOP A's standalone utility claim. No activation
call, vendor-runtime write or inferred receipt is permitted in A; its only operational write
is the explicitly authorized local binding record.

**B entry:** first qualify on disposable operator-opened full sessions, then separately
confirm the exact intended pair. Record CLI versions, session/instance IDs, local route,
permissions and operator-observed subscriber usage; inspect no credentials. Keep the native
UI usable. Show that the mechanism addresses the already-living subscriber session without
new process/session creation, API-path conversion or model/permission overrides. Establish
the idle/approval race guard, correlated acknowledgements and failure behavior before work
dispatch. If those cannot be demonstrated, B does not start; A still stands on its own.

**B pass:** one operator-confirmed native dispatch, no receiver-window switch/paste or
context re-explanation; one exact worked RETURN, independently audited and reflected by
the head. Count the remaining human notice/wake/read step at Oraculum: file return is not
automatic head activation. Record prepared/submitted/consumed/file/audit/STATUS evidence
separately. Compare the same categories to baseline; no savings inferred from token totals.

| Negative case | Predeclared required result |
|---|---|
| Wrong bed/seat, including duplicate seat or wrong RETURN path | Strict validator blocks the handoff; no activation. Also test receiver's wrong-seat guard with a non-executing fixture. |
| Stale/replaced endpoint, including same conversation resumed in another instance | Binding invalid, old preview rejected, explicit rebind required; no name-based substitute or replay. |
| Busy/approval/unknown, including a transition after preflight | No submission into active work or approval UI; preserve native permission handling. If the native mechanism cannot enforce this, mark activation unsupported. |
| Interruption after possible submission, including restart | No retry or fallback; surface unreconciled state and inspect existing evidence. A late RETURN cannot be overwritten or counted twice. |

Add malformed/partial RETURN, duplicate clicks, changed POINT after preview and foreign
thread completion fixtures. Safety pass is zero unintended activation/retarget/replay,
zero false consumption/acceptance, and explicit unknowns. Stop immediately on any violation,
unplanned credential/config access, lost native UI, billing-path drift or screen-parser
dependence. A timeout is not a performance failure that licenses a resend.

## Retirement

Retire an activation adapter when the vendor provides a tested native equivalent for the
same full-session target, permissions, usage and failure semantics. Retire the attachment
delta when native cross-vendor joins bind these independent seats to task evidence without
operator re-carriage or loss of sovereign receipts. Keep task evidence and head authority;
do not preserve an adapter merely because it was built.

Stop expansion if routine safety requires following vendor screen rendering, emulating a
terminal, interpreting approval text, or repeatedly rebuilding identity heuristics. The
fallback is native sessions plus explicit file carriage, not an ever-growing harness.
The immediate decision is A's bounded design, with B specified but unqualified—not a promise
to keep pace with vendor IDEs.
