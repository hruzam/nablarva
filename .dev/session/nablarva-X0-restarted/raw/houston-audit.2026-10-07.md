# houston · audit — whole animal — 2026-10-07

`card: audit (full) · route: living session (claude --agent houston), operator-invoked`
`this is the D-c real audit (L16.13 acceptance input). Classification useful / overreaching /`
`missing is majkee's to assign to this output; I do not class myself.`
`companion: raw/houston-audit.2026-10-07.diff (one proposed wrapper-mechanics hunk, C1).`

## Scope and walk

Whole-animal documentation-coherence walk (identity §audit), not build or functional
verification. Order walked: wrapper (`AGENTS.PROJECT-DESIGN.md`) → keeper role
(`convergence.md`) → whole-animal architecture (`docs/ARCHITECTURE.md`) → flag locks
(`flag.md`, esp. L12, L16) → machine skeleton (`PROJECT.yaml`) → router (`pulse.md`) →
invoking bed (`nablarva-X0-restarted` RUNBOOK + STATUS) → the detail doc L12 cites
(`docs/repo-unification.2026-09-02.md`). Pointer targets resolved by Glob.

## Verdict on the coherence chain

`intent (flag/PROJECT.yaml) ≈ architecture (docs/ARCHITECTURE.md) ≈ RUNBOOK (X0) ≈
implementation ≈ documentation (wrapper)` — **holds**, with two declared gaps that are
tracked, not drift: the architecture node is still a pre-architecture *pointer*, and the
implementation node is empty (docs-only phase, `PROJECT.yaml stack.lang: TBD` — declared,
not a defect). The saddle node (`AGENTS.md`) lags the newest lock (L16.1) — see J2.

No live broken pointer, no verified-wrong fact in the wrapper. The six stale session-03
links (seed / RUNBOOK U10) are confirmed repaired. All wrapper pointers resolve.

---

## mech — tested mechanically

- **M1 · pointers resolve (clean pass).** Every wrapper link resolves on disk:
  `flag.md`, `pulse.md`, `../../PROJECT.yaml`, `../../.germline/agents/convergence.md`,
  `nablarva-03-app-architecture/README.md`, `AGENTS.stridularium-design.md`, all six
  `meshup/*/DESIGN.md`, `survivors.nablarva-03.2026-10-05.md`,
  `docs/repo-unification.2026-09-02.md`. Commit-pinned cites (`nablarva@fd66470:…`) follow
  the durable-cite rule. **No diff needed.**
- **M2 · age-candidate, verified FIXED (report, do not re-report).** Seed flagged a stale
  `PROJECT.yaml` maintainer pointer to `.shared/…`. Verified: `PROJECT.yaml:16`
  `project-design-maintainer: .germline/agents/convergence.md` — resolves. Flagged-by-age,
  already corrected (`9421376`). This is a mechanical fact; age ≠ a finding.
- **M3 · lock text lags the vault set.** `.majkee/` exists as a second operator vault
  (4 files; I listed names to confirm existence, did **not** read contents — sealed by the
  operator-vault pattern, STATUS "contents stay unread"). `flag.md` L12's seal names only
  `.hlm/`. `docs/repo-unification.2026-09-02.md:20` (ADDENDUM 2026-09-03) generalizes the
  seal to *agent-reading, not git tracking* for operator vaults, but **L12's own text still
  names only `.hlm/`**. `inferred: houston` — the governing seal is the pattern, not the
  single path; the lock wording trails it. Fix (majkee's, not mine): one clause in L12 or a
  note that the seal covers all operator vaults (`.hlm/`, `.majkee/`). Low severity.
  **LOCK edit → findings-only, not in the diff.**

**Unverified (declared):** `/home/hruzam/ia-sync/deploy.sh` and
`/home/hruzam/ia-sync/SYNC_DISCIPLINE.md` are cited by the wrapper VOLATILE and
`convergence.md` as the live delivery route but sit **outside this repo and my working
dirs** — I did not resolve them. Whoever owns ia-sync should confirm they exist (bears on
C1).

---

## judge — needs architectural reasoning

- **J1 · wrapper is not thin yet; home-per-fact (L16.10) not satisfied for cross-organ /
  organ-level content — KNOWN interim, not a defect to fix now.**
  `said:` L16.9 homes shared cross-organ grammars and whole-animal architecture in
  `docs/ARCHITECTURE.md`; L16.10 "the wrapper stays thin … organs grow only on need."
  Observed: the wrapper carries (a) the full **KEYS CODE** shared grammar (lines 277–327,
  self-declared "the meanings live only here") — a cross-organ grammar L16.9 would home in
  the architecture doc; (b) organ-level detail — ovitmugen §3.2 Trajectory notes/principles
  (lines 162–213), termbrana §3.1 (lines 117–124) — which L16.10 would home in organ bodies.
  But `docs/ARCHITECTURE.md` is still a pre-architecture pointer ("First real architecture
  doc lands after the gavel docket closes"), and organ-body homes are **not yet locked**
  (`inferred: symmetry`, addendum §1 — `docs/organs/<organ>.md`, proposed not gaveled).
  → This is a *declared, tracked* interim: the content has nowhere locked to move to yet.
  Finding = name it so the thinning happens when the architecture doc and organ-body homes
  land; do not treat the wrapper's current fatness as drift. Not mine to move; not wrapper
  *mechanics* → findings-only, not in the diff.

- **J2 · the saddle's seat model is superseded by L16.1; reconciliation only partly
  scheduled.** `said:` `AGENTS.md` "Route by seat" — "**architect** (@Houston-family) —
  plan + gates; owns `.dev/session/pulse.md`"; `PROJECT.yaml:18`
  `agents: [architect, challenger, researcher, implementer]`. `locked:` L16.1 refined this:
  Houston = grounding architect **only** (explicitly *not* lifecycle, *not* gavel, *not*
  gates), cSharp = session lifecycle / RUNBOOK / STATUS / integration / closure, Oraculum =
  divergence. So "architect owns gates / owns pulse" no longer matches the authority model.
  The pending keeper migration (addendum §4) names only the AGENTS.md **convergence-route**
  edit — the broader architect-seat reconciliation with L16.1 is **not** in that scope.
  `inferred: houston` — a fresh agent reading "Route by seat" gets a pre-L16 picture of the
  architect seat. Majkee decides whether to widen the migration or file it separately.
  **SADDLE edit, not wrapper mechanics → findings-only, not in the diff.**

---

## cross — spans surfaces

- **C1 · L12 "deploy.sh / SYNC_DISCIPLINE.md retired" vs the live delivery route — RESOLVES,
  but the lock wording invites misreading.** Both sides verified, not flattened:
  - `locked:` L12 retired-list: "`sync.sh` / `deploy.sh` / `SYNC_DISCIPLINE.md` retired"
    (bare, no home qualifier).
  - `said:` wrapper VOLATILE (lines 105–108) and `convergence.md` §Interim delivery route
    (lines 46–60) cite `bash ~/ia-sync/deploy.sh` and `~/ia-sync/SYNC_DISCIPLINE.md` as the
    **live** route; convergence.md adds "`~/ia-sync/sync.sh` is the retired reverse-harvest
    script … do not use it" — i.e. it treats ia-sync's deploy.sh as live.
  - **Disambiguator** (`docs/repo-unification.2026-09-02.md:52-54`, which L12 cites as
    "Details:"): the retired trio "**lived in `nablarva.devenv`**"; ia-sync retired only its
    *sync.sh* (line 32). So the ia-sync `deploy.sh`/`SYNC_DISCIPLINE.md` are a **different,
    live** pair. The collision is resolvable — **not drift.**
  `inferred: houston`: the surface reader of L12 + wrapper cannot tell two same-named scripts
  apart without the detail doc. **Two fixes, split by pen:** (a) cheap wrapper mechanics — a
  one-line cross-ref from VOLATILE to repo-unification → **proposed in the companion .diff**
  (adds no new fact, only the in-repo pointer); (b) a qualifier inside L12 itself → **lock
  edit, findings-only, majkee's.** Pairs with the unverified-existence note above.

---

## Mechanics diff — one hunk proposed

`raw/houston-audit.2026-10-07.diff` carries **exactly one** hunk, for **C1**: a clarifying
cross-reference added to the wrapper's VOLATILE delivery paragraph, pointing at
`docs/repo-unification.2026-09-02.md`. It asserts no new fact (VOLATILE already states the
ia-sync route); meaning is unchanged → within the audit pen (L16.14). **Proposed only** —
majkee or convergence (who still holds the wrapper pen pre-migration, wrapper frontmatter
`maintainer: role: convergence`; addendum §4) commits; I never apply it, and the keeper
migration that would hand me this pen lists *this* audit (D-c) as a prerequisite.

All other findings (M3, J1, J2, and C1's lock-side option) are **lock / saddle / structural**
— deliberately **not** in the diff; they return to majkee as findings.

## What remains unverified / out of card

- `~/ia-sync/{deploy.sh,SYNC_DISCIPLINE.md}` existence (outside repo) — C1 / M3-note.
- Contents of `.majkee/` — sealed, deliberately unread.
- Commit-pinned `nablarva@fd66470:…` blobs — not re-fetched (git out of this walk); the pins
  are well-formed.
- My own render's witness/`verified:` state (binding says `none` today) is the head's /
  majkee's acceptance ledger, **not** an animal-coherence finding — noted, not audited here.
- Build/functional truth, lifecycle, promotion, the gavel — not my card.

## Authority self-check

Read + glob + two Writes, to this card's two authorized landing paths only (addendum §2 /
the plan's "exactly two files"). **No spawn used** — the walk fit one reader (me); a
`field`/`zenith` spawn would have been waste, not diligence. No STATUS edit, no wrapper edit,
no lock edit, no promotion, no executor spawned. Findings + one proposed hunk; majkee classes
and decides.
