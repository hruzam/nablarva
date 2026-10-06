---
artifact: stenograph-log
schema: 1
event_typology:
  S1: notice a POINT waits
  S2: locate or open path/target
  S3: copy
  S4: switch window/application/screen/session
  S5: paste
  S6: submit/Enter/send
  S7: type anything extra
  S8: notice a RETURN exists
  S9: switch and relay back to Oraculum
  W: wait (logged, not an action count)
  '?': uncertain; Majkee words verbatim
  X1: voice noise/correction/repeat request
  X2: '[TAB] dialogue-loop group marker'
  X3: pause
  X4: resume
  X5: stop
  X6: rewind; new attempt, prior evidence retained
device_values: [phone, pc]
time_source: phone clock when voiced
---

```text
S1–S9 = manual relay/action events
W     = waiting; logged but not counted as an action
X1–X9 = lifecycle/context/evidence markers; not ordinary action counts

X3 pause  -> recording suspended, block remains open
X4 resume -> recording continues
X5 stop   -> block closes
X6 rewind -> new attempt, previous evidence preserved
X7        -> current arc
X8        -> current session
X9        -> long-output reading boundary

SESSION LOG

X7 5:57 AM pc arc runbook
X8 5:57 AM pc session Astroblay / Codex
X7 5:57 AM pc arc tunnel
X8 5:57 AM pc session Trajectory

S7 --:-- pc typed /rename and Home.Trajectory.Tunnel
S6 --:-- pc submitted rename

S8 1:01 AM pc Trajectory full output arrived
X9 1:01 AM pc read start
X9 --:-- pc read end; attention moved to Codex return

S8 --:-- pc Codex runbook return noticed
S4 --:-- pc switched to terminal tab 2

S7 1:05 AM pc typed src / zsh reload
S6 1:05 AM pc submitted reload
S7 1:05 AM pc typed rb open path
S6 1:05 AM pc submitted rb open
S4 1:05 AM pc returned to deploy
S7 1:05 AM pc typed bash deploy command
S6 1:05 AM pc submitted deploy; deployment finished

S4 --:-- pc returned to testing window
S7 --:-- pc typed RB Open with path
S6 --:-- pc submitted RB Open
S7 --:-- pc tested pane resizing/help bar
S7 --:-- pc tested help board and copy/paste
S7 --:-- pc tested arrow and Ctrl+Shift+arrow navigation

W 1:09 AM pc still testing

S4 1:10 AM pc switched to terminal tab 1
X7 1:10 AM pc arc runbook
X8 1:10 AM pc session Astroblay / Codex
S7 1:10 AM pc started writing feedback

S4 --:-- pc switched to terminal tab 2
S7 --:-- pc typed run health
S6 --:-- pc submitted run health
S4 --:-- pc returned to terminal tab 1 / Astroblay
S7 1:15 AM pc continued writing feedback

S7 --:-- pc typed green/amber/red workflow protocol feedback

S4 1:19 AM pc switched to tunnel arc
X7 1:19 AM pc arc tunnel
X8 1:19 AM pc session Trajectory
S7 1:19 AM pc confirmed placement of new protocol

S4 1:19 AM pc returned to runbook arc
X7 1:19 AM pc arc runbook
X8 1:19 AM pc session Astroblay / Codex

S6 1:20 AM pc sent reply to Astroblay
S4 --:-- pc switched to tunnel arc

S4 1:22 AM pc returned to Astroblay for bash/git confirmation request
S4 1:22 AM pc returned to tunnel / Trajectory
X9 1:22 AM pc read start
X9 1:22 AM pc read end due to pause

X3 1:22 AM pc pause

X4 1:24 AM pc resume
X9 1:24 AM pc read start Trajectory output
X9 --:-- pc read end; switching device

S4 --:-- pc switched from home host to mobile phone
S2 --:-- phone located Trajectory session

S7 1:28 AM phone voice-dictated question to Trajectory about Codex session resume/transcript identity
S6 1:31 AM phone sent voice message to Trajectory
W 1:31 AM phone waiting for Trajectory response

S4 1:31 AM phone switched to runbook / Astroblay output
X7 1:31 AM phone arc runbook
X8 1:31 AM phone session Astroblay / Codex
X9 1:31 AM phone read start programming feedback
X9 1:52 AM phone read end

S4 1:52 AM phone switched to terminal tab 2 / testing
S7 1:52 AM phone killed older process
S7 --:-- phone typed bash deploy command
S6 --:-- phone submitted deploy; deploy finished
S7 1:33 AM phone started runbook

S7 --:-- phone tested board/view
S7 --:-- phone tested navigation
S7 --:-- phone tested context search
W 1 hour 66 minutes phone still testing; looks fine

S4 --:-- phone Alt+1 to terminal tab 1
X7 --:-- phone arc runbook
X8 --:-- phone session Astroblay / Codex
S7 --:-- phone reported test feedback

S4 --:-- phone switched to virtual desktop 3
X7 --:-- phone arc meta terminal
X8 --:-- phone session meta terminal

S3 1:40 AM phone copied /tmp address/supporting tmux commands
S4 1:40 AM phone switched to virtual desktop 1 / terminal tab 1
X7 1:40 AM phone arc runbook
X8 1:40 AM phone session Astroblay / Codex
S5 1:40 AM phone pasted/gave supporting tmux commands as feedback
S6 --:-- phone sent message

S4 1:46 AM phone switched to tunnel arc
X7 1:46 AM phone arc tunnel
X8 1:46 AM phone session Trajectory
X9 1:46 AM phone read start Trajectory output

X9 1:50 AM phone read end due to Astroblay bash confirmation
S4 1:50 AM phone switched to runbook / Astroblay
S6 1:50 AM phone pressed Y and confirmed bash request
S4 1:50 AM phone returned to tunnel / Trajectory
S7 1:50 AM phone started typing answers to Trajectory
```

```text
TOTALS BY ID

S1   0
S2   1
S3   1
S4  20
S5   1
S6  11
S7  22
S8   2
S9   0
W    3   [not an action]

X1   0
X2   0
X3   1   [not an action]
X4   1   [not an action]
X5   0   [block still open]
X6   0
X7  10   [not an action]
X8  10   [not an action]
X9  10   [not an action]
?    0

ordinary S actions: 58
recorded lines total: 93

BY DEVICE

pc:    53 lines
phone: 40 lines
```
```

## Totals

By ID:
- `S1`: 0
- `S2`: 8
- `S3`: 6
- `S4`: 14
- `S5`: 3
- `S6`: 18
- `S7`: 17
- `S8`: 10
- `S9`: 3
- `W`: 7 — not counted as an action
- `?`: 20
- `X1`: 0
- `X2`: 0
- `X3`: 0
- `X4`: 0
- `X5`: 0
- `X6`: 0

By device:
- `phone`: 0
- `pc`: 106
