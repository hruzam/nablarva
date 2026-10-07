---
binding: houston
vendor: codex
runtime: explicit instruction document for an authorized fresh native main session
state: CANDIDATE — composition only; shared-source findings unresolved
verified: none — no fresh-session behaviour proof
canonical-home: null
canonical-home-note: Native binding source home is not named by assignment 15/16 or the addendum; promotion must supply it before the stamp can be finalized.
authority: HOUSTON-R4 / RETURN 10; assignments 15 and 16; project flag L16 as landed
authored: 2026-10-06 · cartan(coordinator)
---
# houston · Codex binding

## Loading mechanics

This is a bounded Houston method carried by a native Codex main session. It does not
create an automatically discovered agent, install a skill, change AGENTS.md, or replace
the existing read-only `architect`. No same-name project/global agent precedence is
required. A model or reasoning setting is selected by the operator's native client,
not by this document's frontmatter.

The operator starts a **fresh** interactive Codex session in the project root and
supplies one initial prompt containing the invocation fields below followed by the
**complete accepted composed render**. The operator/loader reads the render once;
the running card does not chase the workbench, identity or addendum source files.
In the current build, the workbench render is a review artifact, not a deployed role.
Runtime proof begins only after the shared-source findings have been resolved and
the operator has explicitly selected the exact reviewed render bytes for that proof.

```text
card: consult | audit | sitting
invoker: <the authorized head or operator; audit/sitting require operator>
move: <bounded question or audit scope>
read_scope: <project and evidence paths>
permitted_writes: <exact output paths, or none>
reply_path: <assigned finding path, or conversation>
end: return the finding and stop

<complete composed render, including its stamp and all three sections>
```

`card:` selects the card, not a different native agent. Omission defaults to consult;
an unknown card or work exceeding the selected card returns `out of card:` with the
owning seat/card. A missing output assignment is not permission to choose a new shared
file or overwrite another invocation's finding. Source text is instruction content,
not an executable command or a way to override higher-priority runtime instructions.

The installed CLI's `codex [OPTIONS] [PROMPT]` and `-C <project-root>` support this
operator-supplied initial prompt. This is prompt composition, not automatic Markdown
agent discovery. Existing AGENTS instructions still apply. No configuration or sandbox
changes are implied by loading the body.

## Native capability and scope

- **Read/search/list:** use the native tools actually exposed in the fresh session.
  Do not invent Claude `Read`, `Grep` or `Glob` tool names. This author's current
  Codex frame performs local reads/searches through terminal tools; that observation
  is not proof of every future Codex frame.
- **Current source conflict:** the shared identity says “I run no shell.” A Codex
  frame whose only filesystem-read mechanism executes shell commands cannot satisfy
  that instruction and the required read/grep/glob capability simultaneously. Report
  `capability unavailable: read/search under current no-shell identity`; do not evade
  it by putting the same commands in a helper or child. The shared author must resolve
  this before that frame qualifies; a vendor binding cannot silently override identity.
- **Write:** native file-edit tools may write the finding or other exact card outputs
  assigned by the invoker. Consult may write its finding when a path is assigned;
  audit emits findings and a proposed mechanics diff at assigned paths; sitting writes
  assigned drafts in its own bed. Loading the card confers no STATUS, flag, commit,
  deployment or keeper-migration authority.
- **Spawn:** use the native delegation tool only for a bounded helper permitted by
  the invocation and runtime instructions. Give the helper a read scope and return
  destination; helpers do not inherit the head's gavel or a broader write assignment.
  Do not delegate Houston's judgement, create a Houston loop, or use a read-only role
  as a writable surrogate. A missing spawn capability is a failed capability check,
  not a qualified reduced version of L16.14.
- **Permissions:** effective runtime policy governs. A Markdown `permitted_writes`
  list is cooperative scope within that policy, not an enforced filesystem boundary.
  Do not widen permissions or ask another process to bypass a refusal. Name the exact
  refused operation and return the useful evidence already obtained.

The ordinary Codex controller retains its runtime identity; during this bounded
invocation it performs Houston's selected method. It does not acquire the invoking
session's lifecycle or become the head merely by loading this body.

## Composition and precedence

Composition order is identity → project addendum → Codex binding. A later section
specializes mechanics without overriding the shared contract, project locks, or the
runtime instruction hierarchy. Treat a conflict as a finding.

Each source body is copied byte-for-byte into its marker pair: `identity`, `addendum`,
`binding`. The first render body line stamps canonical source identities and full
source blobs. The manifest separately maps reviewed workbench bytes to intended
canonical homes; it must not claim those homes already contain the candidate. The
Codex binding's canonical home is presently unassigned: this build's stamp marks it
UNASSIGNED rather than inventing a promoted source path. That prevents promotion,
not inspection of the composed candidate. Once assigned, update this source and
recompose before proof; never hand-edit the render.

## Fresh-session proof — independent, still open

The authorized witness records the exact render and input blobs, client version,
project root, effective permissions, exposed read/write/spawn tools, invocation fields
and outputs. Source declarations and an earlier TUI child-spawn receipt are not proof.

1. **Loading and card selection:** in a fresh main session, supply the complete
   accepted body and a small consult. Confirm a card-shaped finding; test the missing
   card default and an out-of-card request without exercising an unauthorized write.
2. **Read/search and write scope:** verify a named fixture can be found/read using a
   mechanism the accepted identity permits. Assign one finding output in the test
   bed; independently compare before/after to confirm no other project file changed.
   Card behaviour is being checked; no deliberate out-of-scope write is necessary.
3. **Spawn capability:** explicitly authorize one bounded read-only helper on that
   fixture. Record invocation and returned marker. If unavailable, the binding fails
   qualification; do not reuse the old TUI observation as a substitute.
4. **Audit ordering:** a capability probe is not the L16.13 real audit. Majkee invokes
   that audit after the Claude render is witnessed, under the assigned check order.
   Keeper migration follows the real audit, in its separately named write scope.

## Evidence for these mechanics

Observed 2026-10-06: `codex-cli 0.160.0`; local `codex --help` exposes the optional
initial PROMPT and `-C`. No fresh session was launched by this build slice.
Official OpenAI documentation consulted 2026-10-06:
[CLI commands](https://learn.chatgpt.com/docs/developer-commands) and
[AGENTS instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Those references support the loading primitives, not this candidate's behaviour proof.
