# Frozen invented Codex 0.167 completed-item expectations

These are invented identities and text, frozen before parser implementation.
Source contract: rust-v0.167.0 `protocol/src/protocol.rs` ItemCompletedEvent,
`protocol/src/items.rs` TurnItem, UserMessageItem and AgentMessageItem, and
`protocol/src/user_input.rs` UserInput. No native session content is copied here.

- Explicit input format: `codex-rollout-0.167`; metadata producer `0.167.0`.
- Render three exchanges, in order: user `Repeat this prompt.`, assistant
  `First line.\n\n```python\nprint('fixture')\n````, user `Repeat this prompt.`.
- Native item IDs `u-one`, `a-one`, `u-two` remain distinct provenance; bookmarks
  remain snapshot-bound rollout positions and require validated prefix continuity.
- Ignore response-item and legacy-event alternate representations with disclosures.
- An identical repeated completed item ID renders once and is disclosed; changed
  content under the same item ID is rejected. Do not deduplicate by message text.
- Image input is disclosed as omitted content. A completed compaction blocks
  carry-forward; unsupported tool items stay disclosed rather than rendered.
- An incomplete final record is deferred. Wrong/missing producer version, wrong
  event thread, malformed text, missing item identity and missing turn are errors.
- This fixture proves only the explicit text subset, not complete native fidelity.
