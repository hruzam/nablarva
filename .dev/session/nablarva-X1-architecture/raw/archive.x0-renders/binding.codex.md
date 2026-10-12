---
binding: houston
vendor: codex
runtime: Codex custom agent for a child; named profile for a main session
scope: mechanics only — entry, permissions, delegation and proof; grants no authority beyond the identity, addendum and selected card
authority: HOUSTON-R4 / RETURN 10; assignments 15 and 16; project flag L16, including amended clause 14
state: CANDIDATE — composition only; runtime artifacts not authored or loaded
verified: none — no fresh-session behaviour proof
canonical-home: /home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/binding.codex.md
canonical-home-note: locked-by-gavel: majkee 2026-10-07, binding homes = <project>/.germline/agents/houston/binding.<vendor>.md; source home assigned, promotion remains separate
authored: 2026-10-07 · cartan(coordinator) · re-base of RETURN 15 after majkee journal §1.1.1–1.1.2
---
# houston · Codex binding

## Entry declaration

The invoker puts `card: consult | audit | sitting` on the first line of the assignment.
Omission selects `consult`. An unknown card or work outside the selected card returns
`out of card: <request> → <owning card or seat>`. The identity and nablarva addendum
define the work; these routes only load it.

| | **child binding** (returns bounded work) | **main-session binding** (leads a bounded invocation) |
|---|---|---|
| **cards** | consult · audit-as-probe | audit (full) · sitting |
| **entry** | project custom-agent TOML at `<project>/.codex/agents/houston.toml`, selected by the authorized head or majkee with `spawn_agent` | fresh interactive `codex --profile houston -C <project-root>`; the separately authored `~/.codex/houston.config.toml` profile must carry the accepted composed render as session-level `developer_instructions` |
| **permissions** | effective child sandbox, approval policy and exposed tools; the card bounds writes further (consult: finding only); the TOML cannot enlarge inherited authority | effective main-session sandbox, approval policy and exposed tools; audit writes only assigned findings and proposed wrapper diff, sitting only assigned drafts in its own bed |
| **delegation authority** | consult needs no helper; any helper available to a child is bounded to reading or verification, never Houston's judgment or a wider pen; an audit-as-probe without required capabilities declares itself `unqualified for the complete card` | bounded readers or verifier as the card needs; no Houston → Houston loop, no creator; the session head and majkee retain lifecycle and gavel |
| **return destination** | spawner's context; when the head runs a bus, a `_bus/NN.houston.return.md` assigned by the head, which alone updates RUNBOOK/STATUS | audit: exact assigned `.dev/session/<invoking bed>/raw/houston-audit.<date>[.<cycle>].{md,diff}` paths; sitting: its own assigned bed drafts; return to majkee and stop |

The custom-agent TOML and profile TOML are **additional runtime artifacts**, not members of
this seven-file source package. They do not exist in this workbench. Majkee must name a
promotion/deployment step and a sole writer for each before either route is activated;
the Houston source/render writers here do not create them silently. A custom-agent file
configures spawned sessions, not direct CLI entry. `--profile` does not load that file.
The current workbench render is a composed review artifact, not a runtime-loaded role.

## Native mechanism and scope

- **Read/search/list:** use the native tools exposed in the invoked session for the
  identity's read, grep and glob capabilities. A terminal command is a mechanism, not
  a new authority. Never route a refused read through a child or helper.
- **Write:** use native edit tools for exact card outputs assigned by the invoker.
  Consult writes only its finding; the head decides whether to store it. Audit emits
  findings and a proposed mechanics diff, never applies the diff to the wrapper.
  Sitting drafts only in its own bed. No card grants STATUS, flag, commit or deployment
  authority.
- **Spawn:** use a native delegation tool only when it is available and the selected
  card and invoker authorize a bounded reader or verifier. A child helper inherits the
  effective permission ceiling and receives an explicit read scope and return path.
  A route lacking a capability required by the complete card returns a limited,
  expressly unqualified finding and names the qualifying route.
- **Permissions:** effective runtime policy governs. An assignment's path list is a
  cooperative bound inside that policy, not an enforced filesystem sandbox. Record the
  exact refused operation; do not widen permissions or evade a refusal.

The main-session route is a native Houston entry; it does not require a Cartan parent.
The delegated route follows the current local hierarchy when Cartan is the authorized
head. Neither route makes Houston the invoking bed's cSharp or keeper by itself.

## Composition

Composition order is identity → project addendum → Codex binding. Each source body
(bytes after its leading frontmatter's second `---`) is copied unchanged into its
`<!-- identity -->`, `<!-- addendum -->` or `<!-- binding -->` marker pair. The render's
first body line stamps each **canonical source path @ current Git blob**. A later
section specialises mechanics without overriding the shared contract, project locks
or runtime instruction hierarchy. Any conflict returns as a finding. Edits go to
sources, followed by mechanical recomposition; never hand-edit the render.

## Fresh-session proof — independent, still open

The witness records the exact render and source blobs, CLI version, project root,
effective permissions, exposed tools, invocation and output for **each** route. A
source declaration or an earlier TUI child-spawn receipt is not behaviour proof.

1. **Load and select:** in a fresh child, confirm `spawn_agent` selected the project
   Houston TOML and returned a consult-shaped finding. Test explicit `card: consult`,
   omitted card and an audit-under-consult `out of card:` reply. In a fresh main
   session, confirm the Houston profile loaded the composed render, then select audit.
2. **Read and write:** find/read an assigned fixture with a permitted mechanism.
   Confirm consult writes no project file; an assigned audit finding and diff land at
   their exact paths and no other project file changes.
3. **Delegation:** record whether a child exposes spawning; it is not required for
   consult. In the main session, authorize one bounded read-only helper on the
   fixture and record its returned marker. If unavailable, the full audit binding
   is unqualified. A child audit probe declares any missing capability.
4. **Gate order:** a capability probe is not the L16.13 real audit. Majkee invokes
   that audit after composition and vendor proofs; keeper migration follows the
   real audit under its separately assigned write scope.

## Evidence for these mechanics

Observed on office 2026-10-07: `codex-cli 0.160.1`; `codex --help` exposes
`--profile`, `-C` and an optional initial prompt, but no direct `--agent` selector.
Official OpenAI documentation: [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
defines project `.codex/agents/*.toml` as custom agents for spawned sessions;
[Profiles](https://learn.chatgpt.com/docs/config-file/config-advanced#profiles)
defines `--profile` and `~/.codex/<name>.config.toml`;
[Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)
defines `developer_instructions` as session instructions. These document entry
mechanisms, not this candidate's fresh-session behaviour.
