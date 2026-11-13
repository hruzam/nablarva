# Frozen invented Claude 2.1.323 subset expectations

This fixture was invented before implementing the native parser. It contains no
copied native record content or identities.

- Two visible exchanges, in order: `fictional-user-1`, then `fictional-assistant-1`.
- The assistant's ancestry passes through both attachment nodes to the user.
- The user body is exactly `Please show the selected exchange.`
- The assistant preserves its newline and fenced code boundaries.
- The nested API request representation is omitted and never becomes a message.
- Metadata, attachments and the last-prompt representation are disclosed by type;
  their internal content is not rendered.
- Producer and native adapter contract are explicitly `2.1.323`; native history
  is snapshot-only and complete-history fidelity remains unqualified.
- Missing/cyclic ancestry, duplicate UUIDs, competing branches, sidechains,
  mismatched identity/version, compaction and tool messages fail closed.
- An incomplete final JSONL record is deferred, including incomplete UTF-8;
  malformed complete records produce a redacted line-specific error.
