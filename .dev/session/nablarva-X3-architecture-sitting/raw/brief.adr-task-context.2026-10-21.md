# ADRs in task context — G5 triad consultation

`for: Majkee / Houston sitting; pre-session source preparation design`
`prepared by: myShell / Cartan with Oraculum, reader/researcher and Astrobley, 2026-10-21`
`status: G5 own; team/controller direction and reading schedule gaveled; no reader schema installed`

## What the operator is asking

Majkee asks why ADRs are useful, who naturally reads them, how they enter work across
different agents/project scopes, how to prevent orphan records and context overload,
and whether task-bound Termbrana preparation can selectively source them through the
intended deterministic reader, optional MCP or VIST. This is design input before the
sitting/build, not a request to instantiate those mechanisms here.

The [Nablarva Boost reader concept](brief.nablarva-boost-reader-concept.2026-10-21.md)
already gives the hardcoded source engine a role. This brief supplies the missing
decision-context use case for that engine.

## Why an ADR exists, and what is already here

An architectural decision record preserves the reasoning that a bare choice loses:
the problem, constraints, alternatives, decision, consequences and conditions that could
make revisiting it sensible. A later collaborator can judge whether the original reasons
still apply. Nygard's original practice uses short records for significant decisions,
retains status and links replacements rather than erasing earlier reasoning.
[Original ADR explanation](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

AWS describes overview reading through decision headlines followed by the relevant
record, and using ADRs in implementation, design and review. It assigns ownership during
proposal/review and a replacement lifecycle for changed accepted decisions.
[AWS ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

Microsoft recommends concise records with rationale, alternatives, consequences and
linked supersession; detailed design can remain separately linked material.
[Microsoft ADR guidance](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)

These are human documentation practices. They do not establish an automated relevance
algorithm, a particular YAML schema, a universal directory or a guarantee that keyword
search finds every governing decision.

`observed: local sources` — Termbrana already has ADRs in
[its component ledger](../../../../toolbox/termbrana/DECISIONS.md). Its
[README](../../../../toolbox/termbrana/README.md) points to that ledger and specific
decisions. G5 therefore does not choose between recording reasons and having none.
It concerns the additional root series and its relationship to existing homes.

`locked: L16/L17` — Flag retains locks; component bodies hold local detail; surviving
deltas are promoted by the head, with Majkee holding canon authority. An ADR can own
authorized technical details and reasoning. Its authority follows the cited acceptance
and scope; rationale alone neither creates an exception nor becomes a second lock ledger.

## Natural readers: bind context to the task

`inferred: triad synthesis` — Bind the selection to the assignment's affected component,
interface, work phase and intended change. A permanent agent identity is insufficient:
the same implementer can perform a routine edit today and propose a boundary change
tomorrow. A neighboring project's agent needs the shared interface decisions, not the
whole originating project's archive.

| task/reader | usual starting context | when to open more rationale |
|---|---|---|
| implement within a settled interface | current contract, applicable constraints and prerequisites | the change tests an assumption or alters the boundary |
| verify a scoped result | acceptance scope, relevant evidence and decision obligations | a test or finding conflicts with the adopted rationale |
| architect/challenger proposing a change | relevant alternatives, forces, dependencies and consequences | follow the affected replacement/history chain |
| neighboring component/integration owner | shared guarantees, limits and dependency decisions | the interface changes or responsibility becomes ambiguous |
| operator considering a gavel | proposed choice, consequences, unresolved assumptions and authority | examine evidence or disputed alternatives |

This describes reading depth, not new permission tiers. Applicable project instructions
and constraints remain required independently of optional ADR discovery.

## How reasons enter the process without becoming orphans

Proposed lifecycle using existing owner surfaces first:

1. **During design:** capture significant choices and their alternatives while the context
   is available. Keep proposals distinct from accepted decisions; ordinary implementation
   steps do not each require an ADR.
2. **At acceptance/promotion:** preserve the authorizing source and scope. The head puts
   surviving rationale in its owned durable home and links it from the affected contract
   or component entry. The component's responsible maintainer carries that navigation;
   Houston can check coherence but does not acquire the promotion pen.
3. **At task preparation:** the assignment points to its component/interface. Follow the
   declared decision relationships and current replacements before assembling context.
4. **During implementation/review:** a conflict cites the particular record and affected
   constraint. Work that crosses the selected scope returns that gap to the assignment
   owner instead of assuming no other decisions exist.
5. **At replacement/closure:** preserve the old reasoning, identify what changed, repair
   current pointers and preserve evidence before a session bed is pruned.

An absent owned incoming link is an orphan candidate. A resolvable link alone does not
prove that people or agents actually encounter the record; the preparation/review hooks
and reader task probes test that. Begin with ordinary linking and closure practice.
A generated catalogue or automated check remains a separate mechanism to qualify.

## Proposed task-bound sourcing

The intended reader can resolve declared context automatically within the operator's
selected scope/recipe. That is different from guessing relevance from filenames or
loading every ADR. A useful preparation sequence is:

```text
assignment: component + affected interface + phase + intended change
  -> owning contract and applicable decision references
  -> declared corrections/replacements and required dependencies
  -> required constraints + selected reasons + optional history pointers
  -> acquired original sections and source receipts
  -> Termbrana preparation/composition
```

Frontmatter or a source descriptor can make those relationships machine-readable.
Candidate meanings are applies-to scope, work phase, decision reference, required
context, rationale reference and supersession. They are not approved field names.
A descriptor can address a ledger section or a separate ADR file through adapters.
Maintain relevance links once at their owning source; avoid parallel handwritten lists
in a README, header and reader registry.

The task owner supplies the initial scope and required references. The reader resolves
declared relationships deterministically; it does not determine all architectural impact
from prose. A reviewer can suggest additional context, and the agent can request deeper
sources when the intended change crosses that boundary. Metadata narrows acquisition;
its presence is not proof that the selection is complete.

The acquired parts should remain distinct and have receipts stating task/recipe,
selection reasons, source locations and pins, unresolved relationships and omitted
optional material. A required prerequisite that exceeds the budget must remain visible
as an unresolved loading requirement. Do not silently shorten it to fit. An authored
short decision statement can support quick orientation; a generated summary must not
silently replace the original governing source.

Light key commands, an IDE manager UI and a future MCP adapter can use the same selection
results. MCP provides access, not architectural relevance. VIST can supply separately
attributed observations that motivate review; observed activity cannot prove an ADR was
read, understood or superseded. The source engine acquires context; Termbrana composes;
activation and delivery retain their separate existing boundaries.

## Actual case: why latest-record selection fails

The Termbrana ledger explicitly says ADR-0001's decision survives while some open items
are superseded by ADR-0002. ADR-0002 also declares the re-verification loop before M2
adapter code. Those are textual relationships we inspected, not fresh runtime tests or
a claim that a historical prerequisite is still outstanding today.

For a task proposing lower observer-capture CPU:

- The head checks current owner-state, applicable observer contract and relevant ADR
  sections, including corrections and any currently applicable qualification prerequisite.
- An implementer receives the current target-pane/own-pane/debounce constraints and
  relevant scope; the architect examines the original capture rationale alongside the
  later correction about event behavior.
- A verifier receives the relevant evidence obligations and open performance questions.
- An unrelated composition-parser task does not receive the whole observer ledger merely
  because the component name Termbrana appears in both source families.

Partial supersession requires an explicit section/claim relationship or a human-selected
recipe until an adapter can qualify it. Neither newest timestamp nor whole-record
replacement is a safe inference. Pins establish acquired bytes, not present applicability.

## Storage and G5 consequences

The triad favors component ledger plus flag as the present arrangement, with deliberate
rationale ownership and task-selection links. Small addressable ledger entries can work;
separate files help when independent decisions become hard to reference or maintain.
A genuine cross-component decision may earn a shared rationale home. A root ADR-0000
that merely announces adoption would not by itself solve discovery or selective reading.

There is a separate verified wording issue: the
[root ADR stub](../../../../docs/decisions/README.md) promises that gaveled items land
there, while L16 retains flag's lock authority and the later documentation record limits
ADRs to product-technical decisions. Leaving the stub untouched leaves that promotion
promise ambiguous. Retirement or a bounded correction is a separate operator decision.

Thus printed G5 a can retain the existing homes, but does not alone adopt this reader
process or correct the stub. An own/amended answer could select the existing-home direction,
carry task-bound rationale sourcing into the architecture draft, and name the desired
stub correction or retirement for the reviewed change. This is a proposal for Majkee,
not a gavel inferred from the consultation. Printed b opens the root series; printed c
retires the stub. Neither storage action automatically supplies the reader process.

## Qualification and handoff

### Where the reader procedure survives

`inferred: myShell, operator clarification, 2026-10-21` — A controller/function is a
suitable candidate home for the reusable agent-facing task-preparation procedure.
The current state is a linked design brief in this temporary bed and GLOSS, with a
pointer in the sitting prompt. No durable program function has been authored, promoted
or installed by this consultation. Survival as an operational procedure is therefore
still a promotion obligation, not an observed result.

Keep the responsibilities distinct, with pointers between them:

- **Reusable procedure:** a function under the eventual context-sourcing program,
  indexed by its CONTROLLER. It accepts assignment/scope/work mode, resolves the declared
  sources and dependencies, handles insufficient context and returns acquired parts
  with receipts. This describes a candidate responsibility, not a settled program name,
  filename, global germline layout or format profile.
- **Reader contract and implementation:** the application-owned source engine defines
  deterministic parsing, binding, selection and pinning behavior. A prose function
  can instruct an agent using that engine; software does not automatically execute
  arbitrary procedural Markdown. Both refer to the owned contract rather than inventing
  independent resolution rules.
- **Project facts:** ADRs, authority and applicability links remain in the respective
  project/component homes. The reusable program does not copy their contents into itself.

A GUIDE can explain the general pattern; the selected function is the operational read
path. Termbrana/IDE/MCP clients can invoke the qualified engine without each reproducing
the procedure or source-selection semantics.

Before this bed is pruned, its head must route accepted process material to the appropriate
germline authoring/promotion path and application contract material to its durable body,
then replace temporary references with actual destinations or commit-pinned evidence.
Existing germline/source-contract gates apply. This is not a reason to create the program
inside the personal journal-continuity trial or bypass the unresolved owner/home/API.
This was an outstanding proposed amendment at consultation time. The subsequent operator
acceptance and requested reading schedule are recorded below.

Proposed reader cases: an observer implementation receives the relevant prerequisite;
a composition task avoids unrelated observer history; partial supersession retains the
still-valid decision; broken evidence links and ambiguous selectors remain visible;
dirty-worktree pins are honest; required context is not silently dropped for budget.
Check whether recipients can identify both the binding constraint and its relevant reason.
No such experiment was run here. Full source coverage and existing source-contract gates
remain with the application team and its owning architect/head.

Triad: Astrobley (GPT-6.1-Sol/high) supplied lifecycle and reader mechanics; Oraculum
(GPT-6-Astra/high) separated rationale, authority and task impact; reader/researcher
(GPT-5.6-Terra/high) checked primary ADR practice. myShell read the local ledger, its
entry pointers, the stub and relevant locks, and checked the three primary sources.
No source documents, schemas, code, RUNBOOK, STATUS or flag changed in this consultation.

At consultation close G5 remained unanswered. The subsequent ruling follows; this brief
is not itself an ADR or a substitute for the operator's verbatim report.

## Subsequent operator disposition and reading schedule

`said: Majkee, 2026-10-21` — “ok, your team observaytion + controller possible solution
for selected agent in process chain.” He then requested a fixed who-reads-what process
and asked whether reading happens before the session or at RUNBOOK entry. His complete
message is preserved verbatim as own in G5 report 5; the sitting sink points there.
Branch: RESHAPED.

`inferred: myShell` — Accept the team/controller direction for task-bound context and
carry its survival requirement into the sitting. Existing component ADRs and flag remain
the current homes. The ruling did not select deletion versus correction of the root
stub, create a root ADR series, specify a global program location or qualify a source
schema. Those details must remain visible in the architecture draft rather than being
inferred from an a/b/c label.

`inferred: Astrobley / myShell, follow-up schedule` — Preparation begins before RUNBOOK
authorship. Recipient reading happens again at entry. A planner cannot ground the work
using context first assembled after the plan is already written.

| when | responsible participant | required context and responsibility | resulting handoff |
|---|---|---|---|
| before planning / RUNBOOK authorship | planner or session head | applicable instruction chain and project read order; current locks, router and owning state; machine contract; project direction, affected architecture/interfaces, relevant decisions/prerequisites and applicable process method | grounded scope, gate, responsibilities and explicit unknowns |
| before RUNBOOK release | planner or head | check fit with project direction, source ownership, shared interfaces and required conditional checks | stable assignments/constraints and source pointers; current position remains in STATUS |
| before each assignment is dispatched | controller/context preparer | selected task scope, work phase, source recipe, required references, corrections, pins and budget | acquired parts and receipt; gaps/omissions explicit |
| at worker entry, before changes | builder | own applicable instructions; exact assignment, shared RUNBOOK rules and its numbered prompt, current owning STATUS; relevant mechanism/process architecture, component contract, code entry points and selected decisions | implementation understanding; mismatches returned before the affected action |
| at independent verification entry | verifier | exact assignment and acceptance; governing constraints and relevant decision obligations; actual changed artifacts and evidence | findings from independent inspection, not a restatement of the builder's report |
| when architectural attention is required | Houston | bounded question/card, relevant whole-project direction, affected interfaces/contracts, decisions and evidence | grounding finding; head retains lifecycle/integration and Majkee retains canon |
| on resume or a material change | receiving participant and head | recheck current owner-state and affected source identities; refresh changed scope, interface, authority, bytes or prerequisites | updated selection/receipt, or a precise unresolved requirement |

The builder needs both the mechanism it changes and the process boundaries around it.
For a source-engine task this includes acquisition versus composition/delivery, pin
meaning and failure behavior. The planner needs those boundaries too, plus the wider
project alignment needed to choose the scope and gate. These are different emphases,
not exclusive reading categories.

The common baseline is assignment/ownership, applicable instructions, relevant project
direction, constraints/prerequisites, session gate/current owner-state and conflict route.
For Nablarva the existing any-seat read order still applies: AGENTS → flag → pulse →
PROJECT.yaml → task-needed sources. A selected context profile does not waive that chain.

Read RUNBOOK at entry; it holds stable intent and assignments. Recheck STATUS for current
position, new holds and resume. Keep unchanged pinned source parts during ordinary work;
do not reload the whole corpus each turn. Refresh the affected selection on reassignment,
scope/interface change, changed governing source, newly discovered constraint or conflict.
A pin proves read bytes; it does not prove continued applicability.

The controller prepares and checks a package; the recipient checks that the package fits
the actual task/frame and contains governing sources. It cannot delegate away its own
instruction responsibilities or treat package existence as proof of understanding.
Missing, ambiguous, contradictory or oversized required context holds the affected action;
independent scoped inspection can continue. An unverified summary does not substitute
for a missing prerequisite.

This schedule is concrete design input for the architecture sitting and eventual
controller/function qualification. It does not rewrite global role definitions,
RUNBOOK/STATUS doctrine or the existing source-contract gates. Astrobley returned this
matrix read-only; myShell checked its source timing against the RUNBOOK GUIDE's entry,
numbered-prompt and stable-versus-current-state rules. No controller was installed.

### Explicit confirmation of the reading schedule

`said: Majkee, follow-up after presentation of the matrix` — “gaveled.” then “continue.”
These words are appended verbatim to G5 report 5. The preparation-before-RUNBOOK,
recipient-at-entry and affected-context refresh schedule is now the operator's ruling
for the sitting, rather than merely a request for a schedule. The preceding consultation
provenance remains historical. The head carries the accepted procedure and its promotion
obligation through the architecture/germline authoring path; schema, program home/API and
implementation qualification remain to be settled. No flag, RUNBOOK or STATUS was edited.
