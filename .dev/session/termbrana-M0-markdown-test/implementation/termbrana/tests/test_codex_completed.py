import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


adapter = load("codex_native")
transcript = load("transcript")
FIXTURE = ROOT / "fixtures/codex-native-0.167.jsonl"


class CompletedItemsTests(unittest.TestCase):
    def rows(self):
        return [json.loads(line) for line in FIXTURE.read_text().splitlines()]

    def encode(self, rows):
        return ("\n".join(json.dumps(row) for row in rows) + "\n").encode()

    def parse(self, rows=None):
        return adapter.parse(FIXTURE.read_bytes() if rows is None else self.encode(rows), "0.167.0")

    def test_frozen_completed_subset_and_duplicate_identity(self):
        result = self.parse()
        self.assertEqual([x["role"] for x in result["exchanges"]], ["user", "assistant", "user"])
        self.assertEqual([x["pin"]["native_item_id"] for x in result["exchanges"]], ["u-one", "a-one", "u-two"])
        self.assertEqual(result["exchanges"][0]["body"], result["exchanges"][2]["body"])
        self.assertEqual(result["exchanges"][1]["body"], "First line.\n\n```python\nprint('fixture')\n```")
        kinds = [x["kind"] for x in result["disclosures"]]
        self.assertIn("duplicate_completed_item", kinds)
        self.assertIn("omitted_content", kinds)
        self.assertIn("context_compaction", kinds)
        self.assertEqual(result["vendor_version"], "0.167.0")
        self.assertEqual(result["adapter_contract"], "0.167.0-source-derived")

    def test_version_mismatch_missing_version_and_wrong_format_rejected(self):
        with self.assertRaisesRegex(adapter.SourceError, "version"):
            adapter.parse(FIXTURE.read_bytes())
        for version in (None, "0.168.0"):
            rows = self.rows()
            rows[0]["payload"]["cli_version"] = version
            with self.assertRaisesRegex(adapter.SourceError, "version"):
                self.parse(rows)

    def test_bad_message_identity_and_shapes_rejected(self):
        for mutate in (
            lambda p: p.update(thread_id="other"),
            lambda p: p.pop("turn_id"),
            lambda p: p["item"].pop("id"),
            lambda p: p["item"]["content"][0].update(text=42),
        ):
            rows = self.rows()
            mutate(rows[1]["payload"])
            with self.assertRaises(adapter.SourceError):
                self.parse(rows)

    def test_conflicting_completed_id_rejected_and_partial_tail_deferred(self):
        rows = self.rows()
        rows[5]["payload"]["item"]["content"][0]["text"] = "conflict"
        with self.assertRaisesRegex(adapter.SourceError, "conflicting completed item"):
            self.parse(rows)
        parsed = adapter.parse(FIXTURE.read_bytes() + b'{"unfinished":', "0.167.0")
        self.assertTrue(parsed["deferred_partial"])

    def test_renderer_records_producer_and_blocks_compacted_refresh(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            context = {"project": str(root), "vendor": "codex", "vendor_version": "0.167.0", "input_format": "codex-rollout-0.167"}
            output = transcript.publish(FIXTURE, root / "cache", context)
            metadata = json.loads(Path(output["map"]).read_text())
            self.assertEqual(metadata["identity"]["producer_version"], "0.167.0")
            self.assertFalse(metadata["history"]["carry_forward_allowed"])
            self.assertFalse(metadata["history"]["full_history_claim"])
            context["vendor_version"] = "0.166.0"
            with self.assertRaisesRegex(transcript.SourceError, "vendor version"):
                transcript.inspect_source(FIXTURE, context)

    def test_explicit_cli_format_is_supported_by_renderer_and_collector(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            common = ["--source", str(FIXTURE), "--vendor", "codex", "--vendor-version", "0.167.0",
                      "--input-format", "codex-rollout-0.167", "--project", str(root)]
            rendered = subprocess.run(["python3", "-I", "-S", "-B", str(ROOT / "transcript.py"), "render",
                                       *common, "--out", str(root / "render")], capture_output=True, text=True)
            self.assertEqual(rendered.returncode, 0, rendered.stderr)
            self.assertEqual(json.loads(rendered.stdout)["records"], 3)
            collected = subprocess.run(["python3", "-I", "-S", "-B", str(ROOT / "collector.py"), "collect",
                                        *common, "--cache", str(root / "collect")], capture_output=True, text=True)
            self.assertEqual(collected.returncode, 0, collected.stderr)
            self.assertEqual(json.loads(collected.stdout)["latest_records"], 3)


if __name__ == "__main__":
    unittest.main()
