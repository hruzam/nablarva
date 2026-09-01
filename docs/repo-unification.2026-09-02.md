# Repo unification — 2026-09-02

## What merged

Three repos collapsed into one: `nablarva` (this repo). History preserved for all.

- **nablarva** — now tracks its own harness and session state directly
  (`AGENTS.md`, `GEMINI.md`, `PROJECT.yaml`, `.dev/session/`, `registry.json`).
  Previously several of these paths were gitignored under the assumption that
  `nablarva.devenv` was the harness git-home.
- **nablarva.devenv** — harvested (`registry.json` machine-path map) and retired.
  Its `AGENTS.md` / `GEMINI.md` / `PROJECT.yaml` were byte-identical to the live
  nablarva copies (live had already won every sync), so nothing else carried
  over as content. `.hlm/` was inspected and deliberately NOT harvested — it is
  majkee's sealed, human-only vault (`cooking-recipes.yaml` states "NOTHING in
  this file leaves `.hlm/`"; `MAJKEE.md` is marked TOP SECRET / not wired to
  any LLM). It stays behind in the quarantined clone, not deleted, not moved
  into a repo that gets pushed to GitHub.
- **termbrana** — merged in as `toolbox/termbrana/` via `git subtree`, full
  history preserved and visible under that prefix.

## Why

This was a solo project (majkee, single operator). The three-repo split with
`sync.sh` / `deploy.sh` transport machinery between an "app repo" and a
"devenv harness repo" was a team-topology pattern: useful when multiple
humans or machines need independently-versioned harness vs. app history, not
useful when one operator maintains everything by hand. Precedent: `ia-sync`
retired its own `sync.sh` transport layer on 2026-07-31 for the same reason
(operator-driven, `git pull`/`push` sufficient, indirection was overhead
without a second consumer).

termbrana was pulled in as a toolbox member rather than kept as a fourth
independent repo for the same reason — it has no consumers outside nablarva
today, and a fourth clone-and-sync target added coordination cost with no
offsetting benefit. Its Law 2.3 "standalone first" survives as a **library**
boundary (termbrana-core stays free of nablarva/vendor concepts), not as a
repo boundary — see the addendum in
`toolbox/termbrana/research/termbrana.project-definition.md`.

## New discipline

**ONE repo. Plain git, no custom transport.**

- Cross-machine sync: `git pull --rebase` / `git push` on `core`. That's it.
- Parallel/experimental work: `git worktree add ../nablarva-<topic> -b dev/<topic>`
  instead of a second clone or a sibling repo.
- No sync/deploy shuttling between repos for this project going forward.

## Retired (archived, not deleted)

- `sync.sh`, `deploy.sh`, `SYNC_DISCIPLINE.md` (lived in `nablarva.devenv`)
- The `nablarva.devenv` and `termbrana` GitHub remotes — archived on GitHub,
  local clones quarantined to `/tmp/repo-merge-2026-09-02/` (not removed).

## Where things live now

- Harness + session state: this repo's own root / `.dev/session/`
  (previously devenv-only).
- termbrana: `toolbox/termbrana/` (was `~/unikuklatrix/termbrana/`).
- Machine path map: `registry.json` (was devenv-only).
