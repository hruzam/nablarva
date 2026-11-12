import importlib.util
from pathlib import Path
import unittest


HERE = Path(__file__).resolve().parents[1]
FIXTURE = HERE / "fixtures/claude-2.1.286.synthetic.jsonl"
SPEC = importlib.util.spec_from_file_location("claude_adapter", HERE / "claude_adapter.py")
ADAPTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ADAPTER)


class ClaudeAdapterTest(unittest.TestCase):
    def test_frozen_main_line_and_disclosures(self):
        result = ADAPTER.parse(FIXTURE.read_bytes())
        self.assertEqual(result["native_schema"], "unqualified")
        self.assertEqual([item["uuid"] for item in result["exchanges"]], ["claude-user-001", "claude-assistant-002", "claude-user-004", "claude-assistant-005"])
        self.assertIn("```text\nline one\nline two\n```", result["exchanges"][1]["body"])
        self.assertEqual(result["exchanges"][0]["body"], result["exchanges"][2]["body"])
        disclosures = {item["kind"]: item for item in result["disclosures"]}
        self.assertEqual(disclosures["duplicate_representation"]["source_uuid"], "claude-user-001")
        self.assertEqual(disclosures["permission_mode"]["approval_outcome"], "unknown")
        self.assertEqual(disclosures["alternate_branch"]["main_line_resolution"], "refused")
        self.assertEqual(result["exchanges"][1]["omitted_content"], [])

    def test_duplicate_uuid_and_malformed_records_fail(self):
        duplicate = FIXTURE.read_bytes().replace(b"claude-user-004", b"claude-user-001", 1)
        with self.assertRaisesRegex(ADAPTER.SourceError, "duplicate source UUID"):
            ADAPTER.parse(duplicate)
        with self.assertRaisesRegex(ADAPTER.SourceError, "malformed complete JSONL"):
            ADAPTER.parse(FIXTURE.read_bytes() + b"{bad}\n")

    def test_incomplete_tail_and_non_text_content_are_disclosed(self):
        incomplete = ADAPTER.parse(FIXTURE.read_bytes() + b'{"type":"user"')
        self.assertEqual(incomplete["disclosures"][-1]["kind"], "incomplete_final_line")
        mixed = FIXTURE.read_bytes().replace(
            b'{"type":"text","text":"A multiline response follows:',
            b'{"type":"image","url":"synthetic"},{"type":"text","text":"A multiline response follows:',
            1,
        )
        result = ADAPTER.parse(mixed)
        self.assertEqual(result["exchanges"][1]["omitted_content"], ["image"])

    def test_invalid_utf8_complete_record_fails_but_partial_tail_is_deferred(self):
        complete = FIXTURE.read_bytes()
        line_number = len(complete.splitlines()) + 1
        malformed = b'{"invalid":"\xff"}'
        with self.assertRaisesRegex(ADAPTER.SourceError, f"invalid UTF-8 in complete JSONL record at line {line_number}"):
            ADAPTER.parse(complete + malformed + b"\n")
        baseline = ADAPTER.parse(complete)
        partial = ADAPTER.parse(complete + malformed)
        self.assertEqual(partial["exchanges"], baseline["exchanges"])
        self.assertEqual(partial["disclosures"][-1], {"kind": "incomplete_final_line", "line": line_number})


if __name__ == "__main__":
    unittest.main()
