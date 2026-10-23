VERDICT: FAIL

TASK: Fresh independent acceptance of the frozen Termpanum X0 documentary packet against RUNBOOK items 1–6, approved X2 plan §6 and its eight acceptance mappings, Houston constraints, and cycle-03 POINT.

RAN: Recomputed both frozen SHA-256 identities; read the actual packet, approved plan/GO/source finding/Houston and X3 dispositions, project contracts, relay/lab/Termbrana sources, and local primary manuals; reran only the corrected document-filtered corpus/search expressions; checked path resolution, Q alias/base presence, whitespace, branch/HEAD, bed file set, and the RUNBOOK/STATUS gate and sole-pen witness.

EVIDENCE: The candidates retain their frozen hashes (`418570dbfb41b9161f0d87bd9190134f9c865745b003b13b304330d1963bef98`, `7b3db2b2caed7cba18ebd4104e374182f8777c56b71ca9a1012c31ee69fe00c8`). Local tmux is 3.7c and its installed manual directly supports the pane-PTY, `pipe-pane -O`/`-I`, and rendered `capture-pane` distinctions; local `pty(7)` and termios manuals support the directional/asynchronous and `OPOST`/`ONLCR` claims. The source contract copies the approved independent post-termios oracle, workloads and exact budgets, retains failures/unknowns, separates the struck hook rule from binding D4, scopes Termbrana, and labels runtime work planned. The disposition preserves bounded absence, ADOPT scope, three decision gaps, helper language/dependency release, and the exact no-release final line. Corrected search results remain 20/54/24 paths; the directory roots enumerate 590 Markdown files and root `PROJECT-DESIGN.md` is one additional scanned document. RUNBOOK and STATUS carry the identical approved gate, name `cartan-termpanum-x0` as owner/sole STATUS pen, and agree that cycle 03 is documentary review of the two frozen body paths. The BUS return follows `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` §RETURN's mandatory six-field contract.

FAILURES: (1) RUNBOOK item 1 and plan §6 “verify every cited path”: [source-contract.md](source-contract.md) lines 13–14 name `nablarva-X2-builder-narative/raw/...`; neither path resolves from repository root or document location. The actual sources start at `.dev/session/nablarva-X2-builder-narative/raw/...`. Their digests are correct, but their stated local identities are not usable paths. (2) RUNBOOK item 4 and plan §6 exact corpus requirement: [research-disposition.md](research-disposition.md) lines 13–16 say the eligible corpus including root `PROJECT-DESIGN.md` was enumerated as 590 Markdown paths, while line 24 enumerates only the four directory roots. The observed corpus is 590 directory-root files plus the separately scanned root file, hence 591 documents for the content searches. Search result counts themselves reproduce. (3) RUNBOOK item 5 and cycle-03 requirement for Q's owned paths/base: [source-contract.md](source-contract.md) lines 138–143 uses `Q/expected`, `Q/src`, and `Q/runs` without defining Q; [research-disposition.md](research-disposition.md) lines 92–111 also gives the “Exact proposed Q handoff” without its base. The approved plan defines `Q = .dev/session/termpanum-X1-source-fixture/`, but the decision-input packet omits that resolution.

REPRODUCE:

```sh
cd /home/hruzam/unikuklatrix/nablarva
sha256sum .dev/session/termpanum-X0-source-contract/raw/source-contract.md .dev/session/termpanum-X0-source-contract/raw/research-disposition.md
tmux -V
man -P cat tmux | col -b | sed -n '1350,1388p;1718,1740p'
man -P cat 7 pty | col -b | sed -n '6,27p'
man -P cat 3 termios | col -b | sed -n '108,118p'
set -o pipefail; rg --files --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' .dev/session .dev/research meshup docs | sort | wc -l
test -f PROJECT-DESIGN.md
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'relay-00-research' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u | wc -l
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'L14 D4|\bD4\b|research before (build|any RUNBOOK)' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u | wc -l
set -o pipefail; rg -l -i --hidden -g '*.md' -g '!**/.git/**' -g '!**/.hlm/**' -g '!**/vendor/**' -g '!**/*private*' -g '!**/*transcript*' -g '!**/*history*' -g '!**/*rollout*' -g '!**/*log*' -g '!**/*trace*' -g '!**/*secret*' -g '!**/*env*' -g '!**/termpanum-X0-source-contract/**' 'relay.*(verdict|disposition)|(?:verdict|disposition).*relay' .dev/session .dev/research meshup docs PROJECT-DESIGN.md | sort -u | wc -l
test -f nablarva-X2-builder-narative/raw/research.tmux-source-fidelity.2026-10-22.md; printf 'exit=%s\n' "$?"
test -f nablarva-X2-builder-narative/raw/termpanum.build-plan.md; printf 'exit=%s\n' "$?"
rg -n 'Q/|termpanum-X1-source-fixture|Q =|Q` =' .dev/session/termpanum-X0-source-contract/raw/source-contract.md .dev/session/termpanum-X0-source-contract/raw/research-disposition.md .dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md
rg -n '^(goal|gate|status_owner):|sole STATUS pen|^writer:|^checkpoint:|^in_flight:|^next:' .dev/session/termpanum-X0-source-contract/RUNBOOK.md .dev/session/termpanum-X0-source-contract/STATUS.md
if rg -n '[[:blank:]]+$' .dev/session/termpanum-X0-source-contract/raw/source-contract.md .dev/session/termpanum-X0-source-contract/raw/research-disposition.md; then exit 1; else printf 'no trailing whitespace\n'; fi
for p in .dev/session/termpanum-X0-source-contract/raw/source-contract.md .dev/session/termpanum-X0-source-contract/raw/research-disposition.md; do printf '%s ' "$p"; tail -c 1 "$p" | od -An -t x1; done
```

Expected salient results: hashes match POINT; `tmux 3.7c`; counts `590`, `20`, `54`, `24`; `PROJECT-DESIGN.md` exists; both shortened X2 paths return exit 1; only the approved plan defines Q's base; gate/owner witness agrees; no trailing whitespace and final byte `0a` in both candidates.

RESIDUAL RISK: No runtime, server, session, fixture, product, vendor, private-history, transport, external, or network check was performed. Exact upstream URL reachability was not rechecked; the installed tmux 3.7c and Linux manuals supplied the primary passage check. X0 remains absent from `pulse.md`, a known routing omission already declared in STATUS and outside this review pen.
