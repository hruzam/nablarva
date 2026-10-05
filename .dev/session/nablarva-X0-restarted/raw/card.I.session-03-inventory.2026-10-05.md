# card.I — session-03 inventory, M1 closure
`date: 2026-10-05 · scribe: @Field · rule: M1 majkee 2026-10-05 · session: nablarva-03-app-architecture`
`S = /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-03-app-architecture`
`JPG sizes from reading receipt (Glob has no sizes): 055330=2,016,186 B · 055444=2,210,917 B · 055516=1,965,647 B`

| # | path (rel. S/) | author/seat | date | class | one-line content | unique? | M1 verdict | evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | RUNBOOK.md | Majkee (opener; no frontmatter author) | 2026-09-29 | SESSION-FRAME | Gate def., two participants, two prompts, acceptance criteria, references | gate text duplicated in STATUS:15-16 | HISTORY-ONLY | RUNBOOK:3-8 |
| 2 | STATUS.md | Cartan/Codex | 2026-10-04 | SESSION-FRAME | Checkpoint, attachment record (Flight seat), in-flight state, recovery probe | no | HISTORY-ONLY | STATUS:1-6 |
| 3 | _bus/00.flight-executioner.return.md | flight-executioner (Claude Opus 5.5, Majkee MANNED) | 2026-09-29 | BUS | REVISE(small): fix slice ordering; zsh scope already wired+broken (not unchecked); manual-recipe check still runs on update | partial — findings folded into architecture.working.md per 00.cartan.verdict:7 | HISTORY-ONLY | 00.cartan.verdict:7 |
| 4 | _bus/00.cartan.verdict.md | Cartan | 2026-09-29 | BUS | ACCEPT RETURN 00; slice scanner overlaps runbook.py:687 browser feature; source corrections integrated | no | HISTORY-ONLY | 00.cartan.verdict:6-8 |
| 5 | _bus/01.cartan.point.md | Cartan | 2026-09-29 | BUS | POINT: verify tunnel vs one-shot relay seam; gates + bounded read-set for Flight | no | HISTORY-ONLY | 01.cartan.point:19-27 |
| 6 | _bus/01.flight-executioner.return.md | flight-executioner (Claude Opus 5.5, Majkee MANNED) | 2026-09-29 | BUS | CONFIRM consultation/living-peer split; REVISE carrier map to two carriers: ephemeral relay + continuity tunnel | partial — folded into tunnel-consultation.2026-09-29.md per 01.cartan.verdict:7-8 | HISTORY-ONLY | 01.cartan.verdict:7-8 |
| 7 | _bus/01.cartan.verdict.md | Cartan | 2026-09-29 | BUS | ACCEPT carrier correction; HANDSHAKE "pending" countersign resolved at :166 (stale pointer, not missing action) | no | HISTORY-ONLY | 01.cartan.verdict:5-9 |
| 8 | _bus/02.cartan.point.md | Cartan | 2026-10-04 | BUS | POINT: compare arch. boundaries vs sessions 01/02 within L13/L14 addendum; RETURN not yet received | no | HISTORY-ONLY | 02.cartan.point:31 |
| 9 | raw/notebook-2026-07-30/IMG_20260929_055330.jpg | Majkee (operator) | 2026-07-30 (Taildrop 09-29) | OPERATOR-SUBSTRATE | Notebook: SESSION/CLIPPER/ROLLER/COMPOSER layout; INPUT/OUTPUT entity labels; sideways partial shot | bytes unique; described reading.notebook:22-24 | KEEP → room.brokered-journal.2026-07-31 as raw/ input | reading.notebook:15-17 |
| 10 | raw/notebook-2026-07-30/IMG_20260929_055444.jpg | Majkee (operator) | 2026-07-30 (Taildrop 09-29) | OPERATOR-SUBSTRATE | Processor sheet: OUTPUT A→BUFFER/COMPOSER, ROLLER private/dialog, TRANSLATOR, metadata/anchors | bytes unique; described reading.notebook:25-28 | KEEP → room.brokered-journal.2026-07-31 as raw/ input | reading.notebook:15-17 |
| 11 | raw/notebook-2026-07-30/IMG_20260929_055516.jpg | Majkee (operator) | 2026-07-30 (Taildrop 09-29) | OPERATOR-SUBSTRATE | Features sheet dated 2026-07-30: release/submit per system, per-recipient options, layers/channels, light panel | bytes unique; described reading.notebook:29-31 | KEEP → room.brokered-journal.2026-07-31 as raw/ input | reading.notebook:15-17 |
| 12 | raw/reading.notebook-2026-07-30.md | Cartan | 2026-09-29 | HEAD-WORKING | Provenance receipt for 3 JPEGs: bytes, SHA-256 hashes, visible-content transcription, architectural reading | SHA-256/byte data unique here; content derives from photos (rows 9-11) | HISTORY-ONLY | reading.notebook:1-7 |
| 13 | raw/review.claude.2026-09-29.md | Claude Opus 5.5 one-off CLI (Majkee requested) | 2026-09-29 | EXTERNAL-SEAT-INPUT | Independent arch. challenge: two BLOCKING findings (product-vs-harness; wiring contradiction); phase-0 proposal; cheapest alternative | partial — integration section folded into architecture.working.md:113-146 | KEEP → new design (nablarva app-architecture) as raw/ input | review.claude:1-14 |
| 14 | raw/tunnel-consultation.2026-09-29.md | Cartan | 2026-09-29 | HEAD-WORKING | Two consultation carriers (ephemeral relay vs continuity tunnel); property comparison table; tunnel limits; place in animal | no | HISTORY-ONLY | tunnel-consultation:1-3 |
| 15 | raw/workflow-reading.2026-09-29.md | Cartan | 2026-09-29 | HEAD-WORKING | Workflow episodes from 09-14/09-17 logs; three arch. boundary candidates compared; onion-instrument assessment | no | HISTORY-ONLY | workflow-reading:1-5 |
| 16 | raw/architecture.working.md | Cartan | 2026-09-29 (§1 premises 2026-10-04) | HEAD-WORKING | Full bounded-exchange-loop candidate: §§1-10, L13/L14 premises, 4 open decisions, 5-step contract | §1 L13/L14 premises live in flag.md and seam DESIGN; exchange contract + human-role table unique here (see §a) | HISTORY-ONLY | architecture.working:1-3 |

## (a) Content in `raw/architecture.working.md` §1 not already in meshup seam/lab/room DESIGN files

Three items absent from the REGISTRY descriptions of room/seam/lab designs and present only in session-03's working candidate:

1. **Animal ownership statement** (architecture.working.md:38-40): "nabLarva should own the continuity of an exchange: who addressed whom, what was released, what delivery evidence exists, which reply belongs to it, and what still needs attention." — room DESIGN owns broker/journal/PTY; seam DESIGN owns relay mechanism; neither names this as the animal's identity boundary.
2. **5-step bounded exchange loop contract** (architecture.working.md:59-85): specifies scope limits, round limits, no-unsolicited-discovery, and no-blind-retry as first-class animal invariants — seam DESIGN covers bonding/relay protocol at the transport level; this contract names who owns each arc and what the human must decide, absent from any existing DESIGN file.
3. **Event/human-role table** (architecture.working.md:92-98): maps five exchange events to the human's required action and the system's promise — absent from room/seam/lab DESIGN files, which describe mechanism rather than the human boundary per exchange event.

## (b) RETURN 00 and 01 conclusions; existence of RETURN 02

- **RETURN 00** concluded REVISE(small): the baseline shows the return/attention leg (~19 actions + 16 min lag) dominates the recorded exchange, so the first slice should target that leg rather than outbound send (~5 actions); the nablarva zsh scope is already wired in both host configs and deployed on office (not "unchecked"); manual recipes still run their `check` block before the manual/automatic branch on `update`.
- **RETURN 01** concluded CONFIRM the consultation/living-peer split; REVISE carrier mapping: consultation has two existing carriers — ephemeral `codex-run.zsh` relay for a fresh independent opinion, stored-thread `tunnel-codex.zsh` for continuity; prior documentation wrongly routed all second-opinion work to the tunnel.
- `_bus/02.flight-executioner.return.md` does **not** exist — confirmed by Glob (bus/ contains only 00 and 01 flight-executioner returns) and STATUS:36-39 ("no 02.flight-executioner.return.md observed").

## (c) Gate line from RUNBOOK.md, verbatim (RUNBOOK:7-8)

> Majkee records GO or STOP on a source-backed, independently challenged architecture blueprint covering animal/toolbox boundaries, code/config/data/runtime homes, delivery/install/wiring/admin lifecycle, and the first prompt/reply slice, with unresolved choices explicit.
