---
date: `2026-11-25`
scope: `eSharp groups roster`
---




syntax: 
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

# 1. `eSharp`

vendor: `claude`
agent: `trajectory`
posture|nick: `eSharp|*`
tmux window: ``

## 1.1. subagents `{claude, codex, vendor neutral (germline)}`

1. `houston` - architect, vendor neutral
2. `trajectory` - senior developer, claude 
3. `delta` - junior developer, claude
4. `epoch` - researcher (local|internet according request), claude
5. `researcher` - researcher (local|internet according request), codex
6. `astrobley` - senior developer, codex
7. `oraculum` - advisor, vendor neutral
8. `atlas-ui` - harness expert, claude 
9. `harness expert` - harness expert, codex
10. `assay` - step auditor tracker, claude 

---

# 2. `ovitmugen` : `session-window-X*`

---

vendor: `claude`
agent: `flight`
posture: `lead.seswin|houston|trajectory|delta|epoch`
tmux window: `lead.seswin`

scope:

---

vendor: `codex`
agent: `oraculum`
posture: `audit.seswin|houston|astrobley`
tmux window: `audit.seswin`

scope: co-thinking| honest critique in conceptual phase. Audit when arrives build part. Can provide tests.

---

`+ supervisorCli`

---

# 3. **ovitmugen|termbrana** : `terminal-workspace-X*`

---

vendor: `codex`
agent: `*(main 'cartan')*`
posture: `lead.seswin|houston|oraculum|astrobley|researcher|harness-expert`
tmux window: `lead.terwor`

scope:

---

vendor: `claude`
agent: `oraculum`
posture: `audit.terwor|houston|trajectory|assay|delta|epoch|atlas-ui`
tmux window: `audit.terwor`

scope: co-thinking| honest critique in conceptual phase. Audit when arrives build part. Can provide tests.

---

`+ supervisorCli`


# 4. `supervisorCli`

> to trajectory: one shared or per group? or each group one?
> to trajectory END
vendor: `codex`
agent: `*(main 'cartan')*`
posture|nick: `supervisorCli<.if by slug seswin,...>|houston|astrobley|oraculum`
thinking: `gpt-6.1-sol max`
tmux window: `supervisorCli.<if by slug seswin,...>`

scope: 
> to trajectory: u brief. i propose also making caches by js -> `CACHE.<posture>.md`. Should be also providing second continuity of steream.
> to trajectory END

