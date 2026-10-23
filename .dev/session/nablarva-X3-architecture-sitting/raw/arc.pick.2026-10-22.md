---
doc: arc pick record — X3 architecture sitting
seat: houston · card: sitting · route: child of the Claude Oraculum MAIN head (Mode B), operator-assigned
written: 2026-10-22 · office
records: Majkee's PARTIAL pick on raw/arc.r2.md (shape + Q5); Q1–Q4 and Q6–Q8 not yet answered
state: STOPPED — no ARCHITECTURE.draft.md, wrapper diff, lock-proposals or card draft until the head relays Majkee's Q answers
pen: new file in raw/; arc.md and arc.r2.md stay as written
---

# Arc pick record

## 1. Majkee's words, verbatim (relayed by the head)

`said: majkee (relayed 2026-10-22)`:

> 1. how the architecture document is laid out : B.
> 2. Q5 : i need little coherence, not saying some bricks can't live independent, but on another side would be fine main body as 'ready to install packages' which requires at least nablarva + toolboxes as application which need all legs coherent with build. But agree that can be solved later if this session do not need to decide.
> 3. questions Q{1-8} I will reply in next loop.

What this record takes from those words:
- **Shape = B (seam ledger)**, as described in arc.r2 §6. My lean was B with v0's
  "decision · reason · revisit when" columns. Majkee said "B". He did not explicitly accept or
  refuse that borrowing, so I treat it as part of B as described there and do not count it as a
  separate ruling.
- **Q5 is Majkee's own answer, not my default.** The words above govern. §4 below is my reading of
  their consequence and does not replace them.
- **No Q default is accepted by silence.** Item 3 defers Q1–Q8 to the next loop.

## 2. Correction: L13 attribution (arc.r2 §4 item 1 is superseded on this point)

arc.r2 §4 item 1 said "Observe seam owner = termpanum (locked: L13)". **That overstated the
lock.** L13 reads "Observation lab = termpanum" (said: flag.md L13; the head checked it). It
locks the **name**. It does not lock observe-seam ownership, exclusive observation production,
co-production or collector lifetime.

The correction comes from two sources. One is myShell's relay, at
`raw/relay.x2-answers.myshell.2026-10-22.md` and cited as `said: myShell relay`. The other is
Cartan X2's disposition, heading 6, "Decline its asserted locked ownership", at
`.dev/session/nablarva-X2-builder-narative/raw/disposition.x3-vectors.cartan.2026-10-22.md`,
sha256 `efe7573d…68f7b` as pinned by the head. I accept it; this was my error.

In the B draft:
- The observe row names **termpanum as the observation lab (locked: L13, the name only)**.
- Producer and seam ownership is written as **`unknown:` / open**.
- The rest of that row stays attributed to its own sources: siblings (said: X2 RUNBOOK), local
  records, separate delivery and the viewer restriction. Those are compatible boundaries, and none
  of them appoints an owner.

## 3. X2-1..3 answers

`said: cartan-x2 (relayed by Majkee; confirming said: myShell relay)`:

| question | answer | consequence for the B draft (`inferred: houston`) |
|---|---|---|
| X2-1: sole producer or co-producers? | "Exclusive producer/co-producer ownership is unspecified." | The observe row lists termpanum (lab), v0's "living tissue" hooks (said: v0) and VIST's Antensor (said: VIST brief) as candidate producers. Ownership stays open. No topology is chosen. |
| X2-2: animal-level compatibility in C? | "C requires no first-release animal-level consumer compatibility." | Local records are consistent with the doc by construction. The shared envelope stays open (docket 8; four candidate envelopes, X4). Per X2's disposition, a docket-8 disposition alone would not promote X2's records. An explicit interface agreement would still be needed. |
| X2-3: collector lifetime owner? | "Collector-lifetime ownership is unspecified." | The lifetime row carries L17's ovitmugen protection as a constraint, and it neither extends nor transfers that protection. The collector owner is `unknown:`. The viewer restriction (said: X2 plan §3 L) stays. |

Also `said: cartan-x2`: "X2's plan GO does not wait on X3", and "No material amendment was
needed". The draft therefore adds no X2 prerequisite. Q8 is answered on its substance by these
replies; see §5.

## 4. What changes in the planned B draft because of Q5's own answer

`inferred: houston` throughout this section. Nothing here is resolved.

**Two kinds of coherence, kept apart.** Majkee asks for coherence of *build and install*: a main
body as "ready to install packages … nablarva + toolboxes as application … all legs coherent with
build". He also keeps independence possible: "not saying some bricks can't live independent".
L17 speaks to *runtime and use*: "independently useful clients; shared mechanisms belong at a
narrow integration boundary … no common framework or transport is authorized by the Phase 0
build" (locked: L17). I read these as two different axes:
- **Run/use independence** (L17, termbrana "standalone … nabLarva completely absent"): each organ
  works alone.
- **Build/install coherence** (Majkee's Q5): the organs ship together as one installable
  application whose legs build consistently.

They can both hold: one install that delivers independently usable clients. One point is still
open, and I name it without resolving it. **Does build/install coherence imply any shared runtime
mechanism?** Examples would be one router (X5), one `init.zsh` (v0), or one substrate (X11). If it
does, the L17 narrow-edge rule applies, along with its open owner/home/API.

**Changes to the B draft** (these follow from the pick and remain proposals until GO):
1. **New seam row: build · install · publication.**
   - Owner: `unknown:`.
   - Governing locks: L6 (promotion out = reviewed merge, never auto-deploy); L8′ (composer
     publication to or through ia-sync; deploy, installer or agent-assisted); L12 (one repo,
     `toolbox/termbrana/` subtree); L17 (composition family at `~/ia-sync/zsh/termbrana/`).
   - Current route (`said:` wrapper VOLATILE): ia-sync source → `deploy.sh` → `~/.config/zsh/`,
     plus `install-pkgs`.
   - Candidates (`said:`): X2 plan §3 E (a packaged termpanum in `~/ia-sync/zsh/termpanum/`,
     "Packaging GO is not deploy GO"); v0's single `nabla/` repository and init line.
   - Accepted: today's delivery route as described in VOLATILE, which is `said:` and not locked.
   - Planned: Majkee's "ready to install packages" direction (`said: majkee`, Q5).
   - Open: the package shape, whether the install is one or several, how source homes split
     between nablarva and ia-sync, and the keeper of packaged copies.
2. **Layer model.** Build/install becomes a cross-cutting concern that sits *beside* the runtime
   layers, not inside them. v0's six layers remain the brick-layer sub-model, which is still a
   candidate.
3. **X5 (one animal-wide router vs a pattern per organ) stays open.** Majkee's words point toward
   coherence and do not mandate a single router. "can be solved later" applies.
4. **X6 (the `nabla` name vs L13's `nablarva` command rule) gains weight.** An installable
   "nablarva + toolboxes" application needs a name for its install surface. L13 constrains that name.
   Unresolved.
5. **Open-questions section.** Q5's own answer is recorded verbatim as a direction with a "solved
   later" qualifier. It is not a lock. lock-proposals.md may carry a lean (G7 b), tagged
   `inferred: houston`.

## 5. Which Q still blocks

The head notes that Q1 is open and that drafting, including the R-5 re-pin, must not start.

| Q | state | blocks |
|---|---|---|
| Q1 fresh audit before drafting | open | **Drafting as a whole, including R-5.** A "yes" sends the work to a separate audit first (to-oraculum prompt in arc.md §6). |
| Q2 ovitmugen §3.2.x notes | open | **The wrapper diff's scope.** |
| Q3 VIST placement | open | The observe and deliver rows' VIST cells. |
| Q4 two architecture-owner texts | open | The compose row and the commit-order note. |
| Q5 v0 scope | **answered (own, §1)**, "can be solved later" | Does not block. It shapes §4 above and is carried as an open direction. |
| Q6 vocabulary collisions | open | The collisions list (X12/X13) in open questions. |
| Q7 v0 implementation material | open | Only whether a GLOSS question is asked. It does not block the draft. |
| Q8 X2 questions | answered on substance by cartan-x2 (§3) | Does not block. Majkee may still confirm or override in his next loop. |

So **Q1 blocks the start**, and Q2, Q3, Q4 and Q6 block draft content. Q7 only affects whether a
GLOSS question is asked. Q5 and Q8 do not block.

## 6. Unknowns this record adds

- `unknown:` whether build/install coherence (Q5) implies any shared runtime mechanism (see §4).
- `unknown:` the owner of the build/install seam row, and its package shape.
- `unknown:` observe-seam producer ownership (X2-1) and collector lifetime owner (X2-3). Both are
  confirmed unspecified.

STOPPED. Next step: the head relays Majkee's Q1–Q8 answers verbatim to this same child.
