# Audit 3 of 3 — session progress

*Oraculum · Claude · 2026-09-29 · session `nablarva-00`.*
*Status: audit report. Uncanonical. Observations and proposals; no decisions.*

Evidence marks are the same as in [audit 1](audit.patterns-and-loop.oraculum.2026-09-29.md) §0.

## 1. The short answer

Majkee asked whether he is the biggest problem. **Partly, and mostly by construction.**

- Every active gate waits on one person, in two repositories.
- The development process uses that same person as its wire: each review cycle between
  vendors needs him to carry a path by hand.
- The same decisions were put to him four times without the evidence that would let
  him decide.

His own part: new sessions and new names open before old ones close, and prepared
experiments are not run. The agents' part: long documents as gavel inputs, fresh
designs that do not build on the previous one, and summaries that are wrong about half
the time.

## 2. What waits on Majkee

### nablarva

| # | Session | What is needed | Since | Mark |
|---|---|---|---|---|
| 1 | `nablarva-01-design` | `commit ok` and the sender count, to preserve a closed bed | 2026-09-13 | `[S]` |
| 2 | `nablarva-02-pipe-qualification` | The one-line `open_approval`, or a re-pin | 2026-09-14 | `[R]` |
| 3 | `nablarva-03-app-architecture` | Tell Flight that POINT 02 is on disk | 2026-09-29 | `[R]` |
| 4 | `ovitmugen-00-console` | Pull, deploy and run the selftests on home | 2026-09-29 | `[S]` |
| 5 | `muticula-01-qualify` | The Codex trust answer; then relay POINT 02 to Cartan | 2026-09-29 | `[S]` |
| 6 | `toolbox-termbrana-02-m0-truthspike` | Commit and push a dirty tree | 2026-09-02 | `[S]` |
| 7 | Working tree | Commit the `.shared` → `.germline` move, `AGENTS.md`, `PROJECT.yaml` (uncommitted about four days), all of session 03, and this session | — | `[S]` |

### ia-sync `[S]`

| # | Session | What is needed |
|---|---|---|
| 8 | `codex-identity-resolution` | One gavel over decisions 1–5. It blocks `runbook-tool-01-coordination` |
| 9 | `tunnel-upgrade-01-parametrization` | Open the table for the T2 probe `[R: card]` |
| 10 | `voice-meetings-01-threshold` | Run loop 01 |
| 11 | `publish-gate-00-design` | GO or STOP |

### Older, in `meshup/` `[R]`

| # | Item | Since |
|---|---|---|
| 12 | Entity study, round two: commit or amend; the Wave attribution; green light for the experiment design; the `therapy.md` amendment | 2026-08-04 |
| 13 | The docket: seven items and O1–O4 in `flag.md` | 2026-08-02 |

## 3. Orphans and contradictions

**No agent prunes anything in `.dev/session/`.** The list below is for Majkee to act
on by hand. An agent cannot tell debris from something kept on purpose.

### Without a session around them `[S]`

| Directory | Content | Last touched |
|---|---|---|
| `relay-contract/` | Two contract drafts from the 2026-09-16 meeting | 2026-09-18 |
| `toolbox-ommatermia-00-brief/` | Brief marked handoff-ready; no session opened | 2026-09-04 |
| `nablarva-communication-protocole/` | One note, parked from session 02 | 2026-09-18 |
| `promptbook-coder-foil/` | Observation notes | 2026-09-02 |
| `recovery/` | Says "in progress"; one file | 2026-09-02 |
| `voice-relay-00-probe/` | Parked draft, by design | 2026-09-18 |
| `harvest`, `nablarva-00-`, `nablarva-00-main-design-signpost`, `test` | Empty | — |

Cited as closed, with no directory on disk: `muticula-00-brief` and a round named "B0".

### Contradictions

| # | Conflict | State |
|---|---|---|
| 1 | `PROJECT.yaml` says docs-only with language TBD; Python and shell bricks are built and deployed | Open. The bricks decide nothing for the animal's language |
| 2 | Docket items pending since 2026-08-02 while sessions proceed | Open |
| 3 | Keystroke doorbells proposed in September against `flag.md` L4 | **Fenced.** Cartan's fold and blueprint mark them as proposals `[R]`. L4 stands |
| 4 | L5 and L11 read as live; L12 supersedes both | By design: the file is append-only |
| 5 | `AGENTS.md` and `flag.md` cite paths that moved | Open. See audit 2, §4 |
| 6 | `docs/repo-unification` says `pull --rebase`; L12 forbids it | Open `[S]` |
| 7 | Seats in use (Trajectory, Flight, Cartan) against a four-seat roster | Open |
| 8 | ia-sync pulls with `--rebase`; nablarva must never | Both correct for their own repository. A trap for a seat that works in both |

## 4. Progress patterns

### 4.1 One person serves every queue
About a dozen gates wait on Majkee across two repositories, plus the docket. Each needs
him to reload its context first. Work arrives faster than one person can clear it.

### 4.2 The development bus uses him as its wire
A review cycle is POINT, RETURN, VERDICT between two vendors. Each leg needs a path
carried by hand. The process built to remove human carriage consumes it. Verdicts come
within one to three rounds `[S]`; the delay sits between rounds.

### 4.3 Prepared, not run

| # | Step | Prepared | Mark |
|---|---|---|---|
| 1 | Files-only control spike (docket 1) | 2026-07-31 | `[R]` |
| 2 | Seam-probe stage 6, the write-back | 2026-08-01 | `[R]` |
| 3 | Invariant experiment design (entity study) | 2026-08-04 | `[R]` |
| 4 | Laboratory capture fixture (Wave's next move) | 2026-08-05 | `[R]` |
| 5 | Costa probes A–D | 2026-08-07 | `[S]` |
| 6 | The four task files of the blind research program | 2026-08-07 | `[R]` |
| 7 | Pipe-qualification sitting 1 | 2026-09-14 | `[R]` |
| 8 | Voice-relay probe | 2026-09-16 | `[S]` |
| 9 | Onion probes P1–P3 | 2026-09-18 | `[R]` |
| 10 | Tunnel T2 verification probe | 2026-09-21 | `[R]` |

What was measured in the same period: the seam-probe read side; termbrana's host
contract and tunnel round trip; the ovitmugen office walk; offline tests of the
qualification probe.

### 4.4 Decisions re-presented, not decided

| Date | Where |
|---|---|
| 2026-07-31 | Triad comparison: seven-item docket |
| 2026-08-02 | `flag.md`: the docket, plus O1–O4 |
| 2026-08-07 | Preflight task files, under "DECISIONS FOR MAJKEE" `[R]` |
| 2026-09-29 | Cartan's blueprint: four decisions that point back to the docket `[R]` |

The items are posed as choices between two goods, with nothing to weigh. Docket 1 was
designed to be settled by a one-day experiment. The experiment is the decision.

### 4.5 Designed again under a new name

- **Sensing a living session:** four instruments between 2026-08-05 and 2026-09-18
  (laboratory, termbrana, ommatermia, onion observer). Each has its own object, and
  one is partly built. This audit found no brief that states what it adds to the
  previous ones.
- **A file bus:** three directory layouts. Only `_bus/` is in use.

### 4.6 Sessions open faster than they close
Session 02 opened the day 01 received its GO. Session 03 opened while 02 waited. Peak
was four at once `[S]`. Closed beds stay listed and unpreserved.

### 4.7 Long inputs to a short decision
The working blueprint is 507 lines `[R]`. It is careful work, and it ends with four
decisions. A person deciding needs the four decisions and the evidence for each.

### 4.8 Approval ladders
Session 02 needs three separately transcribed approvals before anything is sent. **The
ladder is proportionate:** the private server shares `~/.codex`, with credentials and
the thread database, with the working sessions `[R: STATUS line 22]`. The cost is the
waiting: fifteen days. A probe that touches nothing shared would not need such a
ladder.

## 5. How reliable the agents were in this audit

Thirteen sub-readers ran. About half made a material error that a check against the
source exposed.

| Reader | Error |
|---|---|
| Onion extraction | Read the plan's `DONE:` tests as claims of completion. Reported status flags that a search of the files does not find |
| Meshup melt | Graded the seam-probe write path as measured. The report says stage 6 was not run |
| Structure inventory | Said the seam-probe files survive in git history only. The report is on disk |
| Gap loop 1 | Rated the driller as a direct match to the loop. It solves a problem the file loop removes |
| Gap loop 2 | Gave a seat an affiliation the file does not state. Called Wave's proposals "selected" decisions |
| Gap loop 3 | Said the text does not mention delivery. Section 7 of the seed is about it |
| Session audit | Counted 77 actions where the STATUS says 99 |

Oraculum's own errors, caught by Janus:

| Claim | Correction |
|---|---|
| One narrow unknown; two outward probes decide the pattern | The return wake decides it, and no prepared probe measures it |
| The keystroke-doorbell conflict is unreconciled | It is fenced in the open |
| Ratify Python as decided by practice | Docket 2 is Majkee's alone and carries a learning motive |
| Approval ladders are long relative to risk | The ladder guards shared credentials |

**Consequence.** A summary from an agent is a lead. Before anything reaches a gavel,
the head checks the quoted lines in the source.

## 6. Proposals

Ordered. Each needs Majkee's word.

### M1 · Close sweep, in one sitting
Clear items 1, 6 and 7 of §2 with one-line words. Decide each orphan in §3 by hand:
keep, park with a reason, or remove.

### M2 · Two active gates in nablarva
Keep at most two sessions active. Park the rest with one line saying why and what
reopens them. A parked session is a recorded choice; it is no longer waiting on anyone.

### M3 · Return-wake probe first
Majkee's decision of 2026-09-29. Shape only; the owning session writes the procedure.

| Part | Question | Kind of answer |
|---|---|---|
| Facts | On a disposable session of each vendor: does the Stop hook fire; what does it receive; does a native message arrive in a running session | Instrumented. Settled once |
| Behaviour | Does one full round trip close without hands; does it stop at its limit | Characterized. Needs several runs |

- Session 02 owns native experiments `[R: blueprint line 383]`. Its accepted sequence
  puts the return wake last, as increment C. The proposal is to re-pin so that C is
  measured beside B.
- Prefer targets that share nothing with the working sessions. That shortens the
  ladder honestly.
- A stop result is a good result. It tells which pattern to drop.

### M4 · Decide by experiment; park the rest

| Docket item | Needed for the first loop? | Proposal |
|---|---|---|
| 1 · Files-only spike | The loop is the spike | Re-table; declare the first loop to be the control |
| 2 · Language | No. Hooks and short scripts suffice | Park until a broker is wanted. The C++ appetite stays open |
| 3 · Git as archive | No | Park |
| 4 · Broker lifecycle | No. The first loop has no broker | Park |
| 5 · Journal store | No. The first loop uses released files | Park |
| 6 · v1 cut | Yes | Ratify. Practice already matches it |
| 7 · Naming | No | Park |
| O1–O4 | No. All concern stage 2 or the monitor | Park |

### M5 · The first customer is the development bus
Use the loop first on the review cycles between Claude and Codex seats. The files
exist, the pain is measured, and the baseline is the 2026-09-14 carry.

### M6 · One-line asks
Every ask to Majkee fits one line and names its cost: quota, risk, and whether it can
be undone. Evidence stays in the linked file.

### M7 · Build on the previous design
A brief for a new instrument names the earlier members of its family and states what
it adds.

### M8 · Check quotes before a gavel
See §5.

## 7. The words Majkee can give

Each line is one decision. None is urgent except the working tree.

| # | Word | Effect |
|---|---|---|
| 1 | Commit the working tree | Secures four days of uncommitted work and all of session 03 |
| 2 | `commit ok` and the count for session 01 | Closes and preserves the bed |
| 3 | Commit and push termbrana-02 | Closes a bed open since 2026-09-02 |
| 4 | Re-pin session 02 toward the return wake, or give `open_approval` | Starts the first measurement |
| 5 | Which two sessions stay active | Sets the limit of M2 |
| 6 | Ratify docket 6; park 2, 3, 4, 5, 7 and O1–O4 | Empties most of the docket |
| 7 | Re-table docket 1 as the first loop | Settles a question open since 2026-07-31 |
| 8 | Confirm or correct the trust-sphere reading | Audit 1, §2 |
| 9 | Keep, park or remove each orphan | §3 |
| 10 | Describe the reposoma tool, or remove its heading | Audit 2, §2.4 |
| 11 | Approve, amend or reject the wrapper rewrites | Cartan folds what is approved |
