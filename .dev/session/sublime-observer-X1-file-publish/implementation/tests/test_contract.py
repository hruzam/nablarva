import json
import os
import stat
import tempfile
import threading
import unittest

import fakes
import reader

contract = fakes.load_contract()
UID = os.getuid()

STATE_FIELDS = {
    'contract_version', 'epoch', 'seq', 'share_id', 'window', 'view', 'buffer', 'path', 'title',
    'dirty', 'loading', 'revision', 'captured_at', 'encoding', 'size_chars', 'text_file',
    'published_chars', 'cap', 'truncated', 'selections', 'visible_region', 'viewport_position',
    'viewport_extent', 'coordinate_units', 'error'}


def body(revision):
    return 'synthetic revision {}\n'.format(revision) * 3


def capture(revision, text=True, sel=0, path='/tmp/synthetic.md', loading=False, size=None):
    t = body(revision) if text else None
    return {'window': 1, 'view': 11, 'buffer': 21, 'path': path, 'title': 'synthetic.md',
            'dirty': True, 'loading': loading, 'revision': revision, 'captured_at': 1.0,
            'encoding': 'UTF-8', 'size_chars': len(body(revision)) if size is None else size,
            'text': None if loading else t, 'truncated': False if size is None else size > len(body(revision)),
            'selection_count': 1, 'selections_truncated': False,
            'selections': [{'a': sel, 'b': sel, 'empty': True, 'start': [0, sel], 'end': [0, sel]}],
            'visible_region': {'begin': 0, 'end': 10}, 'viewport_position': [0.0, float(sel)],
            'viewport_extent': [800.0, 600.0], 'error': None}


def load(path):
    with open(path, 'rb') as handle:
        return json.loads(handle.read().decode('utf-8'))


def mode(path):
    return stat.S_IMODE(os.lstat(path).st_mode)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='sublime-observer-test-')
        self.addCleanup(self.tmp.cleanup)
        self.base = self.tmp.name
        os.chmod(self.base, 0o700)
        self.root = os.path.join(self.base, 'sublime-observer')
        self.now = [5000.0]

    def store(self, epoch='e' * 32, pid=None, alive=None, cap=200000):
        s = contract.Store(self.root, epoch, os.getpid() if pid is None else pid, UID,
                           {'sublime_build': '4215', 'plugin_python': '3.14.6'}, cap, 5.0,
                           clock=lambda: self.now[0], alive=alive or contract.pid_alive)
        self.addCleanup(s.shutdown)
        return s

    def started(self, **kw):
        s = self.store(**kw)
        ok, message = s.start()
        self.assertTrue(ok, message)
        return s

    def vdir(self, share_id):
        return os.path.join(self.root, 'views', share_id)


class RootTests(Base):
    def test_explicit_root_needs_private_base(self):
        self.assertEqual(contract.resolve_root(self.root, {}, UID), self.root)
        os.chmod(self.base, 0o755)
        with self.assertRaises(contract.ContractError):
            contract.resolve_root(self.root, {}, UID)
        with self.assertRaises(contract.ContractError):
            contract.resolve_root('relative/dir', {}, UID)

    def test_xdg_used_only_when_absolute_and_private(self):
        self.assertEqual(contract.resolve_root(None, {'XDG_RUNTIME_DIR': self.base}, UID),
                         os.path.join(self.base, 'sublime-observer'))
        fallback = '/run/user/{}'.format(UID)
        if not contract.is_private_dir(fallback, UID):
            self.skipTest('no private /run/user/<uid> on this host')
        for env in ({}, {'XDG_RUNTIME_DIR': 'relative'}):
            self.assertEqual(contract.resolve_root(None, env, UID), fallback + '/sublime-observer')
        os.chmod(self.base, 0o755)
        self.assertEqual(contract.resolve_root(None, {'XDG_RUNTIME_DIR': self.base}, UID),
                         fallback + '/sublime-observer')

    def test_symlinked_base_and_foreign_root_refused(self):
        real = os.path.join(self.base, 'real')
        os.mkdir(real, 0o700)
        link = os.path.join(self.base, 'link')
        os.symlink(real, link)
        with self.assertRaises(contract.ContractError):
            contract.resolve_root(os.path.join(link, 'sublime-observer'), {}, UID)
        os.mkdir(self.root, 0o755)
        ok = None
        with self.assertRaises(contract.ContractError):
            ok = self.store().start()
        self.assertIsNone(ok)
        self.assertEqual(os.listdir(self.root), [])


class SealedTests(Base):
    def test_sealed_paths(self):
        for path in ('/home/u/.majkee/notes.md', '/home/u/p/.hlm/x/y.txt', '/srv/app/.env',
                     '/srv/app/.env.local', '/srv/app/.envrc'):
            self.assertIsNotNone(contract.sealed_reason(path), path)
        for path in (None, '/tmp/synthetic.md', '/srv/app/prod.env', '/srv/majkee/x', '/a/.hlmx/b'):
            self.assertIsNone(contract.sealed_reason(path), path)

    def test_symlink_into_vault_is_sealed(self):
        vault = os.path.join(self.base, '.majkee')
        os.mkdir(vault)
        target = os.path.join(vault, 'secret.md')
        open(target, 'w').close()
        link = os.path.join(self.base, 'innocent.md')
        os.symlink(target, link)
        self.assertIsNotNone(contract.sealed_reason(link))


class ConsistencyTests(Base):
    def test_text_exists_and_is_named_by_state(self):
        s = self.started()
        s.publish('a' * 32, capture(1))
        state = load(os.path.join(self.vdir('a' * 32), 'state.json'))
        self.assertEqual(set(state) - {'text_file_encoding', 'selection_count', 'selections_truncated'}, STATE_FIELDS)
        self.assertEqual(state['text_file'], 'text.1')
        with open(os.path.join(self.vdir('a' * 32), 'text.1'), encoding='utf-8') as handle:
            self.assertEqual(handle.read(), body(1))
        self.assertEqual(state['published_chars'], len(body(1)))
        self.assertIsNone(state['error'])

    def test_named_text_exists_at_the_moment_state_is_replaced(self):
        s = self.started()
        original = contract.atomic_write
        checked = []

        def watching(directory, name, data):
            if name == 'state.json':
                named = json.loads(data.decode('utf-8'))['text_file']
                if named is not None:
                    self.assertTrue(os.path.exists(os.path.join(directory, named)), named)
                    checked.append(named)
            return original(directory, name, data)
        contract.atomic_write = watching
        try:
            for revision in (1, 1, 2, 3, 3, 4):
                s.publish('a' * 32, capture(revision, text=revision != 1 or not checked))
        finally:
            contract.atomic_write = original
        self.assertEqual(checked, ['text.1', 'text.1', 'text.2', 'text.3', 'text.3', 'text.4'])

    def test_caret_only_change_rewrites_state_only(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        text_path = os.path.join(self.vdir(sid), 'text.1')
        inode = os.stat(text_path).st_ino
        s.publish(sid, capture(1, text=False, sel=5))
        state = load(os.path.join(self.vdir(sid), 'state.json'))
        self.assertEqual(state['seq'], 2)
        self.assertEqual(state['text_file'], 'text.1')
        self.assertEqual(state['selections'][0]['a'], 5)
        self.assertEqual(os.stat(text_path).st_ino, inode)
        self.assertEqual(sorted(n for n in os.listdir(self.vdir(sid)) if n.startswith('text.')), ['text.1'])

    def test_revision_change_and_retention_current_plus_previous(self):
        s = self.started()
        sid = 'a' * 32
        for revision in (1, 2, 3, 4):
            s.publish(sid, capture(revision))
            names = sorted(n for n in os.listdir(self.vdir(sid)) if n.startswith('text.'))
            expected = ['text.{}'.format(r) for r in (revision - 1, revision) if r >= 1]
            self.assertEqual(names, expected)
            self.assertEqual(load(os.path.join(self.vdir(sid), 'state.json'))['text_file'], 'text.{}'.format(revision))
        self.assertEqual(s.text_rev[sid], 4)

    def test_cap_and_truncated_are_explicit(self):
        s = self.started(cap=10)
        c = capture(1, size=250000)
        c['text'] = c['text'][:10]
        c['truncated'] = True
        s.publish('a' * 32, c)
        state = load(os.path.join(self.vdir('a' * 32), 'state.json'))
        self.assertEqual((state['cap'], state['published_chars'], state['size_chars'], state['truncated']),
                         (10, 10, 250000, True))

    def test_loading_publishes_no_text_and_says_so(self):
        s = self.started()
        s.publish('a' * 32, capture(1, loading=True))
        state = load(os.path.join(self.vdir('a' * 32), 'state.json'))
        self.assertIsNone(state['text_file'])
        self.assertTrue(state['loading'])
        self.assertEqual(state['error']['code'], 'loading')

    def test_no_temp_files_left(self):
        s = self.started()
        for revision in range(1, 6):
            s.publish('a' * 32, capture(revision))
        leftovers = [n for d in (self.root, self.vdir('a' * 32)) for n in os.listdir(d) if n.startswith('.tmp-')]
        self.assertEqual(leftovers, [])


class CurrentAndCleanupTests(Base):
    def current(self):
        link = os.path.join(self.root, 'current')
        return os.readlink(link) if os.path.islink(link) else None

    def shared_ids(self):
        return [e['share_id'] for e in load(os.path.join(self.root, 'index.json'))['shared']]

    def test_current_only_for_exactly_one_share(self):
        s = self.started()
        a, b = 'a' * 32, 'b' * 32
        self.assertIsNone(self.current())
        s.publish(a, capture(1))
        self.assertEqual(self.current(), 'views/' + a)
        s.publish(b, capture(1))
        self.assertIsNone(self.current())
        self.assertEqual(self.shared_ids(), [a, b])
        s.remove_share(a)
        self.assertEqual(self.current(), 'views/' + b)
        s.remove_share(b)
        self.assertIsNone(self.current())
        self.assertEqual(self.shared_ids(), [])

    def test_unshare_removes_dir_and_index_entry_and_never_resurrects(self):
        s = self.started()
        a = 'a' * 32
        s.publish(a, capture(1))
        s.remove_share(a)
        self.assertFalse(os.path.exists(self.vdir(a)))
        self.assertEqual(self.shared_ids(), [])
        self.assertFalse(s.publish(a, capture(2)))
        self.assertFalse(os.path.exists(self.vdir(a)))

    def test_shutdown_removes_this_epoch_files(self):
        s = self.started()
        s.publish('a' * 32, capture(1))
        s.shutdown()
        self.assertFalse(os.path.exists(self.root))

    def test_shutdown_leaves_another_epochs_publication(self):
        s = self.started()
        info = load(os.path.join(self.root, 'publisher.json'))
        info['epoch'] = 'f' * 32
        contract.atomic_write(self.root, 'publisher.json', json.dumps(info).encode())
        s.shutdown()
        self.assertTrue(os.path.exists(os.path.join(self.root, 'publisher.json')))


class LivenessTests(Base):
    def plant(self, pid, heartbeat_at, epoch='0' * 32, body_bytes=None):
        os.mkdir(self.root, 0o700)
        os.makedirs(os.path.join(self.root, 'views', 'c' * 32), 0o700)
        with open(os.path.join(self.root, 'views', 'c' * 32, 'state.json'), 'w') as handle:
            handle.write('{}')
        os.symlink('views/' + 'c' * 32, os.path.join(self.root, 'current'))
        data = body_bytes if body_bytes is not None else json.dumps(
            {'epoch': epoch, 'pid': pid, 'heartbeat_at': heartbeat_at, 'heartbeat_interval_s': 5.0}).encode()
        with open(os.path.join(self.root, 'publisher.json'), 'wb') as handle:
            handle.write(data)

    def test_dead_epoch_residue_is_removed(self):
        self.plant(pid=424242, heartbeat_at=self.now[0])
        s = self.store(alive=lambda pid: False)
        ok, message = s.start()
        self.assertTrue(ok)
        self.assertIn('residue', message)
        self.assertFalse(os.path.exists(os.path.join(self.root, 'views', 'c' * 32)))
        self.assertFalse(os.path.lexists(os.path.join(self.root, 'current')))
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], 'e' * 32)

    def test_real_dead_pid_via_proc(self):
        with open('/proc/sys/kernel/pid_max') as handle:
            impossible = int(handle.read()) + 1
        self.assertFalse(contract.pid_alive(impossible))
        self.assertTrue(contract.pid_alive(os.getpid()))
        self.plant(pid=impossible, heartbeat_at=self.now[0])
        self.assertTrue(self.store().start()[0])

    def test_live_publisher_is_left_alone(self):
        self.plant(pid=424242, heartbeat_at=self.now[0] - 4)
        s = self.store(alive=lambda pid: True)
        ok, message = s.start()
        self.assertFalse(ok)
        self.assertIn('does not publish', message)
        self.assertTrue(os.path.exists(os.path.join(self.root, 'views', 'c' * 32, 'state.json')))
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], '0' * 32)
        self.assertFalse(s.publish('a' * 32, capture(1)))

    def test_alive_pid_with_stale_heartbeat_is_residue(self):
        self.plant(pid=424242, heartbeat_at=self.now[0] - 60)
        self.assertTrue(self.store(alive=lambda pid: True).start()[0])

    def test_unreadable_publisher_is_refused_not_cleaned(self):
        self.plant(pid=0, heartbeat_at=0, body_bytes=b'{not json')
        ok, message = self.store(alive=lambda pid: False).start()
        self.assertFalse(ok)
        self.assertTrue(os.path.exists(os.path.join(self.root, 'views', 'c' * 32)))

    def test_heartbeat_refreshes(self):
        s = self.started()
        self.now[0] += 7
        s.heartbeat()
        info = load(os.path.join(self.root, 'publisher.json'))
        self.assertEqual(info['heartbeat_at'], self.now[0])
        self.assertEqual(info['stale_after_s'], 15.0)
        for key in ('contract_version', 'epoch', 'pid', 'sublime_build', 'plugin_python', 'started_at'):
            self.assertIn(key, info)


class ModeTests(Base):
    def test_modes_even_with_permissive_umask(self):
        old = os.umask(0)
        try:
            s = self.started()
            sid = 'a' * 32
            s.publish(sid, capture(1))
            s.publish(sid, capture(2))
        finally:
            os.umask(old)
        for d in (self.root, os.path.join(self.root, 'views'), self.vdir(sid)):
            self.assertEqual(mode(d), 0o700, d)
        for f in (os.path.join(self.root, 'publisher.json'), os.path.join(self.root, 'index.json'),
                  os.path.join(self.vdir(sid), 'state.json'), os.path.join(self.vdir(sid), 'text.1'),
                  os.path.join(self.vdir(sid), 'text.2')):
            self.assertEqual(mode(f), 0o600, f)


class ReaderTests(Base):
    def test_reader_never_pairs_new_state_with_old_text(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        steps = {'n': 1}

        def publish_two_more(state):
            if steps['n'] < 3:          # text.1 deleted after rev 3 -> reader must retry
                steps['n'] += 1
                s.publish(sid, capture(steps['n']))
                steps['n'] += 1
                s.publish(sid, capture(steps['n']))
        state, text = reader.read_capture(self.vdir(sid), between=publish_two_more)
        self.assertEqual(text, body(state['revision']))
        self.assertEqual(state['revision'], 3)

        def publish_one_more(state):
            if steps['n'] < 4:          # text.3 stays as "previous": old pair, still consistent
                steps['n'] += 1
                s.publish(sid, capture(steps['n']))
        state, text = reader.read_capture(self.vdir(sid), between=publish_one_more)
        self.assertEqual((state['revision'], text), (3, body(3)))

    def test_concurrent_reader_sees_only_consistent_pairs(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        done = threading.Event()
        seen, bad = [], []

        def write():
            for revision in range(2, 400):
                s.publish(sid, capture(revision))
                s.publish(sid, capture(revision, text=False, sel=revision % 7))
            done.set()

        def read():
            while not done.is_set():
                try:
                    state, text = reader.read_capture(self.vdir(sid), retries=50)
                except reader.Unavailable:
                    continue
                seen.append(state['seq'])
                if text != body(state['revision']):
                    bad.append(state['revision'])
        threads = [threading.Thread(target=write), threading.Thread(target=read)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(60)
        self.assertEqual(bad, [])
        self.assertTrue(seen)
        self.assertEqual(seen, sorted(seen))       # seq never goes backwards for a reader

    def test_read_current_refuses_stale_publisher(self):
        s = self.started()
        s.publish('a' * 32, capture(1))
        state, text = reader.read_current(self.root, now=self.now[0] + 1)
        self.assertEqual(text, body(1))
        with self.assertRaises(reader.NotLive):
            reader.read_current(self.root, now=self.now[0] + 16)


class DebouncerTests(unittest.TestCase):
    def test_trailing_debounce(self):
        d = contract.Debouncer(0.15, 1.0)
        self.assertAlmostEqual(d.touch('v', 0.0), 0.15)
        self.assertIsNone(d.touch('v', 0.05))          # already armed
        self.assertAlmostEqual(d.fire('v', 0.15), 0.05)  # touched at .05: wait till .20
        self.assertIsNone(d.fire('v', 0.20))
        self.assertFalse(d.pending('v'))

    def test_maximum_delay_bounds_continuous_typing(self):
        d = contract.Debouncer(0.15, 1.0)
        timer = d.touch('v', 0.0)
        fired_at, t = None, 0.0
        due = timer
        while fired_at is None and t < 5.0:                 # bounded: a starving debounce fails, never hangs
            t = round(t + 0.1, 6)
            d.touch('v', t)                            # keystroke every 100 ms < debounce
            if t >= due - 1e-9:
                again = d.fire('v', t)
                if again is None:
                    fired_at = t
                else:
                    due = t + again
        self.assertIsNotNone(fired_at, 'continuous typing starved publication')
        self.assertLessEqual(fired_at, 1.0 + 1e-6)
        self.assertGreaterEqual(fired_at, 0.95)


class WriterTests(unittest.TestCase):
    def test_order_errors_and_close(self):
        errors, out = [], []
        w = contract.Writer(errors.append)
        for n in range(50):
            w.submit(out.append, n)
        w.submit(lambda: 1 / 0)
        w.submit(out.append, 'after')
        drained = threading.Event()
        w.submit(drained.set)
        self.assertTrue(drained.wait(5))
        self.assertTrue(w.close(5))
        self.assertEqual(out[:50], list(range(50)))
        self.assertEqual(out[-1], 'after')
        self.assertEqual(len(errors), 1)
        w.submit(out.append, 'late')
        self.assertNotIn('late', out)


if __name__ == '__main__':
    unittest.main()
