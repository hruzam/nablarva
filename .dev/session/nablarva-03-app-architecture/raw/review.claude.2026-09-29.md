# Claude review and Cartan integration — 2026-09-29

Controller-preserved response from a bounded, one-off Claude Code CLI consultation
requested by Majkee. Read/Glob/Grep only, no shell or write tools, no MCP servers,
no session persistence. This is not an attached full working session and proves no
inter-agent wake path. CLI completed successfully; output reports model
`claude-opus-5-5`. The reviewer reports inspecting all three photos.

Source receipt: SHA-256 of original CLI JSON
`788a252cda26456e406340f19dbe52379e28062b688910b05598f4b0da495e58`.
The JSON itself is temporary local process evidence; the complete returned review is
preserved below. External ia-sync reads were denied by the reviewer's scoped tools;
its ia-sync conclusions use excerpts supplied by Cartan. That limitation is retained.
Line references below refer to the draft before integration, not the revised draft.

## Review — verbatim

# Independent architecture challenge: nablarva-03-app-architecture

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), running as a one-off read-only subagent. I am not an attached or persistent living session. This review is architectural evidence only. It does not prove any live transport, and it is not a GO or a passed gate; those are Majkee's.

**Photos:** I opened and inspected all three JPEGs.

## Verdict: REVISE (small revision)

The direction holds. A small core plus adapters plus thin clients, with no GUI or daemon for now, fits Majkee's workflow and flag L3/L4/L6/L8/L12. Supporting it as written would miss two blocking contradictions, but both need only a few lines. Rejecting it isn't justified: nothing in it goes against a lock.

## Findings (ranked)

**1. BLOCKING. The first slice tests the harness task protocol, not Majkee's chosen workflow.**
- Majkee's first workflow is "prompt file → wake recipient → reply file → wake sender" (`RUNBOOK.md:26-28`).
- The blueprint itself says ordinary messages must not need a RUNBOOK, VERDICT or STATUS (`architecture.working.md:79-84`).
- Yet the slice's success chain in §10 runs POINT → RETURN → VERDICT → STATUS, with "review precedes STATUS advancement" (`architecture.working.md:293-301`, `:392-395`).
- **Edit to §9/§10:**
  - Slice success = a released prompt file, the bound recipient woken, and a correlated reply file. The sender is woken, or the manual return is recorded as the gap.
  - Reuse POINT/RETURN file shapes and the `cycle`/`return_to` correlation as the carrier, so no second vocabulary appears.
  - Move VERDICT/STATUS to "optional harness wrapping when the exchange is an engineering assignment."
  - Keep the attention signal inside the slice. The 055516 sheet asks for this too: "system should recognize interactive prompts."

**2. BLOCKING. The wiring route contradicts the session scope's own contract.**
- §7's "Wire client" row names `session/base.zsh` as the precedent (`architecture.working.md:185`).
- But `ia-sync/zsh/session/base.zsh:11-12` says session was "rescoped out of nablarva/, which is a different animal."
- `convergence.md:40-42` also limits session tools to "where their task scope fits."
- **Edit to §7:** the nabLarva client wires through its own define-only zsh scope, sourced from `config.<machine>.zsh`. That means reconciling the stale `ia-sync/zsh/nablarva/` engine (§4, `:104-108`) instead of adding a `session/` partition.
- Session tools may consume the app optionally. `runbook.py:597-604` is the precedent: import it if present, degrade silently when absent.

**3. DECISION TO NAME, NOT BLOCKING. Delay promotion and installation until after the first pair.**
- §5 correctly flags that "app source in nablarva, release via ia-sync" conflicts with L6's "structural builds stay on the surgical table" (`flag.md:27-29`).
- The only existing precedent goes the other way: ovitmugen's source lives in ia-sync, with docs in nablarva (`AGENTS.PROJECT-DESIGN.md:158`, `base.zsh:39-43`).
- **Edit to §5–§8:** add a "Phase 0" line.
  - The first pair runs in the foreground from the nablarva bed as an L6 experiment.
  - No install-pkgs recipe, no XDG homes, no PATH launcher.
  - Removal = stop the process, then preserve and prune the bed.
- Label §6–§8 "post-pair release design." Decide the promotion model only once the pair passes.
- This fits §6 (`:152`): Phase 0 is not a release, so the "never resolve a release through a changing checkout" rule doesn't apply.

**4. LATER DECISION, MUST STAY EXPLICIT. The roller's history conflicts with prunable beds.**
- L9 says `session/<topic>/` dirs "die with the task" (`flag.md:40`).
- Majkee wants collectable messages for the roller (`RUNBOOK.md:29-30`).
- §6 (`:166-170`) notices this but leaves it open.
- **Edit:** list it in the §9 decision list as item 3a. For the first pair only:
  - Released prompts are write-once copies (released content can't change afterwards). Replies sit beside them.
  - Bed closure preserves them into a named durable home.
- Choosing DATA_HOME vs a room journal stays a post-pair decision.

**5. HYGIENE. Fix the install-leg evidence and slim the blueprint.**
- These claims check out against the supplied excerpts:

  | Claim | Where verified |
  |---|---|
  | Even `list` creates install state | `run.sh:38-41` |
  | `update` runs every eligible auto task | `run.sh:118-161` |
  | `unmark` only forgets a receipt | `run.sh:174-178` |
  | No uninstall verb | `run.sh:182-185`, though the excerpt ends at 185 |

- "Additive `rsync -a`" (`architecture.working.md:183`) cannot be confirmed: `RSYNC_FLAGS` is defined outside `deploy.sh:231-277`. Cite the defining line or mark it unverified.
- **Add to §7:** any future nablarva recipe should be `automation: manual` or host-gated. Otherwise a routine `run.sh update` would install it without being asked.
- §10 (about 170 lines) repeats §3/§9. Fold it to a pointer plus the acceptance conditions.
- The wrapper itself is already thin, with a correct VOLATILE section. Leave it as it is.

## Cheapest coherent alternative

Build no app yet. For the first pair:
- One small foreground command in the nablarva bed that does three things: `release` (write-once copy of the prompt, plus `return_to`), `wake` (only through whatever carrier nablarva-02 qualifies), and `await-reply` (checks that the reply's correlation matches).
- The existing session tools stay independent.
- Manual return carriage is recorded as the measured gap.

Decide the core-versus-bricks question, promotion, XDG homes and lifecycle only once that loop has been measured against `nablarva-02-pipe-qualification/raw/baseline.md`. This is the blueprint's own "small core" at size zero, so nothing needs to be rejected.

## Read-set

- `AGENTS.md`, `.dev/session/flag.md`, `.dev/session/pulse.md`, `PROJECT.yaml`
- The bed: `RUNBOOK.md`, `STATUS.md`, `raw/architecture.working.md`, `raw/reading.notebook-2026-07-30.md`, and the three JPEGs in `raw/notebook-2026-07-30/`
- `.dev/session/AGENTS.PROJECT-DESIGN.md` (full; the Trajectory notes were read, not touched)
- `.germline/agents/convergence.md:30-69`
- `docs/repo-unification.2026-09-02.md` (grep). Its lines 11/54 show that the "retired" `sync.sh`/`deploy.sh`/`SYNC_DISCIPLINE.md` were the nablarva.devenv copies, not ia-sync's, so citing ia-sync's `deploy.sh` does not conflict with L12.
- `docs/ARCHITECTURE.md` (heading only: a pointer, no build)
- Existence checks for the linked `design.r1.md`, `baseline.md`, the meshup room proposal and the termbrana README
- ia-sync: only the controller-supplied excerpts

## Unknowns and limits

- **ia-sync:** my file tools are confined to the nablarva tree, so `/home/hruzam/ia-sync` was not readable. I did not independently check `deploy.sh` flags (`--codex-only`, the `RSYNC_FLAGS` contents), `run.sh` beyond line 185, `ovitmugen.py`, the stale `zsh/nablarva/nablarva.zsh`, `SYNC_DISCIPLINE.md` outside 104-117, or the publish-gate STATUS.
- **Not read:** the Muticula, Termbrana, Ommatermia, relay-contract and Costa sources cited in §4/§10. Their characterisations are Cartan's, not mine.
- **Photo receipt:** it matches what I see, with two notes.
  - It leaves out the 055444 header, "COMMIT PHILOSOPHY IS NICE LIGHT." Read it as immutable-release philosophy, not Git transport (L4).
  - 055516's "each option can be dedicated to separate receiver" suggests one prompt going to several recipients. That goes beyond a pair and should stay post-slice.
- **Not checked:** live deployment state, and whether the wake paths work in either direction. Both belong to nablarva-02 and I made no probe.

---

## Integration — Cartan

**Disposition: revised draft ready for Majkee / an attached colleague; no gavel.**
The [blueprint](architecture.working.md) incorporates the supported revisions:

1. **Product versus harness:** checked against the accepted first-brick A/B/C design
   and Majkee's prompt/reply direction. §9 now gives product success explicitly;
   §10 makes VERDICT/STATUS an engineering wrapper. Existing task steps stay binding.
2. **Wiring:** checked `session/base.zsh:11-12`, its optional runbook/ovitmugen bridge
   and the stale `zsh/nablarva/nablarva.zsh`. §7 proposes an explicit animal scope;
   generic session tools remain optional consumers. This is proposed future wiring,
   not a prohibition on the already accepted browser extension in session/.
3. **Experiment versus release:** §5 makes the bounded experiment distinct; §§6–8
   are post-pair release design. The suggested blanket move of the first pair into
   a new foreground command is qualified: existing A/B/C source ownership and live
   gates remain unchanged. Installation is not a prerequisite for qualification.
4. **Retention:** §9 requires a named preservation destination before pruning and
   proposes fixed released artifacts. The actual store and copy/reference contract
   remain undecided; no task files or schemas were changed by this proposal.
5. **Installer:** Cartan inspected `deploy.sh:24-38` and `install-pkgs/run.sh:181-189`.
   `RSYNC_FLAGS=(-a)` and the absence of an uninstall verb are confirmed from source.
   The draft now cites the flags definition and proposes initial manual activation;
   merely selecting a host would not prevent a routine automatic `update`.
   Repetitive exchange detail was condensed while preserving source pointers.

The notebook receipt now includes the commit-philosophy header. Interpreting it as
immutable-release philosophy is an inference, not a transcribed requirement. Likewise,
options addressed to separate recipients do not by themselves establish broadcasting
one prompt to many recipients. Multiparty behavior remains outside the first pair.

Independent verification here checked the cited source and the revised contracts;
it did not run an installer, inspect private runtime history, exercise a carrier or
re-test unrelated tools. The reviewer's reference to both wake paths belonging to
bed 02 is too broad: bed 02 owns the outward qualification; a return-wake extension
still needs its own declared qualification scope under the accepted C increment.
