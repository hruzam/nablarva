"""Bound per-view external ttyd adapters; credentials never cross to the browser."""
import asyncio
import base64
import hashlib
import hmac
import json
import os
from pathlib import Path
import secrets
import socket

from aiohttp import ClientSession, ClientTimeout, WSMsgType, web

from .security import APIError

TTYD_SHA256 = '8a217c968aba172e0dbf3f34447218dc015bc4d5e59bf51db2f2cd12b7be4f55'
MAX_FRAME = 256 * 1024


def dimensions(value):
    if not isinstance(value, dict):
        raise APIError(400, 'dimensions', 'Expected terminal dimensions object')
    columns, rows = value.get('columns'), value.get('rows')
    if type(columns) is not int or type(rows) is not int or not (2 <= columns <= 400 and 1 <= rows <= 200):
        raise APIError(400, 'dimensions', 'Terminal dimensions exceed the supported bounds')
    return {'columns': columns, 'rows': rows}


def client_frame(data):
    if not isinstance(data, bytes) or not data or len(data) > MAX_FRAME:
        raise APIError(400, 'frame', 'Invalid terminal frame')
    if data[:1] == b'0':
        data[1:].decode('utf-8')
    elif data[:1] == b'1':
        return b'1' + json.dumps(dimensions(json.loads(data[1:]))).encode()
    elif data not in {b'2', b'3'}:
        raise APIError(400, 'frame', 'Unsupported terminal frame')
    return data


class TerminalProxy:
    def __init__(self, sessions, binary, runtime_root):
        self.sessions = sessions
        self.binary = str(Path(binary).resolve())
        if hashlib.sha256(Path(self.binary).read_bytes()).hexdigest() != TTYD_SHA256:
            raise ValueError('Pinned ttyd checksum mismatch')
        self.root = Path(runtime_root)
        self.views = {}
        self.client = None

    async def start(self, app):
        self.client = ClientSession(trust_env=False)

    async def cleanup(self, app):
        for view_id in list(self.views):
            await self.remove(view_id)
        if self.client:
            await self.client.close()

    async def create(self, target_id, generation):
        if len(self.views) >= 8:
            raise APIError(409, 'limit', 'Detach an existing view before opening another')
        target = await self.sessions.resolve(target_id, generation)
        session = await self.sessions.view(target)
        view_id, binding = secrets.token_hex(16), secrets.token_urlsafe(32)
        credential = 'gateway:' + secrets.token_urlsafe(32)
        # ttyd cannot inherit a prebound TCP fd. A bind collision fails closed below.
        with socket.socket() as candidate:
            candidate.bind(('127.0.0.1', 0))
            port = candidate.getsockname()[1]
        process = None
        try:
            env = dict(os.environ)
            env.pop('TMUX', None)
            process = await asyncio.create_subprocess_exec(self.binary, '-i', '127.0.0.1',
                '-p', str(port), '-W', '-O', '-c', credential,
                *self.sessions.attach_argv(session), env=env,
                stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL)
            authorization = 'Basic ' + base64.b64encode(credential.encode()).decode()
            origin = f'http://127.0.0.1:{port}'
            for _ in range(50):
                if process.returncode is not None:
                    raise APIError(503, 'gateway', 'Disposable terminal gateway exited')
                try:
                    async with self.client.get(origin + '/token',
                            headers={'Authorization': authorization},
                            timeout=ClientTimeout(total=2)) as response:
                        token = await response.json()
                        if response.status != 200 or token.get('token') != authorization[6:]:
                            raise APIError(503, 'gateway', 'Unexpected terminal gateway identity')
                        break
                except (OSError, asyncio.TimeoutError):
                    await asyncio.sleep(.05)
            else:
                raise APIError(503, 'gateway', 'Disposable terminal gateway did not start')
            view = {'viewId': view_id, 'target': target, 'binding': binding,
                    'wsPath': f'/api/views/{view_id}/ws'}
            self.views[view_id] = {**view, 'session': session, 'process': process,
                'authorization': authorization, 'origin': origin, 'ws': None, 'claimed': False}
            return view
        except BaseException:
            if process and process.returncode is None:
                process.terminate()
                await process.wait()
            await self.sessions.drop_view(session)
            raise

    async def remove(self, view_id):
        view = self.views.pop(view_id, None)
        if not view:
            return
        if view['ws']:
            await view['ws'].close(code=1000, message=b'Detached')
        process = view['process']
        if process.returncode is None:
            process.terminate()
            try:
                await asyncio.wait_for(process.wait(), 3)
            except asyncio.TimeoutError:
                process.kill()
                await process.wait()
        try:
            await self.sessions.drop_view(view['session'])
        except APIError:
            # A missing base/server means a view may be the last owner. Preserve it.
            pass

    async def websocket(self, request):
        view_id = request.match_info['id']
        view = self.views.get(view_id)
        if not view:
            raise APIError(404, 'view', 'View no longer exists; select the target again')
        if view['claimed']:
            raise APIError(409, 'binding', 'This attachment was already used; select again')
        await self.sessions.validate_view(view)
        view['claimed'] = True
        ws = web.WebSocketResponse(protocols=('tty',), max_msg_size=MAX_FRAME, heartbeat=10)
        await ws.prepare(request)
        view['ws'] = ws
        tasks = []
        try:
            first = await asyncio.wait_for(ws.receive(), 5)
            if first.type != WSMsgType.TEXT:
                raise APIError(400, 'init', 'Expected attachment initialization')
            initial = json.loads(first.data)
            if not isinstance(initial, dict):
                raise APIError(400, 'init', 'Expected attachment initialization object')
            if not hmac.compare_digest(str(initial.get('binding', '')), view['binding']):
                raise APIError(403, 'binding', 'Attachment binding mismatch')
            size = dimensions(initial)
            await self.sessions.validate_view(view)
            async with self.client.ws_connect(view['origin'] + '/ws', protocols=('tty',),
                    headers={'Authorization': view['authorization']}, origin=view['origin'],
                    max_msg_size=MAX_FRAME, heartbeat=10) as upstream:
                await upstream.send_bytes(json.dumps({**size, 'AuthToken': view['authorization'][6:]}).encode())

                async def browser_to_gateway():
                    async for message in ws:
                        if message.type != WSMsgType.BINARY:
                            raise APIError(400, 'frame', 'Expected binary terminal data')
                        frame = client_frame(message.data)
                        await self.sessions.validate_view(view)
                        await upstream.send_bytes(frame)

                async def gateway_to_browser():
                    async for message in upstream:
                        if message.type == WSMsgType.BINARY:
                            await self.sessions.validate_view(view)
                            await ws.send_bytes(message.data)
                        else:
                            break

                async def watch_target():
                    while True:
                        await asyncio.sleep(1)
                        await self.sessions.validate_view(view)

                tasks = [asyncio.create_task(fn()) for fn in
                         (browser_to_gateway, gateway_to_browser, watch_target)]
                done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                for task in done:
                    task.result()
        except APIError as error:
            await ws.close(code=4009 if error.code == 'stale' else 4003,
                           message=error.message.encode()[:120])
        except (ValueError, TypeError, asyncio.TimeoutError, OSError):
            await ws.close(code=4003, message=b'Terminal initialization or transport failed')
        finally:
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            await ws.close()
            await self.remove(view_id)
        return ws
