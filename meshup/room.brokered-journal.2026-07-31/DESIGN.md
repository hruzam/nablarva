# DESIGN — room.brokered-journal.2026-07-31

`scope: the production room — broker + append-only journal + adapter-owned PTY sessions + cursor projections (stage 1 → stage 2). Broker and its CLI = stridulatrix (L13).`
`status: live · S1–S8 locked (triad 2026-07-31) · hybrid Y+Z selected 2:1 · name stridulatrix locked 2026-10-01 · full design = nablarva-03-app-architecture's gate · origin 2026-07-31`
`sources: raw.nablarva/ (prefix rule) — cite, never copy. Composed from cards A, D, E + design-chapters §3.7 (10-01).`

## Shape

`stridulatrix` (was `larvad`): broker + append-only NDJSON journal + adapter-owned PTY sessions + sparse cursor projections; Unix socket same-host, SSH to one central broker cross-host (S7).
— `raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md:25` · `01_ARCHITECTURE_ROOM_AND_BROKER.md:28`

Journal has two projections: **braid** = raw interleaved audit trail, **book** = chapter-folded reasoning view; book derived from braid, braid never destroyed. (Cartan RETURN 01, 2026-10-01: placement in `room` confirmed — the braid is the journal.)
— `raw.nablarva/nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md:161-163`

**stridulatrix — name + boundary (L13, chapter 3.7, 2026-10-01):** Latin-style agent noun from *stridulate*, `-trix` = she who does it; chosen over larvad/larva and stridulator to survive voice input (voice test passed 10-01). Single writer of the journal (S1), per-participant cursors (S2), delivery through each adapter's own PTY (L3), never send-keys (L4). **Owns everything that writes into sessions**, including the onion study's context bus (ch. 6) — and with it the open question *who writes the PreCompact checkpoint* (lab h5). Reads termpanum's state events from its own cursor; no pipe to name. Lifecycle (docket 4) and journal store (docket 5) stay open. Commands: one family under the claviature rule; prefix open (`sx` is taken in Arch's repos).

## Phases

| phase | origin | state | source |
|---|---|---|---|
| X — primary-larva file-ledger room, cooperative convention, fails soft | 2026-07-31 | superseded (2:1 vote) | `oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` · `_preflight/task.T3-T4.orchestration-fork.md:38` |
| Y — larvad CREATURE: static binary, PTY adoption, structural turn-quota, fails hard | 2026-07-31 | folded into hybrid | `oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` |
| Wave hybrid V1 — closer to Y, Python-stdlib candidate, NDJSON events, larva-agent-{claude,codex} adapters | 2026-08-05 | selected direction | `oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` · `03_COST_COMPLEXITY_AND_STAGED_DECISION.md` |
| Braid-and-Book journal projections | 2026-08-01 | live stone | `nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md` |
| Four-phase blind triangulation as consultation lease | 2026-07-31 | Z novel organ 2 | `oraculum-basic-triangulation/triad.comparison.2026-07-31.md` |
| Two-lane evidence channel (conversation vs machine events) | 2026-08-05 | fork A, open | `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md:226` |
| Adapter capability handshake | 2026-08-05 | post-V1 | `oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md:4.15` |
| **stridulatrix** — name, boundary, owns the writes + context bus | 2026-10-01 | locked (L13); design → session 03 | `.dev/session/nablarva-X0-restarted/raw/design-chapters.for-cartan.2026-10-01.md` §3.7 |
| L14 D1/D2 — PTY base layer; files are the spine | 2026-09-30 → 10-02 | locked | `.dev/session/flag.md` L14 |
| majkee's notebook sheets 2026-07-30 — the operator's seed drawing (clipper · roller · composer · release/submit per system) | 2026-07-30 (photos 09-29) | operator substrate, kept whole | `raw/notebook-2026-07-30/` |

## Records, not design

`oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` (session close) · `nablarva.wave.full-report.2026-08-05.md` (concat of 01–07) · `brief.triangulation.2026-07-31.md` (sealed Z brief) · `06_ORACULUM_TRANSMISSION.md` · `07_AI_HANDOFF.md` (synthesis chapters).

## Boundaries

stage 1 · stage 2 (S7) · stage 3 (stridularium is the door; the room is what it opens onto) · broker/room · naming (L13) · LAB (termpanum feeds states into the journal; the room never reads screens). Locks live in `.dev/session/flag.md`; this file does not re-litigate them. Full architecture (homes, lifecycle, install, first prompt/reply slice) = `nablarva-03-app-architecture` — which, as of 2026-10-02, has not yet read L14 or the 09-30 stream (POINT 03 to Cartan).

## Sources (14 archived + 4 own)

- raw.nablarva/oraculum-basic-triangulation/seed.oraculum.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/brief.triangulation.2026-07-31.md
- raw.nablarva/oraculum-basic-triangulation/00_README.md
- raw.nablarva/oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md
- raw.nablarva/oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md
- raw.nablarva/oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md
- raw.nablarva/oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md
- raw.nablarva/oraculum-basic-triangulation/07_AI_HANDOFF.md
- raw.nablarva/oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md
- raw.nablarva/oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md
- raw.nablarva/_preflight/task.T3-T4.orchestration-fork.md
- raw.nablarva/nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md
- raw/notebook-2026-07-30/IMG_20260929_055330.jpg · IMG_20260929_055444.jpg · IMG_20260929_055516.jpg — majkee's notebook sheets of 2026-07-30 (SESSION/CLIPPER/ROLLER/COMPOSER · processor sheet · features sheet); operator substrate; git mv from the closed 03 bed 2026-10-05
- raw/notebook-2026-07-30/reading.notebook-2026-07-30.md — Cartan 2026-09-29: SHA-256 + transcription receipt for the three sheets (their text layer); git mv, history preserved

Pointer: .dev/session/nablarva-X0-restarted/raw/design-chapters.for-cartan.2026-10-01.md §3.7 (stays with Cartan's input)
