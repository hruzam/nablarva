---
title: Muticula — master brief (the animal plan)
status: proposed · every challenged point decided (majkee) — D1–D4 2026-09-26, D5 2026-09-27 · r3 awaits the witness's fold check (_bus/01), then majkee's GO/STOP
revision: r3 — Cartan's r2 fold CHALLENGE (four bounded corrections) and D5 folded 2026-09-27 by @Trajectory; reviewed r2 kept byte-identical as muticula.master.2026-09-26.reviewed-6db74151.md (r1 …reviewed-17a2641e.md, r0 …reviewed-7c41b520.md)
born: 2026-09-26 · voice session majkee × Nabla, folded in chat
phase: B (architecture) → C (build order, §5)
---

# Muticula

tmux + cuticula: the thin outer layer that keeps concurrent CLI sessions from abrading each other in one working tree.

**Tags.** Provenance: `[ARCH]` settled in the voice session — majkee's X, shaped together (dialogue consensus, not triangulated) · `[NABLA]` added while folding — not yet argued, veto-able · `[DECIDED <date>]` majkee's gavel on a challenged point (§6) · `[OPEN]` needs a decision. Tier: `[CORE]` build first · `[v2]` grow only when its trigger fires. A heading's tag covers its body unless a line says otherwise.

---

## 1. The animal `[ARCH]`

**What.** A file-backed concurrency guard for several agent CLI sessions (Claude Code, Codex, …) sharing one git working tree. One script; its `watch` mode is the only long-running piece.

**Field problems it answers.**
1. Shared bookkeeping — task journal, invariant file — is the main collision point: every session head writes it.
2. Whole-tree git verbs (`git add -A`, `git commit -a`) sweep a neighbor's work into your commit.
3. `git diff` is a global surface: a session rebuilding its picture from the diff adopts a neighbor's changes as its own.
4. Read-once claims: the first session checks for neighbors at start and never again. The second sees the first; the first never learns about the second.
5. Rare cross-cutting operations — migration, mass rename, dependency change — whose footprint no per-file claim can express.

**Stance.** Coordinate in one shared tree instead of isolating each session. A mix of pessimistic (claim before you touch) and optimistic (check again at commit), borrowed from how processes share files and databases share rows. Isolation — worktrees — is Alternative B (§9).

**Scope** `[NABLA]`. One repo, one machine, local filesystem, cooperating sessions — in one explicitly identified checkout `[DECIDED 2026-09-26]`. Worktrees are Alternative B (§9), never a second default.
**Out of scope** `[NABLA]`. Security: a seatbelt against accidents, not a wall against a session that means to get around it — launch keys included (§5). Runtime isolation: §8.

**Roles.**
- **C# ("sharp")** — session head. First in, holds the observation line across the whole task, last out. Owns every Muticula write for its team.
- **Spawn** — sub-agent under a sharp. Works locally, reports up, never calls Muticula write verbs — by convention: a spawn carries its sharp's credential (§8).
- **Human** — the top voice, acting through explicit operator commands `[DECIDED 2026-09-26]`. Only the human launches a team, reaps a dead sharp, lights the beacon, presses stop and records a recovery; a beacon passes by its current holder or the human (D1). In v0 also the relay between sharps. A session without `MUTICULA_ID` is **unenrolled** — write verbs refused — and never taken for the human.
- **Maintainer** — folds abandoned work back. In v0: the human.

## 2. Invariants

1. **Machine says stop; only an authorized voice says go.** Every automatic path ends in refusal or hold, never in release. Release and handoff belong to the owner or the human; override and recovery to the human alone — never to rank `[DECIDED 2026-09-26]`. An expired or revoked authorization refuses; it never frees what it guarded. A policy bug makes Muticula too cautious, never too reckless. `[ARCH]`
2. **Checks ride on actions.** No polling, no clock for sessions. Awareness refreshes at `claim` and at `commit` — and the commit is the one action nobody skips. The only clock in the system faces the human (leg 3). `[ARCH]`
3. **No verb waits on another session.** Every verb answers at once: exit 0 / 3 / 4. Waiting inside a hook or a tool call runs into the CLI's timeouts; a refused sharp retries at its next natural checkpoint. Lock acquisition is bounded (`flock -w`); the commit inside the lock is not — Git hooks run there — so its duration is measured, never assumed `[DECIDED 2026-09-26]`. `[ARCH]` concern · `[NABLA]` rule
4. **One writer per file.** Per-sharp files have one writer. Human overrides are appended as tombstones in the human's own file, never edits of a sharp's file. Shared views — registry, journal — are projections: rebuilt, never edited. One `flock` serializes check-then-act across files; it is never held while thinking. Views never take it and may be approximate; permission decisions read under it and never take absent, damaged or half-written state for free. A write is atomic per file, never across files `[DECIDED 2026-09-26]`. `[NABLA]` — carried from larva's invariants (one writer per file, derived-is-disposable, tombstones)
5. **In a shared tree, every whole-tree git verb is a cross-session write.** Sharps get path-scoped verbs only, and stage/commit only through the gate. `[ARCH]`, generalized `[NABLA]`

## 3. State `[CORE]`

Intent `[ARCH]`: a registry of sessions with purpose and state, a journal per session, a live status `.md` per head, settled states gathered in one main journal. Layout `[NABLA]`:

Location: `$(git rev-parse --git-common-dir)/muticula/` — next to git: never tracked, never dirties the tree, one per repo. → D2
`[DECIDED 2026-09-26]` **Host-local.** Resolve the Git directory through git — never assume `.git` is a directory. Every record carries its `host`. State from another host is never local authority: copying the directory elsewhere enrolls nobody. The host stamp is provenance, not exclusion or authentication.
`[DECIDED 2026-09-26]` **One checkout.** The state pins the one checkout it coordinates; from any other checkout — a worktree — it is not authority. Visibility through the common dir is not cross-worktree claim identity (§9).

```
muticula/
  lock                  flock target — check-then-act only
  checkout              the one worktree root this state coordinates       writer: the first launch (the human)
  keys/<id>             <key-hash> <host> <since> — created exclusively    writer: launch (the human)
  sharps/<id>           <state> <host> <since> <purpose…>                  writer: sharp <id>
  claims/<id>           one normalized path per line · dir/ = subtree ·
                        <path> inherited = dirty on arrival, not adopted   writer: sharp <id>
  passes/<id>.<n>       one transfer, write-once:
                        <paths…> → <to> <to's key-hash>                    writer: the giver <id>
  status/<id>.md        live state, carries a `pending:` line              writer: sharp <id>
  log/<id>              append-only: <id>'s verbs, its own notes, native
                        child ids where the runtime shows them             writer: sharp <id>
  settled/<ts>.<id>.md  settled entry, write-once                          writer: sharp <id> at close · human at reap
  beacon                empty = dark · <instance> <holder> <since> <why…>  writer: one at a time under the lock —
                                                                           the human at on, then the holder or the human
  human                 append-only: the human's own acts — reap · beacon
                        on/pass/off · stop · recover — and watch's suspend  writer: the human (watchdog on their behalf)
  journal.md            the book: settled/* in name order                  writer: the projector — rebuilt at close / reap
```

- **Registry = `muticula ls`** — a view over `sharps/`, `claims/`, `passes/`, `status/`, `beacon`, `human`. The one central place without a shared write head — for Muticula's own records. Existing shared project files — `AGENTS.md`, pulse, journals — stay ordinary paths: they need claims like any other file, and no projection removes them `[DECIDED 2026-09-26]`.
- **A sharp's claims** = its own `claims/<id>`, plus paths passed to it, minus paths it passed on. A transfer is written once by the giver, never into the recipient's file.
- **Paths** `[OPEN]`. Normalization, accepted filename encoding and subtree overlap are defined before the build, and before the language is chosen `[DECIDED 2026-09-26]`.
- **Last seen** = mtime of `log/<id>`. Every verb appends; no extra field.
- **Journal** = settled entries only, materialized so an editor can watch it. Nobody edits it.
- **States**: active → closed (the sharp's `close`) · abandoned (the human's `reap`). A reaped sharp's claims — passed-in ones too — are void from the tombstone on; its own files stay untouched; its dirty bytes stay in the tree, inherited by whoever claims them next.
- **Ids are single-use.** A closed or reaped id never reopens; identity lives in the file lineage. `launch` creates `keys/<id>` exclusively: an existing id is refused, its stored hash never replaced `[DECIDED 2026-09-26]`.

## 4. The three legs `[CORE]`

### Leg 1 — Claims: the map `[ARCH]`
- **Claim before you touch.** Narrow paths, or `dir/` for a subtree. Claims belong to the team and are advisory: they constrain commits, not the editor (§8).
- **Check-then-act under the lock.** A live claim of another sharp overlaps — same path, or one is a `dir/` prefix of the other → exit 3 with holder and since. Otherwise the path joins `claims/<id>`.
- **Awareness rides on output** `[NABLA]`. Every `claim` and `commit` prints one neighbors line — `c2 · app/model/ · 3m · beacon dark`. The first sharp learns about the second the next time it acts: read-once asymmetry gone, no polling.
- **Dirty on arrival — shown, not adopted** `[DECIDED 2026-09-26]`. Claiming a path with uncommitted changes marks it `inherited` — typical after a reap or a pass. Showing is not adopting: the gate leaves an inherited path alone until the sharp adopts it explicitly (`adopt`, logged).
- **Contested path — explicit ways forward only** `[DECIDED 2026-09-26]`. The holder releases it, or passes it to the requester (`pass`): a transfer — the requester becomes the owner, the holder loses it, dirty bytes arrive inherited. One owner per path, sequential, never shared in v0; the human relays in v0. Model-tier rank is gone: a model is not authority over a task — the task's owner consents. Withdrawn: r0's `[ARCH]` Opus-over-Sonnet rank and the `ack` co-claim.
- **A commit selects files, not authors** `[DECIDED 2026-09-26]`. A file two writers touched is committed whole, with both writers' bytes; concurrent same-file work is deferred (§7).

### Leg 2 — The gate: `muticula commit` `[ARCH]`
The check is welded to the one action nobody skips. A wrapper, not a git hook: a hook reacts inside someone else's commit; the wrapper owns the commit and decides what goes in.

**Correction to the voice session** `[NABLA]`. Scoping `git add` is not enough. The index is one file shared by every session in the tree — a neighbor's staged paths ride a plain `git commit`. The gate commits with an explicit `--only` and a literal, NUL-framed list of concrete paths: it records exactly those paths from the working tree and leaves the rest of the index alone `[DECIDED 2026-09-26]`. Each part is load-bearing, per a Trajectory-reported scratch receipt — not independently witnessed, and no qualification of the product gate (`raw/gate-fixture.2026-09-26.md`): without `--literal-pathspecs`, a file named `*.md` is a wildcard that pulls in a neighbor's unstaged file; an empty list with `--only` is a hard error — without it, the whole index is committed.

```
muticula commit -m "<msg>"
  1  take the lock — bounded wait
  2  beacon lit by another · beacon suspended · stopped · I'm reaped      → exit 4
  3  mine      = changed paths under my live, adopted claims — beacon or not
     foreign   = changed paths under any other claim, retained ones included  → left alone
     inherited = changed paths I claimed but have not adopted                  → reported, never staged
     orphan    = changed paths under no claim                                  → reported, never staged
     mine empty                                                                → refused before staging (exit 1)
  4  git --literal-pathspecs add --pathspec-from-file=- --pathspec-file-nul                   ← untracked in mine
     git --literal-pathspecs commit --only -m "<msg>" --pathspec-from-file=- --pathspec-file-nul   ← mine
  5  verify: the paths HEAD changed == mine; any other path → incident: exit 1, logged, reported — never undone automatically
  6  append "commit <sha> <paths>" to log/<id>; print the neighbors line
  7  release the lock
```

**The beacon holds others; it adopts nothing** `[DECIDED 2026-09-26]` · corrected r3. Every committed path is under the committer's live, adopted claim — the beacon holder's included. The beacon is permission for exclusive work: while it is lit the others are held, so its holder can claim broadly (`dir/`) and adopt what it inherits — but it never commits a path it has not claimed and adopted, nor one under another sharp's claim, retained claims included. Beacon privilege belongs to the holder of the current instance: after a pass, the original lighter keeps none.
**Git hooks** `[OPEN]`. Hooks run inside step 4 and can change what is committed. Step 5 compares path sets only: it detects a hook that adds or drops a path, not one that changes the bytes of a selected path. Which hooks may run, and how same-path changes are handled, is defined before the build.
**Other Git clients** `[DECIDED 2026-09-26]`. The lock serializes cooperating wrapper calls only; the human, an IDE or a hook can still hold `index.lock`. That contention is a git error (exit 1), never waited on.

**`muticula diff`** — a view of my claimed paths: `git diff HEAD` over them, plus my untracked files. It shows where I work, not who wrote what: it cannot establish authorship `[DECIDED 2026-09-26]`. A sharp builds its picture of its own work from it and may read the global diff as context; reading a neighbor's change never makes it its own (field problem 3).

**Deny list** — in each CLI's own permission layer. `[ARCH]` for `add -A` · `[NABLA]` the rest
- stage / commit: `git add`, `git commit` in every form → only through `muticula commit`
- tree rewrites: `git stash`, `git reset --hard`, `git checkout -- .`, `git restore .`, `git clean`
- HEAD movers: `git pull`, `git merge`, `git rebase`, `git switch`, `git checkout <branch>` → human only; they rewrite everyone's tree
- human verbs: `muticula launch`, `reap`, `stop`, `beacon on`, the human form of `beacon off` / `beacon pass`, recovery

Whether a rule bites is qualified, not assumed `[DECIDED 2026-09-26]`: build step 0 proves, per runtime and mode, the wrapper's allowed route and the denied raw routes. B0 (2026-09-25) tested PreToolUse hooks, not these permission rules. Where coverage is unproven, the agent contract (§5) is the only fence — a declared cooperative rule.

### Leg 3 — The beacon: a global hold `[ARCH]`
*Maják* — the blinking roof light, not the lighthouse.
- **Binary.** Dark or lit. One question: is a cross-cutting operation in flight?
- **Beacon-class** `[NABLA]` = a footprint that can't be written as narrow claims beside others' work: migrations, mass renames, dependency/lockfile changes, router rewrites, the human's HEAD movers.
- **Operator-lit in v0** `[DECIDED 2026-09-26]`. A clean floor is not a stopped-writer barrier: an editor, tool or child admitted before the light can still write a claimed file (Cartan's CHALLENGE, finding 1). So the human coordinates: every other team stops and accounts for its running tools and children, then the human lights the beacon for one holder — `beacon on <id> "<why>"`. Suspension, keys and passwords do not repair this race. A sharp-lit beacon waits for a qualified barrier (§7).
- **Clean floor to light** `[NABLA]` — still required, no longer sufficient. `beacon on` refuses (exit 3) while uncommitted changes exist outside the holder's own claims, and names the paths and holders that must commit or release first. Once lit, everyone else gets exit 4 on `claim` and `commit` — hold, tell the user. The holder commits like any sharp (Leg 2): only its live, adopted claims — the beacon holds the others; it adopts nothing.
- **Normal path.** The human lights it for the holder before the operation; the holder turns it off after. It stays lit only when forgotten.
- **Watchdog.** `muticula watch` runs in a multiplexer pane or popup and faces the human. Every 5 min while lit: `lit by c1 for 25m: <why> — keep / off?` Keep resets the strikes; off clears; silence is a strike.
- **Kill switch.** The human's `muticula beacon off`, from any terminal, any time — an explicit, recorded recovery decision, never an inferred one.
- **Silence → suspension, not release** `[DECIDED 2026-09-26]` → D1. After **three** unanswered notices the operation is **suspended** and ownership is **retained**: silence neither clears the beacon nor grants it to anyone. Reading and work outside the protected scope continue; recovery stays available even if `watch` dies. Naming a state "suspended" does not stop a running process.
- **Explicit handoff to one named successor** `[DECIDED 2026-09-26]`. Only the current holder or the human authorizes `pass to B`, and only after the old operation has stopped and its outstanding writers and children are accounted for — acknowledging a notice is not enough, and stopping writers is a precondition the design must establish, not something B0 proved. Muticula atomically revokes A's beacon authority and grants it to B, bound to the **current beacon instance** so a stale release can never clear a newer holder's beacon. A pass is a transfer: B becomes the holder and A keeps no beacon privilege — not a delegation A could still govern.
- **Retained claims** `[DECIDED 2026-09-26]`. A's unfinished files keep their claims: B gets the next turn, not A's files or their dirty bytes. If B needs them, an explicit file handoff is required; no whole-tree operation or commit may sweep through retained claims. A's resume must respect B's current beacon — the original holder cannot silently override its successor.
- **One successor, no queue** `[DECIDED 2026-09-26]`. v0 names exactly one next holder; no persistent FIFO, no scheduler. If the protected scope is the whole repository, an unresolved suspension honestly reserves the whole repository.
- **A file, not a process** `[NABLA]`. The beacon survives crashes on purpose. Without `watch`, a forgotten beacon simply holds — same fail direction.

## 5. Surface `[CORE]` `[NABLA]`

| verb | who | effect | exit |
|---|---|---|---|
| `launch <id> -- <cli…>` | human | register a fresh team incarnation: create `keys/<id>` exclusively, mint a key, store only its hash; start the CLI with `MUTICULA_ID` + `MUTICULA_KEY` in its environment, never in argv | 0 · 3 id exists |
| `open "<purpose>"` | sharp | set purpose, print the status-file path; implicit on the first verb | 0 |
| `claim <path>…` | sharp | take paths; `dir/` = subtree; dirty ones arrive `inherited` | 0 · 3 held · 4 hold |
| `adopt <path>…` | sharp | take inherited dirty bytes as mine — logged | 0 |
| `release [<path>…]` | sharp | give back; all if none | 0 |
| `pass <id> <path>…` | holder | transfer to sharp `<id>`, bound to its current key; I lose them; dirty bytes arrive inherited | 0 · 1 not mine / no live `<id>` · 4 hold |
| `diff` | sharp | a view of my claimed paths — not authorship | 0 |
| `commit -m "<msg>"` | sharp | the gate | 0 · 4 hold · 1 refused or git error |
| `beacon on <id> "<why>"` | human | light for holder `<id>` once every other team has stopped and accounted for its tools and children | 0 · 3 floor dirty · 4 already lit |
| `beacon off` | holder / human | clear the current instance | 0 |
| `beacon pass <id>` | holder / human | atomic handoff of the current beacon instance to one named successor; A's file claims stay A's `[DECIDED 2026-09-26]` | 0 · 3 writers not accounted for · 4 stale instance |
| `close` | sharp | settled entry, release all, rebuild the journal | 0 |
| `ls` | anyone | registry: sharps, purpose, claims (inherited marked), last seen, pending, orphans, beacon | 0 |
| `reap <id>` | human | tombstone: claims void, settled as abandoned | 0 |
| `stop` | human | panic button, no password: revoke every launch key in this state — write verbs exit 4; ownership and bytes stay; running processes are not stopped | 0 |
| `watch` | human | the beacon watchdog | — |

**Recovery after `stop`** `[OPEN]` — a human action that needs none of the revoked keys `[DECIDED 2026-09-26]`; its shape is open.

**Exit codes.** `0` go · `1` error or refused · `3` held by another — work elsewhere, tell the user, retry later · `4` hold — beacon, suspension, stop, reaped, unenrolled or wrong key: stop, tell the user.

**Env.** `MUTICULA_ID` + `MUTICULA_KEY`, placed by `muticula launch c1 -- claude` — never typed, never in argv. Spawns inherit both: identity is per team, and a child holds its head's credential (§8). Every write verb checks the key against `keys/<id>`; a known id alone grants nothing. Whether the environment reaches each runtime's tools and children is qualified in step 0, not assumed.

**Identity — an accident guard, not authentication** `[DECIDED 2026-09-26]` → D3
- **Who says go, by verb.** Owner verbs (`open`, `claim`, `adopt`, `release`, `pass`, `commit`, `close`; `beacon off` / `beacon pass` by the holder) are authenticated by the owner's key. Human verbs (`launch`, `reap`, `stop`, `beacon on`; the human form of `beacon off` / `beacon pass`; recovery, override) are explicit operator commands, kept off agents' routes by the deny list — an unenrolled call is refused, never read as the human. Views (`ls`, `diff`) grant nothing and need no key. A terminal is interaction hygiene, not proof of a human: an agent can open its own controlling terminal (Cartan's probe 4).
- **One current owner per resource.** A transfer (`pass`, `beacon pass`) moves ownership: the recipient owns, the giver loses its powers. A temporary delegation — the owner stays owner and may revoke — is a different thing, not in v0 (§7).
- **Separated confirmation.** If an approval is ever separated from its execution, it is a scoped, single-use authorization bound to the recipient's registration and the resource instance; its expiry refuses an unconsumed approval and never frees ownership.
- **Refusal only.** Expiry, revocation and `stop` refuse future guarded actions. They never free a resource, return ownership, undo an admitted write or stop a running process.
- **Lifetimes per credential.** A launch key lives until `close`, `reap` or `stop`; no other credential's deadline covers it. A leaked key stays usable until then — `stop` is the answer, not an approval's expiry.
- **Keys stay out of argv, prompts and logs.** The environment is itself a disclosure surface — subprocesses, diagnostics (§8).

**Settled entry** — a fixed envelope; the content stays the sharp's. `[ARCH]` "the structure must be clear" · `[NABLA]` fields
```
## <iso-time> · <id> · closed | abandoned
purpose: …   host: …   commits: <sha …>
<status/<id>.md verbatim — without a `pending:` line, the envelope writes `pending: (not stated)`>
```

**Implementation** `[OPEN]`. The language follows the path and encoding definitions (§3), never a line count `[DECIDED 2026-09-26]`; bash + `flock(1)` + git is a candidate. Every write is temp + rename — atomic per file, not across files. `flock -w` bounds the lock wait, not the commit inside it.

**Agent contract** — paste into CLAUDE.md / AGENTS.md:
```
You are sharp $MUTICULA_ID. Muticula guards this shared working tree.
- Claim before you touch: muticula claim <path>  (dir/ = subtree). Claim narrow, release early.
- Dirty bytes you inherit are not yours until you adopt them: muticula adopt <path>
- Build your picture of your own work from muticula diff. The global diff is context —
  reading a neighbor's change never makes it yours.
- Commit only with: muticula commit -m "…"
- Exit 3: someone holds it. Work elsewhere or tell the user. Don't fight it.
- Exit 4: hold — beacon, suspension, stop, you were reaped, or you are not enrolled. Stop and tell the user.
- A cross-cutting change (migration, mass rename, dependency change, router rewrite) needs the beacon:
  ask the user — they stop the other teams and light it for you. You still claim what you touch
  (dir/ is cheap while the others are held). When done: muticula beacon off
- Keep your status file current (path from muticula open), with a pending: line.
- Never print, echo or pass on $MUTICULA_KEY.
- Spawns: no muticula write verbs; report to your sharp.
- Last act: muticula close
```

**Build order** — each step ships alone. Before step 1: define path normalization, accepted filename encoding, subtree overlap, absent/damaged-state handling and Git-hook handling — then choose the language.
0. **Qualification, per runtime and mode** `[DECIDED 2026-09-26]` — not "zero code, kills the sweep today". Prove the wrapper's allowed route and the denied raw routes, indirect shell forms included (aliases, `sh -c`, `command git`, compound commands, permission-bypass modes), and that the launch environment reaches tools and children. Unproven coverage is declared a cooperative rule. `claude -p` is B0 test instrumentation only — nothing built may invoke or depend on it.
1. State dir, lock, `launch`, `claim` / `adopt` / `release` / `pass` / `ls` / `diff`.
2. `commit` — the gate, with its step-5 verification.
3. `close` / `reap` / `stop`, settled entries, the journal book.
4. `beacon` + `watch` — operator-lit (Leg 3).

## 6. Decisions — majkee's veto

**D1 — DECIDED 2026-09-26 (majkee): suspension on silence + explicit handoff.**
After three unanswered notices the operation is suspended and ownership retained; the holder or the human explicitly passes the beacon to one named successor, atomically and bound to the current beacon instance; the old holder's file claims stay its own. Rules in §4 Leg 3. Path to the decision: freeze (r0 default) → a human-delegated auto-burn trial (majkee) → Cartan's challenge of the trial contract → handoff accepted. Superseded: both freeze-until-human-clears and auto-burn. Invariant 1 holds unchanged — no automatic path ever releases.
Record: `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.point.muticula-handoff.2026-09-26.md`.

**D2 — DECIDED 2026-09-26 (majkee): v0 single-host, `.git/muticula/`, host-stamped.**
Local, untracked, resolved through git; every record carries its host; foreign-host state is never local authority (§3). Cross-host overflow (office + home on one repo) is future scope: live exclusion needs **one authority** both hosts reach — nablarva's Stage 2, one broker over SSH (flag L2/L3) — never git as the wire (flag L4, recorded death: git gives visibility later, not exclusion now). Cross-host **awareness** today: the Git-tracked presence board, and an explicitly exported settled journal — both advisory and possibly delayed. The journal inside `.git/muticula/` is not tracked; any snapshot is a deliberate export by the human.

**D3 — DECIDED 2026-09-26 (majkee): identity and authority — Cartan's lean version.**
A missing `MUTICULA_ID` means unenrolled; human powers are explicit operator actions. "The same lock" in majkee's token idea means the same claim or beacon ownership, not the internal `flock`. One fresh launch credential per team incarnation (a duplicate live id refused); one current owner per resource; transfers atomic and bound to the recipient's registration and the resource instance; transfer is not delegation; expiry refuses and never frees; `stop` needs no password and leaves a recovery route that needs no revoked key; who says go is decided per verb, and a terminal is not a human; model-tier rank removed — task ownership and consent decide. **Deferred:** password mode and every lifetime number, concurrent same-file sharing, temporary delegation, the system/admin slot (§7). Rules in §1, §3, §4 Leg 1, §5. Path: majkee's token idea (session key at launch, timed grants, optional password) → Trajectory's addendum → Cartan's consolidated CHALLENGE (REVISE; probe 4: an agent can open a controlling terminal) → lean version accepted.
Record: `raw/relays/TRAJECTORY-CARTAN-addendum.muticula-identity-tokens.2026-09-26.md` (moved from the meeting room 2026-09-27; `raw/relays/move-map.2026-09-27.json`) · `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.challenge.muticula-consolidated.2026-09-26.md`.

**D4 — DECIDED 2026-09-26 (majkee): the master CHALLENGE findings, accepted as corrections.**
Beacon: operator-coordinated exclusive maintenance in v0 — a clean floor is not a stopped-writer barrier. Gate: explicit `--only`, literal NUL-framed paths, empty selection refused, hook handling defined, the commit verified. Views and bytes: a claimed-path diff is not authorship; inherited bytes need explicit adoption; a whole-file commit carries every writer's bytes; projected journals don't remove shared project files. State: normalized paths, subtree overlap, absent or damaged state never free, coherent authorization reads, no multi-file atomicity claimed, the lock wait bounded apart from the commit. Step 0 is qualification. Single checkout explicit, worktrees stay Alternative B; no B1 queue/store machinery; no language from a line count; "prevents contamination" withdrawn.
Record: `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.challenge.muticula-master.2026-09-26.md` · `…/raw/cartan.verify.muticula-master-r1.2026-09-26.md` · `…/raw/cartan.challenge.muticula-consolidated.2026-09-26.md`.

**D5 — DECIDED 2026-09-27 (majkee): the fold vocabulary.**
The verbs `launch`, `adopt`, `pass`, `stop`, the human-lit `beacon on <id>`, and the records `checkout`, `keys/`, `passes/` — r2's veto-able fold wording — are accepted ("Vocabulary is ok"). r3's correction adds no verb: the beacon holder uses `claim` and `adopt` like any sharp.
Record: majkee in the Trajectory session, 2026-09-27 · this bed's `RUNBOOK.md`.

## 7. Growth — only when the trigger fires `[v2]`

- **Edit-time check** `[NABLA]` — a pre-edit hook in the CLI: instant allow/deny against claims, never waits. B0 (2026-09-25) saw a healthy PreToolUse deny with native child identity in both runtimes — Claude lane qualified ACCEPT, Codex lane STOP — and each tested guard fault (timeout, exit 1, malformed output, missing executable) failing open with no denial on the recorded output surfaces, in the modes tested (Claude print, Codex grouped exec); Bash writes pass an edit-tool guard. A check, not prevention: add it only with an explicit coverage promise and a fixture/witness gate. *When:* unclaimed edits keep surfacing as orphans.
- **Sharp inbox** `[NABLA]` — `inbox/<id>`, append-only, shown at `claim` / `commit`. *When:* you, as the relay, become the bottleneck.
- **Wait line** `[ARCH]` idea, deferred — FIFO per contested path. *When:* a sharp keeps losing the same path.
- **Claim lease** `[ARCH]` corner (the dead sharp) — silence expires claims; the gate already fences a sharp that wakes up; dirty-on-arrival shows the next claimant what it inherits. Still the machine saying go: argue it against invariant 1 first. *When:* reaping by hand becomes a chore.
- **Graded operations — the traffic light** `[ARCH]` idea · `[NABLA]` scoping. Its one legitimate job: choose the beacon's fail direction per operation — fragile → suspend, routine → clear. Never ownership; that stays with the owner. Two mechanisms deciding one question will disagree. *When:* D1's single default proves wrong for a real class of operations.
- **Stopped-writer barrier** — what a sharp-lit beacon would need: participants stop admitting writes, finish outstanding ones, acknowledge, then the floor is rechecked — qualified in fixtures before any live use. *When:* operator-lit maintenance becomes a chore.
- **Temporary delegation and same-file sharing** — the owner stays owner and grants rights it can revoke; a grant dies when its issuer stops owning the resource, when either team closes or is reaped, or when a relevant key is revoked. Consent alone doesn't solve mixed bytes: sharing needs its own commit contract. *When:* sequential handoff proves too slow for real work.
- **Password mode and lifetimes** — a deliberate confirmation for go-verbs through a trusted implementation; its strength never justifies a longer window; a missing hash while the mode is selected fails stop; lifetime numbers need workload evidence; a complete reset is detectable only against a trusted reference outside the mutable state. *When:* accidents get past the launch key.
- **System/admin slot** — a store agents cannot write: another system user reached through `sudo`/polkit, or the Stage-2 broker checking the kernel's view of the caller. A named slot; no protection claimed. *When:* nablarva's next generation.
- **One Rust binary** `[NABLA]`. *When:* the path, encoding or parsing rules outgrow the script — never a line count alone.

## 8. Known limits `[NABLA]`

- **Claims are advisory until the edit-time check exists** — and a hook is a check, not prevention (§7). An unclaimed edit inside someone's claimed file rides their next commit; the gate can't see who typed what.
- **A commit selects files, not authors.** A file two writers touched carries both writers' bytes.
- **Shared tree, shared runtime.** A neighbor's half-edit can break your test run or build. Muticula's promise is narrower `[DECIDED 2026-09-26]`: among cooperating sharps, each commit carries only the committer's claimed, adopted paths, and the committed path set is checked. It does not keep a neighbor's bytes out of your build. If interference dominates → §9.
- **Holds don't stop processes.** A beacon, suspension or `stop` refuses the next verb; an editor, tool or child already running keeps writing until it stops.
- **Team identity.** Spawns inherit the sharp's id and key: head and child hold one credential, so the sharp/spawn split is convention, not mechanism. Native child ids are logged where the runtime shows them; no unique child writer binding is promised.
- **Moves touch two paths.** `git mv a b` needs both claimed.
- **Seatbelt, not a wall.** A session can unset its env, or find a gap in the deny list. Everything runs as one Linux user: on office, a same-user probe read its test child's environment (probe 1 — subject to ptrace access checks) and its argv (probe 3; `/proc` is mounted without `hidepid`). The launch key stops wrong-session, typo'd-id, stale-session and confused-agent accidents — not a deliberate same-user adversary.

## 9. Alternative B — the open door `[ARCH]`

Muticula answers the first fork — coordinate in one tree, or isolate each session — with *coordinate*. B is the other branch, deliberately not designed here. Anyone may open it, any time. Opening it is the normal turn-back, not a failure: one solution didn't fit, find another.

**Signals.** Interference (§8) dominates; sharps spend more time holding (exit 3 / 4) than working.
**Bridge** `[NABLA]`. The state lives in git's common dir, so claims and the beacon stay visible from worktrees — visibility, not authority: v0 pins one checkout, and cross-worktree claim identity is B's to design `[DECIDED 2026-09-26]`. Parts of Muticula may survive into B.

---

**Provenance.** Born in the 2026-09-26 voice session, folded in chat the same day. Dialogue consensus, not triangulated — a heterogeneous challenger pass before code is still open. Restart: the earlier Muticula build is not an input to this brief; carried is the name.
r1 (2026-09-26): the heterogeneous pass ran — Cartan's CHALLENGE, verdict REVISE, at `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.challenge.muticula-master.2026-09-26.md` (+ D1/D2 addendum beside it); D1 and D2 decided and folded above; Cartan's other findings are **not** folded here — they await majkee's disposition.
r2 (2026-09-26): majkee accepted Cartan's consolidated batch (REVISE) — the identity CHALLENGE as D3, the master findings as D4 — folded by @Trajectory together with the two r1 consistency fixes from Cartan's r1 verification (roles: holder or human passes; Leg 2: current authority, never through retained claims). New verb shapes (`launch`, `adopt`, `pass`, `stop`, the human-lit `beacon on`) and the `checkout`, `keys/`, `passes/` records are the fold's wording of decided requirements — veto-able. The bed moved from `.dev/session/toolbox-muticula-00-/` to `.dev/session/muticula-00-brief/` (majkee: "'muticula' only"); frozen records cite the old path and pin content by sha256.
r3 (2026-09-27): Cartan's r2 CHALLENGE (REVISE, fold only — `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.challenge.muticula-r2.2026-09-27.md`) folded: every committed path needs a live, adopted claim — the beacon adopts nothing; step 5 is a path-set check; the argv and fault wording bounded to what was measured; the gate fixture labeled a Trajectory-reported receipt. majkee accepted the fold vocabulary as D5. The bed has a RUNBOOK (cSharp head @Trajectory, standing witness @Cartan); Trajectory's four meeting-room relays moved to `raw/relays/`, bytes unchanged.
**Next:** the witness's fold check of r3 (`_bus/01`) → majkee's GO/STOP on the brief closes `muticula-00-brief` → `muticula-01-<phase>` opens for build step 0 with its own gate, head and independent witness.
