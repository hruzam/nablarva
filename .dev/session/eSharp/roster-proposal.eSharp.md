---
date: `2026-11-25`
scope: `eSharp groups roster`
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

# 0. `side-quest`

> to `eSharp` : with `myShell` tmux session|window|pane: `$36 | 3 myShell @59 | %61`
> ***collect syntax due session work experiences***
> - for 'alien code' - that what is understable (best: naturaly). I know for LLMs is not comfortable languague like syntax, rather have their own natural jargon, pokes worked as understable. Cosider how much dos part can have sideeffect.
> - roster bulding experinces
> - does `supervisor *(supervisorCli)*` fulfiling your expectations? Even episthemic or socratic: what would be optimal rosters for `eSharp` multisessions (?), can it save tokens, can progress work more, what gives us, what cost us, what are consequencess? 
> - caching -> best options . `majkee`s note: think best can be hold attached to tmux-window identity (?)
>   So can serve as continuity safe lock, but thin. 
> - solve episthemic|socratic Q2 : `poke` and its possible usage as semi-mail instead tool bash to shared terminal in later phase.
> - --> SYNTAX, CACHE can be part of `eSharp` property or even project property in optimal meaning.
> - solve episthemic|socratic Q3: how to design `runbook` or similar shape in case `eSharp` aaproach aproove itself?
> to `eSharp` END 

---

# 1. `eSharp`

---

vendor: `claude`
agent: `trajectory`
posture|nick: `eSharp|*`
tmux session|window|pane: `$36 | 0 eSharp @75 | %77`

---

**TMUX MAP: `helloWorld`**

```bash
tmux list-windows -t helloWorld -F '#{session_id} | #{window_index} #{window_name} #{window_id} | #{pane_id}'
$36 | 0 eSharp @75 | %77
$36 | 1 supervisor-relay @57 | %59
$36 | 2 seniorDev @58 | %60
$36 | 3 myShell @59 | %61
$36 | 4 auditor @64 | %66
$36 | 5 exec @66 | %68
$36 | 6 lead @68 | %70
$36 | 7 spare-codex @100 | %102
$36 | 8 supervisorCli @73 | %75
$36 | 9 spare-claude @76 | %78
```
---


# 2. `ovitmugen` : `session-window-X*`

---

vendor: `claude`
agent: `flight`, `claude-opus-5-5`, `effort xhigh`
posture: `lead|trajectory|delta|epoch|assay`
tmux session|window|pane: `$44 | 0 lead @78 | %80`

scope:

---

vendor: `codex`
agent: `oraculum`, `gpt-6.2-astra`
posture: `audit|houston|astrobley`
tmux session|window|pane: `$44 | 1 audit @79 | %81`

scope: co-thinking| honest critique in conceptual phase. Audit when arrives build part. Can provide tests.

---

`+ supervisorCli`

---

**TMUX MAP: `seswin`**
```bash
tmux list-windows -t seswin -F '#{session_id} | #{window_index} #{window_name} #{window_id} | #{pane_id}'
$44 | 0 lead @78 | %80
$44 | 1 audit @79 | %81
```
---


# 3. **ovitmugen|termbrana** : `terminal-workspace-X*`

---

vendor: `codex`
agent: `*(main 'cartan')*` , *(set on `gpt-6.1-sol` manualy by me)*
posture: `lead.seswin|houston|oraculum|astrobley|researcher|harness-expert`
tmux session|window|pane: `$45 | 0 lead @80 | %82`

scope:

---

vendor: `claude`
agent: `flight` *(set on `claude-fable-5-2` manualy by me)*
posture: `audit.terwor|houston|trajectory|assay|delta|epoch|atlas-ui`
tmux session|window|pane: `$45 | 1 audit @81 | %83`

scope: co-thinking| honest critique in conceptual phase. Audit when arrives build part. Can provide tests.

---

`+ # 4. shared`

**TMUX MAP: `terwor`**
```bash
tmux new-session -d -s terwor -n lead -c ~/unikuklatrix/nablarva
tmux new-window  -d -t terwor: -n audit -c ~/unikuklatrix/nablarva
tmux list-windows -t terwor -F '#{session_id} | #{window_index} #{window_name} #{window_id} | #{pane_id}'
$45 | 0 lead @80 | %82
$45 | 1 audit @81 | %83
```

---

# 4. shared

## 4.1. `supervisorCli` *(ex controller by function not by tmux session)*

> to trajectory: one shared or per group? or each group one?
> to trajectory END
vendor: `codex`
agent: `*(main 'cartan')*`
posture|nick: `supervisorCli|houston|astrobley|oraculum`
thinking: `gpt-6.1-sol max`
tmux session|window|pane: `$36 | 8 supervisorCli @73 | %75`
cwd: `~/unikuklatrix/nablarva`

scope: 
> to trajectory: u brief. i propose also making caches by js -> `CACHE.<#{window_name}>.md`. 
> Should be also providing second continuity of steream.
> to trajectory END


## 4.2. `seniorDev`

vendor: `codex`
agent: `oraculum`
posture: `seniorDev|houston|astrobley`
tmux session|window|pane: `$36 | 2 seniorDev @58 | %60`
cwd: `~/unikuklatrix/nablarva`

scope: for `eSharp` co-thinking| honest critique in conceptual phase. Audit when arrives build part. Can provide tests. 
> to `eSharp` : FYI `helloWord` leader : `$36 | 6 lead @68 | %70` will have enough capable partner in auditor: `$36 | 4 auditor @64 | %66`, so everybody will have enough co-brains online from another vendor. You need to brief in propper time.
> to `eSharp` END.

---

# 5. spawnable subagents `{claude, codex, vendor neutral (germline)}`

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

# 6. SANDBOX

`sandbox-server` is a separate tmux server. Its `sandbox` session has four shell
windows. Use `-L sandbox-server` to target this server. Window and pane IDs are
local to each server.

```bash
tmux -L sandbox-server list-windows -t '=sandbox' -F '#{session_id} | #{window_index} #{window_name} #{window_id} | #{pane_id}'
```

```text
$0 | 0 codex-sample @0 | %0
$0 | 1 claude-sample @1 | %1
$0 | 2 session @2 | %2
```

Attach from a fresh terminal with `tmux -L sandbox-server attach-session -t '=sandbox'`.

---

# X . additional

## contract between `eSharp` *(trajectory)* & `majkee`

> to `eSharp` : accepting points as was proposed in text bellow: 
***Four rules***
1. One seat is one window with one pane; no split in a seat's window.
2. No dot in a window name. tmux reads a dot in a target as the pane separator: a read-only query for helloWorld:lead.zzz answered with the relay lead's pane %70. The nicks keep their dot (lead.seswin); the windows are lead and audit inside seswin.
3. Never a seat on a -L server. The sandbox server is made by the group's prepared script, after your yes on the release.
4. Names stay once a seat has started.
> to `eSharp` END.

---

