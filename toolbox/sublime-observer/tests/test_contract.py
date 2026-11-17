import json
import os
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import unittest

import fakes
import reader

contract = fakes.load_contract()
UID = os.getuid()

STATE_FIELDS = {
    'contract_version', 'epoch', 'seq', 'share_id', 'window', 'view', 'buffer', 'path', 'title',
    'dirty', 'loading', 'revision', 'captured_at', 'encoding', 'size_chars', 'text_file', 'text_encoding_replaced',
    'published_chars', 'cap', 'truncated', 'selections', 'visible_region', 'viewport_position',
    'viewport_extent', 'coordinate_units', 'error'}


def body(revision):
    return 'synthetic revision {}\n'.format(revision) * 3


def tn(share_id, revision):
    return 'text.{}.{}'.format(share_id, revision)


def capture(revision, text=True, sel=0, path='/tmp/synthetic.md', loading=False, size=None, value=None):
    t = (body(revision) if value is None else value) if text else None
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

    def store(self, epoch='e' * 32, pid=None, cap=200000):
        s = contract.Store(self.root, epoch, os.getpid() if pid is None else pid, UID,
                           {'sublime_build': '4215', 'plugin_python': '3.14.6'}, cap, contract.DEFAULTS['heartbeat_s'],
                           clock=lambda: self.now[0])
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
        self.assertEqual(state['text_file'], tn('a' * 32, 1))
        self.assertFalse(state['text_encoding_replaced'])
        with open(os.path.join(self.vdir('a' * 32), tn('a' * 32, 1)), encoding='utf-8') as handle:
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
        self.assertEqual(checked, [tn('a' * 32, r) for r in (1, 1, 2, 3, 3, 4)])

    def test_caret_only_change_rewrites_state_only(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        text_path = os.path.join(self.vdir(sid), tn(sid, 1))
        inode = os.stat(text_path).st_ino
        s.publish(sid, capture(1, text=False, sel=5))
        state = load(os.path.join(self.vdir(sid), 'state.json'))
        self.assertEqual(state['seq'], 2)
        self.assertEqual(state['text_file'], tn(sid, 1))
        self.assertEqual(state['selections'][0]['a'], 5)
        self.assertEqual(os.stat(text_path).st_ino, inode)
        self.assertEqual(sorted(n for n in os.listdir(self.vdir(sid)) if n.startswith('text.')), [tn(sid, 1)])

    def test_revision_change_and_retention_current_plus_previous(self):
        s = self.started()
        sid = 'a' * 32
        for revision in (1, 2, 3, 4):
            s.publish(sid, capture(revision))
            names = sorted(n for n in os.listdir(self.vdir(sid)) if n.startswith('text.'))
            expected = [tn(sid, r) for r in (revision - 1, revision) if r >= 1]
            self.assertEqual(names, expected)
            self.assertEqual(load(os.path.join(self.vdir(sid), 'state.json'))['text_file'], tn(sid, revision))
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


CHILD = r'''
import json, os, sys
sys.path.insert(0, sys.argv[1])
from SublimeObserver import contract
root, epoch = sys.argv[2], sys.argv[3]
s = contract.Store(root, epoch, os.getpid(), os.getuid(), {}, 1000, 1.0)
sys.stdin.readline()                                    # "go"
ok, message = s.start()
print('ok' if ok else 'refused', flush=True)
for line in sys.stdin:
    if line.strip() == 'publish':
        print('published', s.publish(epoch[:32], json.loads(sys.stdin.readline())), flush=True)
os._exit(0)                                             # stdin closed: die without cleanup, like a crash
'''


class OwnershipTests(Base):
    """Acceptance (a): one publisher per root, by the kernel lock; no takeover by heartbeat age."""

    def plant(self, pid, heartbeat_at, epoch='0' * 32, body_bytes=None, interval=1.0):
        os.mkdir(self.root, 0o700)
        os.makedirs(os.path.join(self.root, 'views', 'c' * 32), 0o700)
        with open(os.path.join(self.root, 'views', 'c' * 32, 'state.json'), 'w') as handle:
            handle.write('{}')
        os.symlink('views/' + 'c' * 32, os.path.join(self.root, 'current'))
        data = body_bytes if body_bytes is not None else json.dumps(
            {'epoch': epoch, 'pid': pid, 'heartbeat_at': heartbeat_at, 'heartbeat_interval_s': interval}).encode()
        with open(os.path.join(self.root, 'publisher.json'), 'wb') as handle:
            handle.write(data)

    def child(self, epoch):
        proc = subprocess.Popen([sys.executable, '-I', '-S', '-B', '-c', CHILD, fakes.IMPL, self.root, epoch],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

        def reap():
            if proc.poll() is None:
                try:
                    os.kill(proc.pid, signal.SIGCONT)
                except OSError:
                    pass
                proc.kill()
            proc.communicate(timeout=10)
        self.addCleanup(reap)
        return proc

    @staticmethod
    def say(proc, *lines):
        proc.stdin.write(''.join(l + '\n' for l in lines))
        proc.stdin.flush()

    def test_residue_without_a_lock_holder_is_removed_even_if_it_looks_live(self):
        # the old rule kept a live pid with a fresh heartbeat; only the lock decides now
        self.plant(pid=os.getpid(), heartbeat_at=self.now[0])
        s = self.store()
        ok, message = s.start()
        self.assertTrue(ok, message)
        self.assertIn('residue', message)
        self.assertFalse(os.path.exists(os.path.join(self.root, 'views', 'c' * 32)))
        self.assertFalse(os.path.lexists(os.path.join(self.root, 'current')))
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], 'e' * 32)

    def test_holder_with_a_stale_heartbeat_keeps_the_root(self):
        a = self.started(epoch='a' * 32)
        a.publish('a' * 32, capture(1))
        self.now[0] += 3600                         # A's heartbeat is an hour old: still the owner
        b = self.store(epoch='b' * 32)
        ok, message = b.start()
        self.assertFalse(ok)
        self.assertIn('does not publish', message)
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], 'a' * 32)
        self.assertFalse(b.publish('b' * 32, capture(1)))
        self.assertTrue(a.publish('a' * 32, capture(2)))
        self.assertEqual(os.listdir(os.path.join(self.root, 'views')), ['a' * 32])

    def test_simultaneous_start_in_threads_one_owner(self):
        # Step 5b: losers' exceptions are collected. Legitimate outcomes here are exactly one
        # (True, ...) and (False, "... does not publish") for every other thread. No Store shuts
        # down in this test, so the lock file is never unlinked and the root never vanishes:
        # the "kept being replaced / kept disappearing" ContractErrors (legitimate only under
        # shutdown churn) and any other exception are failures.
        stores = [self.store(epoch='{:032x}'.format(n)) for n in range(8)]
        barrier = threading.Barrier(len(stores))
        results = [None] * len(stores)
        errors = []

        def go(n):
            barrier.wait()
            try:
                results[n] = stores[n].start()
            except BaseException as exc:
                errors.append((n, '{}: {}'.format(type(exc).__name__, exc)))
        threads = [threading.Thread(target=go, args=(n,)) for n in range(len(stores))]
        for t in threads:
            t.start()
        for t in threads:
            t.join(10)
        self.assertEqual(errors, [])
        self.assertNotIn(None, results)             # every thread finished with an answer
        self.assertEqual([r[0] for r in results].count(True), 1, results)
        for ok, message in results:
            if not ok:
                self.assertIn('does not publish', message)
        owner = stores[[r[0] for r in results].index(True)]
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], owner.epoch)

    def test_simultaneous_start_in_processes_one_owner(self):
        procs = [self.child('{:032x}'.format(n + 100)) for n in range(4)]
        for p in procs:
            self.say(p, 'go')
        answers = [p.stdout.readline().strip() for p in procs]
        self.assertEqual(sorted(answers), ['ok', 'refused', 'refused', 'refused'])
        owner = '{:032x}'.format(answers.index('ok') + 100)
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], owner)

    def test_resumed_old_owner_and_a_new_start_never_both_publish(self):
        a_epoch = 'a' * 32
        a = self.child(a_epoch)
        self.say(a, 'go')
        self.assertEqual(a.stdout.readline().strip(), 'ok')
        os.kill(a.pid, signal.SIGSTOP)              # paused owner: no heartbeat, pid alive
        try:
            self.now[0] = time.time() + 600
            b = self.store(epoch='b' * 32)
            ok, message = b.start()
            self.assertFalse(ok)
            self.assertIn('does not publish', message)
        finally:
            os.kill(a.pid, signal.SIGCONT)
        self.say(a, 'publish', json.dumps(capture(7)))
        self.assertEqual(a.stdout.readline().strip(), 'published True')
        self.assertEqual(load(os.path.join(self.vdir(a_epoch), 'state.json'))['epoch'], a_epoch)
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], a_epoch)
        self.assertFalse(b.publish('b' * 32, capture(1)))
        a.stdin.close()                             # A dies without cleanup (crash)
        a.wait(10)
        c = self.store(epoch='c' * 32)
        ok, message = c.start()
        self.assertTrue(ok, message)
        self.assertIn(a_epoch, message)
        self.assertEqual(os.listdir(os.path.join(self.root, 'views')), [])

    def test_second_store_in_the_same_process_is_refused(self):
        # a previous plugin load whose unload never ran still holds the lock: refuse, touch nothing
        a = self.started(epoch='a' * 32)
        a.publish('a' * 32, capture(1))
        b = self.store(epoch='b' * 32)
        self.assertFalse(b.start()[0])
        self.assertTrue(os.path.exists(os.path.join(self.vdir('a' * 32), 'state.json')))

    def test_lock_file_unlinked_by_a_finishing_holder_is_not_a_second_lock(self):
        a = self.started(epoch='a' * 32)
        real = contract.fcntl.flock
        fired = []

        def flock(fd, op):
            if not fired:                           # B has opened the path; A shuts down now
                fired.append(True)
                a.shutdown()
            return real(fd, op)
        contract.fcntl.flock = flock
        try:
            b = self.store(epoch='b' * 32)
            ok, message = b.start()
        finally:
            contract.fcntl.flock = real
        self.assertTrue(fired)
        self.assertTrue(ok, message)
        c = self.store(epoch='c' * 32)
        self.assertFalse(c.start()[0])              # B holds the file that is at the path
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['epoch'], 'b' * 32)

    def test_shutdown_never_unlinks_a_lock_file_it_does_not_hold(self):
        # step 5b: the _holds_path check at shutdown. A's lock file is removed behind it (same
        # user, R3 territory) and B locks a fresh file at the path; A's shutdown must leave it.
        a = self.started(epoch='a' * 32)
        lock = os.path.join(self.root, contract.LOCK_NAME)
        os.unlink(lock)
        b = self.started(epoch='b' * 32)
        b_file = os.lstat(lock).st_ino
        a.shutdown()
        self.assertTrue(os.path.lexists(lock))
        self.assertEqual(os.lstat(lock).st_ino, b_file)
        self.assertFalse(self.store(epoch='c' * 32).start()[0])     # B still holds the file at the path
        self.assertTrue(b.live)

    def test_symlinked_lock_file_is_refused(self):
        os.mkdir(self.root, 0o700)
        outside = os.path.join(self.base, 'outside-lock')
        os.symlink(outside, os.path.join(self.root, 'publisher.lock'))
        with self.assertRaises(OSError):
            self.store().start()
        self.assertFalse(os.path.lexists(outside))

    def test_unreadable_publisher_is_refused_not_cleaned(self):
        # kept under the lock: no lock holder is live, but an unparseable publisher.json is
        # not ours to interpret (foreign writer or a damaged root); the operator removes it
        self.plant(pid=0, heartbeat_at=0, body_bytes=b'{not json')
        s = self.store()
        ok, message = s.start()
        self.assertFalse(ok)
        self.assertIn('not cleaning', message)
        self.assertTrue(os.path.exists(os.path.join(self.root, 'views', 'c' * 32)))
        self.assertTrue(self.store(epoch='f' * 32).start()[0] is False)     # lock was released

    def test_heartbeat_refreshes(self):
        s = self.started()
        self.now[0] += 7
        s.heartbeat()
        info = load(os.path.join(self.root, 'publisher.json'))
        self.assertEqual(info['heartbeat_at'], self.now[0])
        self.assertEqual(info['heartbeat_interval_s'], 1.0)            # the default
        self.assertEqual(info['stale_after_s'], 3.0)
        for key in ('contract_version', 'epoch', 'pid', 'sublime_build', 'plugin_python', 'started_at'):
            self.assertIn(key, info)

    def test_lock_file_lives_with_the_publisher_and_goes_at_shutdown(self):
        s = self.started()
        lock = os.path.join(self.root, 'publisher.lock')
        self.assertTrue(os.path.isfile(lock))
        self.assertEqual(mode(lock), 0o600)
        s.shutdown()
        self.assertFalse(os.path.exists(self.root))
        self.assertTrue(self.store(epoch='f' * 32).start()[0])


class CurrentSwitchTests(Base):
    """Acceptance (b): `current` switches from A to B between a reader's state read and its
    text read; both shares at revision 1 with distinct bodies. Never a wrong pairing."""
    A, B = 'a' * 32, 'b' * 32
    BODIES = {A: 'BODY OF SHARE A\n', B: 'BODY OF SHARE B\n'}

    def prepare(self, sub):
        self.root = os.path.join(self.base, sub)
        self.s = self.started()
        self.s.publish(self.A, capture(1, value=self.BODIES[self.A]))
        self.switched = []

    def switch(self, _state=None):
        if not self.switched:                       # B shared, then A unshared: current -> B
            self.switched.append(True)
            self.s.publish(self.B, capture(1, value=self.BODIES[self.B]))
            self.s.remove_share(self.A)

    def naive_read(self):
        """The v1.0 reader rule: open current/state.json, then current/<text_file>."""
        link = os.path.join(self.root, 'current')
        state = load(os.path.join(link, 'state.json'))
        self.switch()
        with open(os.path.join(link, state['text_file']), 'rb') as handle:
            return state, handle.read().decode('utf-8')

    def assert_paired(self, state, text):
        self.assertEqual(text, self.BODIES[state['share_id']])

    def test_naive_reader_finds_no_file_instead_of_another_shares_text(self):
        # publisher-side guard: the text file name carries the share id
        self.prepare('naive')
        try:
            state, text = self.naive_read()
        except FileNotFoundError:
            pass
        else:
            self.assert_paired(state, text)
        self.assertTrue(self.switched)

    def test_reader_rule_never_pairs_across_shares(self):
        for legacy in (False, True):               # True: as if the publisher used text.<revision>
            with self.subTest(legacy_names=legacy):
                original = contract.text_name
                if legacy:
                    contract.text_name = lambda share_id, revision: 'text.{}'.format(revision)
                try:
                    self.prepare('legacy' if legacy else 'named')
                    try:
                        state, text = reader.read_current(self.root, now=self.now[0], between=self.switch)
                    except reader.Unavailable:
                        pass
                    else:
                        self.assert_paired(state, text)
                    self.assertTrue(self.switched)
                    state, text = reader.read_current(self.root, now=self.now[0])     # a fresh read sees B
                    self.assertEqual((state['share_id'], text), (self.B, self.BODIES[self.B]))
                finally:
                    contract.text_name = original


class RevocationTests(Base):
    """Acceptance (c), contract side: a removal that fails stops the publisher."""

    def fail_on(self, names):
        """Inject removal failures; returns a function that removes the injection."""
        real_tree, real_current = contract._remove_tree, contract.set_current

        def tree(path):
            if 'tree' in names:
                raise OSError(5, 'injected removal failure', path)
            return real_tree(path)

        def current(root, share_id):
            if 'current' in names:
                raise OSError(5, 'injected removal failure', 'current')
            return real_current(root, share_id)
        contract._remove_tree, contract.set_current = tree, current

        def restore():
            contract._remove_tree, contract.set_current = real_tree, real_current
        self.addCleanup(restore)
        return restore

    def test_failed_directory_removal_stops_publishing_and_reads_not_live_at_once(self):
        s = self.started()
        a = 'a' * 32
        s.publish(a, capture(1))
        self.fail_on({'tree'})
        with self.assertRaises(contract.Stopped):
            s.remove_share(a)
        self.assertFalse(s.live)
        with self.assertRaises(reader.NotLive):
            reader.read_current(self.root, now=self.now[0])
        self.assertFalse(os.path.lexists(os.path.join(self.root, 'current')))
        before = os.listdir(self.root)
        s.heartbeat()
        self.assertFalse(s.publish('b' * 32, capture(1)))
        self.assertEqual(os.listdir(self.root), before)

    def test_when_nothing_can_be_removed_the_heartbeat_stops_and_staleness_takes_over(self):
        s = self.started()
        a = 'a' * 32
        s.publish(a, capture(1))
        self.fail_on({'tree', 'current'})
        real_unlink = os.unlink

        def unlink(path, *args, **kwargs):
            raise OSError(5, 'injected removal failure', path)
        os.unlink = unlink
        try:
            with self.assertRaises(contract.Stopped):
                s.remove_share(a)
        finally:
            os.unlink = real_unlink
        # current and publisher.json could not be removed: only the stopped heartbeat protects readers
        self.assertTrue(os.path.lexists(os.path.join(self.root, 'current')))
        beat = load(os.path.join(self.root, 'publisher.json'))['heartbeat_at']
        self.now[0] += 10
        s.heartbeat()
        self.assertEqual(load(os.path.join(self.root, 'publisher.json'))['heartbeat_at'], beat)
        with self.assertRaises(reader.NotLive):
            reader.read_current(self.root, now=beat + contract.STALE_FACTOR * contract.DEFAULTS['heartbeat_s'] + 0.01)

    def test_shutdown_after_a_stop_still_cleans_and_releases(self):
        s = self.started()
        s.publish('a' * 32, capture(1))
        restore = self.fail_on({'tree'})
        with self.assertRaises(contract.Stopped):
            s.remove_share('a' * 32)
        restore()                                   # removal works again
        s.shutdown()
        self.assertFalse(os.path.exists(self.root))

    def beat(self):
        return load(os.path.join(self.root, 'publisher.json'))['heartbeat_at']

    def test_no_heartbeat_while_a_revocation_is_pending_and_again_after_removal(self):
        # step 5b, R1
        s = self.started()
        a, b = 'a' * 32, 'b' * 32
        s.publish(a, capture(1))
        s.publish(b, capture(1))
        beat = self.beat()
        s.revoke(a)                                 # main thread; removal not yet executed
        self.now[0] += 10
        s.heartbeat()
        self.assertEqual(self.beat(), beat)
        with self.assertRaises(reader.NotLive):
            reader.publisher(self.root, now=self.now[0])
        s.remove_share(a)
        s.heartbeat()
        self.assertEqual(self.beat(), self.now[0])
        state, text = reader.read_current(self.root, now=self.now[0])
        self.assertEqual(state['share_id'], b)

    def test_heartbeat_in_flight_at_revoke_stamps_a_time_before_it(self):
        # step 5b, R1 bound: a heartbeat executing when revoke() runs. Both orders of revoke
        # relative to the heartbeat's own steps; any stamp written must precede the revoke.
        for where in ('during the clock read', 'right after the pending check'):
            with self.subTest(where=where):
                self.root = os.path.join(self.base, where.replace(' ', '-'))
                s = self.started()
                a = 'a' * 32
                s.publish(a, capture(1))
                self.now[0] += 1
                revoked_at = []

                def revoke_now():
                    if not revoked_at:
                        self.now[0] += 0.5          # time passes; then the operator's revoke lands
                        revoked_at.append(self.now[0])
                        s.revoke(a)
                if where == 'during the clock read':
                    s._clock = lambda: (revoke_now(), self.now[0])[1]
                else:
                    real = s._revocation_pending
                    s._revocation_pending = lambda: (real(), revoke_now())[0]
                s.heartbeat()
                self.assertTrue(revoked_at)
                self.assertLess(self.beat(), revoked_at[0])

    def test_revoke_discards_a_publish_that_was_queued_before(self):
        s = self.started()
        a = 'a' * 32
        s.publish(a, capture(1))
        seq = load(os.path.join(self.vdir(a), 'state.json'))['seq']
        s.revoke(a)                                 # main thread, before the queued publish runs
        self.assertFalse(s.publish(a, capture(2)))
        self.assertEqual(load(os.path.join(self.vdir(a), 'state.json'))['seq'], seq)


class ListingOrderTests(Base):
    """Item 7: `current` is removed before the index changes, and set only after it."""

    def record(self):
        events = []
        real_write, real_current, real_tree = contract.atomic_write, contract.set_current, contract._remove_tree

        def write(directory, name, data):
            if name == 'index.json':
                events.append(('index', tuple(e['share_id'] for e in json.loads(data.decode())['shared'])))
            return real_write(directory, name, data)

        def current(root, share_id):
            events.append(('current', share_id))
            return real_current(root, share_id)

        def tree(path):
            events.append(('remove', os.path.basename(path)))
            return real_tree(path)
        contract.atomic_write, contract.set_current, contract._remove_tree = write, current, tree
        self.addCleanup(setattr, contract, 'atomic_write', real_write)
        self.addCleanup(setattr, contract, 'set_current', real_current)
        self.addCleanup(setattr, contract, '_remove_tree', real_tree)
        return events

    def test_second_share_removes_current_before_the_index(self):
        s = self.started()
        a, b = 'a' * 32, 'b' * 32
        s.publish(a, capture(1))
        events = self.record()
        s.publish(b, capture(1))
        self.assertEqual(events, [('current', None), ('index', (a, b))])

    def test_removal_order(self):
        s = self.started()
        a, b = 'a' * 32, 'b' * 32
        s.publish(a, capture(1))
        s.publish(b, capture(1))
        events = self.record()
        s.remove_share(a)                           # two -> one: index, directory, then current
        s.remove_share(b)                           # the current share: current off first
        self.assertEqual(events, [('index', (b,)), ('remove', a), ('current', b),
                                  ('current', None), ('index', ()), ('remove', b)])


class SmallFixTests(Base):
    def test_unresolvable_path_is_refused(self):
        self.assertIn('cannot be resolved', contract.sealed_reason('/tmp/synthetic\0name.md'))
        real = os.path.realpath

        def broken(path, *a, **k):
            raise OSError(40, 'injected loop')
        os.path.realpath = broken
        try:
            self.assertIn('cannot be resolved', contract.sealed_reason('/tmp/synthetic.md'))
        finally:
            os.path.realpath = real
        self.assertIsNone(contract.sealed_reason('/tmp/synthetic.md'))

    def test_encoding_replacement_is_flagged(self):
        s = self.started()
        sid = 'a' * 32
        text = 'lone \udc80 surrogate\n'
        s.publish(sid, capture(1, value=text))
        state = load(os.path.join(self.vdir(sid), 'state.json'))
        self.assertTrue(state['text_encoding_replaced'])
        self.assertEqual(state['published_chars'], len(text))
        with open(os.path.join(self.vdir(sid), state['text_file']), 'rb') as handle:
            self.assertEqual(handle.read(), b'lone ? surrogate\n')
        s.publish(sid, capture(1, text=False, sel=2))     # caret-only: flag follows the text file
        self.assertTrue(load(os.path.join(self.vdir(sid), 'state.json'))['text_encoding_replaced'])
        s.publish(sid, capture(2, value='clean\n'))
        self.assertFalse(load(os.path.join(self.vdir(sid), 'state.json'))['text_encoding_replaced'])


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
                  os.path.join(self.vdir(sid), 'state.json'), os.path.join(self.vdir(sid), tn(sid, 1)),
                  os.path.join(self.vdir(sid), tn(sid, 2)), os.path.join(self.root, 'publisher.lock')):
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
            if steps['n'] < 4:          # text.3 stays as "previous" and is read, but the second
                steps['n'] += 1         # state read sees seq move on: the reader retries
                s.publish(sid, capture(steps['n']))
        state, text = reader.read_capture(self.vdir(sid), between=publish_one_more)
        self.assertEqual((state['revision'], text), (4, body(4)))

    def test_second_state_read_rejects_a_superseded_pair(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        once = []

        def caret_move(state):
            if not once:
                once.append(state['seq'])
                s.publish(sid, capture(1, text=False, sel=4))     # same text, newer state
        state, text = reader.read_current(self.root, now=self.now[0], after_text=caret_move)
        self.assertEqual(state['seq'], once[0] + 1)
        self.assertEqual(state['selections'][0]['a'], 4)
        self.assertEqual(text, body(1))

    def test_state_must_name_the_share_current_points_at(self):
        s = self.started()
        sid = 'a' * 32
        s.publish(sid, capture(1))
        path = os.path.join(self.vdir(sid), 'state.json')
        state = load(path)
        state['share_id'] = 'b' * 32
        contract.atomic_write(self.vdir(sid), 'state.json', json.dumps(state).encode())
        with self.assertRaises(reader.Unavailable):
            reader.read_current(self.root, now=self.now[0])

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
