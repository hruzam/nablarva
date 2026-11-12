import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "codex_native.py"
FIXTURE = ROOT / "fixtures" / "codex-native-source-derived.jsonl"

spec = importlib.util.spec_from_file_location("codex_native", ADAPTER_PATH)
adapter = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(adapter)


class CodexNativeTests(unittest.TestCase):
    def test_source_derived_fixture_preserves_native_identity_and_pins(self):
        parsed = adapter.parse(FIXTURE.read_bytes())
        thread_id = "11111111-1111-4111-8111-111111111111"
        self.assertEqual(parsed["identity"]["thread_id"], thread_id)
        self.assertEqual(parsed["identity"]["session_id"], thread_id)
        self.assertEqual(parsed["identity"]["history_mode"], "paginated")
        self.assertEqual([item["role"] for item in parsed["exchanges"]], ["user", "assistant"])
        self.assertEqual(parsed["exchanges"][0]["body"], "Summarize this fixture.")
        self.assertEqual(parsed["exchanges"][1]["pin"]["ordinal"], 2)
        pin = parsed["exchanges"][1]["pin"]
        self.assertEqual(parsed["exchanges"][1]["id"], f"snapshot:thread:{thread_id}:ordinal:2")
        self.assertEqual(pin["kind"], "snapshot_bound_rollout_ordinal")
        self.assertTrue(pin["snapshot_bound"])
        self.assertEqual(pin["carry_forward_requires"], "validated_capture_continuity")
        self.assertFalse(parsed["deferred_partial"])
        self.assertEqual(parsed["native_qualification"], "unqualified_without_isolated_operator_rollout")

    def test_unsupported_duplicate_and_compaction_stay_visible(self):
        disclosures = adapter.parse(FIXTURE.read_bytes())["disclosures"]
        self.assertEqual(
            [item["kind"] for item in disclosures],
            ["potential_duplicate_representation", "context_compaction", "unsupported_event"],
        )
        self.assertEqual(disclosures[0]["response_item_type"], "message")
        self.assertEqual(disclosures[1]["pin"]["kind"], "snapshot_bound_rollout_ordinal")

    def test_legacy_positions_are_explicitly_snapshot_relative(self):
        data = (
            b'{"timestamp":"t0","type":"session_meta","payload":{"id":"thread","session_id":"session","history_mode":"legacy"}}\n'
            b'{"timestamp":"t1","type":"event_msg","payload":{"type":"user_message","message":"hello"}}\n'
        )
        parsed = adapter.parse(data)
        pin = parsed["exchanges"][0]["pin"]
        self.assertEqual(pin["kind"], "snapshot_relative_position")
        self.assertTrue(pin["snapshot_relative"])
        self.assertEqual(pin["carry_forward_requires"], "validated_capture_continuity")
        self.assertNotIn("branch_id", parsed["identity"])

    def test_paginated_record_without_ordinal_is_rejected(self):
        data = (
            b'{"timestamp":"t0","ordinal":0,"type":"session_meta","payload":{"id":"thread","session_id":"session","history_mode":"paginated"}}\n'
            b'{"timestamp":"t1","type":"event_msg","payload":{"type":"user_message","message":"hello"}}\n'
        )
        with self.assertRaisesRegex(adapter.SourceError, "missing ordinal"):
            adapter.parse(data)

    def test_unterminated_final_line_is_deferred(self):
        data = (
            b'{"timestamp":"t0","type":"session_meta","payload":{"id":"thread","session_id":"session","history_mode":"legacy"}}\n'
            b'{"timestamp":"t1","type":"event_msg","payload":{"type":"user_message","message":"hello"}}\n'
            b'{"timestamp":"unfinished"'
        )
        parsed = adapter.parse(data)
        self.assertTrue(parsed["deferred_partial"])
        self.assertEqual(parsed["disclosures"][-1]["kind"], "incomplete_final_line")

    def test_fork_lineage_is_disclosed_without_merging_other_history(self):
        meta = {"id": "child", "session_id": "root", "history_mode": "legacy", "forked_from_id": "parent", "history_base": {"thread_id": "parent", "end_ordinal_exclusive": 2, "end_byte_offset": 99}}
        data = "\n".join((
            json.dumps({"timestamp": "t0", "type": "session_meta", "payload": meta}),
            json.dumps({"timestamp": "t1", "type": "event_msg", "payload": {"type": "user_message", "message": "child only"}}),
            "",
        )).encode()
        disclosure = adapter.parse(data)["disclosures"][-1]
        self.assertEqual(disclosure["kind"], "fork_or_history_base")
        self.assertEqual(disclosure["forked_from_id"], "parent")


if __name__ == "__main__":
    unittest.main()
