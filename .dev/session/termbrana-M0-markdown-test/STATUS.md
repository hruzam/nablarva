# STATUS: termbrana-M0-markdown-test

```yaml
updated: 2026-11-05 10:02 CET
writer: Cartan · Codex
host: home · hruzam
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · d50b0a0ed32661416e3e4ac5ac2cfe593b509b13 ·
  planning changes in .dev/session/pulse.md and
  .dev/session/termbrana-M0-markdown-test/{RUNBOOK.md,STATUS.md};
  pre-existing untracked .dev/session/termbrana-M0-markdown-test/raw/sublime-pin-install-handoff.cartan.2026-11-05.md belongs to Cartan's handoff.
gate: >-
  Majkee records GO or STOP on an independently verified home-host transcript-view
  experiment for Codex and Claude, demonstrating zsh selection and Sublime opening,
  source-bookmark fidelity across rebuild and append/resume, truthful interactive
  approval references, native-session independence, measured performance, and a
  reviewed ia-sync source-wiring and publication proposal with capability limits.
checkpoint: >-
  Launcher and initial position authored from Majkee's accepted proposal and three
  raw inputs. Existing zsh family and deploy path inspected read-only; experimental
  implementation and operator UI qualification have not started. YAML, gate/router
  agreement and original raw-input digests checked. No executor active.
in_flight: none
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
  # Matching raw hashes, control-only changes, no additional artifacts and the parked
  # STATUS support the initial no-start checkpoint. Any new artifact, changed input,
  # STATUS transition or uncertain effect requires content review and updated recovery
  # before work; do not infer completion from file presence or absence alone.
holds:
  - Only the declared experimental implementation and evidence scope is released when Majkee wakes Cartan; no executor is started by this planning session.
  - Permanent placement under L8/L8′ needs disposition before promotion; no ia-sync, host-config, live plugin, installation or deployment writes are released.
  - Preserve all existing raw inputs and other participants' work; no production pin claims, session injection, approval forwarding or private-log publication.
  - Runtime home writes require effective filesystem permission; override-only tests cannot qualify the selected temporary layout.
  - Native UI, both vendor adapters, approval evidence and weak-host performance remain unverified; reboot cleanup and automatic paging remain deferred.
next: >-
  Majkee wakes Cartan in Medusa posture on GPT-6.1-Terra, high effort, in
  /home/hruzam/unikuklatrix/nablarva and gives it prompt-0 from
  /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/RUNBOOK.md.
expected: >-
  Cartan reads both controls, reconciles the read-only recovery probe and records
  one bounded fixture-qualification action in STATUS before implementation.
```

Initial snapshot initialized by Oraculum under Majkee's explicit Octopus assignment.
`writer` names the declared continuing STATUS owner; Cartan has not been activated.
