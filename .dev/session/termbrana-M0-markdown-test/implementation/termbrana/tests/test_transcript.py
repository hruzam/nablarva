import json
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parents[1]
FIXTURE = HERE / "fixtures/codex-0.166.synthetic.jsonl"
PROGRAM = HERE / "transcript.py"


class TranscriptTest(unittest.TestCase):
    def command(self, *args, check=True):
        return subprocess.run(["python3", "-I", "-S", "-B", str(PROGRAM), *map(str, args)], text=True, capture_output=True, check=check)

    def render(self, source, cache, project=None):
        project = project or Path(source).parent
        return json.loads(self.command(
            "render", "--vendor", "codex", "--vendor-version", "0.166.0",
            "--project", project, "--source", source, "--out", cache,
        ).stdout)

    def complete_fixture(self):
        raw = FIXTURE.read_bytes()
        return raw[:raw.rfind(b"\n") + 1]

    def module(self):
        spec = importlib.util.spec_from_file_location("stage1_transcript", PROGRAM)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_frozen_conversation_creates_immutable_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = self.render(FIXTURE, root / "cache")
            bundle = root / "cache" / "snapshots" / result["snapshot"]
            body = (bundle / "read.md").read_text()
            metadata = json.loads((bundle / "map.json").read_text())
            self.assertEqual(result["records"], 4)
            self.assertEqual((bundle / "source.jsonl").read_bytes(), self.complete_fixture())
            self.assertEqual(metadata["context"]["vendor_version"], "0.166.0")
            self.assertEqual(body.count("Please show the selected exchange."), 2)
            self.assertIn("```python\nprint('hello')\n```", body)
            self.assertIn("item-unknown-006 · future_vendor_event", body)
            self.assertNotIn("Deferred incomplete final record", body)
            self.assertTrue(metadata["capture_state"]["deferred_incomplete_tail"])
            self.assertEqual(metadata["pins"]["item-user-003"]["markdown_line"], body.splitlines().index("## 3. user · 2026-11-05T20:01:00Z · item-user-003") + 1)

    def test_cold_rebuild_uses_retained_source_not_dropped_tail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(FIXTURE.read_bytes())
            result = self.render(source, cache, root / "project")
            source.unlink()
            bundle = Path(result["map"]).parent
            rebuilt = self.module().rebuild_bundle(bundle)
            self.assertEqual(rebuilt, (bundle / "read.md").read_bytes())

    def test_snapshot_pin_survives_original_source_loss(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(FIXTURE.read_bytes())
            result = self.render(source, cache)
            source.unlink()
            pin = json.loads(self.command("pin", "--cache", cache, "--snapshot", result["snapshot"], "--record", "item-user-003").stdout)
            self.assertEqual(pin["source_record_id"], "item-user-003")
            self.assertTrue(Path(pin["read"]).is_file())

    def test_carry_forward_accepts_append_and_blocks_observable_discontinuities(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache = root / "source.jsonl", root / "cache"
            source.write_bytes(self.complete_fixture())
            result = self.render(source, cache)
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            carried = json.loads(self.command("carry-forward", "--source", source, "--cache", cache, "--snapshot", result["snapshot"]).stdout)
            self.assertTrue(carried["carry_forward"])
            source.write_bytes(b"short\n")
            shortened = self.command("carry-forward", "--source", source, "--cache", cache, "--snapshot", result["snapshot"], check=False)
            self.assertIn("source shortened", shortened.stderr)
            source.write_bytes(self.complete_fixture().replace(b"selected exchange", b"altered  exchange", 1))
            mutated = self.command("carry-forward", "--source", source, "--cache", cache, "--snapshot", result["snapshot"], check=False)
            self.assertIn("captured prefix changed", mutated.stderr)
            replacement = root / "replacement.jsonl"
            replacement.write_bytes(self.complete_fixture())
            os.replace(replacement, source)
            replaced = self.command("carry-forward", "--source", source, "--cache", cache, "--snapshot", result["snapshot"], check=False)
            self.assertIn("source identity changed", replaced.stderr)

    def test_pointer_resolves_complete_bundle_and_ignores_staging(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cache = root / "cache"
            first = self.render(FIXTURE, cache)
            (cache / "snapshots" / ".staging-interrupted").mkdir()
            second = self.render(FIXTURE, cache)
            self.assertEqual(first["snapshot"], second["snapshot"])
            current = json.loads((cache / "current.json").read_text())
            self.assertEqual(current["snapshot"], first["snapshot"])
            pin = self.command("pin", "--cache", cache, "--record", "item-user-001")
            self.assertIn(first["snapshot"], pin.stdout)

    def test_distinct_capture_contexts_and_partial_state_never_collide(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cache = root / "cache"
            left, right = root / "left", root / "right"
            left.mkdir()
            right.mkdir()
            left_source, right_source = left / "source.jsonl", right / "source.jsonl"
            left_source.write_bytes(self.complete_fixture())
            right_source.write_bytes(self.complete_fixture())
            first = self.render(left_source, cache, left)
            repeat = self.render(left_source, cache, left)
            other = self.render(right_source, cache, right)
            self.assertEqual(first["snapshot"], repeat["snapshot"])
            self.assertNotEqual(first["snapshot"], other["snapshot"])
            left_source.write_bytes(FIXTURE.read_bytes())
            partial = self.render(left_source, cache, left)
            self.assertNotEqual(first["snapshot"], partial["snapshot"])
            partial_map = json.loads(Path(partial["map"]).read_text())
            self.assertTrue(partial_map["deferred_partial_final_line"])

    def test_concurrent_publishers_leave_a_complete_current_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cache = root / "cache"
            sources = []
            for name in ("one", "two"):
                project = root / name
                project.mkdir()
                source = project / "source.jsonl"
                source.write_bytes(FIXTURE.read_bytes())
                sources.append((project, source))
            commands = [
                ["python3", "-I", "-S", "-B", str(PROGRAM), "render", "--vendor", "codex", "--vendor-version", "0.166.0", "--project", str(project), "--source", str(source), "--out", str(cache)]
                for project, source in sources
            ]
            processes = [subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) for command in commands]
            results = [process.communicate() for process in processes]
            self.assertTrue(all(process.returncode == 0 for process in processes), results)
            current = json.loads((cache / "current.json").read_text())
            bundle = cache / "snapshots" / current["snapshot"]
            metadata = json.loads((bundle / "map.json").read_text())
            self.assertEqual((bundle / "read.md").read_bytes().__len__(), metadata["files"]["read.md"]["bytes"])

    def test_interrupted_before_pointer_preserves_previous_snapshot(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, cache, project = root / "source.jsonl", root / "cache", root / "project"
            project.mkdir()
            source.write_bytes(self.complete_fixture())
            first = self.render(source, cache, project)
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            module = self.module()
            context = {"project": str(project.resolve()), "vendor": "codex", "vendor_version": "0.166.0"}
            with mock.patch.object(module, "atomic_write", side_effect=OSError("interrupted")):
                with self.assertRaises(OSError):
                    module.publish(source, cache, context)
            current = json.loads((cache / "current.json").read_text())
            self.assertEqual(current["snapshot"], first["snapshot"])
            pin = self.command("pin", "--cache", cache, "--record", "item-user-001")
            self.assertIn(first["snapshot"], pin.stdout)

    def test_cache_cannot_alias_source_or_ancestor(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.jsonl"
            source.write_bytes(FIXTURE.read_bytes())
            same = self.command("render", "--vendor", "codex", "--vendor-version", "0.166.0", "--project", root, "--source", source, "--out", source, check=False)
            self.assertIn("cache must not", same.stderr)
            ancestor = self.command("render", "--vendor", "codex", "--vendor-version", "0.166.0", "--project", root, "--source", source, "--out", root, check=False)
            self.assertIn("cache must not", ancestor.stderr)

    def test_complete_malformed_line_and_duplicate_identity_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            malformed = root / "bad.jsonl"
            malformed.write_bytes(FIXTURE.read_bytes().replace(b'{"timestamp":"2026-11-05T20:01:06Z"', b"{bad\n", 1))
            bad = self.command("render", "--vendor", "codex", "--vendor-version", "0.166.0", "--project", root, "--source", malformed, "--out", root / "bad-cache", check=False)
            self.assertIn("malformed complete JSONL", bad.stderr)
            duplicate = root / "duplicate.jsonl"
            duplicate.write_bytes(FIXTURE.read_bytes().replace(b"item-user-003", b"item-user-001"))
            duplicate_run = self.command("render", "--vendor", "codex", "--vendor-version", "0.166.0", "--project", root, "--source", duplicate, "--out", root / "duplicate-cache", check=False)
            self.assertIn("duplicate source record identity", duplicate_run.stderr)

    def test_duplicate_after_long_unique_prefix_preserves_order_and_error(self):
        module = self.module()
        ids = [f"unique-{i}" for i in range(300)]
        lines = [json.dumps({"type": "event_msg", "payload": {
            "type": "user_message", "id": record_id, "message": "same body",
            "thread_id": "thread", "session_id": "session", "branch_id": "main",
        }}).encode() + b"\n" for record_id in ids]
        records, _, _, _, _ = module.load_codex(b"".join(lines))
        self.assertEqual([record["id"] for record in records], ids)
        with self.assertRaises(module.SourceError) as raised:
            module.load_codex(b"".join(lines + [lines[0]]))
        self.assertEqual(str(raised.exception), "duplicate source record identity at line 301: unique-0")


if __name__ == "__main__":
    unittest.main()
