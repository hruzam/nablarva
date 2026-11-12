# pad.1-home-witness — prepare the home-host transcript sitting

> Operator test surface. Sequential: one step, report back, then the driver supplies the next step. Driver: Cartan.
> Give a short plain-language reason for each step; perform machine-verifiable work independently and ask Majkee only for the actual host or native-session witness.

Candidate path:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana`

Precondition: Majkee is at the home desktop with a terminal and Sublime available. No private session or pin store is needed for this step.

### STEP 0 — check the host and tools

In a home terminal, run:

```sh
hostname
command -v zsh
command -v subl
codex --version
claude --version
```

Expected: host `hruzam`, paths for zsh and Sublime, and both CLI versions. Report the output to Cartan. If a command fails or the host differs, stop; do not open a native session yet.

> to-cartan
> from-majkee
> 
> ---
>
>on office has newer, codex 0.167.0, cluade 2.1.318
> 

```text
 hostname
hruzam
❯ command -v zsh
/usr/bin/zsh
❯ command -v subl
/usr/bin/subl
❯ codex --version
codex-cli 0.160.0
❯ claude --version
2.1.286 (Claude Code)

```

### STEP 1 — identify the Codex executable

In the same home terminal, run:

```sh
type -a codex
command -v codex
/home/hruzam/.npm-global/bin/codex --version
```

Report the output. This checks whether the terminal and Cartan's sandbox select different executables; it does not update either installation. If the absolute executable is missing or a command fails, report that result and stop.

> MAJKEE report 1

```text
❯ type -a codex
codex is /home/hruzam/.npm-global/bin/codex

❯ command -v codex
/home/hruzam/.npm-global/bin/codex

/home/hruzam/.npm-global/bin/codex --version
codex-cli 0.166.0



```

### STEP 2 — check the synthetic witness paths

In the home terminal, run this read-only check:

```sh
python3 -I -S -B - <<'PY'
import os
from pathlib import Path
root = Path('/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test')
for name in ('cache.ui-witness-20261106', 'read.ui-witness-20261106.md'):
    path = root / name
    print(f'{path}:', 'EXISTS' if os.path.lexists(path) else 'ABSENT')
PY
```

Expected: both paths say `ABSENT`. Report the output. If either says `EXISTS`, stop; Cartan will choose another witness identity without touching that path.

> MAJKEE report 2

```text
/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106: ABSENT
/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.ui-witness-20261106.md: ABSENT
```

### STEP 3 — render the synthetic conversation

In the home terminal, run:

```zsh
zsh -f -c '
  cache=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106
  reading=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.ui-witness-20261106.md
  if [[ -e "$cache" || -L "$cache" || -e "$reading" || -L "$reading" ]]; then
    print -u2 "Witness path already exists; stop and report it."
    exit 1
  fi
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_render --vendor codex --vendor-version 0.166.0 \
    --project /home/hruzam/unikuklatrix/nablarva \
    --bed termbrana-M0-markdown-test --agentive-session ui-witness-20261106 \
    --source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/fixtures/codex-0.166.synthetic.jsonl
'
```

Expected: one JSON result naming a snapshot, cache and reading file. This creates only derived files for the fictional fixture at the checked paths. Report the complete output; if there is an error, stop and report it without retrying.

> MAJKEE report 3

```text
{"cache": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106", "context": {"project": "/home/hruzam/unikuklatrix/nablarva", "vendor": "codex", "vendor_version": "0.166.0"}, "map": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106/snapshots/32c2c7f640fe3ff065724f03/map.json", "read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106/snapshots/32c2c7f640fe3ff065724f03/read.md", "reading": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.ui-witness-20261106.md", "records": 4, "snapshot": "32c2c7f640fe3ff065724f03"}

```

### STEP 4 — list the synthetic exchanges

In the home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_select --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106
'
```

Expected: four numbered entries, including two user entries with the same snippet but different record IDs. Report the complete output; if the command fails, stop and report the error.

> MAJKEE report 4

```text
{"entries": [{"line": 11, "number": 1, "record": "item-user-001", "role": "user", "snippet": "Please show the selected exchange.", "timestamp": "2026-11-05T20:00:00Z"}, {"line": 15, "number": 2, "record": "item-assistant-002", "role": "assistant", "snippet": "Here is a fenced example: ```python print('hello') ``` The blank lines and fence", "timestamp": "2026-11-05T20:00:02Z"}, {"line": 25, "number": 3, "record": "item-user-003", "role": "user", "snippet": "Please show the selected exchange.", "timestamp": "2026-11-05T20:01:00Z"}, {"line": 29, "number": 4, "record": "item-assistant-004", "role": "assistant", "snippet": "The second matching prompt is a distinct source record.", "timestamp": "2026-11-05T20:01:03Z"}], "snapshot": "32c2c7f640fe3ff065724f03"}

```

### STEP 5 — open the second matching prompt in Sublime

In the home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_open --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106 --record item-user-003
'
```

Expected: a **new Sublime window** opens at the heading `3. user … item-user-003` in the fictional transcript. The following response says the second matching prompt is a distinct source record. Report the terminal output and what you actually see: did a new window open, and did it land at that heading? If it fails or you are unsure, stop and report; do not retry yet.

> MAJKEE report 5
>to-cartan from majkee :
>---
> Q1: will be still oppening new and new window. not saying now but later, can attach to speciffic oppened Sublime session.
> Q2: do you thing I will be able to send back message to agent from sublime markdown and eventually confirm approval request (as far as i know not part of frozen transcript but cached in another part of system). Again later phase? 
```text
`/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106/snapshots/32c2c7f640fe3ff065724f03/read.md`

```

STEP 5 follow-up: Majkee confirmed in conversation that the new window and heading matched the expectation.

### STEP 6 — open the first prompt while the file is already open

Leave the STEP 5 Sublime window open. In the home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_open --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106 --record item-user-001
'
```

Expected: Sublime opens a new window at `1. user … item-user-001`, while the same snapshot file was already open from STEP 5. Report what happened and the terminal output. If it differs or is uncertain, stop and report without retrying.

> MAJKEE report 6

---

>to-cartan from-majkee
>
>---
>
>Both same. tested side by side in sublime.
>
>---

```text
{"opened": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.ui-witness-20261106/snapshots/32c2c7f640fe3ff065724f03/read.md:11", "snapshot": "32c2c7f640fe3ff065724f03", "source_record_id": "item-user-001"}
```

STEP 6 follow-up: Majkee confirmed a new Sublime window opened the same file and both requested positions matched; he compared the views side by side.

### STEP 7 — render a fictional approval reference

In the home terminal, run:

```zsh
zsh -f -c '
  cache=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106
  reading=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.approval-witness-20261106.md
  if [[ -e "$cache" || -L "$cache" || -e "$reading" || -L "$reading" ]]; then
    print -u2 "Approval witness path already exists; stop and report it."
    exit 1
  fi
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_render --vendor codex --vendor-version 0.166.0 \
    --project /home/hruzam/unikuklatrix/nablarva \
    --bed termbrana-M0-markdown-test --agentive-session approval-witness-20261106 \
    --source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/fixtures/codex-approval.synthetic.jsonl
'
```

Expected: a JSON result for one fictional exchange and its snapshot. This only creates derived files for the fictional fixture; no real approval is requested. Report the full output. If it fails, stop without retrying.

> MAJKEE report 7

```text
{"cache": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106", "context": {"project": "/home/hruzam/unikuklatrix/nablarva", "vendor": "codex", "vendor_version": "0.166.0"}, "map": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106/snapshots/35ef94c8ffd2f965a03adb97/map.json", "read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106/snapshots/35ef94c8ffd2f965a03adb97/read.md", "reading": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.approval-witness-20261106.md", "records": 1, "snapshot": "35ef94c8ffd2f965a03adb97"}

```

### STEP 8 — open the fictional approval view

In the home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_open --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106 --record user-approval-demo
'
```

Expected: a new Sublime window shows the fictional transcript. Below its user exchange is `approval-demo-1`, the request, a `cached source` address ending in `source.jsonl:2`, and an **unknown** outcome. Report what you see and the terminal output. If the result is uncertain or fails, stop without retrying. Do not navigate the address yet; that is the next step.

> MAJKEE report 8

```text
{"opened": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.approval-witness-20261106/snapshots/35ef94c8ffd2f965a03adb97/read.md:11", "snapshot": "35ef94c8ffd2f965a03adb97", "source_record_id": "user-approval-demo"}
```

STEP 8 follow-up: Majkee reported the new Sublime window and file matched the expectation.

### STEP 9 — follow the cached source address

In the fictional approval view opened in STEP 8:

1. Place the caret **inside the path** on the `cached source:` line, before its `:2` suffix.
2. Press **Ctrl+Alt+O**, the current home binding for `editor_pin_open_target`.

Expected: Sublime opens the retained `source.jsonl` at line 2, whose JSON contains `approval-demo-1` and `synthetic_approval_request`. Report what opened and whether the caret landed on that line. If nothing happens or the result differs, stop and report; do not retry yet. This is a fictional record and has no approval action.

> MAJKEE report 9

```text
pin worked oppened json in new tab.
including demanded|expected value
caret: [LN20,CLMN] starting file.
caret: [2,1] target json
```

### STEP 10 — make a separate synthetic source for collection

In the home terminal, run:

```sh
python3 -I -S -B - <<'PY'
from pathlib import Path
fixture = Path('/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/fixtures/codex-0.166.synthetic.jsonl')
target = Path('/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl')
data = fixture.read_bytes()
prefix = data[:data.rfind(b'\n') + 1]
with target.open('xb') as handle:
    handle.write(prefix)
print('created', target, 'bytes', len(prefix))
PY
```

Expected: `created` and 1573 bytes. The exclusive create refuses to overwrite an existing file. Report the output; if it fails, stop without retrying. This is a copy of fictional fixture records, not a native history.

> MAJKEE report 10

```text
created /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl bytes 1573
```

### STEP 11 — create the collector’s initial snapshot

In the home terminal, run:

```zsh
zsh -f -c '
  cache=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106
  reading=/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.collector-witness-20261106.md
  if [[ -e "$cache" || -L "$cache" || -e "$reading" || -L "$reading" ]]; then
    print -u2 "Collector witness path already exists; stop and report it."
    exit 1
  fi
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_render --vendor codex --vendor-version 0.166.0 \
    --project /home/hruzam/unikuklatrix/nablarva \
    --bed termbrana-M0-markdown-test --agentive-session collector-witness-20261106 \
    --source /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl
'
```

Expected: one JSON result for a four-exchange snapshot with `cache` and `reading` paths. Report the complete output. If a path already exists or the command fails, stop without retrying.

> MAJKEE report 11

```text
{"cache": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106", "context": {"project": "/home/hruzam/unikuklatrix/nablarva", "vendor": "codex", "vendor_version": "0.166.0"}, "map": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/cbac671eb95c508fbfef2130/map.json", "read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/cbac671eb95c508fbfef2130/read.md", "reading": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.collector-witness-20261106.md", "records": 4, "snapshot": "cbac671eb95c508fbfef2130"}
```

### STEP 12 — start the foreground collector

In a home terminal that you can leave open, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_watch --vendor codex --vendor-version 0.166.0 \
    --project /home/hruzam/unikuklatrix/nablarva \
    --source /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl \
    --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106 \
    --interval 2 --cycles 600
'
```

Expected: JSON poll output appears, with `ok: true`; the initial selected and latest snapshots match. The command polls in the foreground for at most 600 cycles (about 20 minutes plus processing time). **Leave this terminal open and the watcher running**, then report the first output. If it exits, reports an error, or reaches its cycle limit before the next step, report that; do not restart it yet.

> MAJKEE report 12

---

>to-cartan:
>number "cycle" : `$n` is growing. Now we are on nr 110 and still growing.

```text
{"complete_prefix_unchanged": true, "cycle": 1, "latest_read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/cbac671eb95c508fbfef2130/read.md", "latest_records": 4, "latest_snapshot": "cbac671eb95c508fbfef2130", "new_records_available": false, "new_snapshot_available": false, "ok": true, "published_snapshot": null, "selected_read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/cbac671eb95c508fbfef2130/read.md", "selected_record": null, "selected_records": 4, "selected_snapshot": "cbac671eb95c508fbfef2130"}
```

### STEP 13 — open the collector’s selected view

First check the watcher terminal: its cycle number should still be increasing and it should not have returned to a shell prompt. If it has stopped, report that and stop here.

While the watcher remains running, use a **second terminal** to run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_open --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106 --record item-user-003
'
```

Expected: a new Sublime window opens the synthetic collector view at `item-user-003`; the watcher keeps polling in its own terminal. Leave both open and report what you see, the command output, and the current watcher cycle. If either part fails or is uncertain, stop without retrying.

> MAJKEE report 13

> to-cartan:
> only FYI after reaching cycle 600, script 12 stopped as expected.
```text
Sublime oppened on expected place [25,1] 

# =========

{"opened": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/cbac671eb95c508fbfef2130/read.md:25", "snapshot": "cbac671eb95c508fbfef2130", "source_record_id": "item-user-003"}

```

### STEP 14 — restart the watcher and append one fictional record

Leave the STEP 13 Sublime view open. In the watcher terminal, restart the **same command from STEP 12**. When its first `ok: true` JSON line appears, promptly use the second terminal to run:

```sh
python3 -I -S -B - <<'PY'
from pathlib import Path
import hashlib, json
p = Path('/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl')
before = p.read_bytes()
expected = '8659bc74bff17572da7d8d1498357ea4d5de7ac902fc4bf6fe32361ddd48f856'
if hashlib.sha256(before).hexdigest() != expected:
    raise SystemExit('Synthetic source changed already; stop without appending.')
event = {'timestamp': '2026-11-06T17:34:00Z', 'type': 'event_msg',
         'payload': {'id': 'item-user-007', 'type': 'user_message',
                     'message': 'Synthetic collector append witness.',
                     'thread_id': 'thread-demo-01', 'session_id': 'session-demo-01',
                     'branch_id': 'branch-main'}}
with p.open('ab') as handle:
    handle.write((json.dumps(event) + '\n').encode())
print('appended one fictional record: item-user-007')
PY
```

Expected: the second terminal prints the append confirmation; a following watcher line says `new_records_available: true` while `selected_snapshot` remains `cbac671eb95c508fbfef2130`. The open Sublime view should still show the original snapshot. Report the append output, one watcher JSON line showing the result, and whether the open view stayed unchanged. Leave the watcher and view open. If the watcher is not running, the append command refuses, or anything differs, stop and report without repeating the append.

> MAJKEE report 14

```text

```

STEP 14 recovery: Cartan inspected the files after the guard message. The fictional `item-user-007` is already present exactly once, and the latest snapshot contains it while the selected reading remains unchanged. **Do not run the append again.** The watcher terminal and the visible Sublime view still need an operator observation.

STEP 14 follow-up: Majkee reported the watcher flags `new_records_available: true` and `new_snapshot_available: true`, and the open `read.md` content looked the same.

### STEP 15 — explicitly refresh the bookmarked view

In the second home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_refresh --vendor codex --vendor-version 0.166.0 \
    --project /home/hruzam/unikuklatrix/nablarva \
    --source /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/source.collector-witness-20261106.jsonl \
    --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106 \
    --record item-user-003
'
```

Expected: JSON reports `refreshed: true`, `carry_forward: true`, and the newer selected snapshot. This updates the selected reading file; it does not automatically move the already-open immutable snapshot window. Report the complete output. If it fails or is uncertain, stop without retrying.

> MAJKEE report 15

```text
{"carry_forward": true, "latest_read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/347a3a52069a3ea6a376f494/read.md", "latest_records": 5, "latest_snapshot": "347a3a52069a3ea6a376f494", "new_records_available": false, "new_snapshot_available": false, "reading_materialized": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/read.collector-witness-20261106.md", "refreshed": true, "selected_read": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/347a3a52069a3ea6a376f494/read.md", "selected_record": "item-user-003", "selected_records": 5, "selected_snapshot": "347a3a52069a3ea6a376f494"}

```

### STEP 16 — inspect the refreshed snapshot

**Why:** STEP 15 moved the bookmark in the cache. This checks that Sublime can open the newer snapshot at the *same* exchange and that the appended fictional record is present.

In the second home terminal, run:

```zsh
zsh -f -c '
  source /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/base.zsh
  _tbv_open --cache /home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106 --record item-user-003
'
```

Expected: a new Sublime window opens at heading `3. user … item-user-003`. A little below it is a new fifth entry containing `Synthetic collector append witness.` Report the terminal output and whether you see both. If the result differs or is uncertain, stop without retrying.

> MAJKEE report 16

```text
caret: [25,01].
expected: `Synthetic collector append witness.` existing. 
terminal: 
{"opened": "/home/hruzam/.nablarva/nablarva-3ca44d762f78/termbrana-M0-markdown-test/cache.collector-witness-20261106/snapshots/347a3a52069a3ea6a376f494/read.md:25", "snapshot": "347a3a52069a3ea6a376f494", "source_record_id": "item-user-003"}

```

### STEP 17 — start a separate real Codex test conversation

**Why:** Everything so far used invented messages. This creates a small real conversation so we can test whether the reader understands what Codex actually writes, without searching your existing conversations. Your new conversation will stay open for the later independence check.

In a **new terminal**, run:

```zsh
witness_dir=$(mktemp -d /tmp/nablarva-native-XXXXXX)
printf 'Test directory: %s\n' "$witness_dir"
codex --no-daemon -C "$witness_dir"
```

When Codex opens, send this harmless message:

```text
Please reply exactly: Synthetic native witness ready.
```

Expected: Codex replies in that separate session. Leave it open. Report the printed test directory and whether the reply arrived; do not paste any private conversation or authentication information. If a prompt or error prevents the session starting, report it and stop without retrying.

> MAJKEE report 17

```text
The separate Codex test session was spawned and replied.
Test directory: /tmp/nablarva-native-JQfnzz
Thread ID: 01a1b58c-fd98-7d13-ba68-5d1f98acc6d9
```

### STEP 18 — inspect the native test conversation in Sublime

**Why:** Check that the actual Codex prompt and reply appear in the reader,
at the selected user message, while the native session stays open.

Cartan rendered only the explicitly identified disposable session into
`/tmp/nablarva-native-view-mf7s3v06/cache` using the `codex-rollout-0.167`
input format. The reader reported two exchanges and opened snapshot
`aaf65a51d71709a32e93881f/read.md:21` using `_tbv_open`.

Majkee: check the newly opened Sublime window. Does it show the fictional
prompt and expected reply, with the caret at the user heading? Keep your
separate Codex terminal open and report what you see.

> MAJKEE report 18

```text
Majkee reported the caret at line 21, column 1, on the chapter marker above
the message block, rather than inside the words of the message. Majkee confirmed
that both the fictional prompt and expected reply are visible.
```

### STEP 19 — keep the native conversation working

**Why:** Check that reading the snapshot did not take over or interrupt Codex.
Leave the Sublime view open. In the same disposable Codex terminal, send:

```text
Please reply exactly: Second native witness ready.
```

Report whether the reply appears; keep the terminal and Sublime view open.

> MAJKEE report 19

```text
Majkee sent the requested follow-up and observed that the previously opened
read.md did not include it. Cartan checked only the explicitly identified
test rollout: both the follow-up prompt and expected assistant reply were
recorded, and the native process remained running. The displayed read.md is an
immutable snapshot created before the follow-up.
```

### STEP 20 — compare the new snapshot

**Why:** Show that the earlier reading stays fixed while newly collected
conversation content is available in a later snapshot.

Cartan explicitly collected the selected native test source and opened the
new snapshot `d19afe1c22becfa96fb30f61/read.md` at line 29, the follow-up user
heading. The original snapshot `aaf65a51d71709a32e93881f/read.md` remains
separate. This is an explicit collect and open in a non-layout cache, not a
test of automatic watching or bookmark refresh.

Majkee: does the new Sublime window show `Second native witness ready.` and
its reply, while the earlier window still shows the original snapshot? Keep
the native Codex terminal open.

> MAJKEE report 20

```text
Majkee confirmed that snapshot d19afe1c22becfa96fb30f61 includes the second
request and reply, while the earlier aaf65a51d71709a32e93881f snapshot is unchanged.
```

### STEP 21 — test automatic collection of one new exchange

**Why:** Check that an explicitly started foreground watcher notices a new
native exchange without changing the selected snapshot. Cartan starts the
bounded watcher and confirms it is ready before asking Majkee to continue.

> MAJKEE report 21

```text
Majkee reports that the third native reply appeared. The explicitly started
watcher recorded both new-snapshot and new-record availability: its selected
snapshot stayed d19afe1c22becfa96fb30f61 with four exchanges while the latest
snapshot advanced to b0a24f356e8b961db527955c with six exchanges. Codex remained
running. The original open snapshot was not rewritten.
```

### STEP 22 — refresh the selected bookmark

**Why:** Test that the reader moves only on explicit refresh and can carry
the selected exchange forward to the newer snapshot. Cartan runs the refresh
against the second user exchange while the watcher remains active.

The refresh reported `carry_forward: true` and `refreshed: true`, selected
snapshot `b0a24f356e8b961db527955c`, and retained the same second-user
bookmark. Cartan opened that snapshot at line 29. This temporary cache has no
separate materialized reading file, so this witnesses snapshot selection and
opening, not a layout-mode reading-file update.

Majkee: in the new Sublime window, is the caret at the second user heading,
and is the third prompt and reply present later in the file? Keep the Codex
terminal open.

> MAJKEE report 22

```text
Majkee confirmed that the refreshed snapshot b0a24f356e8b961db527955c
includes the third test. The precise caret position was not separately reported.
```

### STEP 23 — stop collection and close the reader

**Why:** Check that the collector and Sublime reader can stop while the native
conversation remains usable. Cartan stops only the bounded test watcher.

Cartan verified watcher PID 1713656's exact command, sent it SIGTERM, and
confirmed it exited with status 143 while the separate test Codex process
remained running. Majkee: close the refreshed test snapshot in Sublime; in
the same test Codex terminal, send `Please reply exactly: Native session still
works.` Report whether the reply appears. Keep the Codex terminal open.

> MAJKEE report 23

```text
Majkee closed the Sublime test windows and reported that the native Codex
session replied. Cartan checked only the explicitly identified test rollout:
the final fictional prompt and its expected reply were both present.
```

### STEP 24 — create a separate Claude test conversation

**Why:** Establish an explicit, disposable Claude 2.1.286 session so the
native adapter can be checked against a real source without searching existing
conversations. Leave the Codex test session alone.

In a new terminal:

```sh
claude_test_dir=$(mktemp -d /tmp/nablarva-claude-native-XXXXXX)
claude_test_id=$(python3 -c 'import uuid; print(uuid.uuid4())')
printf 'Test directory: %s\nTest session ID: %s\n' "$claude_test_dir" "$claude_test_id"
cd "$claude_test_dir"
claude --session-id "$claude_test_id"
```

When Claude opens, send `Please reply exactly: Claude native witness ready.`
Report the two printed values and whether the reply appeared; leave this test
session open. Stop and report any login, trust or other prompt rather than
sharing credentials or retrying automatically.

> MAJKEE report 24

```text
pending
```
