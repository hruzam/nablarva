# Component documentation and a possible Nablarva Boost

`for: Majkee / Houston architecture sitting, expanded G4 context`
`prepared by: myShell / Cartan, 2026-10-21`
`status: pre-gavel consultation; subsequent G4 acceptance recorded in closing addendum`
`authority: operator-requested group consultation; larger briefing home authorized in this sitting raw/`

## Operator question

G4's default-home question now includes what an organ/toolbox is, how its documentation
body should be shaped, and how human readers, CLI agents, a frontmatter parser, an index
and possible MCP/VIST consumers would find and use it. These are related but separable
questions. At preparation, G4 was unanswered; no a/b/c choice was inferred.

Majkee proposes a component-slug directory with a generic entry document and res/ or
subchapters. He asks for Oraculum's current first-read preferences, challenged from several
angles, and for a Laravel-Boost-like capability to be considered while shaping the docs.
Model taste is advisory. We cannot inspect training data or treat one model's preference
as proof of a standard or reader performance.

## Local method and publication sources

- [05_WAY_OF_THINKING](../../nablarva-X2-builder-narative/raw/05_WAY_OF_THINKING.md): name the conventional pattern; find what is solved; inspect open user/developer/operations edges; identify what is specifically ours. Only this fifth handoff file is currently present in that folder; the worked example's referenced earlier files are not assumed available here.
- [Project documentation record](../../../architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md): the corrected publication reference supplied by Majkee. Its K1–K8 and claims point to L16, while its default organ-body placement remains explicitly open.
- [Flag L16/L17](../../flag.md): current durable authority for documentation homes, one-home-per-fact, earned machinery and existing Termbrana boundaries.
- [Houston map](../../../../.germline/agents/houston/nablarva.md): current documentation roles and proposed body-location fallback.

A second file exists under the record's process/ subfolder. Its header says DRAFT,
un-gaveled, contrast-signature pending. The root record says final and supersedes the
earlier same-day draft; flag L16 pins the root triad at nablarva@2ae8636. The root record
is therefore the relevant publication input. This distinction was checked against both
headers and the flag, rather than resolved by combining their text.

## Finding and proposed direction

`inferred: myShell` — Yes, keep a possible Nablarva Boost consumer in mind while writing
documentation. Prepare clear source boundaries and selective entry points now. A future
consumer should read the same owned facts that a human reads, with their provenance.

Majkee's component folder is a reasonable candidate. A folder containing just README.md
can remain thin. Adding empty res/ trees, compulsory metadata or generated indexes is a
separate decision. The current record does favor line → subchapter → folder growth, so
adopting folder-first as the general default would be an explicit refinement for the
sitting to consider, rather than something already settled by L16.

The important distinctions are:

| decision | what it controls | consequence if coupled prematurely |
|---|---|---|
| organ/toolbox classification | relationship to the animal and independent usefulness | reclassification forces avoidable moves |
| code home | implementation and ownership | a documentation choice accidentally becomes a topology change |
| documentation home | authoritative explanatory body | duplicate bodies compete for truth |
| entry and chapters | navigation and reading size | scaffolding obscures the first useful page |
| machine metadata | answers required by a named consumer | a second schema needs maintenance without a user |
| publication/MCP/VIST view | presentation or runtime observation | rendered or observed data gains unintended authority |

These choices can be designed together without making one filesystem name answer all six.

## 1. Conventional names and established mechanisms

The ordinary patterns are component documentation, documentation-as-code, a documentation
catalog, selective context loading, and an optional resource adapter. A catalog answers
which documents exist and where. A search index answers relevance queries and introduces
collection, update and ranking concerns. Neither follows automatically from frontmatter.

Laravel Boost is a useful analogy because it distinguishes upfront guidelines, on-demand
skills, application-inspection tools and package-aware documentation search. Its custom
guidelines accept Markdown or Blade; its skills have their own frontmatter contract.
Project rules use frontmatter globs and an index because an actual agent-loading contract
consumes them. The PHP/Composer discovery, generated agent files and hosted documentation
search are specific implementations, not a directory convention to import wholesale.
[Official Boost documentation](https://laravel.com/framework/docs/boost)

`inferred: myShell` — The portable idea is a small entry leading to relevant bodies and
inspection of actual local state. Nablarva's authority and promotion rules still govern
any future writer. An analogy to Boost's rule-recording tool does not grant an agent a
new canon pen.

MCP resources require a server that advertises resources and implements listing and
reading URI-addressable content. Templates can describe parameterized resource URIs.
The host decides how users select or incorporate that context. Thus a Markdown header
could feed an adapter, but does not make the file discoverable through MCP by itself.
[MCP resources, versioned specification](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)

Tools expose model-invocable operations; prompts expose user-selected message templates.
Neither should be treated as interchangeable with a document resource.
[MCP tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools),
[MCP prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts)

These sources establish mechanisms. They do not establish that Nablarva needs an MCP
server, semantic retrieval, or a particular component taxonomy. The cited MCP revision
is an explicit reference, not a claim to have qualified a future Nablarva protocol version.

## 2. Local constraints and layout alternatives

`locked: L16.9–12` — Documentation roles, one home per fact, thin growth, honest staleness,
claim provenance and head-owned promotion apply. The universal docs/organs fallback is
still explicitly proposed in the record's Open section and Houston's map.

`said: current component sources` — Termbrana already has a README/DECISIONS family at
[toolbox/termbrana](../../../../toolbox/termbrana/README.md); L17 also establishes the
composition source family under ~/ia-sync/zsh/termbrana/. A uniform documentation proposal
must preserve those source and ownership distinctions. The
[stridularium page](../../../../docs/organs/stridularium.md) calls itself a working draft,
describes an organ, and distinguishes a standalone console core from a room-dependent
layer. It demonstrates why classification needs attention per layer; its wording alone
cannot settle the taxonomy for every component.

| candidate | immediate benefit | cost or decision required |
|---|---|---|
| one small component page | cheapest body; follows printed growth proposal | later move when chapters become useful |
| component folder with README.md only | predictable entry; room for actual chapters later | explicit folder-first policy refinement; root and naming still open |
| existing source-local README | reader starts close to implementation | wrapper must identify which source family/body applies |

Illustration of Majkee's candidate, with no root selected:

```text
<component-slug>/
  README.md             purpose, scope, contract pointers, key files
  res/                  only when distinct chapters/resources exist
    <topic>.md
```

README.md is my preferred generic entry for this candidate because it expresses the
entry role plainly. A chapter should hold distinct detail; the entry points to it.
No extra AGENTS.md, local harness or parallel project contract is implied. Existing homes
should not migrate solely to make a drawing symmetrical.

## 3. Separate contracts for the readers

| reader | useful preparation | unresolved contract |
|---|---|---|
| human | short purpose/scope, working links, useful key files | whether the proposed entry actually reduces confusion |
| CLI agent | canonical body pointer, narrow sections and targeted search | which question warrants loading which chapter |
| parser | explicit source boundary and distinguishable fields if needed | exact query, field meanings, errors and schema evolution |
| publication | render owned source with links and source revision | renderer, inclusion rules, build owner and stale output handling |
| MCP client | explicit resource mapping to those sources | server owner, URI policy, access scope, refresh semantics |
| VIST | distinguish declared design from observed runtime state | bindings, observation provenance and freshness |

`inferred: myShell` — VIST can show an observation alongside a component document. Seeing
a process or window does not establish the component's completed design, identity or
delivery authority. A documentation reader is also distinct from Composer's qualified
Phase-0 packet parser; its acceptance does not qualify a new source loader.

For metadata, start with a consumer question. For example, a reader asking "what applies
here?" may need scope and a canonical pointer; a publication view asking "what version?"
may derive revision from Git. Do not copy locks from flag or doing-state from STATUS into
a new header. Keep manually declared meaning separate from derived build provenance.

A proposed metadata field earns its place by naming its consumer, owning source,
validation and missing/stale behavior. This is a design test, not an approved schema.
Mandatory IDs are premature unless a concrete consumer needs identity across renames;
existing source pointers can serve current navigation. A future published URI contract
would make that question consequential and should address it explicitly then.

## 4. Consultation and challenge

- Local source reader: GPT-5.6-Terra/high, reused g1_context_terra. Distinguished final
  record from draft and settled documentation law from proposed directory fallback.
- External mechanisms reader: researcher, GPT-5.6-Terra/high, reused keys_host_research.
  Checked official Boost/MCP sources; distinguished selective loading, catalog and search.
- Independent challenger: g4_docs_challenger, GPT-5.6-Sol/xhigh. Verdict REVISE: do not
  make physical taxonomy permanent identity for docs, publication and MCP. Its suggestion
  of new stable IDs was itself challenged as unearned without a consumer.
- Oraculum: GPT-6-Astra/high, reused oraculum_keys. Independent design synthesis is
  recorded below. This child is a consultation seat, not the Claude session head or
  STATUS owner.

The parent checked load-bearing claims against source headers, flag L16, Houston's map,
the current component examples and official web pages. No navigation experiment was run;
first-read preferences remain heuristics rather than measured results.

### Oraculum's independent return

`inferred: oraculum · GPT-6-Astra/high, consultation, 2026-10-21`

First follow the canonical body pointer from PROJECT.yaml or PROJECT-DESIGN. If handed
only a directory, look for README.md and follow the links relevant to the task. This is
a navigation heuristic, not a claim about training data. The entry should quickly explain
purpose, boundary, what exists versus what is proposed, contract/key-file locations and
change authority; it should not require reading every chapter first.

Ranked recommendation: preserve established homes and explicit body pointers; permit a
deliberately chosen README-only folder convention for new bodies; earn machine metadata
and adapters through named consumers. Houston should reconcile folder-first explicitly
with the recorded growth law. The strongest caveat is authority resolution: a fast reader
that reaches the wrong draft has failed, however tidy the hierarchy or stable its IDs.

Oraculum also challenged an immediate neutral-ID registry: a need for identity across
renames must be established before taking on assignment, uniqueness and retirement duties.
Its proposed comparison includes the existing Termbrana entry, stridularium page and a
README-only sketch, recording wrong-source selections and missing information as well as
navigation effort. No comparison was dispatched or run.

## 5. Open edges through the X2 method

For users: finding the first useful page, learning which context matters, and telling
design intent from live state. For developers: field ownership, source selection,
renames, duplicate truth and parser errors. For operations: publication revision,
staleness, access boundaries and adapter lifecycle. These are predicted local risks;
this bounded consultation has not collected a practitioner-complaint corpus demonstrating
their prevalence. That part of X2 question 3 remains unresearched.

What is specifically ours is how these readers fit Nablarva's component roles, current
tmux/PTY direction, promotion boundaries and independent clients. Neither vendor docs
nor model taste can choose that policy for Majkee.

A small candidate probe is to give fresh readers the same intent-only questions against
the current page shape and a manually sketched folder entry. Measure correct source,
time to first relevant file, mistaken authority and stale pointers. This is a proposed
comparison, not dispatched work or an acceptance result. A folder preference itself
need not wait for a retrieval-framework benchmark; the test would check its benefit.

The record's tier-1 threshold is at least two stale-pointer findings in one audit before
a checker/regenerator is earned. Its vector tier requires measured retrieval failure
in a large unstructured corpus. Those are recorded upgrade conditions, not evidence
that either tier has been earned here.

## G4 handoff and decision consequences

`inferred: myShell` — Bring this smaller design proposition to the sitting: each component
has one explicitly pointed-to documentation body; existing homes remain; for new homes,
consider README.md in a component folder, adding chapters/resources on need. Keep
organ/toolbox terminology under architectural review and prepare sources for selective
reading, without choosing a metadata schema or adapter yet.

This would be an amended direction, not a silent selection of printed G4 a. The gavel
must still say whether that fallback is locked now, proposed for final GO, or left open,
and which root it uses. It can also leave taxonomy open while settling entry shape.

Locking a layout would constrain later documentation placement and migrations. Locking
a schema or public resource identity would additionally constrain parsers and consumers.
Keeping these decisions separate preserves a smaller next choice without deferring the
user's folder idea indefinitely. No choice here closes source coverage, shared-interface
ownership, Sublime feasibility or runtime-history design.

At the close of this consultation, G4's report was empty and the approved sink remained
UNANSWERED. G1–G3 retained their recorded answers. No source directory, code home, AGENTS
routing, frontmatter schema, MCP service or VIST format was selected or modified by the
consultation itself.

## Subsequent operator disposition — G4

`said: Majkee, 2026-10-21` — “Taking your team RESULT as GAVELED” followed by a request
for Astrobley's consultation and a floating Nablarva Boost documentation-reader concept.
The full message is preserved verbatim as own in G4 report 4; the approved sitting sink
points to it. Branch: RESHAPED. This is the recorded operator ruling; a flag entry by the
named head has not been observed here.

`inferred: myShell` — The accepted direction preserves existing homes and the thin
README-entry/folder approach, while taxonomy remains for architectural review and machine
metadata/adapters await their actual design. This did not specify a new parent directory
for every component. The preceding open alternatives and unanswered statements describe
the research's earlier state, not a request to gavel the same direction again.

Majkee correctly identified that README plus res/ leaves discovery/navigation undefined.
The follow-up [Nablarva Boost reader concept](brief.nablarva-boost-reader-concept.2026-10-21.md)
provides a separate, explicitly open design home for discover/read/search, same-source
file and programmatic readers, and possible MCP/VIST presentation. That subsequent
concept is future design, not an inferred implementation approval.
