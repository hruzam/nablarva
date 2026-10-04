# Workflow reading — what should the animal own?

*Cartan · 2026-09-29 · working observations and alternatives, not a selected
architecture. Majkee requested this broader pass before choosing the basic stones.*

The [existing blueprint](architecture.working.md) describes one candidate. This
pass asks whether its boundary fits the work, rather than assuming that all
existing organs must become dependencies. Flight's independent assignment is
[POINT 02](../_bus/02.cartan.point.md); its delivery and review state live in STATUS.

## Observed jobs

These are readings of operator logs and project receipts, not a live experiment.

| Episode and source | Work being done | Architectural implication — inference |
|---|---|---|
| [Sep 14](../../nablarva-02-pipe-qualification/raw/human-relay-time-logs/stenograph.real.pc.2026-09-14.md), lines 28–42: collect notes while waiting, recover an omitted prompt, carry it, then relay a partial answer | Prepare context and move a particular assignment while preserving its purpose | A durable selected prompt and its exact destination matter; moving terminal text is only one possible carrier. Partial updates need a visible relationship to the outstanding assignment. |
| Same log, lines 43–84: open/resume twins, repair launch quoting, name sessions, decide which original may close | Manage session identity and continuity during another arc | A work arc, a conversation, a running process and a terminal view are different things. A rename helps the human but cannot establish a delivery address. |
| Same log, lines 56–78 and 108–126: repeated checks, delayed approval discovery, failed copying, notice confused with completion | Allocate attention and recover from uncertain state | Distinguish “needs permission,” “still working,” “reply available” and “unknown.” Improving outbound send alone leaves much of this work intact. |
| [Sep 17](../../nablarva-02-pipe-qualification/raw/human-relay-time-logs/stenograph.real.pc.2026-09-17.md), lines 53–101: reload, deploy, test navigation, write feedback, leave reading for an approval | Operate a build/test/feedback loop across two arcs | Human testing and judgment are productive work; eliminating every switch is the wrong objective. The system should preserve place and purpose across interruptions. |
| Same log, lines 105–158: move to phone, locate a session, ask about resume identity, test again, interrupt reading for approval | Continue work across devices | A terminal layout alone cannot be the durable home of the work. Showing the same records on another device need not imply moving or restarting its agents. |
| [Mobile rehearsal](../../nablarva-02-pipe-qualification/raw/human-relay-time-logs/rehearsal.mobile.telemetry.2026-09-14.md), lines 27–65: voice stops across apps, connection drops, buffer lost | Recover draft and context | Supports studying a durable draft/selection surface. It is simulated evidence, not an observed production failure rate; L8 keeps the composer mechanism outside nabLarva. |

The useful unit of study is an **arc with interruptions**, containing multiple
exchanges and human decisions. The product may still implement a small exchange
primitive; the unit used to evaluate its usefulness must include the surrounding work.

### Measurement limits

September 14 interleaves the qualification and reincarnation arcs. Its whole-log
totals are not the cost of one relay. The owner's [baseline](../../nablarva-02-pipe-qualification/raw/baseline.md)
already separates setup, carriage, recovery and audit/gavel, and labels its episode
segmentation as a proposal. Its reported notice lag combines recipient timestamps
with human observation; this study has not run a replacement workflow for comparison.

September 17 is open-ended, changes clock order (including 01:52 → 01:33), contains
“1 hour 66 minutes,” and has conflicting totals at lines 162–192 and 196–219.
Use episodes qualitatively. Do not aggregate durations or compare its totals to
September 14. The original logs remain untouched. Historical token/cache claims in
the token-economy brief and its fold have not been verified for this study and do
not decide the architecture.

## What sessions 01 and 02 actually contribute

- [Design r1](../../nablarva-01-design/raw/design.r1.md), accepted in bed 01's
  [STATUS](../../nablarva-01-design/STATUS.md), supplies useful distinctions:
  explicit binding; session versus incarnation; assignment/RETURN correlation;
  prepared, submitted, consumed, RETURN present, accepted and STATUS advanced.
  Its A/B/C sequence deliberately limits the first build. Accepting the design
  did not prove a working pipe.
- Bed 02's [VERDICT 03](../../nablarva-02-pipe-qualification/_bus/03.oraculum.verdict.md)
  accepts a bounded inspection probe and reports nine reproduced offline tests.
  Its [STATUS](../../nablarva-02-pipe-qualification/STATUS.md) still records live
  arming as not begun and native qualification as unverified. We read these
  receipts; we did not rerun the probe or inspect live endpoints.
- The [experience transfer](../../nablarva-01-design/raw/oraculum.experience-transfer.2026-09-12.md)
  describes stale head instructions, corrections aimed at the head's preference,
  and lost measurement requests. File-based review caught real mistakes; it also
  takes human attention. The development harness is a way to verify a build, not
  automatically the workflow every eventual user should have to reproduce.
- The [relay-seam v2](../../../../meshup/a-symmetry-lightest/brief.relay-seam.v2.2026-09-13.md)
  values independent sessions and keeping Majkee out of routine carriage. Its
  [nablarva fold](../../nablarva-02-pipe-qualification/raw/fold.relay-seam-v2.2026-09-13.md)
  explicitly resolves the conflicting actuator and file vocabulary. Neither a
  tmux doorbell nor RETURN presence becoming acceptance is silently restored here.
  Its reference to a future “nablarva-03” build bed is historical, not authority
  for this architecture bed to implement anything.

## Three boundaries worth comparing

These alternatives differ in ownership and process lifetime, not merely UI.

| Candidate | Smallest mechanism and owner | Benefit | Cost / evidence that could defeat it |
|---|---|---|---|
| **1. Operator workbench around existing terminals** | Existing task browser and terminal navigation expose selected work, artifact links and attention evidence. Agents retain their own lifetimes; operator initiates handoffs. | Preserves place across arcs and reduces locating/copying/recovery. Can improve the current workflow before a reliable wake exists. | An interim aid: manual notification still leaves Majkee in the relay. More panels may add work. Must beat the existing browser/path-carry workflow, not an imagined empty baseline. It does not satisfy the full agent↔agent ladder on its own. |
| **2. Exchange service beside independent agents** | A small exchange boundary carries released file references, recipient bindings, reply correlation and uncertainty through qualified native adapters. Agents run independently; views are clients. | Directly addresses the requested living-peer loop, with records that survive view/device changes. | Depends on reliable access to living sessions. If native adapters cannot preserve identity, approvals and UI without ongoing emulation, the core cannot manufacture that capability. Initial engineering exchanges reuse their existing records; a room journal needs an explicit later boundary. |
| **3. Room host that owns agent processes** | The application creates the participating processes and owns their connection through adapters; a room journal and projections follow L3. The native interaction surface must remain available. | Can establish process/connection identity at launch and apply structural room regulation. | Much larger lifecycle responsibility: launch, attach, permissions, restart and recovery. It does not automatically reach existing external sessions or guarantee native UI/usage compatibility. It diverges from bed 01's chosen scope and the relay brief's rejection of full PTY orchestration; selecting it would require an explicit scope decision. L4 still forbids send-keys injection. |

The earlier blueprint prefers candidate 2. That preference is **provisional** while
this comparison is open. Candidate 1 can be useful alongside 2, but combining them
does not remove 2's qualification dependency. Candidate 3 deserves an honest cost
comparison if the terminal study shows that owning launch/lifecycle is acceptable.
No alternative changes bed 02's current gate or authorizes an L4 exception.

A fresh headless consultation is a useful separate capability; it changes which
conversation is doing the work. The [carrier note](tunnel-consultation.2026-09-29.md)
keeps it distinct from reaching the already-running colleague. It cannot be counted
as a successful living-peer exchange merely because it returns useful text.

## Stones to keep; commitments to make earn their place

The strongest reusable stones are durable selected artifacts, explicit recipient
binding, correlated replies, a distinction between observation and accepted work,
and a human route for permission or uncertainty. Existing native agents, the task
browser and the ia-sync delivery discipline provide the present environment.

Do not make every organ mandatory. Terminal frames help navigation; Termbrana's
observation product must earn a role through retrieval needs; Muticula addresses
shared-write discipline, a separate problem from message delivery. Compression,
RAG, an autonomous scheduler and a replacement terminal are not prerequisites for
the first loop. Their research can remain valuable without entering that build.

For a layer-by-layer terminal study, ask where each responsibility belongs:
**durable work → exchange → runtime connection → process/terminal → human view and
device**. A layer's display or process signal must not silently become the truth
for another layer. A zsh entrypoint or IDE integration alone chooses none of these
ownership boundaries.

## What would distinguish the candidates

First replay one existing episode on paper with the current tools as the baseline:
an assignment, a partial reply, an approval interruption, a final RETURN and a
device switch. For each candidate, mark each remaining human action and each
unproven machine capability. Count setup, carriage, recovery and judgment separately;
do not claim saved minutes from this replay.

Candidate 1 earns further work only if the replay exposes avoidable navigation or
recovery that today's tools do not already cover. Candidate 2 depends on bed 02's
native qualification plus a separately qualified return wake. Candidate 3 becomes
serious only if owning agent launch/lifecycle is desirable and its native interaction
and usage constraints can be demonstrated. Those are proposed discriminators,
not new experiments opened here.

No need to read every historical file before deciding: expand the read set when it
could change ownership, a required capability, a failure policy or the first useful
slice. Preserve the rest as research rather than turning it into implementation debt.

## Onion-terminal input — an instrument, with a separate control proposal inside it

Majkee supplied [unilarvatrix's build plan](/home/hruzam/ia-sync/.dev/session/voice-meetings-01-threshold/meeting-themes/onion-terminal/build-plan.md)
during this reading. His clarification: an observation device should attach,
read selected session data/logs and produce samples; it might serve nabLarva's
testing as well as become a useful sub-app on its own.

The plan is dated September 18 and cites `docs/terminal-onion.study.2026-09-17.md`.
The supplied directory contains the plan only; its proposed
`~/unikuklatrix/unilarvatrix/` repository does not exist on this host at inspection.
A filename search under ia-sync/.dev, unikuklatrix and reposoma found the older
[terminal-onion study](../../../../meshup/old-but-good-onion/terminal-onion-study.md),
which says June provenance and has different sections. Both available files were
read in full; the exact companion and any separate implementation remain unverified.
Commands in either document were not executed.

The plan contains two different responsibilities:

- Phases 0–2 propose probes, hook records, process/FD snapshots, viewport observation,
  samples and a viewer. This can supply evidence about what an agent and its terminal
  were doing. It need not own the agent or deliver messages.
- Phase 3 adds cross-session summaries and automatic checkpoint insertion at session
  start. That changes the recipient's context: it is a communication/selection policy,
  not observation. It would need the explicit release and delivery boundaries already
  under discussion, plus the L8 boundary where composition is involved. It should not
  enter an observer as an incidental later phase.

The useful relationship is **observer → attributed samples → human/test analysis**,
alongside **nabLarva → addressed exchanges**. A sample may explain an exchange's
delay without becoming its receipt or authorizing a retry. The two products can
share narrowly defined identifiers or sample readers later; neither must import
the other's full runtime.

### Three corrections before treating the plan as executable

1. The plan calls unchanged viewport + living process a stall. That only establishes
   those observations; computation, waiting for input, approval and genuine failure
   remain different possible explanations. Preserve “unknown” and qualify any
   stronger sensor claim against a known scenario. Official [Zellij programmatic-control
   docs](https://zellij.dev/documentation/programmatic-control.html) describe subscribe
   output as rendered viewport/scrollback. It is not a raw PTY stream or semantic
   proof of agent state. Installed-host compatibility was not tested here.
2. Truncating `tool_input` below `PIPE_BUF` does not establish safe concurrent JSONL
   appends to a regular file. The [pipe guarantee](https://www.man7.org/linux/man-pages/man7/pipe.7.html)
   concerns pipes/FIFOs and a write's byte count. The complete encoded record, write
   behavior and actual storage need their own rule. Start with explicit writer
   ownership; test overlap and incomplete records before relying on the archive.
3. “A model gives a correct five-line answer” is insufficient as a sample-reader
   acceptance test. Use scenarios with known events and identities; check what was
   captured, omitted, duplicated, reordered or misclassified. A model summary can
   help interpretation after that. Keep missing observations visible.

These are architecture findings, not a full audit of every hook name, current vendor
format or command. The older study's claim that JSONL implies append-only storage is
also too strong: encoding one JSON value per line does not enforce storage behavior.
Neither study authorizes reading credentials or private reasoning/history.

### Possible observer experiment, if needed

Do not open two full application builds from these documents. The exchange
candidate remains the synthesis target; an observer is useful if existing tools
cannot answer a named question that decides it. In that case, define one
small observer experiment inside the existing nabLarva study's evidence scope:
one explicitly selected session, one sampling interval, a declared set of sources,
and a stop condition. Begin with already-released artifacts and metadata; any public
message export is an explicit source, not a recursive harvest of runtime homes.
No context injection, approval handling or automatic agent wake belongs in this cut.

Its concrete question: **can the samples distinguish a permission wait, ordinary
work and an available RETURN, with their times and target identity, more reliably
than today's manual checks?** First use controlled fixtures to test the sample
reader; a later bounded live observation would qualify what each actual sensor can
prove. A fixture pass alone proves no native capability.

If the small instrument answers that question, it supplies nabLarva's tests and
earns consideration as a standalone toolbox. If the existing artifact browser
already answers it, extend or reuse that rather than build another dashboard.
If native permission signals remain unavailable, report that gap; a larger terminal
host is not automatically the remedy. Flight's POINT 02 now includes this input.
No observer implementation or live collection has started.
