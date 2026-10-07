# closing receipt — nablarva-X0-restarted · DRAFT by oraculum(cSharp) 2026-10-07 · for majkee's KEEP / AMEND / RETIRE

`status: DRAFT — numbers from existing receipts only (raw/tunnel-turns/*.meta, _bus/, witness file, journal); finalized when the last slice lands`

## Gate checks (L16.13 + the discipline check)

| check | state | evidence |
|---|---|---|
| body matches L16 + record | PASS (frozen; checks 1–3 PASS; witness rounds 1–3) | README @ second/third freeze · `_bus/23.assay.return.md` · `raw/witness.claude.2026-10-07.md` |
| one real audit run, output classified | PASS — D-c audit (majkee-invoked, living route) → USEFUL ×6 · overreaching 0 · missing 2 | `raw/houston-audit.2026-10-07.{md,diff}` · `_bus/24.oraculum.return.md` |
| no authority boundary crossed | PASS — refused/escalated none in 8 tunnel turns; write checks clean ×3; audit applied nothing; one STATUS writer; Houston reported a falsified binding premise against its own card instead of hiding it | turn `.meta` files · `_bus/19/23.assay.return.md` · `_bus/20.*` |
| discipline KEEP / AMEND / RETIRE | **majkee's word** — facts below | this receipt |

## Carriage facts (the discipline under test: carrier · tunnel · bus · three living seats + gavel)

- Tunnel turns: **10** — 8 carrier (cycles 10+11, 13, 15, 16, 17, 18, 22 … ), 2 Atlas on slots majkee yielded (12, 15). Driver time ≈ 16 min total; longest single turn 6 m 02 s (rail cycle 13); shortest 13 s.
- Refused commands: **0**. Escalations: **0**. auto_review decisions requested: 0 (T11 honouring: inconclusive — no tunnel turn emitted a turn_context line).
- Recovery events: **1** — an earlier interrupted attempt (`01a110ec…`) before turn 1, not re-sent; recovered by thread read.
- Duplicate/conflicting turns: **0** (per-vault lock; exit 61 never observed).
- Thread resets: **1** — first head retired at 81 % after 16 cycles (RETURN bodies on the wire); second head stayed ≤ 61 % through 8 forge turns with "one line + path".
- Carriage latency incidents: **1** — Atlas's watcher baseline fault, ~80 min on cycle 12 (not a tunnel defect).
- Numbering incidents: cycle **20** minted by majkee's hand (three files written by the test sessions on his behalf); slice RETURNs under one cycle (15 ×7) — bus GUIDE has no suffix form (Atlas observations §A.3).
- Record faults by the carrier, all corrected on disk: stale pins/hash in POINT 07; failed first L16 append (guard bug); STATUS fence broken once by backticks; two commits failed on relative pathspecs; POINT 17 stale on three facts a fresh head resolved by reading README §Manifest.
- Second-vendor audits caught: cleanup YAML + staged hunk (RETURN 01); receipts/pointers (RETURN 04); R4 against triad (Atlas RETURN 12); binding premise falsified (witness round 1).

## What the discipline bought / cost (inferred: oraculum — for majkee to weigh)

- Bought: every exchange is a file with a hash; the fresh head re-briefed from two cards + STATUS in one turn; one-line-plus-path kept the second thread flat; a FAIL on the author's premise was found by fresh eyes, not by the author.
- Cost: the carrier is a serialization point (one human-paced relay); POINTs went stale against a moving disk within minutes; slice RETURNs need a numbering rule; the carrier's own record-keeping produced most of the faults.

## Open after the gate (not blockers)

Promotion of the package to canonical homes (majkee's named step) · keeper migration (cartan; after promotion, since it points at the canonical card) · Codex runtime TOML/profile (cartan, W-c) · audit's L12 clarifications (M3, C1-lock) · J2 saddle reconciliation · next audit = its own small session · bus GUIDE: slice/suffix rule · PROJECT.yaml `docs:` line for the stridularium wrapper (U-table) · nablarva rail U1–U9.
