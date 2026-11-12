#!/usr/bin/env python3
"""Create immutable synthetic Codex transcript snapshots."""

import argparse
from contextlib import contextmanager, nullcontext
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

RENDERER_VERSION = "0.2-stage1"
CONVERSATION_TYPES = {"user_message": "user", "agent_message": "assistant"}
CLAUDE_ADAPTER_PATH = Path(__file__).with_name("claude_adapter.py")
CODEX_NATIVE_ADAPTER_PATH = Path(__file__).with_name("codex_native.py")
SYNTHETIC_EVENT_FORMAT = "synthetic-event-jsonl"
CODEX_NATIVE_FORMAT = "codex-rollout-0.166"
CODEX_COMPLETED_FORMAT = "codex-rollout-0.167"
CODEX_NATIVE_FORMATS = (CODEX_NATIVE_FORMAT, CODEX_COMPLETED_FORMAT)


class SourceError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_context(context: dict | None) -> dict:
    """Compare legacy synthetic metadata without rewriting its immutable map."""
    normalized = dict(context or {})
    normalized.setdefault("input_format", SYNTHETIC_EVENT_FORMAT)
    return normalized


def contexts_equal(left: dict | None, right: dict | None) -> bool:
    return normalized_context(left) == normalized_context(right)


def snapshot_context(context: dict) -> dict:
    """Retain legacy synthetic snapshot keys while keeping native format explicit."""
    key = normalized_context(context)
    if key["input_format"] == SYNTHETIC_EVENT_FORMAT:
        key.pop("input_format")
    return key


def read_snapshot(source: Path) -> tuple[bytes, dict]:
    resolved = source.resolve(strict=True)
    with resolved.open("rb") as handle:
        before = os.fstat(handle.fileno())
        data = handle.read()
        after = os.fstat(handle.fileno())
    fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns")
    if any(getattr(before, field) != getattr(after, field) for field in fields):
        raise SourceError("source changed while reading; retry from a stable snapshot")
    return data, {
        "path": str(resolved), "device": before.st_dev, "inode": before.st_ino,
        "snapshot_sha256": digest(data), "snapshot_bytes": len(data),
    }


def load_codex(data: bytes):
    records, unsupported, offset = [], [], 0
    seen_ids = set()
    deferred_partial = False
    for number, line in enumerate(data.splitlines(keepends=True), 1):
        line_offset = offset
        if not line.endswith(b"\n"):
            deferred_partial = True
            break
        offset += len(line)
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SourceError(f"malformed complete JSONL record at line {number}: {exc.msg}") from exc
        payload = event.get("payload") if event.get("type") == "event_msg" else None
        if not isinstance(payload, dict):
            unsupported.append({"line": number, "offset": line_offset, "reason": "not_event_msg"})
            continue
        kind, record_id = payload.get("type"), payload.get("id")
        if kind == "synthetic_approval_request":
            unsupported.append({
                "kind": "approval_request", "id": record_id, "type": kind,
                "timestamp": event.get("timestamp"), "request": payload.get("message"),
                "source_line": number, "source_offset": line_offset,
                "approval_outcome": "unknown", "schema": "fictional_synthetic_fixture",
            })
            continue
        if kind not in CONVERSATION_TYPES:
            unsupported.append({"id": record_id, "type": kind, "line": number, "offset": line_offset})
            continue
        required = (record_id, payload.get("message"), payload.get("thread_id"), payload.get("session_id"), payload.get("branch_id"))
        if not all(isinstance(value, str) and value for value in required):
            raise SourceError(f"incomplete conversation identity at line {number}")
        if record_id in seen_ids:
            raise SourceError(f"duplicate source record identity at line {number}: {record_id}")
        seen_ids.add(record_id)
        records.append({
            "id": record_id, "role": CONVERSATION_TYPES[kind], "timestamp": event.get("timestamp"),
            "body": payload["message"], "line": number, "offset": line_offset,
            "thread_id": payload["thread_id"], "session_id": payload["session_id"], "branch_id": payload["branch_id"],
        })
    if not records:
        raise SourceError("source contains no conversation records")
    identity = {key: records[0][key] for key in ("thread_id", "session_id", "branch_id")}
    if any(any(record[key] != value for key, value in identity.items()) for record in records):
        raise SourceError("source mixes conversation identities")
    return records, unsupported, deferred_partial, offset, identity


def load_claude(data: bytes):
    spec = importlib.util.spec_from_file_location("termbrana_claude_adapter", CLAUDE_ADAPTER_PATH)
    if spec is None or spec.loader is None:
        raise SourceError("unable to load adjacent Claude adapter")
    adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter)
    try:
        parsed = adapter.parse(data)
    except adapter.SourceError as exc:
        raise SourceError(str(exc)) from exc
    locations, offset = {}, 0
    for number, line in enumerate(data.splitlines(keepends=True), 1):
        if not line.endswith(b"\n"):
            break
        record = json.loads(line)
        uuid = record.get("uuid") if isinstance(record, dict) else None
        if isinstance(uuid, str):
            locations[uuid] = {"line": number, "offset": offset}
        offset += len(line)
    records, disclosures = [], list(parsed["disclosures"])
    for exchange in parsed["exchanges"]:
        location = locations.get(exchange["uuid"])
        if location is None:
            raise SourceError(f"missing source location for exchange: {exchange['uuid']}")
        records.append({
            "id": exchange["uuid"], "role": exchange["role"], "timestamp": exchange["timestamp"],
            "body": exchange["body"], "line": location["line"], "offset": location["offset"],
        })
        if exchange["omitted_content"]:
            disclosures.append({
                "kind": "omitted_content", "uuid": exchange["uuid"],
                "types": exchange["omitted_content"], "semantics": "unqualified",
            })
    identity = {
        "session_id": parsed["session_id"],
        "branch_id": "unqualified",
        "thread_id": "unqualified",
    }
    deferred_partial = any(item.get("kind") == "incomplete_final_line" for item in disclosures)
    return records, disclosures, deferred_partial, offset, identity


def load_codex_native(data: bytes, contract_version: str = "0.166.0"):
    """Adapt the public rollout subset without claiming qualified native support."""
    spec = importlib.util.spec_from_file_location("termbrana_codex_native", CODEX_NATIVE_ADAPTER_PATH)
    if spec is None or spec.loader is None:
        raise SourceError("unable to load adjacent Codex native adapter")
    adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter)
    try:
        parsed = adapter.parse(data, contract_version)
    except adapter.SourceError as exc:
        raise SourceError(str(exc)) from exc
    records = []
    for exchange in parsed["exchanges"]:
        pin = exchange["pin"]
        records.append({
            "id": exchange["id"], "role": exchange["role"], "timestamp": exchange["timestamp"],
            "body": exchange["body"], "line": pin["source_line"], "offset": pin["source_offset"],
            "native_pin": pin,
        })
    return records, parsed["disclosures"], parsed["deferred_partial"], parsed["complete_bytes"], parsed["identity"]


def load_vendor(vendor: str, data: bytes, input_format: str = SYNTHETIC_EVENT_FORMAT):
    if vendor == "codex" and input_format == SYNTHETIC_EVENT_FORMAT:
        return load_codex(data)
    if vendor == "codex" and input_format in CODEX_NATIVE_FORMATS:
        return load_codex_native(data, "0.167.0" if input_format == CODEX_COMPLETED_FORMAT else "0.166.0")
    if vendor == "claude-code" and input_format == SYNTHETIC_EVENT_FORMAT:
        return load_claude(data)
    raise SourceError(f"unsupported vendor/input format: {vendor}/{input_format}")


def history_state(vendor: str, input_format: str, disclosures: list[dict]) -> dict:
    """State the strongest claim this renderer may make about captured history."""
    if vendor != "codex" or input_format not in CODEX_NATIVE_FORMATS:
        return {"state": "synthetic_fixture", "full_history_claim": False}
    blockers = {
        "context_compaction", "compacted_history", "fork_or_history_base", "thread_rolled_back",
    }
    found = [item["kind"] for item in disclosures if item.get("kind") in blockers]
    return {
        "state": "incomplete" if found else "snapshot_only",
        "full_history_claim": False,
        "native_qualification": "unqualified_without_isolated_operator_rollout",
        "incomplete_reasons": found,
        "carry_forward_allowed": not found,
    }


def disclosure_line(item: dict) -> str:
    pin = item.get("pin") if isinstance(item.get("pin"), dict) else {}
    identifier = item.get("id") or item.get("uuid") or pin.get("id") or "no-id"
    kind = item.get("type") or item.get("kind") or item.get("reason") or "unknown"
    suffix = " · approval outcome unknown" if item.get("approval_outcome") == "unknown" else ""
    return f"- {identifier} · {kind}{suffix}"


def render_markdown(vendor, records, unsupported, deferred_partial, identity, cached_source, provenance, history=None):
    native = history is not None and history.get("state") in {"snapshot_only", "incomplete"}
    title = "# Transcript view (native source-derived snapshot)" if native else "# Transcript view (synthetic Stage 1)"
    lines = [title, "", "```text", f"vendor={vendor}", f"renderer={RENDERER_VERSION}"]
    if native:
        lines += [
            f"history_state={history['state']}",
            "full_history_claim=false",
            f"native_qualification={history['native_qualification']}",
        ]
    lines += [f"{key}={value}" for key, value in identity.items()]
    lines += ["```", ""]
    pins = {}
    for ordinal, record in enumerate(records, 1):
        line_number = "\n".join(lines).count("\n") + 2
        lines += [f"## {ordinal}. {record['role']} · {record['timestamp']} · {record['id']}", "", record["body"], ""]
        pins[record["id"]] = {
            "ordinal": ordinal, "markdown_line": line_number,
            "source_line": record["line"], "source_offset": record["offset"],
            "role": record["role"], "timestamp": record["timestamp"],
            "snippet": " ".join(record["body"].split())[:80],
        }
        if "native_pin" in record:
            pins[record["id"]]["native_pin"] = record["native_pin"]
    if unsupported:
        lines += ["## Disclosed unsupported records", ""]
        for item in unsupported:
            lines.append(disclosure_line(item))
            if item.get("kind") == "approval_request":
                lines += [
                    f"  - request: {item.get('request')}",
                    f"  - observed at: {item.get('timestamp')}",
                    f"  - cached source: {cached_source}:{item['source_line']}",
                    f"  - original provenance: {provenance['path']}",
                    "  - outcome: unknown; historical record only, not a live pending approval.",
                ]
        lines += [""]
    if deferred_partial:
        lines += ["## Deferred incomplete final record", "", "- The final unterminated JSONL line is not rendered.", ""]
    if native and history["state"] == "incomplete":
        lines += [
            "## Native history limitation", "",
            "- This snapshot is incomplete; inherited or compacted context is not reconstructed.",
            "- It must not be presented as the complete conversation history.",
            "",
        ]
    return "\n".join(lines).encode(), pins


def atomic_write(target: Path, data: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def safe_cache(source: Path, cache: Path) -> Path:
    cache_path = cache.resolve(strict=False)
    if source == cache_path or source.is_relative_to(cache_path):
        raise SourceError("cache must not be the source file or an ancestor of it")
    return cache_path


def safe_token(value: str, field: str) -> str:
    if not value or any(character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for character in value):
        raise SourceError(f"{field} must contain only letters, digits, hyphen, or underscore")
    return value


def project_slug(project: str) -> str:
    resolved = Path(project).resolve(strict=False)
    stem = "".join(character.lower() if character.isalnum() else "-" for character in resolved.name).strip("-") or "project"
    return f"{stem}-{digest(str(resolved).encode())[:12]}"


def prepare_layout(home: Path, context: dict, bed: str, agentive_session: str, source: Path) -> tuple[Path, Path]:
    bed = safe_token(bed, "bed")
    agentive_session = safe_token(agentive_session, "agentive session")
    project = str(Path(context["project"]).resolve(strict=False))
    root = home.resolve(strict=False) / project_slug(project) / bed
    cache = root / f"cache.{agentive_session}"
    reading = root / f"read.{agentive_session}.md"
    source_path = source.resolve(strict=True)
    cache = safe_cache(source_path, cache)
    if any(path.resolve(strict=False) == source_path for path in (cache / "layout.json", reading)):
        raise SourceError("generated layout path aliases the input source")
    expected = {
        "project": project, "bed": bed, "agentive_session": agentive_session,
        "vendor": context["vendor"], "vendor_version": context["vendor_version"],
        "input_format": context.get("input_format", SYNTHETIC_EVENT_FORMAT),
        "cache": str(cache), "reading": str(reading),
    }
    metadata = cache / "layout.json"
    if metadata.is_file():
        try:
            actual = json.loads(metadata.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            raise SourceError(f"layout cache metadata is unreadable: {exc}") from exc
        if not contexts_equal(actual, expected):
            raise SourceError("layout cache identity collision")
    elif cache.exists() and any(cache.iterdir()):
        raise SourceError("layout cache exists without identity metadata")
    else:
        cache.mkdir(parents=True, exist_ok=True)
        atomic_write(metadata, (json.dumps(expected, sort_keys=True) + "\n").encode())
    return cache, reading


def layout_metadata(cache: Path) -> dict | None:
    path = cache / "layout.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise SourceError(f"layout cache metadata is unreadable: {exc}") from exc


def initialize_selected_snapshot(cache: Path, snapshot: str) -> None:
    selected = cache / "selected.json"
    with selection_lock(cache):
        if not selected.exists():
            map_path = cache / "snapshots" / snapshot / "map.json"
            pointer = {"snapshot": snapshot, "map_sha256": digest(map_path.read_bytes())}
            atomic_write(selected, (json.dumps(pointer, sort_keys=True) + "\n").encode())


@contextmanager
def selection_lock(cache: Path):
    with (cache / ".selection.lock").open("a+b") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        yield


def reading_materialization_matches(cache: Path, bundle: Path) -> bool:
    layout = layout_metadata(cache)
    if layout is None:
        return True
    reading = Path(layout["reading"])
    return reading.is_file() and reading.read_bytes() == (bundle / "read.md").read_bytes()


def materialize_selected_reading(cache: Path, *, selection_locked: bool = False) -> Path | None:
    """Repair the derived copy from the committed pointer; no multi-file atomicity claim."""
    with nullcontext() if selection_locked else selection_lock(cache):
        layout = layout_metadata(cache)
        if layout is None:
            return None
        bundle, _ = resolve_reading_bundle(cache, None, validate_materialized=False)
        reading = Path(layout["reading"])
        if not reading_materialization_matches(cache, bundle):
            atomic_write(reading, (bundle / "read.md").read_bytes())
        return reading


def bundle_map(bundle: Path) -> dict:
    data = json.loads((bundle / "map.json").read_text())
    for name in ("source.jsonl", "read.md"):
        actual = (bundle / name).read_bytes()
        expected = data["files"][name]
        if len(actual) != expected["bytes"] or digest(actual) != expected["sha256"]:
            raise SourceError(f"snapshot bundle is inconsistent: {name}")
    return data


def inspect_source(source: Path, context: dict) -> dict:
    """Read one stable vendor source without publishing a bundle."""
    source_bytes, provenance = read_snapshot(source)
    vendor = context.get("vendor")
    if not isinstance(vendor, str):
        raise SourceError("context requires vendor")
    input_format = context.get("input_format", SYNTHETIC_EVENT_FORMAT)
    if vendor == "codex" and input_format in CODEX_NATIVE_FORMATS:
        expected_version = "0.167.0" if input_format == CODEX_COMPLETED_FORMAT else "0.166.0"
        if context.get("vendor_version") != expected_version:
            raise SourceError("vendor version does not match explicit native input format")
    records, disclosures, deferred_partial, boundary, identity = load_vendor(vendor, source_bytes, input_format)
    return {
        "source_bytes": source_bytes,
        "retained": source_bytes[:boundary],
        "provenance": provenance,
        "records": records,
        "disclosures": disclosures,
        "deferred_partial": deferred_partial,
        "boundary": boundary,
        "identity": identity,
        "history": history_state(vendor, input_format, disclosures),
    }


def snapshot_key(provenance: dict, retained: bytes, identity: dict, context: dict, deferred_partial: bool) -> str:
    capture = {
        "renderer": RENDERER_VERSION,
        "source": provenance,
        "retained_sha256": digest(retained),
        "identity": identity,
        "context": snapshot_context(context),
        "deferred_partial_final_line": deferred_partial,
    }
    return digest(json.dumps(capture, sort_keys=True, separators=(",", ":")).encode())[:24]


def publish(source: Path, cache: Path, context: dict) -> dict:
    inspected = inspect_source(source, context)
    provenance = inspected["provenance"]
    cache = safe_cache(Path(provenance["path"]), cache)
    vendor = context["vendor"]
    retained = inspected["retained"]
    records, unsupported, retained_partial, boundary, identity = load_vendor(
        vendor, retained, context.get("input_format", SYNTHETIC_EVENT_FORMAT)
    )
    if retained_partial or boundary != len(retained):
        raise SourceError("retained source is not a complete-record snapshot")
    deferred_partial = inspected["deferred_partial"]
    snapshot_id = snapshot_key(provenance, retained, identity, context, deferred_partial)
    snapshots, lock_path = cache / "snapshots", cache / ".publish.lock"
    target = snapshots / snapshot_id
    markdown, pins = render_markdown(
        vendor, records, unsupported, False, identity,
        target / "source.jsonl", provenance, inspected["history"],
    )
    cache.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+b") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        if not target.exists():
            snapshots.mkdir(parents=True, exist_ok=True)
            staging = Path(tempfile.mkdtemp(prefix=".staging-", dir=snapshots))
            try:
                (staging / "source.jsonl").write_bytes(retained)
                (staging / "read.md").write_bytes(markdown)
                metadata = {
                    "snapshot": snapshot_id, "renderer": RENDERER_VERSION, "vendor": vendor,
                    "context": context,
                    "source": provenance,
                    "retained": {"bytes": len(retained), "sha256": digest(retained), "complete_boundary": boundary},
                    "identity": identity, "deferred_partial_final_line": deferred_partial,
                    "history": inspected["history"],
                    "capture_state": {"deferred_incomplete_tail": deferred_partial},
                    "unsupported": unsupported, "pins": pins,
                    "approval_references": [item for item in unsupported if item.get("kind") == "approval_request"],
                    "files": {
                        "source.jsonl": {"bytes": len(retained), "sha256": digest(retained)},
                        "read.md": {"bytes": len(markdown), "sha256": digest(markdown)},
                    },
                    "continuity_limit": "Byte-identical same-inode truncate/regrow restoring the retained prefix is indistinguishable from append without a native generation identity.",
                }
                (staging / "map.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
                for entry in staging.iterdir():
                    with entry.open("rb") as handle:
                        os.fsync(handle.fileno())
                os.replace(staging, target)
            except BaseException:
                shutil.rmtree(staging, ignore_errors=True)
                raise
        metadata = bundle_map(target)
        pointer = {"snapshot": snapshot_id, "map_sha256": digest((target / "map.json").read_bytes())}
        atomic_write(cache / "current.json", (json.dumps(pointer, sort_keys=True) + "\n").encode())
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return {"cache": str(cache.resolve()), "snapshot": snapshot_id, "read": str((target / "read.md").resolve()), "map": str((target / "map.json").resolve()), "records": len(metadata["pins"]), "context": metadata["context"]}


def rebuild_bundle(bundle: Path) -> bytes:
    """Render a retained bundle without consulting its original source."""
    data = bundle_map(bundle)
    retained = (bundle / "source.jsonl").read_bytes()
    records, disclosures, deferred_partial, boundary, identity = load_vendor(
        data["vendor"], retained, data["context"].get("input_format", SYNTHETIC_EVENT_FORMAT)
    )
    if deferred_partial or boundary != len(retained):
        raise SourceError("retained bundle source is incomplete")
    return render_markdown(
        data["vendor"], records, disclosures, False, identity,
        bundle / "source.jsonl", data["source"], data.get("history"),
    )[0]


def resolve_bundle(cache: Path, snapshot: str | None) -> tuple[Path, dict]:
    if snapshot is None:
        pointer = json.loads((cache / "current.json").read_text())
        snapshot = pointer["snapshot"]
        map_path = cache / "snapshots" / snapshot / "map.json"
        if digest(map_path.read_bytes()) != pointer["map_sha256"]:
            raise SourceError("current pointer does not match its snapshot map")
    bundle = cache / "snapshots" / snapshot
    return bundle, bundle_map(bundle)


def resolve_reading_bundle(cache: Path, snapshot: str | None, *, validate_materialized: bool = True) -> tuple[Path, dict]:
    if snapshot is not None:
        return resolve_bundle(cache, snapshot)
    selected = cache / "selected.json"
    if not selected.is_file():
        return resolve_bundle(cache, None)
    try:
        pointer = json.loads(selected.read_text())
        selected_snapshot = pointer["snapshot"]
        map_path = cache / "snapshots" / selected_snapshot / "map.json"
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise SourceError(f"selected reading pointer is invalid: {exc}") from exc
    try:
        matches = digest(map_path.read_bytes()) == pointer.get("map_sha256")
    except OSError as exc:
        raise SourceError(f"selected reading snapshot is unavailable: {exc}") from exc
    if not matches:
        raise SourceError("selected reading pointer does not match its snapshot map")
    bundle, metadata = resolve_bundle(cache, selected_snapshot)
    if validate_materialized and not reading_materialization_matches(cache, bundle):
        raise SourceError("selected reading copy is inconsistent; run collector status to recover")
    return bundle, metadata


def carry_forward(source: Path, cache: Path, snapshot: str) -> dict:
    bundle, previous = resolve_bundle(cache, snapshot)
    current, provenance = read_snapshot(source)
    old = previous["source"]
    if (provenance["path"], provenance["device"], provenance["inode"]) != (old["path"], old["device"], old["inode"]):
        raise SourceError("carry-forward blocked: source identity changed")
    retained = (bundle / "source.jsonl").read_bytes()
    if len(current) < len(retained):
        raise SourceError("carry-forward blocked: source shortened")
    if current[:len(retained)] != retained:
        raise SourceError("carry-forward blocked: captured prefix changed")
    history = previous.get("history", {})
    if not history.get("carry_forward_allowed", True):
        raise SourceError("carry-forward blocked: native source history is incomplete")
    _, _, _, _, identity = load_vendor(
        previous["context"]["vendor"], current,
        previous["context"].get("input_format", SYNTHETIC_EVENT_FORMAT),
    )
    if identity != previous["identity"]:
        raise SourceError("carry-forward blocked: conversation identity changed")
    return {"from_snapshot": snapshot, "source": provenance, "carry_forward": True}


def selection(cache: Path, snapshot: str | None) -> dict:
    _, data = resolve_reading_bundle(cache, snapshot)
    entries = []
    for record_id, pin in sorted(data["pins"].items(), key=lambda item: item[1]["ordinal"]):
        entries.append({
            "number": pin["ordinal"], "record": record_id, "line": pin["markdown_line"],
            "role": pin["role"], "timestamp": pin["timestamp"], "snippet": pin["snippet"],
        })
    return {"snapshot": data["snapshot"], "entries": entries}


def open_record(cache: Path, snapshot: str | None, record: str) -> dict:
    bundle, data = resolve_reading_bundle(cache, snapshot)
    pin = data["pins"].get(record)
    if pin is None:
        raise SourceError("open blocked: source record is absent from this snapshot")
    target = f"{bundle / 'read.md'}:{pin['markdown_line']}"
    try:
        subprocess.run(["subl", "-n", target], check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SourceError(f"editor open failed for {target}: {exc}") from exc
    return {"opened": target, "snapshot": data["snapshot"], "source_record_id": record}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    command = parser.add_subparsers(dest="command", required=True)
    render_parser = command.add_parser("render")
    render_parser.add_argument("--vendor", required=True, choices=("codex", "claude-code"))
    render_parser.add_argument("--vendor-version", required=True)
    render_parser.add_argument("--input-format", choices=(SYNTHETIC_EVENT_FORMAT, *CODEX_NATIVE_FORMATS), default=SYNTHETIC_EVENT_FORMAT)
    render_parser.add_argument("--project", required=True, type=Path)
    render_parser.add_argument("--source", required=True, type=Path)
    render_parser.add_argument("--out", type=Path, help="disposable cache root")
    render_parser.add_argument("--home", type=Path, help="runtime home; defaults to ~/.nablarva in layout mode")
    render_parser.add_argument("--bed", help="task bed slug for layout mode")
    render_parser.add_argument("--agentive-session", help="safe vendor conversation/branch identifier for layout mode")
    pin_parser = command.add_parser("pin")
    pin_parser.add_argument("--cache", required=True, type=Path)
    pin_parser.add_argument("--snapshot")
    pin_parser.add_argument("--record", required=True)
    select_parser = command.add_parser("select")
    select_parser.add_argument("--cache", required=True, type=Path)
    select_parser.add_argument("--snapshot")
    open_parser = command.add_parser("open")
    open_parser.add_argument("--cache", required=True, type=Path)
    open_parser.add_argument("--snapshot")
    open_parser.add_argument("--record", required=True)
    carry_parser = command.add_parser("carry-forward")
    carry_parser.add_argument("--source", required=True, type=Path)
    carry_parser.add_argument("--cache", required=True, type=Path)
    carry_parser.add_argument("--snapshot", required=True)
    args = parser.parse_args()
    try:
        if args.command == "render":
            context = {
                "project": str(args.project.resolve(strict=False)),
                "vendor": args.vendor,
                "vendor_version": args.vendor_version,
                "input_format": args.input_format,
            }
            if args.out is not None:
                if args.home is not None or args.bed is not None or args.agentive_session is not None:
                    raise SourceError("--out cannot be combined with layout arguments")
                cache = args.out
            else:
                if args.bed is None or args.agentive_session is None:
                    raise SourceError("layout mode requires --bed and --agentive-session")
                home = args.home or (Path.home() / ".nablarva")
                cache, _ = prepare_layout(home, context, args.bed, args.agentive_session, args.source)
            result = publish(args.source, cache, context)
            if layout_metadata(cache) is not None:
                initialize_selected_snapshot(cache, result["snapshot"])
            reading = materialize_selected_reading(cache)
            if reading is not None:
                result["reading"] = str(reading)
        elif args.command == "pin":
            bundle, data = resolve_reading_bundle(args.cache, args.snapshot)
            pin = data["pins"].get(args.record)
            if pin is None:
                raise SourceError("pin invalid: source record is absent from this snapshot")
            result = {"vendor": data["vendor"], "snapshot": data["snapshot"], "context": data["context"], "identity": data["identity"], "source_record_id": args.record, "read": str((bundle / "read.md").resolve()), **pin}
        elif args.command == "select":
            result = selection(args.cache, args.snapshot)
        elif args.command == "open":
            result = open_record(args.cache, args.snapshot, args.record)
        else:
            result = carry_forward(args.source, args.cache, args.snapshot)
        print(json.dumps(result, sort_keys=True))
    except (OSError, ValueError, SourceError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
