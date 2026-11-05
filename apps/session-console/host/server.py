"""Run with python -m host.server --config /absolute/private/config.json."""
import argparse
import asyncio
import hmac
import json
import os
from pathlib import Path
import stat
import subprocess
import sys

from aiohttp import web

from .security import APIError, security_middleware
from .sessions import FixtureSessions
from .owner_sessions import OwnerSessions
from .terminal_proxy import TerminalProxy

HOME = Path(__file__).resolve().parent.parent


def private_directory(value):
    path = Path(value)
    if not path.is_absolute() or path.is_symlink():
        raise ValueError('Private storage roots must be absolute, non-symlink directories')
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    info = path.stat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise ValueError('Private storage roots must be owned by this user with mode 0700')
    return path


def create_app(config, *, sessions=None, proxy=None, install_storage=True):
    credential_path = Path(config['credential_file'])
    if not credential_path.is_absolute() or credential_path.is_symlink():
        raise ValueError('An absolute private credential file is required')
    info = credential_path.stat()
    if info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise ValueError('Credential file must be private to its owner')
    credential = json.loads(credential_path.read_text())['credential']
    if not isinstance(credential, str) or ':' not in credential or not credential.split(':', 1)[1]:
        raise ValueError('A username:password credential is required')
    runtime = private_directory(config['runtime_root'])
    vault = private_directory(config['vault_root'])
    mode = config.get('mode', 'fixture')
    if mode not in {'fixture', 'live'}:
        raise ValueError('mode must be fixture or live')
    if sessions is None:
        sessions = (OwnerSessions(config['ovitmugen_script'], config['agents_socket']) if mode == 'live'
                    else FixtureSessions(config['fixture_socket']))
    if sessions.mode != mode:
        raise ValueError('Configured mode and session adapter do not match')
    proxy = proxy or TerminalProxy(sessions, config['ttyd_binary'], runtime)
    app = web.Application(middlewares=[security_middleware(credential, config['public_origin'])],
                          client_max_size=21 * 1024 * 1024)
    app['sessions'], app['terminal_proxy'] = sessions, proxy
    app.on_startup.append(proxy.start)
    app.on_cleanup.append(proxy.cleanup)

    async def state(request):
        return web.json_response({'mode': mode, 'host': {'id': sessions.host_id, 'label': 'office'},
            'capabilities': {'createFixture': mode == 'fixture', 'endFixture': mode == 'fixture', 'live': mode == 'live',
                             'agentStart': False, 'agentEnd': False},
            'targets': await sessions.targets()})

    async def create_view(request):
        body = await request.json()
        return web.json_response(await proxy.create(body['targetId'], body['generation']), status=201)

    async def office_workbenches(request):
        if request.query:
            raise APIError(400, 'invalid', 'This listing takes no parameters')
        command = [sys.executable, str(Path.home() / '.config/zsh/session/ovitmugen.py'), 'ls']
        try:
            result = await asyncio.to_thread(subprocess.run, command, capture_output=True,
                                            text=True, timeout=15, check=False)
        except subprocess.TimeoutExpired:
            raise APIError(504, 'office_timeout', 'Office workbench listing timed out. Try again.')
        except OSError:
            raise APIError(503, 'office_unavailable', 'Office workbench listing is unavailable.')
        if result.returncode:
            raise APIError(503, 'office_unavailable', 'Office workbench listing failed. Try again.')
        return web.json_response({'output': result.stdout})

    async def remove_view(request):
        await proxy.remove(request.match_info['id'])
        return web.json_response({'detached': True})

    async def create_fixture(request):
        body = await request.json()
        return web.json_response(await sessions.create(body['name']), status=201)

    async def end_fixture(request):
        body = await request.json()
        if body.get('confirm') is not True:
            raise APIError(400, 'confirmation', 'Explicit confirmation required')
        await sessions.end(request.match_info['id'], body['generation'])
        return web.json_response({'ended': True})

    async def history(request):
        view = proxy.views.get(request.match_info['id'])
        if not view:
            raise APIError(409, 'stale', 'Attachment no longer exists')
        body = await request.json()
        if not isinstance(body, dict):
            raise APIError(400, 'invalid', 'Expected a history action object')
        if not hmac.compare_digest(str(body.get('binding', '')), view['binding']):
            raise APIError(403, 'binding', 'Attachment binding mismatch')
        return web.json_response(await sessions.history(view, body.get('action')))

    async def index(request):
        return web.FileResponse(HOME / 'web' / 'index.html')

    async def asset(request):
        name = request.match_info['name']
        if name not in {'app.js', 'app.css'}:
            raise web.HTTPNotFound()
        return web.FileResponse(HOME / 'dist' / name)

    app.add_routes([web.get('/', index), web.get('/assets/{name}', asset),
        web.get('/api/state', state), web.post('/api/views', create_view),
        web.get('/api/office-workbenches', office_workbenches),
        web.delete('/api/views/{id}', remove_view), web.get('/api/views/{id}/ws', proxy.websocket),
        web.post('/api/views/{id}/history', history),
        web.post('/api/fixtures', create_fixture), web.delete('/api/fixtures/{id}', end_fixture)])
    if install_storage:
        from .vault import install_vault
        install_vault(app, vault)
    return app


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args()
    if not args.config.is_absolute():
        parser.error('config must be an absolute path')
    config = json.loads(args.config.read_text())
    port = config['port']
    if type(port) is not int or not 1024 <= port <= 65535:
        parser.error('port must be an unprivileged TCP port')
    web.run_app(create_app(config), host='127.0.0.1', port=port, access_log=None)


if __name__ == '__main__':
    main()
