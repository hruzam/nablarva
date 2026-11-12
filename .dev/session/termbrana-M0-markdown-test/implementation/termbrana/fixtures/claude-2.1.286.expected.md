# Frozen expectation: Claude Code 2.1.286 synthetic source

This fixture is synthetic. It does not assert that every field or the `summary`
record occurs in a native Claude Code 2.1.286 transcript. The 2026-11-05 research
handoff observed retained JSONL records with `assistant`, `user`, `last-prompt`,
`mode`, `permission-mode`, and `queue-operation` types, and `sessionId` on relevant
records. It did not establish native branch, compaction, or stock pending-approval
schemas. Those fields are deliberately adversarial test input, not observed history.

```text
vendor=claude-code
vendor_version=2.1.286
session_id=claude-session-demo-01
```

## Canonical main-line exchanges

The main-line projection contains exactly four exchanges, in source order. The
duplicate user text remains distinct because the source UUID differs.

| Ordinal | Source UUID | Role | Timestamp | Required body |
| --- | --- | --- | --- | --- |
| 1 | `claude-user-001` | user | `2026-11-05T20:10:00.000Z` | `Show me the selected exchange.` |
| 2 | `claude-assistant-002` | assistant | `2026-11-05T20:10:03.000Z` | Full multiline content including its fenced `text` block and blank lines. |
| 3 | `claude-user-004` | user | `2026-11-05T20:11:00.000Z` | `Show me the selected exchange.` |
| 4 | `claude-assistant-005` | assistant | `2026-11-05T20:11:03.000Z` | `This duplicate-looking prompt has a different source UUID.` |

The literal code content of ordinal 2 is:

```text
line one
line two
```

## Required distinction and disclosure

- `claude-last-prompt-003` is a duplicate representation of `claude-user-001` by its
  explicit `sourceUuid`. It must not render as a second user exchange.
- `claude-summary-006` is an unsupported synthetic compaction marker. The renderer
  reports its source UUID and leaves compaction semantics explicitly unknown; it must
  not merge, delete, or rewrite the four canonical exchanges.
- `claude-user-007` is a synthetic alternate branch because its parent points to
  `claude-user-004`, not the main-line assistant. It must be separately disclosed and
  must not be silently mixed into the main line. Native branch reconstruction remains
  unqualified until an operator-approved isolated native session supplies evidence.
- `permission-mode` reports only the recorded mode. It is not an approval request,
  resolution, or proof that an approval is currently answerable. The approval outcome
  for this fixture is **unknown**.
- `claude-queue-009` is non-conversation metadata and must not become an exchange.

## Pin expectation

Pins for ordinal 1 and 3 must preserve their different source UUIDs despite identical
text. A pin for a synthetic branch item must include branch status or refuse main-line
resolution. Text similarity is never a fallback.
