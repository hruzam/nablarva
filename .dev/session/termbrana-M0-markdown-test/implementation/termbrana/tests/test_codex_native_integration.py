import json
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parents[1]
FIXTURE = HERE / "fixtures" / "codex-native-source-derived.jsonl"
TRANSCRIPT = HERE / "transcript.py"
COLLECTOR = HERE / "collector.py"
NATIVE_FORMAT = "codex-rollout-0.166"
SYNTHETIC = HERE / "fixtures" / "codex-0.166.synthetic.jsonl"


class CodexNativeIntegrationTests(unittest.TestCase):
    def transcript_module(self):
        spec = importlib.util.spec_from_file_location("termbrana_transcript_legacy", TRANSCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        return module

    def command(self, program, *args, check=True):
        return subprocess.run(
            ["python3", "-I", "-S", "-B", str(program), *map(str, args)],
            text=True, capture_output=True, check=check,
        )

    def render_args(self, source, cache, project):
        return (
            "render", "--vendor", "codex", "--vendor-version", "0.166.0",
            "--input-format", NATIVE_FORMAT, "--project", project,
            "--source", source, "--out", cache,
        )

    def collect_args(self, source, cache, project):
        return (
            "collect", "--source", source, "--cache", cache, "--project", project,
            "--vendor", "codex", "--vendor-version", "0.166.0",
            "--input-format", NATIVE_FORMAT,
        )

    def test_native_format_is_explicit_and_preserves_snapshot_bound_source_pins(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = json.loads(self.command(
                TRANSCRIPT, *self.render_args(FIXTURE, root / "cache", root / "project")
            ).stdout)
            bundle = Path(result["map"]).parent
            metadata = json.loads((bundle / "map.json").read_text())
            read = (bundle / "read.md").read_text()
            record_id = "snapshot:thread:11111111-1111-4111-8111-111111111111:ordinal:2"
            pin = metadata["pins"][record_id]
            self.assertEqual(metadata["context"]["input_format"], NATIVE_FORMAT)
            self.assertEqual(metadata["history"]["state"], "incomplete")
            self.assertFalse(metadata["history"]["full_history_claim"])
            self.assertEqual(pin["source_line"], 3)
            self.assertEqual(pin["native_pin"]["kind"], "snapshot_bound_rollout_ordinal")
            self.assertEqual(pin["native_pin"]["carry_forward_requires"], "validated_capture_continuity")
            self.assertIn("full_history_claim=false", read)
            self.assertIn("native_qualification=unqualified_without_isolated_operator_rollout", read)
            self.assertIn("It must not be presented as the complete conversation history.", read)

    def test_native_incomplete_history_is_not_refreshable(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache, project = root / "rollout.jsonl", root / "cache", root / "project"
            source.write_bytes(FIXTURE.read_bytes())
            first = json.loads(self.command(COLLECTOR, *self.collect_args(source, cache, project)).stdout)
            record = "snapshot:thread:11111111-1111-4111-8111-111111111111:ordinal:1"
            refreshed = json.loads(self.command(
                COLLECTOR,
                "refresh", "--source", source, "--cache", cache, "--project", project,
                "--vendor", "codex", "--vendor-version", "0.166.0",
                "--input-format", NATIVE_FORMAT, "--record", record,
            ).stdout)
            self.assertFalse(refreshed["refreshed"])
            self.assertEqual(refreshed["reason"], "carry-forward blocked: native source history is incomplete")
            self.assertEqual(refreshed["selected_snapshot"], first["selected_snapshot"])

    def test_native_format_cannot_be_used_for_an_existing_synthetic_fixture(self):
        synthetic = HERE / "fixtures" / "codex-0.166.synthetic.jsonl"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            failed = self.command(
                TRANSCRIPT, *self.render_args(synthetic, root / "cache", root / "project"), check=False
            )
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("rollout must begin with session_meta", failed.stderr)

    def native_source(self, meta_extra=None, events=None):
        meta = {
            "session_id": "root", "id": "thread", "history_mode": "legacy",
        }
        meta.update(meta_extra or {})
        rows = [{"timestamp": "t0", "type": "session_meta", "payload": meta}]
        rows.extend(events or [{"timestamp": "t1", "type": "event_msg", "payload": {"type": "user_message", "message": "hello"}}])
        return ("\n".join(json.dumps(row) for row in rows) + "\n").encode()

    def assert_native_history_marker_blocks_refresh(self, meta_extra=None, events=None, reason=None):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache, project = root / "rollout.jsonl", root / "cache", root / "project"
            source.write_bytes(self.native_source(meta_extra, events))
            first = json.loads(self.command(COLLECTOR, *self.collect_args(source, cache, project)).stdout)
            bundle = cache / "snapshots" / first["selected_snapshot"]
            metadata = json.loads((bundle / "map.json").read_text())
            self.assertEqual(metadata["history"]["state"], "incomplete")
            self.assertIn(reason, metadata["history"]["incomplete_reasons"])
            record = next(iter(metadata["pins"]))
            refreshed = json.loads(self.command(
                COLLECTOR,
                "refresh", "--source", source, "--cache", cache, "--project", project,
                "--vendor", "codex", "--vendor-version", "0.166.0",
                "--input-format", NATIVE_FORMAT,
                "--record", record,
            ).stdout)
            self.assertFalse(refreshed["refreshed"])
            self.assertEqual(refreshed["reason"], "carry-forward blocked: native source history is incomplete")

    def test_parent_thread_lineage_blocks_native_refresh(self):
        self.assert_native_history_marker_blocks_refresh({"parent_thread_id": "parent"}, reason="fork_or_history_base")

    def test_fork_ordinal_lineage_blocks_native_refresh(self):
        self.assert_native_history_marker_blocks_refresh({"forked_from_ordinal_exclusive": 2}, reason="fork_or_history_base")

    def test_subagent_history_start_blocks_native_refresh(self):
        self.assert_native_history_marker_blocks_refresh({"subagent_history_start_ordinal": 2}, reason="fork_or_history_base")

    def test_zero_ordinal_lineage_boundaries_block_refresh_but_attached_false_does_not_hide_them(self):
        self.assert_native_history_marker_blocks_refresh(
            {
                "forked_from_ordinal_exclusive": 0,
                "subagent_history_start_ordinal": 0,
                "attached_thread": False,
            },
            reason="fork_or_history_base",
        )

    def test_rollback_marker_blocks_native_refresh(self):
        events = [
            {"timestamp": "t1", "type": "event_msg", "payload": {"type": "user_message", "message": "hello"}},
            {"timestamp": "t2", "type": "event_msg", "payload": {"type": "thread_rolled_back", "num_turns": 1}},
        ]
        self.assert_native_history_marker_blocks_refresh(events=events, reason="thread_rolled_back")

    def test_unknown_native_history_mode_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "rollout.jsonl"
            source.write_bytes(self.native_source({"history_mode": "future_mode"}))
            failed = self.command(
                TRANSCRIPT, *self.render_args(source, root / "cache", root / "project"), check=False
            )
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("unsupported session_meta.history_mode", failed.stderr)

    def test_legacy_synthetic_layout_and_map_compare_as_default_format_without_rewrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "synthetic.jsonl"
            source.write_bytes(SYNTHETIC.read_bytes().rsplit(b"\n", 1)[0] + b"\n")
            module = self.transcript_module()
            legacy = {"project": str(root / "project"), "vendor": "codex", "vendor_version": "0.166.0"}
            current = {**legacy, "input_format": "synthetic-event-jsonl"}
            cache, _ = module.prepare_layout(root / "home", legacy, "bed", "session", source)
            first = module.publish(source, cache, legacy)
            legacy_map = json.loads(Path(first["map"]).read_text())
            self.assertNotIn("input_format", legacy_map["context"])
            reused_cache, _ = module.prepare_layout(root / "home", current, "bed", "session", source)
            self.assertEqual(reused_cache, cache)
            repeated = module.publish(source, cache, current)
            self.assertEqual(repeated["snapshot"], first["snapshot"])
            module.initialize_selected_snapshot(cache, first["snapshot"])
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            second = module.publish(source, cache, current)
            self.assertTrue(module.contexts_equal(legacy_map["context"], current))
            collector_spec = importlib.util.spec_from_file_location("termbrana_collector_legacy", COLLECTOR)
            collector = importlib.util.module_from_spec(collector_spec)
            assert collector_spec.loader is not None
            collector_spec.loader.exec_module(collector)
            state = collector.status(cache)
            self.assertTrue(state["new_records_available"])
            refreshed = collector.refresh(source, cache, current, "item-user-003")
            self.assertTrue(refreshed["refreshed"])
            self.assertEqual(refreshed["latest_snapshot"], second["snapshot"])


if __name__ == "__main__":
    unittest.main()
