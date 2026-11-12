"""Synthetic Claude Code 2.1.286 fixture adapter.

The native transcript schema is not qualified. This module only parses explicitly
supplied bytes matching the frozen synthetic fixture and keeps unknown semantics visible.
"""

import json


class SourceError(ValueError):
    pass


def _body(record):
    message = record.get("message")
    if not isinstance(message, dict):
        raise SourceError(f"missing message object: {record.get('uuid', 'no-uuid')}")
    content = message.get("content")
    if isinstance(content, str):
        return content, []
    if isinstance(content, list):
        texts = [part.get("text") for part in content if isinstance(part, dict) and part.get("type") == "text"]
        omitted = [part.get("type", "object_without_type") if isinstance(part, dict) else "non_object" for part in content if not isinstance(part, dict) or part.get("type") != "text"]
        if texts and all(isinstance(text, str) for text in texts):
            return "\n".join(texts), omitted
    raise SourceError(f"unsupported message content: {record.get('uuid', 'no-uuid')}")


def parse(data: bytes) -> dict:
    """Return main-line exchanges and explicit disclosures for synthetic fixture bytes."""
    exchanges, disclosures = [], []
    session_id = None
    last_uuid = None
    seen = set()
    for line_number, raw_line in enumerate(data.splitlines(keepends=True), 1):
        if not raw_line.endswith(b"\n"):
            disclosures.append({"kind": "incomplete_final_line", "line": line_number})
            break
        try:
            record = json.loads(raw_line)
        except UnicodeDecodeError as exc:
            raise SourceError(f"invalid UTF-8 in complete JSONL record at line {line_number}") from exc
        except json.JSONDecodeError as exc:
            raise SourceError(f"malformed complete JSONL record at line {line_number}: {exc.msg}") from exc
        if not isinstance(record, dict):
            raise SourceError(f"non-object record at line {line_number}")
        current_session = record.get("sessionId")
        if not isinstance(current_session, str) or not current_session:
            raise SourceError(f"missing session identity at line {line_number}")
        if session_id is None:
            session_id = current_session
        elif session_id != current_session:
            raise SourceError("source mixes session identities")
        kind, uuid = record.get("type"), record.get("uuid")
        if isinstance(uuid, str):
            if uuid in seen:
                raise SourceError(f"duplicate source UUID at line {line_number}: {uuid}")
            seen.add(uuid)
        if kind == "last-prompt":
            source_uuid = record.get("sourceUuid")
            disclosures.append({"kind": "duplicate_representation", "uuid": uuid, "source_uuid": source_uuid})
            continue
        if kind == "permission-mode":
            disclosures.append({"kind": "permission_mode", "mode": record.get("permissionMode"), "approval_outcome": "unknown"})
            continue
        if kind not in {"user", "assistant"}:
            disclosures.append({"kind": "unsupported", "type": kind, "uuid": uuid, "semantics": "unknown"})
            continue
        if not isinstance(uuid, str) or not uuid:
            raise SourceError(f"missing exchange UUID at line {line_number}")
        parent = record.get("parentUuid")
        if not exchanges:
            main_line = parent is None
        else:
            main_line = parent == last_uuid
        body, omitted = _body(record)
        exchange = {"uuid": uuid, "role": kind, "timestamp": record.get("timestamp"), "body": body, "omitted_content": omitted}
        if not main_line:
            disclosures.append({"kind": "alternate_branch", "uuid": uuid, "parent_uuid": parent, "main_line_resolution": "refused"})
            continue
        exchanges.append(exchange)
        last_uuid = uuid
    if session_id is None or not exchanges:
        raise SourceError("source contains no canonical exchanges")
    return {"vendor": "claude-code", "vendor_version": "2.1.286", "session_id": session_id, "exchanges": exchanges, "disclosures": disclosures, "native_schema": "unqualified"}
