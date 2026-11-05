"""Public applied-owner CLI + actual ttyd, on explicit disposable sockets only."""
import asyncio
import base64
import contextlib
import json
import os
from pathlib import Path
import secrets
import shlex
import tempfile
import unittest
from unittest.mock import patch

from aiohttp import WSMsgType
from aiohttp.test_utils import TestClient, TestServer

from host.owner_sessions import OwnerSessions
from host.security import APIError
from host.server import create_app

OWNER = Path('/home/hruzam/ia-sync/zsh/session/ovitmugen.py')
BINARY = Path('/tmp/phone-console-ttyd-1.7.7/ttyd')
ORIGIN = 'http://owner-console.test:18790'
HEADERS = {'Host': 'owner-console.test:18790', 'Authorization': 'Basic ' +
           base64.b64encode(b'owner-test:private-only').decode()}
ACTION = {**HEADERS, 'Origin': ORIGIN, 'X-Console-Action': '1'}


@unittest.skipUnless(BINARY.is_file() and OWNER.is_file() and 'def cmd_phone_view' in OWNER.read_text(),
                     'Applied public owner phone API and pinned ttyd required')
class OwnerAdapterTests(unittest.IsolatedAsyncioTestCase):
    async def control(self, *args, check=True):
        assert self.socket_name.startswith('pc-owner-test-')
        env = dict(os.environ)
        env.pop('TMUX', None)
        child = await asyncio.create_subprocess_exec('tmux', '-L', self.socket_name,
            '-f', '/dev/null', *args, env=env, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        out, error = await child.communicate()
        if check:
            self.assertEqual(child.returncode, 0, error.decode())
        return child.returncode, out.decode().strip()

    async def populate(self):
        await self.control('new-session', '-d', '-s', 'alpha', '-n', 'first',
                           'env', 'PC_PICKED=alpha-first', 'bash', '--noprofile', '--norc', '-i')
        await self.control('new-window', '-d', '-t', '=alpha:', '-n', 'second',
                           'env', 'PC_PICKED=alpha-second', 'bash', '--noprofile', '--norc', '-i')
        await self.control('new-session', '-d', '-s', 'alpha--left', '-t', '=alpha')
        await self.control('select-window', '-t', '=alpha--left:0')
        await self.control('new-session', '-d', '-s', 'beta', '-n', 'third',
                           'env', 'PC_PICKED=beta-third', 'bash', '--noprofile', '--norc', '-i')
        await self.control('new-session', '-d', '-s', 'beta--left', '-t', '=beta')

    async def asyncSetUp(self):
        self.socket_name = f'pc-owner-test-{os.getpid()}-{secrets.token_hex(4)}'
        self.temp = tempfile.TemporaryDirectory(prefix='pc-owner-test-')
        self.root = Path(self.temp.name)
        await self.populate()
        credential = self.root / 'credential.json'
        credential.write_text(json.dumps({'credential': 'owner-test:private-only'}))
        credential.chmod(0o600)
        self.config = {'mode': 'live', 'ovitmugen_script': str(OWNER), 'agents_socket': self.socket_name,
            'credential_file': str(credential), 'runtime_root': str(self.root / 'runtime'),
            'vault_root': str(self.root / 'vault'), 'ttyd_binary': str(BINARY), 'public_origin': ORIGIN}
        self.app = create_app(self.config, install_storage=False)
        self.sessions = self.app['sessions']
        self.proxy = self.app['terminal_proxy']
        self.client = TestClient(TestServer(self.app))
        await self.client.start_server()

    async def asyncTearDown(self):
        await self.client.close()
        await self.control('kill-server', check=False)
        self.temp.cleanup()

    async def selected(self):
        targets = await self.sessions.targets()
        return next(row for row in targets if row['bed'] == 'alpha' and 'second' in row['label'])

    async def new_view(self):
        target = await self.selected()
        response = await self.client.post('/api/views', headers=ACTION,
            json={'targetId': target['id'], 'generation': target['generation']})
        self.assertEqual(response.status, 201, await response.text())
        return await response.json()

    async def connect(self, view):
        ws = await self.client.ws_connect(view['wsPath'], headers=HEADERS, origin=ORIGIN, protocols=('tty',))
        await ws.send_str(json.dumps({'binding': view['binding'], 'columns': 70, 'rows': 25}))
        for _ in range(20):
            message = await ws.receive(timeout=5)
            if message.type == WSMsgType.BINARY and message.data.startswith(b'0'):
                return ws
            self.assertNotEqual(message.type, WSMsgType.CLOSE, message.data)
        self.fail('Owner target did not produce terminal output')

    async def test_discovery_and_disabled_lifecycle(self):
        response = await self.client.get('/api/state', headers=HEADERS)
        self.assertEqual(response.status, 200)
        state = await response.json()
        self.assertEqual(state['mode'], 'live')
        self.assertTrue(state['capabilities']['live'])
        self.assertFalse(state['capabilities']['createFixture'])
        self.assertFalse(state['capabilities']['endFixture'])
        self.assertEqual({row['bed'] for row in state['targets']}, {'alpha', 'beta'})
        self.assertTrue(all(row['kind'] == 'live' and not row['canEnd'] for row in state['targets']))
        target = state['targets'][0]
        response = await self.client.post('/api/fixtures', headers=ACTION, json={'name': 'forbidden'})
        self.assertEqual(response.status, 501)
        response = await self.client.delete('/api/fixtures/' + target['id'], headers=ACTION,
            json={'generation': target['generation'], 'confirm': True})
        self.assertEqual(response.status, 501)
        self.assertEqual(len(await self.sessions.targets()), 3)

    async def test_selected_input_independent_view_and_detach_survival(self):
        target = await self.selected()
        await self.control('set-option', '-w', '-t', target['windowId'], 'window-size', 'largest')
        _, before = await self.control('list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}')
        _, desktop_before = await self.control('display-message', '-p', '-t', '=alpha--left:', '#{window_id}')
        view = await self.new_view()
        ws = await self.connect(view)
        output = self.root / 'selected.txt'
        command = 'printf %s "${PC_PICKED}:příliš žluťoučký kůň" > ' + shlex.quote(str(output))
        await ws.send_bytes(b'0' + command.encode())
        await asyncio.sleep(.1)
        self.assertFalse(output.exists())
        await ws.send_bytes(b'0\r')
        for _ in range(50):
            if output.exists():
                break
            await asyncio.sleep(.05)
        self.assertEqual(output.read_bytes(), 'alpha-second:příliš žluťoučký kůň'.encode())
        _, desktop_after = await self.control('display-message', '-p', '-t', '=alpha--left:', '#{window_id}')
        self.assertEqual(desktop_after, desktop_before)
        _, policy = await self.control('show-option', '-w', '-v', '-t', target['windowId'], 'window-size')
        self.assertEqual(policy, 'largest', 'Live attach must not change shared window policy')
        await ws.close()
        await self.proxy.remove(view['viewId'])
        _, after = await self.control('list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}')
        self.assertEqual(after, before)

    async def test_diverged_view_refuses_input_resize_and_history(self):
        view = await self.new_view()
        ws = await self.connect(view)
        cap = self.proxy.views[view['viewId']]['session']
        await self.control('select-window', '-t', '=' + cap['name'] + ':0')
        marker = self.root / 'must-not-exist'
        with contextlib.suppress(ConnectionResetError):
            await ws.send_bytes(('0touch ' + shlex.quote(str(marker)) + '\r').encode())
        for _ in range(30):
            message = await ws.receive(timeout=3)
            if message.type == WSMsgType.CLOSE:
                self.assertEqual(message.data, 4009)
                break
        else:
            self.fail('Diverged view stayed connected')
        self.assertFalse(marker.exists())
        response = await self.client.post('/api/views/' + view['viewId'] + '/history', headers=ACTION,
            json={'action': 'enter', 'binding': view['binding']})
        self.assertEqual(response.status, 409)
        await ws.close()

    async def test_history_uses_only_bound_copy_mode(self):
        view = await self.new_view()
        ws = await self.connect(view)
        for action in ['leave', 'enter', 'pageUp', 'pageDown', 'leave', 'leave']:
            response = await self.client.post('/api/views/' + view['viewId'] + '/history', headers=ACTION,
                json={'action': action, 'binding': view['binding']})
            self.assertEqual(response.status, 200, await response.text())
        await ws.close()

    async def test_changed_owner_marker_refuses_binding(self):
        view = await self.new_view()
        internal = self.proxy.views[view['viewId']]
        cap = internal['session']
        await self.control('set-option', '-t', '=' + cap['name'] + ':', '@ov-phone-token', 'wrong')
        with self.assertRaises(APIError) as error:
            await self.sessions.validate_view(internal)
        self.assertEqual(error.exception.code, 'stale')
        # Cleanup must preserve a view whose token ownership was changed externally.
        await self.proxy.remove(view['viewId'])
        self.assertEqual((await self.control('has-session', '-t', '=' + cap['name'], check=False))[0], 0)

    async def test_failed_post_create_validation_cleans_only_owned_view(self):
        target = await self.selected()
        _, before = await self.control('list-sessions', '-F', '#{session_name}')
        with patch.object(self.sessions, 'validate_view', side_effect=APIError(409, 'stale', 'Injected failure')):
            with self.assertRaises(APIError):
                await self.sessions.view(target)
        _, after = await self.control('list-sessions', '-F', '#{session_name}')
        self.assertEqual(after, before)

    async def test_rejected_attach_argv_cleans_only_owned_view(self):
        target = await self.selected()
        _, before = await self.control('list-sessions', '-F', '#{session_name}')
        original = self.sessions.owner
        async def wrong_argv(*args):
            result = await original(*args)
            if args[:2] == ('phone-view', 'create'):
                result['attachArgv'] = ['refuse-this-command']
            return result
        with patch.object(self.sessions, 'owner', side_effect=wrong_argv):
            with self.assertRaises(APIError):
                await self.sessions.view(target)
        _, after = await self.control('list-sessions', '-F', '#{session_name}')
        self.assertEqual(after, before)

    async def test_history_never_falls_back_to_prefix_session(self):
        view = await self.new_view()
        internal = self.proxy.views[view['viewId']]
        cap = internal['session']
        original = self.sessions._tmux_read
        injected = False
        async def replace_before_history(*args):
            nonlocal injected
            if args[0] == 'copy-mode':
                injected = True
                await self.control('new-session', '-d', '-s', cap['name'] + '-other', '-t', '=alpha')
                await self.control('kill-session', '-t', '=' + cap['name'])
            return await original(*args)
        with patch.object(self.sessions, '_tmux_read', side_effect=replace_before_history):
            with self.assertRaises(APIError):
                await self.sessions.history(internal, 'enter')
        self.assertTrue(injected)
        _, mode = await self.control('display-message', '-p', '-t', view['target']['paneId'], '#{pane_in_mode}')
        self.assertEqual(mode, '0')

    async def test_pane_respawn_and_server_restart_stale_no_replay(self):
        target = await self.selected()
        await self.control('respawn-pane', '-k', '-t', target['paneId'], 'bash', '--noprofile', '--norc', '-i')
        with self.assertRaises(APIError):
            await self.sessions.resolve(target['id'], target['generation'])
        view = await self.new_view()
        internal = self.proxy.views[view['viewId']]
        cap = internal['session']
        await self.control('kill-server')
        # Wait for the old server to release its socket before recreating it.
        for _ in range(100):
            if not Path('/tmp/tmux-' + str(os.getuid()), self.socket_name).exists():
                break
            await asyncio.sleep(.02)
        await self.populate()
        _, replacement_id = await self.control('new-session', '-d', '-P', '-F', '#{session_id}',
                                               '-s', 'unrelated-replacement', '-t', '=alpha')
        self.assertEqual(replacement_id, cap['viewId'], 'Must deliberately reuse old numeric view ID')
        _, before = await self.control('list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}')
        with self.assertRaises(APIError):
            await self.sessions.validate_view(internal)
        await self.proxy.remove(view['viewId'])
        self.assertEqual((await self.control('has-session', '-t', '=unrelated-replacement', check=False))[0], 0)
        _, after = await self.control('list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}')
        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
