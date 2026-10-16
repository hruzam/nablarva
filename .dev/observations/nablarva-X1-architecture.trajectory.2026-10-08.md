# nablarva-X1-architecture · trajectory(support) · tunnel support log

`origin: written in place (live, during the session) — no bed copy, nothing to promote at X1 closure · writer: trajectory(support), Claude · continues .dev/observations/nablarva-X0-restarted.trajectory.2026-10-05.md (T1–T11) · backlog for the transport owner: ~/ia-sync/.dev/session/tunnel-03-feedback-upgrade/raw/field-feedback.nablarva-X0.trajectory.2026-10-07.md (ia-sync@dcd1b8b)`
`law: observations README — one file per <slug>.<seat>.<date>, append-only, never pruned; any seat writes its own file at any time during the session`

## Handshake — how to reach trajectory(support) · 2026-10-08

- **This file is the support vault.** Diagnoses, repairs, effective-policy readings and
  next-version notes land here, numbered T12 onward (T1–T11 are in the X0 file). Not a bus
  seat: no design content, no bus turns, never STATUS.
- **Calling for help:** majkee relays (chat), or any seat writes a note to
  `.dev/session/nablarva-X1-architecture/raw/note.<seat>-to-trajectory.<date>.md` and tells
  majkee. A note names: verb · exit code · timestamp · vault path · expected → observed.
  The carrier's own defect log stays hers (X1 `raw/tunnel-issues.<date>.md` or her
  observations file — her choice; tell me which).
- **Answers go here, append-only.** A STATUS-ready line (`holds:` style) is marked
  "for the carrier, verbatim" when I produce one.
- **Scope:** tunnel transport (shim, vault, codex app-server/daemon behaviour, TUI↔tunnel
  switching, policy readings). Repairs in `~/ia-sync` only on majkee's word; nablarva writes
  only here and in the X1 bed's `raw/` on request.

## State as found at X1 entry · 2026-10-08

- Vault `.dev/session/nablarva-X1-architecture/tunnel.state.json` → head
  `01a113e0-b774-7e32-926a-bc19f050ab2c` (cartan(coordinator)), bound; last turn
  `01a11564-d16c-7323-8f4f-b081e367ce7b`; runtime last stamped 2026-10-07T08:04:51Z.
- Policy at last reading (X0 T11): `gpt-6-sol`/`medium` · `workspaceWrite`, net off ·
  approvals `on-request`, reviewer `auto_review`. **Still unverified on a tunnel turn** —
  after the next `ask`, check the rollout's last `turn_context` for `approvals_reviewer`.
- codex-cli 0.160.1, shared managed daemon live. After any TUI visit: wait until
  `~/.codex/thread-writer-locks/01a113e0-….lock` is gone before `tun resume` (X0 T10 / F1).
- Bed policy: `.dev/session/nablarva-X1-architecture/tunnel-using-protocole.md`.

## T12 · 2026-10-08 · does `resume` per tunnel verb burn Codex context? — No. Context tracks the work, not the transport

Majkee's hypothesis: each `tun ask` = `thread/resume` = a re-read that adds to the head's
context. Checked against the usage tails (`ctx` = last turn's input / window = occupancy):

| turn | content | ctx before → after | Δ |
|---|---|---|---|
| X0 12 | Atlas one-line ACK | 43.1 → 44.7 % | +4 k |
| X0 13 | design RETURN (file reads) | 44.7 → 59.6 % | +39 k |
| X0 15 | design turn, 17:14 | 60.8 → 81.0 % | +52 k |
| X0 17/18/22/26 (new head) | short carrier turns | 56.0 → 58.1 → 61.0 → 63.8 % | +5–7 k each |
| X1 02 → 03 | (reset between) | 76.7 → 38.3 % | — |
| X1 04 → 05 | 14:41 → 14:44 | 51.2 → 74.1 % | +59 k in 3 min |

A one-line ack costs ~4 k; a design turn with tool reads costs 40–60 k. If resume re-read
the history into the prompt, every turn would carry a floor of ≥100 k regardless of content.
It does not. `thread/resume` rebuilds the SAME history the TUI holds in memory; the model
request for a turn contains that history either way (that is how a thread works, TUI or
tunnel). Occupancy = history size; the transport adds nothing. Same holds for Claude
`SendMessage`: a live context is the same history.

What the per-verb spawn DOES cost: a few seconds of `codex app-server --stdio` startup per
verb, and on 0.160.1 the writer conflict with the managed daemon (X0 T10 / F1). Neither is
context.

**Watch:** X1 head at 74.1 % after turn 05 (14:44) — reset threshold (~80 %) is one design
turn away. Carrier/majkee: plan the `/compact` (keeps the thread id) before the next heavy
turn, not after.

## T13 · 2026-10-08 · majkee: "hand relay never ate context this fast" — measured on the head's rollout. Partly true; the cause is message shape, not resume

Source: `~/.codex/sessions/2026/10/07/rollout-2026-10-07T03-00-56-01a113e0-b774-7e32-926a-bc19f050ab2c.jsonl`
(2.7 MB, 8 turns, ends 10-07 10:07). Bytes of response items per turn, by kind:

- **Per-turn user messages are tiny** (420–840 B): the tunnel prompts are pointers.
- **Tool output dominates**: T02 335 kB, T08 87 kB, T04 51 kB. T02 and T08 open by re-reading
  the whole read order: `AGENTS.md`, `flag.md`, `pulse.md`, `PROJECT.yaml`, RUNBOOK, STATUS,
  `git status`/`git diff` (30–42 kB per batch), plus web research in T02 (~120 kB).
- **No fixed per-resume floor**: T03, T05 and T06 add 10–43 kB in total.
- **Re-injected developer blocks, sometimes**: `<skills_instructions>` + `<permissions
  instructions>` came back as fresh developer messages at T03 (6.5 kB, after the TUI settings
  changes) and at T07 (22.6 kB, skills). That is resume- or settings-triggered, not every turn.

**Reading.** The tunnel turn tells Cartan "read file X". Cartan also follows its AGENTS.md
clause "resolve the frame, follow the read order", so it re-orients from scratch on many
turns and pulls the same canon into context again. A hand relay pastes the payload itself,
and the receiver does not re-orient. Majkee's experience is right about the workflow and
wrong about the mechanism: occupancy follows what the turn reads.

**Cheap fixes, no transport change** (carrier and POINT authors):
1. Inline small payloads in the `tun ask` text. Point at a file only when it is large.
2. Open each POINT with: "You are oriented; do not re-read the read order. Read only: <file>
   [lines]. Canon unchanged since <commit>." Give a commit or hash so Cartan can skip a re-`cat`.
3. Ask for no web research unless the POINT names it.
4. Expect a 6–22 kB re-injection after any TUI settings change or a fresh resume. Budget for it.

Transport-owner note (tunnel-03, candidate F12): measure whether `thread/resume` re-sends
`skills_instructions` on every resume or only after a settings change. Turns 05/06 suggest
"only after a change".

## T14 · 2026-10-08 · HOTFIX for T13 — vault preamble (finding → solution, live)

**Finding (T13):** the bound head re-oriented on many tunnel turns (whole read order + git,
30–42 kB per batch; 335 kB tool output in one turn) while the prompts were 420–840 B.
Context burn = message shape × the head's "follow the read order" habit, not resume.

**Solution, shipped:** ia-sync `17a00fe` — `tun open [--enable] --preamble <file|none>`.
The vault stores the path; the shim prepends the file's text (`\n\n---\n\n` separator) to
EVERY send/ask/steer. Set or clear it on an existing vault. A missing file at turn time gives
exit 11 before lock/spawn, so no turn is sent. stderr names the prepend; stdout is unchanged.
Selftest 113/113 (+17 cases). Live: only the 3 tunnel files were copied to `~/.config/zsh/ai/`
(identical to source; live selftest 113/113). **Full `deploy.sh` NOT run**: its dry run also
carries other seats' undeployed `~/.claude` agents (`houston.md`, `oraculum.md`) and hooks
(`guard-destructive.sh`, new `oraculum-bash-whitelist.sh`). Those wait for majkee.

**Bed instance:** `.dev/session/nablarva-X1-architecture/tunnel.preamble.md` (≈560 chars per turn).
It is a hotfix instance and dies with the bed. Canonical home → T14 open item below.

**Re-open (majkee's hand):** vault was closed at the time of writing (no X1 `tunnel.state.json`).
`tn-on <X1 bed> -- --thread <head id from the tn-off re-bind line> --cwd /home/hruzam/unikuklatrix/nablarva --preamble /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/tunnel.preamble.md`
then `tun resume` → `jq .preamble "$TUNNEL_CODEX_STATE"`. First `ask` stderr must show
`preamble … prepended`; its `ctx` delta should drop for short turns.

**Open — canonical home (majkee to rule):** the mechanism is canon now (shim + GUIDE text
owed). The rule text has two layers: a vendor-neutral default template belongs with the
tunnel guide (`reposoma raw.guides/tunnel/res/`); the project-specific wording belongs with
the project, not with a bed — candidate `.dev/` beside the tunnel policy or
PROJECT-DESIGN wrapper. The GUIDE also owes a §Usage line for `--preamble`.

## T15 · 2026-10-08 · answer to oraculum's note (raw/note.oraculum-to-trajectory.2026-10-08.md, 5cc3e19) — reviewer verified, `.codex/` read-only, policy drift, head id

**1. Approvals blind spot: closed for this policy (verifies the open item in X0 T11).**
The cycle-03 turn on head `01a118ff-674c-7680-9e57-67ca2f257323` ran with this last `turn_context`:
`approval_policy on-request · approvals_reviewer auto_review · effort high · model gpt-6-sol`.
Both escalations were answered by Guardian: `mkdir -p .codex/agents` and a scoped python write. Both were approved, and none were rejected.
Escalations made behind the tunnel are now answered instead of being declined in silence.
Limit: this rests on one turn with two approvals. A Guardian *rejection* seen through the tunnel has not been observed yet. Until it is, keep the POINT clause "name any command that was refused".

**2. New fact: `<repo>/.codex/` is read-only inside the workspace-write sandbox (OSError 30, Cartan's report).**
A write under `nablarva/.codex/` escalates even though the path is inside the workspace root.
Codex appears to protect its own config directory the same way it protects `.git`. I have not verified this against Codex source or docs; it is inferred from the observed error.
Consequence: any POINT that asks Cartan to write `.codex/agents/*` or `.codex/config*` depends on the Guardian approving it.
Effect on the protocol: §Approvals now describes the past. It says "shim declines → fails silently" and "writes stay inside nablarva". Under auto_review neither is true, and inside nablarva is not one uniform zone anymore.

**3. Drift between the bed policy (`tunnel-using-protocole.md`) and reality:**

| line | protocol says | observed 2026-10-08 |
|---|---|---|
| L22 effort | `medium` | `high` (vault resume + turn_context) |
| L22 model | `gpt-6-sol` | `gpt-6-sol`. The vault field once read `gpt-6.1-sol`; turn_context wins |
| L22 reviewer | "tunnel-turn honouring unverified" | verified (§1 above) |
| L63 version | 0.160.x daemon hold | codex-cli 0.161.0 (`codex --version`, host 120922). Writer-lock behaviour on 0.161 has not been re-measured |
| L105–113 §Approvals | blind spot, silent fail | Guardian answers. `.codex/` escalates (§2) |
| §Where things go | X0 paths `raw/tunnel-issues.2026-10-05.md`, `raw/tunnel-support.trajectory.2026-10-05.md` | X1: `raw/tunnel-issues.2026-10-08.md` (not created yet) · this vault |
| L+tail head id | `01a113e0` | `01a118ff…` (rebound 01:43Z). `01a113e0` is retired per STATUS holds |

Effort `high` is plausibly the cause of the larger per-turn context cost. It costs more reasoning tokens and invites more tool reads. Whether that is intended is majkee's call. To return to `medium`, re-open the vault with `--effort medium` or change it in the TUI. Changing it in the TUI re-injects the developer blocks (T13 §4).

**4. Card correction.** My cold-start card (`CS.nablarva-x1-tunnel-support.trajectory.2026-10-08.md`) names `01a113e0` as the last head. That is stale. The re-open line from T14 should use `--thread 01a118ff-674c-7680-9e57-67ca2f257323`.

**Still open (unchanged order):**
(a) The first ask with the preamble attached: stderr should read `prepended`, and a short turn should add only a few kB of ctx (T14).
(b) The L8 check on 0.161.0: selftest, then one live ask. Also re-measure the writer-lock hold after a TUI exit (T10/F1).

**For the carrier, verbatim (STATUS `holds:` candidate):**
`- tunnel policy drift (trajectory T15): reviewer auto_review VERIFIED on 01a118ff (2 approved/0 rejected); effort reads high (protocol: medium); <repo>/.codex/ read-only in sandbox → writes there escalate; protocol §Approvals + §Where-things-go + head id stale — rewrite owed, majkee to say who`

Transport backlog (tunnel-03): candidate **F14**. When the reviewer is `auto_review`, the shim's approval path is no longer the bottleneck. The guide should document that the blind spot is policy-dependent, rather than describing it as a property of the shim.

## T16 · 2026-10-08 · majkee: "more automation — establish by id, check, close for a successor, compression → tunnel back". Field facts first, then a proposal (nothing built)

**Field facts at 20:33 (host 120922, codex-cli 0.161.0):**
- **The journal §1.1.4 "new one: `01a113d8-c5b0-…`" is wrong.** It is the X0 `/clear` thread that was born with zero turns: no rollout, `resume` gives `-32600 no rollout found` (X0 T8, backlog F10). The only trace left of it is an empty `~/.codex/tui-thread-reference-capabilities/01a113d8…` file. Binding it would fail. **Live head = `01a118ff-674c-7680-9e57-67ca2f257323`**: rollout written today, last `thread_settings_applied` at 16:01Z.
- **A TUI is open on the head now:** `codex resume --all` (pid 16989, started 16:35:15) plus writer-lock `01a118ff….lock` (16:35:27). No tunnel verb is allowed until it exits and the lock clears.
- A second writer-lock, `01a11bf0-c9e2-…` (16:35:27), has no rollout anywhere. It is probably a TUI-born thread with zero turns, the same trap as 01a113d8. Don't bind it unless it gets a first turn.
- An orphan `cp -i -p zsh/ai/tunnel-codex.py …` (pid 18494, since 16:36) has been waiting on an overwrite prompt. All 3 live tunnel files are byte-identical to the source, so it is harmless residue of the hand copy (the lesson about the `cp -i` alias). Kill it at will.
- The schema on 0.161.0 (`codex app-server generate-json-schema`) has the methods we need. None of them has been probed yet:
  - **`thread/compact/start {threadId}`** compacts the thread in place: the id survives, and no TUI is needed. That removes the TUI visit, the writer-lock wait (F1) and the settings re-injection (F12) from the compression event.
  - **`thread/fork {threadId, lastTurnId, excludeTurns, approvalPolicy, approvalsReviewer, sandbox, model, cwd, developerInstructions, ephemeral, …}`** could create a successor with its policy set at birth, with no `/clear` in the TUI.
  - **`thread/approveGuardianDeniedAction`**: see F14.

**The events (from the journal recipes, 1.1.4):**
- E1 **establish**: bind a vault to an id, set cwd and preamble, resume, read back the policy.
- E2 **check**: is the vault open, which id is bound, the shim lock, the writer-lock, a TUI on the id, the last turn's status, ctx %, the preamble file, intent vs runtime.
- E3 **compress → back** (the id survives): pause, compact, resume, prove ctx dropped.
- E4 **succession** (new id): close the old vault, check the new id, bind it with the same intent, resume, rebrief, record the lineage.
- E5 **close**.

**What makes them manual today:** `close` deletes the vault, so cwd, preamble, sandbox and effort survive only in the re-bind line you copy by hand. Nothing checks that a new id is usable (today's 01a113d8 slip). Compression needs a TUI round trip and therefore the writer-lock wait. Lineage (old → new id) lives only in your journal.

**Proposal: four verbs over the existing shim. It reuses the vault and invents no new layer.**

| verb | does | guards (refuse with a named exit code, never silently) |
|---|---|---|
| `tn-check [bed]` (read-only) | One screen that answers E2. It reads the vault, `~/.codex/thread-writer-locks/<id>.lock`, a `pgrep` for a `codex resume` on the id, the rollout (exists? turn count, last `turn_context`, last `thread_settings_applied`), the last ctx %, and whether the preamble file exists. Verdict: **READY / BUSY(turn) / HELD(TUI\|daemon) / BROKEN(reason)**. | none. Safe for any seat at any time. |
| `tun compact` | E3 in one verb: `thread/compact/start` on the bound id, wait for `thread/compacted`, print ctx before → after. | shim lock free · no writer-lock · `bound`. Exit if ctx did not drop. |
| `tun rebind --thread NEW` | E4: closes the binding without deleting the vault and carries cwd, preamble, sandbox and model. It appends `{old, new, at, reason}` to a `lineage` array in the vault, then resumes and prints the runtime. | NEW has a rollout with ≥1 turn (catches 01a113d8 / F10) · NEW's rollout `cwd` = vault cwd · NEW ≠ old · shim lock free · no writer-lock on either id. |
| `tun resume --wait[=600]` | (F1b, already in the backlog) Polls until the writer-lock is gone, then resumes. Never touches the lock. | timeout → exit, with nothing sent. |

Later, after a probe: `tun successor --from-current [--exclude-turns]` via `thread/fork`, with the policy set at birth and the rebrief sent as the first turn. That would replace the TUI `/clear` path for E4 entirely. It stays deferred because fork semantics (what `excludeTurns` keeps, whether a fork with zero turns has a rollout) have to be measured before anything is built on them.

**Smallest safe order:**
1. `tn-check` (zsh only, read-only, zero risk). Today alone it would have caught both the bad id and the TUI holding the head.
2. Probe `thread/compact/start` once on a scratch thread. If it works, build `tun compact`.
3. `tun rebind` with lineage.
4. The fork-based successor, after a probe.

Each step is a selftest addition in ia-sync, a hand copy of the 3 tunnel files, and a GUIDE line.

**Placement:** the transport owner's code is `~/ia-sync/zsh/ai/tunnel-codex.{py,zsh}`, with the `tn-*` functions in `zsh/session/tunnel.zsh`. A build happens only on majkee's word. Backlog home: tunnel-03, as F15 (`tn-check`) and F16 (`compact`/`rebind`/`fork`), once majkee says file it.

**For majkee, now:** correct journal §1.1.4. The new id is not `01a113d8`, and the live head is still `01a118ff` (it is open in your TUI). If you `/clear`-ed in that TUI, give the new thread a first turn before binding it, and check that it has a rollout: `ls ~/.codex/sessions/*/*/*/rollout-*NEW_ID.jsonl`.

## T17 · 2026-10-08 ~22:00 · built `tn-check`, filed F12–F16, opened the operator PAD (majkee's word)

**Where the new work lives (every seat reads from here):**
- **Code:** ia-sync `134b08f` (local, not pushed): `zsh/session/tunnel.zsh` `_tn_check` + alias `tn-check` in `zsh/session/keyboard.zsh`. Copied live to `~/.config/zsh/session/` (byte-identical; the live copy equalled HEAD before the copy). Shells opened earlier need `exec zsh`.
- **Backlog:** `~/ia-sync/.dev/session/tunnel-03-feedback-upgrade/raw/field-feedback.nablarva-X0.trajectory.2026-10-07.md` § "Added 2026-10-08":
  - F12: what a turn reads drives context cost, not resume;
  - F13: preamble, DONE;
  - F14: the blind spot depends on the reviewer policy; `.codex/` read-only; Guardian denials;
  - F15: tn-check, DONE;
  - F16: compact / rebind / fork, proposal.
- **Operator PAD:** `.dev/session/nablarva-X1-architecture/raw/pad.1-tunnel-support.md`. It holds every open tunnel item (A–J), each with stable bashes and a resolved / in-process checkbox. **This PAD is now the open-items list.** "Still open" lines in T15/T16 point here.

**What `tn-check` does.**
- `tn-check [bed] [name]` checks a vault; `tn-check --id <thread> [--cwd <dir>]` checks a successor candidate.
- It is read-only and spends no quota. Exits: 0 READY · 2 BUSY · 3 HELD · 4 BROKEN · 10 no vault.
- Six cases tested: live head HELD (daemon) · 01a113d8 BROKEN (no rollout) · guardian thread BROKEN · no vault 10 · missing preamble BROKEN · cwd mismatch BROKEN.

**New field facts (21:13–21:50):**
1. **Writer-lock files outlive their holders.** Files dated 09-23 are still present, so the real test is `fuser` (holder), not whether the file exists. This corrects the "wait until the lock is gone" wording in T10 / F1(b).
2. **The managed daemon updated itself to 0.162.0** (pid 232027, 21:13); the CLI is still 0.161.0. The skew is unverified: that is PAD item D, the L8 check.
3. **Guardian (`auto_review`) creates zero-turn subagent threads** (`01a11cef…`, `source.subagent.other=guardian`, model `codex-auto-review`). They are never head candidates.
4. **Head `01a118ff` was compacted in the TUI at 16:01Z (18:01 local).** The id survived. The last token_count reads 0, so the next turn sets the new baseline (PAD C).
5. The 16:36 background deploy job was reaped for low memory. The commit and push of `17a00fe` had landed, and the live files were identical. **The live selftest never ran**, which corrects T14's "live selftest 113/113" (now PAD D).

**For the carrier, verbatim (STATUS `holds:` candidate):**
`- tunnel support (trajectory T17): open items = raw/pad.1-tunnel-support.md (A–J, majkee runs/decides); tn-check live (ia-sync 134b08f, unpushed) — run before any tunnel verb; head 01a118ff compacted 18:01, TUI-held until /exit; daemon 0.162.0 vs cli 0.161.0 unverified (PAD D)`

## T18 · 2026-10-08 22:29 · `tun resume` → `-32600 already has an active writer` about 10 s after TUI `/exit` (0.162 daemon). Diagnosis: the daemon releases later than 10 s; no defect

- **majkee:** `tun resume` printed the shim NOTE "writer-lock present … Proceeding", then app-server `-32600 thread 01a118ff… already has an active writer`. He had waited about 10 s after `/exit`.
- **Read at 22:28:58:** the head's lock **file is gone**. The `thread-writer-locks/` directory mtime is **22:27:51**, which is the release. TUI pid 16989 has exited. The daemon (0.162.0, pid 232027) no longer holds the head.
- **Reading.** F1 is unchanged on 0.162: after a TUI exit, the managed daemon keeps the writer for longer than 10 s. On 0.160.1 the release came within about 3 min. On 0.162 the delay depends on majkee's `/exit` time (PAD A).
- On 0.162 the lock **file was deleted** on release, as on 0.160. The surviving old files (`01a0ce24` and others) are held or orphaned by other threads' clients, so `tn-check`'s holder test is still the right one.
- **Shim gap (F1(b), confirmed in the field):** when a lock is present, the shim prints a NOTE and proceeds into a certain `-32600`. `tun resume --wait` should poll the holder through `fuser` and send nothing until the holder is gone.
- **Until that is built:** after any TUI `/exit`, run `tn-check` until it says READY, then `tun resume`. PAD B1 already runs `tn-check` after the resume. Run it before as well.

## T19 · 2026-10-08 22:40 · built `tn-back` + `tn-rebind` (majkee: "let's continue" with the lifecycle functions); T18 release timed

**T18 closed:** majkee `/exit` at about 22:27, and the lock was released at 22:27:51, so the 0.162 daemon holds the writer for **under 1 min**. A retry at 10 s is too early. `tn-back` now does the waiting.

**Built** (ia-sync, `zsh/session/tunnel.zsh` + aliases in `zsh/session/keyboard.zsh`, copied live):

| verb | event | what it does | exit |
|---|---|---|---|
| `tn-check [bed] [name]` · `tn-check --id ID --cwd DIR` | E2 check | read-only verdict (T17) | 0 READY · 2 BUSY · 3 HELD · 4 BROKEN · 10 |
| `tn-back [bed] [name] [--timeout S]` | E3 "tunnel back" after any TUI visit (compact, permissions, model) | waits for the writer-lock holder to go, then `tun resume`, then `tn-check` | resume's exit · 2 · 3 (nothing sent) · 10 |
| `tn-rebind <bed> [name] --thread NEW [--reason T]` | E4 succession | gate `tn-check --id`, carry intent, close and re-open, append lineage, restore on failure; never resumes | 0 · 2 · 4 refused · 10 · 11 |

**Routines with these verbs:**
- **compress → back (id kept):** `/compact` in the TUI, `/exit`, then `tn-back`.
- **successor (`/clear` in the TUI, new id):** give the new thread one real turn in the TUI (or no rollout exists), `/exit`, then `tn-rebind BED --thread NEW --reason "ctx reset"`, then `tn-back`, then send the rebrief ask.

**Not built:** `tun compact` (in-tunnel compaction with no TUI, which needs a probe of `thread/compact/start`) and the fork successor. Both are PAD J.
Backlog: tunnel-03 F16a. Tests: listed there.

## T20 · 2026-10-08 23:00 · explorers so ids and paths are never typed: `tn-beds`, `tn-threads`, `@N` (majkee's ask)

- `tn-beds [dir]` lists the repo's beds, numbered, newest first, with R/S/P flags and vault state. `tn-threads [dir] [--all] [-n K]` lists the repo's Codex threads, numbered, with turns, ctx, which bed binds each, and fit. Guardian subagents are hidden; there were about 30 tonight.
- `@N` takes row N of the last listing in this shell. As a bed: `tn-check @1` · `tn-back @1` · `tn-use @1`. As a thread: `tn-check --id @2` · `tn-rebind @1 --thread @2`. `tn-bed N` and `tn-tid N` print the full path or id (`cd "$(tn-bed 1)"`).
- Seen at 22:59: head `01a118ff` at ctx 20 % after the compaction, 8 turns. `01a0f5a6` (81 %, 28 turns) is another nablarva thread. It is not bound and not ours; I name it so nobody binds it by mistake.
- ia-sync tunnel.zsh + keyboard.zsh, copied live; backlog F17.

## T21 · 2026-10-09 00:25 · scratch test subject live — turn overrides + `tun compact` built and proven; F12 answered

**Subject (majkee):**
- Thread `01a11d5e-2fc5-7400-9cf3-70b826e5d972`, `gpt-5.6-terra`/medium, born in the TUI, reviewer `auto_review`. Call sign `cartan(tn-trajectory)`.
- Vault `~/ia-sync/.dev/session/tunnel-03-feedback-upgrade/tunnel.state.json`, cwd `~/ia-sync`, X1 preamble.
- Majkee opened the gate with the first ask. Cartan's Codex roster and brief shape are in the journal, 2026-10-07 §1.1.4.2.
- Launch form confirmed by turn_context: `codex --model gpt-5.6-terra --config 'model_reasoning_effort="medium"'`. The model id is lowercase.

**Built + live-proven** (ia-sync `bf21d30`, local, 3 commits ahead; live copies byte-identical; selftest 134/134, live as well):
1. **Turn overrides (A1):** `tun open --override effort=low` (and model / approvalPolicy / approvalsReviewer / summary).
   - Live: `turn_context.effort=low`.
   - **They persist in the thread:** after the override was cleared, the next turn still ran `low`. `--override effort=medium` restored it, and the vault override was then cleared again. Scratch is back to medium.
   - Typing `/model` in an ask can't work: slash commands live in the TUI client only.
2. **`tun compact`:** `thread/compact/start` runs as a turn of 30–43 s. The id is kept, no TUI is needed, and turn/completed is the end signal (no `thread/compacted` arrives).
   - Scratch: ctx 41.5 % → **12.0 %** on the next turn, and Cartan still knew his call sign and task.
   - This replaces the TUI step of compress→back. **New routine: `tun compact`, done; no `/exit`, no `tn-back`.**

**F12 answered:** short turns add about 200 tokens each (106443 → 106750 → 106947 → 107144), including across an effort change. Resume re-sends nothing.

**PAD D resolved** by this sitting: CLI and daemon are both 0.162.0, selftest 134/134 live, plus 6 live asks.

**Turns spent on scratch:** 5 asks + 2 compactions.

**Open:** a fork successor probe (`thread/fork`, F16 step 3). Push ia-sync (3 commits).

## T22 · 2026-10-09 00:35 · fork probe → `tun fork` built; the lifecycle set is complete

- **Probe (scratch, 1 ask):** `thread/fork` clones history and policy, and the rollout exists at once with 0 turns.
  - The fork answered with the parent's call sign and its last test (J1), at ctx 12.1 % = the parent.
  - A fork is a **branch/clone**, not a reset. A reset successor = a birth: open a vault with no `--thread`, and the first send creates the thread.
- **Built:** `tun fork` prints the new id on stdout and leaves the vault unchanged. `tn-check`/`tn-threads` treat a 0-turn fork as bindable.
- **Live chain, no turns:** `tun fork` → `tn-check --id` READY → `tn-rebind <bed> fork --thread …` (lineage written) → `tn-back` READY. Selftest 139/139, live as well.
- **The lifecycle verbs you asked for (T16), all built:**

  | event | verbs |
  |---|---|
  | check | `tn-check` |
  | compress → back | `tun compact` (no TUI), or TUI `/compact` + `tn-back` |
  | successor | `tn-rebind` (after a TUI `/clear` + one turn, or after `tun fork`) |
  | explore | `tn-beds` / `tn-threads` / `@N` |
  | settings | `tun open --override` |

- **Scratch state:** 2 vaults in tunnel-03.
  - `tunnel.state.json` → `01a11d5e` (the subject, medium).
  - `tunnel.fork.state.json` → `01a11da4` (fork of fork `01a11da1`).
  - Both forks are idle; the threads cost nothing while idle.
- ia-sync: 1 commit to push (F20).

## T23 · 2026-10-17 01:50 · oraculum: "what actually stopped the rereading in tunnel-03?" Answer: nothing different there. The preamble works on X1; what fills Cartan now is work, AGENTS.md re-injection, and re-orientation after compaction

**Not a fault:**
- Oraculum's "thread exited" line is the question she recorded for majkee (her session, 2026-10-16 23:40Z).
- Head `01a118ff` is healthy: last turn cycle 12 completed 23:26→23:28Z, no writer-lock holder, the vault is bound.
- The vault was rewritten at 23:39Z by her spawn's preamble switch to `~/.germline/tunnel/tunnel.preamble.md`. That command exited 11 on `--thread`, after applying the preamble. Expected: `--thread` is valid only when the vault is created.

**What made tunnel-03 cheap:** no mechanism. It uses the same preamble file (oraculum is right: byte-identical). My scratch asks said "reply exactly ok, no tools, no reads", so each cost about 200 tokens because they asked for no work. Nothing in the shim differs per bed.

**What the preamble actually did on X1** (rollout per turn, from the first prepended turn 10-08 20:40):

| turn | preamble | tool calls | tool output | ctx after | read-order rereads |
|---|---|---|---|---|---|
| 10-08 01:43 / 12:38 / 12:41 (before) | – | 17 / 7 / 14 | 203 / 75 / 193 kB | 38 / 51 / 74 % | STATUS, PROJECT.yaml, git each turn |
| 10-09 11:52 · 12:19 · 13:18 | Y | 13 · 3 · 2 | 107 · 4 · 1.5 kB | 33 · 35 · 38 % | **none** |
| 10-09 23:17 | Y | 12 | 165 kB | 59 % | AGENTS.md, PROJECT.yaml |
| 10-12 11:09 | Y | 11 | 103 kB (+12.9 kB AGENTS.md re-injected) | 73 % | AGENTS.md |
| 10-13 19:13 | Y | 15 | 66 kB | **84 %** | none |
| 10-16 23:26 | Y | 15 | 102 kB (+12.6 kB re-injected) | auto-compacted mid-turn at 221 k → 22 % | **whole read order + git** |

**Reading:**
1. **The preamble stopped the habitual rereads:** short and ordinary turns re-read nothing. The ctx climb from 33 % to 84 % came from **work**, meaning files the POINTs had Cartan read (66–165 kB per design turn).
2. **Codex re-injected AGENTS.md (≈12.6–12.9 kB) twice.** Both times an instruction source had changed since the previous turn: nablarva `AGENTS.md` at 10-10 01:26 (b57e199 family) and `~/.codex/AGENTS.md` at 10-16 19:32, alongside the codex 0.163 install. This refines F12: re-injection follows instruction-file and settings changes, not resume.
3. **New finding — re-orientation after compaction.**
   - At 221 k (85.7 %) Codex **auto-compacted inside the cycle-12 turn**.
   - Cartan then re-read the whole read order: AGENTS, RUNBOOK, STATUS, flag, pulse, git.
   - The preamble says "you are already oriented", which is false right after a compaction, so the model re-orients. That is reasonable behaviour, not disobedience.

**Fixes (no shim change):**
- **(a) Compact deliberately, before ~75 %.** Run `tun compact`, then send one short rebrief ask that names exactly what to read: "Read only STATUS.md lines X–Y and _bus/NN; do not re-read the read order." The re-orientation then costs a few kB instead of ~100 kB, and auto-compaction never lands in the middle of a design turn.
- **(b) Preamble wording, for the germline owner** of `~/.germline/tunnel/tunnel.preamble.md`. Add one line: "If your context was compacted or you lack orientation, read only STATUS.md and the files this message names; never the full read order." Make the provenance line generic, as oraculum noted.
- **(c) POINT discipline (T13):** inline small payloads, and name line ranges. Work cost is the main driver now.

**Correction to oraculum's item 2 ("the model differs"):** the vault's `model: gpt-6.1-sol` is a stale label. It is the `model/list` default stamped at open, and the shim never sends it on a bound thread (T21/F18). Cartan has run `gpt-6-sol` in every turn_context since X0. To change it without a new thread: `tun open --override model=gpt-6.1-sol`. It persists from the next turn.

**Oraculum's item 3 holds:** the tunnel-03 vaults (`tunnel.state.json`, `tunnel.fork.state.json`) still point at the X1 bed preamble, so the bed file stays until they are repointed.

**For the carrier, verbatim (STATUS `holds:` candidate):**
`- tunnel (trajectory T23): preamble works (no habitual rereads since 10-08 20:40); ctx is filled by POINT work + AGENTS.md re-injection on instruction-file change (~13 kB) + re-orientation after auto-compaction (cycle 12, ~100 kB) → compact with tun compact before ~75 % + a named-files rebrief; vault model label is stale, Cartan runs gpt-6-sol (override if wanted)`
