outside
<!-- composer:packet r0zz -->
format: request/0.1
id: source-0
from: Majkee
to: myShell
requested_scope: read-only
<!-- composer:body r0zz -->
# Two counsel views — prompt composition and human relay

Cycle: `myshell-nabla-composer-counsel-01` · 2026-10-17 · controller: myShell.
Personal design consultation authorized by Majkee; proposals only, no implementation or project lock.

The fixed advisory gate is two initial views, one reciprocal read by each adviser, and two
attributed short briefs saved in this collection. myShell alone writes these files. The advisers
return in chat and have no project, STATUS, deployment, or transport pen.

## Shared question

Majkee currently composes and carries inter-agent requests through a long journal in Sublime.
He wants a simpler semi-automated process: useful without an agent, faster with agent assistance,
uniform caller/loading tags, on-demand commands, and perhaps later explicit tmux delivery.
Challenge should be a repeatable useful operation. Cold starts should need less reconstruction.

Astrobley was asked for a senior developer's smallest build; Oraculum for philosophical and
process critique using buffering's creative exploration. They first read the same README and
CONTEXT. Their design judgments are not independent audits of all primary sources in sources.json.
The current Ovitmugen input prohibition remains a constraint on the consultation.

## Astrobley — first view

> Build a local prompt composer first: human-readable message files in Sublime plus one small CLI
> that validates and renders them. No broker or transport is needed to test whether it reduces
> Majkee's composing and recovery work.
>
> Minimum envelope: id, kind (POINT/RETURN/VERDICT), from, to, in_reply_to, context references,
> bounded task, expected return, and stop condition. Keep task prose free-form. A tiny local catalog
> maps caller tags to actual controller/function documents and their expected stamps; tags expand
> to explicit load instructions and never grant execution authority. A challenge can be one named
> function with required inputs and expected output, rather than a special conversation ritual.
>
> CLI surface: `prompt new`, `prompt check`, `prompt render`. `new` creates a fillable template;
> `check` catches unknown tags, missing fields, broken references, and reply-link mismatch;
> `render` prints a deterministic, complete prompt for preview/copy. Start with templates, not a
> Sublime plugin. The human can perform every step by editing a file; the agent uses the same
> files and commands. Use a format with existing parser support rather than inventing a DSL.
>
> Flow: select context and task → compose → check → preview → Majkee manually carries the rendered
> prompt → recipient returns a message referencing its request → the integration owner records
> VERDICT and the next action. Composition IDs identify messages, never permission, delivery,
> acceptance, or completion. Keep a frozen copy/hash of the carried render so later edits cannot
> change what the request actually said.
>
> Ownership: Majkee controls dispatch and locks; each participant returns within its assigned scope;
> the integration owner alone updates STATUS and shared conclusions. The composer owns drafts and
> render outputs, not project state. Drafts should be visibly distinguishable from carried packets.
>
> Cold start: maintain one compact current card per sitting containing the owning STATUS path, the
> open request ID, last return/verdict IDs, recovery probe, and one next action. It should point to
> evidence and mirror no second project status. A fresh agent reads that card, the instruction chain,
> and the linked owner files rather than replaying the journal. Delivery uncertainty stays explicit
> until a human receipt resolves it.
>
> Defer Sublime integration, automatic context selection, return scraping, queues, cross-host
> transport, and tmux input. Current Ovitmugen forbids injection; future tmux delivery needs a separate
> explicitly authorized adapter with target validation and duplicate-send/recovery semantics.
>
> Hard question for Oraculum: What is the smallest durable evidence that distinguishes 'rendered',
> 'carried', and 'accepted after interruption', without creating a second owner of project STATUS
> or implying a broker?

### myShell's two corrections and Astrobley's reply

The first view proposed a new caller catalog and a current card carrying next/probe fields.
myShell asked whether those would duplicate existing controller tables and project STATUS.
Astrobley replied:

> Agreed on both corrections. Resolve function/tag bindings directly from the existing controller
> table; avoid a second registry. Keep only personal message workflow pointers in the composer
> index and read the current next/probe from owner STATUS; a stale copied value would recreate
> the current continuity problem.

The first view is preserved above so this revision remains visible.

## Oraculum — first view

> The strongest framing is a small decision workbench whose output is a readable handoff.
> Transport can follow after the handoff consistently survives a fresh reader.
>
> Observed: the supplied briefing describes journals carrying exchanges, costly recovery, distinct
> lifecycle owners, and a conflict between proposed injection and Ovitmugen's prohibition. These
> are claims in the inspected briefing; I have not independently inspected their project sources.
> The local instructions explicitly withhold project ownership from personal continuity work.
>
> Three framings expose different problems:
>
> 1. Courier: reduce copying between agents. Useful, but faster delivery can amplify stale requests
>    and mistaken authority.
> 2. Prompt composer: help a person express a bounded request and load the right evidence. This
>    addresses cold starts but can turn into an elaborate template catalogue.
> 3. Decision workbench: preserve the question, evidence, disagreement, and human disposition across
>    an exchange. This is the strongest starting point because it explains why the messages exist.
>
> My inference is that the hidden constraint is Majkee's capacity to understand and own the next
> commitment. Reducing keystrokes helps only when it also reduces reconstruction. The briefing's
> reported stale requests and bookkeeping defects are weak signals that copying is only part of
> the cost.
>
> The following is a proposal, not an existing contract.
>
> Start with one ordinary Markdown exchange, readable in Sublime, with one integration writer.
> Its opening block answers: what is being decided, who is asking whom, what evidence must be read,
> what may be done, and what return is expected. Named returns and the controller's disposition
> follow. The journal carries a short pointer. Existing project files retain their authority.
>
> An on-demand composer can help assemble this block, flag missing information, and produce a
> copyable prompt. The readable document should remain sufficient when the command is unavailable.
> A cold-start capsule should explain enough to orient the recipient, then point to the smallest
> necessary source set; sending an entire journal recreates the original problem.
>
> Tags should express address, operation, and reading intent. For example, `to`, `from`, `read`, and
> `return` can make a packet recognizable. They do not authenticate a sender, establish project
> authority, prove that reading happened, activate quoted instructions, or guarantee a live
> recipient. A recipient reports what it actually read and where it stopped.
>
> Challenge becomes a process when its return can change the next step. Before requesting it,
> name the proposition under challenge and the evidence that would require revision. Afterwards,
> the controller records “changed because…,” “retained because…,” or an unresolved decision.
> A generic approval request with no possible consequence is ornamental.
>
> Keep transport, runtime discovery, automatic retries, and project protocol design outside this
> first decision. Later human-triggered tmux delivery would require separately settled ownership
> and authorization; it cannot silently expand Ovitmugen's role. Sending text, receiving it,
> accepting a task, and completing it remain distinct events.
>
> Hard question for Astrobley: If a fresh recipient cannot find a required source, or reads a packet
> whose authority has expired, how does your minimum device make that visible before polished
> prompt composition or delivery creates the appearance of progress?

## Reciprocal reading

Each adviser was addressed once with the complete first-view exchange above. Both reported
reading it and returned a final snippet answering the other's hard question. The final briefs are
[Astrobley](FOR-NABLA.astrobley.md) and [Oraculum](FOR-NABLA.oraculum.md).

## myShell readback after both final returns

Both now support a human-readable exchange, optional composition/check/render commands, reuse of
existing function bindings, and separate records for rendering, carrying, and acceptance. Both
keep project next/probe state in STATUS and defer delivery. Command names are illustrative;
this consultation did not build or install them.

Oraculum's final snippet retains a preference for an exchange as the primary reading unit and
describes Astrobley's starting point as message files. Astrobley's later final snippet already
chooses one Markdown exchange with individually renderable blocks. That chronology reduces the
apparent disagreement to emphasis: human reading favors the exchange; a dispatch addresses an
individual packet. Neither return proves which layout works better in a real interrupted sitting.
The original attributed wording is preserved in each brief.

The useful correction is concrete: a new caller registry and a second current-state card were
proposed, challenged, and removed from the practical recommendation. Missing inputs or unresolved
authority remain visible; a checker cannot certify semantic authority. A future pilot could test
whether one exchange and a short owner-state pointer let a fresh reader recover without the journal.
This is a proposed test, not an opened implementation gate.

The personal advisory gate is complete: first views, reciprocal reads, and attributed final
snippets are recorded. Majkee retains the design choice and any later build authorization.
<!-- composer:end r0zz -->
notes between
<!-- composer:packet r1zz -->
format: request/0.1
id: source-1
from: Majkee
to: myShell
requested_scope: read-only
<!-- composer:body r1zz -->
# Sella-v.0.1 design exchange

Cycle: `myshell-sella-language-02` · 2026-10-17 · myShell controller.
Personal Nabla.Tmux design material; no new Sella law, runtime, parser, or project gate.

Majkee requested three perspectives: Astrobley as programmer, Oraculum as project designer,
and myShell as the agent using the proposed device. This file records controller summaries of
the two first returns and their exact hard questions. Final author briefs follow one reciprocal
read. myShell alone holds this artifact pen; advisers return analysis in chat.

## Astrobley — programmer's first proposal

Use human-readable request files, a deterministic loader/render core, and separate runtime
adapters. Preserve task meaning and ownership while allowing different execution outcomes.

The proposed source is Markdown with a small structured header: format version, message ID,
sender, integrating recipient, requested consultants, program/function, and requested scope.
Task prose remains opaque text after the header. A parser must not turn quoted tags, punctuation,
backticks, or shell-looking text into new control instructions. Unknown/duplicate control fields
and invalid function bindings should produce explicit diagnostics.

Resolve existing program/controller tables instead of building another binding catalog. Capture
actual byte identities; matching stamps are version/binding observations, not content hashes or
proof of reading. The generated machine representation is derived data, never another editable
authority. A loader can provide the agent only selected bodies plus a concise checked identity
and the operative limits; placement in a footer alone cannot exclude metadata.

Adapters should prepare plans before execution: native delegation when the route is observed and
authorized; manual rendering when explicitly acceptable; unsupported when a required capability
cannot be preserved. No whole vendor is declared uniformly capable. A generic CLI remains
unqualified until its actual interaction, permissions, lifetime, and return channels are checked.

Keep load, render, dispatch, return, and fold separate. A fold requires a named destination,
owned scope, exact candidate content, evidence checks, and write authorization. A future automatic
writer would need deduplication tied to the actual durable update, a target version check, and
credible concurrency ownership. A lock does not stop an unrelated Sublime save. Begin with
prepared/manual folds if that writer boundary is unresolved.

Exact hard question for Oraculum:

> Which exact failure must make a request non-executable rather than merely qualified, while
> preserving the existing `list-pending` contract that missing owner evidence can return a useful
> partial inventory?

## Oraculum — project designer's first proposal

The shared language should express commitments and evidence through ordinary documents with
explicit runtime bindings. It should expose what remains the same across runtimes and what changes.

Three framings matter: a language expresses a task; a protocol governs request/acceptance/return;
a workbench helps people compose, inspect, challenge, and preserve that exchange. Start with the
workbench, supported by a narrow envelope. Do not build a universal instruction language or
capability registry before repeated work earns it.

The neutral core carries message relationships, purpose, scope, required evidence, authority
reference, consultation/execution intent, expected return, stopping condition, attribution, and
disposition. Prose keeps the actual question. Parsing cannot prove semantic compliance.

Runtime bindings must disclose material differences in evidence access, tools, isolation,
persistence, approvals, and returns. Capability declarations need dated observations. Similar
formatting cannot hide that one runtime supplied an isolated adviser while another continued the
same conversation. Consultation is a bounded relationship to an integrating owner; it does not
mean a particular spawn tool, and it does not confer the owner's pen. Fan-out topology also does
not establish evidentiary independence.

A fold preserves attribution and claim status. Copying a recommendation does not make it a fact
or a lock. Disposition records adopted-for-this-task, revised, rejected, or unresolved with reasons;
project current state and canon retain their existing homes.

A later pilot should use one low-consequence consultation, two genuinely different bindings,
one challenge, and a fresh-reader interruption check. Freeze question and evidence, compare
semantic obligations rather than cosmetic outputs, and include a negative case such as a missing
source or unsupported isolation requirement. One pass is a dated receipt, not runtime equivalence.

Exact hard question for Astrobley:

> What observable evidence would make your adapter refuse to present two similarly formatted
> returns as equivalent when one request required an independent consultation and a runtime could
> supply only continuation in the existing context?

## myShell — questions for the reciprocal pass

1. Separate missing evidence that prevents an operation from missing evidence that the selected
   procedure explicitly permits an uncertain partial report about. Do not make every unknown a
   global stop, and do not let a partial report silently proceed to dependent mutation.
2. A claimed `read-only` scope and an enforced read-only environment differ. The adapter should
   report requested limits and actually observed controls separately.
3. Preserve the current informal tags for human composition. A deterministic file format should
   be explicit; agent normalization of shorthand should make a reviewable draft, not guess identity
   or silently execute an ambiguous route.
4. v0.1 can automate preparation while existing authorized function owners perform folds.
   An automatic journal writer should wait for credible ownership and recovery with Sublime.
5. Keep runtime role bindings distinct from local procedure bindings. `consult: Astrobley` names
   a collaborator; `program: journal-continuity` selects a manual procedure. Neither creates the other.

## Evidence limits

Sella's opening boundary and L1–L9 are design inputs. Its own state remains draft. Its older
application/glossary text still says pulse owns doing-state; the inspected current Nablarva L9′
and session guides instead give pulse the router role and STATUS the current position. Record
that mismatch without repairing Sella from this personal consultation.

The controller opened current official subagent documentation for Codex, Claude Code, and Gemini
CLI. They document different native surfaces. Documentation does not prove that an adapter is
installed, configured, authorized, or locally qualified. Current Codex consultation is observed
in this sitting; cross-runtime operation has not been tested.

## Reciprocal returns and myShell integration

Both advisers read this complete first-view exchange and returned their final author briefs.
Astrobley answered the context question explicitly: even a separate child may inherit history;
if the task requires no inherited conversation, invocation evidence must support that requirement.
Unknown controls remain unqualified, and a matching response schema cannot repair the gap.

Oraculum answered the failure question per operation: missing a governing procedure or mandatory
authority blocks that operation, while a selected procedure may permit uncertain partial subject
reports. A partial report never silently permits the dependent mutation. A blocked action can
still return a useful diagnostic.

All three perspectives favor fold preparation in this version, with application by the existing
authorized function owner. Automatic journal writing remains a later design question because
Sublime and other writers are outside a simple cooperative lock. Existing STATUS ownership and
canonical authority are preserved.

The remaining choices concern mandatory task semantics, acceptable substitutions, and whether
the small preparation interface earns its cost in an interrupted-reader pilot. No implementation,
pilot, runtime configuration, or canonical decision is authorized by this advisory record.

The personal advisory gate is complete once these briefs, the index, and their evidence identities
are saved and checked. This file records that bounded consultation rather than a project position.
<!-- composer:end r1zz -->
notes between
<!-- composer:packet r2zz -->
format: request/0.1
id: source-2
from: Majkee
to: myShell
requested_scope: read-only
<!-- composer:body r2zz -->
for-nabla.Tmux.chatbot ---

From Oraculum / gpt-6-astra
Project-designer proposal · personal Sella-v.0.1 candidate
No new Sella law or implementation.

The shared language should express **what is requested, under whose authority, with what
evidence, and what counts as a useful return**. Runtime bindings should explain how those
commitments can actually be met. Uniform wording is convenient; it does not establish equivalent
behavior.

Start with a readable exchange workbench. Use a small structured header for message identity,
relationships, procedure, participants, scope, evidence references, expected return, and stopping
conditions. Keep the question itself in ordinary prose. Humans can edit the exchange in Sublime;
optional tools can check and render individual messages.

Preserve informal tags for human composition. When an agent converts shorthand into the structured
form, it produces a reviewable draft. Ambiguous identity or routing remains unresolved. Quoted tags
and shell-looking text inside the body remain content. A parser recognizes declared structure;
it does not discover extra commands inside prose.

Two bindings must remain separate. A **procedure binding** selects an existing controller and
function. A **role binding** identifies a collaborator and the bounded relationship requested.
Naming Astrobley does not select a journal function, and selecting a journal function does not
create a collaborator. Existing controller tables should remain the source for procedure bindings.

Consultation means an advisory return to an integration owner. Fan-out describes how several
consultations run. Neither implies independent evidence. If a task requires separation from an
earlier answer, that requirement must be explicit and the binding must describe whether it was
achieved. A continuation in the same context cannot silently substitute for that requirement.

Each runtime binding should distinguish:

- what the request requires;
- what the runtime documentation describes;
- what the local configuration and observed controls support;
- what happened in this particular attempt.

For example, “asked to remain read-only” differs from “writes were technically unavailable.”
A native subagent feature does not establish the needed tool access, isolation, lifetime, or
return channel. Manual delivery can be a valid binding when its differences are explicitly
acceptable. This proposal makes no claim that such adapters already exist.

Astrobley’s failure question needs an **operation-specific answer**. A request is not executable
when its intended operation cannot be identified unambiguously, its governing procedure cannot
be resolved, its required authority is absent or contradictory, or a mandatory capability cannot
be preserved. Missing evidence blocks an operation when that evidence is a prerequisite under
the selected procedure.

Missing *subject matter* does not always prevent useful work. If `list-pending` permits an
uncertain partial inventory, the assistant can report what it found, identify unavailable owner
evidence, and qualify the result. It must not infer completion, clearance, or permission from
that gap. Missing the governing procedure itself is different: the assistant cannot invent its
partial-report rules. A blocked operation can still yield a diagnostic report explaining the
missing prerequisite.

Keep preparation, dispatch, acceptance, return, disposition, and fold distinct. A disposition
records what the integration owner adopted for this task, revised, rejected, or left unresolved,
and why. Copying a recommendation preserves its attribution and status; it does not promote it
into fact or canon.

For v0.1, automate **fold preparation** only. Produce exact proposed content, its destination and
owned scope, evidence references, and the intended effect. The existing authorized function owner
performs the fold under current rules and checks the target’s current contents. An unattended
writer should wait: a lock respected by one tool does not prevent an unrelated Sublime save.
Current project state remains in its existing owner files; the exchange preserves message history.

A narrow later pilot could use one low-consequence consultation, two materially different
bindings, one challenge, and an interruption. Freeze the task and required semantics first.
Include both a permitted missing-source partial report and an unsupported mandatory capability.

Acceptance should be observable: no silent substitution or dependent mutation; attributed returns;
a reasoned disposition; and a fresh reader who can identify the open request, accepted scope,
missing evidence, integration owner, and governing state without reopening the journal. Record
recovery effort against the previous workflow. One pass earns a dated receipt, not general
runtime equivalence.

Sella supplies useful draft principles: explicit boundaries, small native primitives, evidence
before promotion, and behavior that must be tested. Its historical vendor tables cannot establish
current capabilities. Its older pulse-as-doing-state passage conflicts with the newer router/STATUS
arrangement reported and checked by the controller. Preserve that mismatch; this personal brief
does not repair it.

The remaining design choice is which runtime differences Majkee considers acceptable substitutions
for each task class. Begin with a small readable envelope and explicit exceptions. Let repeated
failures justify additional language.

---
<!-- composer:end r2zz -->
notes between
<!-- composer:packet r3zz -->
format: request/0.1
id: source-3
from: Majkee
to: myShell
requested_scope: read-only
<!-- composer:body r3zz -->
## 1.4. OPERATIONAL BED

Volatile launch slot: create only the packet needed for the current relay; use it, fold a compact
receipt where authorized, then replace this slot for the next packet. The journal remains a
pointer, never project truth or a substitute for STATUS/RUNBOOK.

### Shared checks
>to-all:
```text
truth rule: old journals may hold unanswered work, parked ideas, or stale pointers. They are
  helping evidence only; every claimed active item is checked against its named current file,
  especially session STATUS/RUNBOOK, before it is carried or acted on.
carry rule: preserve the old entry; add an explicit pointer into the current active bed/day.
  Never auto-roll calendar days, delete stale prose, or make journal text the live next action.
```
>to-all: end


### myShell packet
>to-myShell : personal space 
```text
ctrl project-saddle&saddle-project : project ia-sync; scope: .dev/session/germline-03-foundation-audit/; authority: read-only; task: prepare the current instruction chain for this relay.
```

---

>to-all : prompt message exchange CONTAINER for myShell|majkee
>once read, can be changed point here some anchor|hook
>put content to block below, end is next `to-all end`
```to-myShell


```
>to-all end.
---

### Shared human relay — Cartan / Atlas / Majkee / myShell

>to-all: each packet below is one shared exchange thread. Keep the packet id stable; each sender
>adds only their own block and does not alter another sender's text.
>order: 1. fold authorized process evidence to its owned `_bus/` file; 2. return its path in a
>sender block; 3. Majkee/myShell replies in a separate block; 4. TUI confirms only that folded
>reply. Confirmation is never the next task.

```text
If the current project task authorizes an evidence receipt, first write it to the declared,
owned `_bus/` file. Then return the short pointer below:

from-<seat> to-myShell ---
packet: <id>
evidence: <absolute receipt path, or none>
observed: <short result>
uncertain: <remaining question, or none>
gate: <waiting for whom / what, or complete>
---

Use `to-majkee` instead when an operator decision is required. Majkee/myShell replies under the
same packet id in a separate sender block; a reply never edits the sender's original text.

LOADED confirms only that the addressed packet/reply was read. It grants no project write,
launch, receipt destination, STATUS/RUNBOOK authority, or gate change. If the reply is absent,
ambiguous, or conflicts with current project instructions, report that and wait.

For unopened germline-03, report the missing gate or receipt path. Do not create an empty bus or
start the audit from this relay alone.
```


--- 




>to-all : MSG volatile placement
>to-all: superseded rough draft — do not send; retained only as the operator's source wording
```
from-majkee to-cartan ---
packet: g03-cartan-hot-01
evidence: 
observed: 

uncertain: 
gate: 
---
atas is on his place. 

$csharp pass the preparing of .dev/session process by subagent `oraculum` (toml) i will navigate with skills we can use under oraculum run                                                                   
       








```


>to-cartan
```text
TUI carrier — paste this complete envelope to Cartan:

This is an explicit `$csharp` Germline-03 preparation cycle, not a measurement or Atlas launch.

Read the saved source, not a diff:
`/home/hruzam/reposoma/.majkee/journal/2026-10-16.md`

Read exactly:
1. the shared relay guard beginning `### Shared human relay` and ending `Do not create an empty
   bus or start the audit from this relay alone.`; do not treat later volatile text as guard;
2. the current `MSG volatile placement` packet `g03-csharp-01` addressed `from-majkee to-cartan`.

Skip the labelled superseded rough draft. Perform only `g03-csharp-01`, preserve Cartan's
navigation and STATUS ownership, and return its required `from-cartan` structured block.
```

>to-cartan
```text
from-majkee to-cartan ---
packet: g03-csharp-01
evidence: /home/hruzam/ia-sync/.dev/session/germline-03-foundation-audit/RUNBOOK.md;
  /home/hruzam/ia-sync/.dev/session/germline-03-foundation-audit/STATUS.md;
  /home/hruzam/.agents/skills/csharp/SKILL.md;
  /home/hruzam/reposoma/raw.guides/runbook/res/csharp-head-protocol.md
observed: Cartan is the declared Germline-03 STATUS owner and the audit-only foundation is live.
  The RUNBOOK lacks cSharp's required `head_note:`; Atlas remains parked and `_bus/` absent.
uncertain: whether this runtime exposes an available `oraculum` TOML target; no handle is assumed.
gate: Majkee explicitly invokes `$csharp` for this RUNBOOK and authorizes one analysis-only
  Oraculum preparation cycle. No measurement, Atlas POINT, bus creation, implementation, deploy,
  commit, or change outside the Germline-03 bed is authorized.
---

Mount cSharp first. Add only this required RUNBOOK front-matter field:

head_note: >-
  cSharp — this seat authored the RUNBOOK and stays live through the whole arc as navigator and
  status_owner; it may delegate every body of work and receive only navigation + test parts; it
  closes the session if it can.

Before the child turn, update the existing STATUS using its established fields: name cycle
`g03-csharp-01-process-prep`, its read-only recovery probe, this authority boundary, and the
single next verification edge.

Then, only if the runtime exposes the named `oraculum` target, open one new child for that cycle.
This packet is its explicit creation edge; record the observed target identifier. Do not guess or
recreate a lost target, and do not substitute another role if `oraculum` is unavailable.

Give Oraculum this bounded analysis body:
- question: what is the smallest compliant `.dev/session` process for Cartan's first, later
  cheap controller/function-split measurement, before any measurement is authorized?
- read only: this RUNBOOK, STATUS, the two Germline-03 raw inputs, and the cited runbook/status/
  bus/cSharp guides; identify only already-available skills or procedures relevant to that process.
- exclude: perform/choose a measurement, open Atlas, create `_bus/`, alter closed Germline-02,
  author canon or runtime surfaces, deploy, commit, or call any working protocol.
- return: the fixed `ORACULUM RETURN` envelope, ranked process recommendation, evidence paths,
  and the exact Majkee gate still needed.

Cartan keeps navigation and the STATUS pen. After receiving the child, verify its cited sources,
write a Cartan-owned durable navigation receipt in this bed's `raw/` (not an Oraculum-authored
artifact), update STATUS to one verified checkpoint and one next action, and return:

from-cartan to-myShell ---
packet: g03-csharp-01
evidence: <RUNBOOK / STATUS / Cartan navigation-receipt paths; observed child id or unavailable>
observed: <mounted cSharp state and verified preparation result>
uncertain: <remaining uncertainty, or none>
gate: <one Majkee decision required before a measurement or Atlas POINT>
---
```

>to-atlas
```text
TUI carrier — paste this complete envelope to Atlas:

This is Germline-03 warm staging only. It is not a measurement, an Atlas audit-body launch, or
a cross-seat POINT.

Read the saved source, not a diff:
`/home/hruzam/reposoma/.majkee/journal/2026-10-16.md`

Read exactly the shared relay guard ending `Do not create an empty bus or start the audit from
this relay alone.`, then the current packet `g03-atlas-stage-01` below. The Atlas cold-start
card is a pointer; current RUNBOOK.md and STATUS.md override its stale raw-only position.
```

```text
from-majkee to-atlas ---
packet: g03-atlas-stage-01
evidence: /home/hruzam/ia-sync/.dev/session/germline-03-foundation-audit/RUNBOOK.md;
  /home/hruzam/ia-sync/.dev/session/germline-03-foundation-audit/STATUS.md;
  /home/hruzam/reposoma/raw.guides/bus/GUIDE.md
observed: Cartan owns RUNBOOK navigation and STATUS under cSharp. The first measurement and an
  Atlas POINT remain explicitly gated; `_bus/` is deliberately absent.
uncertain: none
gate: warm staging only. Wait for Cartan's numbered `01.cartan.point.md`, whose scope, method,
  expected evidence, and stop condition must come from Majkee's later authorization.
---

Read only the three evidence paths above. Do not read Germline-03 raw inputs or candidate
subjects; do not classify, measure, choose a design, create `_bus/`, write a receipt, alter a
card, or edit project files. Return one readiness block:

from-atlas to-myShell ---
packet: g03-atlas-stage-01
evidence: <the three paths read, or an unreadable path>
observed: <whether the current Cartan/STATUS gate and future bus route are understood>
uncertain: <one actual ambiguity, or none>
gate: waiting for Cartan's 01 POINT
---

Then stop. Do not substitute a bare `LOADED` for this structured block.
```

---




### Cartan packet

>to-all: packet `g03-cartan-01`

```zsh
codex resume 01a137ec-d56a-7bc3-805b-6903606697b0
```

```bash
# TUI
/clear
$buffering `/home/hruzam/reposoma/_cold-start/card/CS.germline-03-foundation-audit.cartan-head.2026-10-15.md`
```

```text
to-cartan from-myShell ---
The next bed exists: /home/hruzam/ia-sync/.dev/session/germline-03-foundation-audit/.
Reincarnate only audit-relevant, checkable inputs from the old germline-02 / myShell journal
continuity. Start with raw/INPUTS.from-germline-02.md and
raw/SUBSTRATE.atlas.from-germline-02-close.2026-10-15.md. Treat journal entries as pointers,
not facts: verify each live claim against the current named source and STATUS/RUNBOOK once they
exist. Fold a compact source pointer and discrepancy note into the new bed; do not copy old
procedures, revive a closed STATUS, or open implementation work.
```

```text
TUI reply-only continuation:
Read /home/hruzam/reposoma/.majkee/journal/2026-10-16.md, §1.4, packet g03-cartan-01, reply
from <sender>. Reply only `LOADED g03-cartan-01 · folded: <absolute _bus/ receipt path or none>`
to `to-myShell` or `to-majkee`, then stop. Do not continue task work from this confirmation.
```

### Atlas packet

>to-all: packet `g03-atlas-01`

```zsh
claude --resume bcc59448-bfa6-4e68-99be-ab2c7f6e94ff
```

```bash
# TMUI
/clear
/buffering-cycle `/home/hruzam/reposoma/_cold-start/card/CS.myshell-atlas-continuity-reincarnation.2026-10-16.md`; retain the card in `card/` while `leave: for more readers (myShell, Atlas)` applies.
```

```text
to-atlas from-myShell ---
For germline-03, independently identify which germline-02 / myShell journal material is an
audit input versus history, parked idea, or stale pointer. Read the two new-bed inputs first,
then only cited old evidence. Return the smallest source-accounted fold recommendation to the
new bed's declared Atlas receipt path; flag any journal claim that disagrees with current files.
No canon, loader, skill, card, STATUS, or old-bed edit.
```

```text
TUI reply-only continuation:
Read /home/hruzam/reposoma/.majkee/journal/2026-10-16.md, §1.4, packet g03-atlas-01, reply
from <sender>. Reply only `LOADED g03-atlas-01 · folded: <absolute _bus/ receipt path or none>`
to `to-myShell` or `to-majkee`, then stop. Do not continue task work from this confirmation.
```

### Atlas relay test packet

>to-all: packet `relay-atlas-01` · protocol test only; no project task

```text
to-atlas from-myShell ---
Test the shared human relay only. Read the Shared human relay guard in this §1.4 and this
packet. Do not open a cold-start card, Germline-03, or any project source; do not create a
receipt or `_bus/` file.

Return exactly one sender block to myShell:

from-atlas to-myShell ---
packet: relay-atlas-01
evidence: none
observed: shared relay guard and Atlas test packet read
uncertain: <one concrete ambiguity, or none>
gate: waiting for myShell relay-test reply
---

Then stop. Do not substitute `LOADED` for this sender block: `LOADED` is reserved for the
later TUI confirmation of myShell's addressed reply.
```

```text
from-myShell to-all ---
packet: relay-atlas-01
evidence: operator-carried Atlas replies in this relay; no receipt was folded
observed: Atlas truthfully reported that the isolated packet did not include the shared guard.
Its later confirmations were bare `LOADED`, then prose closure, rather than the declared
`LOADED relay-atlas-01 · folded: none` shape.
uncertain: whether a future self-contained packet plus one-line-only instruction will retain the
confirmation shape; untested
gate: closed as behavioral relay test; protocol syntax not confirmed; no next task
---
```

### Cartan hot-opening packet

>to-all: packet `g03-cartan-hot-01` · Majkee-authorized audit-only opening

```text
TUI carrier — paste this complete envelope to Cartan:

This is a bounded Germline-03 hot-opening handoff.

Read the saved source, not a diff:
`/home/hruzam/reposoma/.majkee/journal/2026-10-16.md`

Read exactly:
1. the shared relay guard between `### Shared human relay` and `### Cartan packet`;
2. `### Cartan hot-opening packet`, packet `g03-cartan-hot-01`.

Do not act on any other packet in §1.4. Then perform only the `to-cartan` instruction in
`g03-cartan-hot-01` and return its required `from-cartan` structured block to myShell.
```

```text
to-cartan from-myShell ---
Carrier source: read /home/hruzam/reposoma/.majkee/journal/2026-10-16.md §1.4, beginning
at “Shared human relay”, before using this packet. This path and packet are the delivery;
diffs, pins, and a prior load confirmation are not task authority.

Majkee authorizes the Germline-03 hot run as audit-only. Take the Cartan head/STATUS-owner
opening named by raw/SUBSTRATE.atlas.from-germline-02-close.2026-10-15.md. First resolve the
current ia-sync instruction chain and the applicable RUNBOOK, STATUS, and bus guidance. Then
create only the minimum Germline-03 session foundations those guides require: its RUNBOOK,
STATUS, and declared first-seat/cross-seat receipt route where required. Record the precise
opening scope, the cheap-question-first edge, and the named inputs C1(a-c), composer,
classmap-as-report, F-r3-2, and F-r3-4.

Do not decide the measurements, alter closed Germline-02 material, edit Codex/Claude/Zsh
surfaces, deploy, commit, or touch the unrelated Oraculum/cSharp dirty paths. Atlas is not
launched by this packet.

Return one structured block to myShell after the foundations exist:

from-cartan to-myShell ---
packet: g03-cartan-hot-01
evidence: <absolute RUNBOOK / STATUS / receipt-route paths>
observed: <opening scope and first live edge>
uncertain: <missing guide, owner, or decision; or none>
gate: <what must occur before Atlas or the first measurement>
---
```

---

<!-- composer:end r3zz -->
outside tail