---
date: `2026-11-27`
scope: `session groups roster`
---




**SYNTAX** 
> to trajectory: you may rewrite according optimal `alien code` = "CLI natural understanding" , in such case you should brief `lead`s
> to trajectory END
1. `oraculum|astrobley|houston` : 
- `oraculum` can spawn `astrobley` senior developersubagent for coding tasks.   
- `oraculum` can spawn `houston` architect for coding tasks.
2. `oraculum-><subagent> : [task] -> ` : `oraculum` spawning `<subagent>` 
3. `poke` protocole | syntax, if you not remember: 
```
/home/hruzam/reposoma/.majkee/journal/raw.2026-11-13.md:261
---
name: `trajectory`
written: 2026-11-14
scope: this section only. Teaching notes, uncanonical. Built from the lines that actually worked in vistMini.
---
/```

### A. The one line (the poke)

```text
[<tag> <id>] from <who> -> read <absolute path> ; ack: <none|per file>
 └─ label ─┘ └ sender ┘    └──── the only instruction ────┘  └ what you owe back ┘
/```

| part | what to put | examples |
|---|---|---|
| `[tag …]` | **what kind of message**, so the receiver and the log know before reading. First word = kind, then an optional short id | `[vist p10]` normal bus message · `[manual p10]` **typed by hand** (never counts as mechanism delivery) · `[consult]` · `[vist return]` · `[vist decision]` · `[$cold-start-card]` |
| `from …` | who sends, by seat name | `from trajectory`, `from cartan`, `from majkee` |
| `-> read …` | **one absolute path**. The file holds everything; the line holds nothing else | `-> read /home/hruzam/unikuklatrix/nablarva/.dev/session/vist-X0-helloWorld/raw/brief.witness.trajectory.2026-11-14.md` |
| `; ack:` | what the receiver owes: `none` (just read), `per file` (the file says what to return) | |

Rules for the line: **one line, plain ASCII, under ~200 characters if possible, absolute path, no instructions in the line itself.**
Why: it may be typed into a screen, and a short pointer cannot be misread as a task. The task lives in the file, where it can be checked later.

Your own lines that were perfect: `[manual p10] read /home/hruzam/…/_bus/10.cartan.point.md` · `[consult final] read …; ack: per file`.

### B. The file behind it (the real prompt)

```text
---
msg: 20261114T-p01          # unique: date + T + short tag. Never reuse an id
from: majkee                 # who asks
---

```

---

# `side-quest` , please for collections.

> with `myShell` tmux session|window|pane: `$36 | 3 myShell @59 | %61`
> ***collect syntax due session work experiences***
> - for 'alien code' - that what is understable (best: naturaly). I know for LLMs is not comfortable languague like syntax, rather have their own natural jargon, pokes worked as understable. Cosider how much dos part can have sideeffect.
> - roster bulding experinces
> - caching -> best options . `majkee`s note: think - can be hold attached to tmux-window identity or you have better one. (?)
> - solve episthemic|socratic Q2 : `poke` and its possible usage as semi-mail instead tool bash to shared terminal in later phase.
> - --> SYNTAX, CACHE can be interpreted as project|agent|* property in which optimal meaning.
> - solve episthemic|socratic Q3: how to design `runbook` or similar shape in case 


**TMUX MAP: `helloWorld`**

```bash
tmux list-windows -t helloWorld -F '#{session_id} | #{window_index} #{window_name} #{window_id} | #{pane_id}'
$36 | 1 supervisor-relay @57 | %59
$36 | 3 myShell @59 | %61
$36 | 4 auditor @64 | %66
$36 | 5 exec @66 | %68
$36 | 6 lead @68 | %70
$36 | 7 spare-codex @100 | %102
$36 | 9 spare-claude @76 | %78
```
---

> from `majkee`: 7, 9 can hold some new fresh heads, than you have to list them as you need, your launch and kill acording roster.



# spawnable (sub)agents `{claude, codex, vendor neutral (germline)}`

> sometimes can be name of agent same as spawnable subagent, normal in LLM world.

1. `houston` - architect, vendor neutral
2. `trajectory` - senior developer, coding design|tasks, claude 
3. `delta` - junior developer, claude
4. `epoch` - researcher (local|internet according request), claude
5. `researcher` - researcher (local|internet according request), codex
6. `astrobley` - senior developer, coding design|tasks, codex
7. `oraculum` - advisor, high thinking models by default, vendor neutral
8. `atlas-ui` - harness expert, claude 
9. `harness expert` - harness expert, codex
10. `assay` - step auditor tracker, claude 

---

