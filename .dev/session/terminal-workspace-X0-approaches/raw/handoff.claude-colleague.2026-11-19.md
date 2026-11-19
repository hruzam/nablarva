# claude-colleague handoff — terminal-workspace X0 → X1 proposals

2026-11-19 · inferred: claude-colleague (Claude Code, Trajectory persona) · written at Majkee's
request for the move to the office host. **Proposals only.** No gate, VERDICT, STATUS or release
is changed. Cartan has not yet verified cycle 01, and only his VERDICT dispositions it.
Companion to `handoff.cartan.2026-11-17.md`, which is Cartan's pen and was left untouched.

Evidence and citations: `_bus/01.claude-colleague.return.md` (RETURN 01). This file distils it;
on any conflict, the RETURN and its cited sources win.

## Read next

1. `STATUS.md` owns the position (next = Cartan verifies RETURN 01 and writes `01.cartan.verdict.md`).
2. `_bus/01.claude-colleague.return.md` §4 (M1–M8) and §5. That is the full argument.
3. `raw/next-experiment.proposal.2026-11-18.md`, the proposal these changes apply to.

## Position in one line

**Revise X1, don't replace it.** As written it re-proves the probe and builds receipt machinery for a
one-client batch executor. The operator's intent is two parties in one shell
(`request.majkee.2026-11-17.md:7`).

## Proposed X1 delta (smallest coherent change)

| Change | What | Why |
|---|---|---|
| **+ Row A: second client** | A synthetic attach client on the same PTY takes input ownership (generation bump). The executor holds all dispatch while it's held. After handback, a queued request runs only after re-confirmation. Detaching leaves the shell alive. | Turns "batch executor" into "two parties, one shell" without needing a live human. |
| **+ Row B: busy foreground** | A command request submitted while a `read` fixture waits is **held**, not consumed as the answer. | The cooperation-critical failure; currently untested. |
| **− Markdown history, current-state snapshot** | Drop from X1. | Derivable, and neither is evidence. |
| **Restart = new incarnation** | State that executor death ⇒ shell death (the fixture holds the PTY master). Restart tests only prove `unknown` reconciliation with no replay, plus stale-target rejection. | Prevents a false claim of shell survival. Survival needs a separate PTY holder, which is the reuse question. |
| **Define duplicate** | Same request id → no-op that returns existing state. Same content with a new id → a new request. | The proposal leaves it undefined. |

All within X1's existing effect envelope: stdlib Python + Bash, private `/tmp`, owned PTY, no tmux/zellij
server, no native CLI.

## Mechanism sketch (advice to the X1 launcher author, not an adopted format)

- **Submit** = atomic rename of a finished draft into `submit/`. Never close/save (inotify `IN_CLOSE_WRITE` ≠ ready).
- **Adopt** = the executor copies the bytes to `approved/<id>.sh` and records sha256 + target incarnation. The
  hash must be in a frozen synthetic allowlist (X1's "approval"). The shell sources only that copy.
- **Same-UID honesty:** the binding is cooperative (the agent can rewrite `approved/`). Label it so.
- **Wire bytes:** the executor writes only `__tw_run <id>\n` to the PTY. Content never travels as terminal
  input (avoids echo, control-character interpretation and the 4096-char canonical line truncation).
- **Three signals, three facts:**
  - `done/<id>.exit` (out-of-band, via tmp + rename) = execution complete.
  - OSC 133 A/B/C/D emitted by the shell = output slicing + prompt readiness (terminal appearance only).
  - `waitpid` = shell ended.
  - A timeout is `unknown`, never "failed, retry".
- **Write-ahead:** record `dispatched` before writing bytes. One request in flight at a time.
- **Request kinds:** X1 implements `command` only. `input` (bytes to a foreground program) is rejected,
  and the rejection is tested.
- **Three independent axes:** execution scope (which hashes may run) · input owner (generation) ·
  lifetime (detach ≠ kill).
- **Records:** per-request files plus one executor-written `events.jsonl`. No schema adopted.
- **Corpus must include shell-hostile harmless cases:** `exit`, `set -e`, a stdin reader, a `trap` change.

## Native-path observation (SOURCE: Claude Agent View docs, retrieved 2026-11-18)

- `claude --bg --exec 'bash …'` plausibly gives a supervisor-owned persistent PTY shell with documented
  **human** attach and agent-readable `claude logs`.
- On that page the only input route is an agent-view TUI reply "as typed input". Output is held in memory
  only and expires ~5 min after exit.
- Codex `exec_command`/`write_stdin` is the inverse: agent-side PTY, no documented human attach.
- Inference: both vendors and the X1 fixture leave the same gap open: **one PTY, two clients, arbitrated input.**

## Proposed role for this seat in a released build

1. *Preferred:* a **parallel reuse lane**, with disjoint files and its own release. Qualify
   `claude --bg --exec bash` against X1's frozen corpus: attach/detach, `claude logs` fidelity, the absence
   of scripted input, Ctrl-C/EOF, cleanup, output expiry.
2. *Alternative:* **oracle author before build.** Write the frozen expectations and adversarial fixtures
   blind to the implementation.

Either way Cartan stays the sole integration owner and a third seat (Assay/Oraculum) verifies. This seat
does not verify what it authored.

## Open questions for Majkee (decisions, not mine to take)

- Accept the two-row revision into X1, or keep X1 narrow and open the second-client case as X2?
- Release the native Claude shell-job lane in parallel (needs native CLI launch authority), or defer it?
- Is a synthetic second client enough for the X1 gate, or must you personally attach once as witness?

## Not established

Nothing above was executed. The "no scriptable send" finding covers the Agent View page only, not the
CLI reference. The Codex facts are the researcher's, not re-fetched. Remaining uncertainty: RETURN 01 §6.
