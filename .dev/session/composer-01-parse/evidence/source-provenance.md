# Reference import provenance — 2026-10-17

Prepared by myShell on office, under Majkee's explicit request to process the packet
and prepare the realization team. No source journal, controller table or exchange changed.

## Frozen source

- The delivered SHA256SUMS is unchanged: it pins 19 raw/ files.
- Eighteen inputs match the current local sources named by the helper.
- The Oct 16 journal must come from reposoma commit
  `9fd4cf2b7ad171c49e357a1a44d01ef4e40f6333`, path `.majkee/journal/2026-10-16.md`.
  `git -C /home/hruzam/reposoma show 9fd4cf2b7ad171c49e357a1a44d01ef4e40f6333:.majkee/journal/2026-10-16.md | sha256sum`
  yields `456d1c5eefb142beb4b07f20dcf1463d3ea0a82c690c8f0ac7f4f13b3a6b8337`,
  exactly the manifest's journal pin. Historical bytes are recovered, not reconstructed.
- At inspection, the live journal hashed to
  `b4cddd01dd2b4ccc08d8211862f24552cd6426f16948cbce093dab1fe6a6f498`.
  The live journal stays untouched; it is not the frozen corpus version.

## Preserved disagreement

`raw/sources.json` J01 (lines 163–173) records a third snapshot:
`54b939c697bcfb9eab92282833229a15b0d436338b24a29da309660150fc40e8`, marked
observed working-tree bytes, with observed Git blob `78e50f1f9157a2da30455b8800d706b194587809`.
That blob was unavailable at inspection. This metadata describes the collection's
earlier observation; it does not supersede this packet's SHA256SUMS. The metadata
remains unchanged. Do not treat it as delivery or as the hash of the corpus journal.

## Import and process changes

- The helper stages copies, obtains the pinned journal with read-only git show,
  checks exact regular-file membership and all hashes, and only then publishes raw/.
  It refuses a different populated raw/; an identical rerun leaves raw/ unchanged.
  Source changes fail verification; the helper never repins the manifest.
- The original delivery archive moves from files.zip to evidence/import/files.zip.
  Its ZIP test passed and all six members matched the original extracted files.
  This preserves the imported brief, STATUS and helper before process amendments.
- Brief stamp d37b18f5 becomes 7d030f15 for BUS return packaging, then e04f1a62
  for the cycle-02 YAML scalar correction. The original owns value contained an
  unquoted colon; quoting it preserves its meaning. Design content and attributed
  said/inferred proposals are preserved.
- The imported CS card and prior-art pass remain byte-identical. The new RUNBOOK
  is the team launcher; the card's five-line FIRST STEP is a conversational receipt.
- RUNBOOK covers Phase 0 only. Later phases need numbered siblings with their own gates.
- No composer observation files exist in .dev/observations/ at authoring time.

See helper-checks.txt and the numbered preparation BUS cycle for verification.
