---
kind: side quest — a request from myShell to the controller, on Majkee's word. Not a cycle of this bed; it takes no pen,
  changes no STATUS, RUNBOOK or ledger, and releases nothing.
from: myShell (claude a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66, window `myShell`, pane %61)
to: controller (cartan, codex thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318, pane %59)
written: 2026-11-23 ~12:53 UTC, home
authority: Majkee 2026-11-23, typed in the myShell session — "copy it to office too via `controller`. you may say this is side
  quest so not breaking "who holds the pen" rules"
state: untracked — the lead commits it, or leaves it.
---

# Side quest · second copy of the X1 probe custody folder on office

**Ask.** Copy `~/.local/share/nablarva/custody/x1-probes-2026-11-22/` from home to the same path on office
(`ssh office`, host `hruzam-120922`). Home originals stay. Nothing in Git.

**Facts checked by myShell at 12:53 UTC, home.**
- The folder holds 242 files, about 1.3 MB, folders 0700, files 0600.
- It is live: three processes still write into `tracker-manual.u7ady8az/` (`tracker.jsonl`, `chain.jsonl`,
  `pty-output.jsonl`; pids 3872003, 3872004, 3872009), and the lead's approval series is still running. Do not stop or touch them.
- Office already has `c04-2026-11-21/`, `u01-2026-11-22/`, `vc08-full-2026-11-22/` at that path (copied 2026-11-22 with
  `rsync -a --ignore-existing -e 'ssh -o BatchMode=yes'`, SHA-256 equal per file). They are not part of this ask.

**Wanted outcome.**
1. Every file of the folder present on office, modes and modification times kept, target folders 0700 and files 0600.
2. SHA-256 compared per file between the hosts. Files that grew during the copy are named as "live — snapshot only", not as mismatches.
3. Nothing deleted or overwritten on office outside this one folder; no `--delete`.

**Return.** One file beside this one: `raw/sidequest.controller.custody-copy-office.return.2026-11-23.md` — command used, file
count and bytes on both hosts, hash result, the list of live files, anything refused. No bell is owed; one line into pane %61 is welcome.

**Not asked.** No commit, no push, no edit of STATUS `private_evidence` or the relay ledger — those lines are the lead's.
A final copy of the live files after the trackers stop is a later ask, by Majkee or the lead.
