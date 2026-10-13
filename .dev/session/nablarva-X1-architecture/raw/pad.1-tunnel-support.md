# pad.1-tunnel-support — every open tunnel item, with stable bashes to test or decide it

> Operator test + decision surface. Sequential inside an item: run a step, paste the output under
> `>MAJKEE report`, then the next step. Items are independent, so take them in any order.
> Driver: trajectory(support). Evidence lives in the support vault (T-entries); this PAD is raw.
> Item close: tick exactly one of the last two boxes. **resolved** = done, with its evidence pasted
> here. **in process** = claimed, with who and when written on that line.

Paths used in all commands:
```
BED   /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture
HEAD  01a118ff-674c-7680-9e57-67ca2f257323          (live Cartan head, compacted 2026-10-08 18:01)
VAULT /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-architecture.trajectory.2026-10-08.md
```

Precondition: an interactive zsh **opened after 2026-10-08 21:50**, so that the `tn-check` alias
exists (ia-sync `134b08f`, copied live). An older pane needs `exec zsh` first.

---

## STEP 0 — state check (non-destructive, run before any item)

```zsh
type tn-check && tn-check --id 01a118ff-674c-7680-9e57-67ca2f257323 --cwd /home/hruzam/unikuklatrix/nablarva; echo "exit=$?"
```

Expected: `tn-check is an alias…`. The verdict is one of:
- `READY` (0): no TUI holds the head, so the tunnel can resume it.
- `HELD` (3): a TUI or the daemon holds the head. Item A tells you how long the hold lasts.
- `BROKEN` (4): STOP and paste the output; trajectory reads it.
- `command not found`: the shell is too old. Run `exec zsh` and retry.

>MAJKEE report 0
```zsh

```

---

## A · writer-lock release after TUI `/exit` (F1, on 0.161 CLI / 0.162 daemon) — TEST

Why: if the daemon keeps holding the head after the TUI leaves, the tunnel can never resume it.
On 0.160.1 the hold cleared after about 3 min. Nobody has measured it on the 0.162 daemon.

### A1 — exit the TUI that sits on the head
In the Codex TUI started 16:35 (`codex resume --all`, pid 16989), type `/exit`. Then:
```zsh
date +%T; pgrep -af 'codex resume' ; echo "---"; fuser ~/.codex/thread-writer-locks/01a118ff-674c-7680-9e57-67ca2f257323.lock
```
Expected: no `codex resume --all` line, and a holder pid still printed (the daemon).

>MAJKEE report A1
```zsh

```

### A2 — time the release (polls for up to 15 min; read-only)
```zsh
t0=$(date +%s); for i in {1..90}; do fuser ~/.codex/thread-writer-locks/01a118ff-674c-7680-9e57-67ca2f257323.lock >/dev/null 2>&1 || { echo "released after $(( $(date +%s) - t0 )) s"; break; }; sleep 10; done; [[ $i -eq 90 ]] && echo "STILL HELD after 900 s"
```
- `released after N s` → paste it. Proceed to item B.
- `STILL HELD after 900 s` → this is a finding, not a dead end. Paste it, then run
  `pgrep -af app-server` and paste that too. Trajectory files it as F1 evidence. Do NOT kill the daemon.

>MAJKEE report A2
```zsh

```

- [ ] resolved
- [ ] in process —

---

## B · re-open the vault on HEAD with the preamble (T14 recipe, corrected id) — TEST

Needs: STEP 0 or A2 gives READY. Spends no quota (resume only).

### B1 — open and resume
```zsh
tn-on /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture -- --thread 01a118ff-674c-7680-9e57-67ca2f257323 --cwd /home/hruzam/unikuklatrix/nablarva --sandbox workspace-write --preamble /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/tunnel.preamble.md
tn-check; echo "exit=$?"     # must say READY before resume — HELD = the daemon still holds the head after the TUI exit (T18): wait, re-run
tun resume; echo "exit=$?"
tn-check; echo "exit=$?"
```
Expected: `open: enabled …`, then `resume` with exit 0, then `VERDICT READY`. The policy line should read
`effort=high … approvals_reviewer=auto_review`.
- exit 61 or `-32600 … active writer` → the head is still held. Go back to A2.
- `VERDICT BROKEN` → STOP and paste.

>MAJKEE report B1
```zsh

```

- [ ] resolved
- [ ] in process —

---

## C · first ask with the preamble, after compaction (F13a + L8 live ask) — TEST

Needs: B resolved. **Spends one short turn.** By protocol the carrier sends turns; you may send this
one yourself as operator, or hand it to oraculum.

### C1 — one short ask
```zsh
export TUNNEL_CODEX_STATE=/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/tunnel.state.json
TUNNEL_CODEX_TIMEOUT=600 zsh ~/.config/zsh/ai/tunnel-codex.zsh ask "majkee(operator) · tunnel check · Reply with ONE line: your thread id and the last cycle you remember. No file reads, no tools." ; echo "exit=$?"
```
Expected, all three:
- stderr shows `tunnel-codex.py: preamble …tunnel.preamble.md (N chars) prepended`;
- exit 0;
- stdout ends with `[usage: ctx=…]`, which should be low after the 18:01 compaction (well under 50 %).
  That figure is the head's new baseline.

What a miss means:
- no `prepended` line → the preamble is not wired. Paste it.
- exit 30/40 → run `tun read` first, never resend.
- a ctx near the old 74 % → the compaction did not take. Paste it.

>MAJKEE report C1
```zsh

```

- [ ] resolved
- [ ] in process —

---

## D · selftest on 0.161 CLI + 0.162 daemon (L8; it was cut short tonight by the memory reaper) — TEST

Spends no quota. Run it when memory is calm.
```zsh
zsh ~/.config/zsh/ai/tunnel-codex.selftest.zsh 2>&1 | tail -5; codex --version
```
Expected: `113/113` (or `pass … fail 0`).
- Any fail → paste the tail. A version-skew failure is filed as an L8 finding.
- If `codex --version` now prints 0.162.x, the CLI caught up. Note it.

>MAJKEE report D
```zsh

```
trajectory 2026-10-09 00:20: `codex --version` → 0.162.0 (CLI caught up; daemon 0.162.0) · live selftest 134/134 · 6 live asks + 2 compactions on scratch 01a11d5e (T21).

- [x] resolved — trajectory, T21
- [ ] in process —

---

## E · effort on the head: keep `high` or return to `medium` (T15 §3) — DECIDE

Facts:
- The bed protocol says `medium`. The head runs `high` (every turn_context since 00:55Z).
- `high` costs more reasoning per turn and invites more reads.
- Changing it in the TUI re-injects 6–22 kB of developer blocks (F12).
- **Since 2026-10-09:** `tun open --override effort=medium` (on the open vault). It is sent on the next turn and
  persists in the thread, so to revert you set the old value. No TUI is needed (T21).

Decision (write it):
```
effort =            · reason:
```

- [ ] resolved
- [ ] in process —

---

## F · journal §1.1.4 correction (your file, your hand) — DECIDE/DO

`new one : 01a113d8-c5b0-…` is wrong. That id is the X0 zero-turn thread and has no rollout.
The live head is `01a118ff-…`, which the 18:01 compaction kept. Proof:
```zsh
tn-check --id 01a113d8-c5b0-7343-a927-cb960dd641f7; echo "exit=$?"
```
Expected: `VERDICT BROKEN — no rollout`, exit 4.

- [ ] resolved
- [ ] in process —

---

## G · who rewrites the bed protocol's stale lines (T15 §3 table) — DECIDE

Stale in `tunnel-using-protocole.md`:
- L22 effort and reviewer line;
- L63 version;
- §Approvals: it calls the blind spot silent, but it is policy-dependent; `.codex/` is read-only;
- §Where things go: X0 paths;
- head id `01a113e0` (it is now `01a118ff`).

Options:
- **carrier (oraculum):** it is her bed policy;
- **trajectory:** on your word, as one diff for you to review.

```
owner =
```

- [ ] resolved
- [ ] in process —

---

## H · commits and pushes owed — DECIDE

```zsh
git -C /home/hruzam/ia-sync log --oneline origin/main..main
git -C /home/hruzam/unikuklatrix/nablarva status --short
```
- **ia-sync** `134b08f` (tn-check + backlog F12–F16) is pushed (2026-10-08 22:20). The tn-back/tn-rebind commit is local only:
  `git -C /home/hruzam/ia-sync push`.
- **nablarva**, uncommitted:
  - support vault T12–T16 and this PAD: carrier's bookkeeping;
  - `tunnel.preamble.md`;
  - `.codex/` and `raw/houston.config.toml.candidate`: held for the probe and assay witness, not mine.
- **full `deploy.sh`** is still pending (it ships other seats' agents and hooks): yours.

- [ ] resolved
- [ ] in process —

---

## I · canonical home for the preamble wording (T14 open item) — DECIDE

Options:
- **(a)** vendor-neutral template in reposoma `raw.guides/tunnel/res/`, plus nablarva's wording beside the
  tunnel policy in `.dev/`;
- **(b)** keep the bed instance until X1 closes, then decide.

```
home =
```

- [ ] resolved
- [ ] in process —

---

## J · F16 lifecycle verbs (`tun compact` · `tun rebind` · fork successor) — BUILD ORDER

**Update 2026-10-09 (T21):** steps 1 and 2 are DONE. `tun compact` is built and live-proven on scratch
(41.5 % → 12.0 %, id kept, no TUI); `tun rebind` exists as `tn-rebind`. Left: the fork successor probe
(`thread/fork`) on scratch.

```
go for probe =  yes / later
```

trajectory 2026-10-09 00:35: fork probed, and `tun fork` built + live chain fork→rebind→back proven (T22, F20).

- [x] resolved — trajectory, T22

---

## K · lifecycle routines with the new verbs (T19) — first real use = TEST

Needs a shell opened after 22:40, or `exec zsh` first. Check: `tn-help` lists `tn-back` and `tn-rebind`.

### K1 — compress → back (the id is kept)
**Since 2026-10-09 the tunnel can do it alone, with no TUI:**
```zsh
tn-use /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture
tn-check && tun compact; echo "exit=$?"
```
Expected: `compact: thread … compacted in N s … id kept`. The next ask shows a low `ctx=`. The TUI route below still works.
Do this when the head's ctx is high, with no turn in flight:
```zsh
cd /home/hruzam/unikuklatrix/nablarva && codex resume 01a118ff-674c-7680-9e57-67ca2f257323
#   in the TUI:  /compact   then   /exit
tn-use /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture
tn-back; echo "exit=$?"
```
Expected: `[tn-back] writer free after N s — resuming …`, then `resume exit=0 · tn-check exit=0`.
That N is item A's number on 0.162. Paste it.
- exit 3 → the TUI is still open somewhere: `pgrep -af 'codex resume'`.

>MAJKEE report K1
```zsh

```

### K2 — successor (`/clear` in the TUI, new id)
```zsh
cd /home/hruzam/unikuklatrix/nablarva && codex resume 01a118ff-674c-7680-9e57-67ca2f257323
#   in the TUI:  /clear  → /status (copy the NEW id) → send ONE line, e.g. "hello, short ack" (it creates the rollout) → /exit
tn-check --id NEW_ID --cwd /home/hruzam/unikuklatrix/nablarva; echo "exit=$?"
tn-rebind /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture --thread NEW_ID --reason "ctx reset"; echo "exit=$?"
tn-back; echo "exit=$?"
jq -c '.lineage' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/tunnel.state.json
```
Replace `NEW_ID` (three places) with the id from `/status`.
Expected: `tn-check` READY or HELD, `tn-rebind` exit 0 with `carried: …preamble=…tunnel.preamble.md`, `tn-back` exit 0, and a lineage entry old→new.
Then the carrier sends the rebrief ask (journal §1.1.4 has the text).
- `tn-rebind` exit 4 → the new id has no turn yet, or it is the wrong id. The vault is unchanged.

>MAJKEE report K2
```zsh

```

- [ ] resolved
- [ ] in process —

---

## parked
