import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures/claude-native-2.1.323.jsonl"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


adapter = load("claude_adapter")
transcript = load("transcript")
collector = load("collector")


class ClaudeNativeTests(unittest.TestCase):
    def rows(self):
        return [json.loads(line) for line in FIXTURE.read_text().splitlines()]

    def encode(self, rows):
        return ("\n".join(json.dumps(row) for row in rows) + "\n").encode()

    def context(self):
        return {"vendor": "claude-code", "vendor_version": "2.1.323",
                "input_format": "claude-jsonl-2.1.323", "project": "/synthetic/claude-project"}

    def test_frozen_text_and_attachment_ancestry(self):
        result = adapter.parse_native(FIXTURE.read_bytes())
        self.assertEqual([x["uuid"] for x in result["exchanges"]], ["fictional-user-1", "fictional-assistant-1"])
        self.assertEqual([x["source_line"] for x in result["exchanges"]], [3, 7])
        self.assertEqual(result["exchanges"][0]["body"], "Please show the selected exchange.")
        self.assertEqual(result["exchanges"][1]["body"], "A multiline response:\n```text\nline one\nline two\n```")
        self.assertEqual(result["vendor_version"], "2.1.323")
        self.assertEqual(result["complete_bytes"], len(FIXTURE.read_bytes()))
        self.assertEqual({x["type"]: x["count"] for x in result["disclosures"]}["attachment"], 2)

    def test_render_omits_api_and_attachment_payloads(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = transcript.publish(FIXTURE, Path(temporary) / "cache", self.context())
            text = Path(result["read"]).read_text()
            metadata = json.loads(Path(result["map"]).read_text())
            self.assertNotIn("This nested representation must never render.", text)
            self.assertNotIn("invented omitted context", text)
            self.assertIn("api-request-blob · count=1", text)
            self.assertEqual(metadata["history"]["state"], "snapshot_only")
            self.assertFalse(metadata["history"]["full_history_claim"])
            self.assertEqual(metadata["identity"]["producer_version"], "2.1.323")
            self.assertEqual(list(metadata["pins"]), ["fictional-assistant-1", "fictional-user-1"])

    def test_identity_and_version_fail_closed(self):
        for change in ({"sessionId": "other"}, {"cwd": "/other"}, {"version": "2.1.324"},
                       {"session_id": "other"}, {"isSidechain": True}, {"timestamp": None}):
            rows = self.rows()
            rows[6].update(change)
            with self.subTest(change=change), self.assertRaises(adapter.SourceError):
                adapter.parse_native(self.encode(rows))
        rows = self.rows()
        del rows[3]["version"]
        with self.assertRaisesRegex(adapter.SourceError, "identity or version"):
            adapter.parse_native(self.encode(rows))

    def test_missing_cyclic_duplicate_and_competing_parents_fail(self):
        for index, change in ((3, {"parentUuid": "missing"}),
                              (3, {"parentUuid": "fictional-attachment-1"}),
                              (6, {"uuid": "fictional-user-1"}),
                              (6, {"parentUuid": None})):
            rows = self.rows()
            rows[index].update(change)
            with self.subTest(index=index, change=change), self.assertRaises(adapter.SourceError):
                adapter.parse_native(self.encode(rows))

    def test_compaction_tools_and_unknown_ancestry_fail(self):
        for mutate in (
            lambda rows: rows[7].update(subtype="compact_boundary"),
            lambda rows: rows[3]["attachment"].update(type="unqualified_attachment"),
            lambda rows: rows[6]["message"].update(stop_reason="tool_use"),
            lambda rows: rows[2]["message"].update(content=[{"type": "tool_result", "content": "secret"}]),
            lambda rows: rows[2].update(isCompactSummary=True),
        ):
            rows = self.rows()
            mutate(rows)
            with self.assertRaises(adapter.SourceError):
                adapter.parse_native(self.encode(rows))

    def test_omitted_metadata_cannot_hide_sidechain_or_compaction_flags(self):
        for field in ("isSidechain", "isMeta", "isCompactSummary"):
            rows = self.rows()
            rows[4][field] = True
            with self.subTest(field=field), self.assertRaisesRegex(adapter.SourceError, "sidechain or compacted"):
                adapter.parse_native(self.encode(rows))

    def test_every_attachment_and_system_node_must_extend_the_main_chain(self):
        for template in (3, 7):
            rows = self.rows()
            detached = copy.deepcopy(rows[template])
            detached.update(uuid="fictional-detached", parentUuid="fictional-user-1")
            rows.append(detached)
            with self.subTest(template=template), self.assertRaisesRegex(adapter.SourceError, "competing ancestry"):
                adapter.parse_native(self.encode(rows))
        rows = self.rows()
        sibling = copy.deepcopy(rows[3])
        sibling.update(uuid="fictional-sibling")
        rows.insert(4, sibling)
        with self.assertRaisesRegex(adapter.SourceError, "competing ancestry"):
            adapter.parse_native(self.encode(rows))

    def test_completed_utf8_error_is_redacted_and_partial_is_deferred(self):
        malformed = b'{"type":"user","private_marker":"\\x41\xff"}'
        with self.assertRaises(adapter.SourceError) as failure:
            adapter.parse_native(FIXTURE.read_bytes() + malformed + b"\n")
        self.assertIn("line 10", str(failure.exception))
        self.assertNotIn("private_marker", str(failure.exception))
        partial = adapter.parse_native(FIXTURE.read_bytes() + malformed)
        self.assertEqual(len(partial["exchanges"]), 2)
        self.assertTrue(partial["deferred_partial"])
        self.assertEqual(partial["complete_bytes"], len(FIXTURE.read_bytes()))

    def test_native_format_and_project_are_explicit(self):
        with self.assertRaises(adapter.SourceError):
            adapter.parse(FIXTURE.read_bytes())
        for field, value in (("vendor_version", "2.1.286"), ("project", "/other")):
            context = self.context()
            context[field] = value
            with self.subTest(field=field), self.assertRaises(transcript.SourceError):
                transcript.inspect_source(FIXTURE, context)

    def test_append_preserves_identity_and_refreshes_only_explicitly(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "source.jsonl"
            source.write_bytes(FIXTURE.read_bytes())
            cache = folder / "cache"
            first = collector.collect_once(source, cache, self.context())
            rows = self.rows()
            new_user = copy.deepcopy(rows[2])
            new_user.update(uuid="fictional-user-2", parentUuid="fictional-duration-1")
            with source.open("ab") as handle:
                handle.write(self.encode([new_user]))
            second = collector.collect_once(source, cache, self.context())
            self.assertEqual(second["selected_snapshot"], first["selected_snapshot"])
            self.assertTrue(second["new_records_available"])
            result = collector.refresh(source, cache, self.context(), "fictional-user-1")
            self.assertTrue(result["refreshed"])
            self.assertTrue(result["carry_forward"])
            self.assertEqual(result["selected_records"], 3)

    def test_standalone_and_collector_cli_accept_only_native_opt_in(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            common = ["--vendor", "claude-code", "--vendor-version", "2.1.323",
                      "--input-format", "claude-jsonl-2.1.323", "--project", "/synthetic/claude-project",
                      "--source", str(FIXTURE)]
            for program, command, output_arg in (("transcript.py", "render", "--out"),
                                                  ("collector.py", "collect", "--cache")):
                result = subprocess.run(["python3", "-I", "-S", "-B", str(ROOT / program), command,
                                         *common, output_arg, str(folder / program)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                data = json.loads(result.stdout)
                self.assertEqual(data.get("records", data.get("latest_records")), 2)


if __name__ == "__main__":
    unittest.main()
