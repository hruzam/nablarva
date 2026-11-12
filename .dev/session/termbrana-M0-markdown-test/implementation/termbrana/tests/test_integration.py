import json
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parents[1]
PROGRAM = HERE / "transcript.py"
COLLECTOR = HERE / "collector.py"
BASE = HERE / "base.zsh"
CLAUDE = HERE / "fixtures/claude-2.1.286.synthetic.jsonl"
APPROVAL = HERE / "fixtures/codex-approval.synthetic.jsonl"
CODEX = HERE / "fixtures/codex-0.166.synthetic.jsonl"


class IntegrationTest(unittest.TestCase):
    def command(self, *args, check=True):
        return subprocess.run(
            ["python3", "-I", "-S", "-B", str(PROGRAM), *map(str, args)],
            text=True, capture_output=True, check=check,
        )

    def render(self, vendor, version, source, project, cache):
        return json.loads(self.command(
            "render", "--vendor", vendor, "--vendor-version", version,
            "--project", project, "--source", source, "--out", cache,
        ).stdout)

    def collector(self, *args):
        return json.loads(subprocess.run(
            ["python3", "-I", "-S", "-B", str(COLLECTOR), *map(str, args)],
            text=True, capture_output=True, check=True,
        ).stdout)

    def module(self):
        spec = importlib.util.spec_from_file_location("integration_transcript", PROGRAM)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_claude_bundle_keeps_uuid_offsets_and_unqualified_semantics(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, project, cache = root / "claude.jsonl", root / "project", root / "cache"
            project.mkdir()
            source.write_bytes(CLAUDE.read_bytes())
            result = self.render("claude-code", "2.1.286", source, project, cache)
            metadata = json.loads(Path(result["map"]).read_text())
            body = Path(result["read"]).read_text()
            pin = metadata["pins"]["claude-user-004"]
            self.assertEqual(metadata["context"]["project"], str(project.resolve()))
            self.assertEqual(metadata["identity"]["branch_id"], "unqualified")
            self.assertEqual(pin["source_offset"], CLAUDE.read_bytes().find(b'{"type":"user","uuid":"claude-user-004"'))
            self.assertIn("duplicate_representation", body)
            self.assertIn("approval outcome unknown", body)
            selector = json.loads(self.command("select", "--cache", cache).stdout)
            self.assertEqual(selector["entries"][2]["record"], "claude-user-004")
            self.assertEqual(selector["entries"][2]["role"], "user")
            self.assertEqual(selector["entries"][2]["snippet"], "Show me the selected exchange.")

    def test_approval_reference_points_to_retained_source_after_original_loss(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, project, cache = root / "approval.jsonl", root / "project", root / "cache"
            project.mkdir()
            source.write_bytes(APPROVAL.read_bytes())
            result = self.render("codex", "0.166.0", source, project, cache)
            source.unlink()
            metadata = json.loads(Path(result["map"]).read_text())
            body = Path(result["read"]).read_text()
            reference = metadata["approval_references"][0]
            cached_source = Path(result["map"]).parent / "source.jsonl"
            self.assertEqual(reference["id"], "approval-demo-1")
            self.assertTrue(cached_source.is_file())
            self.assertIn(f"cached source: {cached_source}:2", body)
            self.assertIn("outcome: unknown; historical record only, not a live pending approval.", body)
            self.assertIn(str(source.resolve()), body)
            self.assertEqual(self.module().rebuild_bundle(Path(result["map"]).parent), Path(result["read"]).read_bytes())

    def test_read_commands_stay_on_selected_snapshot_until_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, project, cache = root / "source.jsonl", root / "project", root / "cache"
            project.mkdir()
            raw = CODEX.read_bytes()
            source.write_bytes(raw[:raw.rfind(b"\n") + 1])
            first = self.collector("collect", "--source", source, "--cache", cache, "--project", project, "--vendor", "codex", "--vendor-version", "0.166.0")
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            second = self.collector("collect", "--source", source, "--cache", cache, "--project", project, "--vendor", "codex", "--vendor-version", "0.166.0")
            self.assertNotEqual(first["selected_snapshot"], second["latest_snapshot"])
            selected = json.loads(self.command("select", "--cache", cache).stdout)
            latest = json.loads(self.command("select", "--cache", cache, "--snapshot", second["latest_snapshot"]).stdout)
            selected_pin = json.loads(self.command("pin", "--cache", cache, "--record", "item-user-003").stdout)
            self.assertEqual(selected["snapshot"], first["selected_snapshot"])
            self.assertEqual(selected_pin["snapshot"], first["selected_snapshot"])
            self.assertEqual(latest["snapshot"], second["latest_snapshot"])
            self.assertEqual(len(selected["entries"]), 4)
            self.assertEqual(len(latest["entries"]), 5)

    def test_claude_omitted_content_is_disclosed_in_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, project, cache = root / "claude.jsonl", root / "project", root / "cache"
            project.mkdir()
            source.write_bytes(CLAUDE.read_bytes().replace(
                b'{"type":"text","text":"A multiline response follows:',
                b'{"type":"image","url":"synthetic"},{"type":"text","text":"A multiline response follows:',
                1,
            ))
            result = self.render("claude-code", "2.1.286", source, project, cache)
            metadata = json.loads(Path(result["map"]).read_text())
            body = Path(result["read"]).read_text()
            disclosure = next(item for item in metadata["unsupported"] if item["kind"] == "omitted_content")
            self.assertEqual(disclosure["uuid"], "claude-assistant-002")
            self.assertEqual(disclosure["types"], ["image"])
            self.assertIn("claude-assistant-002 · omitted_content", body)

    def test_shell_surface_is_quiet_and_exposes_explicit_commands(self):
        run = subprocess.run(
            ["zsh", "-f", "-c", 'source "$1"; source "$1"; whence -w _tbv_select _tbv_open _tbv_collect _tbv_refresh _tbv_watch', "tbv", str(BASE)],
            text=True, capture_output=True, check=True,
        )
        self.assertIn("_tbv_open: function", run.stdout)
        self.assertIn("_tbv_collect: function", run.stdout)
        self.assertEqual(run.stderr, "")


if __name__ == "__main__":
    unittest.main()
