#!/usr/bin/env python3
"""Foreground collection for immutable transcript snapshots.

This module only polls an explicitly supplied file.  It neither discovers nor resumes
native sessions, starts an editor, nor runs after its command exits.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import time


_TRANSCRIPT_PATH = Path(__file__).with_name("transcript.py")
_TRANSCRIPT_SPEC = importlib.util.spec_from_file_location("termbrana_transcript", _TRANSCRIPT_PATH)
if _TRANSCRIPT_SPEC is None or _TRANSCRIPT_SPEC.loader is None:
    raise RuntimeError("unable to load adjacent transcript engine")
transcript = importlib.util.module_from_spec(_TRANSCRIPT_SPEC)
_TRANSCRIPT_SPEC.loader.exec_module(transcript)


class CollectionError(ValueError):
    pass


def _selection_path(cache: Path) -> Path:
    return cache / "selected.json"


def _write_selection(cache: Path, snapshot: str, record: str | None = None) -> None:
    bundle, metadata = transcript.resolve_bundle(cache, snapshot)
    del bundle
    payload = {
        "snapshot": snapshot,
        "map_sha256": transcript.digest((cache / "snapshots" / snapshot / "map.json").read_bytes()),
        "identity": metadata["identity"],
    }
    if record is not None:
        payload["record"] = record
    transcript.atomic_write(
        _selection_path(cache),
        (json.dumps(payload, sort_keys=True) + "\n").encode(),
    )


def _select_and_materialize(cache: Path, snapshot: str, record: str | None = None) -> Path | None:
    """Commit pointer, then derive its reading copy under the selection lock.

    A hard interruption can separate these writes. Implicit readers reject the
    mismatch and status/collect/refresh repair the copy from the committed pointer.
    """
    with transcript.selection_lock(cache):
        return _select_and_materialize_locked(cache, snapshot, record)


def _select_and_materialize_locked(cache: Path, snapshot: str, record: str | None = None) -> Path | None:
    pointer = _selection_path(cache)
    previous = pointer.read_bytes() if pointer.is_file() else None
    _write_selection(cache, snapshot, record)
    try:
        return transcript.materialize_selected_reading(cache, selection_locked=True)
    except (OSError, ValueError, transcript.SourceError):
        if previous is None:
            try:
                pointer.unlink()
            except FileNotFoundError:
                pass
        else:
            transcript.atomic_write(pointer, previous)
        raise


def _selection(cache: Path, fallback: str) -> dict:
    with transcript.selection_lock(cache):
        return _selection_locked(cache, fallback)


def _selection_locked(cache: Path, fallback: str) -> dict:
    path = _selection_path(cache)
    if not path.is_file():
        _select_and_materialize_locked(cache, fallback)
        return json.loads(path.read_text())
    selection = json.loads(path.read_text())
    snapshot = selection.get("snapshot")
    if not isinstance(snapshot, str) or not snapshot:
        raise CollectionError("selected snapshot pointer is invalid")
    map_path = cache / "snapshots" / snapshot / "map.json"
    if not map_path.is_file() or transcript.digest(map_path.read_bytes()) != selection.get("map_sha256"):
        raise CollectionError("selected snapshot pointer does not match its bundle")
    bundle, _ = transcript.resolve_bundle(cache, snapshot)
    if not transcript.reading_materialization_matches(cache, bundle):
        transcript.materialize_selected_reading(cache, selection_locked=True)
    return selection


def status(cache: Path) -> dict:
    _, latest = transcript.resolve_bundle(cache, None)
    latest_snapshot = latest["snapshot"]
    selected_pointer = _selection(cache, latest_snapshot)
    selected_snapshot = selected_pointer["snapshot"]
    _, selected = transcript.resolve_bundle(cache, selected_snapshot)
    selected_records = len(selected["pins"])
    same_source = (
        latest["source"]["path"],
        latest["source"]["device"],
        latest["source"]["inode"],
    ) == (
        selected["source"]["path"],
        selected["source"]["device"],
        selected["source"]["inode"],
    )
    same_conversation = latest["identity"] == selected["identity"]
    same_context = transcript.contexts_equal(latest.get("context"), selected.get("context"))
    selected_carryable = selected.get("history", {}).get("carry_forward_allowed", True)
    latest_carryable = latest.get("history", {}).get("carry_forward_allowed", True)
    latest_retained = (cache / "snapshots" / latest_snapshot / "source.jsonl").read_bytes()
    selected_retained = (cache / "snapshots" / selected_snapshot / "source.jsonl").read_bytes()
    complete_prefix_extended = (
        len(latest_retained) > len(selected_retained)
        and latest_retained.startswith(selected_retained)
    )
    return {
        "selected_snapshot": selected_snapshot,
        "latest_snapshot": latest_snapshot,
        "selected_read": str((cache / "snapshots" / selected_snapshot / "read.md").resolve()),
        "latest_read": str((cache / "snapshots" / latest_snapshot / "read.md").resolve()),
        "selected_record": selected_pointer.get("record"),
        "new_snapshot_available": latest_snapshot != selected_snapshot,
        "new_records_available": (
            latest_snapshot != selected_snapshot
            and same_source
            and same_conversation
            and same_context
            and complete_prefix_extended
            and selected_carryable
            and latest_carryable
        ),
        "selected_records": selected_records,
        "latest_records": len(latest["pins"]),
    }


def _complete_prefix_unchanged(source: Path, cache: Path, context: dict, snapshot: str | None = None) -> bool:
    """Whether a same-source poll adds no complete records to one retained bundle."""
    _, latest = transcript.resolve_bundle(cache, snapshot)
    if not transcript.contexts_equal(latest.get("context"), context):
        return False
    inspected = transcript.inspect_source(source, context)
    provenance = inspected["provenance"]
    old = latest["source"]
    if (provenance["path"], provenance["device"], provenance["inode"]) != (
        old["path"], old["device"], old["inode"],
    ):
        return False
    if inspected["identity"] != latest["identity"]:
        return False
    return transcript.digest(inspected["retained"]) == latest["retained"]["sha256"]


def collect_once(source: Path, cache: Path, context: dict) -> dict:
    """Capture one complete-prefix snapshot without moving the reading selection."""
    if (cache / "current.json").is_file() and _complete_prefix_unchanged(source, cache, context):
        return {"published_snapshot": None, "complete_prefix_unchanged": True, **status(cache)}
    published = transcript.publish(source, cache, context)
    current = status(cache)
    return {"published_snapshot": published["snapshot"], "complete_prefix_unchanged": False, **current}


def _published_carries_selected(cache: Path, selected_snapshot: str, published_snapshot: str, context: dict) -> bool:
    selected_bundle, selected = transcript.resolve_bundle(cache, selected_snapshot)
    published_bundle, published = transcript.resolve_bundle(cache, published_snapshot)
    if not transcript.contexts_equal(selected.get("context"), context):
        return False
    if not transcript.contexts_equal(published.get("context"), context):
        return False
    if selected["identity"] != published["identity"]:
        return False
    if not selected.get("history", {}).get("carry_forward_allowed", True):
        return False
    if not published.get("history", {}).get("carry_forward_allowed", True):
        return False
    old = selected["source"]
    new = published["source"]
    if (old["path"], old["device"], old["inode"]) != (new["path"], new["device"], new["inode"]):
        return False
    retained = (selected_bundle / "source.jsonl").read_bytes()
    candidate = (published_bundle / "source.jsonl").read_bytes()
    return len(candidate) >= len(retained) and candidate.startswith(retained)


def refresh(source: Path, cache: Path, context: dict, record: str | None) -> dict:
    """Move the selected view only after validating carry-forward from that selection."""
    before = status(cache)
    if record is None:
        return {**before, "refreshed": False, "reason": "refresh blocked: no bookmark selected"}
    _, selected = transcript.resolve_bundle(cache, before["selected_snapshot"])
    if record not in selected["pins"]:
        return {**before, "refreshed": False, "reason": "refresh blocked: bookmark is absent from selected snapshot"}
    try:
        carried = transcript.carry_forward(source, cache, before["selected_snapshot"])
    except transcript.SourceError as exc:
        return {**before, "refreshed": False, "reason": str(exc)}
    except OSError as exc:
        return {**before, "refreshed": False, "reason": f"refresh unavailable: source is missing or unreadable: {exc}"}
    if _complete_prefix_unchanged(source, cache, context, before["selected_snapshot"]):
        return {**before, "refreshed": False, "reason": "no newer complete records"}
    published = transcript.publish(source, cache, context)
    if not _published_carries_selected(cache, before["selected_snapshot"], published["snapshot"], context):
        return {**status(cache), "refreshed": False, "reason": "refresh blocked: source changed during capture"}
    _, latest = transcript.resolve_bundle(cache, published["snapshot"])
    if record not in latest["pins"]:
        return {**status(cache), "refreshed": False, "reason": "refresh blocked: bookmark is absent from newer snapshot"}
    try:
        reading = _select_and_materialize(cache, published["snapshot"], record)
    except (OSError, ValueError, transcript.SourceError) as exc:
        return {**status(cache), "refreshed": False, "reason": f"refresh blocked: selected reading update failed: {exc}"}
    return {
        **status(cache),
        "refreshed": True,
        "carry_forward": carried["carry_forward"],
        "reading_materialized": str(reading) if reading is not None else None,
    }


def watch(source: Path, cache: Path, context: dict, interval: float, cycles: int):
    if interval <= 0:
        raise CollectionError("interval must be positive")
    if cycles < 1:
        raise CollectionError("cycles must be at least one")
    for cycle in range(cycles):
        try:
            yield {"cycle": cycle + 1, "ok": True, **collect_once(source, cache, context)}
        except (OSError, ValueError, transcript.SourceError) as exc:
            yield {"cycle": cycle + 1, "ok": False, "reason": str(exc)}
        if cycle + 1 < cycles:
            time.sleep(interval)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("collect", "refresh"):
        command = commands.add_parser(name)
        command.add_argument("--source", required=True, type=Path)
        command.add_argument("--cache", required=True, type=Path)
        command.add_argument("--project", required=True, type=Path)
        command.add_argument("--vendor", required=True, choices=("codex", "claude-code"))
        command.add_argument("--vendor-version", required=True)
        command.add_argument("--input-format", choices=(transcript.SYNTHETIC_EVENT_FORMAT, *transcript.CODEX_NATIVE_FORMATS), default=transcript.SYNTHETIC_EVENT_FORMAT)
        if name == "refresh":
            command.add_argument("--record")
    status_parser = commands.add_parser("status")
    status_parser.add_argument("--cache", required=True, type=Path)
    watch_parser = commands.add_parser("watch")
    watch_parser.add_argument("--source", required=True, type=Path)
    watch_parser.add_argument("--cache", required=True, type=Path)
    watch_parser.add_argument("--project", required=True, type=Path)
    watch_parser.add_argument("--vendor", required=True, choices=("codex", "claude-code"))
    watch_parser.add_argument("--vendor-version", required=True)
    watch_parser.add_argument("--input-format", choices=(transcript.SYNTHETIC_EVENT_FORMAT, *transcript.CODEX_NATIVE_FORMATS), default=transcript.SYNTHETIC_EVENT_FORMAT)
    watch_parser.add_argument("--interval", required=True, type=float)
    watch_parser.add_argument("--cycles", required=True, type=int)
    args = parser.parse_args()
    try:
        context = None
        if args.command in {"collect", "refresh", "watch"}:
            context = {
                "project": str(args.project.resolve(strict=False)),
                "vendor": args.vendor,
                "vendor_version": args.vendor_version,
                "input_format": args.input_format,
            }
        if args.command == "collect":
            result = collect_once(args.source, args.cache, context)
        elif args.command == "refresh":
            result = refresh(args.source, args.cache, context, args.record)
        elif args.command == "status":
            result = status(args.cache)
        elif args.command == "watch":
            for cycle in watch(args.source, args.cache, context, args.interval, args.cycles):
                print(json.dumps(cycle, sort_keys=True), flush=True)
            return 0
        print(json.dumps(result, sort_keys=True))
    except (OSError, ValueError, CollectionError, transcript.SourceError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
