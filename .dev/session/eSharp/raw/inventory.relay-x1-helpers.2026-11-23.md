# relay-X1-probes helper inventory

2026-11-22 and 2026-11-23 · eSharp working material · noncanonical. The group’s own records remain authoritative. States describe the last recorded checkpoint. No private output, operator quotes or cache content is included.

Cycle paths are relative to `.dev/session/relay-X1-probes/` unless otherwise noted. The first and second X1 custody trees are `~/.local/share/nablarva/custody/x1-probes-2026-11-22/` and `~/.local/share/nablarva/custody/x1-chooser-2026-11-23/`. Prior X0 evidence is identified where it was handed forward.

## Coordination and editing

**Scheduler tick** · Inline CronCreate 71185a9a; fork decision, f02. Lead fork · Ad hoc · Spent.

The lead fork set a one-shot 17:45 local wake for the status round. The fire delivered a prompt to its owner and ended the job. Standing use needs an owner, time zone, expiry and firing record.

**Folder doorbell** · `~/.cache/nablarva/relay-x1-doorbell/doorbell.sh` and `state`; f01–f02. Lead fork · Ad hoc · Kept; unarmed at last report.

The lead fork armed it to watch names, sizes and times in the fork and selected bed paths. It excludes its own logs, writes its baseline and wakes the lead on one stable change after a three-second debounce. It also exits on timeout. Standing use needs a scope, deadline and one owned notification.

**Finite RETURN watch** · Inline shell; RUNBOOK and cycles 16–29. Lead · Standing practice; inline · Current wait ends at RETURN or deadline.

The lead starts this after a poke to poll the exact RETURN path, nominally every three seconds. Arrival or deadline ends the background wait and wakes its owner. It reads file existence. The reusable contract is start, named file, expiry and one wake.

**File-poke** · RUNBOOK; `raw/pokes.log.md`, `raw/pokes.fork.log.md`. Shared BUS practice; lead and peers run it · Standing provisional · Available.

A seat writes a POINT, binds the receiver, checks the relevant pane state and sends one pathname through queue or the permitted pane door. It can place session input. The call ends at carrier outcome. File read and worked RETURN are independently established.

**Reply bell** · Inline tmux staging and submission; RUNBOOK, RETURNs 16 and 28. Shared BUS practice; responding seats run it · Standing provisional · Available when composer clear.

A seat writes its RETURN, checks the receiver, stages the label and submits it separately after rechecking. It can enter the lead’s pane. Each bell is a hint. A blocked or uncertain input ends the attempt without a blind retry.

**Armed send** · Inline; `_bus/19`, `23`, `24`, `26` lead try files and VERDICTs. Lead · Ad hoc · Spent.

Lead starts one bounded shell action from a recorded try. It waits for the independent ready marker and checks its binding, age, five holds and running watch before making the authorized carrier call. A paired attempt waits separately for marker 2 or expires. It writes private call evidence. Standing use needs release per try, deadlines and an uncertainty stop.

**setf** · Inline Python with YAML check; POINT 29 lead list. Lead · Ad hoc · Per-edit work spent.

The lead invokes it to set a named field in STATUS. It writes the one owned file and ends after parse validation. Standing use needs an exact edit boundary and concurrent-write protection.

**rep** · Inline Python with YAML check; POINT 29 lead list. Lead · Ad hoc · Per-edit work spent.

The lead invokes it to replace exact text in STATUS. It writes the one owned file and ends after parse validation. Standing use needs an exact edit boundary and concurrent-write protection.

**notice.sh** · `~/.cache/nablarva/relay-x1-doorbell/notice.sh` and `notice.log`. Lead · Ad hoc · One display spent; script kept.

Lead invokes it manually. It appends a trace and shows one line in each attached client’s status area for its duration. It sends no pane input. Standing use needs an audience, expiry and a clear distinction from command delivery.

## Sample setup and receipts

**First sample launch** · Inline; `packet.md`, sample-up decision and exec window receipt. Lead and desk prepared; Majkee ran · Ad hoc · First sample closed.

Majkee starts Codex by hand in the prepared sample folder using the default permission frame. The session ends at operator closure. A reusable setup needs a bound directory and recorded permissions before start.

**start-sample.sh + instruction.txt** · `~/.cache/nablarva/relay-x1-samples/2026-11-23/`; cycle 19. Lead made; Majkee ran · Ad hoc · Second sample stopped.

Starts the second sample in its own directory with fixed sandbox and human approval settings. Input is its standing instruction at startup. Ends at session exit. Standing use requires a known directory, runner and lifecycle.

**start-sample-2.sh + instruction-2.txt** · Same launcher directory; cycle 26 and packet 4. Lead made; Majkee ran · Ad hoc · Third sample up at last bed record.

Starts the fresh third sample with its own directory and fixed approval profile. Majkee runs and closes it by hand. Standing use would also verify the new native identity before measuring.

**Sample receipt writer** · Sample instructions and receipt sections of the packets. Lead wrote instruction; samples ran · Ad hoc · Released attempts spent; receipts retained.

A delivered task can cause the sample to write a named local receipt and answer. The scoped observation ends at receipt or deadline. Standing use needs a fresh operation ID, owned receipt directory and independent checking.

## Observation and readiness

**Observer precheck and ready marker** · Inline; `_bus/*.auditor.precheck.md` and `*.auditor.ready.md`, cycles 06–26. Auditor · Ad hoc per try · Spent.

Auditor uses pane and record checks, paired file stats and scoped baseline reads. It writes a ready marker only for the bound target and running watch. The precheck ends in an emitted or withheld marker. Reuse needs exact predicates, identity, independent ownership and expiry.

**c07.watch.sh** · first X1 custody tree; cycle 07 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler at a nominal two-second cadence through the first queue observation. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c08.watch.sh** · first X1 custody tree; cycle 08 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler at a nominal one-second cadence through paste and submit. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c11.watch.sh** · first X1 custody tree; cycle 11 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler at a nominal one-second cadence with scoped outside-folder state during C1. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c12.watch.sh** · first X1 custody tree; cycle 12 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler at a nominal one-second cadence with scoped outside-folder state during C2. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c19.watch.sh** · second X1 custody tree; cycle 19 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler through the first chooser observation. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c23.watch.sh** · second X1 custody tree; cycle 23 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler through the first interrupted-turn observation. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c24.watch.sh** · second X1 custody tree; cycle 24 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler through the bounded second-sample observation; chooser marker not emitted. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**c26.watch.sh** · second X1 custody tree; cycle 26 auditor RETURN. Auditor · Ad hoc · Stopped; script retained.

Auditor starts a detached bounded sampler through the fresh third-sample observation; chooser marker emitted. It reads pane output and scoped metadata, writes private rows and changed frames, and exits at the sample budget or error. Standing use needs fixed cadence, capture bounds, native lifetime and a completion record.

**Chooser marker 2** · `c24.watch.sh` and `c26.watch.sh`; `_bus/26.auditor.chooser.md`. Auditor · Ad hoc behavior in two watches · Cycle 24 expired; cycle 26 spent.

The watch publishes a one-time marker after two consecutive chooser observations, with thread and times. It writes a file rather than calling the carrier. Standing use needs independent ownership, receiver binding, freshness and a bounded wait by the sender.

## Trackers and output routing

**tracker.2EvwcVSe/tracker.py** · first X1 custody tree; packet 1. Auditor · Ad hoc · Stopped 11:42:24 UTC.

Auditor starts it on a released tracker request. It samples pane and native rollout/receipt metadata into private tracker JSONL, ending at its lifetime bound or stop. Standing use needs identity, a visible start/stop and a handover record.

**tracker.2EvwcVSe/chain.py** · first X1 custody tree; packet 1. Auditor · Ad hoc · Stopped with 11:42:24 UTC run.

Auditor starts companion process-chain and PTY modes. They read process/binding details, runtime-log metadata and the output stream into private chain and PTY JSONL. Stop or output EOF ends collection. Reuse needs separated provenance and bounded retention.

**tracker-manual.u7ady8az/tracker.py** · first X1 custody tree; packet 1–2 and f02 auditor RETURN. Auditor · Ad hoc · Stopped 13:05:53 UTC.

Auditor starts it on a released tracker request. It samples pane and native rollout/receipt metadata into private tracker JSONL, ending at its lifetime bound or stop. Standing use needs identity, a visible start/stop and a handover record.

**tracker-manual.u7ady8az/chain.py** · first X1 custody tree; packet 1–2 and f02 auditor RETURN. Auditor · Ad hoc · Stopped with 13:05:53 UTC run.

Auditor starts companion process-chain and PTY modes. They read process/binding details, runtime-log metadata and the output stream into private chain and PTY JSONL. Stop or output EOF ends collection. Reuse needs separated provenance and bounded retention.

**tracker-chooser.21swz5ue/tracker.py** · second X1 custody tree; packets 3–4 and 25 auditor RETURN. Auditor · Ad hoc · Stopped 21:06:43 UTC.

Auditor starts it on a released tracker request. It samples pane and native rollout/receipt metadata into private tracker JSONL, ending at its lifetime bound or stop. Standing use needs identity, a visible start/stop and a handover record.

**tracker-chooser.21swz5ue/chain.py** · second X1 custody tree; packets 3–4 and 25 auditor RETURN. Auditor · Ad hoc · Stopped with 21:06:43 UTC run.

Auditor starts companion process-chain and PTY modes. They read process/binding details, runtime-log metadata and the output stream into private chain and PTY JSONL. Stop or output EOF ends collection. Reuse needs separated provenance and bounded retention.

**PTY output tap** · Inline tmux output plumbing; packet 1, f02 and 25 auditor RETURNs. Auditor · Ad hoc · Detached or ended in recorded runs.

Auditor attaches it for a tracker start and removes it at detach, stop or pane exit. It changes output routing and supplies bytes to the private collector; pane input is untouched. Standing use needs an exact lifetime, owner and private storage.

## Cache, copy and predecessor evidence

**build-cache.js** · `~/.cache/nablarva/relay-x1-cache/build-cache.js`; f01, f01r1 and f02. Cartan · Ad hoc · Kept for requested refresh.

Cartan runs a finite cut across three named transcripts. It deduplicates shared history, preserves delivered queued input and writes one untracked private cache. It exits after the cut. Standing use needs bounded input, provenance and private publication.

**CACHE.md generation** · Bed `CACHE.md`; cache-and-commits decision and f01 POINT. Maker and runner unknown; Majkee owns cache · Unknown · Owner-held.

The record establishes the cache and ownership. The generating tool, start, end and implementation are unverified. Its named output serves continuity.

**CACHE.exec.md generation** · Bed `CACHE.exec.md`; f01 POINT. Maker and runner unknown · Unknown · Owner-held; production unverified.

This is a named desk continuity cache. The records consulted do not identify a generator, run, end condition or lifecycle.

**Office copy and SHA-256 check** · Inline rsync, SSH and Python; s01 and cycles 16/28 RETURNs. Cartan · Ad hoc · s01, 16 and 28 completed.

Cartan inventories the released tree, checks prefix before replacing an existing shorter file, sends selected paths and verifies SHA-256 and modes. Writes go only into the authorized custody tree. Verification ends each pass. Standing use needs target authorization, conflict refusal and explicit snapshot semantics.

**c04-custody.py** · X0 `scripts/c04-custody.py`; X1 exec experience note. Exec desk’s Astrobley child · Ad hoc predecessor work · Spent; evidence retained.

Exec delegated the released pinned-byte copy. The child checks pins, writes private files and provenance, then exits. A standing tool needs an explicit pin set and independent verification.

**capture-folders-custody.py** · X0 `scripts/capture-folders-custody.py`; X0 cycle 15. Trajectory made; Cartan ran · Ad hoc predecessor work · Spent; evidence retained.

Trajectory prepared the script. Cartan reviewed and ran it once to create the private destination and hash manifest, then independently verified both trees. Standing use requires scope, modes, verified checksums and safe failure handling.

**U01 Terra r1 reader** · Private U01 folder, crawl.01.md, crawl.04.md; X0 11–12 and X1 spawning note. Cartan / Terra · Ad hoc predecessor work · Finished.

Cartan dispatched a bounded r1 read. The child inspected that slice, returned a scoped private report and stopped. Reuse needs fixed source boundaries, masking and an independent selection judgment.

**U01 Terra r2 reader** · Private U01 folder, crawl.02.md, crawl.05.md; X0 11–12 and X1 spawning note. Cartan / Terra · Ad hoc predecessor work · Finished.

Cartan dispatched a bounded r2 read. The child inspected that slice, returned a scoped private report and stopped. Reuse needs fixed source boundaries, masking and an independent selection judgment.

**U01 Terra archive reader** · Private U01 folder, crawl.03.md, crawl.06.md; X0 11–12 and X1 spawning note. Cartan / Terra · Ad hoc predecessor work · Finished.

Cartan dispatched a bounded archive read. The child inspected that slice, returned a scoped private report and stopped. Reuse needs fixed source boundaries, masking and an independent selection judgment.

## Decision and review helpers

**Exec gate sheets and read-back** · RUNBOOK exec prompt; gate sheets and exec RETURNs. Lead makes sheets; exec runs them · Standing role; ad hoc sheets · Last read-back: gate 3, on the second packet (cycle 14); packets 3 and 4 were decided in the lead's window.

The lead gives the exec desk one sheet. Exec walks one theme at a time and writes an attributed record and RETURN. That ends the desk cycle. The operator supplies the decision and the lead verifies it.

**Exec window preparation** · `raw/return.exec.window-lead.2026-11-22.md`. Exec desk · Ad hoc · Lead window prepared.

The desk prepares the named tmux window on operator direction and ends at handover. It changes terminal layout. Standing use needs exact identity, owner and recorded end state.

**Oraculum counter-read** · Named Oraculum RETURNs; 18 reviewed chooser scope. Lead dispatches; Oraculum reads · Standing role; bounded uses · Cycles 01, 04, 05 and 18 returned.

The lead assigns a fixed wording or evidence question. Oraculum reads, writes the scoped finding and stops. Cycle 18 challenged the chooser evidence and observed sampling limit. The lead owns disposition.

**myShell continuity lookup** · Cycle 03 VERDICT and s01 request. Lead and operator dispatch; myShell reads · Standing role; bounded uses · Cycle 03 and s01 routing complete.

myShell resolves ownership or continuity by returning scoped pointers. It also routed the released office-copy request. The request ends when the evidence or assigned path is returned.

**Assay fresh-eyes check** · `_bus/03.lead.verdict.md`. Lead / assay · Ad hoc · Cycle 03 returned.

The lead gives a fixed handoff, draft sheet and saved help for an independent read. The child returns defects and stops. Standing review needs fixed input, scope and disposition.

**L14 narrowing child** · L14 names decision and cycle 15 POINT. Lead; vector named in the decision · Ad hoc · Cycle 15 work returned.

The lead assigned a child to narrow the chapter mapping and make the owned documentation changes. The work ends at the scoped diff. Standing use needs file authority and independent verification.

**L14 wiring child** · L14 names decision and cycle 15 POINT. Lead; assay named in the decision · Ad hoc · Cycle 15 check returned.

A second child checks live references and returns a scoped finding. Standing use needs explicit reference coverage and preservation of historical names.

## All 46 entries

| Name | Kind | Maker or runner | Ad hoc or standing | State |
|---|---|---|---|---|
| Scheduler tick | One-shot timer | Lead fork | Ad hoc | Spent |
| Folder doorbell | Metadata watch | Lead fork | Ad hoc | Kept; unarmed at last report |
| Finite RETURN watch | Deadline poll | Lead | Standing practice; inline | Current wait ends at RETURN or deadline |
| File-poke | Coordination carrier | Shared BUS practice; lead and peers run it | Standing provisional | Available |
| Reply bell | Coordination carrier | Shared BUS practice; responding seats run it | Standing provisional | Available when composer clear |
| Armed send | Bounded actuator | Lead | Ad hoc | Spent |
| setf | STATUS editor | Lead | Ad hoc | Per-edit work spent |
| rep | STATUS editor | Lead | Ad hoc | Per-edit work spent |
| notice.sh | tmux status notifier | Lead | Ad hoc | One display spent; script kept |
| First sample launch | Manual launcher | Lead and desk prepared; Majkee ran | Ad hoc | First sample closed |
| start-sample.sh + instruction.txt | Manual launcher and instruction | Lead made; Majkee ran | Ad hoc | Second sample stopped |
| start-sample-2.sh + instruction-2.txt | Manual launcher and instruction | Lead made; Majkee ran | Ad hoc | Third sample up at last bed record |
| Sample receipt writer | Native receiver scaffold | Lead wrote instruction; samples ran | Ad hoc | Released attempts spent; receipts retained |
| Observer precheck and ready marker | Read-only qualification and file signal | Auditor | Ad hoc per try | Spent |
| c07.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c08.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c11.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c12.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c19.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c23.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c24.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| c26.watch.sh | Detached pane watch | Auditor | Ad hoc | Stopped; script retained |
| Chooser marker 2 | Scripted arm signal | Auditor | Ad hoc behavior in two watches | Cycle 24 expired; cycle 26 spent |
| tracker.2EvwcVSe/tracker.py | Pane and rollout sampler | Auditor | Ad hoc | Stopped 11:42:24 UTC |
| tracker.2EvwcVSe/chain.py | Process-chain and PTY collector | Auditor | Ad hoc | Stopped with 11:42:24 UTC run |
| tracker-manual.u7ady8az/tracker.py | Pane and rollout sampler | Auditor | Ad hoc | Stopped 13:05:53 UTC |
| tracker-manual.u7ady8az/chain.py | Process-chain and PTY collector | Auditor | Ad hoc | Stopped with 13:05:53 UTC run |
| tracker-chooser.21swz5ue/tracker.py | Pane and rollout sampler | Auditor | Ad hoc | Stopped 21:06:43 UTC |
| tracker-chooser.21swz5ue/chain.py | Process-chain and PTY collector | Auditor | Ad hoc | Stopped with 21:06:43 UTC run |
| PTY output tap | Output routing | Auditor | Ad hoc | Detached or ended in recorded runs |
| build-cache.js | Private transcript reader | Cartan | Ad hoc | Kept for requested refresh |
| CACHE.md generation | Private continuity cache | Maker and runner unknown; Majkee owns cache | Unknown | Owner-held |
| CACHE.exec.md generation | Private desk cache | Maker and runner unknown | Unknown | Owner-held; production unverified |
| Office copy and SHA-256 check | Private transfer | Cartan | Ad hoc | s01, 16 and 28 completed |
| c04-custody.py | Pinned custody copy | Exec desk’s Astrobley child | Ad hoc predecessor work | Spent; evidence retained |
| capture-folders-custody.py | Whole-folder custody copy | Trajectory made; Cartan ran | Ad hoc predecessor work | Spent; evidence retained |
| U01 Terra r1 reader | Bounded child reader | Cartan / Terra | Ad hoc predecessor work | Finished |
| U01 Terra r2 reader | Bounded child reader | Cartan / Terra | Ad hoc predecessor work | Finished |
| U01 Terra archive reader | Bounded child reader | Cartan / Terra | Ad hoc predecessor work | Finished |
| Exec gate sheets and read-back | Operator decision desk | Lead makes sheets; exec runs them | Standing role; ad hoc sheets | Last read-back: gate 3, on the second packet (cycle 14); packets 3 and 4 were decided in the lead's window |
| Exec window preparation | Terminal setup | Exec desk | Ad hoc | Lead window prepared |
| Oraculum counter-read | Strategic review | Lead dispatches; Oraculum reads | Standing role; bounded uses | Cycles 01, 04, 05 and 18 returned |
| myShell continuity lookup | Continuity desk | Lead and operator dispatch; myShell reads | Standing role; bounded uses | Cycle 03 and s01 routing complete |
| Assay fresh-eyes check | Lead child review | Lead / assay | Ad hoc | Cycle 03 returned |
| L14 narrowing child | Lead child author | Lead; vector named in the decision | Ad hoc | Cycle 15 work returned |
| L14 wiring child | Lead child checker | Lead; assay named in the decision | Ad hoc | Cycle 15 check returned |

## Kinds that recur

- **Bounded waiting and notification.** Scheduled wakes, path watches, a status flash and a reply bell each need an owner, deadline and observable outcome.
- **Independent observation.** Pane sampling, preflight baselines, native record metadata, process tracing and PTY output establish different facts within their sampling bounds.
- **Permission to proceed.** A readiness marker verifies predicates for a separately released call. Each marker needs a writer, intended receiver and expiry.
- **Private continuity and custody.** A transcript cut or a hash-checked copy needs explicit scope, provenance and retention.
- **Independent reading and read-back.** Children and reviewers return scoped observations. The desk records attributed operator decisions, and the lead dispositions the evidence.

Unknowns: the two older cache generators, exact private tracker launch wrappers, and any further observer-only helpers are not known from the files checked. Ask the auditor later if those details matter. An operator-side sample tutor was discussed, with no verified run in the consulted bed records.
