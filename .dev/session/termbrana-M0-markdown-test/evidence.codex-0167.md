# Codex 0.167 native-format observation

On 2026-11-07, home reported `codex-cli 0.167.0`; the earlier 0.166.0
observations remain historical. A separately created test session in
`/tmp/nablarva-observer-native-5ZKQ4Q` contained only deliberately fictional
conversation prompts. Cartan observed replies in its terminal and later closed
it. Only its exact, explicitly selected rollout was inspected; no other native
history was searched. Private rollout content and identities are not reproduced
here.

The scoped rollout's metadata identified producer version 0.167.0 and
paginated history. The observed three user and three assistant items appeared
as `event_msg` / `item_completed` records; this sample had no `user_message` or
`agent_message` events. The existing 0.166 source-derived parser returned
`source contains no supported conversation events` on that sample. This is a
specific observed compatibility gap, not a complete schema survey.

The researcher compared tagged public sources: the rollout and history payload
files inspected were unchanged between 0.166 and 0.167, while the protocol file
changed in areas including audio and approval behavior. This comparison does
not establish universal version compatibility. Source pointers: [0.166 protocol](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/protocol/src/protocol.rs)
and [0.167 protocol](https://raw.githubusercontent.com/openai/codex/rust-v0.167.0/codex-rs/protocol/src/protocol.rs).

This separate test session is not the operator's possibly in-flight PAD step 17
session, does not establish visual rendering or native approval answerability,
and does not justify reading any other native histories. Parser changes and
qualification evidence must be independently verified before a native PASS.

The experimental adapter now exposes a separate `codex-rollout-0.167` format
with producer-version validation. The invented fixture and tests cover its
bounded completed-text subset. The sole test rollout parsed into six distinct
items without reproducing its content here. The full 57-test suite passed;
`raw/verdict.codex-0167-refresh.md` records the independent recheck. This is
one-session subset evidence, not a claim of complete native history fidelity.

For PAD STEP 17, Majkee created a separate test session and supplied its
directory and thread ID. Exact metadata lookup matched both to one rollout,
whose 0.167 parser result contained two distinct exchanges: the expected
fictional user prompt and assistant reply. The result reported a complete
source and disclosed unsupported or potentially duplicate representations.
Only that explicit rollout was read. The session was rendered to the private
temporary cache `/tmp/nablarva-native-view-mf7s3v06/cache`; `_tbv_open` then
reported its first user record at snapshot line 21. At that point the operator's
Sublime observation and live-session independence check were still pending.

Subsequently, Majkee witnessed the first prompt and reply in Sublime, then
confirmed that a newer snapshot contained a second exchange while the earlier
snapshot stayed unchanged. An explicitly started bounded watcher recorded
new-record and new-snapshot availability after a third exchange while the
selected snapshot stayed fixed. An explicit refresh carried the second-user
bookmark to the newer six-exchange snapshot; Majkee confirmed the third test
appeared there. The cache used an explicit output override, with no separate
layout-mode reading file. After Cartan stopped only the verified watcher and
Majkee closed the Sublime test windows, Majkee reported another native reply;
the exact authorized test rollout contained that fictional prompt and reply.
This is a bounded native-session independence witness, not complete native
history, approval, branch or compaction qualification.
