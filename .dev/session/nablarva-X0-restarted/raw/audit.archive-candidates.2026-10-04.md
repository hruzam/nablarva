# audit — archive candidates · nablarva · 2026-10-04

`read-only; written by @Field (Claude Sonnet 4.6). Sources: flag.md · pulse.md · AGENTS.md · meshup/REGISTRY.md · STATUS files · raw.guides/runbook/GUIDE.md · raw.guides/status/GUIDE.md.`

## A — flag.md

| item | verdict | evidence |
|---|---|---|
| L1 | LIVE | flag.md:10 |
| L2 | LIVE | flag.md:12 |
| L3 | LIVE | flag.md:14 |
| L4 | LIVE | flag.md:20 |
| L5 | LIVE | flag.md:23 |
| L6 | LIVE | flag.md:27 |
| L7 | LIVE | flag.md:30 |
| L8 | LIVE | flag.md:32 |
| L9 | LIVE (pulse-role sub-clause only: SUPERSEDED-BY L9') | flag.md:35; L9' at flag.md:61 |
| L10 | LIVE | flag.md:41 |
| L11 | LIVE | flag.md:45 |
| L12 | LIVE | flag.md:74 |
| L13 | LIVE | flag.md:82 |
| L14 | LIVE | flag.md:88 |
| L9' | LIVE | flag.md:61 |
| thresh-domain | LIVE | flag.md:114 |
| thresh-orch | LIVE | flag.md:115 |
| thresh-robust | LIVE | flag.md:116 |
| docket 1 | LIVE — note: L14 D2 "file plane is the spine; no transport is truth" (flag.md:96) settles "accept 2:1 and skip" directionally; no formal docket-1 gavel yet | flag.md:120, flag.md:96 |
| docket 2 | LIVE | flag.md:121 |
| docket 3 | LIVE | flag.md:122 |
| docket 4 | LIVE | flag.md:123 |
| docket 5 | LIVE | flag.md:124 |
| docket 6 | LIVE | flag.md:125 |
| docket 7 | CLOSED (by L13, majkee 2026-10-01) | flag.md:126 (item); flag.md:82 (L13: "docket 7 closed") |
| docket 8 | LIVE — pending EVENTS map (opened 2026-10-02) | flag.md:128 |
| O1 | LIVE | flag.md:135 |
| O2 | LIVE — L14 D5/D6 (flag.md:99-108) establishes phone-as-thin-lens lean; L14 D1 "vendor doors … weather, parked" (flag.md:93); Tailscale vs per-host restriction not gaveled | flag.md:137 |
| O3 | LIVE | flag.md:139 |
| O4 | LIVE | flag.md:141 |
| untabled-1 | LIVE (mathematical engine research) | flag.md:149 |
| untabled-2 | LIVE (brick-factory stock) | flag.md:150 |
| untabled-3 | LIVE (rough file lot) | flag.md:151 |
| untabled-4 | STALE-POINTER — cites `meshup/nabla_drafts/report.seam-probe.2026-08-01.md`; `meshup/nabla_drafts/` dir does not exist; resolving path (per REGISTRY.md sources for lab design): `raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` (confirmed on disk) | flag.md:152-153 |
| out-of-scope-1 | LIVE | flag.md:156 |
| out-of-scope-2 | LIVE | flag.md:157 |
| out-of-scope-3 | LIVE | flag.md:158 |

Special notes:
- **Docket 7 vs L13:** docket 7 asks "larvad/larva vs stridulator/stridularium organ mapping"; L13 (flag.md:82) settles it ("docket 7 closed"). Docket 7 (flag.md:126) is CLOSED. AGENTS.md:11-12 and :73 still reference docket 7 as open — see C.
- **L9 pulse clause vs L9':** L9 (flag.md:37-38) originally made pulse the "single canonical doing-state"; L9' (flag.md:63-64) narrows it to "bounded router." All other L9 clauses remain locked; only the pulse-role sub-clause is superseded.
- **Docket 1 vs L14 D2:** "Only bad transports exist today → the file plane is the spine" (flag.md:96) answers the 2:1 question of docket 1, but no formal gavel closes docket 1. A single-line majkee gavel would clear it.
- **O2 vs L14 stridularium lean:** L14 D5/D6 and L13 together define the phone as a thin lens sending commands through a host-side engine; the specific cross-host transport (Tailscale vs per-host restrictions) is still open in O2.

## B — pulse.md

| session | bed exists? | STATUS updated | gate state | verdict | evidence |
|---|---|---|---|---|---|
| nablarva-02-pipe-qualification | YES | 2026-09-14T15:39+02:00 | open — awaiting majkee open_approval for sitting 1 | ROUTER-LIVE | STATUS.md:2 (yaml updated) |
| ovitmugen-01-basement | YES | 2026-10-02 | open — awaiting majkee live walk on office | ROUTER-LIVE | STATUS.md:4 |
| muticula-01-qualify | YES | 2026-10-02 | open — awaiting Cartan verdict on POINT 03 | ROUTER-LIVE | STATUS.md:3 |
| none — 03-tunnel CLOSED (PASS) | N/A | N/A | CLOSED | ROUTER-STALE — gate closed, evidence file exists; runbook/GUIDE.md §"On gate closure" says "remove the session from pulse.md's router line"; row should be removed; no new rule required | pulse.md:11; GUIDE.md:204 |

nablarva-01-design row: not present in pulse.md; bed not on disk. Correctly pruned.
Also noticed: nablarva-03-app-architecture bed EXISTS (STATUS updated 2026-09-29, gate OPEN, in_flight: "candidate ready for independent challenge"), NOT in pulse.md — candidate ROUTER-ORPHAN; pulse.md:6 lists no row for it; STATUS: .dev/session/nablarva-03-app-architecture/STATUS.md:1.

## C — AGENTS.md stale references

- AGENTS.md:11-12 — "which organ carries the name is gavel docket item 7. Not the whole." — SUPERSEDED by L13 (flag.md:82, gaveled 2026-10-01); stridularium is now definitively the phone app.
- AGENTS.md:59 — "`GEMINI.md` — retired Bluebottle stub (pre-project era); superseded by this file." — file exists on disk (confirmed); line correctly labels it superseded; no path is broken, but the stub persists on disk without a removal record.
- AGENTS.md:73 — "docket item 7-adjacent" — stale framing post-L13; the Cluster A / stridularium feed boundary now has a resolved name (stridularium = phone app, L13) and no longer requires the "adjacent" hedge.

## D — Counts

flag.md: 35 LIVE · 2 non-LIVE (docket 7 CLOSED; untabled-4 STALE-POINTER) · 37 items total.
pulse.md: 3 ROUTER-LIVE · 1 ROUTER-STALE · 4 rows (nablarva-01-design row already removed).

## E — Archive rule options

*Listed without recommendation.*

**(1) Append-only + one-line marker + text extracted to `.dev/archive/flag.<item>.<date>.md`.**
Cost: creates a new archive dir; requires consistent extraction discipline; each move is a write.
Breaks: L9 append-only if the original block is removed; session-history citations lose their anchor unless the one-line marker quotes the archive path; prefix rule does not apply (flag items are not substrate files, no raw.nablarva/ analogue). A 3-line `.dev/archive/README.md` would suffice as an index.

**(2) Append-only; no moves; `## Archived index` section at end lists superseded items with date and cross-reference.**
Cost: minimal — one appended section; no external files.
Breaks: nothing; append-only law L9 preserved; all existing citations remain valid; index is additive. No README needed — the section IS the index.

**(3) Pulse rows for closed gates simply removed.**
Cost: zero beyond the edit.
Breaks: nothing — pulse.md is a volatile bounded router (L9'); GUIDE §"On gate closure" already mandates removal. The 03-tunnel row is an existing violation of the current rule, not a gap. No new rule needed; a 3-line README would add no value here.

**(4) Periodic reconciliation pass with a fixed trigger (e.g., every gate closure) vs ad hoc.**
Fixed trigger — cost: adds ceremony to every closure; needs majkee gavel for the process rule itself; risks becoming boilerplate.
Ad hoc (current state) — cost: relies on challenge seats (@Janus, @Field) noticing drift; demonstrated here to work but leaves gaps between passes.
Both: a 3-line `.dev/archive/README.md` could record the trigger and ownership without creating a standing process file, consistent with the "no standing plan.md" doctrine.
