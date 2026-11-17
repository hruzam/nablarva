---
what: normal-profile witness checklist — sublime-observer X1, host home
by: oraculum · claude (head) · 2026-11-15
for: majkee's hands. Agents do not act in the live editor.
state: parts B to D wait until the head says the recorder is verified
---
# Witness checklist

Synthetic files only, all under `/tmp/sublime-observer-witness/`. Share nothing else during
the witness. If anything surprises you, stop, stamp the step, and tell the head; a surprise is
a result, not a failure of yours.

Paths used below:

- task: `/home/hruzam/ia-sync/install-pkgs/sublime-observer.md`
- bed: `/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish`
- published files: `/run/user/1000/sublime-observer/`

## Before you start

- [X] Save all your real work in Sublime. Step 13 kills the editor on purpose.
> I killed by `sublime`.

- [X] Create the test folder: `mkdir -p /tmp/sublime-observer-witness`

## Part A — install (does not need the recorder)

- [X] A1. Run the task's "check alone" one-liner. Expect `prereqs ok (Sublime build 4215)`.
- [X] A2. Paste the task's install block. Expect "five files installed". Do not restart Sublime yet.
>to `oraculum` : filled to task's lines.
- [X] A3. Do the task's verify-by-eye list. Note for the head:
  - did the package load without a restart (palette entry present, console clean)?
  - `plugin_python` in `/run/user/1000/sublime-observer/publisher.json` (expect 3.14.x)
  - `ls -la ~/.config/sublime-text/Packages/SublimeObserver/` — exactly five files, nothing added by Sublime?
- [X] A4. `bash /home/hruzam/ia-sync/install-pkgs/run.sh mark sublime-observer`

If the package did not load live, restart Sublime once and say so.

## Part B — the walk (recorder running)

Start the recorder in a second terminal and leave it running to the end of part D:

    python3 -I -B /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/witness_recorder.py \
      --out /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/witness/recording.jsonl \
      --forbid WITNESS-FORBIDDEN-7Q4X

After each step, type the step number in the recorder terminal and press Enter (a word after
the number is welcome, for example `8 closed`). If you must start the recorder again, use
`recording-2.jsonl`; it refuses to overwrite.

| # | Do | See by eye |
|---|---|---|
| 1 | Create and open `/tmp/sublime-observer-witness/shared-one.md`. Type a first line `WITNESS-SHARED-ONE`, then about 100 short lines (hold Enter with a letter, or paste). Save. Do not share. | No status-bar marker. |
| 2 | Command palette → "Sublime Observer: Share This View (toggle)". | Marker `Observer: SHARED` in the status bar. |
| 3 | Type a few words on line 2. Do not save. | Typing feels normal. |
| 4 | Select one word with the mouse. Then scroll to the bottom with the wheel, and back to the middle. | The selection and the scroll position stay where you put them; nothing jumps; focus stays in the view. |
| 5 | Create and open `/tmp/sublime-observer-witness/private.md`. Type `WITNESS-FORBIDDEN-7Q4X` and a few more words, move the caret, scroll. Save. Do NOT share it. | No marker on this view. The recorder prints no forbidden-hit line. majkee: no hint from recorder|
| 6 | Create and open `/tmp/sublime-observer-witness/shared-two.md`, type `WITNESS-SHARED-TWO`, share it. | Marker on both shared views, not on `private.md`. |
| 7 | With `shared-two.md` focused, run the toggle again (unshare). | Marker gone from `shared-two.md`, still on `shared-one.md`. |
| 8 | Close the `shared-one.md` tab while it is shared. | — |
| 9 | Open `shared-one.md` again. Then share it again. | On reopen: no marker (sharing did not survive the close). After sharing: marker. |
| 10 | Create and open `/tmp/sublime-observer-witness/.env`, type `X=1`, try to share it. | Refused, with a message; no marker. -> majkee: `correctly refused to share`|
| 11 | With `shared-one.md` shared, quit Sublime normally (File → Quit). Stamp after it has closed. | — |
| 12 | Start Sublime. Look at `shared-one.md`, then share it again. | After start: no marker. After sharing: marker. |
| 13 | **Crash.** Save everything. In a terminal: `pgrep -x sublime_text` (expect one pid), then `kill -9 <that pid>`. Stamp at once. Wait 15 seconds. Stamp `13 waited`. | The editor disappears. -> majkee: `4012466`, `` |
| 14 | Start Sublime. Do not share anything. Wait 5 seconds. | No marker anywhere. |
| 15 | Share `shared-one.md`. Type continuously for about 20 seconds, the way you normally type. | Any lag, stutter or dropped key? Tell the head in words. -> majkee: `seems fine all`|

## Part C — removal and reinstall (recorder still running)

- [X] 16. Follow the task's Removal section exactly as written, including what it says about
  Sublime running or not. Stamp `16`. Note: did the palette entry disappear? Is
  `/run/user/1000/sublime-observer/` 
>  gone, let sublime run during deinstalation
```bash
ls ~/.cache/sublime-text/Cache/__pycache__/data/Packages/SublimeObserver/
contract.cpython-314.opt-1.pyc  publisher.cpython-314.opt-1.pyc


```
- [X] 17. Install again with the task's install block and `run.sh mark sublime-observer`
  (after the `unmark` the removal asked for). Stamp `17`. Check the palette entry is back.

## Part D — the two fresh reads (recorder still running)

- [X] 18. Share `shared-one.md` and nothing else. Stamp `18`.
- [ ] 19. Open a **fresh Claude Code session** (plain `claude`, default permissions, started in
  the bed directory). Give it exactly:

      Read /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/01.oraculum.point.md and do what it says. You are the Claude session.

  Do not approve a permission change for reading. An approval prompt for writing its own
  return file is fine; tell the head if a prompt appeared for a read. Stamp `19`.
- [X] 20. Open a **fresh Codex session** (default sandbox, started in the bed directory). Give it:

      Read /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/_bus/01.oraculum.point.md and do what it says. You are the Codex session.

  Stamp `20`.
- [X] 21. Unshare `shared-one.md`. Stamp `21`. Stop the recorder with Ctrl-C.

## Afterwards

Tell the head "witness done" and anything you noticed, especially:

- A3 notes (live load, plugin host, five files).
- Step 4: did caret, selection, scroll or focus ever move by itself?
- Step 15: typing feel.
- Step 16: did removal behave as the task says?
- Any console error in Sublime (View → Show Console) during the walk.

The head then gives the recording and the two return files to the verifier. You may delete
`/tmp/sublime-observer-witness/` when the verdict is in.

## What this witness does not show

A real Python 3.8 plugin host; hosts other than home; several agents reading at once; a crash
where the editor is never restarted beyond the 15 seconds watched in step 13.
