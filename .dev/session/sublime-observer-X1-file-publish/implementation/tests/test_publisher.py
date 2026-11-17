import contextlib
import io
import json
import os
import tempfile
import unittest

import fakes
import reader


def load(path):
    with open(path, 'rb') as handle:
        return json.loads(handle.read().decode('utf-8'))


class PluginBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='sublime-observer-plugin-')
        self.addCleanup(self.tmp.cleanup)
        os.chmod(self.tmp.name, 0o700)
        self.root = os.path.join(self.tmp.name, 'sublime-observer')
        self.clock = fakes.Clock()
        self.mod, self.sub = fakes.install(self.clock, {'root': self.root})
        self.window = fakes.Window(1)
        self.rt = self.runtime()
        self.assertTrue(self.rt.start())
        self.mod._RT = self.rt
        self.addCleanup(self.teardown_runtime)
        self.listener = self.mod.SublimeObserverListener()
        self.publishes = []
        original = self.rt.store.publish

        def counting(share_id, capture):
            self.publishes.append((self.clock.now, capture.get('revision'), capture.get('text') is not None))
            return original(share_id, capture)
        self.rt.store.publish = counting

    def runtime(self, **kw):
        settings = self.mod.read_settings(self.sub.load_settings('x').get)
        return self.mod._Runtime(settings, clock=self.clock, wall=self.clock,
                                 writer_factory=fakes.SyncWriter, **kw)

    def teardown_runtime(self):
        if self.mod._RT is not None:
            self.mod.plugin_unloaded()

    def view(self, ident=11, text='alpha\nbeta\n', path='/tmp/synthetic-observer.md'):
        v = fakes.View(ident, text, path, self.window)
        return v

    def toggle(self, view):
        self.window.active = view
        self.mod.SublimeObserverToggleShareCommand(self.window).run()

    def share_id(self, view):
        return self.rt.shares[view.id()].share_id

    def vdir(self, share_id):
        return os.path.join(self.root, 'views', share_id)

    def state(self, share_id):
        return load(os.path.join(self.vdir(share_id), 'state.json'))


class ShareTests(PluginBase):
    def test_share_marks_view_and_publishes_then_unshare_cleans(self):
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        self.assertEqual(v.status.get('sublime_observer'), 'Observer: SHARED')
        state, text = reader.read_current(self.root, now=self.clock.now)
        self.assertEqual(text, 'alpha\nbeta\n')
        self.assertEqual((state['view'], state['window'], state['share_id']), (11, 1, sid))
        self.toggle(v)
        self.assertNotIn('sublime_observer', v.status)
        self.assertFalse(os.path.exists(self.vdir(sid)))
        self.assertFalse(os.path.lexists(os.path.join(self.root, 'current')))
        self.assertEqual(load(os.path.join(self.root, 'index.json'))['shared'], [])
        self.assertEqual(v.forbidden, [])

    def test_each_share_gets_new_share_id(self):
        v = self.view()
        self.toggle(v)
        first = self.share_id(v)
        self.toggle(v)
        self.toggle(v)
        self.assertNotEqual(self.share_id(v), first)

    def test_sealed_paths_refused_with_status_message(self):
        for ident, path in ((21, '/home/u/.majkee/a.md'), (22, '/p/.hlm/b.md'), (23, '/srv/.env.local')):
            v = self.view(ident, path=path)
            self.toggle(v)
            self.assertNotIn(ident, self.rt.shares)
            self.assertNotIn('sublime_observer', v.status)
            self.assertIn('refused', self.sub.messages[-1])
            self.assertNotIn('substr', v.calls)
        self.assertEqual(os.listdir(os.path.join(self.root, 'views')), [])

    def test_untitled_view_shares_with_null_path(self):
        v = self.view(path=None)
        self.toggle(v)
        state = self.state(self.share_id(v))
        self.assertIsNone(state['path'])
        self.assertEqual(state['title'], 'untitled synthetic')

    def test_save_as_into_vault_unshares(self):
        v = self.view(path=None)
        self.toggle(v)
        sid = self.share_id(v)
        v.__dict__['path'] = '/home/u/.majkee/now-sealed.md'
        self.listener.on_post_save(v)
        self.clock.advance(0.2)
        self.assertNotIn(v.id(), self.rt.shares)
        self.assertFalse(os.path.exists(self.vdir(sid)))

    def test_close_cleans_up(self):
        a, b = self.view(11), self.view(12)
        self.toggle(a)
        self.toggle(b)
        self.assertFalse(os.path.lexists(os.path.join(self.root, 'current')))
        sid = self.share_id(a)
        self.listener.on_close(a)
        self.assertFalse(os.path.exists(self.vdir(sid)))
        index = load(os.path.join(self.root, 'index.json'))['shared']
        self.assertEqual([e['view'] for e in index], [12])
        self.assertEqual(os.readlink(os.path.join(self.root, 'current')), 'views/' + self.share_id(b))

    def test_cap_and_truncated(self):
        self.rt.settings['cap_chars'] = self.rt.store.cap = 10
        v = self.view(text='x' * 25)
        self.toggle(v)
        state, text = reader.read_current(self.root, now=self.clock.now)
        self.assertEqual((len(text), state['published_chars'], state['size_chars'], state['cap'],
                          state['truncated']), (10, 10, 25, 10, True))


class NoReachTests(PluginBase):
    def test_unshared_view_is_never_read(self):
        trap = fakes.TrapView(31, 'private synthetic', '/tmp/unshared.md', self.window)
        shared = self.view(11)
        self.toggle(shared)
        for hook in ('on_modified', 'on_selection_modified', 'on_reload', 'on_revert',
                     'on_post_save', 'on_load', 'on_close'):
            getattr(self.listener, hook)(trap)
        self.clock.advance(3.0)
        self.assertEqual(trap.forbidden, [])
        self.assertEqual(trap.calls, [])
        index = load(os.path.join(self.root, 'index.json'))['shared']
        self.assertEqual([e['view'] for e in index], [11])

    def test_publishing_never_changes_view_focus_selection_or_scroll(self):
        v = self.view()
        self.toggle(v)
        before = (list((r.a, r.b) for r in v.selection), v.viewport, self.window.active)
        for n in range(5):
            v.edit(v.text + 'line {}\n'.format(n))
            self.listener.on_modified(v)
            self.clock.advance(0.3)
        self.clock.advance(2.0)
        self.assertEqual(v.forbidden, [])
        self.assertEqual((list((r.a, r.b) for r in v.selection), v.viewport, self.window.active), before)


class TriggerTests(PluginBase):
    def test_caret_only_change_skips_text_read(self):
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        substr_calls = v.calls.count('substr')
        v.__dict__['selection'] = [fakes.Region(3, 6)]
        self.listener.on_selection_modified(v)
        self.clock.advance(0.2)
        state = self.state(sid)
        self.assertEqual(state['selections'][0], {'a': 3, 'b': 6, 'empty': False, 'start': [0, 3], 'end': [1, 0]})
        self.assertEqual(state['text_file'], 'text.1')
        self.assertEqual(v.calls.count('substr'), substr_calls)

    def test_edit_publishes_new_text(self):
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        v.edit('gamma\n')
        self.listener.on_modified(v)
        self.clock.advance(0.1)
        self.assertEqual(self.state(sid)['revision'], 1)        # still debouncing
        self.clock.advance(0.1)
        state, text = reader.read_capture(self.vdir(sid))
        self.assertEqual((state['revision'], text), (2, 'gamma\n'))

    def test_debounce_with_maximum_delay_under_continuous_typing(self):
        v = self.view()
        self.toggle(v)
        start = self.clock.now
        for _ in range(25):                    # 2.5 s of keystrokes every 100 ms
            self.clock.advance(0.1)
            v.edit(v.text + 'k')
            self.listener.on_modified(v)
        typing_end = self.clock.now
        self.clock.advance(1.0)
        times = [t - start for t, rev, has_text in self.publishes]
        self.assertEqual(times[0], 0.0)                         # share publishes at once
        gaps = [b - a for a, b in zip(times, times[1:])]
        self.assertTrue(all(g <= 1.1 + 1e-6 for g in gaps), gaps)
        self.assertGreaterEqual(len(times), 3)                  # max delay fired during typing
        self.assertAlmostEqual(self.publishes[-1][0], typing_end + 0.15, places=6)
        self.assertEqual(self.publishes[-1][1], v.rev)

    def test_viewport_poll_publishes_state_only(self):
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        reads = v.calls.count('substr')
        v.__dict__['viewport'] = (0.0, 120.0)
        v.__dict__['visible'] = (5, 11)
        self.clock.advance(0.5 + 0.15 + 0.01)
        state = self.state(sid)
        self.assertEqual(state['viewport_position'], [0.0, 120.0])
        self.assertEqual(state['visible_region'], {'begin': 5, 'end': 11})
        self.assertEqual(v.calls.count('substr'), reads)

    def test_eventless_selection_change_is_published_by_poll(self):
        # Sublime 4215: view.sel().add() from the API fires no on_selection_modified.
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        reads = v.calls.count('substr')
        v.__dict__['selection'] = [fakes.Region(2, 2), fakes.Region(4, 7)]   # no listener call
        self.clock.advance(0.5 + 0.15 + 0.01)
        state = self.state(sid)
        self.assertEqual([(s['a'], s['b']) for s in state['selections']], [(2, 2), (4, 7)])
        self.assertEqual(state['text_file'], 'text.1')
        self.assertEqual(v.calls.count('substr'), reads)
        seq = state['seq']
        self.clock.advance(2.0)                                            # unchanged: no republish
        self.assertEqual(self.state(sid)['seq'], seq)

    def test_load_completion_publishes_text(self):
        v = self.view()
        v.__dict__['loading'] = True
        self.toggle(v)
        sid = self.share_id(v)
        self.assertIsNone(self.state(sid)['text_file'])
        v.__dict__['loading'] = False
        self.listener.on_load(v)
        state, text = reader.read_capture(self.vdir(sid))
        self.assertEqual(text, 'alpha\nbeta\n')

    def test_change_during_capture_is_retried_not_published(self):
        v = self.view()
        self.toggle(v)
        sid = self.share_id(v)
        v.edit('one\n')
        v.__dict__['on_substr'] = lambda: (v.edit('two\n'), v.__dict__.update(on_substr=None))
        self.listener.on_modified(v)
        self.clock.advance(0.2)
        self.assertEqual(self.state(sid)['revision'], 1)        # torn capture dropped
        self.clock.advance(0.2)
        state, text = reader.read_capture(self.vdir(sid))
        self.assertEqual((state['revision'], text), (3, 'two\n'))

    def test_heartbeat_timer(self):
        first = load(os.path.join(self.root, 'publisher.json'))['heartbeat_at']
        self.clock.advance(5.01)
        self.assertGreater(load(os.path.join(self.root, 'publisher.json'))['heartbeat_at'], first)


class LifecycleTests(PluginBase):
    def test_unload_removes_epoch_files_and_markers_and_stops_timers(self):
        v = self.view()
        self.toggle(v)
        self.mod.plugin_unloaded()
        self.assertFalse(os.path.exists(self.root))
        self.assertNotIn('sublime_observer', v.status)
        v.edit('after unload\n')
        self.listener.on_modified(v)
        self.clock.advance(10)
        self.assertFalse(os.path.exists(self.root))

    def test_graceful_exit_cleans_like_unload(self):
        # Sublime 4215: plugin_unloaded is not called on app exit; on_exit is.
        v = self.view()
        self.toggle(v)
        self.listener.on_exit()
        self.assertFalse(os.path.exists(self.root))
        self.assertIsNone(self.mod._RT)

    def test_second_publisher_beside_live_one_refuses(self):
        other = self.runtime(pid=987654321)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertFalse(other.start())
        lines = [l for l in out.getvalue().splitlines() if l]
        self.assertEqual(len(lines), 1)
        self.assertIn('does not publish', lines[0])
        self.mod._RT, keep = other, self.mod._RT
        try:
            v = self.view(41)
            self.toggle(v)
            self.assertIn('not publishing', self.sub.messages[-1])
            self.assertNotIn('sublime_observer', v.status)
        finally:
            self.mod._RT = keep
            other.stop()
        self.assertTrue(os.path.exists(os.path.join(self.root, 'publisher.json')))

    def test_reload_cleans_own_previous_epoch(self):
        v = self.view()
        self.toggle(v)
        old_epoch = self.rt.epoch
        self.rt.active = False            # simulate an unload that never ran (same plugin host pid)
        fresh = self.runtime()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertTrue(fresh.start())
        self.assertIn('residue', out.getvalue())
        self.addCleanup(fresh.stop)
        self.assertNotEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], old_epoch)
        self.assertEqual(os.listdir(os.path.join(self.root, 'views')), [])
        self.assertEqual(fresh.shares, {})

    def test_bad_base_refuses_without_crash(self):
        os.chmod(self.tmp.name, 0o755)
        self.addCleanup(os.chmod, self.tmp.name, 0o700)
        broken = self.runtime()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertFalse(broken.start())
        self.assertIn('not publishing', out.getvalue())
        broken.stop()

    def test_settings_validation_falls_back(self):
        s = self.mod.read_settings({'debounce_ms': 'fast', 'cap_chars': -5, 'heartbeat_s': True}.get)
        self.assertEqual((s['debounce_s'], s['cap_chars'], s['heartbeat_s']), (0.15, 200000, 5.0))


if __name__ == '__main__':
    unittest.main()
