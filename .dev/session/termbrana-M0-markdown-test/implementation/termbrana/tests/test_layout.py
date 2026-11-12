import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parents[1]
PROGRAM = HERE / "transcript.py"
FIXTURE = HERE / "fixtures/codex-0.166.synthetic.jsonl"


class LayoutTest(unittest.TestCase):
    def command(self, *args, check=True):
        return subprocess.run(
            ["python3", "-I", "-S", "-B", str(PROGRAM), *map(str, args)],
            text=True, capture_output=True, check=check,
        )

    def module(self):
        spec = importlib.util.spec_from_file_location("layout_transcript", PROGRAM)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def complete_fixture(self):
        raw = FIXTURE.read_bytes()
        return raw[:raw.rfind(b"\n") + 1]

    def render_layout(self, source, project, home, version="0.166.0"):
        return json.loads(self.command(
            "render", "--vendor", "codex", "--vendor-version", version,
            "--project", project, "--source", source, "--home", home,
            "--bed", "termbrana-M0-markdown-test", "--agentive-session", "session-001",
        ).stdout)

    def test_layout_uses_collision_resistant_project_slug_and_identity_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home = root / "runtime-home"
            one, two = root / "one" / "same-name", root / "two" / "same-name"
            one.mkdir(parents=True)
            two.mkdir(parents=True)
            source_one, source_two = one / "source.jsonl", two / "source.jsonl"
            source_one.write_bytes(self.complete_fixture())
            source_two.write_bytes(self.complete_fixture())
            first = self.render_layout(source_one, one, home)
            second = self.render_layout(source_two, two, home)
            first_cache, second_cache = Path(first["cache"]), Path(second["cache"])
            self.assertNotEqual(first_cache, second_cache)
            self.assertEqual(first_cache.name, "cache.session-001")
            self.assertEqual(first_cache.parent.name, "termbrana-M0-markdown-test")
            self.assertEqual(Path(first["reading"]).name, "read.session-001.md")
            metadata = json.loads((first_cache / "layout.json").read_text())
            self.assertEqual(metadata["project"], str(one.resolve()))
            self.assertEqual(metadata["vendor_version"], "0.166.0")
            collision = self.command(
                "render", "--vendor", "codex", "--vendor-version", "0.167.0",
                "--project", one, "--source", source_one, "--home", home,
                "--bed", "termbrana-M0-markdown-test", "--agentive-session", "session-001",
                check=False,
            )
            self.assertIn("layout cache identity collision", collision.stderr)

    def test_layout_reading_stays_selected_until_materialized_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home, project, source = root / "runtime-home", root / "project", root / "source.jsonl"
            project.mkdir()
            source.write_bytes(self.complete_fixture())
            first = self.render_layout(source, project, home)
            cache, reading = Path(first["cache"]), Path(first["reading"])
            original = reading.read_bytes()
            module = self.module()
            self.assertTrue((cache / "selected.json").is_file())
            source.write_bytes(source.read_bytes() + b'{"timestamp":"2026-11-05T20:02:00Z","type":"event_msg","payload":{"id":"item-user-008","type":"user_message","message":"new","thread_id":"thread-demo-01","session_id":"session-demo-01","branch_id":"branch-main"}}\n')
            latest = self.render_layout(source, project, home)
            self.assertEqual(reading.read_bytes(), original)
            self.assertEqual(module.materialize_selected_reading(cache), reading)
            self.assertEqual(reading.read_bytes(), original)
            latest_map = Path(latest["map"])
            module.atomic_write(
                cache / "selected.json",
                (json.dumps({"snapshot": latest["snapshot"], "map_sha256": hashlib.sha256(latest_map.read_bytes()).hexdigest()}) + "\n").encode(),
            )
            module.materialize_selected_reading(cache)
            self.assertIn(b"item-user-008", reading.read_bytes())

    def test_generated_reading_alias_is_rejected_before_layout_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home, project = root / "runtime-home", root / "project"
            project.mkdir()
            module = self.module()
            layout_root = home / module.project_slug(str(project.resolve())) / "termbrana-M0-markdown-test"
            layout_root.mkdir(parents=True)
            source = layout_root / "read.session-001.md"
            source.write_bytes(self.complete_fixture())
            run = self.command(
                "render", "--vendor", "codex", "--vendor-version", "0.166.0",
                "--project", project, "--source", source, "--home", home,
                "--bed", "termbrana-M0-markdown-test", "--agentive-session", "session-001",
                check=False,
            )
            self.assertIn("generated layout path aliases the input source", run.stderr)
            self.assertFalse((layout_root / "cache.session-001").exists())


if __name__ == "__main__":
    unittest.main()
