---
what: smoke walk for package version 1.1 (after the fix round) — sublime-observer X1, host home
by: oraculum · claude (head) · 2026-11-16
for: majkee's hands. About ten minutes. Write your notes into this file freely.
state: ready — the new code is verified by assay (98 tests; lock, pairing and revocation attacked)
---
# Smoke walk, version 1.1

Synthetic files only, under `/tmp/sublime-observer-witness/`. Share nothing else.
Please keep the window layout as it is during the walk (no split, no resize); if you do
change it, just write when.

- task: `/home/hruzam/ia-sync/install-pkgs/sublime-observer.md` (now version 1.1)
- session folder: `/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish`

## Before

- [ ] Save your real work. Step S9 kills the editor.
- [ ] `mkdir -p /tmp/sublime-observer-witness/.hlm` (a fake sealed folder for step S7; it is not a real vault)

## Install 1.1

- [ ] I1. The task's "check alone" one-liner → `prereqs ok`.
- [ ] I2. The task's install block → `ok: five files installed`.
- [ ] I3. Verify by eye as the task says. New in 1.1: the folder listing also shows `publisher.lock`.
- [ ] I4. `bash ~/ia-sync/install-pkgs/run.sh mark sublime-observer`

## Walk (recorder running)

Second terminal:

    python3 -I -B /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/witness_recorder.py \
      --out /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/witness/recording-3.jsonl \
      --forbid WITNESS-FORBIDDEN-7Q4X

Type the stamp in the recorder terminal and press Enter **after** doing the step, unless it says "first".

| Stamp | Do | See |
|---|---|---|
| `S1` | Open `shared-one.md`. Share it (palette → "Sublime Observer: Share This View (toggle)"). | Marker `Observer: SHARED`. |
| `S2 start` | Stamp first. Then type in the shared tab for about 20 seconds. | |
| `S2` | Stamp when you stop. | Any lag or dropped key? |
| `S3 start` | In the shared tab scroll to the MIDDLE of the file and click a word there. Then File → New View into File. Stamp. | |
| `S3` | In the NEW tab only: go to the very end, type about ten short lines, wait two seconds. Stamp. Then close the new tab. | Did the first tab's caret or scroll move by itself? |
| `S4` | Open `shared-two.md` and share it too. Stamp. | Marker on both. |
| `S5` | Unshare `shared-two.md` (toggle again). Stamp. | Marker only on `shared-one.md`. |
| `S6` | Fresh **Claude Code** session, prompt A below. Stamp when it has finished. | Did it ask approval for a read? |
| `S7` | Fresh **Codex** session, prompt B below. Stamp when it has finished. | Which approval mode was it in? Did it ask for a read? |
| `S8` | With `shared-one.md` shared and focused: File → Save As… → `/tmp/sublime-observer-witness/.hlm/moved.md`. Stamp. | Marker should disappear, with a refusal message. |
| `S9` | Open `shared-one.md` again, share it. Then crash: `pgrep -x sublime_text`, `kill -9 <pid>`. Stamp at once with the pid, e.g. `S9 12345`. | Editor disappears. |
| `S10` | Wait 10 seconds. Start Sublime. Share nothing. Wait 5 seconds. Stamp. | No marker anywhere. |
| `S11` | Share `shared-one.md`, then quit Sublime normally (File → Quit). Stamp after it closed. Stop the recorder with Ctrl-C. | |

Prompt A (Claude):

    Read /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/11.oraculum.point.md and do what it says. You are the Claude session.

Prompt B (Codex):

    Read /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/11.oraculum.point.md and do what it says. You are the Codex session.

## Afterwards

Tell the head "smoke done". Useful words: typing feel at S2; S3 moved or not; what you saw at
S8; any console line naming SublimeObserver (View → Show Console).

You may start Sublime again after S11; the package stays installed.
