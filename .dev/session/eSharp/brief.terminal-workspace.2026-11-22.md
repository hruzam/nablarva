---
kind: reader's brief for RUNBOOK authoring — facts and pointers, no verdict
line: terminal-workspace
by: field (reader agent), asked by the eSharp manager
date: 2026-11-22
read:
  - terminal-workspace-X.ledger.md
  - terminal-workspace-X0-approaches/RUNBOOK.md
  - terminal-workspace-X0-approaches/STATUS.md
  - terminal-workspace-X0-approaches/CS.terminal-workspace.office.2026-11-19.md
  - terminal-workspace-X0-approaches/_bus/01.cartan.point.md
  - terminal-workspace-X0-approaches/_bus/01.claude-colleague.return.md
  - terminal-workspace-X0-approaches/raw/NEW.read-before-continue.shared-terminal-organ-card.md
  - terminal-workspace-X0-approaches/raw/request.majkee.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/request.majkee.command-files.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/request.majkee.next.2026-11-18.md
  - terminal-workspace-X0-approaches/raw/brief.cartan.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/probe.pty-feasibility.2026-11-17.py (first 50 lines)
  - terminal-workspace-X0-approaches/raw/probe.pty-feasibility.2026-11-17.json
  - terminal-workspace-X0-approaches/raw/research.approaches.2026-11-17.md (first 80 lines)
  - terminal-workspace-X0-approaches/raw/research.correction.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/consult.oraculum.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/consult.houston.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/architecture-preparation.md
  - terminal-workspace-X0-approaches/raw/next-experiment.proposal.2026-11-18.md
  - terminal-workspace-X0-approaches/raw/handoff.cartan.2026-11-17.md
  - terminal-workspace-X0-approaches/raw/handoff.claude-colleague.2026-11-19.md
  - pulse.md (row 19)
  - flag.md (L3, L4, L13, L14, L17, L18, L19, L20, L21, L22)
  - relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md (T6 only)
  - eSharp.decisions.majkee.2026-11-22.md
---

# Reader's brief — terminal-workspace line

## 1. What the line is for — Majkee's words

Earliest statement. `raw/request.majkee.2026-11-17.md:6`:
> "does make a sense to as we trying sublime give CLIs their own terminal. And I do not thinking the are in fact 'terminal', but like f.e. "run bash|terminal commands together with user" - but full terminal."

Session and consultation request. `raw/request.majkee.2026-11-17.md:11-16`:
> ". Cartan, please, can you create new sesion line for that, similar naming like this sublime has + preparing documentation for architecture.
> -> `oraculum`: consultation -technical side.
> -> `houston` : architectural side + documentation.
> ---
> Bed + `raw/` substrate handoff, or you can perform basic tests. I think theoreticaly can CLI put prompts as 'files' to dogfeed container. I can set regime, similar as permission mode. Or you see different way. Or... maybe would be best send one subagent to make deep-research, what approaches we can possibly use."

Refinement same day. `raw/request.majkee.command-files.2026-11-17.md:5`:
> "ok, that has reason as far as I can see, when agent can put|construct (write) command there. Thats is why I thought, that can be input file consumed by tool, whenever is closed f.e. and eventualy also see result. Minimal bash need in case."

Next day. `raw/request.majkee.next.2026-11-18.md:5-7`:
> "So, where we could collect terminal|agent|human-user input output. What caching like some jsonl, or md 'history'.
> how we could permissions or rhythm of usage.
> I mean whole conceptual approach."

Descriptions across dates: the 2026-11-17 initial framing is a "full terminal" for joint human-and-CLI bash use. The same-day refinement narrows toward file-in, result-out ("whenever is closed"). The 2026-11-18 message broadens again to history collection, caching, and usage regimes. `architecture-preparation.md:9-10` captures this drift: "give CLIs a full terminal for working together with the human; explore file-fed container requests and a regime like permission modes." The file-fed interpretation (`inferred: Cartan`) is Cartan's reading; it was proposed, not locked by Majkee. `request.majkee.2026-11-17.md:19-21` explicitly notes this.

---

## 2. Where the bed stands today

Gate text verbatim. `pulse.md:19` and `STATUS.md:12-14`:
"Majkee records GO or STOP on an evidence-backed preparation packet for a human-and-agent shared task terminal: dated native/reuse alternatives, Oraculum technical consultation, Houston architecture and documentation review, a disposition of file-fed container requests and operator-selected input regimes, and the exact scope and proof obligations of one recommended next experiment."

Participants. `RUNBOOK.md:10-16`:
- cartan — controller, sole STATUS owner
- oraculum — bounded technical child consultation
- researcher — bounded primary-source research
- houston — bounded consult on architecture and documentation
- majkee — intent and gavel
- claude-colleague — independent technical co-thinking/challenge; added 2026-11-18 (`RUNBOOK.md:144-151`)

STATUS position (`STATUS.md:1-5`, updated 2026-11-19 20:49 CET):
- Checkpoint: preparation bed, POINT 01 and Claude RETURN tracked in 519bb37; base 3bbbf08. `STATUS.md:15-16`.
- RETURN 01 says REVISE. Its suggestions are "not yet dispositioned by Cartan". `STATUS.md:18-19`.
- No VERDICT, X0 acceptance, X1 release, or successor bed recorded. `STATUS.md:34-36`.
- Next: "Cartan on office verifies RETURN 01 against POINT 01 and cited artifacts, then writes `_bus/01.cartan.verdict.md`." `STATUS.md:39-41`.

What was actually probed or measured. `probe.pty-feasibility.2026-11-17.json`:
- Six synthetic feasibility checks all pass: same-shell file requests retain cwd/env/function; a fresh process does not retain them; TTY and interactive line reply work; Ctrl-C signals foreground child while shell survives; PTY dimensions change; PTY survives a brief unobserved interval.
- `qualified: false`. `probe.pty-feasibility.2026-11-17.json:3`.
- Eight things explicitly unproven: native CLI attachment/permissions, human client attachment, actual detach/reconnect, input ownership/takeover, container isolation, rendered screen/TUI correctness, raw single-key mode, restart/replay safety. `probe.pty-feasibility.2026-11-17.json:17-26`.
- Ran in an isolated PID namespace (`pid:[4026532881]`), not on office, not against any native CLI. The earlier exploratory run is not the saved run. `architecture-preparation.md:131-143`.

What was only researched or written:
- Approaches research: four families (native facility, reusable manager+bridge, file-fed fresh jobs, file-fed persistent worker); primary sources; six unknowns. `raw/research.approaches.2026-11-17.md:19-70`.
- Correction to research: Claude `--bg --exec` is a native PTY-attach candidate, not conversation-only; Termbrana observer vs. composition family clarified. `raw/research.correction.2026-11-17.md`.
- Oraculum consultation: recommended persistent attachable task process; proposed a six-row test spec; flagged L3/L4/L14/L17/L20 constraints. `raw/consult.oraculum.2026-11-17.md`.
- Houston consultation: verdict `stretches`; five constraints dispositioned in `architecture-preparation.md §8`. `raw/consult.houston.2026-11-17.md:14`.
- Architecture preparation document: candidate seam row for ARCHITECTURE.md §4; proposed §2 paragraph; PROJECT-DESIGN.md §2.2 pointer; operation-specific proof obligations table. `raw/architecture-preparation.md`.
- Proposed X1 gate and demonstration steps. `raw/next-experiment.proposal.2026-11-18.md`.
- POINT 01 sent to claude-colleague; RETURN 01 received with REVISE verdict and eight mismatches (M1-M8). `_bus/01.cartan.point.md`, `_bus/01.claude-colleague.return.md`.
- Cartan and claude-colleague handoffs written. `raw/handoff.cartan.2026-11-17.md`, `raw/handoff.claude-colleague.2026-11-19.md`.
- Transfer cold-start card for home-to-office move. `CS.terminal-workspace.office.2026-11-19.md`.

---

## 3. The NEW card against today's shape

The NEW card (`raw/NEW.read-before-continue.shared-terminal-organ-card.md`) is version 2, dated 2026-11-22. It replaces version 1 of 2026-11-19. It calls itself "a builders' handoff card" with "design agreed, nothing built yet." `NEW.card:3-5`. The bed's documents are dated 2026-11-17 to 2026-11-19.

| topic | what the bed says today (file:line) | what the NEW card says (line) | what would have to change in the bed if the NEW card is taken |
|---|---|---|---|
| **Purpose and scope** | A preparation gate; selecting/recommending an approach; no organ, name, or component yet locked. `RUNBOOK.md:27-30`. "No selected organ owner, final component directory, persistent schema, transport or product stack is locked here." `RUNBOOK.md:114-115`. | "design agreed, nothing built yet"; build v0 is the next step; build order and acceptance probes stated. `NEW.card:4-5`. | The X0 gate has not formally closed; a VERDICT and Majkee GO are still required before build authority. The head must reconcile "design agreed" against the open gate. |
| **Who uses it** | "human and agent clients of an identified task shell/application" — open. `architecture-preparation.md:213`. | "An agent that can write a file into the organ's inbox can have a command run in a real, living terminal pane, and can read the result back. The human shares the same pane and controls the gate." `NEW.card:12-14`. Vendor-neutral. `NEW.card:33`. | Narrower than the bed's open consumer description; the human's role is now "controls the gate" not an equal participant in typing. |
| **Input format** | File-fed; submit mechanism open; "ordinary file close/save is not implicitly submit"; atomic rename preferred but not locked. `architecture-preparation.md:60-66`. No schema selected. `architecture-preparation.md:92-93`. | Atomic rename into `inbox/`; filename = request id; directories are states (inbox/inflight/done/denied/unknown); files moved, never deleted; same id refused on any re-entry. `NEW.card:51-58`. | The NEW card settles these conventions; the bed would need to record the submission trigger and state machine as decided rather than open. |
| **Output/result format** | "output plus a distinguishable pending/running/completed/failed/unknown outcome"; JSONL events and Markdown/current-state snapshot proposed for X1 (not locked). `next-experiment.proposal.2026-11-18.md:42-43`. No final schema. `architecture-preparation.md:72`. | Named result record fields per request (id, submitter, hash, gate decision, outcome, reason, dir before and after, shell pid, exit code, start, end, output path). `NEW.card:103`. Current-state snapshot and Markdown history not included; v2 adds JSONL store as a later rebuildable projection. `NEW.card:165, 29`. | RETURN 01 also recommends dropping snapshot and Markdown view (`_bus/01.claude-colleague.return.md:188`), so the NEW card and the reviewer agree here. The bed's X1 proposal still carries them. |
| **Where execution happens** | Open; four approach families compared; bed fixture uses owned Python PTY (single pane, executor holds PTY master). `architecture-preparation.md:82-93`. `probe.pty-feasibility.2026-11-17.py:43`. | Two panes: control pane (executor script + reads approval key) and exec pane (persistent interactive zsh). Send-keys doorbell. "source plus the quoted absolute path of the frozen file." `NEW.card:30-33, 83-86`. | A major topological change: the NEW card separates executor from PTY owner (tmux holds the exec pane). The bed's probe had the executor holding the PTY master, which RETURN 01 M3 called "executor death = shell death." `_bus/01.claude-colleague.return.md:92-100`. The NEW card's two-pane design dissolves that failure mode architecturally. |
| **Approval mechanism** | "file-fed container requests and operator-selected input regimes" as hypotheses. `RUNBOOK.md:28-29`. "A request file or a named mode does not prove enforcement, consent or isolation." `RUNBOOK.md:113-114`. X1 uses a frozen synthetic allowlist. `next-experiment.proposal.2026-11-18.md:52-54`. | "ask gate, by keypress" in the control pane. "Approval is never a file." `NEW.card:79-81`. | The bed explicitly leaves the regime open; the NEW card settles it. The NEW card is candid: "This gate governs the cooperative path: it stops a write-only agent, not one that can send keys through tmux." `NEW.card:81`. |
| **Recording responses** | JSONL events, current-state snapshot, Markdown view — proposed for X1. `next-experiment.proposal.2026-11-18.md:42-44`. | Per-request files in named directories; one result record per request written before the doorbell rings. No snapshot; no Markdown history; v2 adds rebuildable JSONL store. `NEW.card:103, 101-102, 165`. | The bed's X1 proposal still carries the snapshot and Markdown view; the NEW card drops them and both agree with RETURN 01. |
| **Organ name and home** | "terminal-workspace" is a provisional slug; `attach: unassigned`. `ledger.md:6`. No organ name, no component directory locked. `RUNBOOK.md:114-115`. | Working name "shared-terminal organ"; "rename freely." `NEW.card:6`. Control pane + exec pane defined; source home not settled. | The NEW card gives an organ name but marks it provisional. Source directory and owner remain unset in both. |
| **Relation to other organs** | Explicit placement against ovitmugen (lifetime), termpanum (observation distinction), stridulatrix/room-bus (no room journal or autonomous sender), phone-console (precedent). `architecture-preparation.md:116-121`. | "Sits beside each CLI's native bash and does not replace it." "Same envelope as the existing CLI-to-CLI bus. The executor is one more consumer on the bus." `NEW.card:16-17, 42-43`. Does not explicitly name ovitmugen, termpanum, or stridulatrix. | The NEW card's organ-to-bus relation ("one more consumer") would need to be checked against L14 D2 (file spine) and L4 (send-keys death) before it can be called architecturally grounded. The bed's architectural placement table is richer and would remain needed for the RUNBOOK. |
| **What is explicitly out of scope** | Native human attach, vendor permissions, container isolation, human takeover, relay transport, language/product stack. `RUNBOOK.md:112-120`. Six-row matrix rows 4-6 unproven. `architecture-preparation.md:166-167`. | v0: no background launch or launch-in-second-pane (those are v1). Remote consumers are v2 and "belong to the bus, not to the executor." `NEW.card:130-131, 167-170`. Native CLI qualification not gated; "No vendor hooks and no local model in the required path." `NEW.card:33`. | The NEW card is lighter on what it defers than the bed. The bed's architectural placement and operation-specific proof obligations table (`architecture-preparation.md §8`) are not in the NEW card. |
| **What the NEW card adds the bed never mentions** | — | Numbered build order 1-26 with concrete implementation requirements. `NEW.card:62-170`. `preexec`/`precmd` hooks in the exec pane's zsh writing begin/end/exit-code/cwd/pid, registered with `add-zsh-hook`. `NEW.card:87-89`. Lock file for single executor per exec pane. `NEW.card:98-99`. "Result before doorbell" rule. `NEW.card:101-102`. Ten acceptance probes for v0 as a named table. `NEW.card:187-200`. v1 "named operations and instant mode" (auto-approval for reviewed named ops). `NEW.card:119-121`. Security posture section stated plainly. `NEW.card:172-185`. Prior art list (agent-tmux, agent-mux, NTM, runme, mdsh). `NEW.card:217-221`. Open question for the human about what the existing bus provides. `NEW.card:203-207`. | The bed would need to absorb or reference all of these before a head can build. |
| **What the bed has that the NEW card drops or contradicts** | Three-vendor comparison (Codex App Server `process/*`, Claude `--bg --exec`, Zellij). `research.approaches.2026-11-17.md:22-29`. Six-row test matrix from Oraculum. `consult.oraculum.2026-11-17.md:57-66`. Operation-specific proof obligations table (observe/read, attach/detach, type/submit, resize, interrupt/EOF, takeover/handback, terminate/recreate). `architecture-preparation.md:262-270`. Houston's five constraints. `consult.houston.2026-11-17.md:20-43`. Architecture document preparation (ARCHITECTURE.md §4 seam row, §2 paragraph, PROJECT-DESIGN.md §2.2 pointer). `architecture-preparation.md §7-8`. Generation-number takeover mechanism from RETURN 01 M6. `_bus/01.claude-colleague.return.md:135-139`. | The NEW card does not map to these; whether they are superseded or still required must be decided. |

⚡ CONFLICT — executor death semantics: RETURN 01 M3 states that in the X1 fixture, "the executor holds the PTY master (`probe.py:43`). When it dies, the master closes and the shell gets SIGHUP. So a 'restarted executor' always means a new shell incarnation." `_bus/01.claude-colleague.return.md:92-95`. The NEW card uses two separate panes; tmux holds the exec pane's PTY, not the executor. So executor death does not kill the shell. The NEW card rule 13 says "On start, anything found in `inflight` is moved to `unknown`." `NEW.card:107-109`. These are compatible designs but require the bed's X1 proposal to be abandoned or rewritten.

⚡ CONFLICT — send-keys and L4: The NEW card uses `tmux send-keys` as a doorbell ("sends one line, `source` plus the quoted absolute path of the frozen file"). `NEW.card:84-86`. L4 (`flag.md:20-22`) locks "tmux send-keys injection" as a recorded death. The RUNBOOK preserves L4 (`RUNBOOK.md:103`). Whether a single-line source-doorbell is inside or outside L4's scope is not resolved in any file.

⚡ CONFLICT — gate status: STATUS.md says no X0 acceptance and no X1 release has been recorded; next is Cartan's VERDICT on RETURN 01. `STATUS.md:34-36, 39-41`. The NEW card says "design agreed." `NEW.card:4`. These are in tension. No file records Majkee closing the X0 gate or Cartan writing a VERDICT. (Whether the NEW card represents Majkee bypassing the gate is not established in the files. `inferred`.)

---

## 4. Gate texts and next steps found in the files

Gate text (X0 preparation gate). Verbatim from `pulse.md:19` and `STATUS.md:12-14`, identical to `RUNBOOK.md:8-10`:
"Majkee records GO or STOP on an evidence-backed preparation packet for a human-and-agent shared task terminal: dated native/reuse alternatives, Oraculum technical consultation, Houston architecture and documentation review, a disposition of file-fed container requests and operator-selected input regimes, and the exact scope and proof obligations of one recommended next experiment."

Proposed X1 gate. `next-experiment.proposal.2026-11-18.md:21-25`:
"Majkee records GO or STOP on an independently checked synthetic file-to-task-terminal round trip: an explicitly submitted command file reaches one newly owned persistent shell exactly as intended, correlated output and truthful outcome are readable, incomplete, changed, duplicate and stale-target requests do not cause unintended execution, and the owned processes and temporary runtime are cleaned up with retained evidence."

Oraculum's proposed preparation gate (never adopted). `consult.oraculum.2026-11-17.md:85-89`:
"Majkee accepts a source-grounded comparison of file-driven jobs, a persistent worker and a shared PTY task session; a frozen six-row synthetic test specification; and Houston's disposition of lifecycle, delivery and permission boundaries. Open choices remain attributed. Acceptance releases no native-session attachment, container deployment or shared transport adoption."

Next-step statements:

STATUS.md `next:` field, 2026-11-19: "Cartan on office verifies RETURN 01 against POINT 01 and cited artifacts, then writes `_bus/01.cartan.verdict.md` with confirmed/refuted/unverified findings and the effect on the proposed X1 scope. Resolve the open design choices before requesting an actual release." `STATUS.md:39-42`.

RETURN 01 recommended next task (ranked verdict): "1. REVISE X1 (keep its file → persistent shell → correlated result core), ahead of 2. prefer the native Claude shell-job qualification (cheaper for the human half, but it cannot supply agent input and needs a separate release) and 3. proceed as written." `_bus/01.claude-colleague.return.md:171-174`.

RETURN 01 smallest coherent change: "Rewrite the proposal gate to add exactly two rows and remove two artifacts: + Row A (second client) [...] + Row B (busy foreground) [...] − Markdown history and current-state snapshot [...] Restate restart as new incarnation (M3) and define duplicate (M5)." `_bus/01.claude-colleague.return.md:181-189`.

After X1 gate. `next-experiment.proposal.2026-11-18.md:79-82`:
"Use its result to choose the smallest qualified process-owner/attachment path. Then qualify actual human attachment, input takeover and native CLI access, preserving ovitmugen lifetime and the distinction between task-program input and conversation delivery. Only after that should collection/retention policy, usage regimes and a durable component home be selected."

eSharp assignment. `eSharp.decisions.majkee.2026-11-22.md:75-79`:
"Group 2 (Codex head, Codex controller, Claude auditor) takes the terminal-workspace line, and the NEW card is read against today's bed first. My answer to his question: yes, by not reading either line raw — two reader agents write one brief each, with file-and-line pointers, and the RUNBOOKs are written from the briefs."

---

## 5. Locks and organ boundaries

**L3/L4** (`flag.md:14-22`): L3 locks "adapter-owned PTY, tmux never the protocol." L4 records as dead: "tmux send-keys injection." The bed preserves both (`RUNBOOK.md:103`). The NEW card's send-keys doorbell requires L4 to be interpreted — the bed explicitly says "rejected input mechanisms stay rejected" (`brief.cartan.2026-11-17.md:35`). No file resolves whether a single-line source-doorbell is injection in L4's sense.

**L14** (`flag.md:88-111`): D1 — PTY is the base layer for session relay; "full PTY orchestration as architecture stays dead." D2 — the file plane is the spine; no transport is truth. D7 — blind triangulation before locking relay architecture. The bed cites these throughout. The NEW card's "same envelope as the existing CLI-to-CLI bus" and the file-based state machine are consistent with D2. The architectural distinction between task-terminal input and relay/room bus is required by L14 and stated in `architecture-preparation.md:118-119`: "no new room journal, agent-assignment transport or autonomous terminal sender is installed by this preparation."

**L17** (`flag.md:193-216`): Termbrana is the terminal membrane (Zellij observer + composition family). Ovitmugen keeps view/layout and protected process-lifetime ownership. "Discovery is not delivery authority; future transmission requires checked target binding and explicit authority." The bed requires the new organ to avoid displacing ovitmugen's lifetime role. `architecture-preparation.md:116-117`. The NEW card does not address ovitmugen.

**L20** (`flag.md:235-242`): VIST is an observation principle. "Observations authorize nothing." The bed's exec-pane idle check ("Dispatch only when the last event from the current shell pid was a prompt") — `NEW.card:92-94` — is explicitly labelled "a heuristic, not a lock." `NEW.card:93-94`. This is consistent with L20.

**L21** (`flag.md:244-256`): "the Phase 0 build authorizes no shared layer, framework or transport implementation; designing them is architectural work, and implementing, activating, delivering through or adopting a transport for any of them needs its own separate release." The NEW card rule 30 ("Remote consumers... that bridge belongs to the bus") defers bus integration to a separate decision; this is consistent with L21.

**L13** (`flag.md:82-87`): termpanum = observation lab; stridulatrix = broker+CLI. No new room journal is authorized. The bed states explicitly no new stridulatrix room journal or autonomous terminal sender. `architecture-preparation.md:119`.

**L18/L19** (`flag.md:218-233`): A new organ body starts as a component folder with a thin README; product rationale cites the session authorization. No permanent component directory is selected in this preparation. `RUNBOOK.md:114-116`.

Organ placement stated in the bed (`architecture-preparation.md:116-121`):
- Ovitmugen: preserve its lifecycle responsibility; ask its owner whether task shells attach as existing views or need an explicit extension; do not create a competing lifecycle manager.
- Termpanum/Termbrana: reuse the PTY-bytes vs. rendered-state vs. derived-observations distinction. Input is a different capability.
- VIST (L20): no observed prompt/idle signal grants authority to execute or answer.
- Stridulatrix room/delivery: no new room journal, agent-assignment transport, or autonomous terminal sender.
- Phone-console: reuse fixed-attach and target-generation lessons; its paused gate is not resumed.

---

## 6. What already exists and could be reused

`raw/probe.pty-feasibility.2026-11-17.py` + `probe.pty-feasibility.2026-11-17.json`:
Synthetic PTY feasibility check; six checks pass; `qualified: false`; script hash `1de49ad3...0bea`; runs in a private PID namespace in an isolated temp dir; cleanup confirmed. This is the only code artefact with a measured result. Result: same-shell state (cwd, env variable, function) is retained across two sourced files; fresh processes do not retain it. Eight things unproven. `probe.pty-feasibility.2026-11-17.json:17-26`.

`raw/consult.oraculum.2026-11-17.md`:
Bounded technical child consultation. Result: recommends persistent attachable task process with file requests; proposes a six-row synthetic test spec; flags L3/L4/L14/L17/L20 constraints; names the busy-shell problem explicitly (`consult.oraculum.2026-11-17.md:24`). No runtime work performed.

`raw/consult.houston.2026-11-17.md`:
Architecture consultation; verdict `stretches`. Five constraints returned; exact proposed ARCHITECTURE.md §4 seam wording supplied. `consult.houston.2026-11-17.md:14-43`. No files written by Houston.

`raw/research.approaches.2026-11-17.md` + `raw/research.correction.2026-11-17.md`:
Dated primary-source approaches research; four families matrix; six primary sources (Codex exec, App Server, Claude background bash, Agent View, Zellij, Docker); correction clarifies Claude `--bg --exec` as a PTY-attach candidate and Termbrana observer vs. composition scope.

`raw/architecture-preparation.md`:
Candidate architecture document; approach disposition; proposed ARCHITECTURE.md §4 seam row + §2 paragraph + PROJECT-DESIGN.md §2.2 pointer; eight open architectural questions; operation-specific proof obligations table. Houston's five constraints integrated in §8. `architecture-preparation.md`.

`raw/next-experiment.proposal.2026-11-18.md`:
Proposed X1 gate and six-step concrete demonstration. The gate text is stated; the effect envelope is bounded. This is what RETURN 01 assessed and recommended REVISE on.

`_bus/01.claude-colleague.return.md`:
Independent technical review; REVISE verdict; eight mismatches (M1-M8); concrete design improvements including OSC 133 mechanism sketch, three-signal completion model, three-axis independence (execution scope / input owner / lifetime), write-ahead ordering. All mechanism proposals are unproven at runtime. `_bus/01.claude-colleague.return.md`.

`raw/handoff.claude-colleague.2026-11-19.md`:
Distilled X1 delta proposals (five changes: +Row A second client, +Row B busy foreground, -Markdown/snapshot, restart=new incarnation, define duplicate). Marked "proposals only" — Cartan has not dispositioned them. `handoff.claude-colleague.2026-11-19.md:5`.

---

## 7. Links to other lines

**Relay line:**
T6 from `relay-X0-carryover/raw/decision.majkee.walkthrough.2026-11-21.md:120`:
"The shared-terminal organ is a possible future carrier for structured status events. Review Majkee's newer substrate when that interface is ready to be decided." Status: deferred (`decision.majkee.walkthrough.2026-11-21.md:123`). T6 also states "The paired session-window helper is the likely operator surface for a deadline, the seat that owes the next action, and alerts or errors." (`decision.majkee.walkthrough.2026-11-21.md:119`).

NEW card rule 30 (`NEW.card:167-170`): "Remote consumers. An agent with no access to this host [...] needs a bridge that carries requests in and records out. That bridge belongs to the bus, not to the executor." This directly names the relay/bus as the future delivery mechanism for remote agents, not part of v0 or v1.

The bed's architectural placement: "stridulatrix room/delivery — no new room journal, agent-assignment transport or autonomous terminal sender is installed by this preparation." `architecture-preparation.md:119`. This separates the terminal execution organ from the relay bus at the design level.

**session-window helper line:**
`eSharp.decisions.majkee.2026-11-22.md:33`: "A staggered start: the helper-window group first, the shared-terminal group once the first has closed a cycle." Group 1 (Claude head, Codex controller, Codex auditor) takes session-window; Group 2 (Codex head, Codex controller, Claude auditor) takes terminal-workspace. `eSharp.decisions.majkee.2026-11-22.md:75-76`.

T6 (`decision.majkee.walkthrough.2026-11-21.md:119`): session-window helper is "the likely operator surface" for status events linked to the terminal organ. These two lines share a surface dependency: terminal-workspace can emit status; session-window displays it.

The git commit record (`ia-sync` commit `2026-11-19`): `helper-utils-00-tmux` was moved to `nablarva session-window-X0-substrate` (MOVED.md tombstone). The session-window line holds the tmux helper substrate that the terminal-workspace line may rely on.

---

## 8. Read-first list for a head

1. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/raw/NEW.read-before-continue.shared-terminal-organ-card.md` — the design card, v2 2026-11-22; most current; operator-designated as "fresher than the rest of the bed." Read first.

2. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/STATUS.md` — current gate position; holds and next action; recovery probe.

3. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/raw/architecture-preparation.md` — full prepared architecture candidate; Houston constraints; operation-specific proof obligations; proposed documentation deltas.

4. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/_bus/01.claude-colleague.return.md` — REVISE verdict; eight mismatches (M1-M8); undispositioned; mechanism proposals; role proposal for the build.

5. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/RUNBOOK.md` — gate law; participants; constraints; operator-authorized additions.

6. `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — read L3, L4, L14, L17, L20, L21 in full before authoring any gate that includes send-keys, lifetime ownership, or bus integration.

7. `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md` — which group takes this line, sequence, staggered start, what the manager needs before writing RUNBOOKs.

8. `/home/hruzam/unikuklatrix/nablarva/.dev/session/terminal-workspace-X0-approaches/raw/next-experiment.proposal.2026-11-18.md` — the proposed X1 gate still formally in play; the RUNBOOK head must decide whether to carry it, replace it with the NEW card's v0 build order, or close it.

**Files stale against the NEW card:**
- `raw/next-experiment.proposal.2026-11-18.md` — X1 narrow scope (single-pane Python probe, no second client, single-client batch executor framing); superseded by NEW card's two-pane v0 design. RETURN 01 also said REVISE on this proposal; it has never been updated.
- `raw/handoff.claude-colleague.2026-11-19.md` and `_bus/01.claude-colleague.return.md` — the REVISE delta proposals (Row A and Row B) are partially addressed in the NEW card's acceptance probes; the files are not formally dispositioned and STATUS.md records them as pending Cartan's VERDICT.

---

## 9. Open questions only Majkee can answer

As left by the files. No new questions invented.

From `handoff.claude-colleague.2026-11-19.md:79-81`:
1. Accept the two-row revision into X1, or keep X1 narrow and open the second-client case as X2?
2. Release the native Claude shell-job lane in parallel (needs native CLI launch authority), or defer it?
3. Is a synthetic second client enough for the X1 gate, or must you personally attach once as witness?

From STATUS.md `holds:` field (`STATUS.md:33-34`):
4. Reviewer suggests a second synthetic client and busy-foreground rejection; are these proposals accepted by Majkee, or pending Cartan's VERDICT only?

From architecture-preparation.md open questions (`architecture-preparation.md:122-125`):
5. Who may create and end the task shell? Who can revoke input and acknowledge takeover? Does queued input survive handover? Which view controls geometry? How are target incarnation and uncertain results reconciled?

From NEW card (`NEW.card:203-207`):
6. What does the existing bus already provide for ids, status and correlation? Reuse it where it does; the conventions above fill only what is missing.

From the CONFLICT on send-keys and L4 (this brief, §3):
7. Does the NEW card's single-line source-doorbell via `tmux send-keys` fall inside L4's "tmux send-keys injection" death, or is it architecturally distinct? This is a lock question only Majkee can gavel.

From the CONFLICT on gate status (this brief, §3):
8. The NEW card says "design agreed"; STATUS.md says no X0 acceptance and no VERDICT has been recorded. Does the NEW card replace or supplement the X0 gate? Must the VERDICT be written before the RUNBOOK head may treat the design as decided?

From `eSharp.decisions.majkee.2026-11-22.md:82-84` (not decided there):
9. The gates of the two groups; which seat pushes commits; the name of the separate tmux server; whether `eSharp` becomes a named protocol in the RUNBOOK guide.
