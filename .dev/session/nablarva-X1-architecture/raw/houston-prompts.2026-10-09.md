# Houston — install + prompts per situation (X1, install-for-test)

`author: oraculum(cSharp) · 2026-10-09 · state: install-for-test (majkee) · renders: .claude/agents/houston.md · .codex/agents/houston.toml · .codex/profiles/houston-nablarva.config.toml (body 9c0856f5 in both Codex files) · pins: raw.card.model-effort active_pins`

Card law (render §Card selection): the **first line** names the card — `card: consult | audit | sitting`; absent → consult. Work outside the card's pen → `out of card:`.
Install name = neutral `houston` (majkee 2026-10-09: one global neutral build narrowed by project .germline at runtime — design goes to germline-01). Content today = the nablarva-composed body; the project file .codex/profiles/houston-nablarva.config.toml is its source until germline-01 renders the neutral one.

## 0. Install (majkee, office, once)

Journal entry in ~/ia-sync/journal.host-cleanup.md is written by a spawn per the file's own rules (newest first) — never an `echo >>`.

```zsh
cp ~/unikuklatrix/nablarva/.codex/profiles/houston-nablarva.config.toml ~/.codex/houston.config.toml
cmp ~/unikuklatrix/nablarva/.codex/profiles/houston-nablarva.config.toml ~/.codex/houston.config.toml && echo installed
```

## 1. Codex · main (profile) — smoke

```zsh
codex --profile houston -C ~/unikuklatrix/nablarva
```
```text
card: consult
Entry proof only, no files touched: (1) who are you, in one line; (2) which card are you on;
(3) quote verbatim the first source-stamp line and the last sentence of your instructions;
(4) one consult finding: does PROJECT.yaml point docs.architecture at the L16.9 home?
Read only PROJECT.yaml and .dev/session/flag.md.
```
Pass = says Houston (not Cartan), stamp + tail quoted, one finding `fits|stretches|breaks|unclear`. Then give oraculum the rollout path → assay checks turn_context = gpt-6.1-sol / high (pin `codex/houston-main`).

## 2. Codex · child — pin witness

Fresh `codex -C ~/unikuklatrix/nablarva`, paste Turn 1 of `raw/probe-brief.houston-child.2026-10-09.md` unchanged. Rollout paths (head + child) → oraculum → assay checks the child's turn_context = gpt-6.1-sol / high (pin `codex/houston-child`).

## 3. Claude · main

```zsh
cd ~/unikuklatrix/nablarva && claude --agent houston
```
```text
card: consult
Who are you, in one line; then one consult finding: does PROJECT.yaml point docs.architecture at the
L16.9 home? Read only PROJECT.yaml and .dev/session/flag.md. No writes.
```

## 4. Claude · child (from any Claude head in nablarva)

```text
Spawn the `houston` subagent with this prompt, return its finding verbatim, make no edits:

card: consult
<one question touching a component boundary / lock / drift>. Evidence: name the paths you read.
Return: card · verdict (fits|stretches|breaks|unclear) · evidence paths · unverified · ≤5 constraints.
```

## 5. Check 4 — the sitting (Claude main recommended: opus/high, witnessed render; Codex main is not yet witnessed)

Before it: majkee names the sitting bed slug (one gate, under `/runbook`); oraculum opens it. Open question to rule first:
`docs/ARCHITECTURE.md` stub says the first real doc lands "after the gavel docket closes (v1 language + V1 cut)" — is that
still a precondition, or does L16.9 supersede it?

```zsh
cd ~/unikuklatrix/nablarva && claude --agent houston
```
```text
card: sitting
Bed: .dev/session/<slug>/ (yours; drafts only here — never docs/, never flag.md, never another head's STATUS).
Gate: majkee records GO on a draft of the first real whole-animal architecture doc, ready to promote to
docs/ARCHITECTURE.md (L16.9 homes: shared cross-organ grammars + whole-animal architecture).

This is the first real sitting: your card says "the full card is written at the first real sitting" —
write that card as a draft too (<bed>/raw/card.sitting.draft.md).

Inputs (cite, do not copy):
- locks: .dev/session/flag.md (L12–L16; L16.9 homes)
- whole-animal evidence: .dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md (classified USEFUL;
  J1 = wrapper fat because the doc has no body)
- wrapper: .dev/session/AGENTS.PROJECT-DESIGN.md (KEYS CODE grammar → moves to the doc; J1 thinning as a PROPOSED diff)
- substrate: meshup/REGISTRY.md, raw.nablarva/ (triad comparison 2026-07-31), docs/ARCHITECTURE.md (current pointer)
- organs: termbrana (toolbox/termbrana/), stridularium, ovitmugen, muticula — read their wrappers/STATUS only as needed

Write in the bed:
1. <bed>/raw/ARCHITECTURE.draft.md — whole-animal shape · organ list with homes · cross-organ grammars (KEYS CODE
   moved here) · the ladder stages 1–3 · open questions.
2. <bed>/raw/wrapper-thinning.diff — J1 as a proposed diff against AGENTS.PROJECT-DESIGN.md (the keeper commits).
3. <bed>/raw/lock-proposals.md — any proposed lock text (the head carries it to the docket).
4. <bed>/raw/card.sitting.draft.md.

Pen: Write only new files in the bed. Readers (field/zenith/eagle) and assay allowed; no executors.
Before drafting, give me the arc and 2–3 alternatives with constraints, and wait for my pick.
```

## 6. Audit (check 5, after the doc is promoted)

```text
card: audit
Walk wrapper → organ bodies (termbrana) → docs/ARCHITECTURE.md → guides → flag. Findings mech · judge · cross;
propose `checked:` stamps. Write to .dev/session/<invoking bed>/raw/houston-audit.<YYYY-MM-DD>.{md,diff}.
Majkee commits the diff; you never apply it.
```
