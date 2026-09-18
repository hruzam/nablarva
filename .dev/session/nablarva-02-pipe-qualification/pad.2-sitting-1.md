# pad.2-sitting-1 — open a private endpoint, read it once, send nothing

> Operator test surface. Sequential — one step, report back, next step. Driver: oraculum (cSharp).
> Engineering steps are Cartan's; [HANDS] steps are majkee's. Reports go into the fences; the
> distilled result goes to VERDICT 04. Native disposition stays STOP unless evidence says otherwise.
> Source of the commands: `raw/route.r2.md` §2–§4 (Cartan, accepted in VERDICT 03).

## Recording this sitting (same instrument as pad.1)

Run the stenograph (`res/skills/stenograph/skill.stenograph.md`) in `real` mode for the whole
sitting. At each step boundary say `special tab step N` — the skill logs `X2` with that
sentence, which segments the flush by step; narrate with `?` as you like; say the time aloud.
Outputs (what the commands printed) still go into the fences below; the flush artifact goes to
`raw/human-relay-time-logs/` and the head copies its times into the fences. Nothing changes in
the skill.

## Shared constants (verbatim in every step)

    PRIVATE SOCKET  /run/user/1000/nablarva-b-entry-20260913-01.sock
    REMOTE URI      unix:///run/user/1000/nablarva-b-entry-20260913-01.sock
    WORKSPACE       /tmp/nablarva-b-entry-20260913-01
    DISPLAY NAME    nablarva-b-entry-20260913-01
    READER          python3 -B /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/raw/probe/qualify.py
    NEVER           /run/user/1000/codex-pocket-test.sock · thread …c57d8 · thread 0a27e884… · the ia-sync TUI (…9cea3c)

## Precondition

STATUS carries `open_approval:` for this sitting (STEP 1). Without that line nothing after STEP 0 runs.

### STEP 0 — state check + non-interference baseline (head, read-only, metadata only)

```sh
ss -xl | grep -c -F -- '/run/user/1000/nablarva-b-entry-20260913-01.sock'
ls -ld /tmp/nablarva-b-entry-20260913-01; find /tmp/nablarva-b-entry-20260913-01 -mindepth 1 -maxdepth 1 -print
ls -la /home/hruzam/.codex/app-server-control/
stat -c '%y %n' /home/hruzam/.codex/auth.json
```

Expected: count `0`; scratch `drwx------ hruzam`, empty; control dir listing recorded; auth mtime
recorded (mtime only — contents are never read). Branch: count ≠ 0 or scratch not empty → STOP, no
cleanup by any seat. Otherwise → STEP 1.

>ORACULUM report 0
```zsh

```

### STEP 1 — open_approval ([HANDS] · gavel)

Say, in one line: `open_approval: sitting-1 · private socket /run/user/1000/nablarva-b-entry-20260913-01.sock · one TUI attached, default settings, workspace /tmp/nablarva-b-entry-20260913-01 · granted by majkee <date>`.
The head transcribes it into STATUS `holds:` verbatim. It authorizes exactly one server and one
TUI, nothing else, and expires when either process ends or the sitting is closed.

>MAJKEE report 1
```zsh

```

### STEP 2 — start the private server ([HANDS 1a])

In a tmux window whose working directory is the scratch (`cd /tmp/nablarva-b-entry-20260913-01`), run in the foreground:

```sh
codex app-server --listen unix:///run/user/1000/nablarva-b-entry-20260913-01.sock
```

Expected: the process stays in the foreground; no prompt for login; no error. Branch: any login/trust/
permission prompt → STOP and report it verbatim, do not answer it. Paste the first lines it prints.

>MAJKEE report 2
```zsh

```

### STEP 3 — bracket-after (head, read-only)

```sh
ss -xl | grep -F -- '/run/user/1000/nablarva-b-entry-20260913-01.sock'
ls -la /home/hruzam/.codex/app-server-control/
stat -c '%y %n' /home/hruzam/.codex/auth.json
ss -xlp | grep -i codex | grep -v -F 'nablarva-b-entry' | cut -c1-160
```

Expected: exactly one LISTEN line whose address field is the exact private path; the control-dir
listing unchanged (no new `*.sock`, no new lock); auth mtime unchanged; the only other codex
listener still pocket-test. Branch: any change in the control dir or auth mtime, or a second
private listener → STOP; server is closed by majkee (Ctrl-C in its window); record everything.

>ORACULUM report 3
```zsh

```

### STEP 4 — open the attached TUI ([HANDS 1b])

In a second tmux window, working directory the scratch:

```sh
codex --remote unix:///run/user/1000/nablarva-b-entry-20260913-01.sock -C /tmp/nablarva-b-entry-20260913-01
```

Then, in that TUI: `/rename nablarva-b-entry-20260913-01`, then `/status`.
Report: thread UUID · display name · cwd · remote address/version if shown · model · approval policy ·
sandbox · login/plan indicator as shown (no account identifiers, no tokens) · time opened · whether the
TUI feels normal. Branch: no UUID visible → STOP (a separately approved identity source is needed; no
tokenless list). Any override, unexpected login mode or trust prompt → STOP, do not repair.

>MAJKEE report 4
```zsh

```

### STEP 5 — armed_target (head, from STEP 4 only)

The head writes into STATUS: `armed_target: <UUID> · nablarva-b-entry-20260913-01 · /tmp/nablarva-b-entry-20260913-01 · hruzam-120922 · <opened_at> · route unix:///run/user/1000/nablarva-b-entry-20260913-01.sock · instance <what /status showed, or unknown>`.
Nothing is invented; an incomplete tuple is not an armed target.

>ORACULUM report 5
```zsh

```

### STEP 6 — armed_approval: inspect ([HANDS] · gavel)

Say: `armed_approval: sitting-1 · permitted action inspect · one bounded read · granted by majkee <date> · expires on any target/server change`.
The head transcribes it, then mints the interlock for exactly this target (public data:
`nablarva-inspect-v1:` + sha256 of `<socket path>` + NUL + `<uuid>`), and hands Cartan the exact
reader command from `raw/route.r2.md` §4 with the observed UUID, the token and the canonical
launch-evidence JSON.

>MAJKEE report 6
```zsh

```

### STEP 7 — one bounded read (Cartan, engineering; released once)

Cartan runs the reader command exactly once and pastes its JSON output: label, `read_route_observed`,
route/version, `id`, `sessionId`, `cwd`, status type, `activeFlags`, `updatedAt`.
Expected: `thread/list` returned exactly one entry matching the UUID and workspace; label
`STOP_IDENTITY_UNKNOWN` is the *expected good outcome* here (idle summary read; incarnation unproved)
— it is a successful read, not a failure. Branch: `BLOCKED` / `STOP_ROUTE_UNKNOWN` / 0 or 2 list
results → record, no retry, sitting ends. Note the reader's wall time from the head's clock.

>CARTAN report 7
```zsh

```

### STEP 8 — close the sitting ([HANDS])

Report whether both working TUIs (Cartan …c57d8, the ia-sync one) behaved normally throughout; then
close the attached TUI (`/quit` or Ctrl-C) and the server (Ctrl-C). Head repeats STEP 0's four
commands: count `0`, scratch still empty (a `qualification.return.md` must NOT exist — nothing was
sent), control dir unchanged, auth mtime unchanged. No send happened in this sitting by design.

>MAJKEE report 8
```zsh

```

## Verdict mapping

| observation | means |
|---|---|
| STEP 3 or STEP 8 shows control-dir or auth mtime change | non-interference REFUTED for private servers → STOP; next sibling re-designs |
| STEP 4 shows UUID + normal TUI; STEP 7 reads exactly 1 thread, `STOP_IDENTITY_UNKNOWN` | read route OBSERVED on a private endpoint (`UNVERIFIED-native` for delivery); sitting 2 may ask for `characterize` / `send-once` |
| STEP 7 `BLOCKED` / route unknown / 0 or 2 results | route not established → cycle 04 corrective, or STOP |

## parked
(driver appends off-pad questions here)
