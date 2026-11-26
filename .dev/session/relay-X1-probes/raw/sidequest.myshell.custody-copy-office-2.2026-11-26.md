---
kind: side quest s02 — a request from myShell to the controller, on Majkee's word. Not a cycle of this bed; it takes no pen,
  changes no STATUS, RUNBOOK or ledger, and releases nothing.
from: myShell (claude a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66, window `myShell`, pane %61)
to: controller (codex thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318, pane %59, window now `supervisor-relay`)
written: 2026-11-26, home
authority: Majkee 2026-11-26, typed in the myShell session — his yes to a copy to office by the controller (the lead replaced his quoted words by this paraphrase before committing the file; his words stay in myShell's session)
state: untracked — the lead commits it, or leaves it.
---

# Side quest s02 · bring the chooser custody folder on office up to date

**Ask.** Bring `~/.local/share/nablarva/custody/x1-chooser-2026-11-23/` on office (`ssh office`, host `hruzam-120922`)
level with home. Home originals stay. Nothing in Git.

**Facts checked by myShell today, home.**
- Home has 169 files in that folder; office has 160. Office lacks the subfolder `tracker-sample2-2026-11-26.rsztjnz1/`
  (9 files, with its own `SHA256SUMS`). myShell did not compare the other 160 file by file.
- No tracker process runs on home now (`STOP` is present in that subfolder), so nothing in the folder is live.
- The earlier side quest s01 is `raw/sidequest.myshell.custody-copy-office.2026-11-23.md`; same method is fine.

**Wanted outcome.**
1. Every file of the folder present on office, modes and modification times kept, folders 0700, files 0600.
2. SHA-256 compared per file between the hosts for the whole folder; any file that differs is named, not overwritten.
3. No `--delete`; nothing touched on office outside this folder.

**Return.** One file beside this one: `raw/sidequest.controller.custody-copy-office-2.return.2026-11-26.md` — command, counts and
bytes on both hosts, hash result, anything refused or different. No bell is owed.

**Not asked.** No commit, no push, no edit of STATUS or the relay ledger.
