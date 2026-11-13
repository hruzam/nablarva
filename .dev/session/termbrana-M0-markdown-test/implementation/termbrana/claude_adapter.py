"""Claude synthetic fixtures and explicit 2.1.323 native text subset.

The native transcript schema is internal and version-specific. Neither parser
claims complete native-history fidelity; callers must select the native subset.
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


NATIVE_VERSION = "2.1.323"
_NATIVE_METADATA = {
    "mode", "permission-mode", "session-owner", "atis-latch", "file-history-snapshot",
    "api-request-shape", "api-request-blob", "api-request", "last-prompt", "ai-title", "cost-state",
}
_NATIVE_ATTACHMENTS = {
    "environment", "model", "deferred_tools_delta", "agent_listing_delta",
    "mcp_instructions_delta", "skill_listing", "auto_mode", "instructions",
    "session_context", "date", "credential_org", "remote_session_change", "prompt_snapshot",
}


def parse_native(data: bytes) -> dict:
    """Read the explicitly observed 2.1.323 main-line completed-text subset.

    Nested API representations and attachment payloads are never message sources.
    This is an internal, version-specific format, not a complete-history reader.
    """
    exchanges, disclosures, nodes, omitted = [], [], {}, {}
    session_id = cwd = None
    last_node = None
    complete_bytes = 0
    deferred_partial = False
    for line_number, raw_line in enumerate(data.splitlines(keepends=True), 1):
        if not raw_line.endswith(b"\n"):
            deferred_partial = True
            disclosures.append({"kind": "incomplete_final_line", "line": line_number})
            break
        offset = complete_bytes
        complete_bytes += len(raw_line)
        try:
            record = json.loads(raw_line)
        except UnicodeDecodeError as exc:
            raise SourceError(f"invalid UTF-8 in complete JSONL record at line {line_number}") from exc
        except json.JSONDecodeError as exc:
            raise SourceError(f"malformed complete JSONL record at line {line_number}: {exc.msg}") from exc
        if not isinstance(record, dict):
            raise SourceError(f"non-object record at line {line_number}")
        kind = record.get("type")
        current_session = record.get("sessionId")
        if current_session is None and kind == "file-history-snapshot":
            pass
        elif not isinstance(current_session, str) or not current_session:
            raise SourceError(f"missing session identity at line {line_number}")
        elif session_id is None:
            session_id = current_session
        elif current_session != session_id:
            raise SourceError(f"source mixes session identities at line {line_number}")
        if "session_id" in record and record["session_id"] != current_session:
            raise SourceError(f"conflicting session identity at line {line_number}")
        if "version" in record and record["version"] != NATIVE_VERSION:
            raise SourceError(f"unsupported producer version at line {line_number}")
        if "cwd" in record:
            current_cwd = record["cwd"]
            if not isinstance(current_cwd, str) or not current_cwd.startswith("/"):
                raise SourceError(f"invalid project identity at line {line_number}")
            if cwd is None:
                cwd = current_cwd
            elif current_cwd != cwd:
                raise SourceError(f"source mixes project identities at line {line_number}")
        uuid = record.get("uuid")
        if uuid is not None and (not isinstance(uuid, str) or not uuid or uuid in nodes):
            raise SourceError(f"invalid or duplicate source UUID at line {line_number}")
        if any(field in record and record[field] is not False
               for field in ("isSidechain", "isMeta", "isCompactSummary")):
            raise SourceError(f"unsupported sidechain or compacted history at line {line_number}")
        if kind in _NATIVE_METADATA and uuid is None:
            omitted[kind] = omitted.get(kind, 0) + 1
            continue
        if kind not in {"user", "assistant", "attachment", "system"}:
            raise SourceError(f"unsupported native record structure at line {line_number}")
        if not isinstance(uuid, str) or not uuid:
            raise SourceError(f"missing source UUID at line {line_number}")
        if record.get("version") != NATIVE_VERSION or record.get("cwd") != cwd or current_session != session_id:
            raise SourceError(f"missing native identity or version at line {line_number}")
        if record.get("isSidechain") is not False:
            raise SourceError(f"unsupported sidechain or compacted history at line {line_number}")
        parent = record.get("parentUuid")
        if "parentUuid" not in record or (parent is not None and (not isinstance(parent, str) or not parent)):
            raise SourceError(f"invalid parent identity at line {line_number}")
        if parent is not None and parent not in nodes:
            raise SourceError(f"missing, cyclic or forward parent at line {line_number}")
        if parent != last_node:
            raise SourceError(f"unsupported competing ancestry branch at line {line_number}")
        nodes[uuid] = {"kind": kind, "parent": parent}
        last_node = uuid
        if kind == "attachment":
            attachment = record.get("attachment")
            if not isinstance(attachment, dict) or attachment.get("type") not in _NATIVE_ATTACHMENTS:
                raise SourceError(f"unsupported attachment ancestry at line {line_number}")
            omitted["attachment"] = omitted.get("attachment", 0) + 1
            continue
        if kind == "system":
            if record.get("subtype") != "turn_duration":
                raise SourceError(f"unsupported system or compaction semantics at line {line_number}")
            omitted["turn_duration"] = omitted.get("turn_duration", 0) + 1
            continue
        ancestor = parent
        while ancestor is not None and nodes[ancestor]["kind"] not in {"user", "assistant"}:
            ancestor = nodes[ancestor]["parent"]
        expected_parent = exchanges[-1]["uuid"] if exchanges else None
        expected_role = "assistant" if exchanges and exchanges[-1]["role"] == "user" else "user"
        if ancestor != expected_parent or kind != expected_role:
            raise SourceError(f"unsupported competing branch or message sequence at line {line_number}")
        message = record.get("message")
        if not isinstance(message, dict) or message.get("role") != kind:
            raise SourceError(f"invalid native message role at line {line_number}")
        if not isinstance(record.get("timestamp"), str) or not record["timestamp"]:
            raise SourceError(f"missing native message timestamp at line {line_number}")
        if kind == "assistant" and message.get("stop_reason") not in {"end_turn", "stop_sequence"}:
            raise SourceError(f"unsupported incomplete or tool assistant message at line {line_number}")
        content = message.get("content")
        if isinstance(content, str):
            body, omitted_content = content, []
        elif isinstance(content, list) and content:
            if any(not isinstance(part, dict) or part.get("type") not in {"text", "thinking", "redacted_thinking", "image"} for part in content):
                raise SourceError(f"unsupported tool or content structure at line {line_number}")
            texts = [part.get("text") for part in content if part.get("type") == "text"]
            if not texts or not all(isinstance(text, str) for text in texts):
                raise SourceError(f"missing native text at line {line_number}")
            body = "\n".join(texts)
            omitted_content = [part["type"] for part in content if part["type"] != "text"]
        else:
            raise SourceError(f"unsupported native content at line {line_number}")
        exchanges.append({"uuid": uuid, "role": kind, "timestamp": record.get("timestamp"),
                          "body": body, "omitted_content": omitted_content,
                          "source_line": line_number, "source_offset": offset})
    if session_id is None or cwd is None or not exchanges:
        raise SourceError("source contains no supported native exchanges")
    disclosures.extend({"kind": "omitted_native_records", "type": kind, "count": count}
                       for kind, count in sorted(omitted.items()))
    return {"vendor": "claude-code", "vendor_version": NATIVE_VERSION,
            "adapter_contract": NATIVE_VERSION + "-observed-subset", "session_id": session_id,
            "cwd": cwd, "exchanges": exchanges, "disclosures": disclosures,
            "deferred_partial": deferred_partial, "complete_bytes": complete_bytes,
            "native_schema": "unqualified_complete_history"}
