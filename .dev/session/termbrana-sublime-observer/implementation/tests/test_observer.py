import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Region:
    def __init__(self, a, b): self.a, self.b = a, b
    def begin(self): return min(self.a, self.b)
    def end(self): return max(self.a, self.b)
    def empty(self): return self.a == self.b

class View:
    def __init__(self, ident, text, rev=0, buffer_id=30):
        self.ident, self.text, self.rev, self.buf = ident, text, rev, buffer_id
    def id(self): return self.ident
    def buffer_id(self): return self.buf
    def file_name(self): return '/tmp/synthetic.md'
    def name(self): return 'synthetic'
    def is_dirty(self): return True
    def is_loading(self): return False
    def change_count(self): return self.rev
    def size(self): return len(self.text)
    def rowcol(self, pos):
        pre = self.text[:pos]; return (pre.count('\n'), len(pre.rsplit('\n', 1)[-1]))
    def text_point(self, row, col):
        lines = self.text.splitlines(keepends=True)
        return min(sum(map(len, lines[:row])) + col, len(self.text))
    def full_line(self, point):
        start = self.text.rfind('\n', 0, point) + 1
        end = self.text.find('\n', point)
        return Region(start, len(self.text) if end < 0 else end + 1)
    def sel(self): return [Region(1, 1), Region(0, 2)]
    def visible_region(self): return Region(0, len(self.text))
    def viewport_position(self): return (1.0, 2.0)
    def viewport_extent(self): return (300.0, 400.0)
    def substr(self, region): return self.text[region.begin():region.end()]

class Window:
    def __init__(self, ident, views, active): self.ident, self._views, self.active = ident, views, active
    def id(self): return self.ident
    def folders(self): return []
    def views(self): return self._views
    def sheets(self): return []
    def active_view(self): return self.active

class ObserverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = View(11, 'αβ\nsecond\n', 3, 42)
        cls.v2 = View(12, 'different\n', 7, 42)
        cls.w1, cls.w2 = Window(1, [cls.v1], cls.v1), Window(2, [cls.v2], cls.v2)
        fake = types.ModuleType('sublime'); fake.Region = Region
        fake.windows = lambda: [cls.w1, cls.w2]
        fake.active_window = lambda: cls.w2
        sys.modules['sublime'] = fake
        sys.modules['sublime_plugin'] = types.ModuleType('sublime_plugin')
        spec = importlib.util.spec_from_file_location('observer_plugin_test', ROOT/'plugin/observer.py')
        cls.mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(cls.mod)
        cls.instance = cls.mod._INSTANCE

    def call(self, op, **fields):
        return self.mod._capture({'operation': op, 'instance': self.instance, **fields})

    def test_explicit_target_ignores_active_window_and_preserves_state(self):
        result = self.call('read', window=1, view=11)
        self.assertEqual(result['text'], 'αβ\nsecond\n')
        self.assertEqual(result['window'], 1)
        self.assertEqual(self.mod.sublime.active_window().id(), 2)
        self.assertEqual(result['viewport_position'], [1.0, 2.0])
        self.assertEqual(len(result['selections']), 2)

    def test_stale_instance_and_mismatched_view_fail(self):
        self.assertEqual(self.mod._capture({'operation':'windows','instance':'stale'})['error']['code'], 'expired_instance')
        self.assertEqual(self.call('read', window=2, view=11)['error']['code'], 'invalid_view')
        self.assertEqual(self.call('state', window=9, view=11)['error']['code'], 'invalid_window')

    def test_revision_conflict_and_unicode_line_range(self):
        self.assertEqual(self.call('read', window=1, view=11, expected_revision=2)['error']['code'], 'revision_conflict')
        result = self.call('read', window=1, view=11, start_line=1, end_line=1)
        self.assertEqual(result['text'], 'αβ\n')
        self.assertEqual(result['returned_through_line'], 1)

    def test_truncation_and_invalid_ranges(self):
        self.assertTrue(self.call('read', window=1, view=11, max_chars=2)['truncated'])
        self.assertEqual(self.call('read', window=1, view=11, start_line=5)['error']['code'], 'invalid_range')
        self.assertEqual(self.call('read', window=1, view=11, max_chars=200001)['error']['code'], 'invalid_limit')

    def test_cloned_buffer_ids_do_not_conflate_views(self):
        a = self.call('state', window=1, view=11)
        b = self.call('state', window=2, view=12)
        self.assertEqual(a['buffer'], b['buffer'])
        self.assertNotEqual(a['view'], b['view'])

    def test_cli_failures_are_structured_and_bounded(self):
        command = [sys.executable, '-I', '-S', '-B', str(ROOT/'observer.py'), '--runtime', '/tmp', 'read']
        proc = subprocess.run(command, capture_output=True, text=True, timeout=3)
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(json.loads(proc.stderr)['error']['code'], 'usage')
        command = [sys.executable, '-I', '-S', '-B', str(ROOT/'observer.py'), '--runtime', '/tmp', 'windows', '--instance', 'missing']
        proc = subprocess.run(command, capture_output=True, text=True, timeout=3)
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(json.loads(proc.stderr)['error']['code'], 'request_failed')

if __name__ == '__main__': unittest.main()
