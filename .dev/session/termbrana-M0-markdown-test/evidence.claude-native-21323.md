# Claude Code 2.1.323 native subset · 2026-11-13

Majkee created and explicitly identified a disposable Claude session, observed
the fictional prompt and reply, and reopened the session. Only that exact source
was inspected; unrelated sessions were not searched. Its complete records
identify Claude Code 2.1.323 and contain the two expected top-level text
exchanges. The first assistant message's parent ancestry passes through
attachment nodes. API request records also contain internal context and must
not be treated as additional conversation exchanges.

The separately selected `claude-jsonl-2.1.323` adapter implements a narrow
completed-text subset, validates session, project and producer version, and
discloses omitted types without rendering attachment or API payloads. It uses
strict single-chain ancestry and fails closed on competing ancestry, tools,
sidechains, compaction or unsupported structures. The test source parsed in
memory only as two exchanges, with `snapshot_only` and `full_history_claim:
false`; no real source was cached or copied during development.

Independent review initially found metadata flags and detached attachment
ancestry bypasses. They were fixed with invented regressions. The final review
passed all 70 tests and confirmed that the authorized source still parses in
memory; see `raw/verdict.claude-native-21323.md`. This is a narrow one-session
result, not proof of complete Claude history fidelity.

Snapshot publication retains the entire complete source prefix, including
internal records omitted from Markdown. A separate privacy review recommends
an owner-private host-local directory, `umask 077`, no symlinked cache root,
and private file and directory permissions; never copy raw source, maps or
reading files into repository evidence, ia-sync, shared storage or transport.
The current engine does not itself enforce those protections or exclude backups.

For the operator witness, Cartan rendered the exact authorized test source
with `umask 077` into `/tmp/nablarva-claude-view-5jo5eqmz/cache`, beneath an
owner-only temporary root. A recursive check found no symlinks and confirmed
owner-only modes and ownership. Two text exchanges were listed, and the first
user record was opened in Sublime at snapshot line 17. Majkee confirmed the
prompt and reply are visible; caret position was not separately confirmed.
This host-local cache contains the entire retained source,
including omitted internal request records; do not publish or transport it.
