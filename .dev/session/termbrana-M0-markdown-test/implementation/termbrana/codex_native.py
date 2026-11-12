#!/usr/bin/env python3
"""Conservative, explicitly versioned reader for Codex public rollout JSONL.

This is deliberately separate from ``transcript.py``.  It reads only bytes supplied
by its caller and models the public, tagged rollout envelope; it neither discovers nor
opens a Codex home directory.  Native qualification still requires an isolated
operator-produced rollout from the target build.

Sources (tag rust-v0.166.0):
* codex-rs/rollout/src/lib.rs: ``RolloutLine`` and the canonical decoder.
* codex-rs/history/src/rollout_payload.rs: the ``type``/``payload`` item wire form.
* codex-rs/protocol/src/protocol.rs: ``SessionMeta`` and message event payloads.

The explicit 0.167.0 subset additionally follows rust-v0.167.0
``protocol/src/{protocol,items,user_input}.rs`` completed-item text definitions.
It renders completed items only; alternate event/response representations stay
disclosed and do not become a second copy of a message.
"""

import json


class SourceError(ValueError):
    """The supplied bytes cannot be read under this deliberately narrow contract."""


CONVERSATION_EVENTS = {"user_message": "user", "agent_message": "assistant"}
SUPPORTED_HISTORY_MODES = {"legacy", "paginated"}


def _require_string(value, field, line):
    if not isinstance(value, str) or not value:
        raise SourceError(f"missing {field} at line {line}")
    return value


def _location(line, offset, ordinal, thread_id):
    """Return an explicit snapshot-bound reader pin.

    A paginated ordinal locates a record in this captured rollout, but it is not a
    universal durable identity: a revert can retain a stable thread ID while writing
    a distinct rollout ID.  Carrying an ordinal into another snapshot therefore
    requires separately validated capture continuity.  Legacy history has no native
    per-item identifier at all.
    """
    if ordinal is not None:
        return {
            "id": f"snapshot:thread:{thread_id}:ordinal:{ordinal}",
            "kind": "snapshot_bound_rollout_ordinal",
            "thread_id": thread_id,
            "ordinal": ordinal,
            "snapshot_bound": True,
            "carry_forward_requires": "validated_capture_continuity",
            "source_line": line,
            "source_offset": offset,
        }
    return {
        "id": f"snapshot:line:{line}:offset:{offset}",
        "kind": "snapshot_relative_position",
        "snapshot_relative": True,
        "carry_forward_requires": "validated_capture_continuity",
        "source_line": line,
        "source_offset": offset,
    }


def _parse_meta(payload, line):
    if not isinstance(payload, dict):
        raise SourceError(f"session_meta payload must be an object at line {line}")
    history_mode = payload.get("history_mode", "legacy")
    if history_mode not in SUPPORTED_HISTORY_MODES:
        raise SourceError(f"unsupported session_meta.history_mode at line {line}: {history_mode!r}")
    meta = {
        "thread_id": _require_string(payload.get("id"), "session_meta.id", line),
        "session_id": _require_string(payload.get("session_id"), "session_meta.session_id", line),
        "forked_from_id": payload.get("forked_from_id"),
        "attached_thread": payload.get("attached_thread", False),
        "forked_from_ordinal_exclusive": payload.get("forked_from_ordinal_exclusive"),
        "parent_thread_id": payload.get("parent_thread_id"),
        "history_mode": history_mode,
        "history_base": payload.get("history_base"),
        "subagent_history_start_ordinal": payload.get("subagent_history_start_ordinal"),
    }
    if payload.get("cli_version") is not None:
        meta["producer_version"] = payload["cli_version"]
    return meta


def parse(data: bytes, contract_version: str = "0.166.0") -> dict:
    """Parse a source-derived subset of a Codex rollout JSONL snapshot.

    Only the selected version's complete text representation becomes exchanges. Every other
    native representation stays visible as a disclosure rather than being guessed as
    a user-visible message.  In particular, ``response_item`` is not rendered: it
    can be an alternate persisted representation, but this reader cannot establish
    duplicate semantics from the file alone.
    """
    if contract_version not in {"0.166.0", "0.167.0"}:
        raise SourceError("unsupported Codex adapter contract version")
    exchanges, disclosures, seen_pins = [], [], set()
    completed_items = {}
    meta, offset, complete_records = None, 0, 0
    deferred_partial = False

    for line_number, raw_line in enumerate(data.splitlines(keepends=True), 1):
        line_offset = offset
        if not raw_line.endswith(b"\n"):
            deferred_partial = True
            disclosures.append({
                "kind": "incomplete_final_line",
                "source_line": line_number,
                "source_offset": line_offset,
                "semantics": "not parsed or rendered",
            })
            break
        offset += len(raw_line)
        try:
            record = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            raise SourceError(f"malformed complete JSONL record at line {line_number}: {exc.msg}") from exc
        if not isinstance(record, dict):
            raise SourceError(f"rollout record must be an object at line {line_number}")
        timestamp = _require_string(record.get("timestamp"), "rollout timestamp", line_number)
        ordinal = record.get("ordinal")
        if ordinal is not None and (not isinstance(ordinal, int) or isinstance(ordinal, bool) or ordinal < 0):
            raise SourceError(f"invalid rollout ordinal at line {line_number}")

        kind, payload = record.get("type"), record.get("payload")
        if complete_records == 0:
            if kind != "session_meta":
                raise SourceError("rollout must begin with session_meta")
            meta = _parse_meta(payload, line_number)
            producer = meta.get("producer_version")
            if producer is not None and producer != contract_version:
                raise SourceError("session_meta.cli_version does not match adapter contract")
            if contract_version == "0.167.0" and producer is None:
                raise SourceError("0.167 adapter requires session_meta.cli_version")
        elif kind == "session_meta":
            raise SourceError(f"duplicate session_meta at line {line_number}")
        complete_records += 1

        if meta["history_mode"] == "paginated" and ordinal is None:
            raise SourceError(f"paginated rollout record missing ordinal at line {line_number}")
        pin = _location(line_number, line_offset, ordinal, meta["thread_id"])
        if pin["id"] in seen_pins:
            raise SourceError(f"duplicate rollout position at line {line_number}: {pin['id']}")
        seen_pins.add(pin["id"])

        if kind == "session_meta":
            continue
        if kind == "response_item":
            disclosures.append({
                "kind": "potential_duplicate_representation",
                "native_type": "response_item",
                "response_item_type": payload.get("type") if isinstance(payload, dict) else None,
                "pin": pin,
                "semantics": "not rendered; relation to event_msg is unknown",
            })
            continue
        if kind == "compacted":
            disclosures.append({
                "kind": "compacted_history",
                "pin": pin,
                "semantics": "not rendered; prior context may have been replaced",
            })
            continue
        if kind != "event_msg" or not isinstance(payload, dict):
            disclosures.append({
                "kind": "unsupported_rollout_item",
                "native_type": kind,
                "pin": pin,
                "semantics": "not rendered",
            })
            continue

        event_type = payload.get("type")
        if contract_version == "0.167.0" and event_type == "item_completed":
            if payload.get("thread_id") != meta["thread_id"]:
                raise SourceError(f"completed item thread mismatch at line {line_number}")
            turn = _require_string(payload.get("turn_id"), "item_completed.turn_id", line_number)
            item = payload.get("item")
            if not isinstance(item, dict):
                raise SourceError(f"completed item must be an object at line {line_number}")
            item_type = item.get("type")
            if item_type == "ContextCompaction":
                disclosures.append({"kind": "context_compaction", "pin": pin,
                                    "semantics": "completed compaction; context reconstruction unavailable"})
                continue
            role = {"UserMessage": "user", "AgentMessage": "assistant"}.get(item_type)
            if role is None:
                disclosures.append({"kind": "unsupported_completed_item", "item_type": item_type,
                                    "pin": pin, "semantics": "not rendered"})
                continue
            item_id = _require_string(item.get("id"), "item.id", line_number)
            content = item.get("content")
            if not isinstance(content, list):
                raise SourceError(f"completed item content must be a list at line {line_number}")
            expected_text_type = "text" if role == "user" else "Text"
            texts, omitted = [], []
            for chunk in content:
                if not isinstance(chunk, dict):
                    raise SourceError(f"completed item content must contain objects at line {line_number}")
                if chunk.get("type") == expected_text_type:
                    if not isinstance(chunk.get("text"), str):
                        raise SourceError(f"completed item text must be a string at line {line_number}")
                    texts.append(chunk["text"])
                else:
                    omitted.append(chunk.get("type"))
            fingerprint = json.dumps({"turn": turn, "item": item}, sort_keys=True)
            if item_id in completed_items:
                if completed_items[item_id] != fingerprint:
                    raise SourceError(f"conflicting completed item identity at line {line_number}")
                disclosures.append({"kind": "duplicate_completed_item", "item_id": item_id,
                                    "pin": pin, "semantics": "identical item rendered once"})
                continue
            completed_items[item_id] = fingerprint
            if omitted:
                disclosures.append({"kind": "omitted_content", "types": omitted,
                                    "pin": pin, "semantics": "non-text content not rendered"})
            extra = sorted(key for key in item if key not in {"type", "id", "content", "phase", "client_id"}
                           and item[key] is not None)
            if extra:
                disclosures.append({"kind": "unsupported_item_metadata", "fields": extra,
                                    "pin": pin, "semantics": "not rendered"})
            if not texts:
                continue
            pin.update({"native_item_id": item_id, "turn_id": turn})
            if item.get("phase") is not None:
                pin["native_phase"] = item["phase"]
            exchanges.append({"id": pin["id"], "role": role, "body": "\n".join(texts),
                              "timestamp": timestamp, "pin": pin, "phase": item.get("phase")})
            continue
        if event_type == "thread_rolled_back":
            disclosures.append({
                "kind": "thread_rolled_back",
                "pin": pin,
                "semantics": "not rendered; persisted rollback removes earlier user turns",
            })
            continue
        if event_type == "context_compacted":
            disclosures.append({
                "kind": "context_compaction",
                "pin": pin,
                "semantics": "not rendered; adapter does not reconstruct replaced context",
            })
            continue
        role = CONVERSATION_EVENTS.get(event_type)
        if contract_version == "0.167.0" and role is not None:
            disclosures.append({"kind": "potential_duplicate_representation", "event_type": event_type,
                                "pin": pin, "semantics": "only completed items rendered in 0.167 contract"})
            continue
        if role is None:
            disclosures.append({
                "kind": "unsupported_event",
                "event_type": event_type,
                "pin": pin,
                "semantics": "not rendered",
            })
            continue
        message = payload.get("message")
        if not isinstance(message, str):
            raise SourceError(f"{event_type}.message must be a string at line {line_number}")
        exchanges.append({
            "id": pin["id"],
            "role": role,
            "body": message,
            "timestamp": timestamp,
            "pin": pin,
            "phase": payload.get("phase"),
        })

    if meta is None:
        raise SourceError("source contains no complete rollout metadata")
    if not exchanges:
        raise SourceError("source contains no supported conversation events")
    lineage_present = (
        meta["forked_from_id"] is not None
        or meta["attached_thread"] is True
        or meta["forked_from_ordinal_exclusive"] is not None
        or meta["parent_thread_id"] is not None
        or meta["history_base"] is not None
        or meta["subagent_history_start_ordinal"] is not None
    )
    if lineage_present:
        disclosures.append({
            "kind": "fork_or_history_base",
            "thread_id": meta["thread_id"],
            "forked_from_id": meta["forked_from_id"],
            "attached_thread": meta["attached_thread"],
            "forked_from_ordinal_exclusive": meta["forked_from_ordinal_exclusive"],
            "parent_thread_id": meta["parent_thread_id"],
            "history_base": meta["history_base"],
            "subagent_history_start_ordinal": meta["subagent_history_start_ordinal"],
            "semantics": "lineage/inherited history disclosed; this adapter does not merge another rollout",
        })
    return {
        "vendor": "codex",
        "vendor_version": meta.get("producer_version"),
        "adapter_contract": contract_version + "-source-derived",
        "identity": meta,
        "exchanges": exchanges,
        "disclosures": disclosures,
        "deferred_partial": deferred_partial,
        "complete_bytes": offset,
        "native_qualification": "unqualified_without_isolated_operator_rollout",
    }
