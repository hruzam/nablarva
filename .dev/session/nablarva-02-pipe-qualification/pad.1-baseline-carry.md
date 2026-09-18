# pad.1-baseline-carry — count one manual carry (POINT 03 → Cartan)

> Operator test surface. Sequential — one step, report back, next step.
> Driver: oraculum (cSharp). Listener: majkee's voice agent — it transcribes, never interprets.
> Reading home: `raw/baseline.md` §Readings (the driver transcribes; this PAD is the raw surface).

## Listener = the `stenograph` skill (majkee's instrument — supersedes any rule list here)

The voice agent runs `res/skills/stenograph/skill.stenograph.md` (Claude-skill copy: `SKILL.md`
beside it). It defines the line form `<ID> <phone-clock time> <device> [recovery] [words]`, the
S1–S9 / W / `?` events, the lifecycle marks `X1` noise · `X2` [TAB] loop marker · `X3` pause ·
`X4` resume · `X5` stop · `X6` rewind, the `special …` control prefix, and the flush contract
(YAML typology + one chronological block + totals). This PAD points at it and adds nothing.

**Phone limitation, observed in the 2026-09-14 rehearsal:** switching app windows ends the
voice regime, so events cannot be voiced *while* carrying on the phone. Allowed real methods:
(a) perform one step, return to the voice window, voice it **with the time said aloud**
("S4 twelve thirty-one phone"), repeat — never reconstruct a batch from memory later;
(b) carry on the PC with the phone as the recorder. Say `special stop` at the end.

## Shared constant (used verbatim in every step)

    POINT: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/03.oraculum.point.md
    CARRY LINE: Read and act on /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/_bus/03.oraculum.point.md — you are seat cartan; resolve your seat first. Baseline remeasure on this cycle: log R1–R6 per raw/baseline.md in RETURN §3.
    CARTAN WINDOW: the living Codex session, thread ending c57d8

## Precondition

Cartan's session is alive; POINT 03 exists; `_bus/03.cartan.return.md` does **not** exist yet.
If it already exists, the carry happened by pull — skip to STEP 3.

### STEP 0 — state check (non-destructive)

Say, to the listener or to oraculum: which device you are on (`phone` / `pc`), whether Cartan's
window is on the same device, and whether the listener is running and has the rules.

Expected: three answers. Branch:
- listener not ready or unsure of the rules → STEP 0′ first
- RETURN 03 already on disk → STEP 3
- otherwise → STEP 1

>MAJKEE report 0
```zsh

```

### STEP 0′ — REHEARSAL (done 2026-09-14 mobile — `raw/human-relay-time-logs/rehearsal.mobile.telemetry.2026-09-14.md`; never a reading)

Say "rehearsal". Voice a made-up carry end to end **without touching Cartan's window**
(e.g. "S1 20:01 phone · S2 20:01 · S3 20:02 · S4 20:02 · S5 20:02 · S6 20:02 · W · S8 20:10 · S9 20:10"),
then say "flush". Check the block: one line per event, ids, times, device, totals.

Expected: a well-formed `REHEARSAL` block. Branch:
- malformed → fix the listener's rules, repeat once
- well-formed → STEP 1. The rehearsal stays in this fence only; it never enters `raw/baseline.md`.

>MAJKEE report 0′
```zsh

```

### STEP 1 — the REAL carry

Say "real". Then do the carry exactly as you normally would — locate the POINT path, copy it,
switch to Cartan's window, paste the CARRY LINE, submit — voicing each event **immediately after
it happens, with the time said aloud** (phone: step → back to the voice window → "S5 twelve
thirty-two phone"), one id per action, no batching, no reasons. Anything typed beyond the carry
line is `S7`. Use `special pause` / `special resume` if a Tailscale drop interrupts you.

Expected: the listener holds a growing `REAL` block; nothing to report yet.
Branch: if Cartan visibly already started on POINT 03 before your paste → do not paste; say "pull" → STEP 3.

### STEP 2 — flush the sender log

Say "flush". Paste the block below (or send it to oraculum verbatim in chat).

Expected: header `REAL`, N lines, totals per id and device.
Branch: any `?` lines → oraculum asks one question per `?`; nothing is guessed.

>MAJKEE report 2
```zsh

```

### STEP 3 — pull path (only if Cartan read the POINT before any paste)

Report exactly: `pull · S1 <time> · S8 <time> · S9 <n>`. A near-zero count is a valid reading.

>MAJKEE report 3
```zsh

```

### STEP 4 — the return leg

When Cartan tells you "RETURN on disk" (however it does), voice `S8` and every `S9`, say "flush"
again, paste the appended block.

Expected: the `REAL` block now ends with S8/S9 lines. Oraculum transcribes the whole block into
`raw/baseline.md` §Readings and pairs it with Cartan's R1–R6 from RETURN 03 §3.

>MAJKEE report 4
```zsh

```

## Verdict mapping

| block | becomes |
|---|---|
| `REAL` with ≥1 line | reading, transcribed verbatim into `raw/baseline.md` |
| `REHEARSAL` | instrument check only; stays here; never a reading |
| no block | `unknown` — recorded as such, never estimated |

## parked
(driver appends off-pad questions here)
