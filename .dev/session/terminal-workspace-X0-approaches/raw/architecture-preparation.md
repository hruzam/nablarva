# Shared task terminal — architecture preparation

Candidate · inferred: Cartan · 2026-11-17 · not a lock or implementation release.
Local base: nablarva `core@3318b17`; user authority is `request.majkee.2026-11-17.md`.

## 1. Intent and evidence

said: majkee — give CLIs a full terminal for working together with the human; explore
file-fed container requests and a regime like permission modes. Prepare the new line,
technical consultation, architecture/documentation and approaches research.

inferred: Cartan — the question is continuity of a task shell/program and human access to
that same running task. Agent conversation queues are an adjacent capability. A task
terminal distinct from the native conversation terminal is a candidate topology, not a
new operator lock. One dedicated terminal per agent, a deliberately shared team terminal,
and qualified access to a vendor-managed task process remain alternatives.

Technical consultation: `consult.oraculum.2026-11-17.md` (attributed child reply).
Approaches research: `research.approaches.2026-11-17.md` with mandatory
`research.correction.2026-11-17.md` (dated primary-source report and corrected scope).
Basic evidence: `probe.pty-feasibility.2026-11-17.json` and its pinned Python helper.
Architectural check: `consult.houston.2026-11-17.md` — stretches for preparation;
five constraints dispositioned in §8 and the exact candidate text below.
Missing outputs at cold entry are missing evidence, never implicit acceptance.

## 2. Separate the questions before selecting the mechanism

| Question | Candidate choices | What it does not establish |
|---|---|---|
| Where requests live | explicit tool call, immutable file, operator-approved draft | execution permission or consumption |
| What executes them | fresh job, persistent shell/worker, running foreground interactive application | human terminal attachment |
| Who owns process lifetime | qualified existing owner/API; tiny isolated fixture owner | ownership by an observer or detachable view |
| How terminal I/O is exposed | native process-control API, PTY manager/adapter, qualified attach proxy | application acceptance or correct screen rendering |
| What the human sees | existing emulator/attach surface; read-only or interactive client | automatic right to type |
| Who may type now | human control, agent control with takeover, approved operations, experimental shared typing | OS containment or native CLI approval inheritance |
| What limits effects | actual sandbox/container and scoped service access | consent merely asserted in a file |

Containers are an execution/isolation choice across these rows. They are optional until a
specific containment requirement is chosen. A short-lived container per request and a
persistent shell inside a long-lived container have different continuity and cleanup semantics.
A host Docker executable exists, but no daemon, socket, runtime, image or isolation was tested.

A prompt addressed to another assistant, a shell script, literal application input and an
interrupt/resize are distinct payloads. No watcher may infer executable intent from arbitrary
prose. Sourcing a script deliberately mutates the existing shell; running it as a child does
not automatically retain cwd, environment, functions or shell options in the parent.

### Operator refinement: commands through files, results through files

said: majkee, subsequent 2026-11-17 input — the agent should construct/write a command
file, a tool consume it when finished (closure suggested), and the agent see its result,
with minimal Bash needed on the agent side. Exact substrate:
`request.majkee.command-files.2026-11-17.md`.

inferred: Cartan — a minimal candidate interaction is prepare file → explicit submission
boundary → executor handles the request under the selected regime → output/completion
record → agent reads it. Bash/shell execution belongs inside the executor; agent-side
file operations can be the usual interface. This does not remove the shell from a shell
terminal, require two tmux sessions or select a container.

Submission remains open. Linux IN_CLOSE_WRITE reports closure of a file opened for writing;
it does not assert application-level readiness. A writer can reopen/edit a file. Prefer
an explicit ready/submit action, such as a final marker or atomic rename of a completed
request on the same filesystem, over executing every ordinary save. The consumer still
needs to identify/adopt the exact content once and apply the chosen input authority.
[Linux inotify manual](https://man7.org/linux/man-pages/man7/inotify.7.html), checked 2026-11-17.
This is a controller recommendation, not an adopted request format or watcher implementation.

Return output plus a distinguishable pending/running/completed/failed/unknown outcome
where actually established; absence of a result must not be interpreted as successful
execution or permission to retry. PTY output can combine stdout and stderr, so this candidate
does not promise separately attributable streams. No final result schema is selected.

First distinguish command submission while the shell can accept commands from input to
an already-running interactive application. A file carrying an answer/key sequence must
not accidentally be treated as a new shell script. Retaining cwd/env requires the same
live shell or an explicitly equivalent state model. Existing synthetic evidence covered
controlled sourcing, not a file watcher, completion receipts or real human handover.

## 3. Approach disposition — proposals

| Family | Why retain it | Missing fact before adoption |
|---|---|---|
| Native persistent task process | reuse the existing process manager and native tool policy where possible | human attachment, process identity/lifetime, full interaction and actual permission boundary |
| Existing terminal manager with a narrow qualified bridge | reuse human attach/rendering and lifetime machinery | governed agent route, exact target identity, writer/resize arbitration and compatibility with ovitmugen |
| File-fed fresh jobs | inspectable batch work and bounded isolated execution | cannot by itself provide one continuing interactive shell |
| File-fed persistent shell/worker | file substrate plus continuing shell state | who handles input while a foreground program runs; interactive and recovery semantics |

inferred: Cartan — first qualify reuse, then build only the missing seam. A custom broker,
mandatory envelope, append-only inbox/outbox, lease implementation, selected multiplexer or
container stack is not adopted by this comparison. A readable proposal file is not proof of
execution, so a controller must distinguish submitted, admitted, delivered, consumed and
completed whenever those distinctions matter. Exact receipt schema remains open.

Current native documentation contains useful task-process controls, but no cited source
establishes the complete requested shared-task-terminal experience for both vendors. In
particular, the documented Codex App Server `process/*` surface is experimental and outside
its sandbox; `command/exec` has a different sandbox contract. [Official App Server guide](https://learn.chatgpt.com/docs/app-server).
Claude documents attachable standalone PTY shell jobs as well as conversation sessions;
shared agent control remains unqualified. [Agent View — shell jobs](https://code.claude.com/docs/en/agent-view#run-a-shell-command).
Neither is treated as a qualified runtime on this host. Retrieved 2026-11-17.

## 4. Architectural placement and ownership questions

locked: flag L3/L4/L14/L17/L20/L21 govern the existing room, relay, observation and ownership
boundaries; cite those sources rather than adopting this note as a restatement of law.

inferred: Cartan — this candidate spans execution/session, observation and human-view
capabilities. It is not a capability extension granted by Sublime observation publication.
The task-terminal executor can be a client of existing mechanisms without becoming the
whole-animal room broker. If it delivers assignments into an agent conversation or becomes
a shared transport, that is a separate architectural/release question.

| Existing boundary | Preparation treatment |
|---|---|
| ovitmugen view/layout and protected process lifetime (L17) | preserve its assigned responsibility; ask its owner whether task shells attach as existing views or need an explicit extension; do not create a competing lifecycle manager |
| termpanum / Termbrana observation | reuse the distinction between raw PTY bytes, rendered ANSI/text and derived observations; input remains a different capability |
| VIST (L20) | no observed prompt/idle signal grants authority to execute or answer |
| stridulatrix room/delivery | no new room journal, agent-assignment transport or autonomous terminal sender is installed by this preparation |
| phone console | reuse fixed attach and target-generation lessons; its human-input pilot remains its own paused gate with unqualified native approvals/special keys |
| permissions / muticula | inspect actual enforcement and bypasses; do not claim native CLI permissions constrain an external worker automatically |

Open: whether a tool-managed PTY can be exposed safely; who may create/end the task shell;
who can revoke input and acknowledge takeover; whether queued input survives handover;
which view controls geometry; how target incarnation and uncertain results are reconciled.
These are distinct from ordinary observing, detaching, interrupting and killing a task.

## 5. What the basic probe did and did not show

Observed in this tool's sandbox PID namespace: the controlled shell was newly created with
`pty.fork`, clean Bash startup and a minimal nonsecret environment. Six checks passed:
file-sourced commands retained cwd, exported state and a function in the same shell; fresh
processes did not retain that state; TTY checks and a line reply worked; Ctrl-C reached an
owned foreground child while the shell survived; dimensions changed; a brief interval
without reading did not end the still-open PTY. The shell exited/reaped and temporary root
was removed. The JSON pins the source hash, namespace, command, transcript and result.

This is feasibility evidence, not product qualification. It used one controller as both
sides of the interaction, no actual human attachment, no vendor CLI, no container, no raw
single-key exchange, no renderer, no real detach/reconnect, no takeover protocol and no
crash/replay mechanism. Synchronization markers belong to this synthetic fixture only.
An initial exploratory run preceded the saved, namespace-recording run; no native session
or host process identity is inferred from the small sandbox PID values.

## 6. Recommended next experiment — not an execution grant

The concrete first slice is now specified in
`next-experiment.proposal.2026-11-18.md`: a synthetic file-to-persistent-shell round trip
with correlated results and failure checks. This is a narrowed precursor to the wider
matrix below. It establishes neither real human attachment nor native/vendor permissions.

inferred: Cartan, informed by Oraculum — select one available existing task-process/terminal
owner and compare it against fresh file-fed jobs. Freeze expected outcomes before execution.
Use one disposable target, synthetic text, one human-side client and one agent-side fixture;
initially no provider session, external service or container is required.

| Case | Discriminating evidence |
|---|---|
| Retained context | later request returns the same shell incarnation, cwd, exported variable and function |
| Foreground application | an independently specified TTY fixture records raw single-key and line input; a prompt alone is insufficient |
| Interrupt | child signal/exit receipt plus independent proof the intended shell survives |
| Detach / reattach / resize | same live process survives an actual client disconnect; dimensions and rendered view checked separately |
| Input handover race | actual received-byte trace identifies inputs before/after acknowledged takeover; stale queued input is rejected or explicitly dispositioned |
| Lost receipt / replaced target | fixture-owned effect counter distinguishes consumed from merely submitted; no blind replay or addressing a replacement by old identity |

The local basic probe covers only parts of rows 1–3 and resize. Rows 4–6 and all native
permission paths remain untested. Native provider qualification, container deployment,
shared transport adoption or lifecycle changes require their exact next release. This
session need not open a successor bed or choose a product stack to prepare that request.

## 7. Documentation preparation — proposed homes and text

Current home: this experimental bed, linked by pulse and `terminal-workspace-X.ledger.md`.
No organ category or permanent component source directory is selected (L18/L19).

After Majkee's disposition, coordinate durable integration with the existing document owner.
`architecture-X1-bookkeeping` records gate complete, closure pending; its router row does
not mean that its earlier documentation implementation remains unfinished. Prepared deltas:

- `docs/ARCHITECTURE.md` §4 seam ledger: propose one candidate **task execution / shared
  terminal** seam, with owner explicitly open, consumers human/agent, governing locks cited,
  and no accepted implementation claim. Proposed cell wording: “Persistent task-process
  access, human attachment, input authority and lifecycle integration — preparation only;
  mechanism and ownership open.”
- Same document §2 / relevant seam note: if the design is adopted, document the distinction
  between agent-conversation delivery and task-program input, and the relationship to the
  existing lifetime owner. Add no new plane or ownership transfer merely for symmetry.
- `PROJECT-DESIGN.md` §2.2: one thin exploratory capability pointer if accepted, pointing to its
  actual home. Keep comparisons, tests and detailed contracts out of the wrapper.
- A future accepted component keeps its detailed contract in its existing home, or starts
  with a thin component README under L18 after the source parent is assigned. Product
  rationale cites the session authorization under L19; new locks remain Majkee's flag pen.
- Durable citations to this prunable bed require a preservation commit. Until Majkee commits,
  paths here are working references only; do not invent a commit pin for these new files.

No patch is applied to architecture, wrapper, flag, existing components or native harness.
Houston has checked this preparation; its constraints are applied below. This is an
architecture candidate, not an operator acceptance or capability qualification.


## 8. Houston disposition and exact candidate documentation

inferred: Cartan — Houston's `stretches` applies to this preparation within five constraints:
endpoint boundary, protected lifetime ownership, operation-specific authority, concrete
bed-local documentation deltas and source-error disposition. The returned finding is
preserved verbatim; this section records the controller's integration, not a new Houston
verdict. No architecture lock or release is claimed.

### Candidate §4 seam row — for later integration into docs/ARCHITECTURE.md

| seam | owner | consumers | governing | accepted | planned | open |
|---|---|---|---|---|---|---|
| **task-program input / shared terminal** (inferred: cartan; preparation only) | open; process/lifetime integration must preserve §4.4 and L17 | human and agent clients of an identified task shell/application | L3/L4/L14/L17/L20/L21, each in its existing scope | no runtime capability accepted by this preparation | qualify native/reusable task-process access and human attachment | component ownership, mechanism, input authority, lifecycle integration and operational proof |

Accompanying seam note:

> inferred: cartan — The endpoint is an identified task shell or application. Delivery of
> an assignment into a living agent conversation belongs to the existing delivery seam
> and its qualification (§4.3). Process/lifetime integration remains unresolved (§4.4);
> a technical PTY owner does not acquire architectural lifetime authority or turn
> ovitmugen into an input sender.

### Candidate §2 dependency paragraph

> inferred: cartan — Task-program interaction and delivery into an agent conversation
> have different endpoints and acceptance conditions. L14's impulse-only description is
> a relay plan, not a universal restriction on interactive task-program input bytes.
> This study grants no exception for conversation injection or full relay orchestration;
> L4's rejected mechanisms remain rejected. Process ownership, input, resize, interrupt,
> takeover and termination each require their own established authority and integration
> with the existing lifetime seam (§4.4).

### Candidate PROJECT-DESIGN.md §2.2 pointer

> Exploratory shared task terminal: preparation compares native/reusable task-process
> access, human attachment, file-carried requests and input regimes. Mechanism and
> component ownership remain open; working preparation is routed through pulse.md.

No new organ entry or PROJECT.yaml key is proposed. An accepted durable evidence link
will replace the generic working pointer only after its preservation commit is available.

### Source corrections and verification

- Preserve the research reply and correction separately. Its global “Termbrana is
  observation-only” description applies only to the Zellij observer. L17 also assigns
  Termbrana its composition family; no new sender is created here.
- L14 D2 locks the file spine. Only the impulse-only formulation is a plan. The research
  slash formulation must not demote the file-spine lock or promote the impulse mechanism.
- Controller opened the official Agent View page, including “Run a shell command” and
  “Peek and reply,” on 2026-11-17. The initial conversation-only reading omitted the
  standalone shell-job path; the saved researcher correction supersedes that reading.
  Runtime interoperability and permissions still require qualification.
- Controller checked the App Server command/process sections and their distinct sandbox
  contracts; Linux PTY semantics; and the Zellij terminal documentation. Primary URLs
  are in the research report. Current documentation is not proof of installed versions.
- Local checks covered flag, architecture §§1–4/7, the phone live-attachment contract,
  Termbrana README, the architecture-X1 doing-state and adjacent session holds. Historical
  receipts remain historical; no adjacent live service, owner operation or gate was resumed.

### Operation-specific proof obligations for the next release

| Operation | Boundary to identify and prove |
|---|---|
| Observe / read | explicit shared target and representation; grants no write capability |
| Attach / detach | bound process incarnation; detach must not silently terminate it |
| Type / submit | actual authorized writer and route, including direct-attachment bypasses |
| Resize | authorized geometry source and effect on every attached view |
| Interrupt / EOF | intended terminal/program semantics; distinct from view detach and kill |
| Takeover / handback | acknowledged input-owner boundary; explicit treatment of queued/in-flight input |
| Terminate / recreate | lifecycle owner's authority, cleanup and a new process incarnation |

This packet favors a reuse-first discriminating experiment and leaves the actual owner,
bridge, policy enforcement, container choice and input regime for explicit selection.
