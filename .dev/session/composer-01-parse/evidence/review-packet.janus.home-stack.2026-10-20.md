---
kind: review-packet
date: 2026-10-20
author: Cartan · navigation owner
scope: Written v4, reusable Termbrana composition direction, source home, conditional Python and verification
status: Prepared for Majkee-carried Janus challenge; no reviewer launched
---

# Composer — current home, stack and review decision

Read the project entry/read order and this session's RUNBOOK/STATUS:

- /home/hruzam/unikuklatrix/nablarva/AGENTS.md
- /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/RUNBOOK.md
- /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/STATUS.md

This packet is a concrete proposal for challenge, not an implementation or a grammar
GO. The fixed gate remains Phase 0 exit finding, brief §3. No final GO on written
v4 or implementation release has been recorded. This is not the older v2 packet.

## Operator words and Cartan's response

Majkee's source-home/stack/reviewer message, verbatim:

```text
1. Code home: `~/ia-sync/zsh/termbrana/composer.zsh` + its family scripts according sibling pattern (?) confirm if agree or need totaly separate brick `prompt-composer`?
2. python if fast enough.
3. agree with verifier as `subagent: challenger` or give me prompt: `to-janus from-cartan --- <what to test> ---`
```

Cartan agrees with the offered Termbrana home. Keep the parser as a cohesive helper
in this family; a separate `prompt-composer` family/repository is not justified by
the current dependency boundary. Composition should remain callable by different
clients; it need not acquire another family or repository to do so. This records the operator's offered home and Cartan's confirmation,
without creating the directory, selecting a command prefix or enabling anything.

Majkee subsequently directed that architecture live above session limitations in
the original files, and explicitly included tmux or similar push targets, Sublime
Text/Lite XL, pipes and assistant contributions. Exact words are captured at
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/direction.majkee.termbrana.2026-10-20.md.
The current documentation body is /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md,
indexed by /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md §3.1. Read the actual
changes there. Session beds attach to this reusable surface; their gates limit
execution in a sitting, not the product's architectural boundary.

Composition ingress from humans/editors/pipes/assistants and explicit target
delivery need distinct operations and shared ownership/binding rules. Exact APIs,
writer arbitration, storage and carrier qualification are open. The existing
Zellij observer remains read-only by default. Its adopted project definition §2.4
already allows a separately enabled input capability. L3/L4 still reject tmux as
the regulated room protocol/injection leg: the operator's requested push surface
must not silently be promoted to an accepted relay. Check this seam explicitly.
Phase 0 only parses and preserves bytes; the broader input/output direction does
not add sending or instruction discovery to that parser.

Proposed family shape follows the observed local convention:

```text
/home/hruzam/ia-sync/zsh/termbrana/
  base.zsh       # idempotent, silent signpost; definitions only on source
  keyboard.zsh   # aliases/comments only
  composer.zsh   # thin zsh command functions
  composer.py    # standalone Python stdlib parser logic
```

Keep Python logic callable independently of the interactive shell and any future
editor client. Exact callable interfaces, fixture/output paths and tests must be
bound in the later implementation POINT. This folder is an ia-sync shell family,
not a new project harness or a change to Nablarva/Termbrana's L11/L12 topology.
Publication remains L8′; activation, installer runs and both-host wiring are separate.
The command name must not replace existing `/usr/bin/composer` (PHP Composer).

Python stdlib is accepted conditionally on observed speed. Cartan expects it to
fit a byte-oriented, single-pass parser at the present corpus size, but no parser
exists to benchmark. The four frozen bodies total 38,799 bytes (inventory below).
Future acceptance must measure the real CLI including interpreter startup on the
corpus and a larger valid input, report host/input/commands/timings, and expose
whether runtime grows with input size. A latency budget and larger-input extent
must be made explicit in the implementation acceptance contract; no measured
performance or selected hard limit is claimed here. One Python invocation per
operation is the proposed wrapper shape, rather than one invocation per line.

The requested role substitution has a substantive limitation: native `challenger`
provides a ranked design judgment; Claude Janus has Read/Grep/Glob only and never
executes commands. Neither contract supplies functional acceptance evidence.
Cartan recommends retaining a fresh native `verifier` (or separately selected
Claude Assay) after the build. That functional seat remains unbound; Janus here
challenges the written contract and plan only. Builder and verifier stay separate.

## Actual review inputs and observed evidence

- Written v4: /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/grammar.builder.v4.md
  SHA256 `a977682c65bcd6b3c66cc67cb7c2b40a926cf4d96a7f58eb50f1a1fb0839b2ec`.
- Literal packet: /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/fixtures/packet.handwritten.v4.md.
- Controlling C1 instruction: /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/decision.majkee.c1.2026-10-20.md.
- Phase 0 exit and corpus: /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/brief.nabla.composer-build.2026-10-17.md §3;
  /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/corpus-inventory.cartan.json.
- Sibling implementation: /home/hruzam/ia-sync/zsh/session/ovitmugen.zsh invokes its adjacent stdlib Python body;
  /home/hruzam/ia-sync/zsh/session/base.zsh and /home/hruzam/ia-sync/zsh/nablarva/base.zsh show the family signpost pattern.
- Applicable convention: /home/hruzam/ia-sync/zsh/AGENTS.md §Control-panel convention;
  /home/hruzam/ia-sync/zsh/guides/guide-for-builder.md §Architecture rules;
  /home/hruzam/ia-sync/zsh/guides/keyboard.md §The grammar.
- Role contracts: /home/hruzam/.codex/agents/challenger.toml;
  /home/hruzam/.codex/agents/verifier.toml;
  /home/hruzam/ia-sync/claude/agents/janus.md.
- Product/transport boundary: /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/research/termbrana.project-definition.md §2.4;
  /home/hruzam/unikuklatrix/nablarva/raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md §Settled points and §Deaths;
  /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md L3/L4/L11/L12/L16/L8′.

Read-only probes on office found no existing `zsh/termbrana/`, `composer.zsh` or
`prompt-composer` family in the searched zsh/install-pkgs/deploy scope. PHP Composer
resolves to `/usr/bin/composer`; Python resolves to `/usr/bin/python3`, version
3.14.7. This is a local observation, not a cross-host qualification. V4's manifest
and all 19 raw entries verify. No parser, family scaffold, benchmark or live wiring
was authored by this preparation.

## The bounded challenge

Find the single weakest assumption in the proposed Phase 0 move. Inspect v4's
field/body boundary, exact-byte framing, diagnostics and acceptance cases; assess
whether reusable composition and optional session/editor/pipe/assistant clients
retain a coherent write and explicit delivery boundary, whether the offered home
and thin zsh/Python separation fit the sibling rules,
and whether the proposed independent functional evidence and performance condition
would be sufficient before acceptance. Existing builder transcripts and earlier
advisors' conclusions are not inputs to this fresh judgment.

The candidate must reject program/function header occurrences with unknown_key,
require the remaining five fields, preserve composed body text without discovering
or executing it, stop on the first exact wrong-EOL closer, reject an entire invalid
document, and preserve all body/packet/document bytes under §9. Parser success
grants no identity, permission, reference resolution, delivery or writer authority.

Return your native proceed/revise/stop judgment, one primary risk with source
anchors, one concrete alternative, and an execution watch if sound. Read-only:
no file writes, commands, helpers, implementation, STATUS, transport or gavel.
Majkee carries your reply to Cartan for attributed capture and checked disposition.
Final grammar GO, the functional verifier and implementation release remain human
decisions; the Python choice retains its performance condition.
