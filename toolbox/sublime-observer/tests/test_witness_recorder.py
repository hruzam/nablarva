"""Witness recorder (step 4a): fake roots built with the real contract Store, no editor."""
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import time
import unittest

import fakes
import witness_recorder as wr

contract = fakes.load_contract()
UID = os.getuid()
RECORDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'witness_recorder.py')
TEXT_1 = 'witness body alpha seven lines\n' * 4
TEXT_2 = 'witness body beta after the edit\n' * 5
FORBID = 'UNSHARED-MARKER-4a'


def capture(revision, text):
    return {'window': 1, 'view': 11, 'buffer': 21, 'path': '/tmp/witness-synthetic.md',
            'title': 'witness-synthetic.md', 'dirty': True, 'loading': False, 'revision': revision,
            'captured_at': 1.0, 'encoding': 'UTF-8', 'size_chars': len(text), 'text': text,
            'truncated': False, 'selection_count': 1, 'selections_truncated': False,
            'selections': [{'a': 3, 'b': 3, 'empty': True, 'start': [0, 3], 'end': [0, 3]}],
            'visible_region': {'begin': 0, 'end': 10}, 'viewport_position': [0.0, 0.0],
            'viewport_extent': [800.0, 600.0], 'error': None}


def records(path):
    with open(path, 'rb') as handle:
        return [json.loads(line) for line in handle.read().decode('utf-8').splitlines() if line.strip()]


def slurp(path, mode='r'):
    with open(path, mode) as handle:
        return handle.read()


def samples(recs):
    return [r['snapshot'] for r in recs if r['kind'] == 'sample']


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='x1-4a-witness-')
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.base = os.path.join(self.tmp, 'run')
        os.mkdir(self.base, 0o700)
        self.root = os.path.join(self.base, 'sublime-observer')
        self.out = os.path.join(self.tmp, 'timeline.jsonl')

    def store(self, epoch='ep-4a'):
        st = contract.Store(self.root, epoch, os.getpid(), UID, {}, contract.DEFAULTS['cap_chars'],
                            contract.DEFAULTS['heartbeat_s'])
        ok, reason = st.start()
        self.assertTrue(ok, reason)
        self.addCleanup(st.shutdown)
        return st

    def spawn(self, *extra, forbid=(FORBID,), out=None, root=None):
        cmd = [sys.executable, '-I', '-B', RECORDER, '--out', out or self.out,
               '--root', root or self.root, '--interval-ms', '20']
        for s in forbid:
            cmd += ['--forbid', s]
        proc = subprocess.Popen(cmd + list(extra), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        self.addCleanup(self._reap, proc)
        return proc

    @staticmethod
    def _reap(proc):
        if proc.poll() is None:
            proc.kill()
        proc.communicate(timeout=5)

    def wait_snapshot(self, pred, timeout=5.0):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if os.path.exists(self.out):
                try:
                    for snap in samples(records(self.out)):
                        if pred(snap):
                            return snap
                except ValueError:
                    pass                    # a line mid-write
            time.sleep(0.02)
        self.fail('no snapshot matched within {} s'.format(timeout))

    def wait_last(self, pred, timeout=5.0):
        """Wait until the most recent sample record matches."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                snaps = samples(records(self.out))
            except ValueError:
                snaps = []
            if snaps and pred(snaps[-1]):
                return snaps[-1]
            time.sleep(0.02)
        self.fail('last snapshot did not match within {} s'.format(timeout))

    def stamp(self, proc, text):
        proc.stdin.write((text + '\n').encode())
        proc.stdin.flush()

    def stop(self, proc, sig=signal.SIGTERM):
        proc.send_signal(sig)
        _out, err = proc.communicate(timeout=5)
        return proc.returncode, err.decode('utf-8', 'replace')


def shared_ids(snap):
    return [e.get('share_id') for e in (snap.get('index') or {}).get('shared') or []]


class TimelineTests(Base):
    def test_share_edit_unshare_and_root_removal_are_recorded(self):
        proc = self.spawn()
        self.wait_snapshot(lambda s: s['root']['exists'] is False)
        st = self.store()
        self.stamp(proc, '1 share')
        st.publish('s1', capture(1, TEXT_1))
        first = self.wait_snapshot(lambda s: s.get('read_current', {}).get('revision') == 1)
        self.assertEqual(shared_ids(first), ['s1'])
        self.assertEqual(first['current']['target'], 'views/s1')
        self.assertTrue(first['current']['resolves_inside_root'])
        self.assertEqual(first['publisher']['reader'], 'live')
        view = first['views']['dirs']['s1']
        self.assertEqual(view['state']['text_file'], 'text.s1.1')      # step 5: names carry the share id
        self.assertEqual(view['text']['chars'], len(TEXT_1))
        self.assertTrue(view['text']['chars_equal_published'])
        self.stamp(proc, '2 edit')
        st.publish('s1', capture(2, TEXT_2))
        second = self.wait_snapshot(lambda s: s.get('read_current', {}).get('revision') == 2)
        self.assertNotEqual(second['views']['dirs']['s1']['text']['sha256'], view['text']['sha256'])
        self.assertEqual(second['read_current']['text_chars'], len(TEXT_2))
        proc.stdin.close()                  # EOF must not stop the recorder
        time.sleep(0.3)
        self.assertIsNone(proc.poll())
        st.remove_share('s1')
        gone = self.wait_snapshot(lambda s: s.get('index', {}).get('shared') == [] and
                                  s.get('views', {}).get('dirs') == {})
        self.assertFalse(gone['current']['present'])
        self.assertTrue(gone['read_current']['reason'].startswith('Unavailable'))
        st.shutdown()
        self.wait_last(lambda s: s['root']['exists'] is False)
        code, err = self.stop(proc)
        self.assertEqual(code, 0)
        recs = records(self.out)
        kinds = [r['kind'] for r in recs]
        self.assertEqual(kinds[0], 'start')
        self.assertEqual(kinds[-1], 'end')
        self.assertIn('stdin_eof', kinds)
        self.assertEqual([r['stamp'] for r in recs if r['kind'] == 'stamp'], ['1 share', '2 edit'])
        end = recs[-1]
        self.assertEqual((end['reason'], end['stamps'], end['forbidden_hits']), ('SIGTERM', 2, []))
        self.assertEqual(end['records'], len(recs))
        for r in recs:
            self.assertTrue({'wall', 'mono', 'iso', 'n'} <= set(r), r['kind'])
        # the root disappeared after it had existed
        exists = [s['root']['exists'] for s in samples(recs)]
        self.assertIn(True, exists)
        self.assertFalse(exists[-1])
        self.assertIn('stopped by SIGTERM', err)
        self.assertEqual(stat.S_IMODE(os.stat(self.out).st_mode), 0o600)
        raw = slurp(self.out, 'rb').decode('utf-8')
        for line in set(TEXT_1.splitlines()) | set(TEXT_2.splitlines()):
            self.assertNotIn(line, raw)

    def test_keepalive_when_nothing_changes(self):
        proc = self.spawn()
        time.sleep(2.4)
        code, _err = self.stop(proc, signal.SIGINT)
        self.assertEqual(code, 0)
        recs = [r for r in records(self.out) if r['kind'] == 'sample']
        self.assertGreaterEqual(len(recs), 3)
        self.assertTrue(recs[0]['changed'])
        self.assertTrue(all(not r['changed'] for r in recs[1:]))
        self.assertGreater(recs[-1]['sample_n'], len(recs) * 5)     # sampled far more often than written
        self.assertEqual(records(self.out)[-1]['reason'], 'SIGINT')


class ForbiddenTests(Base):
    def test_planted_string_is_reported_with_the_file_name_and_loudly(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        proc = self.spawn()
        self.wait_snapshot(lambda s: s.get('read_current', {}).get('ok'))
        stray = os.path.join(self.root, 'views', 's1', '.tmp-stray')
        with open(stray, 'w') as handle:
            handle.write('residue ' + FORBID + ' residue')
        hit = self.wait_snapshot(lambda s: s.get('forbidden_hits'))
        self.assertEqual(hit['forbidden_hits'], [{'file': 'views/s1/.tmp-stray', 'forbid': [0]}])
        code, err = self.stop(proc)
        self.assertEqual(code, 0)
        self.assertIn('FORBIDDEN STRING FOUND: views/s1/.tmp-stray', err)
        self.assertEqual(records(self.out)[-1]['forbidden_hits'], [{'file': 'views/s1/.tmp-stray', 'forbid': 0}])
        st.shutdown()

    def test_json_escaped_form_is_found(self):
        st = self.store()
        marker = 'quote"and\\slash'
        st.publish('s1', dict(capture(1, TEXT_1), title=marker))       # lands JSON-escaped in index/state
        snap = wr.snapshot(self.root, wr.forbidden_forms([marker]), wr.load_reader(self.root))
        files = sorted(h['file'] for h in snap['forbidden_hits'])
        self.assertEqual(files, ['index.json', 'views/s1/state.json'])
        st.shutdown()

    def test_text_is_never_stored(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        snap = wr.snapshot(self.root, wr.forbidden_forms([FORBID]), wr.load_reader(self.root))
        self.assertTrue(snap['read_current']['ok'])
        dumped = json.dumps(snap)
        self.assertNotIn(TEXT_1.splitlines()[0], dumped)
        st.shutdown()


class RefusalTests(Base):
    def test_refuses_existing_out(self):
        with open(self.out, 'w') as handle:
            handle.write('keep me\n')
        proc = self.spawn()
        _o, err = proc.communicate(timeout=5)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn('already exists', err.decode())
        self.assertEqual(slurp(self.out), 'keep me\n')

    def test_refuses_dangling_symlink_out(self):
        os.symlink(os.path.join(self.tmp, 'nowhere'), self.out)
        proc = self.spawn()
        proc.communicate(timeout=5)
        self.assertNotEqual(proc.returncode, 0)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, 'nowhere')))

    def test_refuses_out_under_root_even_before_the_root_exists(self):
        for out in (os.path.join(self.root, 'x.jsonl'), os.path.join(self.root, 'views', 'x.jsonl')):
            proc = self.spawn(out=out)
            _o, err = proc.communicate(timeout=5)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('under the root', err.decode())
        self.assertFalse(os.path.lexists(self.root))
        os.mkdir(self.root, 0o700)
        proc = self.spawn(out=os.path.join(self.root, 'y.jsonl'))
        proc.communicate(timeout=5)
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(os.listdir(self.root), [])

    def test_refuses_empty_forbid(self):
        proc = self.spawn(forbid=('',))
        proc.communicate(timeout=5)
        self.assertNotEqual(proc.returncode, 0)
        self.assertFalse(os.path.lexists(self.out))


class ContainmentTests(Base):
    def outside(self):
        far = os.path.join(self.tmp, 'outside')
        os.mkdir(far, 0o700)
        with open(os.path.join(far, 'state.json'), 'w') as handle:
            json.dump({'epoch': 'ep-4a', 'text_file': 'text.9', 'text_file_encoding': 'utf-8',
                       'title': 'OUTSIDE-STATE-MARKER', 'published_chars': 3}, handle)
        with open(os.path.join(far, 'text.9'), 'w') as handle:
            handle.write('OUTSIDE-TEXT-MARKER')
        return far

    def test_current_pointing_outside_is_not_followed(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        far = self.outside()
        link = os.path.join(self.root, 'current')
        os.unlink(link)
        os.symlink(far, link)
        snap = wr.snapshot(self.root, wr.forbidden_forms(['OUTSIDE-TEXT-MARKER', 'OUTSIDE-STATE-MARKER']),
                           wr.load_reader(self.root))
        self.assertEqual(snap['current']['target'], far)
        self.assertFalse(snap['current']['resolves_inside_root'])
        self.assertFalse(snap['read_current']['ok'])
        self.assertIn('not followed', snap['read_current']['reason'])
        self.assertEqual(snap['forbidden_hits'], [])
        dumped = json.dumps(snap)
        self.assertNotIn('OUTSIDE-STATE-MARKER', dumped)
        self.assertNotIn('OUTSIDE-TEXT-MARKER', dumped)
        st.shutdown()

    def test_reader_is_guarded_against_a_text_file_that_escapes(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        far = self.outside()
        spath = os.path.join(self.root, 'views', 's1', 'state.json')
        state = json.loads(slurp(spath))
        state['text_file'] = os.path.join(far, 'text.9')          # absolute: os.path.join would leave the root
        with open(spath, 'w') as handle:
            json.dump(state, handle)
        snap = wr.snapshot(self.root, wr.forbidden_forms([FORBID]), wr.load_reader(self.root))
        self.assertFalse(snap['read_current']['ok'])
        self.assertIn('refused', snap['read_current']['reason'])
        self.assertIn('not a plain file name', snap['views']['dirs']['s1']['text']['note'])
        self.assertNotIn('OUTSIDE-TEXT-MARKER', json.dumps(snap))
        st.shutdown()

    def test_symlinked_view_dir_and_fifo_are_not_entered(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        far = self.outside()
        os.symlink(far, os.path.join(self.root, 'views', 'evil'))
        os.mkfifo(os.path.join(self.root, 'views', 's1', 'pipe'))
        snap = wr.snapshot(self.root, wr.forbidden_forms(['OUTSIDE-TEXT-MARKER']), wr.load_reader(self.root))
        self.assertEqual(snap['views']['dirs']['evil']['type'], 'symlink')
        kinds = {e['name']: e['type'] for e in snap['entries']}
        self.assertEqual(kinds['views/evil'], 'symlink')
        self.assertEqual(kinds['views/s1/pipe'], 'other')
        self.assertNotIn('views/evil/text.9', kinds)
        self.assertEqual(snap['forbidden_hits'], [])
        st.shutdown()


class ErrorTests(Base):
    def test_bad_json_and_vanished_files_are_recorded_not_fatal(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        with open(os.path.join(self.root, 'index.json'), 'w') as handle:
            handle.write('{not json')
        os.unlink(os.path.join(self.root, 'views', 's1', 'text.s1.1'))
        snap = wr.snapshot(self.root, wr.forbidden_forms([FORBID]), wr.load_reader(self.root))
        self.assertTrue(any(e['path'] == 'index.json' and e['error'].startswith('bad json') for e in snap['errors']))
        self.assertEqual(snap['views']['dirs']['s1']['text'], {'exists': False})
        self.assertFalse(snap['read_current']['ok'])
        st.shutdown()

    def test_stale_heartbeat_is_reported_by_the_reader(self):
        st = self.store()
        st.publish('s1', capture(1, TEXT_1))
        later = time.time() + 10
        snap = wr.snapshot(self.root, wr.forbidden_forms([FORBID]), wr.load_reader(self.root), wall=later)
        self.assertEqual(snap['publisher']['reader'], 'not live: heartbeat is stale')
        self.assertIn('NotLive', snap['read_current']['reason'])
        st.shutdown()


if __name__ == '__main__':
    unittest.main()
