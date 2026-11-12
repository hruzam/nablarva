# Frozen expectation: Codex CLI 0.166.0 synthetic source

This expectation is authored before renderer implementation. It applies only to
`codex-0.166.synthetic.jsonl`, whose explicit source identity is:

```text
vendor=codex
vendor_version=0.166.0
thread_id=thread-demo-01
session_id=session-demo-01
branch_id=branch-main
```

## Canonical exchanges

The projection contains exactly these four exchanges in source order. Source record
IDs are identity; the two identical user texts remain distinct exchanges.

| Ordinal | Source record | Role | Timestamp | Required body |
| --- | --- | --- | --- | --- |
| 1 | `item-user-001` | user | `2026-11-05T20:00:00Z` | `Please show the selected exchange.` |
| 2 | `item-assistant-002` | assistant | `2026-11-05T20:00:02Z` | The full multiline body, including one blank line before and after the fenced Python block. |
| 3 | `item-user-003` | user | `2026-11-05T20:01:00Z` | `Please show the selected exchange.` |
| 4 | `item-assistant-004` | assistant | `2026-11-05T20:01:03Z` | `The second matching prompt is a distinct source record.` |

The fenced content in exchange 2 is literal presentation content:

```python
print('hello')
```

## Required omissions and diagnostics

- `item-tool-005` is a non-conversation representation. It does not become a fifth
  exchange or duplicate an assistant message. The renderer may disclose it as an
  omitted representation.
- `item-unknown-006` is a complete, unsupported vendor record. The renderer reports
  it by its exact source ID and type `future_vendor_event`; it does not invent text.
- The trailing `item-partial-007` has no valid closing JSON object. The renderer defers
  it, records the last complete boundary after `item-unknown-006`, and does not emit an
  error that changes the first four exchanges.

## Pin expectation

A pin for ordinal 1 and a pin for ordinal 3 must differ at least by source record
identity (`item-user-001` versus `item-user-003`), even though their roles and message
text match. Neither pin may be resolved by text similarity.
