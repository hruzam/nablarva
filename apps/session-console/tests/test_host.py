"""Security and terminal transitions on private disposable test sockets only."""
import asyncio
import base64
import json
from pathlib import Path
import shlex
import tempfile
import unittest
from unittest.mock import patch
import subprocess
import sys

from aiohttp import WSMsgType, WSServerHandshakeError
from aiohttp.test_utils import TestClient, TestServer

from host.security import APIError
from host.server import create_app
from host.sessions import FixtureSessions
from host.terminal_proxy import client_frame, dimensions

BINARY = Path('/tmp/phone-console-ttyd-1.7.7/ttyd')
ORIGIN = 'http://console.test:18790'
CREDENTIAL = 'test:private-fixture-password'
HEADERS = {'Host': 'console.test:18790', 'Authorization': 'Basic ' +
           base64.b64encode(CREDENTIAL.encode()).decode()}
ACTION = {**HEADERS, 'Origin': ORIGIN, 'X-Console-Action': '1'}


class FrameTests(unittest.TestCase):
    def test_valid_and_invalid_input(self):
        data = '0příliš žluťoučký kůň'.encode()
        self.assertEqual(client_frame(data), data)
        for data in [b'', b'9arbitrary', b'0\xff', b'0' * (256 * 1024 + 1), b'2anything']:
            with self.assertRaises((APIError, UnicodeError)):
                client_frame(data)
        self.assertEqual(client_frame(b'2'), b'2')

    def test_dimensions_and_resize(self):
        self.assertEqual(dimensions({'columns': 80, 'rows': 24}), {'columns': 80, 'rows': 24})
        for size in [{'columns': True, 'rows': 20}, {'columns': 0, 'rows': 20},
                     {'columns': 80, 'rows': 201}]:
            with self.assertRaises(APIError):
                dimensions(size)
        self.assertEqual(json.loads(client_frame(b'1{"columns":47,"rows":24}')[1:]),
                         {'columns': 47, 'rows': 24})


@unittest.skipUnless(BINARY.is_file(), 'Pinned disposable ttyd dependency not present')
class HostTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pc-test-')
        self.root = Path(self.temp.name)
        self.sessions = FixtureSessions(self.root / 'tmux.sock')
        await self.sessions.tmux('-f', '/dev/null', 'new-session', '-d', '-s', 'desktop',
                                 'bash', '--noprofile', '--norc', '-i')
        secret = self.root / 'credential.json'
        secret.write_text(json.dumps({'credential': CREDENTIAL}))
        secret.chmod(0o600)
        config = {'credential_file': str(secret), 'runtime_root': str(self.root / 'runtime'),
            'vault_root': str(self.root / 'vault'), 'fixture_socket': str(self.sessions.socket),
            'ttyd_binary': str(BINARY), 'public_origin': ORIGIN}
        self.app = create_app(config, sessions=self.sessions, install_storage=False)
        self.client = TestClient(TestServer(self.app))
        await self.client.start_server()

    async def asyncTearDown(self):
        await self.client.close()
        if self.sessions.socket.exists():
            await self.sessions.tmux('kill-server')
        self.temp.cleanup()

    async def test_auth_origin_host_and_csrf(self):
        response = await self.client.get('/api/state', headers={'Host': HEADERS['Host']})
        self.assertEqual(response.status, 401)
        self.assertIn('Basic', response.headers['WWW-Authenticate'])
        response = await self.client.get('/api/state', headers={**HEADERS, 'Authorization': 'Basic wrong'})
        self.assertEqual(response.status, 401)
        response = await self.client.get('/api/state', headers=HEADERS)
        self.assertEqual(response.status, 200)
        self.assertEqual((await response.json())['mode'], 'fixture')
        for headers in [{**HEADERS, 'Host': 'evil.test'},
                        {**HEADERS, 'Origin': ORIGIN.replace('http:', 'https:')},
                        {**HEADERS, 'Origin': 'null'}]:
            self.assertEqual((await self.client.get('/api/state', headers=headers)).status, 403)
        for headers in [HEADERS, {**ACTION, 'Origin': 'http://foreign.test'},
                        {**ACTION, 'Origin': 'null'}, {**HEADERS, 'Origin': ORIGIN}]:
            response = await self.client.post('/api/fixtures', headers=headers, json={'name': 'fixture'})
            self.assertEqual(response.status, 403)
        response = await self.client.post('/api/fixtures', headers=ACTION, json={'name': 'fixture'})
        self.assertEqual(response.status, 201)

    async def test_guarded_close_and_stale(self):
        base = (await self.sessions.targets())[0]
        response = await self.client.delete('/api/fixtures/' + base['id'], headers=ACTION,
            json={'generation': base['generation'], 'confirm': True})
        self.assertEqual(response.status, 403)
        target = await self.sessions.create('owned')
        response = await self.client.delete('/api/fixtures/' + target['id'], headers=ACTION,
            json={'generation': 'stale', 'confirm': True})
        self.assertEqual(response.status, 409)
        response = await self.client.delete('/api/fixtures/' + target['id'], headers=ACTION,
            json={'generation': target['generation'], 'confirm': True})
        self.assertEqual(response.status, 200)
        self.assertTrue(await self.sessions.targets(), 'Base survives owned workbench end')

    async def test_office_listing_uses_only_fixed_read_only_command(self):
        output = 'office-bed\n  ● 0 codex @12 codex\n'
        with patch('host.server.subprocess.run', return_value=subprocess.CompletedProcess(
                [], 0, stdout=output, stderr='')) as command:
            response = await self.client.get('/api/office-workbenches', headers={'Host': HEADERS['Host']})
            self.assertEqual(response.status, 401)
            response = await self.client.get('/api/office-workbenches',
                headers={**HEADERS, 'Origin': 'http://foreign.test'})
            self.assertEqual(response.status, 403)
            response = await self.client.get('/api/office-workbenches?command=down', headers=HEADERS)
            self.assertEqual(response.status, 400)
            command.assert_not_called()
            response = await self.client.get('/api/office-workbenches', headers=HEADERS)
            self.assertEqual(response.status, 200)
            self.assertEqual(await response.json(), {'output': output})
            self.assertEqual(response.headers['Cache-Control'], 'no-store')
            command.assert_called_once_with([sys.executable,
                str(Path.home() / '.config/zsh/session/ovitmugen.py'), 'ls'],
                capture_output=True, text=True, timeout=15, check=False)

    async def test_office_listing_reports_failure_and_timeout(self):
        with patch('host.server.subprocess.run', return_value=subprocess.CompletedProcess(
                [], 1, stdout='', stderr='failure')):
            response = await self.client.get('/api/office-workbenches', headers=HEADERS)
            self.assertEqual(response.status, 503)
            self.assertEqual((await response.json())['error']['code'], 'office_unavailable')
        with patch('host.server.subprocess.run', side_effect=subprocess.TimeoutExpired([], 15)):
            response = await self.client.get('/api/office-workbenches', headers=HEADERS)
            self.assertEqual(response.status, 504)
            self.assertEqual((await response.json())['error']['code'], 'office_timeout')

    async def test_busy_close_is_refused(self):
        target = await self.sessions.create('busy')
        await self.sessions.tmux('respawn-pane', '-k', '-t', target['paneId'], 'sleep', '60')
        busy = next(item for item in await self.sessions.targets() if item['id'] == target['id'])
        self.sessions.owned[busy['windowId']] = busy['generation']
        with self.assertRaises(APIError) as caught:
            await self.sessions.end(busy['id'], busy['generation'])
        self.assertEqual(caught.exception.code, 'busy')
        with self.assertRaises(APIError) as caught:
            await self.sessions.resolve(target['id'], target['generation'])
        self.assertEqual(caught.exception.code, 'stale')

    async def new_view(self):
        target = (await self.sessions.targets())[0]
        response = await self.client.post('/api/views', headers=ACTION,
            json={'targetId': target['id'], 'generation': target['generation']})
        self.assertEqual(response.status, 201, await response.text())
        return await response.json()

    async def open_view(self, view):
        ws = await self.client.ws_connect(view['wsPath'], headers=HEADERS, origin=ORIGIN, protocols=('tty',))
        await ws.send_str(json.dumps({'binding': view['binding'], 'columns': 47, 'rows': 24}))
        for _ in range(20):
            message = await ws.receive(timeout=3)
            if message.type == WSMsgType.BINARY and message.data.startswith(b'0'):
                return ws
            self.assertNotEqual(message.type, WSMsgType.CLOSE, message.data)
        self.fail('No terminal output')

    async def test_proxy_auth_unicode_no_replay_and_detach_survival(self):
        view = await self.new_view()
        ws = await self.open_view(view)
        stored = self.root / 'unicode.txt'
        text = 'příliš žluťoučký kůň'
        await ws.send_bytes(('0printf %s ' + shlex.quote(text) + ' > ' + shlex.quote(str(stored))).encode())
        await asyncio.sleep(.15)
        self.assertFalse(stored.exists(), 'Paste alone must not submit')
        await ws.send_bytes(b'0\r')
        for _ in range(40):
            if stored.exists():
                break
            await asyncio.sleep(.05)
        self.assertEqual(stored.read_bytes(), text.encode())
        pane_pid = (await self.sessions.targets())[0]['generation']
        await ws.close()
        self.assertEqual((await self.sessions.targets())[0]['generation'], pane_pid)
        self.assertEqual((await self.client.get('/token', headers=HEADERS)).status, 404)
        response = await self.client.delete('/api/views/' + view['viewId'], headers=ACTION)
        self.assertEqual(response.status, 200)

    async def test_wrong_binding_cannot_start_backend(self):
        view = await self.new_view()
        ws = await self.client.ws_connect(view['wsPath'], headers=HEADERS, origin=ORIGIN, protocols=('tty',))
        await ws.send_str(json.dumps({'binding': 'wrong', 'columns': 47, 'rows': 24}))
        message = await ws.receive(timeout=3)
        self.assertEqual(message.type, WSMsgType.CLOSE)
        self.assertEqual(message.data, 4003)
        await ws.close()

    async def test_websocket_auth_and_exact_origin_before_upgrade(self):
        view = await self.new_view()
        for headers, origin, expected in [
            ({'Host': HEADERS['Host']}, ORIGIN, 401),
            ({**HEADERS, 'Authorization': 'Basic wrong'}, ORIGIN, 401),
            (HEADERS, None, 403),
            (HEADERS, 'null', 403),
            (HEADERS, ORIGIN.replace('http:', 'https:'), 403),
            (HEADERS, 'http://foreign.test:18790', 403)]:
            with self.assertRaises(WSServerHandshakeError) as caught:
                await self.client.ws_connect(view['wsPath'], headers=headers, origin=origin, protocols=('tty',))
            self.assertEqual(caught.exception.status, expected)
        self.assertFalse(self.app['terminal_proxy'].views[view['viewId']]['claimed'])
        ws = await self.open_view(view)
        await ws.close()

    async def test_view_divergence_rejects_input_and_history(self):
        other = await self.sessions.create('other')
        view = await self.new_view()
        ws = await self.open_view(view)
        private_view = self.app['terminal_proxy'].views[view['viewId']]
        self.assertEqual(await self.sessions.tmux('show-option', '-v', '-t', private_view['session'], 'prefix'), 'None')
        self.assertEqual(await self.sessions.tmux('show-option', '-v', '-t', private_view['session'], 'status'), 'off')
        await self.sessions.tmux('select-window', '-t', private_view['session'] + ':' + other['windowId'])
        marker = self.root / 'must-not-exist'
        await ws.send_bytes(('0touch ' + shlex.quote(str(marker)) + '\r').encode())
        while True:
            message = await ws.receive(timeout=3)
            if message.type == WSMsgType.CLOSE:
                self.assertEqual(message.data, 4009)
                break
        self.assertFalse(marker.exists(), 'Divergent target must not receive pending input')
        await ws.close()

    async def test_history_never_types_q_into_shell(self):
        view = await self.new_view()
        ws = await self.open_view(view)
        for action in ['leave', 'enter', 'pageUp', 'leave', 'leave']:
            response = await self.client.post('/api/views/' + view['viewId'] + '/history',
                headers=ACTION, json={'binding': view['binding'], 'action': action})
            self.assertEqual(response.status, 200, await response.text())
        await ws.close()


if __name__ == '__main__':
    unittest.main()
