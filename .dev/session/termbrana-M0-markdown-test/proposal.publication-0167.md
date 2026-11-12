# Refreshed transcript publication candidate — review only

This review candidate was prepared under `/tmp/termbrana-publication-xqxu1cfh`; its patch, manifest and check summary are retained alongside this document.
It changes no ia-sync source, host configuration, deployed file, Git index or
worktree registration. `proposal.manifest-0167.json` records baseline and candidate hashes;
`proposal.source-wiring-0167.patch` uses relative `a/zsh/termbrana/` and
`b/zsh/termbrana/` paths. `candidate/` is the source-only proposed family,
`baseline/` the exact inspected family, and `applied/` the patch reconstruction.

The 26-file delta adds five runtime files (`transcript.py`, `codex_native.py`,
`claude_adapter.py`, `collector.py`, `transcript.zsh`), ten invented fixture and
expectation files under `fixtures/`, and eight isolated test modules under
`transcript-tests/`. Existing `base.zsh` gains one engine source;
`keyboard.zsh` gains eight aliases and comments; README gains a conservative
transcript section. Composer source, grammar, tests and aliases are preserved.
No connector plugin or GUI test dependency is included.

The separate transcript test directory preserves the tests' source-relative
runtime and fixture resolution without mixing them into composer acceptance.
Runtime, fixtures and test bytes match the current experimental source; the
manifest lists each origin. Candidate source changed during staging is treated
as a failure, rather than silently mixing revisions.

Qualification is limited: synthetic Codex and Claude fixtures pass; explicit
Codex 0.166/0.167 text subsets are separately labeled, and only one authorized
0.167 capture has received a parser check. Full native-history reconstruction,
Claude native fidelity, live approvals, visual usability and cross-host parity
remain unqualified. The selected-reading repair guarantee is recovery, not
multi-file atomicity. Immutable snapshots can be the last source behind bookmarks.

Verification performed in this temporary family:

- `git apply --check proposal.source-wiring.patch` and actual temporary apply
  passed; all reconstructed files match candidate bytes, including deliberately
  unterminated fixture tails.
- `python3 -I -S -B -m unittest discover -s tests -v`: 27 composer tests passed.
- `python3 -I -S -B -m unittest discover -s transcript-tests -v`: 57 transcript
  tests passed.
- `zsh -n` passed for base, keyboard, composer and transcript engines.
- Repeated source was silent, preserved both alias families and started none of
  the guarded Python/editor/session commands. Keyboard contains aliases/comments only.
- Python AST parsing and final current-source hash comparison passed.

`proposal.checks-0167.json` records exact commands and exits; corresponding logs are retained.
A naming sweep of the existing ia-sync zsh source found no `tbv-*` or `_tbv_*`
entry-point collisions before the candidate was overlaid. Baseline family hashes
still match the inspected ia-sync source.

Permanent transcript processor placement under L8/L8′/L17 remains conditional.
Independent functional review and a fresh Houston consult on this exact delta
are still required. A GO on the experiment is not publication or activation.
No deploy command, including deploy dry-run, was run here. Once separately
released, review the actual source delta and each target host's complete deploy
dry-run; the publisher affects more than this family and is not a scoped installer.
Home and office startup activation need separate owner review and fresh-shell
checks. Shell source starts no collector automatically.

For rollback after a separately approved publication, retain the previous source
revision and host-wiring records, revert only the reviewed added files/wiring,
review a new dry-run and verify a fresh shell. Do not remove snapshots or native
histories, and do not roll back the unrelated Sublime installation.
