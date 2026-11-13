# STATUS: termbrana-M0-markdown-test

```yaml
updated: 2026-11-13
writer: Cartan · Codex
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · f525e558aa5a7186f3cbc4abc60f53f72c37023b ·
  RUNBOOK.md, STATUS.md and ../pulse.md modified; untracked bed artifacts include
  implementation/termbrana/, REPORT.md, PAD, benchmark, capability and evidence
  files, proposal and raw verifier/Houston returns. See recovery probe for exact paths.
gate: >-
  Majkee records GO or STOP on an independently verified home-host transcript-view
  experiment for Codex and Claude, demonstrating zsh selection and Sublime opening,
  snapshot-bound bookmarks across rebuild, validated carry-forward on append/resume,
  automatic cache collection with explicit reading-view refresh, truthful interactive
  approval references, native-session independence, measured performance, and a
  reviewed ia-sync source-wiring and publication proposal with capability limits.
checkpoint: >-
  Synthetic home workflow passed PAD STEP 16. The 0.167 completed-text adapter
  and refresh-interruption recovery pass independent review; the final suite has
  70 passing tests, including independently checked Claude native subset and
  duplicate-ID performance fixes. See raw/verdict.claude-performance.md,
  evidence.codex-0167.md and raw/verdict.codex-0167-refresh.md. The refreshed
  latest publication candidate passes independent package review; see
  proposal.publication-review2.md and raw/verdict.publication-review2.md. Fresh Houston
  consult is raw/houston.transcript-0167.md. Majkee witnessed Codex 0.167
  collection, bookmark refresh and native-session independence in PAD 17–23.
  Claude fidelity and complete native history remain unqualified.
in_flight: >-
  Majkee reports PAD STEP 17's separate Codex session started and replied in
  /tmp/nablarva-native-JQfnzz. Supplied thread ID 01a1b58c-fd98-7d13-ba68-5d1f98acc6d9
  and directory match the metadata index; the exact rollout parses as two
  expected exchanges. Majkee confirmed both in the open Sublime view at the
  user heading. The native-test cache is /tmp/nablarva-native-view-mf7s3v06/cache.
  PAD STEP 19's follow-up and expected reply are present in that exact rollout;
  its already-open snapshot remains older. An explicit collector invocation
  published snapshot d19afe1c22becfa96fb30f61 with four exchanges in the same
  temporary cache. Majkee confirmed that the newer window shows the follow-up
  and the earlier view remains unchanged. Bounded watcher session 12068 is
  running against the explicit test source; latest b0a24f356e8b961db527955c
  contains six exchanges, selected d19afe1c22becfa96fb30f61 retains four,
  and both availability flags were true. Explicit refresh then validated
  carry-forward and selected b0a24f356e8b961db527955c at the second user
  bookmark. Majkee confirmed the third test appears in the refreshed file.
  The verified bounded watcher PID 1713656 was stopped and is absent; Majkee
  closed the test Sublime windows and confirmed a native reply afterward.
  PAD STEP 24's explicit Claude test source is
  /home/hruzam/.claude/projects/-tmp-nablarva-claude-native-i97BFz/76b3407f-6d42-4007-a0bc-f362e31aa8b0.jsonl.
  Its session ID and cwd match, and its expected fictional prompt and reply are
  present. Majkee saw the reply and reports reopening the session. A bounded
  worker implemented a native 2.1.323 subset against invented fixtures; the
  independent recheck passed. Private Claude test cache
  /tmp/nablarva-claude-view-5jo5eqmz/cache retains the complete source, including
  internal records, and must stay local. Majkee confirmed its prompt and reply
  appear in Sublime. Bounded Claude watcher session 30689 is running with
  private logs under /tmp/nablarva-claude-view-5jo5eqmz; Majkee reports a new
  reply, and the watcher reported latest 5731e099a0d9a1ec012eff08 with four
  exchanges while selected 30eadeecabcbd1f24d9d0260 remained at two. Explicit
  refresh validated carry-forward, selected the newer snapshot and opened it
  in Sublime. Verified bounded watcher PID 3921129 was stopped; Claude remained
  running. PAD STEP 28 requests the operator's follow-up after closing the view;
  do not signal Claude or inject into the
  session or inspect unrelated histories. Watcher output is
  /tmp/nablarva-native-view-mf7s3v06/watcher.jsonl. Do not stop Codex. This
  non-layout cache has no reading-file layout.
  Ia-sync and host configuration remain untouched.
recovery_probe: |
  git -C /home/hruzam/unikuklatrix/nablarva status --short
  git -C /home/hruzam/unikuklatrix/nablarva diff -- .dev/session/pulse.md .dev/session/termbrana-M0-markdown-test
  python3 -B - <<'PY'
  from pathlib import Path
  import hashlib
  b = Path('/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test')
  expected = {
      'majkee-cartan-log.md': '14b47cb448507c053f95b92d188b9804b12bdf53211174c851044d4ca76231eb',
      'termbrana-M0-transcript-view.cli-handoff.md': '6408e744faf1168c338647e07204c075cdb79044f1fd19beffd857786c5c61b9',
      'sublime-pin-install-handoff.cartan.2026-11-05.md': 'f0397673e730faf24c697204e5217e9d14e14ca13d1b2aa3451431a36316ef25',
  }
  for name, digest in expected.items():
      p = b / 'raw' / name
      actual = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else 'MISSING'
      print('raw', name, 'UNCHANGED' if actual == digest else 'CHANGED', actual)
  for p in sorted(b.rglob('*')):
      if p.is_file() and p.name not in {'RUNBOOK.md', 'STATUS.md'} and p not in [b / 'raw' / n for n in expected]:
          print('additional artifact requiring content review', p, hashlib.sha256(p.read_bytes()).hexdigest())
  for name in ('RUNBOOK.md', 'STATUS.md', 'REPORT.md'):
      p = b / name
      if p.is_file():
          print('\n--- ' + str(p) + ' ---\n' + p.read_text())
  PY
  ls -ld /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106 /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.ui-witness-20261106.md 2>&1
  ls -ld /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106 /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.approval-witness-20261106.md 2>&1
  ls -l /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl 2>&1
  ls -ld /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106 /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.collector-witness-20261106.md 2>&1
  ps -eo pid=,args= | rg 'collector.py watch.*nablarva-native-JQfnzz' || true
  tail -n 1 /tmp/nablarva-native-view-mf7s3v06/watcher.jsonl 2>&1
  ps -eo pid=,args= | rg 'collector.py watch.*nablarva-claude-native-i97BFz' || true
  tail -n 1 /tmp/nablarva-claude-view-5jo5eqmz/watcher.jsonl 2>&1
  # Inspect PAD STEP 17 receipt and ask Majkee whether the separate test session
  # started, its temporary directory and whether it remains open before any retry.
  # Do not scan native history or terminate unrelated processes. The append exists.
  # Inspect layout.json, current.json, selected.json and the referenced bundle map,
  # retained source and reading content against evidence.home.md; do not recreate or
  # overwrite either named witness path without reconciling their current contents.
  # Verify raw hashes and inspect actual diffs against the amended contract.
  # The old continuity reproduction documents a detection limit, not a current PASS.
  # Review candidate/evidence contents before adapting; file presence proves no result.
holds:
  - Only the declared experimental implementation and evidence scope is released.
  - Permanent placement under L8/L8′ needs disposition before promotion; no ia-sync, host-config, live plugin, installation or deployment writes are released.
  - Preserve all existing raw inputs and other participants' work; no production pin claims, session injection, approval forwarding or private-log publication.
  - Runtime home writes require effective filesystem permission; override-only tests cannot qualify the selected temporary layout.
  - Native UI, both vendor adapters, approval evidence and weak-host performance remain unverified; reboot cleanup and automatic paging remain deferred.
  - The universal regrow-detection hold is superseded by the approved snapshot contract; unobserved byte-identical regrow remains undetectable. Synthetic identities do not qualify native fidelity.
  - Rewind only attributable obsolete experiment effects after before/after inspection; preserve useful fixtures, original evidence, unrelated changes and the existing Sublime installation.
  - A research worker's over-broad read exposed native-history excerpts in its tool trace; no excerpts were copied to artifacts. Do not repeat the search; see evidence.reconciliation.md.
next: Majkee closes the Claude test views and sends the fictional follow-up in PAD STEP 28.
expected: Claude replies after both watcher shutdown and reader-view closure.
```
