# Decision package r2 — architecture-X0-spine-and-skin (delta over r1)

`author: oraculum(arch-X0) · 2026-10-24, after the deck closed (X0-7 landed 11:35 CEST) · for majkee · r2 is a DELTA: r1 §1–§3 (problem, facts F1–F14, uncertainties, alternatives A–D, recommendation A) stand unchanged and are not repeated; only what the seven answers moved is rewritten here · source of every change: raw/answers.majkee.deck.2026-10-24.md (verbatim) · nothing here is a lock; bed slugs are PROPOSALS until majkee opens a bed`

## 0. What the deck decided (X0-1…X0-7, all = a)

| block | decision | moves in the package |
|---|---|---|
| X0-1 | spine slice is the first **construction** ("from the elementals, not the jump") | §3 recommendation A confirmed; §4 stands |
| X0-2 | termbrana/stridulatrix split recorded in ARCHITECTURE r8 as `said: majkee` | §5 docs bed content; F5 cited from r8 once written |
| X0-3 | registry + observation record = **new shared-substrate component**, own L18 folder, disk name TBD after sweep, interim steward = spine bed's head | §4 scope items 1, 3 get an owner; U-a closed by admission; **U-steward** opened |
| X0-4 | home `<project>/.nablarva/` + `~/.nablarva/`, every path via the config rule | §4 scope item 2 concrete; U-b closed; U-h narrows to "mechanism" |
| X0-5 | bookkeeping docs bed **now**, before the spine bed | §5 reorder: docs bed 1, spine 2 |
| X0-6 | skin requirements harvested during the slice; instarmux sitting after | §4 scope item 6 gets a file shape; §5 position kept |
| X0-7 | muticula sleeps until registry + notifier; worktrees interim (L12) | §5 position kept; pulse-row shape open (§7) |
| X0-7 rule | **X in a slug = nabLarva generation marker** (restart to order/system; tmux/PTY narrative); every organ's next bed carries X | all §5 slugs re-proposed under X |

## 4. Scope and acceptance evidence for ONE planning RUNBOOK (r2)

**Bed (proposed slug, majkee picks):** `nablarva-X5-spine-slice` — cross-organ, so under the `nablarva-X` line (X4 is the last used). Head: a fresh cSharp. This bed (arch-X0) hands it the RUNBOOK substrate; it does not run it.

**Gate (one line, unchanged from r1):** majkee records GO or STOP on a witnessed read-only spine slice: one producer writes the shared observation record in per-writer files at a config-resolved home, the address registry holds one seat-addressed entry per pane written by ovitmugen on `ov-up` and surviving `ov-down`/`ov-up`, a second client reads both to show one derived state per seat, and an independent witness confirms that no byte was written into any session.

**In scope (r2 — changes marked ►)**
1. Address registry — contract + first writer (ovitmugen on pane creation) + first reader (a status reader or termbrana's target pick, whichever is cheaper); seat-addressed (durable identity), not PID/pane. ► Lives in the **shared-substrate component** (X0-3): own thin folder per L18; disk name chosen in the bed after the mandatory duplicate/cross-interference sweep (AGENTS.md naming law); interim steward = the bed's head; the bed's STATUS carries `steward: interim (U-steward)`.
2. Config rule — the mechanism that resolves the registry and record homes: a settings file, no literal path in any script. ► Home per X0-4: project-scoped state in `<project>/.nablarva/` (registry, record segments, bed-local settings), machine defaults in `~/.nablarva/`; a `.gitignore` line for `<project>/.nablarva/` is part of the slice.
3. Shared observation record — layout only: per-writer append-only files, one serialized writer each (Houston c1), segment-able with a head/index readable in ≤80 lines (U-g), envelope-agnostic lines; **not** docket 8. ► Same component as item 1.
4. One producer — the cheapest honest one: a tmux `set-hook` writing to its own per-pane file, OR Package Q's collector if the termpanum line lands first (coordination row in STATUS). Unchanged.
5. One view — ovitmugen's sessions column or a tiny reader shows one derived state (active / idle by last-event age) from the record, not from tmux polling. Unchanged.
6. Lens-9 harvest — ► one append-only file `raw/skin-requirements.majkee.md` in the spine bed: one line per felt gap, majkee's voice, no analysis, no framework choice; the head asks "one line for the skin note?" whenever majkee says the view is not enough. Input to the later instarmux sitting brief.
7. Houston `card: consult` at closure (implements a shared layer → L21 (2): its own release = this bed's GO; touches L17). Unchanged.

**Out of scope (unchanged):** delivery of any kind (HELLO, doorbell, stridulatrix) · envelope choice (docket 8) · router (`nablarva <tool>`) · dashboard · Zellij loader · muticula · skin framework · phone organ · continuity mechanism · ► naming the real steward (U-steward, majkee).

**Acceptance evidence (unchanged E1–E7; ► E1 now reads against the X0-4 home):**
- E1 `grep` over the slice's scripts finds no literal registry/record path; the resolved path (`<project>/.nablarva/…` or `~/.nablarva/…`) comes from the settings file (command + output).
- E2 `ov-up <slug>` → registry gains N seat entries; `ov-down` + `ov-up` → same seat ids, new pane ids (diff of two registry snapshots).
- E3 record directory: one file per writer; a mechanical check shows no two writers share a file (writer id in filename and in every line).
- E4 reader output shows a state per seat derived from the record; killing the producer changes the state without touching tmux state.
- E5 witness: tmux `pipe-pane`/hook audit shows zero `send-keys`/`paste-buffer`/`load-buffer` into any session pane for the slice's lifetime (L4, L17).
- E6 head/index of the record readable with `head -80`.
- E7 Houston closure consult: fits or stretches with constraints carried to flag/dock; no breaks.

## 5. Ranked next beds (r2 — reordered by X0-5, slugs under the X rule)

1. ► **docs / bookkeeping bed** — proposed slug `nablarva-X5-bookkeeping` (or `architecture-X1-bookkeeping` if majkee wants it under this line). Delta-driven, one evening, majkee commits. Content: ARCHITECTURE r8 — C1 (§2.5/§4.7/§9 cite L21, stale P5 text dropped) · M3/M4/C4 (dock 2026-10-24) · §7 organ table: reposoma OUT · stridularium "retired as cultural name" (docs edit + **one flag line by majkee**, L13) · Antensor = translator termpanum→body · instarmux = skin · termbrana/stridulatrix split as `said: majkee` (X0-2) · shared-substrate component + interim steward (X0-3) · substrate home + config rule (X0-4) · Nablarva Boost "working name, rename pending" · PROJECT-DESIGN §3.4 removal + §3.8 touch · termbrana README C2. Gate: majkee GO on the diff.
2. ► **spine slice** (§4) — proposed slug `nablarva-X6-spine-slice` if the docs bed takes X5; otherwise X5. The first construction.
3. **termpanum line: Package Q** — already theirs (Cartan); coordinate the producer (scope item 4). No slug proposed by this head.
4. **instarmux sitting brief** — after `skin-requirements.majkee.md` exists; proposed slug `instarmux-X0-sitting-brief`.
5. **stridulatrix** — HELLO design on the registry + record; opens relay-00-research for real; U-send-keys decided on slice evidence; U-vendor-spawn Epoch pass as input. Proposed slug `stridulatrix-X0-hello`.
6. **muticula** — asleep until registry + notifier exist; worktrees interim (L12). Next bed when it wakes: `muticula-X0-<slug>` (X0-7 rule). `muticula-01-qualify` parked.

Slug rule applied: organ-scoped beds = `<organ>-X<n>-<slug>`; cross-organ beds = `nablarva-X<n>-<slug>`; `architecture-X<n>` = this briefing line. Proposals only.

## 6. The deck — closed

All seven blocks answered a; verbatim in `raw/answers.majkee.deck.2026-10-24.md`. The r1 §6 texts are the record of what was asked.

## 7. Not decided by this package (named, not dropped)

U-send-keys (majkee, on slice evidence) · docket 8 · U-vendor-spawn · U-continuity (incl. rotation of long canon files) · **U-steward** (real owner of the shared-substrate component; interim = spine bed's head) · stridularium's new name and Boost's new name (one-cell edits later) · the phone organ (backlog) · Zellij loader · Field Q5 (Cartan's bed) · **muticula-01-qualify pulse row: keep-and-reword or remove** (majkee; canon touch) · the shared component's disk name (sweep in the spine bed).

## Addendum A — slugs picked (majkee, 2026-10-24 11:43 CEST)

> architecture-X1-bookkeeping and spine takes X5

§5 r2 slugs resolved: bed 1 (docs/bookkeeping) = **`architecture-X1-bookkeeping`** — continues this briefing line; bed 2 (spine slice, §4) = **`nablarva-X5-spine-slice`**. The "X6" alternative in §5 is void. Other §5 slugs (instarmux-X0-…, stridulatrix-X0-hello, muticula-X0-…) remain proposals.
