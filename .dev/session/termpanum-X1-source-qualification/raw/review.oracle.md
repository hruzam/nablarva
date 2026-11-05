# Independent P1 oracle review — cycle 02

Verdict: **REVISE**. The bytes, manifest and safe regeneration pass the checks below. Two material specification issues remain before head ACCEPT: visibility sampling does not establish the stated normal-workload bound, and the schedule makes deferred R coverage mandatory. This is a finding on a candidate, not source qualification or acceptance.

Reviewer: fresh native witness `/root/witness_termpanum_x1_p1`, 2026-10-30, host `hruzam-120922`, repository HEAD `74f4501ea101f66eddb64f884c70f510cf949754`. The POINT requests gpt-6.1-sol/high; no independent serving-model attestation is claimed. No tmux executable was run, server contacted, fixture/capture started, expected artifact repaired, or delegation performed.

## Reviewed identity and authority

The exact external candidate manifest SHA-256 is **`fe981fa2f53d49279b276f59d487cb282ba6ec8d7f093bdffd6a32cc90cc9692`**. This freezes the identity reviewed here, not an accepted corpus. All 14 listed members match their digests, are regular nonsymlink files, and have unique paths. The only other files are `manifest.json`, `build.log` and `reproducibility.log`, the explicitly excluded manifest/evidence files. Seven observation lines parse as JSON. No `src/` file was present at inspection.

Original inputs match: source contract `7086e59527c77040be9d41ee94966f661dd751c009e5eb636590db103dd32694`; build plan `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`; RUNBOOK `5cbd0c0f33597fdbedf387f6b3fe0812414017840c825af9b23a1df8a8ddc5e3`. The current compiler, tmux and zsh binary hashes match the entry receipt. The receipt records Majkee's Q-only D4 exception and separate C++ helper release; RUNBOOK's Python recommendation is expressly superseded. These release the bounded experiment subject to P1 head ACCEPT, not C/R/L/E/V products, living sessions, integration or deployment. No missing-authority STOP is found for this documentary review and private C++ reproduction.

## Material findings

**R1 — resolve midpoint-only visibility coverage before freezing Q05.** `expected/schedule.md:15` defines just frame 128 as the marker, one observation per normal run. Its 30-sample p95 calculation is unambiguous and correct for that midpoint population. It cannot by itself substantiate the original normal-workload visibility maximum or cover startup/tail delay, and the schedule supplies no explicit qualification limit or justification connecting that sampled measurement to the broader claim. Approved plan §4 says independent release of each marker to completed reader-visible append, p95 ≤500 ms and maximum ≤1,000 ms on normal workload; Q05 requires the population to be frozen, not the bar silently weakened.

A concrete specification counterexample: retain frames 0–119 in collector memory and first append them at emission epoch +1,200 ms, then append later frames immediately. Frame 0 visibility is 1,200 ms, yet frame 128 released at 1,280 ms and appended at 1,281 ms measures 1 ms. All 30 midpoint samples can pass; byte equality, ordering and the six-second whole-capture bar can also pass. This is an analytical counterexample, not an observed runtime defect. The original text does not explicitly demand 256 markers; the defect is the missing defensible relationship and claim limit, not an invented requirement for a particular marker count.

The oracle/head should explicitly disposition the population before implementation. A conservative operationalization is to independently retain release/append measurements for every normal frame, use each run's worst visibility as one of the 30 samples for p95, and report the global maximum. That preserves numeric bars and does not import another package, but head must record that interpretation rather than treating it as already approved wording. Accepting only midpoint evidence instead requires an explicit limited claim and disposition of the original broader bar; this witness does not grant such narrowing.

**R2 — separate required Q comparator checks from deferred R tests.** `expected/schedule.md:21` requires ten runs for each of eight invalid-bundle classes (80 cases) and twice-replay of every retained case. The entry mapping Q09 explicitly defers full R twice-replay/report and the ten-per-class product rejection matrix. Approved plan §4 labels Replay/rejection as R. RUNBOOK likewise defers R's public replay/report product. Calling those requirements Q-local does not resolve the conflict: the candidate still makes their cardinality and universal replay coverage mandatory for this gate.

Q07's ten-per-mode deletion/duplication/reordering tests remain mandatory, as do Q09's nonzero rejection and retained reason for incomplete/mismatched Q bundles and the fresh witness's reproduction. Additional invalid-bundle examples can be useful optional Q robustness coverage. Remove the universal twice-replay and eight-class matrix from mandatory Q acceptance or obtain a specific scope disposition before requiring them. If optional classes remain, define their actual mutations and stale/identity predicates: “mutated metadata” alone could describe a valid change, and retained historical timestamps alone cannot establish invalid staleness. The builder should not invent those acceptance predicates. Preserve full R product coverage with R.

## Independent calculations and reproduction

Private evidence directory allocated and recorded before compilation: `/tmp/termpanum-x1-witness-02.b1YMkw`. No fixed oracle temporary filename or expected destination was reused. The supplied generator and a separately written C++ byte checker compiled with `c++ -std=c++17 -O2 -Wall -Wextra -pedantic`, each exit 0 and empty stdout/stderr. The supplied generator ran only into that directory's new `regenerated/`. The independent checker used a separately built byte vector, decimal header construction and whole-frame vector mutations; it read no collector output. It checked originals and regeneration, exit 0 for both, and administrative byte comparisons found all 11 regenerated files identical.

Independent results:

| File/case | Bytes | Checked property |
|---|---:|---|
| root wire and normal | 262144 each | 256 × 1024; exact formula |
| burst | 4194304 | 4096 × 1024; exact formula |
| ONLCR | 262656 | 512 LF each gains one CR; existing 256 CR retained, total CR 768 |
| delete frame 127 | 261120 | 255 frames; expected comparison must reject |
| duplicate frame 127 | 263168 | 257 frames; expected comparison must reject |
| swap frames 127/128 | 262144 | unchanged length, changed order; must reject |
| screen wire | 18 | ESC[2J ESC[H Alpha CR LF Beta |
| false-completion wire | 19 | exact `Done\r\nuser@host:~$ ` |
| both screen texts | 11 each | exact `Alpha\nBeta\n` |

Frame 0 starts `46 30 30 30 30 30 30 3a 00 0d 0a 5c 1b 5b 33 31 6d 52`; offset 1022 is `49`, offset 1023 LF. Frame 1's offset 17 is `53`. Additional independent header/content checks covered frames 127, 128, 255 and 4095. Deletion/reordering first differ at byte 130054, duplication at 131078: the first six bytes of the changed frame headers still agree, so these are not the frame-start offsets. Frame 128 starts at 131072 and ends at exclusive offset 132096; transformed ONLCR end is 132354. Late attach after frame 127 leaves an expected 131072-byte suffix in the OPOST-off normal stream.

The split ranges `[0,12)`, `[12,13)`, `[13,14)`, `[14,1024)` place ESC and `[` in separate writes as claimed. The ONLCR arithmetic and mutation effects therefore pass independently of generator consistency.

Installed `/usr/share/man/man1/tmux.1.gz`, inspected without tmux contact, documents `capture-pane -p` stdout, zero as the first visible row for `-S/-E`, `-N` trailing-space preservation, and `-J` wrapped-line joining; the proposed options select visible rows 0–1 without those transformations. The independently reasoned screen is Alpha on row 0 and Beta on row 1 after erase/home and CR LF. This is a defensible frozen expectation. Actual screen parsing, final newline and readiness/drain ordering remain runtime hypotheses; no rendered PASS is claimed.

Evidence retained in the private directory: `independent-check.cpp`, `independent-check`, `oracle-generator`, four empty compilation stdout/stderr logs, `independent-original.log`, `independent-regenerated.log`, `manifest-and-regeneration.json`, and `regenerated/`. Checker-source SHA-256 `d9a395f6375646702b5d1ea51453c2031b98bb6646edb24f62f40c6f785d1447`; original-check log `f46a7f66b9cba64a937d14a800d2c174e5c6120a25a1bd63dce74c55fa171752`; manifest/inventory/regeneration evidence `23c5a618a6e909b6e1a92795782973c174a0c6fe8a3a2289e17278afad6a59a2`.

## Q01–Q10 assessment

| Row | P1 assessment |
|---|---|
| Q01 | Documentary coverage sufficient by schedule's explicit RUNBOOK reference: host/boot, binary/socket/server/pane/process incarnation, argv/environment allowlist/load and interval. Actual ownership and identities untested. |
| Q02 | Independent OPOST-off and ONLCR bytes pass. Remaining output flags must suppress other transformations; before/after flags/control characters and any drift invalidation are required at runtime. |
| Q03 | Separate 80×24 screen, wire and exact options are coherent. Rendering/synchronization unexercised. |
| Q04 | Required 30 normal and 30 burst populations, payloads and deadlines are stated. Preserve every run and lateness. “One normal plus one burst separately use split writes” versus all normal runs splitting frame 0 should be clarified as optional extra coverage or explicitly counted variants, without altering the required populations. |
| Q05 | REVISE R1. Ready ≤1500 ms, normal ≤6 s, burst ≤10 s and watchdog 15 s are retained; midpoint p95 is sample 29 of 30, but its qualification scope needs disposition. |
| Q06 | Required 30 false-completion runs and independent five-second alive/quiet proof plus subsequent direct wait are stated. Unknown semantic completion/acceptance/turn-end is preserved. EOF is not exit status. |
| Q07 | Ten each of sink loss, three-second reader pause, disconnect/reconnect and three replay mutations are specified. Fault barriers are out of band and excluded from healthy populations. Supervised detection endpoint is observer detection rather than controller acknowledgement. A healthy reader merely delayed by pause need not invent a failure timestamp; measured coverage/narrowing and no unqualified clean success remain required. |
| Q08 | Ten pane and ten fresh-server recreation cases, late attach after 127 and discontinuity until rebind are explicit. New/unknown incarnation and preserved old timestamps are conservative. Reused labels do not establish identity. Actual identity proof and freshness handling untested. |
| Q09 | REVISE R2. Independent authorship and rejection requirements are present, but mandatory R coverage is imported. Seven observation rows are conservative predicates, not a fully frozen replay/report sequence; that distinction supports deferring R rather than pretending this corpus meets it. |
| Q10 | Required immutable criteria/input/source/config bindings, clocks, termios, control/capture, stderr/exit and owned cleanup evidence are carried by schedule/RUNBOOK references. Runtime bundle immutability and cleanup remain unexercised. |

ONLCR, screen and late-attach repetition counts are extra coverage choices where the original does not prescribe those counts; they must not be presented as original numerical mandates. C heartbeat/health and delayed-record/view tests, R public entry/replay/report qualification, L view/lifetime, E packaging and V shared admission remain deferred. The fixed reusable generator paths in schedule's example were not executed here; future reproduction should retain this review's fresh-private-directory discipline.

No collector exists yet. Exact regeneration proves consistency and these independent byte checks establish the specified byte formulas; neither proves source fidelity, termios behavior, screen rendering, detection latency, process lifetime or cleanup. Return the two material issues to the oracle/head, preserve this candidate and finding, and review a newly identified candidate before any head ACCEPT or capture implementation.
