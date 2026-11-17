---
what: short repeat of the witness — only the pieces the first walk did not show
by: oraculum · claude (head) · 2026-11-16
for: majkee's hands. About five minutes. A new file on purpose: do not merge it into CHECKLIST.md.
---
# Short repeat

The package stays installed; nothing is installed or removed here. Use the same file
`/tmp/sublime-observer-witness/shared-one.md`. Do not resize the window, zoom or change word
wrap during the repeat.

Start the recorder in a second terminal (new output name; it refuses to overwrite):

    python3 -I -B /home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/tests/witness_recorder.py \
      --out /home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/witness/recording-2.jsonl \
      --forbid WITNESS-FORBIDDEN-7Q4X

Type each stamp in the recorder terminal and press Enter.

| Stamp | Do |
|---|---|
| `R1` | Open `shared-one.md` [majkee: `caret on end of line 6 where I left it before ! pkill subl, ! subli`]. Share it (palette → "Sublime Observer: Share This View (toggle)"). Check the status bar shows `Observer: SHARED` [majkee: `ribbon showed message ecatly`]. Then stamp. |
| `R2 start` | Stamp first, then type continuously for about 20 seconds in the shared tab, the way you normally type. |
| `R2` | Stamp when you stop. Note in words: any lag, stutter or dropped key? |
| `R3` | In the shared tab, click a word near the TOP of the file (upper half) and leave the scroll there. Stamp. |
| `R4 start` | File → New View into File (a second tab on the same file). Stamp. |
| `R4` | In the NEW tab only: go to the very end of the file and type about ten short lines. Do not click the first tab. Wait two seconds. Stamp. |
| `R4 moved` | Only if the first tab's caret or scroll moved by itself: stamp this, unshare, repeat the same typing in the second tab with sharing off, and note whether it moves again. [majkee: `in first tab selection and caret stayed on their places`] |
| `R5` | Close the second tab. Unshare `shared-one.md`. Stamp. Stop the recorder with Ctrl-C. |

Optional, one line for the head: while shared, run
`jq .pid /run/user/1000/sublime-observer/publisher.json` and `pgrep -x sublime_text`, and
tell the head both numbers.

Then tell the head "repeat done" with your words for R2 and R4.
