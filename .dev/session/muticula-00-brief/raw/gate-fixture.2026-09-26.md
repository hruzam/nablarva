---
what: scratch fixture for the Leg 2 gate commands (master r2, D4)
ran: 2026-09-26 · office (hruzam-120922) · git 2.55.0 · @Trajectory, Claude session · throwaway repo under the session scratchpad, deleted after
retained_because: Cartan (consolidated CHALLENGE) — the earlier gate fixture was not a retained run artifact
---

# Gate fixture — explicit --only, literal NUL-framed paths, empty selection

Neighbour state in every case: `a` staged, `notes.md` modified but unstaged. Mine: a tracked file
literally named `*.md`, tracked `b`, new file `c d` (space in the name).

```sh
d=$(mktemp -d) && cd "$d" && git init -q . && git config user.email t@t && git config user.name t
printf 'a0\n'>a; printf 'n0\n'>notes.md; printf 's0\n'>'*.md'; printf 'b0\n'>b
git add -A && git commit -qm base
printf 'a1\n'>a && git add a                                  # neighbour: staged
printf 'n1\n'>notes.md                                        # neighbour: unstaged
printf 's1\n'>'*.md'; printf 'b1\n'>b; printf 'c1\n'>'c d'    # mine

# T1 — the r2 gate
printf '%s\0' 'c d' | git --literal-pathspecs add --pathspec-from-file=- --pathspec-file-nul
printf '%s\0' '*.md' b 'c d' | git --literal-pathspecs commit -q --only -m t1 --pathspec-from-file=- --pathspec-file-nul
# T2 — same list, no --literal-pathspecs          (state reset between tests)
# T3 — empty list, with --only:     git --literal-pathspecs commit --only -m t3 --pathspec-from-file=/dev/null --pathspec-file-nul
# T4 — empty list, without --only:  git commit -m t4 --pathspec-from-file=/dev/null --pathspec-file-nul
```

| test | result | committed |
|---|---|---|
| T1 gate: `--only` + literal + NUL | rc 0 · `a` still staged · `notes.md` still dirty | `*.md`, `b`, `c d` |
| T2 without `--literal-pathspecs` | rc 0 — `*.md` acted as a wildcard | `*.md`, `b`, **`notes.md`** (neighbour's unstaged bytes) |
| T3 empty list, `--only` | rc 128 `fatal: No paths with --include/--only does not make sense.` | nothing |
| T4 empty list, no `--only` | rc 0 | **`a`** (neighbour's staged bytes) |

Scope: path selection only. Not covered: hooks during commit, other Git clients holding
`index.lock`, filenames with newlines, post-commit verification (r2 Leg 2 steps 5 and [OPEN] hooks).
