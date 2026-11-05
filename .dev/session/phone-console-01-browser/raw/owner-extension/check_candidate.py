#!/usr/bin/env python3
"""Apply review patch to stdout, then test ONLY uniquely named disposable sockets."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import secrets
import shlex
import subprocess
import tempfile
import threading
import time
import types
import unittest
from unittest.mock import patch

SOURCE = Path('/home/hruzam/ia-sync/zsh/session/ovitmugen.py')
BASE_SHA = '97dba115a36abf216ab6f5deabda601ce82e395cdd285a1b52aca7568f5a3125'
PATCH = Path(__file__).with_name('ovitmugen.phone-api.proposed.patch')
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == BASE_SHA
candidate = subprocess.run(['patch', '--silent', '-o', '-', str(SOURCE), str(PATCH)],
                           check=True, capture_output=True, text=True).stdout
m = types.ModuleType('review_candidate')
# The existing selftest needs its real read-only frame configuration beside source.
m.__file__ = str(SOURCE)
exec(compile(candidate, 'ovitmugen.owner-review.memory.py', 'exec'), m.__dict__)


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.env = {key: os.environ.get(key) for key in
                    ('OV_AGENTS_SOCKET', 'OV_AGENTS_CONF', 'OV_FRAME_SOCKET', 'TMUX')}
        tag = f'ov-phone-check-{os.getpid()}-{secrets.token_hex(4)}'
        os.environ.update(OV_AGENTS_SOCKET=tag, OV_AGENTS_CONF='/dev/null', OV_FRAME_SOCKET=tag + '-frame')
        os.environ.pop('TMUX', None)
        self.A = m.servers()[0]
        self.A.run('new-session', '-d', '-s', 'bed', '-n', 'alpha',
                   'bash', '--noprofile', '--norc', '-i', check=True)
        self.A.run('new-window', '-d', '-t', '=bed:', '-n', 'beta',
                   'bash', '--noprofile', '--norc', '-i', check=True)
        self.A.run('new-session', '-d', '-s', 'bed--left', '-t', '=bed', check=True)
        self.A.run('select-window', '-t', '=bed--left:0', check=True)

    def tearDown(self):
        self.A.run('kill-server')
        for key, value in self.env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), BASE_SHA)

    def target(self, index=0, bed='bed'):
        return m.exact_targets(bed)['targets'][index]

    def command(self, args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = m.main(args)
        self.assertEqual(result, 0, args)
        return json.loads(output.getvalue())

    def create(self, index=0):
        row = self.target(index)
        return self.command(['phone-view', 'create', 'bed', '--window', row['windowId'],
                             '--pane', row['paneId'], '--generation', row['generation']])

    @staticmethod
    def view_args(action, view):
        return ['phone-view', action, 'bed', '--view', view['name'], '--token', view['token'],
                '--server-generation', view['serverGeneration']]

    def pids(self):
        return self.A.run('list-panes', '-s', '-t', '=bed', '-F', '#{pane_id}:#{pane_pid}', check=True).stdout

    def replacement(self, old_id, original_run):
        # Deliberately restart and allocate a new, unrelated session with the OLD numeric ID.
        original_run(self.A, 'kill-server', check=True)
        for _ in range(30):
            result = original_run(self.A, 'new-session', '-d', '-s', 'bed', '-n', 'alpha',
                                  'bash', '--noprofile', '--norc', '-i')
            if result.returncode == 0:
                break
            time.sleep(.03)
        self.assertEqual(result.returncode, 0)
        original_run(self.A, 'new-window', '-d', '-t', '=bed:', '-n', 'beta',
                     'bash', '--noprofile', '--norc', '-i', check=True)
        for index in range(1, int(old_id[1:]) + 1):
            name = 'unrelated-replacement' if '$' + str(index) == old_id else f'other-{index}'
            original_run(self.A, 'new-session', '-d', '-s', name, '-t', '=bed', check=True)
        got = original_run(self.A, 'display-message', '-p', '-t', '=unrelated-replacement:',
                           '#{session_id}', check=True).stdout.strip()
        self.assertEqual(got, old_id, 'Regression fixture must actually reuse the stale numeric ID')
        original_run(self.A, 'select-window', '-t', '=unrelated-replacement:0', check=True)
        return (original_run(self.A, 'list-panes', '-s', '-t', '=bed', '-F', '#{pane_id}:#{pane_pid}',
                            check=True).stdout,
                original_run(self.A, 'display-message', '-p', '-t', '=unrelated-replacement:',
                            '#{window_id}', check=True).stdout)

    def assert_replacement_untouched(self, expected):
        self.assertEqual(self.pids(), expected[0])
        self.assertTrue(self.A.has('unrelated-replacement'))
        self.assertEqual(self.A.run('display-message', '-p', '-t', '=unrelated-replacement:',
                                   '#{window_id}', check=True).stdout, expected[1])

    def test_views_desktop_shape_and_detach_lifetime(self):
        before = m.bed_report('bed')
        pids = self.pids()
        first, second = self.create(0), self.create(1)
        self.assertNotEqual(first['name'], second['name'])
        row = self.target(1)
        self.command(self.view_args('select', first) + ['--window', row['windowId'],
                     '--pane', row['paneId'], '--generation', row['generation']])
        self.assertEqual(m.view_current(self.A, 'bed--left'), self.target(0)['windowId'])
        self.assertEqual(set(before), set(m.bed_report('bed')))
        self.assertEqual(set(before['tabs'][0]), set(m.bed_report('bed')['tabs'][0]))
        self.command(self.view_args('detach', first))
        self.assertEqual(self.pids(), pids)
        self.assertTrue(self.A.has(second['name']))

    def test_restart_id_reuse_on_detach(self):
        view = self.create()
        original_run, expected = m.Tmux.run, []
        def intercept(instance, *args, **kwargs):
            if not expected and args[:1] == ('kill-session',):
                self.assertEqual(args[-1], '=' + view['name'])
                expected.append(self.replacement(view['viewId'], original_run))
            return original_run(instance, *args, **kwargs)
        with patch.object(m.Tmux, 'run', intercept), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(self.view_args('detach', view)), 1)
        self.assert_replacement_untouched(expected[0])

    def test_restart_id_reuse_on_select(self):
        view, row = self.create(), self.target(1)
        original_run, expected = m.Tmux.run, []
        def intercept(instance, *args, **kwargs):
            if not expected and args[:1] == ('select-window',):
                self.assertTrue(args[-1].startswith('=' + view['name'] + ':'))
                expected.append(self.replacement(view['viewId'], original_run))
            return original_run(instance, *args, **kwargs)
        with patch.object(m.Tmux, 'run', intercept), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(self.view_args('select', view) + ['--window', row['windowId'],
                '--pane', row['paneId'], '--generation', row['generation']]), 1)
        self.assert_replacement_untouched(expected[0])

    def test_restart_id_reuse_in_failed_create_cleanup(self):
        original_run, expected, old_id = m.Tmux.run, [], []
        def intercept(instance, *args, **kwargs):
            if args[:1] == ('new-session',) and '-P' in args:
                result = original_run(instance, *args, **kwargs)
                old_id.append(result.stdout.strip())
                return result
            if old_id and not expected and args[:1] == ('select-window',):
                expected.append(self.replacement(old_id[0], original_run))
                raise m.OvError('Injected create failure after restart')
            if expected and args[:1] == ('kill-session',):
                self.fail('Cleanup must preserve on generation mismatch, without issuing kill-session')
            return original_run(instance, *args, **kwargs)
        row = self.target()
        with patch.object(m.Tmux, 'run', intercept), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(['phone-view', 'create', 'bed', '--window', row['windowId'],
                '--pane', row['paneId'], '--generation', row['generation']]), 1)
        self.assertTrue(expected, 'Restart injection precondition must be reached')
        self.assert_replacement_untouched(expected[0])

    def test_wrong_capability_or_orphan_preserves_views(self):
        view = self.create()
        wrong = {**view, 'token': 'wrong'}
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(self.view_args('detach', wrong)), 1)
            self.assertEqual(m.main(self.view_args('detach', {**view, 'name': 'bed--left'})), 1)
        self.assertTrue(self.A.has(view['name']))
        pids = self.pids()
        self.A.run('kill-session', '-t', '=bed', check=True)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(self.view_args('detach', view)), 1)
        self.assertTrue(self.A.has(view['name']))
        self.assertEqual(self.A.run('list-panes', '-s', '-t', '=' + view['name'],
                                    '-F', '#{pane_id}:#{pane_pid}', check=True).stdout, pids)

    def test_close_preserves_owner_patience(self):
        with tempfile.TemporaryDirectory(prefix='ov-phone-patience-') as directory:
            gate = Path(directory) / 'release'
            command = 'while test ! -e ' + shlex.quote(str(gate)) + '; do sleep .05; done; exec bash --noprofile --norc -i'
            self.A.run('new-window', '-d', '-t', '=bed:', '-n', 'transient',
                       'bash', '-c', command, check=True)
            deadline = time.monotonic() + 2
            while True:
                row = next(t for t in m.exact_targets('bed')['targets'] if t['name'] == 'transient')
                if row['busy'] or time.monotonic() >= deadline:
                    break
                time.sleep(.01)
            self.assertTrue(row['busy'], 'A real transient child must be present at initial validation')
            original_close, entered = m.close_idle_tab, []
            def release_in_owner_loop(*args, **kwargs):
                entered.append(True)
                release = threading.Timer(.1, gate.touch)
                release.start()
                try:
                    return original_close(*args, **kwargs)
                finally:
                    release.join()
            with patch.object(m, 'close_idle_tab', release_in_owner_loop):
                self.command(['close-tab', 'bed', '--window', row['windowId'], '--pane', row['paneId'],
                              '--generation', row['generation'], '--confirm'])
            self.assertTrue(entered, 'Initial validation must reach the existing owner patience loop')
            self.assertNotIn(row['windowId'], [t['windowId'] for t in m.exact_targets('bed')['targets']])

    def test_busy_stale_multi_and_missing_confirmation_refuse(self):
        row = self.target(1)
        args = ['close-tab', 'bed', '--window', row['windowId'], '--pane', row['paneId'],
                '--generation', row['generation']]
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(args), 1)
        self.A.run('respawn-pane', '-k', '-t', row['paneId'], 'sleep', '60', check=True)
        with self.assertRaises(m.OvError):
            m._exact('bed', row['windowId'], row['paneId'], row['generation'])
        busy = self.target(1)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(['close-tab', 'bed', '--window', busy['windowId'], '--pane', busy['paneId'],
                '--generation', busy['generation'], '--confirm']), 1)
        self.A.run('split-window', '-d', '-t', row['paneId'], 'sleep', '60', check=True)
        multi = self.target(1)
        with self.assertRaises(m.OvError):
            m._exact('bed', multi['windowId'], multi['paneId'], multi['generation'])

    def test_existing_owner_selftest(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(m.selftest(), 0, output.getvalue())

    def test_command_specific_exact_name_syntax(self):
        name = 'bed--phone-' + secrets.token_hex(8)
        self.A.run('new-session', '-d', '-s', name, '-t', '=bed', check=True)
        self.A.run('set-option', '-t', '=' + name + ':', '@syntax-proof', 'yes', check=True)
        marker = self.A.run('show-options', '-v', '-t', '=' + name + ':', '@syntax-proof', check=True).stdout.strip()
        self.assertEqual(marker, 'yes')
        self.A.run('kill-session', '-t', '=' + name, check=True)
        self.assertFalse(self.A.has(name))


if __name__ == '__main__':
    unittest.main(verbosity=2)
