# Build description — the carrier under the bus law

*Oraculum · Claude · 2026-09-30 · session `nablarva-00` · PRIMARY DRAFT.*
*Describes what would be done. Not a runbook, not a schedule, not code. Closed scope by
scope with Majkee; each scope carries its decisions at the end. Nothing here is a lock.*

Evidence marks as in [audit 1](audit.patterns-and-loop.oraculum.2026-09-29.md) §0, plus
`[C]` = Cartan's independent read, `[K]` = code read of `~/ia-sync/zsh/` on 2026-09-30,
spot-checked by Oraculum at the cited lines.

## 0. What is being built, in one paragraph

The gaveled bus law (`~/reposoma/raw.guides/bus/GUIDE.md`, `runbook/res/csharp-head-protocol.md`,
`runbook/res/fanout-turns.md`) defines the head, the seats, the file shapes, the cycle and
the verification. It declares transport and notification out of scope: "The operator is
the transport" `[R: csharp-head-protocol line 64]`. **nabLarva's first protocol is that
transport.** It carries files between living sessions and tells the right session that a
file is there. It edits no law, replaces no brick, and owns no agent's process.

Not built in this run: a broker, a room journal, a UI, a PTY monitor. The PTY monitor is
kept as a future producer of the same envelope (§3); nothing here depends on it and
nothing here prevents it.

## 1. Application-first frame

**The envelope is the invariant.** What produces it and what consumes it will change;
the envelope, the completion rule and the notice do not.

| Layer | Owns | First run uses |
|---|---|---|
| 5 · Human view | What Majkee sees | runbook browser, ovitmugen, as they are |
| 4 · Process and terminal | tmux, PTY, sensing | nothing new; the monitor arrives later as a producer |
| 3 · Runtime connection | attraction per vendor | one adapter per vendor, smallest possible |
| 2 · Exchange | envelope, completion, notice, brakes | **this build** |
| 1 · Durable work | repos, locks, STATUS | as they are |

Rules that hold across layers:
- A layer's signal never becomes another layer's truth. A busy pane is not a delivery.
- A toolbox works without the animal. The animal consumes what a toolbox publishes. A
  toolbox never imports the animal. (Majkee, 2026-09-29.)

## 2. The envelope contract

### 2.1 From the law, taken as-is `[R: bus/GUIDE.md]`

| Element | Rule | Line |
|---|---|---|
| Home | `<session>/_bus/`, born only when two seats are active | 15, 30 |
| Name | `NN.<seat>.<kind>.md`; kind is `point`, `return` or `verdict`; seat is the writer | 30–35 |
| POINT header | `cycle`, `from`, `to`, `scope`, `paths`, `gates`, `done_when`, `return_to` (absolute path) | 64–73 |
| RETURN body | six mandatory sections | 80–102 |
| VERDICT header | `cycle`, `point`, `return`, `verified_by`, `disposition`, `gate_effect`, `status_rewritten` | 141–150 |
| Writer | single writer per file; a correction is a new cycle | 52–55 |

The runbook browser already parses this grammar `[K: runbook.py line 685]` and shows "return
present, no verdict" `[K: lines 703–709]`. The carrier reuses the same pattern and never a
second one.

### 2.2 Pinned for the carrier (practice drifts; the carrier needs one answer)

| Element | Pin | Why |
|---|---|---|
| Reply destination | `return_to:` in the POINT, absolute path, always present | muticula used `verdict_path`; session 03 has `00.*` files with no POINT `[S]`. A carrier needs one field |
| Correlation | `cycle` plus the POINT path in the RETURN header (`answering:` or `point:`) | Practice uses both spellings; pick one in scope 2 |
| Identity of the reply's author | the `seat` in the filename, plus `from:` | as law |

### 2.3 Added by the carrier

**Completion rule.** A bus file is written under a temporary name in the same directory
and renamed to its final name in one step. A file exists under its final name if and only
if it is complete. No reader ever sees a fragment. Proposed temporary suffix: `.part`.
Source of the technique: pre-consultation file lines 444–451 `[S]`; standard practice.

**Notice.** One line, carrying a pointer and nothing else:

    nabla: <kind> for <seat> · cycle <NN> · <absolute path>

The notice rides the attraction step. Content never rides it. (Relay seam: only a
pointer travels `[R: brief.relay-seam.v2 line 29]`; bus law: "may point a seat at the next
filename" `[R: GUIDE.md line 57]`.)

**Addressed block, as an interface only.** Later producers (a hook, a PTY monitor) will
need to cut "this part is for seat X" out of free output. The carrier defines only the
marker's meaning: a start line naming `to`, `kind`, `cycle`; an end line; the text between
becomes the body of a bus file with the same completion rule. Exact spelling is scope 2's
decision. The cutting tool itself stays where lock L8 puts it, in `applications-in-common`;
this is the OUTPUT(A) interface that L8 says gets one boundary note.

## 3. Producers of the envelope, in order of arrival

| # | Producer | How the file appears | State |
|---|---|---|---|
| 1 | **The agent itself** | Writes the RETURN with its own file tool, then renames | In use today, minus the rename |
| 2 | **A hook** | On `Stop`, checks that the expected file exists under its final name; emits the notice | Hooks documented on both vendors `[C]`, `[W]`; nothing run |
| 3 | **A PTY monitor** | Cuts addressed blocks from the terminal stream; writes them as bus files | Future. The onion plan and the driller's "detect prompt return" belong here |

Producer 1 is enough for the first run. Producer 2 is the first stone after the probe.
Producer 3 is the builder's line and is not on the first run's path.

## 4. The relay layer: the pieces that do not exist

Each is small. Each has one input and one output. Together they are "the engine" for
protocol 1.

| Piece | Input | Output | Notes |
|---|---|---|---|
| **R1 publish** | a drafted bus file | the same file under its final name, headers validated | atomic rename; refuses a file whose `return_to` is missing |
| **R2 watch** | a session directory | one notice per newly complete bus file | the same check the browser makes every second `[K: runbook.py lines 1759, 1861]`, outside the TUI. One-shot from a hook, or a foreground loop the operator owns |
| **R3 attract** | a notice and a seat | delivery through that seat's vendor adapter, or a visible "no route" | one adapter per vendor; the fallback is the operator |
| **R4 bind** | seat name | vendor, host, session or thread handle | a small JSON registry in the style of `zsh/registries/*.json` `[K]`; one outstanding exchange per bound recipient (design r1) |
| **R5 brake** | an exchange | stop when its cycle cap, budget or deadline is reached; report `unknown` on uncertainty | never a blind retry; "NO faster than YES" |

None of these owns a process. R2 as a loop is the only long-running piece, and the
operator starts and stops it in the foreground until a lifecycle decision is earned.

## 5. Attraction per vendor: what is documented, what is not

| Direction | Candidate surface | Established | Missing |
|---|---|---|---|
| → Claude, idle | An armed asynchronous hook with `asyncRewake`, waiting for one expected file; exit 2 wakes the session | Documented `[C]` | Not run on this host |
| → Claude, any state | Cross-session messaging over the per-session Unix socket | Documented for Claude-to-Claude `[W]` | Foreign client protocol not established `[C]` |
| → Claude, opted in | Channel: an MCP server pushes a notice | Documented, research preview `[W]` | Requires launch with the channel flag |
| → Codex, thread on app-server | `codex queue --thread --message`; `turn/start` | Help and schema confirmed on 0.158.0 `[C]` | Queue admission, live-TUI ownership, busy behaviour untested |
| → Codex, plain TUI | unknown | — | Whether it is addressable at all |
| Codex → anything, on turn end | `Stop` hook with `session_id`, `last_assistant_message` | Schema confirmed `[C]` | Not exercised |

## 6. Bricks as they are

| Brick | What the relay consumes | What it must never ask |
|---|---|---|
| runbook browser | nothing at runtime; the same filename grammar | to send, wake or write into `_bus/` |
| ovitmugen | `ov ls --json`: tabs with `busy`, `fg`, `left` `[K: ovitmugen.py line 540]` | to type into a pane; to treat `busy` as readiness |
| tunnel (`tun`) | the stored-thread handle in its state file, for R4 | to reach a living TUI; it owns its own server |
| `codex-run.zsh` | nothing; consultation stays separate | to be a bus leg |
| temple mail | the addressed-file convention as prior art | an acknowledgement; it has none by design |
| muticula | write discipline beside the bus | delivery |
| termbrana, ommatermia, onion | nothing in the first run | to become prerequisites |
| vendor hooks | JSON on stdin at `Stop`, `UserPromptSubmit`, `SessionStart` | to wake an idle session without `asyncRewake` |

## 7. Stones

Each stone has a done test and names what it fills in the larger shape. Order is a
proposal; dates belong to the contract plan.

| # | Stone | Done when | Fills |
|---|---|---|---|
| S0 | Envelope pinned | Scope 2 closed; one example set (point, return, verdict) written by hand under the pinned headers, shown correctly by the runbook browser | §2 |
| S1 | Publish and watch, offline | Fixture directory; R1 renames, R2 emits exactly one notice per complete file and none for a `.part`; selftest with no tmux, no vendor, no network | R1, R2 |
| S2 | Return wake, Claude | Cartan's probe as described in the addendum §4: a disposable idle Claude session resumes on its own and answers with the nonce; negative controls hold | R3 for Claude |
| S3 | Codex facts | On a disposable thread: does `Stop` fire with `session_id`; what does `codex queue` do to an idle thread; documented result, even if negative | R3 for Codex |
| S4 | One cycle without carriage | On office, one head and one worker of different vendors, one POINT and one RETURN, no human relay; measured against the 2026-09-14 baseline | the loop |
| S5 | Bind and brake | R4 registry with two seats; R5 stops a runaway fixture at its cap | R4, R5 |

Out of the first run: the second host, cross-host transport, fan-out to several workers,
the hook producer as default, the PTY producer, any UI.

## 8. Where it lives

| Question | Proposal | Lock touched |
|---|---|---|
| First stones | `~/ia-sync/zsh/experimental/<id>/runner.zsh`, loaded lazily by the dispatcher; a syntax error makes the command absent, not the shell dead `[K]` | none |
| After S2 passes | a `relay/` scope: `base.zsh`, `keyboard.zsh`, one engine; one source line added to both host configs in the same session `[K: SYNC_DISCIPLINE lines 150–157]` | L6: animal code source home is Majkee's decision |
| The nablarva scope (`nab`) | left alone until its dead verbs are repaired; not extended by the relay `[K]` | — |
| Language | shell for R1–R5 as described; nothing here needs more | docket 2 stays open |

## 9. Decisions by scope

| Scope | Decisions | State |
|---|---|---|
| 1 Frame | trust sphere; Oraculum as head; builder and Codex seats; pulse row; bus law over HANDSHAKE | presented 2026-09-30 |
| 2 Envelope | correlation spelling; `.part` suffix; notice text; marker spelling | next |
| 3 Probe | target, owner, one-shot hook, trust exception, quota ceiling; which bed hosts it | after 2 |
| 4 Bricks and home | experimental first, relay scope after S2; source home under L6 | after 3 |
| 5 Monitor | builder's assignment as producer 3; L8 boundary note | after 4 |
| 6 Docket | ratify 6; re-table 1 as S4; park the rest | after 5 |
| 7 Working tree | commit; close sweep; orphans | when at a computer |

## 10. What this draft does not know

- Whether `asyncRewake` behaves on the installed Claude 2.1.285.
- Whether a plain Codex TUI can be reached, and what `codex queue` does to an idle thread.
- Whether Z's four predicted failure modes for a files-only bus (locking, fan-out, cursor
  races, restart) have ever occurred in `_bus/` practice.
- The exact fields the builder's monitor will need from the envelope; scope 5.
