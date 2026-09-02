# status — session 02 (M0 truth spike) · live position

`updated: 2026-09-02 11:20 (Oraculum, office; operator majkee over SSH from home) · gate: M0 host contract — FROZEN (ADR-0002 gaveled by majkee 2026-09-02) · commit/push pending (majkee)`
`checkpoint: pad.1-m0-runtime-confirm.md — ALL fences filled (0 · 0′ · 1 · 2 · 2b · 3 · 4 · 5)`
`gloss: ../GLOSS.termbrana.md (operator learning, uncanonical)`

## Position

The operator pad is sat. Every step returned one of its declared verdicts; four findings were
new to the evidence set (see fences — the pad is the raw surface, this file does not retell it):

- STEP 2 / 2b · `get_pane_scrollback` strips ANSI; `PaneRenderReportWithAnsi` carries it →
  `rendered_ansi` reachable by subscription only. Blind subscription self-feeds (storm; session
  had to be quit).
- STEP 3 · intercept on/off sound; harness ordering bug (intercept before grant); operator
  lock-out real; out-of-band `zellij --session … action pipe` works as the off-switch.
- STEP 4 · plugin pane stable under resize; the *terminal* pane was the one that smeared.
- STEP 5 · unsubscribed probe: zero events during a 100k-line burst, ~0.6 % CPU; scrollback cap
  10 000; counter froze after a tab excursion, woke on a direct message (R1 unresolved).

Resolved on the way: RUNBOOK §4a (README expansion — committed in unification, checked),
§4b/4c (pins re-verified 2026-09-02, `ID=manjaro`, branch `stable`, zellij = Arch build via
Manjaro stable, rustc/cargo via rustup — appended to `research/evidence/host-versions.md`).
Pad re-pathed to `toolbox/termbrana/` (flag L12).

## Pending → gate closure sequence

1. ~~Fold~~ DONE 2026-09-02 (@Vector): pad fences → PENDING-OPERATOR rows of `research/evidence/t02–t05.md` +
   `pane-content-matrix.md`; each file's status/gap section gains "confirmed by pad.1 sitting,
   2026-09-02"; automated-session context preserved. New rows for 2b storm, intercept ordering
   bug, out-of-band off-switch, scrollback cap, tab-return R1.
2. ~~@Assay fresh-eyes~~ PASS 2026-09-02 over the full evidence set (handoff gate law — writer does not verify).
3. ~~Freeze decision~~ GAVELED 2026-09-02 (ADR-0002 r2 appended to DECISIONS.md): ADR-0002 draft at `adr-0002.host-contract-frozen.draft.md` (this dir) presented 2026-09-02 with Assay PASS; on gavel: append to DECISIONS.md, apply the README/ADR-0001 staleness one-liners, commit, push.
4. After freeze: session 03-tunnel unblocks (L11); M1 backlog gets the harness ordering fix
   and the "exclude own pane + debounce + tab re-sync" adapter laws.

## Dirty tree (uncommitted, majkee's to commit)

nablarva: `flag.md` (L12, pre-existing) · this dir: `pad.1…`, `RUNBOOK.md`, `status.md` ·
`../GLOSS.termbrana.md` (new) · `toolbox/termbrana/research/evidence/host-versions.md` (+ fold
targets once step 1 lands). reposoma: `raw.guides/gloss/GUIDE.md` (new, DRAFT) ·
`PAD/GUIDE.md` · `runbook/GUIDE.md` (+ pre-existing unrelated dirt).

## Carry (not this gate)

- `docs/repo-unification.2026-09-02.md` says `pull --rebase`; flag L12 says never — one-line fix.
- ia-sync `AGENTS.md` host-fingerprint row "nginx active = home" was wrong (Valet runs nginx on office) — corrected 2026-09-02 by this seat; journal entry prepended. ia-sync AGENTS.md still names Kelvin as the office seat while majkee says Kelvin/Maxwell are deferred — disagreement noted, majkee's to reconcile.
- 23 historical `unikuklatrix/nablarva/toolbox/termbrana` path refs in evidence/README/DECISIONS — sweep or
  leave, majkee's call.
- GLOSS convention line for nablarva `AGENTS.md` §Session surfaces — majkee's gavel.
