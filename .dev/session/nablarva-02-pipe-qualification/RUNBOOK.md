---
goal: Learn, on disposable sessions, whether a native operator-triggered assignment into an already-running Codex session can be trusted as the first Nablarva pipe — or whether it cannot, and why.
gate: "Majkee records GO or STOP on Oraculum's evidence-backed qualification VERDICT: can one explicitly bound, already-running, disposable Codex session receive a native operator-triggered assignment and produce its exact correlated RETURN, while preserving identity, permissions, native UI and subscriber usage?"
head_note: "cSharp — Oraculum authored this RUNBOOK and stays live through the whole arc as navigator and status_owner; it may delegate every body of work and receive only navigation + test parts; it closes the session if it can."
participant_1: [oraculum, {brand: claude-code-cli, model: fable, effort: operator-selected}, hruzam-120922]
participant_2: [cartan, {brand: codex-cli, model: astra, effort: session-configured}, hruzam-120922, resident]
participant_3: [majkee, {brand: human, model: not-applicable, effort: not-applicable}, hruzam-120922]
status_owner: oraculum
standing_witness: "cartan — tests head coordination and STATUS claims as paths (RETURN §4); never accepts its own plan or probe"
schema_note: "raw.guides/runbook/GUIDE.md verified 2026-09-05 · res/csharp-head-protocol.md gaveled 2026-09-04 · res/fanout-turns.md not engaged (single technical branch) · PAD/GUIDE.md for operator sittings · gloss/GUIDE.md"
founding_reference: "/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-01-design/raw/design.r1.md — sha256 b43d10ae13535e053547523044fb6c22e6448cc00f503457a60e48da3ab6814a — GO by majkee 2026-09-12; audited in .../_bus/01.oraculum.verdict.md"
branch_selection: "B-entry — majkee's choice, made in Cartan's session and relayed by Cartan's public message (rollout 01a092ed…c57d8, line 1985, 2026-09-12T21:18:57Z); majkee's own relay of that pointer on 2026-09-13 is taken as his signal; a direct chat confirmation is welcome and will be transcribed into STATUS"
adopted_on: 2026-09-13
gloss: ../GLOSS.nablarva.md
---

# RUNBOOK — nablarva-02-pipe-qualification

> Read once. Position lives only in `STATUS.md`. Model labels are majkee's allocation. Seats in
> `_bus/` filenames: `oraculum`, `cartan`. This bed qualifies a **mechanism on disposable
> sessions**; it never targets the working Cartan or Oraculum sessions.

## Why this session

- Gate 01 approved design r1. Its own acceptance test says: qualify native activation on
  disposable operator-opened sessions before any build; "B entry" is that qualification.
- Golden rule: the native surface exists — `codex queue --thread <UUID|name> --message` on
  codex-cli 0.154.0 ("queue a message for an existing session"), `codex agents` on the shared
  local app-server daemon, app-server `thread/read` with `status ∈ {notLoaded, idle,
  systemError, active+activeFlags}`. Its ack, busy and usage-path semantics are undocumented.
  The delta this bed may earn is the binding + correlation discipline around it; the native
  change that retires the delta is documented queue acknowledgement/busy semantics plus a native
  cross-vendor join preserving sovereign receipts.
- Divergences from Cartan's relayed handoff, stated once: (1) the queue-during-active-turn
  *characterization* is not dropped — it is a separately labeled optional test requiring
  majkee's explicit approval per sitting, and it can never relax r1's rule that busy, awaiting
  approval, or unknown means **no submission**; (2) the PAD is composed by the head from Cartan's
  audited plan, because a PAD is a test surface and the head may hold test parts.
- What this bed does **not** decide: browser construction, deployment, activation of the working
  sessions, Claude-side activation (sibling C), any L4 exception (if native fails, this gate
  STOPs; an exception request is a new gavel, not a fallback here).

## Scope and phases

| Phase | Owner | Output | Human hand |
|---|---|---|---|
| P0 read-only preflight | cartan (POINT 01) | `raw/preflight.r1.md` · `raw/qualification-plan.r1.md` · RETURN | carry POINT path |
| P1 audit | oraculum (+ @janus) | VERDICT 01; head composes `pad.1-b-entry.md` from the audited plan | — |
| P2 arm | majkee | opens ONE named disposable Codex session in a scratch workspace; approves activation for that sitting, naming the exact target | yes — both |
| P3 sitting | majkee sits, oraculum drives, cartan engineers | PAD breathes into itself; positive + negative cases | yes |
| P4 verdict | oraculum | qualification VERDICT with counts and evidence | — |
| gate | majkee | GO or STOP recorded against the VERDICT | yes |

No native send before P2 approval. Every sitting names its exact disposable target (session
UUID, workspace, host) in STATUS `holds:` before the first step; a changed target is a new arming.

## Shared rules and ownership

- Oraculum: navigator, sole STATUS writer, auditor, PAD driver. Cartan: technical lead —
  preflight, plan, probe code, engineering execution, its own bounded native helpers. Helpers
  on either side are Tier B (no BUS cycle each, no STATUS advance, no seat impersonation).
- Cartan's probe code, if any, lives under this bed's `raw/probe/` — disposable, pruned with the
  bed unless separately promoted through the surgical table; nothing is deployed; existing
  browser code (`/home/hruzam/ia-sync/zsh/session/runbook.py`) stays untouched.
- Cartan's STATUS-claims check lives in RETURN §4; Cartan witnesses coordination, never its own
  acceptance. Oraculum audits without repairing; corrections are new cycles.
- PAD law: one step revealed at a time, copy-pasteable, STEP 0 = state check, each outcome
  branched; the PAD is the raw surface, verdicts distil to the cycle VERDICT; GLOSS notes are
  written **before** each step the operator sits. Never a file per step.
- r1's operational rule binds: prepared / submitted / consumed / RETURN present / accepted /
  STATUS advanced are distinct; timeout is unknown, not permission to resend; no retry,
  retarget, or fallback paste; a status observation alone does not fence an idle-to-busy race;
  file presence is not consumption.
- Baseline discipline: count operator actions per named category (setup · routine carriage ·
  recovery · audit/gavel); no savings claim without a measured baseline; the sender-side count
  of bed 01's POINT carry remains owed and does not block read-only preparation.

## Known holds and write boundaries

- Activation scope: this bed and one router row in `/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md`.
  Oraculum owns `RUNBOOK.md`, `STATUS.md`, `pad.*.md`, the router row, its POINTs and VERDICTs.
  Cartan owns `raw/preflight.r*.md`, `raw/qualification-plan.r*.md`, `raw/probe/**`, its RETURNs.
- Targets: **disposable sessions only**, opened by majkee, named in STATUS before use. The
  working Cartan (`…c57d8`) and Oraculum (`0a27e884…`) sessions are never targets, never steered.
- No terminal injection or send-keys of any kind; no UI-parser readiness (screen text is never
  a readiness signal); no credential inspection; no permission/model overrides
  (`--dangerously-*`, `--approve-for-me`, `-a never`, `--model` are forbidden on the target);
  no headless/API fallback (`codex exec`, `claude -p`) as a substitute for the living session;
  no unattended watcher; no cross-host work; no daemon started that claims the working sessions.
- Transcript pickup stays operator-signalled, public-text, read-only evidence — never a carrier.
- Old bed `nablarva-01-design/` and its receipts stay intact; commit, push, prune, preservation
  authority remain separately owed (its `raw/promotion-manifest.md`).
- `/home/hruzam/unikuklatrix/nablarva/.hlm/` sealed. `runbook-tool-00` is not engaged by this bed
  (browser untouched) — no Trajectory timing dependency here.
- Flag L3/L4/L6/L9′/L12 bind. L4 is untouched by design: native only. Higher mathematics parked.

## prompt-0 — oraculum / cSharp

You are `oraculum`. Read the project chain (`AGENTS.md` → `flag.md` → `pulse.md` →
`PROJECT.yaml`), then this RUNBOOK, `STATUS.md`, the founding reference and VERDICT 01 of
bed 01, and the shared law below. On recovery, STATUS first; reconcile disk before any dispatch.

Write POINT 01 to the existing `cartan` session: read-only native preflight + an executable
qualification plan with the operator-hands steps marked. On RETURN: resolve every cited path,
@assay-rerun the safe commands, @epoch-verify any vendor claim that decides a step, @janus
before the VERDICT; do not repair Cartan's artifacts. Then compose `pad.1-b-entry.md` from the
audited plan, write its GLOSS notes, and ask majkee to arm (P2). Drive the sitting one step at a
time; distil to the VERDICT; ask for GO or STOP only when the package is ready; record the
decision verbatim. Executor grades: reruns → @assay; vendor facts → @epoch; melts → @field;
challenge → @janus; no coding grade for the head.

## prompt-1 — cartan / technical lead

You are `cartan`, majkee's existing independent Codex session, not Oraculum's child. Read the
project chain, this RUNBOOK, `STATUS.md`, the founding reference, VERDICT 01, and the POINT
majkee carries. Resolve your seat first (thread id ending `c57d8`); a mismatch stops the cycle.
Write only the paths the POINT names and one six-field RETURN; never STATUS. Separate observed
facts from proposals; preserve disagreements as curvature. Establish, from installed interfaces
and current official sources: the route from `codex queue` / app-server to a living session
(daemon, socket, `--remote`), session identity vs runtime incarnation and how each is observed,
observable permissions, usage-path evidence, acceptance conditions, positive and negative tests,
recovery rules, and every operator action required. No native send in P0. Autonomous
engineering is yours; the operator's hands are used only where the plan marks them.

## prompt-3 — majkee / arms, sits, gavels

Carry absolute POINT paths, never content. Open one named disposable Codex session in a scratch
workspace when the head asks (P2), approve activation per sitting against the exact target the
head names, sit the PAD one step at a time, approve or refuse the labeled characterization test,
and record GO or STOP against the qualification VERDICT. Your learning file:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/GLOSS.nablarva.md` §nablarva-02.

## References — shared law

- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `res/csharp-head-protocol.md` · `res/research.md`
- `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` · `bus/GUIDE.md` · `PAD/GUIDE.md` · `gloss/GUIDE.md`
- `/home/hruzam/reposoma/raw.guides/tunnel/GUIDE.md` · `/home/hruzam/ia-sync/HANDSHAKE.md` §Delivery rule
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-01-design/raw/design.r1.md` §Native/reuse evidence · §Uncertainty after submission · §Acceptance test (B entry · B pass · negative cases)
- Vendor pages verified 2026-09-12 (VERDICT 01 §Claim verification): app-server, non-interactive mode, CLI reference, cross-session messaging, hooks#stop, channels.

## What closes this gate

One qualification VERDICT on disk — positive case and the four negative cases (wrong/stale
target · replacement · duplicate attempt · interruption after possible submission) plus
busy/approval behavior, each with evidence and counts — and majkee's GO or STOP recorded
against it in STATUS.

## Deliberately out of scope

Browser or binding-record construction, deployment, Claude-side activation, targeting the
working sessions, any L4 exception, unattended operation, cross-host, savings claims.
