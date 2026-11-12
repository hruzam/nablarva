# Codex 0.166.0 source-derived fixture — expected adapter result

This fixture is synthetic; it is shaped only from public source at tag
`rust-v0.166.0`. It is not a qualification of any host's native history.

## Identity

- `thread_id` and `session_id` are both `11111111-1111-4111-8111-111111111111`.
- `history_mode` is `paginated`; each complete record therefore has its native
  rollout ordinal, but that pin is snapshot-bound. Carrying it forward requires
  validated capture continuity because revert can use another rollout for the
  same stable thread ID.
- The adapter does not invent `branch_id`. A fork is represented by native
  `forked_from_id` and `history_base`, when present.

## Render-eligible exchanges

1. `user` — `Summarize this fixture.` — pin
   `snapshot:thread:11111111-1111-4111-8111-111111111111:ordinal:1`.
2. `assistant` — `It is a public-source-derived synthetic rollout.` — pin
   `snapshot:thread:11111111-1111-4111-8111-111111111111:ordinal:2`.

## Mandatory disclosures

- The `response_item` at ordinal 3 is a potential duplicate representation. It
  is not rendered because its relationship to `event_msg` is not provable from
  this source snapshot.
- The `context_compacted` event at ordinal 4 is disclosed, not reconstructed.
- The `token_count` event at ordinal 5 is unsupported presentation data.

An unterminated final JSONL line is separately tested and deferred rather than
parsed; it is not included in this otherwise-valid frozen fixture.

## Public-source basis

- The tagged rollout decoder reads `timestamp`, optional `ordinal`, and a
  flattened item envelope: <https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/rollout/src/lib.rs>.
- The wire enum uses `type` plus `payload`: <https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/history/src/rollout_payload.rs>.
- `SessionMeta` defines session/thread lineage and history fields, while
  `AgentMessageEvent` / `UserMessageEvent` define `message`:
  <https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/protocol/src/protocol.rs>.
