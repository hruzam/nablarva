# Independent P1 correction review — cycle 04

Verdict: **PASS of the corrected oracle specification**, subject to head ACCEPT of this exact candidate. This is not runtime source qualification. Both material cycle 02 findings are resolved; no repair or runtime action was performed by the witness.

Externally recorded active manifest SHA-256: **`627e2e30e1434b8e27c277ffc2a21d8f6120ba92a9aca12d863459a65f9fcf7c`**. Active schedule SHA-256: `5b7dfd8af1abf1649733d74a954b438e96afa17337d56e4faaf5007b6c4dc9cb`.

Reviewer: `/root/witness_termpanum_x1_p1`, 2026-10-30. Authority: cycle 04 POINT, existing RUNBOOK and Q release, head's cycle 02 VERDICT and appended P1 disposition in `raw/entry-and-release.md`. Only this new review and `_bus/04.witness.return.md` are written. Earlier review/RETURN remain untouched. No tmux execution/contact, fixture, capture, delegation or source repair.

## R1 — resolved

Actual schedule now defines every frame in every normal run as a marker: 30 × 256 = 7680 release-to-completed-append samples. It records frame/run identity, independent release and append times, and exact byte intervals. A write completing several frames supplies the same append-completion time to each; partial-frame appends do not complete a marker. Missing/untrustworthy samples prevent PASS. Thirty per-run maxima supply the p95 population, with sample 29 ≤500 ms; the global maximum across all 7680 must be ≤1000 ms. Healthy populations and other timing bars are unchanged.

This implements the head's explicit conservative operationalization, separately identified as inference rather than original quotation or operator gavel. It measures startup, middle and tail rather than assuming midpoint behavior represents them. The earlier counterexample's frame-0 delay of 1200 ms now violates the global maximum directly, regardless of frame 128. Using per-run maxima is conservative relative to pooling frame samples and creates no weaker bar. The clarification stays inside Q05's pre-runtime population definition: no numerical threshold, runtime effect, product/API contract or broader authority changes. Feasible recording and actual timing remain builder/witness execution obligations.

## R2 — resolved

The mandatory every-case twice-replay and eight-class/80-case invalid-bundle matrix are removed from Q and explicitly retained as R's future qualification. All six Q07 failure modes remain ten each, including deletion, duplication and reordering against unchanged normal expectations. Q09 adds a precisely specified incomplete-bundle negative: copy one retained healthy normal bundle, omit only `capture.bin`, keep the original untouched, and require nonzero rejection with a reason identifying missing capture. Together with the required damaged-wire checks, this exercises Q's mismatched/incomplete rejection without importing R's public replay/report product, stale policy or unspecified optional suite.

## Other corrections and preservation

All 30 normal runs and the first of the required 30 burst runs split frame 0; no hidden extra healthy population remains. The ten ONLCR, ten screen and ten late-attach counts are expressly chosen Q coverage rather than original numerical mandates. Reconnect uses the same ten Q07 runs. Freshness, incarnation, false-completion, fault barriers, controls and byte/render separation retain their previous conservative conditions.

The reproduction recipe now allocates and records a fresh `mktemp` directory, compiles with an absolute source path into that directory, generates into its new `regenerated/`, and compares all 11 files without writing into the corpus. No new compilation was needed in this review because generator, assertions and all generated wire/screen hashes are unchanged.

Checked actual `diff -u` of retained versus active schedule and manifest, rather than relying on the author RETURN. Manifest changes are only the revised schedule digest and explicit `revisions/` exclusion. Administrative JSON/hash/inventory verification established:

- All 14 active members match unique listed paths/digests and are regular nonsymlink files.
- All 14 original members reconstruct exactly using active unchanged files and `revisions/01/schedule.md`.
- Preserved original manifest hash is `fe981fa2f53d49279b276f59d487cb282ba6ec8d7f093bdffd6a32cc90cc9692`; preserved schedule hash is `a2a1ea025d9a57614a5985883be8da7d6a5703994360a98038282d491fed0bfb`, matching the cycle 02 independent finding.
- Only `schedule.md` changed among the 14 active member entries. All 11 wire/screen hashes match the prior independent evidence `/tmp/termpanum-x1-witness-02.b1YMkw/manifest-and-regeneration.json`; generator and observation assertions also match the original manifest. Prior independent calculations, successful separate C++ checker, regeneration and installed-manual inspection therefore apply without rerunning them.
- Exact unlisted files are `manifest.json`, `build.log`, `reproducibility.log`, `revisions/01/manifest.json` and `revisions/01/schedule.md`, all explicitly excluded. No unexplained active artifact exists.
- Original review SHA-256 remains `8d206efcf8e81f6943b2d9e4cd9bae4b1605f67d764f7f1bb47c8179e980bfb1`; original RETURN remains `4133b0e52d8b1a5f9bdb110bc81332e3d079b6a945f965358955c9269a1f8405`.

The previous Q01–Q10 assessment is retained: Q05 and Q09 now pass specification review; byte and screen expectations, Q01/Q10 evidence obligations and unexercised-runtime limits remain as recorded in cycle 02. The original rejected candidate can be reconstructed and remains distinct from this corrected identity. Head may now decide P1 ACCEPT against the active hash above.

No collector, source fidelity, rendered capture, termios behavior, timing, failure detection, identity/freshness handling, rejection implementation or owned cleanup has been exercised by this correction review. Those are still P2/P3 work. The head retains the ACCEPT pen, and Majkee retains final qualification GO/STOP.
