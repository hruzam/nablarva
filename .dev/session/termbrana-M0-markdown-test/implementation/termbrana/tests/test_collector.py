import json
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parents[1]
FIXTURE = HERE / "fixtures/codex-0.166.synthetic.jsonl"
CLAUDE_FIXTURE = HERE / "fixtures/claude-2.1.286.synthetic.jsonl"
PROGRAM = HERE / "collector.py"


class CollectorTest(unittest.TestCase):
    def command(self, *args, check=True):
        return subprocess.run(
            ["python3", "-I", "-S", "-B", str(PROGRAM), *map(str, args)],
            text=True,
            capture_output=True,
            check=check,
        )

    def append_record(self, source):
        source.write_bytes(
            source.read_bytes()
            + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n'
        )

    def complete_fixture(self):
        raw = FIXTURE.read_bytes()
        return raw[:raw.rfind(b"\n") + 1]

    def collect_args(self, source, cache, vendor="codex", version="0.166.0"):
        return ("--source", source, "--cache", cache, "--project", "/project/demo", "--vendor", vendor, "--vendor-version", version)

    def refresh_args(self, source, cache, record="item-user-003"):
        return (*self.collect_args(source, cache), "--record", record)

    def module(self):
        spec = importlib.util.spec_from_file_location("stage1_collector", PROGRAM)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_collect_keeps_selected_snapshot_until_explicit_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.assertEqual(first["selected_snapshot"], first["latest_snapshot"])
            self.append_record(source)
            second = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.assertNotEqual(second["selected_snapshot"], second["latest_snapshot"])
            self.assertTrue(second["new_records_available"])
            self.assertEqual(second["selected_read"], first["selected_read"])
            refreshed = json.loads(self.command("refresh", *self.refresh_args(source, cache)).stdout)
            self.assertTrue(refreshed["refreshed"])
            self.assertEqual(refreshed["selected_snapshot"], refreshed["latest_snapshot"])

    def test_partial_tail_does_not_make_new_records_available(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            source.write_bytes(source.read_bytes() + b'{"unfinished"')
            second = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.assertEqual(second["latest_snapshot"], first["latest_snapshot"])
            self.assertFalse(second["new_records_available"])
            self.assertTrue(second["complete_prefix_unchanged"])
            refreshed = json.loads(self.command("refresh", *self.refresh_args(source, cache)).stdout)
            self.assertFalse(refreshed["refreshed"])
            self.assertEqual(refreshed["reason"], "no newer complete records")

    def test_refresh_failure_keeps_selected_snapshot_and_watch_is_bounded(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            source.write_bytes(b"short\n")
            refreshed = json.loads(self.command("refresh", *self.refresh_args(source, cache)).stdout)
            self.assertFalse(refreshed["refreshed"])
            self.assertEqual(refreshed["selected_snapshot"], first["selected_snapshot"])
            watched = self.command("watch", *self.collect_args(source, cache), "--interval", "0.001", "--cycles", "2")
            results = [json.loads(line) for line in watched.stdout.splitlines()]
            self.assertEqual(len(results), 2)
            self.assertTrue(all(not result["ok"] for result in results))

    def test_refresh_missing_source_keeps_selected_snapshot(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            source.unlink()
            refreshed = json.loads(self.command("refresh", *self.refresh_args(source, cache)).stdout)
            self.assertFalse(refreshed["refreshed"])
            self.assertIn("source is missing or unreadable", refreshed["reason"])
            self.assertEqual(refreshed["selected_snapshot"], first["selected_snapshot"])

    def test_refresh_without_bookmark_leaves_selection_unchanged(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.append_record(source)
            self.command("collect", *self.collect_args(source, cache))
            result = json.loads(self.command("refresh", *self.collect_args(source, cache)).stdout)
            self.assertFalse(result["refreshed"])
            self.assertEqual(result["reason"], "refresh blocked: no bookmark selected")
            self.assertEqual(result["selected_snapshot"], first["selected_snapshot"])

    def test_complete_metadata_append_is_available_without_new_exchange(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-tool-008","type":"exec_command_begin","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            second = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.assertTrue(second["new_snapshot_available"])
            self.assertTrue(second["new_records_available"])
            self.assertEqual(second["selected_records"], first["selected_records"])
            self.assertEqual(second["latest_records"], first["latest_records"])

    def test_refresh_revalidates_the_bundle_published_after_its_precheck(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.append_record(source)
            module = self.module()
            context = {"project": "/project/demo", "vendor": "codex", "vendor_version": "0.166.0"}
            original_publish = module.transcript.publish

            def publish_after_replacement(current_source, current_cache, current_context):
                replacement = root / "replacement.jsonl"
                replacement.write_bytes(source.read_bytes())
                os.replace(replacement, source)
                return original_publish(current_source, current_cache, current_context)

            with mock.patch.object(module.transcript, "publish", side_effect=publish_after_replacement):
                refreshed = module.refresh(source, cache, context, "item-user-003")
            self.assertFalse(refreshed["refreshed"])
            self.assertEqual(refreshed["reason"], "refresh blocked: source changed during capture")
            self.assertEqual(refreshed["selected_snapshot"], first["selected_snapshot"])

    def test_context_change_publishes_without_calling_records_new(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            first = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            second = json.loads(self.command(
                "collect", *self.collect_args(source, cache, version="0.167.0")
            ).stdout)
            self.assertIsNotNone(second["published_snapshot"])
            self.assertNotEqual(second["latest_snapshot"], first["latest_snapshot"])
            self.assertFalse(second["new_records_available"])

    def test_replaced_source_never_labels_records_new(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            self.command("collect", *self.collect_args(source, cache))
            replacement = root / "replacement.jsonl"
            replacement.write_bytes(
                self.complete_fixture()
                + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n'
            )
            replacement.replace(source)
            current = json.loads(self.command("collect", *self.collect_args(source, cache)).stdout)
            self.assertTrue(current["new_snapshot_available"])
            self.assertFalse(current["new_records_available"])

    def test_claude_vendor_collects_explicit_synthetic_fixture(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "claude.jsonl", root / "cache"
            source.write_bytes(CLAUDE_FIXTURE.read_bytes())
            result = json.loads(self.command(
                "collect", *self.collect_args(source, cache, vendor="claude-code", version="2.1.286")
            ).stdout)
            self.assertEqual(result["selected_records"], 4)
            bundle = cache / "snapshots" / result["selected_snapshot"]
            metadata = json.loads((bundle / "map.json").read_text())
            self.assertEqual(metadata["context"]["vendor"], "claude-code")

    def test_layout_reading_is_initialized_and_moves_only_on_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.jsonl"
            source.write_bytes(self.complete_fixture())
            module = self.module()
            context = {"project": str(root / "project"), "vendor": "codex", "vendor_version": "0.166.0"}
            cache, reading = module.transcript.prepare_layout(root / "home", context, "bed", "session", source)
            first = module.collect_once(source, cache, context)
            self.assertEqual(reading.read_bytes(), (cache / "snapshots" / first["selected_snapshot"] / "read.md").read_bytes())
            initial = reading.read_bytes()
            self.append_record(source)
            second = module.collect_once(source, cache, context)
            self.assertNotEqual(second["latest_snapshot"], second["selected_snapshot"])
            self.assertEqual(reading.read_bytes(), initial)
            refreshed = module.refresh(source, cache, context, "item-user-003")
            self.assertTrue(refreshed["refreshed"])
            self.assertEqual(reading.read_bytes(), (cache / "snapshots" / refreshed["selected_snapshot"] / "read.md").read_bytes())
            self.assertEqual(Path(refreshed["reading_materialized"]), reading)

    def test_layout_materialization_failure_restores_selection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.jsonl"
            source.write_bytes(self.complete_fixture())
            module = self.module()
            context = {"project": str(root / "project"), "vendor": "codex", "vendor_version": "0.166.0"}
            cache, reading = module.transcript.prepare_layout(root / "home", context, "bed", "session", source)
            first = module.collect_once(source, cache, context)
            pointer = (cache / "selected.json").read_bytes()
            old_reading = reading.read_bytes()
            self.append_record(source)
            module.collect_once(source, cache, context)
            with mock.patch.object(module.transcript, "materialize_selected_reading", side_effect=OSError("read blocked")):
                refreshed = module.refresh(source, cache, context, "item-user-003")
            self.assertFalse(refreshed["refreshed"])
            self.assertIn("selected reading update failed", refreshed["reason"])
            self.assertEqual((cache / "selected.json").read_bytes(), pointer)
            self.assertEqual(reading.read_bytes(), old_reading)
            self.assertEqual(refreshed["selected_snapshot"], first["selected_snapshot"])

    def test_abrupt_refresh_exit_is_detected_and_retry_repairs_reading(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.jsonl"
            source.write_bytes(self.complete_fixture())
            module = self.module()
            context = {"project": str(root / "project"), "vendor": "codex", "vendor_version": "0.166.0"}
            cache, reading = module.transcript.prepare_layout(root / "home", context, "bed", "session", source)
            first = module.collect_once(source, cache, context)
            initial = reading.read_bytes()
            self.append_record(source)
            module.collect_once(source, cache, context)
            # Die after selected.json commits but before the derived reading copy.
            child = '''import importlib.util,json,os,sys
from pathlib import Path
spec=importlib.util.spec_from_file_location("collector_crash",sys.argv[1])
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.transcript.materialize_selected_reading=lambda *a,**k: os._exit(79)
m.refresh(Path(sys.argv[2]),Path(sys.argv[3]),json.loads(sys.argv[4]),"item-user-003")
'''
            died = subprocess.run(["python3", "-I", "-S", "-B", "-c", child, str(PROGRAM), str(source), str(cache), json.dumps(context)])
            self.assertEqual(died.returncode, 79)
            selected = json.loads((cache / "selected.json").read_text())["snapshot"]
            self.assertNotEqual(selected, first["selected_snapshot"])
            self.assertEqual(reading.read_bytes(), initial)
            with self.assertRaisesRegex(module.transcript.SourceError, "inconsistent.*recover"):
                module.transcript.resolve_reading_bundle(cache, None)
            # An explicit retained snapshot is independently readable during recovery.
            module.transcript.resolve_reading_bundle(cache, first["selected_snapshot"])
            retry = module.refresh(source, cache, context, "item-user-003")
            self.assertFalse(retry["refreshed"])
            self.assertEqual(retry["reason"], "no newer complete records")
            self.assertEqual(reading.read_bytes(), (cache / "snapshots" / selected / "read.md").read_bytes())
            self.assertEqual(module.transcript.resolve_reading_bundle(cache, None)[1]["snapshot"], selected)
            unchanged_mtime = reading.stat().st_mtime_ns
            module.collect_once(source, cache, context)
            self.assertEqual(reading.stat().st_mtime_ns, unchanged_mtime)

    def test_watch_flushes_a_cycle_before_it_exits(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            process = subprocess.Popen(
                ["python3", "-I", "-S", "-B", str(PROGRAM), "watch", *map(str, self.collect_args(source, cache)), "--interval", "0.2", "--cycles", "2"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            first = process.stdout.readline()
            self.assertTrue(first)
            self.assertIsNone(process.poll())
            self.assertTrue(json.loads(first)["ok"])
            remaining, errors = process.communicate(timeout=2)
            self.assertEqual(process.returncode, 0, errors)
            self.assertEqual(len(remaining.splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
