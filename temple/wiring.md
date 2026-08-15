# nablarva — temple & machine-layer wiring (snapshot 2026-08-08)

`what this is: a POINTER record of how nablarva is formally wired into the reposoma`
`temple + the machine (zsh) layer. Links + registry references only — no therapy, no`
`mail bodies, no design docs. Point, never copy. On any drift the source files win.`

`author: @Atlas · captured: 2026-08-08 · source-of-truth: the files pointed to below`

---

## 1. Temple layer (`~/reposoma`)

- **No index row.** nablarva is NOT listed in `registry/index.md`. It was never formally
  wired into the temple project table.
- **No temple beacon.** There is no `registry/nablarva.md`. The beacon lives with the
  project itself: `registry.nablarva.beacon.md` (this repo).
- **`larva.dev` sibling refs are NOT nablarva.** The `sibling of larva` lines in
  `registry/reposoma.devenv.md` + `registry/piql.dev.md`, and the `larva / kukla` section
  in `temple/legacy-wall.md`, all point to the **original `larva.dev` orchestrating
  system** (the predecessor temple, 2026-04→05). Different entity — left intact, not
  nablarva's wiring.

Net: nablarva carries essentially **no temple-registry wiring**. Its formal presence is in
the machine layer below.

## 2. Machine (zsh) layer — the real wiring

> **Deploy discipline (esp. here):** zsh is authored on the surgical table
> `~/ia-sync/zsh/` and spread to the live `~/.config/zsh/` by `deploy.sh`. The live copy is
> a deployment, NOT the source. Any change goes to `~/ia-sync/zsh/…` then `deploy.sh` —
> never edit the live copy. Paths below name the live location for orientation; the
> authoritative source is the matching `~/ia-sync/zsh/…` path.

**Scope folder** (`ai/`-pattern, own scope — NOT the `projects/` toolkit mechanism):
- `~/.config/zsh/nablarva/base.zsh` — the scope signpost. Founded 2026-08-02.
  "nabLarva — larva V3 (project flag L1–L10)." Docs-only phase until gavel docket item 2.
- `~/.config/zsh/nablarva/keyboard.zsh` — control panel (aliases only, `nab-*`).
- `~/.config/zsh/nablarva/nablarva.zsh` — the nab engine (project verbs: cd, status,
  harness, devenv transport).

**Wire-in points** (`~/.config/zsh/config.zsh`):
- `config.zsh:93-95` — env block:
  - `PROJECT_NAB_PATH="$HOME/unikuklatrix/nablarva"`
  - `PROJECT_NAB_NAME="nabLarva"`
  - `PROJECT_NAB_DEVENV="$HOME/unikuklatrix/nablarva.devenv"`
- `config.zsh:153` — the source hook (the scope "index" line):
  `[[ -f ~/.config/zsh/nablarva/base.zsh ]] && source ~/.config/zsh/nablarva/base.zsh`
  (sits next to the `ai/base.zsh` hook).

**Doc-comment pointer** (not wiring, just a reference):
- `system/base.zsh:26` — `# Retrofit 2026-08-05 (WP5) — reference: nablarva/base.zsh.`

---

*Snapshot only. The `~/ia-sync/zsh/nablarva/` source + `config.zsh` hooks are live and
stay wired — nothing here was unwired.*
