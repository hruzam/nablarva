---
doc: research.inner-claude-md
question: "Can MAJKEE.md carry an inner CLAUDE.md — markdown-in-markdown — as a mechanism?"
verdict: NO (native); UNSAFE-as-posed for this file
spawned_by: MAJKEE.md · MAIN RULES (open epistemic question)
date: 2026-08-06
wired_to_llm: false
---

# Inner CLAUDE.md as markdown-in-markdown — independent research

**Question (verbatim intent).** Can a single Markdown file embed an *inner `CLAUDE.md`* — a nested, agent-consumed instruction block — such that the harness treats the inner block as real instructions while the outer document stays human-only? Host file: `/home/hruzam/unikuklatrix/nablarva.devenv/.hlm/MAJKEE.md` (pseudo-CLAUDE.md, `wired_to_llm: false`, clean-room wall).

## Verdict

- **(a) Native content-based inner-CLAUDE.md loading — DOES NOT EXIST.** Claude Code discovers instruction files by **filename + location only**, never by extracting a region from the *interior* of another file. A file is loaded whole or not at all. There is no primitive that pulls a ` ```markdown ``` ` fence, a `<details>` block, an HTML comment, a frontmatter field, or any inner span and feeds only that to an agent. (HTML comments are in fact **stripped before injection** — hiding an inner block in a comment guarantees it is discarded.)
- **(b) Nearest native primitive = `@import`** (`@path/to/file`, relative, ~4-hop recursion, backtick-escapes, external paths prompt approval). But it is **whole-file, not section-level** — there is no `@file.md#section` anchor import. `@import` splits across *files*, never *within* a file. So it cannot keep MAJKEE.md human-only while importing "just the machine section" — importing pulls the KEY-side vocabulary too.
- **(c) Epistemic call for THIS file — UNSAFE as posed; a category error.** The wall rests on one checkable invariant: **the file is atomic and never auto-loads** (its name isn't `CLAUDE.md`/`AGENTS.md`, nothing references it). Any route that gets the inner block to an agent (an `@import` from a real CLAUDE.md, or a hook that reads the file) loads the **whole** file — breaching the wall the instant any load path touches it, because the harness cannot load a fraction. It also gives the file two contradictory contracts (never-wired vs. act-on-this) that the harness neither knows nor enforces.
- **(d) Recommended shape for "part human / part agent" — split by file, point away from the human file.** Author the agent-consumed content as its **own real load-path file**, strongest first:
  1. `_preflight/.claude/rules/<topic>.md` with `paths:` frontmatter → loads only when an agent touches matching files (tightest blast radius);
  2. a nested `_preflight/CLAUDE.md` → loads on-demand when files in `_preflight/` are accessed;
  3. a `SKILL.md` → description-triggered / on-demand.
  Any `@import` direction must be **machine → machine**: MAJKEE.md imports nothing agent-side and is imported/hooked by nothing. Never `@import MAJKEE.md` from a live CLAUDE.md. The wall stays enforced by **filename + no-reference** — exactly what the harness respects.

**If a single physical dual-use document is genuinely wanted**, the only path is a **compile-down / hook-inject step** (grep the block, emit it into a real CLAUDE.md or inject via `SessionStart`) — custom tooling, explicitly outside the native harness, and it reintroduces the very contamination risk the wall exists to avoid. Recommended against for this file.

## Discovery set (evidence)

Instruction-file discovery, in precedence — filename/location convention, no interior parsing:
`/etc/claude-code/CLAUDE.md` (managed) · `~/.claude/CLAUDE.md` (user) · `./CLAUDE.md` or `./.claude/CLAUDE.md` (project) · `./CLAUDE.local.md` (local) · subdirectory `CLAUDE.md` (load-on-demand when files in that dir are accessed) · `.claude/rules/*.md` (path-scoped via `paths:` frontmatter) · `AGENTS.md` (fallback only when no CLAUDE.md exists).

## Citations

- `/home/hruzam/reposoma/raw.research/agent-docs/report/raw.agent-docs.2026-08-01.md` — lines 455–465 (discovery set, `@import` semantics, HTML-comment stripping), 467–476 (rules / `paths:` frontmatter).
- `/home/hruzam/reposoma/raw.settings/raw.card.claude-code.md` — always-on context, CWD/filename-convention loading, hook-stdout injection (SessionStart / UserPromptSubmit) only.
- `/home/hruzam/unikuklatrix/nablarva.devenv/.hlm/MAJKEE.md` — frontmatter `wired_to_llm: false`; MAIN RULES / BONDS clean-room non-bond.

## One-line answer for MAJKEE.md

Inner CLAUDE.md-in-markdown is not a harness feature and would dissolve the clean-room guarantee MAJKEE.md exists to hold. Keep the wall (distinct filename, no references); if a machine part is ever needed, make it a **separate** `_preflight/.claude/rules/*.md` or nested `_preflight/CLAUDE.md`, never a block inside this file.
