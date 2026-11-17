---
what: Houston consult return — source home for SublimeObserver
landed-by: oraculum · claude (head) — Houston's consult card writes no file; this is its reply saved word for word
date: 2026-11-15
state: consult return — advice, not a decision; majkee's word on the folder is still owed
---

Route: spawned by a parent agent → child; otherwise main session (canary: cl-e1a94c37).
/home/hruzam/.germline/agents/houston/identity.md · stamp: 3702b18f
/home/hruzam/.germline/agents/houston/binding.claude.md · stamp: 6181ad36
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/consult.md · stamp: 5435b1c7

Route: child · card: consult · addendum: nablarva (found by walking up from the project path you named, not from my cwd `~/ia-sync`).

**out of card: writing `raw/houston.consult-source-home.2026-11-15.md`.** I wrote nothing. Under consult I write no file, on any route, even when given an exact path (consult card, "What I do not do"; binding, "Consult writes no file on any route"). The head saves this reply word for word as a new file in its bed. STATUS `recovery_probe` and `expected:` look for that file, so the head has to write it or the probe will report "consult not returned". The STATUS `in_flight` line "houston … writes raw/houston.consult-source-home…" should say "the head lands".

---

# Houston · consult · source home for SublimeObserver · 2026-11-15

**Verdict: stretches** (no break)

## Constraints (at most five)

1. **The parent folder is majkee's word for this one body.** L18 leaves "the parent directory for new folders" OPEN, so `toolbox/sublime-observer/` is not settled by any lock. Record his word as `said: majkee` in the RUNBOOK's Fixed facts and scope it to this body. The README must say the line is still unattached: being in `toolbox/` does not make it an organ or a toolbox. Whether to add a flag line stays majkee's choice at closure (directive §10 item 5).
2. **One source, and an isolated payload.** Once the source is in `toolbox/sublime-observer/`, the bed's `implementation/` stops being a source. It keeps only evidence. The head changes prompt-1's build scope to the new path. The payload subfolder is exactly what install copies. Tests, the reader, the fakes and the trial fixture stay outside it.
3. **Durable text cites the bed only by commit pin** (`nablarva@<sha>:.dev/session/sublime-observer-X1-file-publish/…`). Decision notes cite the RUNBOOK or a flag line (L19). Do not write: "installed", "organ", "Sublime is the editor", VIST producer or shared layer (directive §8; L20, L21).
4. **Delivery is a reviewed `install-pkgs` task.** It sets `src-root:` to the nablarva tree, `hosts: home`, and `automation: manual` until qualified. It copies only the payload into `Packages/SublimeObserver/` and documents a removal. Nothing auto-deploys from nablarva (L6; L8′ sends publication through ia-sync). No public package name claim, such as Package Control (flag "Out of scope": no public namespace before clearance).
5. **The general "installable toolbox module" is not X1 work.** X1 delivers the first instance only. The general package definition sits on the build · install · publication seam, where the owner is `unknown:` and "package shape; one vs several" is open (ARCHITECTURE §4 row, §4.7). Any shared installer mechanism also needs its own release (L21). That belongs to a later sibling or the architecture line.

## 1. Where the source and tests live

**Recommended path: `/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer/`**. Majkee's word settles it (L18 leaves the parent open), and he has said only "might be" so far.

```
toolbox/sublime-observer/
  README.md          thin entry (L18)
  SublimeObserver/   payload: publisher.py, contract.py, .python-version,
                     .sublime-settings, .sublime-commands. Copied as-is to Packages/SublimeObserver/
  tests/             test_*.py, fakes.py, reader.py, disposable_trial.py, trial_fixture/
```

Evidence:
- `toolbox/` exists and holds one body, `toolbox/termbrana/` (README, DECISIONS, Cargo, crates, research). Read by glob of `toolbox/*/*`.
- The only other planned body with a proposed home already uses this parent: termpanum, proposed at `toolbox/termpanum/` but not created (`PROJECT-DESIGN.md` §3.6; `docs/ARCHITECTURE.md` §7).
- `docs/organs/` holds organ bodies as documents. This line is not an organ and its body is code, so it does not fit there (ARCHITECTURE §7; ledger `attach: none yet`).
- A new top-level parent would add a second open precedent. Inferred (houston).
- The name was swept and accepted; `sublime-observer` appears only in the X0 bed and the shared guide (ledger, Solved).

Why a separate payload subfolder (inferred, houston): Sublime takes the package name from its folder and loads top-level `.py` files as plugins. If the body root were the package, a copy-install would carry tests and fixtures into the live profile. I did not test this Sublime behaviour.

## 2. Self-contained, and when it can be called an installable module

The placement keeps majkee's aim open.

**"Self-contained" in nablarva's terms** means the folder is defined by its own README (L18: "thin README.md is the entry; chapters … only on need"). The README carries:
- a provenance header: name · status · schema · source · trust note (`PROJECT.yaml` comment, lines 20–22; a said rule, not a lock);
- what it does and what it never does: observation only, no notify, no control, no `subl file:line` (L17, L20);
- file contract v1, or a pointer to a `CONTRACT.md` chapter if the README outgrows one page;
- the one home of the publish path, which is plugin settings (directive §4.4);
- the trust boundary: same-user readable, the vault and `.env` refusal (L22);
- the stdlib test command and Python host notes;
- the install and removal pointer: the ia-sync task, by absolute path;
- limits and unverified items;
- provenance pins to the X1 bed.

Add `DECISIONS.md` only if product-technical rationale piles up (L19, the termbrana L11 pattern).

**What must be true before "installable module":**
- the payload is isolated (constraint 2);
- it is versioned in two places: `contract_version` in code and `version:` in the install task (install-pkgs README, STEP B);
- the install-pkgs task is reviewed by majkee, its `check` block gates on the Sublime build and plugin host, and removal has been demonstrated;
- majkee has recorded GO on the X1 gate (RUNBOOK gate);
- it is home only. Office and monitor are later siblings (RUNBOOK, "does not do").

**Belongs to a later sibling, not X1:**
- a general definition of a toolbox package or "app-like" module;
- any shared installer from nablarva;
- registry publication.

These sit on ARCHITECTURE §4.7, which is open, under L21.

## 3. Navigation for the writer (routing only)

| file | what it gains (one or two lines) | owner | when |
|---|---|---|---|
| `toolbox/sublime-observer/` + `SublimeObserver/` + `tests/` (new) | copy of the bed's `implementation/SublimeObserver/` and `implementation/tests/`. Evidence stays in the bed | X1 head directs; implementer (trajectory or delta) copies | **now**, after majkee's word on the folder (STATUS hold) |
| `toolbox/sublime-observer/README.md` (new) | thin entry: the §2 list, a skeleton now. "Line sublime-observer, unattached." | X1 head; writer Delta | skeleton **now**; contract refinements **at closure** (RUNBOOK Fixed facts) |
| X1 `RUNBOOK.md` | Fixed facts: majkee's placement word. prompt-1 build scope: the new path. Known constraint: one source, payload isolated | head (Oraculum) | **now** |
| X1 `STATUS.md` | checkpoint and holds: the source home moved, the bed implementation is evidence only | head | **now** |
| `~/ia-sync/install-pkgs/<slug>.md` (new) + a "Current tasks" entry in `install-pkgs/README.md` | `hosts: home` · `automation: manual` · `src-root: ~/unikuklatrix/nablarva/toolbox/sublime-observer` · copy only the payload · removal steps | ia-sync seat under SYNC_DISCIPLINE; majkee reviews | **install phase**, before the normal-profile witness |
| `~/ia-sync/journal.host-cleanup.md` | home: SublimeObserver installed by task `<slug>` vN, plus the removal check | ia-sync seat | install phase |
| `PROJECT-DESIGN.md` | the "one small line": a non-organ line pointing to `toolbox/sublime-observer/README.md`, marked unattached | majkee's hand, or a supplied-decision mechanics diff from the audit-card keeper that majkee commits | **closure** |
| `docs/ARCHITECTURE.md` | §4 observe row, planned cell: "planned producer: sublime-observer (owner stays `unknown:`)". Optionally §7 "cited only" | through majkee, coordinated with `architecture-X1-bookkeeping` | **closure only** |
| `~/reposoma/raw.guides/sublime-observer/GUIDE.md` | drop the socket CLI; point to the toolbox README | guide owner, through the head | closure (ledger) |
| `~/ia-sync/codex/AGENTS.md` | conditional pointer for Codex seats | Cartan, by mail | closure |
| `sublime-observer-X.ledger.md` | the source-home pointer; attach still none | head | session close only |
| `flag.md` | nothing now. At closure majkee decides whether a line records the parent choice | head carries it to the docket after majkee's GO | closure, if at all |
| no change | `PROJECT.yaml` (no `tools:` key earned), `pulse.md` (router fields only), the X0 bed and its STATUS, `registry.nablarva.beacon.md` (parked) | — | — |

## 4. Locks touched, and drift since the first consult

- **L18:** a parent choice inside an open clause. It does not break the lock, but it sets a precedent (constraint 1).
- **L6, L8′:** satisfied only if delivery is manual and reviewed. This would be the first install-pkgs task that uses nablarva as `src-root`; every existing one points at applications-in-common (read in `install-pkgs/*.md`).
- **L22:** the copy and install steps read no vault. **L19:** rationale lives in the component's own records.
- **Drift: RUNBOOK and directive §8 say "organ README"** while the line is unattached. Use "component README" (the L18 term), so the wording does not suggest attachment. Head's pen.
- **Drift: prompt-1 limits building to the bed's `implementation/`.** Unless the head amends it, any build after the move leaves two sources.
- **Drift: the ledger line for X1 reads "OPEN, parked, nothing built"**, while STATUS shows steps 1 and 2 verified. The ledger updates only at open and close and says STATUS wins, so this is expected staleness, not a fault.
- **Drift: STATUS says this consult writes its own file.** See the out-of-card note at the top.
- Outside this move: the "Current tasks" list in `install-pkgs/README.md` does not list `zellij`, `tmux`, `monitor-ssh` or `harden-host`, which are on disk. Not for X1 to fix.
- I found nothing that contradicts the first consult's five constraints. I saw them only as relayed in directive §4, not my own earlier text.

## Read

All files I read are under `/home/hruzam/unikuklatrix/nablarva/` unless the path is absolute:
- the X1 bed: `RUNBOOK.md`, `STATUS.md`, `raw/oraculum-claude.directive.2026-11-15.md`, and a glob of `implementation/`
- `.dev/session/sublime-observer-X.ledger.md`
- `.dev/session/flag.md`: L6, L8′, L11, L12 (partial), L17–L24, Out of scope, Archived index
- `AGENTS.md`, `PROJECT.yaml`, `PROJECT-DESIGN.md`, `README.md`, `registry.nablarva.beacon.md`
- `docs/ARCHITECTURE.md` §4 table, §4.2–4.8, §7
- `toolbox/termbrana/README.md` (head)
- globs of `toolbox/` and `docs/`; a grep of `.dev/session/pulse.md`
- `/home/hruzam/ia-sync/install-pkgs/README.md` and a header grep of the task files
- the existence of `/home/hruzam/reposoma/raw.guides/sublime-observer/GUIDE.md` (not its content)

I read nothing under `.majkee/` or `.hlm/`.

## Not verified

- the Sublime package loading behaviour (inferred);
- whether the publisher's imports survive the subfolder layout and running tests from `tests/` (that check is for the implementer and assay);
- the content of the shared guide and of `pulse.md` beyond the lines that matched;
- my first consult's original text.

No helper was spawned.
