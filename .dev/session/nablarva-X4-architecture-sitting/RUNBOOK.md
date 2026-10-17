# RUNBOOK: nablarva-X4-architecture-sitting

```yaml
goal: >
  The first real whole-animal architecture doc exists as a reviewed draft in this bed, written by
  Houston on its sitting card from majkee's answered gavels — X1 check 4 (Houston sitting).
gate: >
  majkee GO on raw/ARCHITECTURE.draft.md, ready to promote to docs/ARCHITECTURE.md.
participant_1: [oraculum, {brand: claude, model: runtime-selected, effort: high}, host: hruzam-120922, role: "main session · cSharp head · carrier · status_owner · commits"]
participant_2: [houston, {brand: claude, model: opus, effort: high}, host: hruzam-120922, role: "card: sitting · main session launched by majkee (claude --agent houston, cwd nablarva) · drafts in raw/ only"]
participant_3: [cartan, {brand: codex, model: gpt-6.1-sol, effort: high}, host: hruzam-120922, role: "tunnel thread 01a14731-648c-7a60-a34f-350278fe5897 · review of the drafts (one RETURN)"]
participant_4: [assay, {brand: claude, model: sonnet, effort: high}, host: hruzam-120922, role: "spawn of oraculum · fresh-eyes witness · one prompt per row · never fixes"]
participant_5: [polyp, {brand: codex, model: runtime-selected, effort: runtime-selected}, host: hruzam-120922, role: "majkee's Codex shell running $polyp · drives raw/gavels.X4.2026-10-17.md human-driven · writes only its report blocks + the one sink named there"]
participant_6: [majkee, {brand: human, model: not-applicable, effort: not-applicable}, host: hruzam-120922, role: "gavel · answers the deck · launches the living Houston · opens the tunnel table · GO"]
status_owner: oraculum
head_note: >
  cSharp protocol (~/reposoma/raw.guides/runbook/res/csharp-head-protocol.md) — oraculum authors
  by dispatch and stays as navigator, carrier and status_owner. Bed opened by trajectory(bed) on
  oraculum's dispatch, majkee GO 2026-10-17 ("bed X4 ok, go").
observations_read: >
  [.dev/observations/nablarva-X1-architecture.trajectory.2026-10-08.md (headings T12–T23, T23 in
  full), .dev/observations/codex-houston-held-seat.cartan.2026-10-13.md] — read by trajectory(bed)
  at authoring; the three nablarva-X0-restarted.* files were read by X1's author (X1 RUNBOOK).
opened: 2026-10-17 · predecessor line nablarva-X1-architecture (this bed = its check 4)
```

## Why this session exists

X1's gate needs a real `docs/ARCHITECTURE.md` written by Houston from its canonical homes. Homes,
install and the wrapper move are done (X1 STATUS). What is left is the drafting itself, which the
Houston addendum §2 sends to a sitting's own bed with one gate. This is that bed. It produces a
draft and nothing durable; promotion is a separate row after the gate.

## Sequence under the gate (in order)

| # | row | seat | lands |
|---|---|---|---|
| 1 | Gavel deck answered — confirm or strike the leans, then majkee walks `raw/gavels.X4.2026-10-17.md` one unit at a time | oraculum (leans) → majkee + polyp | report blocks in the deck; the distilled answers in the GAVELS block of `raw/prompt.sitting.2026-10-17.md` (the deck's one sink) |
| 2 | Sitting prompt run — majkee pastes `raw/prompt.sitting.2026-10-17.md` into a fresh `claude --agent houston` (cwd `/home/hruzam/unikuklatrix/nablarva`) | majkee → houston | conversation |
| 3 | Arc + 2–3 alternatives with constraints; Houston waits for majkee's pick | houston → majkee | `raw/arc.md` (pick recorded `said: majkee`) |
| 4 | Drafts | houston | `raw/ARCHITECTURE.draft.md` · `raw/wrapper-thinning.diff` · `raw/lock-proposals.md` · `raw/card.sitting.draft.md` (only if G8 = yes) |
| 5 | Review over the tunnel — one ask naming exactly what to read | oraculum (carrier) → cartan | `_bus/NN.cartan.return.md` (carrier mints NN) |
| 6 | Witness — mechanical claims only (below) | assay (spawn of oraculum) | `_bus/NN.assay.verdict.md` |
| 7 | GO | majkee | gate closes; oraculum rewrites STATUS |

Corrections after 5 or 6 are a new explicit Houston invocation (L16.8), never a self-fix by the
reviewer.

**After the gate — promotion (separate row, not under this gate):** oraculum holds the closure pen
(L16.12): `raw/ARCHITECTURE.draft.md` → `docs/ARCHITECTURE.md`; majkee commits the wrapper diff;
oraculum carries `raw/lock-proposals.md` to the flag docket; a card draft goes to the germline-01
forge bed (`~/ia-sync/.dev/session/germline-01-builds-and-deploy/`), never in place. Then X1 check 4
is done and X1 check 5 (audit from the canonical card) follows in X1.

## prompt-0 — oraculum

```text
Resume nablarva-X4-architecture-sitting as cSharp + carrier. Read /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/STATUS.md, then this RUNBOOK. Row 1 first: read raw/gavels.X4.2026-10-17.md, confirm or strike every `lean: oraculum` marked "drafted by trajectory", then hand the deck to majkee for $polyp. Do not run Houston yourself; majkee launches it. Cartan only over the tunnel, after majkee opens the table on this bed. Assay witnesses row 6.
```

## prompt-1 — polyp (majkee's Codex shell)

```text
$polyp /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/raw/gavels.X4.2026-10-17.md — human-driven mode. STATUS: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/STATUS.md (read only; status_owner is oraculum).
```

Polyp's write boundary here: the deck's `>MAJKEE report` blocks, and after the last unit the GAVELS
block of `raw/prompt.sitting.2026-10-17.md` (the one approved sink). This RUNBOOK does **not**
authorize polyp to advance STATUS; it returns the result to oraculum.

## prompt-2 — houston

The prompt is `raw/prompt.sitting.2026-10-17.md` (pasted whole, after the GAVELS block is filled).
Launch: `cd /home/hruzam/unikuklatrix/nablarva && claude --agent houston`.

## prompt-3 — cartan (tunnel ask, one line + paths)

```text
oraculum(carrier) · X4 row 5 · review /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/raw/{ARCHITECTURE.draft.md,wrapper-thinning.diff,lock-proposals.md} against the GAVELS block in raw/prompt.sitting.2026-10-17.md and flag L16; read nothing else unless a cite sends you. RETURN with the six headings to _bus/<NN>.cartan.return.md.
```

## prompt-4 — assay (witness)

```text
Witness X4 row 6. Bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/. Check only: (1) every repo path cited in raw/ARCHITECTURE.draft.md and raw/lock-proposals.md resolves; (2) `git -C /home/hruzam/unikuklatrix/nablarva apply --check <bed>/raw/wrapper-thinning.diff` passes; (3) after a scratch apply, every pointer that pulse.md or a live STATUS cites into PROJECT-DESIGN.md still resolves; (4) every claim carries one of said:/inferred:/locked:/unknown: and no `locked:` cites an L-id that flag.md lacks; (5) `git status --short` shows Houston wrote nothing outside <bed>/raw/. PASS/FAIL with evidence to _bus/<NN>.assay.verdict.md. Never fix.
```

## Known constraints + destructive holds

- **Houston's pen:** new files in `raw/` of this bed only. Never `docs/`, `.dev/session/flag.md`,
  `/PROJECT-DESIGN.md`, `PROJECT.yaml`, `AGENTS.md`, `~/.germline/`, this bed's RUNBOOK or STATUS, or
  another head's STATUS. A write outside `raw/` is answered `out of card:` (binding.claude.md).
- Houston's Claude wrapper has Read · Grep · Glob · Write · Agent — no shell, no Edit. The thinning
  diff is hand-written; assay's `git apply --check` is its test.
- **The GAVELS block is binding** on the sitting. An unanswered block means the sitting does not
  draft.
- **Claim discipline (L16.11):** `said:` · `inferred: <seat>` · `locked: L<n>` · `unknown:` — never
  merged. Pending docket items block their dependents (flag header); the draft decides none of them.
- **Live citations into the wrapper:** pulse.md's `ovitmugen-01-basement` gate cites
  `PROJECT-DESIGN.md § KEYS CODE`. The thinning diff must leave that pointer resolvable (or the head
  coordinates with that bed's head before commit).
- **Tunnel:** majkee opens the table. Cartan review uses the existing X1 vault (thread 01a14731 is bed-agnostic; no rebind): POINT/RETURN files live in this bed's _bus/ and the tunnel message names their absolute paths. TUI or tunnel, never both; one turn per vault; context routine per X1 STATUS holds
  (T23).
- No commit by any seat except oraculum; majkee pushes (plain pull/push on `core`, never rebase —
  L12). `.hlm/` and `.majkee/` unread.
- Nothing from this bed is promoted to `~/ia-sync/` or `~/.germline/` (L6; card edits = germline-01
  forge bed, majkee 2026-10-10).
- **GLOSS:** when a sitting looks like it needs explaining, the driver ASKS "record
  GLOSS.<slug>.md?" — never assumes (AGENTS.md; `~/reposoma/raw.guides/gloss/GUIDE.md`).

## Acceptance evidence

- `raw/ARCHITECTURE.draft.md` exists, follows the answered GAVELS, every claim tagged.
- Cartan RETURN in `_bus/` with its findings folded or answered.
- Assay VERDICT PASS (or PASS-WITH-FINDINGS accepted by majkee) in `_bus/`.
- majkee's GO, recorded by oraculum in STATUS `checkpoint:`.

## References (point, never copy)

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L3, L8, L11–L16; docket; O1–O4
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md` — check 4 and 5
- `/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md` — §1 map, §2 where sitting output lands
- `/home/hruzam/.germline/agents/houston/cards/sitting.md` — stub card
- `/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md` — L16 record (pinned `nablarva@2ae8636`): K1–K8, growth law, migration notes
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md` — J1, J2
- `/home/hruzam/reposoma/raw.guides/{runbook,status,PAD,bus,gloss}/GUIDE.md`
- `/home/hruzam/ia-sync/codex/skills/polyp/SKILL.md` — the deck driver

## What this session deliberately does not do

- Write `docs/ARCHITECTURE.md`, the wrapper, flag, PROJECT.yaml or AGENTS.md (promotion row and
  the keeper's commit do that).
- Decide docket items, O1–O4, or the J2 saddle reconciliation.
- Run the X1 check 5 audit.
- Build any organ code.
