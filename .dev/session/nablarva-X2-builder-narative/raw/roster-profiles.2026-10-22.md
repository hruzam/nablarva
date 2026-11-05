# Roster profiles — X2 builder preparation

`checked: 2026-10-22 Europe/Prague`  
`scope: portable role definitions, deployed-file drift, and team fit; no role was activated`  
`sources: ~/ia-sync/{codex,claude}/agents/; deployed targets: ~/.{codex,claude}/agents/`

Report content: Terra researcher; durable integration and corrections: myShell. During
preparation myShell mistakenly asked the read-only researcher to write this file, and it
did. That was a role-contract mismatch, not a newly granted capability. myShell checked
and adopted the report; the launcher now keeps researcher consultations read-only and
assigns their durable fold to the head. No global role contract was changed.

## Evidence and limits

**OBSERVED.** `diff -qr ~/ia-sync/codex/agents ~/.codex/agents` and the equivalent
Claude command both exited 0 on 2026-10-22. The two Codex trees have 9 files each and
the two Claude trees 34 files each. The combined sorted-content-hash checks were
`c396d059…bd475a03` (Codex) and `9aa0e2c…33b350f1` (Claude). Thus every source
definition below is byte-identical at its deployed path at this check.

**LIMIT.** Equality of definition and deployed file does *not* prove that a launcher
currently offers its declared model, that a model selection wins over project/runtime
configuration, or that a role may be invoked in the present session. Role definitions
are capability/intention; actual runtime availability needs a fresh launcher-level
probe. The model strings below are copied from the role frontmatter, not benchmark
claims.

**Operator heuristic (not a measured equivalence).** `Luna ≈ Haiku`, `Terra ≈ Sonnet`,
`Sol ≈ Opus`, with Opus possibly stronger; `Astra` was tentatively compared with
“Claude Fable”. Treat this as a routing shorthand only. Fable's current naming was
separately verified by the X2 integration owner, not by this roster read.

## Codex roster (9)

| role | declared model / effort | purpose and hard boundary | source anchor |
|---|---|---|---|
| `architect` | `gpt-5.6-sol` / `xhigh`; read-only | Architecture options, invariants, migration and rollback recommendation. Cannot implement, write ADRs, delegate, lock, or make the owner's decision. | `~/ia-sync/codex/agents/architect.toml:3-25` |
| `astrobley` | `gpt-6.1-sol` / `high`; workspace-write | Senior scoped implementer with one corrective pushback and an evidence-bearing `implementation_return`. Needs a concrete objective/scope/acceptance; returns `NEEDS_GAVEL` for a material lock; no independent verification, delegation unless explicitly requested, commit/push/deploy/transport. | `~/ia-sync/codex/agents/astrobley.toml:3-45` |
| `challenger` | `gpt-5.6-sol` / `xhigh`; read-only | Adversarial pre-lock check: exactly a ranked position, one risk, one alternative, one watch signal. Does not general-review, mutate, delegate, or lock. | `~/ia-sync/codex/agents/challenger.toml:3-23` |
| `harness_builder` | `gpt-5.6-sol` / `xhigh`; workspace-write | Builds Codex-native harness primitives, using the `codex-harness` skill. Must propose first and wait for Majkee confirmation; authors source/surgical table only, never deployed runtime or activation. | `~/ia-sync/codex/agents/harness_builder.toml:3-30` |
| `houston` | `gpt-6.1-sol` / `high` | Germline-loaded grounding architect. Requires identity, Codex binding, nearest addendum, and an explicit card; ambiguous/missing load is its first finding. This thin wrapper alone does not establish project-card authority. | `~/ia-sync/codex/agents/houston.toml:4-36` |
| `implementer` | `gpt-5.6-terra` / `high`; workspace-write | Practical fixed-scope implementer: smallest coherent change plus narrow relevant checks. Stops on genuinely ambiguous scope; never becomes architect/challenger/verifier/controller or commits, deploys, transports. | `~/ia-sync/codex/agents/implementer.toml:3-25` |
| `oraculum` | `gpt-6-astra` / `high`; read-only in contract | Bounded strategic consultation child only for an authorized Cartan/myShell/Astrobley/Houston assignment. Separates substrate/architecture/directive; may not own canon/STATUS, implement, review, delegate, become a user-entry head, or operate transport. | `~/ia-sync/codex/agents/oraculum.toml:3-47` |
| `researcher` | `gpt-5.6-terra` / `high`; read-only | Evidence researcher for volatile APIs/protocols/runtime behavior. Labels OBSERVED/SOURCE/INFERENCE and separates bytes, rendered forms, transport, semantic structure, and replay; makes no lock or change. | `~/ia-sync/codex/agents/researcher.toml:3-23` |
| `verifier` | `gpt-5.6-sol` / `high`; workspace-write only for checks | Fresh-eyes acceptance gate: reads contract/handoff/diff, runs declared and minimal additional checks, returns fixed PASS/FAIL. Never fixes, expands scope, delegates, commits, deploys, or transports. | `~/ia-sync/codex/agents/verifier.toml:3-29` |

## Claude roster (34)

| role | declared model / effort | purpose and hard boundary | source anchor |
|---|---|---|---|
| `advisor-low` | Sonnet / unspecified | Fixed three-part second opinion for a Haiku-tier caller: verdict, primary risk, alternative. No clarification, synthesis, files, or commands. | `~/ia-sync/claude/agents/advisor-low.md:2-31` |
| `advisor-mid` | Opus / medium | Same narrow second-opinion envelope for Sonnet-tier architecture/cross-component choices. | `~/ia-sync/claude/agents/advisor-mid.md:2-32` |
| `advisor-advanced` | Opus / high | Same envelope, one tier above Sonnet for strategic/architectural or phase-transition decisions. | `~/ia-sync/claude/agents/advisor-advanced.md:2-32` |
| `advisor-high` | Fable / unspecified | Same envelope for the highest-stakes Opus-tier gate. Runtime Fable availability remains a launcher question. | `~/ia-sync/claude/agents/advisor-high.md:2-31` |
| `agol` | Fable / high | Broad continuous synthesis across phases/projects; not a challenger or planner. Read-only: it does not write or execute. | `~/ia-sync/claude/agents/agol.md:2-17,28-62` |
| `assay` | Sonnet / unspecified | Independent code/test gate, intentionally separated from builder context; runs declared checks and emits fixed PASS/FAIL. Never fixes, expands, or spawns. | `~/ia-sync/claude/agents/assay.md:2-17,20-62` |
| `astrobley` | `claude-haiku-4-5` / unspecified | **Tombstone.** The name crossed to Codex; this Claude seat must not dispatch and points callers to the handoff/`vega`/`mirror`. | `~/ia-sync/claude/agents/astrobley.md:2-22` |
| `atlas-auto` | Sonnet / medium | Autonomous Claude primitive creator. Writes only deploy-inert staging/specified project path, never live `~/.claude/`; no subagents. | `~/ia-sync/claude/agents/atlas-auto.md:2-12,22-25,70-95` |
| `atlas-ui` | `claude-opus-4-8` / high | Human-present interactive Claude primitive creator. Buffers and confirms before writing to surgical source, never live runtime; Bash is read-only. | `~/ia-sync/claude/agents/atlas-ui.md:2-14,23-28,66-74` |
| `capcom` | Haiku / unspecified | **Retired 2026-10-17.** Former goal-runner gate; do not act. Human gate is MANNED Flight or session head. | `~/ia-sync/claude/agents/capcom.md:2-27` |
| `color` | Opus / max | Mathematical/formal-language co-brain for Houston-family architects: derives proofs, bounds, and counterexamples; it is advisor, not implementer. Current-trend research routes to Epoch. | `~/ia-sync/claude/agents/color.md:2-8,12-45` |
| `delta` | Haiku / low | Pure surgical executor for a fully specified file scope. Makes no suggestions, adjacent changes, abstractions, or unrequested notices; asks once if ambiguous. | `~/ia-sync/claude/agents/delta.md:2-10,20-47` |
| `eagle` | Sonnet / low | Isolated project orientation: reads AGENTS → flag → pulse → PROJECT, maps structure, reports; may write a report only if explicitly asked and never touches harness/canon/source. | `~/ia-sync/claude/agents/eagle.md:2-22,123-152,290-313` |
| `epoch` | Sonnet / medium | Online version-sensitive researcher: resolves current date, web-verifies volatile claims, returns source/date/confidence. It is the Claude research alternative, not proof that its sources were used here. | `~/ia-sync/claude/agents/epoch.md:2-10,19-32,59-104` |
| `ferry` | Sonnet / high | Fixed office→home Tailscale transport conductor, default Freya route, with graded exit ladder and secrets/branch/deploy guards. Not a Nablarva builder role. | `~/ia-sync/claude/agents/ferry.md:2-12,17-44,46-75` |
| `field` | `claude-sonnet-4-6` / high | Large-corpus driller/synthesizer: returns the requested brief, no verdicts, targeted lookup, or implementation. | `~/ia-sync/claude/agents/field.md:2-14,17-70` |
| `flight` | `claude-sonnet-4-6` / high; dynamic Opus selection described | Tactical/session working head. MANNED Flight carries Majkee's live authority; UNMANNED Flight cannot lock/canon-author and routes gates. A project setting can override its frontmatter default; `/model` is described as reassertion. | `~/ia-sync/claude/agents/flight.md:2-21,31-66,105-143` |
| `houston` | Opus / high | Germline thin loader for consult/audit/sitting; project/card content is loaded at entry. It explicitly never owns lifecycle, STATUS, gavel, build, or functional verification. | `~/ia-sync/claude/agents/houston.md:2-20,22-48` |
| `hypatia` | none | **Retired 2026-07-02;** renamed/reconfigured to Claude `oraculum`. | `~/ia-sync/claude/agents/hypatia.md:2-12` |
| `janus` | Opus / xhigh | Read-only adversarial second voice before a lock; returns one ranked verdict/risk/alternative, not a plan or synthesis. | `~/ia-sync/claude/agents/janus.md:2-12,16-47` |
| `maxwell` | `claude-sonnet-4-6` / unspecified | **Tombstone.** Former home-maintenance twin; do not act without a fresh gavel/specification. | `~/ia-sync/claude/agents/maxwell.md:2-23` |
| `metaterminal` | Sonnet / high | Human-invoked, standalone terminal-stack/drift seat; never a subagent target, never deploys/deletes automatically/edits gated `temple-*`, and writes only ephemeral `/tmp` sandbox. | `~/ia-sync/claude/agents/metaterminal.md:2-14,17-36,60-96` |
| `mirror` | Haiku / unspecified | Cross-vendor, position-aware adversarial relay; carries a stated position to Codex and returns raw audit verbatim. Rejects position-free briefs; never blocks caller on relay failure. | `~/ia-sync/claude/agents/mirror.md:2-14,17-79` |
| `oraculum` | Fable / high | Existing direct-invoked scientist-tier strategic main-seat definition: wide/deep modelling, plans/directives, can spawn. It is distinct from the Codex child contract despite the shared name. | `~/ia-sync/claude/agents/oraculum.md:2-29,41-84,121-143` |
| `recorder` | Haiku / low | Session-memory librarian: organizes/synthesizes the designated memory surface, narrates rather than judges, never blesses code or runs tests. | `~/ia-sync/claude/agents/recorder.md:2-10,13-55,90-111` |
| `shannon` | `claude-opus-4-8` / high | Office-only PIQL privacy/information-flow mechanic. Its scope is the PIQL project/host, not X2 planning. | `~/ia-sync/claude/agents/shannon.md:2-10,20-51` |
| `symmetry` | Opus / unspecified | Conceptual AI–human cohabitation/doctrine consultant; parks practical stack work rather than taking it. | `~/ia-sync/claude/agents/symmetry.md:2-17,20-52` |
| `trajectory` | Sonnet / high | Senior hands-on builder: may flag a better path/push back, and may spawn Delta for a surgical task. Not the planner. | `~/ia-sync/claude/agents/trajectory.md:2-9,13-68` |
| `vara` | Haiku / high | Sequential POLYP walker: executes pre-routed track/PAD lines one at a time; append/edit only, never authors/classifies/replans/self-confirms. | `~/ia-sync/claude/agents/vara.md:2-24,27-105` |
| `vector` | Sonnet / medium | Middle-tier well-specified implementer where Delta lacks context capacity and Trajectory's pushback is unwanted. Does not make judgement calls, spawn Delta, or perform destructive work unasked. | `~/ia-sync/claude/agents/vector.md:2-14,27-63` |
| `vega` | Haiku / unspecified | Blind-triangulation Codex relay. Brief must omit caller answer/lean; returns raw Codex stdout, never interprets or blocks caller. | `~/ia-sync/claude/agents/vega.md:2-12,14-86` |
| `zed-editor-expert` | Sonnet / unspecified | Zed-specific adviser/config specialist with persistent agent memory. Its long contract is editor-specific, not a Nablarva build/team role. | `~/ia-sync/claude/agents/zed-editor-expert.md:2-9,11-93,134-270` |
| `zenith-zsh` | Haiku / low | Read-focused resident for deployed `~/.config/zsh` wiring. Its only permitted write is machine-local `blessings/broken-wiring.json`; unsuitable for source↔deploy changes. | `~/ia-sync/claude/agents/zenith-zsh.md:2-14,86-96,153-192` |
| `zenith` | Haiku / low | Targeted reader for heavy `raw.settings`/`raw.research`; extraction, not synthesis. Unavailable as a nested subagent. | `~/ia-sync/claude/agents/zenith.md:2-12,25-76` |

## X2 / X3 boundary and smallest team

**OBSERVED task authority.** Nablarva L16 assigns a cSharp head the session lifecycle,
RUNBOOK, STATUS, integration and closure, while Oraculum owns divergence/move formation;
L16 also requires one gate per session (`.dev/session/flag.md:L16.1-L16.3`). The active
Termpanum substrate proposes read-only observation: it never types into living sessions and
proposes discrete states toward the relay (`raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md:15-40`).
The exact discrete-state vocabulary remains pending under flag L14 D3 / docket 8.

**X3 is not a child.** Nablarva X3 is the existing operator-led **Claude Oraculum MAIN**
session with its own Mode-B head authority, STATUS and preprint. Its authority derives from that
session assignment, not from the generic Codex `oraculum` name. X2 is a separate Codex Cartan
MAIN session; exchange is an attributed handoff between heads. Neither takes the other's STATUS
pen, lifecycle, or transport authority.

**X2 now.** Keep Cartan/cSharp as sole X2 navigator, integration/test-dispatch owner and
STATUS/transport pen. MyShell/root writes the fixed initial launcher/RUNBOOK. Assign Codex
`astrobley` only the explicitly granted Termpanum PLAN raw-file body: it can make the scoped,
evidence-bearing plan contribution but does not replace the launcher or own STATUS. `architect`
may supply read-only ADR-style advice, not author the body. A Codex `oraculum` consult is optional
and remains a bounded child, never a substitute for X3.

**Successor `termpanum-XN`, after planning GO.** A continuing or fresh Cartan head adopts the
successor's sole STATUS pen and new gate. For one frozen, narrow implementation slice use
one Codex `implementer` (Terra/high), then
one fresh Codex `verifier` (Sol/high). If the slice needs senior corrective judgement before the
cut, use *one* `astrobley` instead of parallel writers. Add `researcher` (Terra/high) only for an
unresolved terminal/protocol fact. None gains commit, deploy or transport authority from its role.

**Honest Claude alternatives.** A MANNED `flight` can be a human-proxy working head; UNMANNED
Flight cannot take a lock. For a Claude build slice use `trajectory` when pushback is wanted or
`vector` for fixed specification, followed by `assay` as the fresh gate. Do not route X2/XN to
the Claude Astrobley tombstone, `metaterminal`, `ferry`, or a retired role.

## Smallest next decision

Freeze the exact Termpanum PLAN raw-file paths and acceptance shape in the X2 launcher. Then
Astrobley can author that bounded body while Cartan keeps the X2 STATUS pen and receives X3's
attributed preprint. Release a `termpanum-XN` implementation only through its successor gate.
