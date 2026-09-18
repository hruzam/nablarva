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
REHEARSAL
? --:-- phone "Okay, it doesn't work. I have to simulate ... when I switch off from this application window, I'm losing your voice regime."
S4 --:-- phone
S2 --:-- phone
S1 --:-- phone
S3 --:-- phone
S4 --:-- phone
? --:-- phone "the connection to my tmux session on my computer has fallen"
S2 --:-- phone
S4 --:-- phone
? --:-- phone "switch off the Tailscale connection and switch on again"
S4 --:-- phone
S2 --:-- phone
? --:-- phone "the buffer is lost"
S4 --:-- phone
S3 --:-- phone
S4 --:-- phone
S5 --:-- phone
S6 --:-- phone
S4 --:-- phone
S2 --:-- phone
? --:-- phone "we now switched five minutes ahead, for example"
? --:-- phone "Cartan is stuck on a bash confirmation"
S6 --:-- phone
W --:-- phone
? --:-- phone "we are three and a half minutes ahead"
S8 --:-- phone
S2 --:-- phone
S4 --:-- phone
? --:-- phone "It is lasting fifteen seconds for example."
S3 --:-- phone
S4 --:-- phone
S3 --:-- phone
S3 --:-- phone
S4 --:-- phone
? --:-- phone "It's taking five seconds when I'm still on the proper window ... it takes me fifteen seconds for example."
S5 --:-- phone
S7 --:-- phone
? --:-- phone "depending on how challenging the reply is it might be from two minutes to fifteen"
S6 --:-- phone
X5 --:-- phone
```

## Totals

By ID:
- `S1`: 1
- `S2`: 5
- `S3`: 5
- `S4`: 10
- `S5`: 2
- `S6`: 3
- `S7`: 1
- `S8`: 1
- `S9`: 0
- `W`: 1 — not counted as an action
- `?`: 10
- `X1`: 0
- `X2`: 0
- `X3`: 0
- `X4`: 0
- `X5`: 1
- `X6`: 0

By device:
- `phone`: 40
- `pc`: 0
