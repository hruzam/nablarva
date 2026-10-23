# houston · audit — whole animal, post-promotion — 2026-10-23

`card: audit (full) · route: main session (claude --agent houston, cwd nablarva root), operator-invoked (majkee, X1 check 5)`
`input: raw/input.check5-audit.oraculum.2026-10-23.md (walked; its seven named inputs are answered in §Named inputs)`
`companion: raw/houston-audit.2026-10-23.post-promotion.diff (four checked-stamp hunks on PROJECT-DESIGN.md; majkee commits, Houston never applies)`
`classification useful / overreaching / missing is majkee's; I do not classify myself.`

Entry proof (germline read this session):
- `/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f`
- `/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36`
- `/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067`
- `/home/hruzam/.germline/agents/houston/cards/audit.md · stamp: e517cc86`

## Scope and walk

The card's order: wrapper (`PROJECT-DESIGN.md`) → organ bodies (`toolbox/termbrana/README.md` in full,
`toolbox/termbrana/DECISIONS.md` headings and authority lines, `docs/organs/stridularium.md` headings,
`docs/decisions/README.md`) → `docs/ARCHITECTURE.md` in full → guides and collateral
(`docs/repo-unification…`, `.germline/agents/convergence.md` anchors, ia-sync targets) → `flag.md` in
full, read against those artifacts. Saddle (`AGENTS.md`, `PROJECT.yaml`) and `pulse.md` were read for J2
and routing. One bounded read-only reader (zenith) ran git, sha256 and `ls` lookups that this route cannot
run itself (the Claude binding has no Bash). It wrote nothing.

## Coherence chain

`intent (flag) ≈ architecture (docs/ARCHITECTURE.md) ≈ RUNBOOK ≈ implementation ≈ documentation` —
**it holds, with one live break between flag and architecture** (C1). The promoted architecture is frozen
at r7. The four locks adopted after it (L18–L21) were adopted *from* it, but the document was not updated
to cite them. In one place it now states the opposite of a lock: "L17 holds unchanged". The
implementation node is still docs-only, which is declared and not a defect.

---

## mech — tested mechanically

- **M1 · wrapper pointer re-check, the full pass deferred from 10-07 M1. Clean.** Every link in
  `PROJECT-DESIGN.md` resolves: flag · pulse · PROJECT.yaml · docs/ARCHITECTURE.md (+ `#5-keys-code`
  → heading "## 5. KEYS CODE") · the addendum · `nablarva-03-app-architecture/README.md` · the session-03
  survivors · `toolbox/termbrana/README.md#composition-and-explicit-input-direction` (heading present) ·
  `toolbox/termbrana/DECISIONS.md` · `../../ia-sync/zsh/termbrana/README.md` (exists) ·
  `raw.nablarva/ovitmugen-00-console/draft.trajectory…2026-09-23.md` · the muticula master brief + STATUS ·
  the lab DESIGN/HYPOTHESES · the termpanum brief · the room and seam DESIGNs · the stridularium
  DESIGN/HYPOTHESES · `docs/organs/stridularium.md` · `docs/repo-unification.2026-09-02.md` ·
  `.germline/agents/convergence.md#interim-delivery-route` (heading "## Interim delivery route").
  Frontmatter `bindings:` (`~/.germline/agents/houston/binding.{claude,codex}.md`): I read the Claude
  binding this session; I did not open the Codex one. **This also closes the 10-07 "unverified":**
  `~/ia-sync/deploy.sh`, `~/ia-sync/SYNC_DISCIPLINE.md` and `~/ia-sync/install-pkgs/run.sh` exist (ls,
  2026-10-23). The pulse ovitmugen-01 gate cites `PROJECT-DESIGN.md § KEYS CODE`; that pointer heading
  resolves at :294.
- **M2 · C1 wrapper hunk (10-07 .diff): LANDED.** Commit `189efed` (2026-10-07, "applied by
  convergence") added it to `.dev/session/AGENTS.PROJECT-DESIGN.md`. It survived the move to the root
  (`22cfa26`) and now sits at `PROJECT-DESIGN.md:111–113`, with its links rewritten correctly for the
  root. The lock side of C1 is check 6 (`raw/check6.l12-lines…`). I did not absorb it.
- **M3 · `docs/ARCHITECTURE.md` = r7, byte for byte.** sha256 `3330b99a…e880` equals
  `nablarva-X3-architecture-sitting/raw/ARCHITECTURE.draft.r7.md`. The five relative links resolve. So do
  the non-link paths: the triad and Y vision, `.dev/research/termpanum-events/events-map.v0…`, the room
  design and `~/ia-sync/zsh/guides/claviature.global.spec.md`. **Verified wrong: its own state line.**
  `:3` reads "`state: DRAFT r7 for majkee GO — not promoted; promotion target docs/ARCHITECTURE.md`",
  inside the promoted file (`f20dda5`). `:3` also carries `checked: 2026-10-22`. This is a doc header,
  outside the audit pen (wrapper only), so it gets no hunk. It pairs with C1: fix both in one edit by the
  doc's owner.
- **M4 · Pins owed at promotion were not paid, and part is still unpayable.** `ARCHITECTURE.md`
  §Sources ends "A promoted document must not point into a prunable session folder without these pins"
  (identity evidence rule 7). After promotion, by item:
  - *payable now:* `answers.majkee.pick-and-q1-q8…`, `answers.majkee.r9-1-notes…`,
    `answers.majkee.r9-1-abc…`, `arc.r2.md`, `arc.pick…` all exist at `519a211` (git ls-tree). The pins
    can be written as `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/<file>`.
  - *not payable:* the X2 `termpanum.build-plan.md` and `disposition.x3-vectors.cartan…` are in no
    commit checked (absent at `519a211`; the disposition file is untracked in the X2 bed per git
    status). The doc cites them by sha256 only. If the X2 bed is pruned before they are committed, these
    cites go dark.
  - *unverified:* nablarva.v0 sits in `nablarva-X3-architecture-sitting/raw-additional-my-appology/`,
    not `raw/`. X3 STATUS says `519a211` includes it. My ls-tree covered `raw/` only, so its pin path is
    unconfirmed.
  - The §9 collision table's "`raw/arc.r2.md` §3 (pin owed at promotion)" is the same debt.

  This is a doc edit (not my pen) plus a commit decision on X2 files (the X2 head's). **Order matters:
  prune neither the X3 nor the X2 bed before this is paid.**
- **M5 · `checked:` stamps (the X0 audit's "missing" #2) — proposed in the .diff for four places.**
  These are VOLATILE (`checked 2026-09-29` → `2026-10-23`), §3.2 ovitmugen, §3.5 muticula and §3.7
  stridulatrix. For each, every pointer resolved (M1) and I found nothing in the section contradicted by
  flag L1–L21 or by `docs/ARCHITECTURE.md` §4/§7. No meaning changes. **Deliberately not stamped:**
  - §3.1 termbrana keeps `2026-10-21`. The README it names as owner of the "approved direction" now
    carries a superseded L17 phrase (C2).
  - §3.6 termpanum and §3.8 stridularium are not stamped. Each still names closed "session 03" as the
    owner of open choices (J1b).
  - §3.3 instarmux and §3.4 reposoma are empty headings, with nothing to check.
  - §1/§2 are operator and pre-architecture prose (J1b).
- **M6 · No project Houston wrapper (addendum §5): holds.** `.claude/agents/` holds only `tester.md`, and
  `.codex/agents/` is empty. The global loader route is the only one, as the fold intended.

## judge — needs architectural reasoning

- **J1 · Thinning: KEYS CODE done; the pre-architecture narrative remains (J1 of 10-07, residue).**
  - *J1a, done:* KEYS CODE body moved, pointer kept (`f20dda5`; diff numstat per X3 STATUS). L16.9 is
    satisfied for the shared grammar.
  - *J1b, open:* wrapper §2.2 "Architecture work" still frames the architecture as pending. It says "A
    small application core with explicit adapters and thin clients is the candidate under challenge",
    "The architecture session proposes final organ homes", and §3.6/§3.8 hand open choices to "session
    03" (closed 2026-10-05). The architecture now exists (§4 seams, §7 homes), and L18 locks the home
    rule. `inferred: houston`: these paragraphs should collapse to pointers into `docs/ARCHITECTURE.md`
    §4/§7 and L18. That replaces text with a different claim of where truth lives, so the meaning moves.
    **Not mechanics → finding.** The owner is the wrapper keeper's next sitting/edit, at majkee's word.
- **J2 · Saddle seat model: state unchanged, still open, separately owned (input 6).** Current state:
  `AGENTS.md` "Route by seat" still reads "**architect** (@Houston-family) — plan + gates; owns
  `.dev/session/pulse.md`", and `PROJECT.yaml:18` keeps `agents: [ architect, challenger, researcher,
  implementer ]`. Both still contradict `locked: L16.1`: Houston never owns lifecycle or gates, and cSharp
  owns RUNBOOK/STATUS. X1 STATUS holds name "J2 → its own saddle owner". Reported only, not folded in.
- **J3 · Conventional names per seam (input 2, `said: majkee` "05 Q1: yes").** The ledger
  (`docs/ARCHITECTURE.md` §4) is project vocabulary only. Each candidate below is `inferred: houston`, a
  pattern I recognise, unverified against literature. 05's own template routes the confirmation to a
  research pass (@Epoch). Seams ranked by expected gain, i.e. how much searchable prior art a name would
  unlock for builders:
  1. **room truth** → *event sourcing* (single-writer append-only log), *consumer offsets / cursors*,
     *CQRS projections / read models*. This has the most prior art and touches docket 4/5/8.
  2. **deliver / write into a session** → *notify-and-pull* / *claim check* (content in files,
     signal-only wake), *doorbell* (the hardware-queue term: NVMe/virtio). The doorbell row is still
     open, so naming it may widen the alternatives majkee asked for (R9-1 N3).
  3. **checkout coordination** (muticula) → *advisory locking*, *leases*, cooperative vs mandatory
     locking. The muticula gate question is literally cooperative-vs-enforced.
  4. **view · layout · process lifetime** → *detachable terminal session* (screen/tmux attach model) vs
     *process supervisor*. The X3/X8 collisions are this distinction.
  5. **observe** → *passive tap / sidecar observer*, *terminal session recording*; the VIST controller
     and actuator split ≈ *sense → decide → act (control loop)*.
  6. **context sourcing · reading** → *context assembly / retrieval*, *content-addressed manifest*
     (pins ≈ lockfile hashes).
  7. Low gain, already near-conventional: **compose** (*framing with a boundary delimiter*, cf. MIME
     multipart / heredoc), **configuration · roles** (*RBAC*, *config layering*), **key meanings**
     (*keybinding convention / command palette*), **build · install** (*packaging, staged promotion*),
     **cross-host** (*hub-and-spoke broker over SSH*), **human door** (*thin client / remote console*).

  Shape: an added "conventional name" column (or a note per 4.x) is a content addition to the
  architecture document. It is not in my pen. It goes to the doc's owner, most cheaply with the C1/M3/M4
  edit, after a bounded research pass on ranks 1–4.

## cross — spans surfaces

- **C1 · `docs/ARCHITECTURE.md` (frozen r7) vs flag L18–L21 (input 1). Verified wrong in one place;
  provenance lags in four.** L21's own text says "Record: docs/ARCHITECTURE.md", so a reader following
  the lock lands on the contradiction.
  - *wrong now:* §2 item 5, `:102–104`: "**The tension is named and left unresolved here** … P5 … offers a
    reading (P5-a) or an amendment (P5-b). L17 holds unchanged until a GO names one of them." Majkee
    named P5-b (R9-2), and `locked: L21` superseded two L17 phrases (Archived index line).
  - *the same tension, still listed as open:* §4.7 last bullet; §9 X5 row ("proposal P5"); §9 other open
    items, "majkee's one-body direction against L17's narrow edge". These are now settled by L21. Still
    genuinely open, and correct to keep: the shared layer's owner/home/API (L17 + L21 both leave the
    implementation unreleased).
  - *tag lag, `said:` where a lock now exists:*
    - the §7 home rule ("said: majkee, gavel deck STEP 4") → `locked: L18`;
    - §8 "Where decisions live" ("said: majkee, STEP 5") → `locked: L19`;
    - §4.1 / §7 "VIST — observation principle" ("said: majkee Q3") → `locked: L20`.

    The statements are true. Their epistemic tag is outdated (L16.11).
  - *smallest fix, the owner's choice (not my pen):* (a) one post-promotion note under the `:3` header,
    "Since promotion: L18–L21 lock §7 homes, §8 decision homes, §4.1 VIST, and resolve §2 item 5 as P5-b
    (L21). Where this text says otherwise, flag governs." It costs the r7 byte identity, which the record
    preserves at `519a211` anyway. Or (b) an r8 promotion folding the same plus M3/M4. The tension to
    weigh: freezing r7 keeps the gavel evidence clean, while correcting keeps the durable home true.
    `inferred: houston`: (a) now, (b) when the next architecture-touching sitting runs.
- **C2 · Termbrana organ body vs L21.** `toolbox/termbrana/README.md` §"Layering B — L17" reads "Any
  common mechanism is prospective and belongs at a narrow integration edge with demonstrated consumers,
  not a framework built by this phase", and §Composition repeats it. That is the L17 phrase L21
  superseded. What survives L21: independent clients; "a particular tool still runs without waking the
  whole animal"; no shared-layer implementation released. The README's "standalone operation with
  nabLarva completely absent" remains consistent. The organ contract is the organ owner's (L11
  governance; a README edit citing L21), not mine. Consequence for M5: §3.1's stamp stays at 10-21.
- **C3 · Houston addendum vs L18 and the promotion (input 3).** Verified stale in
  `.germline/agents/houston/nablarva.md` §1:
  - (a) the organ-bodies row says "**proposed, not locked** (`inferred: symmetry`, open for gavel)",
    but `locked: L18`;
  - (b) the architecture row says "today a pre-architecture pointer; becomes the body", but it is the
    body since `f20dda5`;
  - (c) its frontmatter `authority: … flag.md @ 32b645f` predates L18–L21 (age, a candidate rather than
    an error).

  The germline-03 handoff (`~/ia-sync/.dev/session/germline-03-foundation-audit/raw/HANDOFF.oraculum.x3-sitting-card.2026-10-23.md`
  item 2) carries **(a) only**; (b) is not in it. I report this and do not edit it. Addendum §7 says flag
  wins on contradiction, so nothing breaks today, but the next Houston loads a wrong map row.
- **C4 · Decisions stub vs L19 — tracked, not new.** `docs/decisions/README.md` still says "gaveled
  items land here as ADRs". L19 itself names this OPEN (correction vs retirement). One note:
  ARCHITECTURE §8 calls it "the root stub `decisions/README.md`". That resolves (links relative to docs/),
  but "root" misdescribes `docs/decisions/`. Fold it into the C1 edit.

## Named inputs → where answered

| # | input | answer |
|---|---|---|
| 1 | doc vs flag after L21 | C1. Verified wrong at §2 item 5, plus three open-list echoes and three tag lags. Not my pen. |
| 2 | conventional names per seam | J3. Ranked; a finding, not mechanics |
| 3 | stale addendum row | C3. Confirmed, plus one row the handoff lacks (b) |
| 4 | X0 audit "missing" ×2 | The X0 receipt (`d1c4b1e:…/_bus/27`, STATUS) names them as **organ-body/guide walk** and **`checked:` stamps**. #2: closed for four sections by the .diff; the three left unstamped get reasons (M5). #1: partly closed. The termbrana body was walked against flag (C2) and the stridularium body and decisions stub were read. The ADR texts were checked for authority lines only, not in full. Of the guides, only existence and pointers were checked, with no content review of `claviature` or the reposoma process guides, which govern sessions rather than the animal. |
| 5 | C1 wrapper hunk | M2. Landed at `189efed`, live at `PROJECT-DESIGN.md:111–113` |
| 6 | J2 | J2. Unchanged; reported only |
| 7 | M1 full pointer re-check | M1. Clean |

## Verified-wrong vs flagged-by-age

- **Verified wrong:** M3 (`:3` state line) · M4 (unpaid pins, partly unpayable) · C1 (§2 item 5 vs L21)
  · C2 (termbrana README vs L21) · C3 a/b (addendum rows) · J1b (§2.2/§3.6/§3.8 point at a closed
  session as owner).
- **Flagged by age only (candidates, not findings):** addendum `authority … @ 32b645f` · pulse still
  routes `nablarva-X3-architecture-sitting` although its gate closed 17:19. X3 STATUS holds declare that
  the row leaves at closure, so this is declared, not drift.

## Telemetry note (L16.7, report only)

The architecture doc's revisit signal reads "≥2 stale-pointer findings in one audit" (§8 defaults
table). This audit has **zero stale pointers** (M1 clean). Its stale items are stale *claims* and *tags*
(C1, C3, J1b), a different class. `inferred: houston`: the tier-0 default stands. The recurring
class is "lock adopted after a frozen doc is promoted"; if it repeats once more, it earns a promotion
step: "re-tag against locks adopted in the same gavel round". I install nothing.

## What remains unverified / out of card

- nablarva.v0's presence at `519a211` (outside the `raw/` ls-tree run).
- `~/.germline/agents/houston/binding.codex.md` was not opened (the pointer is named in frontmatter).
- Full ADR text of `toolbox/termbrana/DECISIONS.md`; content of the guides (only existence was checked).
- J3 conventional names are recognition only, with no literature check.
- `.hlm/`, `.majkee/` and `~/reposoma/.majkee/` were not read (bounds).
- Fixing C1/M3/M4 (doc owner) · C2 (organ owner) · C3 (germline forge) · J1b (wrapper sitting, majkee) ·
  J2 (saddle owner) · M4's X2 commit (X2 head) · pulse rows (head) are not mine to do.

## Authority self-check

Two Writes, to the two paths the invocation assigned (addendum §2 audit row). One spawn: zenith, a
bounded read-only reader within the binding's main-session delegation row. It ran listed read commands
and wrote nothing. No executor, no Houston→Houston, no creator. No edit to the wrapper, flag, STATUS,
addendum, organ body or architecture doc. The .diff is proposed only.
