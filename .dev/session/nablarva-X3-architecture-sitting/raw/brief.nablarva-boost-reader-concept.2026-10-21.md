# Nablarva Boost — floating documentation-reader concept

`working name: Nablarva Boost`
`prepared by: myShell / Cartan, with Astrobley and primary-source research, 2026-10-21`
`state: open design / nice to have; no implementation or schema approved`
`scope: documentation discovery, navigation and pinned sourcing for humans, agents and an intended deterministic engine`

## Why this has its own space

Majkee accepted the preceding team's direction as GAVELED, then identified a real gap:
README.md plus res/ describes a possible documentation body but does not explain how a
reader discovers, navigates or searches it. He explicitly requested this floating design
space and Astrobley's developer consultation. His verbatim ruling is in
[G4 report 4](gavels.X4.2026-10-17.md#step-4--g4--organ-body-home-lock-docsorgansorganmd).
The [preceding brief](brief.component-docs-and-nablarva-boost.2026-10-21.md) supplies context.

This concept gives the future reader a concrete shape to discuss. Its filenames,
operations, parsing convention and MCP mapping remain proposals. The G4 ruling does not
select a previously unspecified parent directory or turn this subsequent design into a
finished contract.

**Current design direction after Majkee's clarification:** the third reader is an intended
hardcoded source engine operated through his keys, serving Termbrana and IDE clients.
It needs declared navigation and source pins. Frontmatter therefore has a concrete design
consumer now. The typed-source proposal below extends the earlier Markdown-navigation
candidate; it is not postponed merely because the engine is not built yet.

## README: our choice and the Boost analogy

README.md is a conventional entry filename; the proposed component README plus optional
res/ layout is our adaptation for Nablarva. It was not established as a Laravel Boost
reader contract. A repository having a root README would not establish such a contract.

The transferable Boost idea is to make relevant project knowledge available through
deliberate loading and retrieval mechanisms. A directory name alone supplies none of
that behavior. The mechanism evidence is recorded below, separately from our design.

## Laravel Boost mechanism: primary-source trace

Read-only research against Boost main commit
[30e24b7c242049e31bd267cd64b57301fc66b2f4](https://github.com/laravel/boost/tree/30e24b7c242049e31bd267cd64b57301fc66b2f4),
dated 2026-10-17, inspected 2026-10-21. These are static source findings, not a local
installation test or a qualification of the hosted search implementation.

1. **Repository entry.** Boost's
   [root README](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/README.md)
   introduces the package and points to Laravel's website. The traced installation,
   rule and resource mechanisms below use their own explicit sources; they do not
   establish README plus res/ as a discoverable documentation format.
2. **Agent guidance.** The
   [Codex adapter](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Install/Agents/Codex.php)
   defaults guidance to AGENTS.md. The
   [Claude adapter](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Install/Agents/ClaudeCode.php)
   chooses CLAUDE.md when present, otherwise AGENTS.md. The
   [writer](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Install/GuidelineWriter.php)
   inserts or replaces a delimited laravel-boost-guidelines block, preserving surrounding
   text. These are Boost's adapters, not a proposal to create component-local harnesses here.
3. **Navigation and local lookup.** Boost's
   [guidance template](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/.ai/boost/core.blade.php)
   directs the agent to a rule index, matching rule bodies and keyword search. The
   [rule frontmatter parser](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Rules/RuleFrontmatter.php)
   extracts paths; the
   [repository](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Rules/RuleRepository.php)
   generates .ai/rules/index.md from those declarations. Thus programmatic index
   generation and agent-driven navigation/search coexist. The index is not an autonomous
   semantic reader of every document.
4. **Skills.** The
   [skill composer](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Install/SkillComposer.php)
   discovers designated SKILL.md or SKILL.blade.php entries and requires name/description
   frontmatter. That is another specific discovery contract, not a generic requirement
   for all documentation pages.
5. **Documentation search.** The
   [SearchDocs tool](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Mcp/Tools/SearchDocs.php)
   gathers installed PHP/JS packages and major versions, then posts queries and package
   data to a configurable hosted /api/docs endpoint, requesting Markdown. It does not
   search the project's local README tree. Its client code alone does not reveal or
   qualify the hosted service's ranking/index internals.
6. **Runtime context.** The
   [server](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Mcp/Boost.php)
   registers SearchDocs as a tool and
   [ApplicationInfo](https://github.com/laravel/boost/blob/30e24b7c242049e31bd267cd64b57301fc66b2f4/src/Mcp/Resources/ApplicationInfo.php)
   as a resource. ApplicationInfo's file-like URI ends in .md, yet its handler returns
   runtime application/package data as JSON. The URI does not imply automatic Markdown
   filesystem discovery. The official guide's tool table calls Application Info a tool;
   the inspected implementation distinguishes it as a resource.
   [Official Boost guide](https://laravel.com/framework/docs/boost#mcp-server)

`inferred: myShell` — This is the useful precedent for our open concept: one source can
support both a human/agent-readable navigation projection and a programmatic producer,
while documentation search and runtime inspection remain distinct operations. It does
not settle our discovery syntax, corpus or metadata contract.

## Astrobley's proposed reader

`inferred: astrobley · senior developer consultation, 2026-10-21`

Use one owned Markdown documentation corpus through two reading paths: direct file
reading and a read-only programmatic provider. They share sources, navigation meaning
and source authority. They need not implement the same reading algorithm: an agent
interprets prose; a helper deterministically resolves declared entries, sections and
search results.

| operation | file-reading agent or human | helper behavior proposed |
|---|---|---|
| discover | open project entry and its component pointers | enumerate explicitly declared bodies and chapters |
| read | follow a topic link, read the needed section | return that original section with path and source revision |
| search | search terms within the relevant component | bounded lexical search of the declared component corpus |
| widen | deliberately consult project-wide or historical sources | explicit wider scope, labelled separately |

These are logical operations, not approved CLI verbs or MCP tool names.

Example: “What permits Termbrana to send input?” First reach its declared documentation
entry; follow the delivery-boundary topic to the owning contract and lock. A search hit
containing “send” is a candidate to inspect, not sending authority. Existing Termbrana
source families remain distinct even if one topic list routes readers to both.

## Where navigation could live

Astrobley's first consultation candidate was a designated Documentation navigation section in the
entry, using normal Markdown links. Human readers follow it naturally; a helper parses
only that section's declared navigation edges. Citations, bibliography links and arbitrary
prose links do not silently expand the searchable corpus.

The subsequent hardcoded-reader clarification makes typed source declarations another,
more direct candidate. A prose navigation section can remain a human view; the two must
not become separately maintained authorities for the same bindings.

Illustrative entry content, not required headings or a schema:

```text
README.md
  Purpose and boundary
  Existing capability and open design
  Documentation navigation
    composition grammar -> owning source
    delivery boundary -> owning source
    current work -> session router (reference, outside enduring-doc search)
  Key implementation files
  Sources governing changes
```

The contract would still need to distinguish navigable documentation, authority references,
source-code pointers and live-work references. The illustration does not claim ordinary
Markdown links encode those types already. A helper must have a precise rule for the
designated section, link roles, path resolution and traversal limits before it can work.

The alternative is a small structured catalogue that owns those navigation pointers and
generates the human list. Choose it if parsing the navigation section becomes awkward.
Maintain one source for navigation instead of two independent handwritten inventories.
The document bodies remain ordinary Markdown in either approach.

My proposed order is explicit navigation with direct reads and bounded search first;
consider a separate catalogue when actual consumers require it. A prebuilt search index,
ranking service or semantic retrieval is independently optional. This open concept does
not require one to make future MCP access possible.

## What needs a contract before implementation

The corpus needs an owner and explicit inclusion boundary. A scan can verify declared
sources or discover candidates within an authorized area; scanning every Markdown file
must not silently make drafts, sessions or unrelated directories part of the default
corpus. Traversal and search must obey the same boundary, including resolved symlinks.

Frontmatter can supply maintained role, scope and navigation inputs to the intended
source engine; a candidate follows below. Legacy formats can retain their own adapters.
A parser can validate a field or
reference; it cannot prove that a paragraph correctly expresses architectural intent.
Document-level acceptance must not certify all historical quotations and proposals inside.
Git revision, worktree state and content digests should be derived when reading.

Proposed behavior worth preserving in a later specification:

- Missing target: report the unresolved pointer and originating entry.
- Conflicting body declarations: return ambiguity; do not choose the newest filename.
- Older checked date: display it; age alone does not prove incorrect content.
- Draft/history search: include it only through the selected scope and label results.
- Dirty worktree: identify edited source instead of claiming it is the committed revision.
- Search hit: retain source location and read the original before making a claim.

These are candidate requirements, not evidence of implemented behavior.

## Third consumer: deterministic sourcing under operator keys

`said: Majkee, clarification after the G4 gavel, 2026-10-21` — the missing consumer is a
“hardcoded reader which need navigation and pins passed from mechanism”. His two
Termbrana use contexts are “tested houston in run | fresh data collection from intendet
area”. These are operator-described intended uses, not new verification findings about
shipped source loading.

`inferred: astrobley, second consultation` — Give that engine a typed source-descriptor
proposal now. Humans and agents read the entry and its body; the engine resolves declared
members and acquires selected bytes. It does not need to understand arbitrary prose to
navigate. One common entry-plus-members pattern can accommodate different source formats
without pretending their schemas are identical.

The local examples already provide useful material:

- The [RUNBOOK GUIDE](/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md) has YAML title,
  scope, audience, machine and verified fields, plus a Manifest distinguishing chapters,
  assets and raw material excluded from its resolver.
- The [guide-writing contract](/home/hruzam/reposoma/raw.guides/guide-writing/GUIDE.md)
  defines a fixed GUIDE.md entry with res/ chapters and separately typed side directories.
- The personal [journal controller](/home/hruzam/reposoma/.majkee/.germline/programs/journal-continuity/CONTROLLER.md)
  has program/revision/stamp/scope and a sole Functions table binding a function to its
  file and expected stamp. The selected
  [function specimen](/home/hruzam/reposoma/.majkee/.germline/programs/journal-continuity/fn/list-pending.md)
  declares the matching program/function/stamp. This personal trial is an observed
  specimen, not a settled global germline schema or an implemented source engine.

### Candidate frontmatter, not an installed format

```yaml
---
source_schema: nablarva-source/v0-proposal
id: example/composition
kind: guide
entries:
  sourcing:
    kind: chapter
    path: res/sourcing.md
---
```

This is a source-document header illustration, not an extension to Composer's current
request/0.1 packet headers. Field names and requiredness remain open. A local identity
may come from an existing source registration; the example does not require a new global
ID registry. The minimum semantic distinctions are source kind, selected member, its
binding, selection boundary and any required binding token. Navigation members, authority
citations, source-code pointers and live-state references need distinguishable roles.

Authors declare meaningful relationships; operator source profiles declare roots,
supported readers and loading recipes/budgets. The engine derives resolved paths,
reader version, acquisition time, actual Git revision where applicable, worktree state
and content digests. Derived pins belong in an acquisition receipt, not handwritten into
every header. A controller's expected stamp is a binding token, not a content digest;
verified dates and declared revisions are also different from a captured-byte pin.

### Candidate acquisition sequence

1. An operator action selects a recipe and scope: running-Houston grounding or collection
   from a specified area. Discovery candidates remain distinguishable from selected input.
2. Resolve registered roots and source-specific adapters. Parse declared entries and
   validate the selected member. A controller adapter preserves its sole-index rule and
   checks program/function identity plus expected stamp.
3. Follow only the selected, typed navigation edges within the allowed source boundary.
   Read each source into a byte snapshot, then parse/select from that same snapshot.
4. Return the selected original content as distinct parts with source receipts. Include
   commit and path for committed material; identify edited worktree bytes explicitly and
   digest the actual acquired content. Do not label edited content as the committed blob.
5. Apply the recipe's ordering and budget. Report omissions or a selection that does not
   fit. A procedure is not silently shortened. Ambiguous legacy section selection falls
   back only to an explicitly allowed whole-file selection, not a guessed boundary.
6. Termbrana prepares/composes those acquired parts; a client can preview or compare pins.
   Acquisition does not activate the loaded program, execute header commands or send input.

These steps propose behavior to qualify, not behavior exercised by this consultation.

### One engine, clients with different weight

A light key-operated command can list/select/acquire and return content plus a receipt.
An IDE can add a source tree, search, preview, pin comparison and loading controls. Both
should consume the same resolution results, rather than independently interpreting
controllers or GUIDE manifests. An MCP adapter can expose those operations later.
The earlier manager-UI idea—checking what should be sourced—fits this client layer.

Use format adapters for current GUIDE, controller/function, plain-file SPECIAL and actual
germline/vendor shapes. Normalize their results at the acquisition boundary; do not
rewrite all source families into the example YAML. Shared loading semantics do not
erase differing source ownership or format-specific prerequisites.

Qualification should cover identical selected bytes through light and IDE clients,
controller mismatch rejection, scope enforcement, dirty-worktree receipts, source changes
during acquisition, deterministic ordering and visible budget omissions. Duplicate or
missing bindings must return an explicit unresolved result. This proposal remains
subject to the application's source-shape/reader/owner/acceptance matrix and existing
controller-profile/pin-ownership gates; the personal specimen does not freeze them.
See the [generation-X handoff](../../composer-01-parse/evidence/handoff.termbrana-generation-x.2026-10-21.md)
and [Houston's source-contract finding](../../composer-01-parse/evidence/consult.houston.resolve.2026-10-21.md).

For new material, I would prefer frontmatter: it gives the engine a predictable metadata
entry and presents source context before the Markdown body to a direct reader. That is
a practical navigation choice; we have not measured a training-data advantage over
footer metadata. A legacy footer could still have an explicit adapter if required.

## Eventual MCP and VIST relation

An MCP adapter could expose the provider's discovery and read behavior as resources and
its query behavior as a tool. The exact mapping remains open; MCP itself does not supply
a search engine or make arbitrary frontmatter discoverable. Resource publication requires
explicit server capability and list/read behavior.
[MCP resources, versioned specification](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)

VIST has a different role. Its local
[principle brief](../../nablarva-X4-vist/raw/vist-01-principle-and-applications.md)
separates passive observations, controller decisions and actuator effects. A future view
could show documentation beside observations, retaining each source's attribution and
timing. The documentation provider does not thereby become a sensor, controller or sender;
runtime observations do not certify a documentation contract. Detailed vendor claims in
that VIST design were not requalified by this consultation.

## Open architecture topic ready for the sitting

The [G5 ADR task-context consultation](brief.adr-task-context.2026-10-21.md) supplies a
concrete consumer case: task-bound selection of governing constraints, relevant rationale,
replacement relationships and evidence pointers, rather than automatic loading of all ADRs.
G5 subsequently accepted the team/controller direction and requested the role/timing
schedule in that brief. Reader fields, adapters and program placement still need their
actual contract and qualification; acceptance of the direction is not an installed reader.

Suggested pointer text for a later architecture draft, still a proposal:

> Nablarva Boost (working name): an open, read-only documentation-provider concept.
> One owned source serves human/file readers and an intended deterministic sourcing
> engine under operator keys, shared by Termbrana/IDE clients and possibly MCP. Frontmatter
> is a candidate navigation contract; source-specific adapters return selected content
> and derived pins. Schema, discovery scope, ownership/home/API and qualification remain
> open. See this concept before choosing documentation machinery.

The session head can carry this topic into the architecture draft and promote surviving
design to its appropriate durable home. Before pruning this bed, retained references need
the project's commit-pinning/promotion treatment. This raw brief is a discussion home,
not an additional standing documentation index.

Remaining decisions: choose the navigation surface and its owner; define scope and link
roles; pick metadata only for real queries; specify search and stale-source behavior;
then qualify file-reader/helper equivalence with the same tasks. A useful first case is
the Termbrana sending-authority question above, including a misleading historical hit.
No implementation, installation or retrieval experiment ran.

## Consultation provenance

Astrobley (GPT-6.1-Sol/high) supplied the senior-developer workflow and diagnosed what
README does not define. A researcher (GPT-5.6-Terra/high) traced the pinned upstream Boost
implementation. myShell folded both and directly checked the README, guidance adapters,
writer, rule parser/index generator, guidance template, search client and MCP registration
sources supporting the main distinctions. Training-data naturalness was not measured;
ordinary Markdown entry/link behavior remains a navigation heuristic.
Astrobley's follow-up consultation addressed the explicitly named hardcoded source
engine and proposed typed headers, adapters and acquisition receipts. myShell directly
checked the controller/function specimen, GUIDE headers/manifests and the cited Composer
source-contract constraints before integrating that extension. No source format changed.
