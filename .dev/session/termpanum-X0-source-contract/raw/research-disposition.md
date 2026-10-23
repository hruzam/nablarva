# Termpanum X0 — research disposition

2026-10-22 · finite scoped D4 evidence pass · recipient: Majkee unless he names the
applicable relay-verdict owner.

## Scope, method and result

Cycle 01's four commands are historical: their literal filters excluded generated X0 body and
RETURN paths, but did not demonstrate the broader private/history exclusions claimed in its
prose. This packet makes no assertion that those commands avoided every forbidden candidate or
that any forbidden content was read. The original command limitation remains visible here.

Cycle 02 repeated one finite, documentary-only search over the same approved roots:
`.dev/session/`, `.dev/research/`, `meshup/`, `docs/`, plus root
`PROJECT-DESIGN.md`. Before content matching, `rg --files` enumerated 590 Markdown paths
under the four directory roots; the separately scanned root `PROJECT-DESIGN.md` made the
snapshot's content corpus 591 documents. Only project documentation/decision Markdown was eligible. Filters were
provided to `rg` before each content scan to omit `.git`, `.hlm`, `vendor`, private,
transcript, history, rollout, log, trace, secret and environment-named paths, and the entire
generated X0 bed. No shell error suppression was used; `set -o pipefail` makes any failed
`rg` stage fail the command. This proves the command's declared path filters and exit status;
it does not prove properties of omitted files that were not opened.

```text
set -o pipefail; rg --files --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' .dev/session .dev/research meshup docs | sort
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'relay-00-research' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'L14 D4|\bD4\b|research before (build|any RUNBOOK)' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'relay.*(verdict|disposition)|(?:verdict|disposition).*relay' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u
```

All four cycle-02 commands exited 0. The content searches returned respectively 20,
54 and 24 unique paths. Relevant inspected identities were
`meshup/REGISTRY.md`,
`meshup/seam.cross-vendor-relay.2026-08-05/raw/seed.relay-research.2026-09-30.md`, and
`meshup/seam.cross-vendor-relay.2026-08-05/raw/decisions.relay.2026-09-30.md`; their
plain paths resolve from repository root. The registry says `relay-00-research NOT opened`;
the seed says `SEED · session not opened`; and the decision file specifies the pending
REINVENT/ADOPT/REFUSE shape. The result set also includes X2 planning/review and unrelated
architecture/session documentation by textual reference; none has the required relay gate
identity and recorded recommendation.

These finite results returned references and planning/review records, including X2's
accepted plan/GO and X3's separate architecture materials. They did not identify a
`relay-00-research/` bed with a recorded REINVENT, ADOPT or REFUSE verdict. The fourth
cycle-01 query remains an informative historical pointer, not evidence of its claimed
exclusions; the cycle-02 filtered search is the current bounded result.

| Plausible-looking record | Identity/scope check | Disposition |
|---|---|---|
| `meshup/REGISTRY.md`, seam row | Explicitly says `relay-00-research NOT opened`; it is an index, not a verdict. | Evidence that the gate remains absent. |
| `meshup/seam.cross-vendor-relay.2026-08-05/raw/seed.relay-research.2026-09-30.md` | `status: SEED · session not opened`; it defines the required recorded verdict and the three checks. | The authoritative-looking seed is a pre-verdict contract, not a completed decision. |
| `meshup/seam.cross-vendor-relay.2026-08-05/raw/decisions.relay.2026-09-30.md` | D4 says the three parts are decided and the one-session mapping is proposed; it names `relay-00-research` → REINVENT/ADOPT/REFUSE. | Establishes the decision shape, not its result. |
| `.dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md` and catalogue references | These are vendor/source studies and a local `VERDICT` word match; neither claims relay-00 authority, all three gate checks, or an applicable release. | Sweep input only. |
| X2 plan, review and Majkee GO | Identities are the reviewed plan SHA `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`, P4 PASS, and X2 plan GO. Their stated scope is documentary D preparation. | They authorize this packet; they do not issue D4 or Q/C execution authority. |

This is bounded absence for the named roots and queries at 2026-10-22, not proof that no
verdict exists elsewhere. A future claimed verdict must be checked for its actual
`relay-00-research` identity, recorded recommendation, scope, authority and release effects
before it is accepted.

## Evidence disposition and recommendation

Existing evidence supports an **ADOPT recommendation for the narrow lab/source method**:
the dated tmux 3.7c/termios source finding supports a prospective output-only
`pipe-pane -O` question; the approved X2 plan specifies its independent post-termios oracle,
bounded workloads and retained failure cases; the lab registry/design establish Termpanum as
the observation lab with a PTY base. This adopts neither a shared event API, animal-level
consumer contract, source/lifetime owner, language/home/install decision nor a Zellij source
claim.

The following evidence exists but is not the D4 verdict:

- a prior-art/vendor-source sweep and hooks-versus-PTY materials under `.dev/research/`;
- the dated tmux/PTY/termios primary-source finding and corrected oracle in the X2 packet;
- relay seed, decisions and blind briefs that prescribe a wheel, overengineering and
  vendor-harness decision before dependent work;
- tracker and PTY directions that are explicitly downstream of the missing verdict.

The applicable `relay-00-research` verdict is absent from this scoped pass. Documentary D
does not issue it; no runtime test, fixture, source qualification, collector or product build
occurred here.

## Decision gaps for Majkee

1. Name or open the applicable relay decision path and record the D4 verdict with its
   REINVENT, ADOPT-with-delta or REFUSE recommendation and evidence scope.
2. If Q may run before that verdict, record a narrow exception that names its exact synthetic
   fixture effects; do not infer a C/product-build release from it.
3. Before C and later packages, choose the separate product-build authority plus local
   implementation/home/language/record-contract owner; later still, appoint any view/lifetime
   or operational-admission owner that those packages require.

## Exact proposed Q handoff

Relative to repository root `/home/hruzam/unikuklatrix/nablarva`,
`Q = .dev/session/termpanum-X1-source-fixture/`. It is an approved proposed base, not a
created directory or an execution release; every Q-owned subpath below is relative to it.

**Objective:** on office, qualify one tmux-3.7c prospective `pipe-pane -O` pane-output source
on a new private socket/server and isolated synthetic process. Compare pipe output to an
independently frozen PTY-master byte oracle after declared slave termios; compare rendered
state only to a separately frozen 80×24 screen oracle. Preserve provenance, coverage, gaps,
termios, sink/reader failures, quiet-alive versus exit, replay, staleness and identity reuse.

**Effects:** a separately assigned Q may create and use only its named private socket,
synthetic fixture, independent expected corpus, collector/compare artifacts and unique
retained run directories. It must not contact a living session, inject input, use a shared
transport, claim task semantics from text, build C/product code, or activate a VIST mapping.

**Release prerequisites:** (1) an applicable recorded L14 D4 verdict, or Majkee's explicit
recorded exception specifying exactly Q's executable effects; (2) a separate Q RUNBOOK and
paths/owners; (3) an independent oracle author and accepted frozen expected corpus/schedule
and hashes before collector work; (4) actual tmux binary/tag/hash, termios and fixture identity
recorded at run time; and (5) an explicit Q-only release of the experimental helper's language
and dependencies. The plan does not choose that language or dependency set; this packet does
not choose, install or authorize either. Q's release is not C's release.

Houston's five constraints remain intact: preparation differs from release; fixture execution
is separate; reports appoint no operational receiver; comparisons retain failures/unknowns;
and consequential homes, APIs, language, publication and integration remain with later
packages. The X2 post-review disposition also keeps producer/co-producer and
collector-lifetime ownership open, and gives C no animal-consumer compatibility requirement.

no execution release supplied by this packet.
