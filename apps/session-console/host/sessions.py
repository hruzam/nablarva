"""Explicit private-socket fixture adapter; live ovitmugen operations stay gated."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import stat

from .security import APIError


def process_start(pid):
    try:
        raw = (Path('/proc') / str(pid) / 'stat').read_text()
        return raw[raw.rindex(')') + 2:].split()[19]
    except (OSError, ValueError, IndexError):
        raise APIError(409, 'stale', 'Process identity unavailable; refresh the target')


class FixtureSessions:
    mode = 'fixture'

    def __init__(self, socket_path, base='desktop'):
        if Path(socket_path).is_symlink():
            raise ValueError('Fixture socket must not be a symlink')
        self.socket = Path(socket_path).resolve()
        if not self.socket.parent.name.startswith(('pc-trial-', 'pc-test-')):
            raise ValueError('Only an explicit disposable pc-trial/pc-test socket is accepted')
        self.base = base
        self.host_id = os.uname().nodename
        self.epoch = None
        self.owned = {}
        self.lock = asyncio.Lock()

    async def tmux(self, *args):
        env = dict(os.environ)
        env.pop('TMUX', None)
        child = await asyncio.create_subprocess_exec('tmux', '-S', str(self.socket), *args,
            env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        try:
            out, _ = await asyncio.wait_for(child.communicate(), 3)
        except asyncio.TimeoutError:
            child.kill()
            await child.wait()
            raise APIError(503, 'tmux_timeout', 'Fixture server did not respond')
        if child.returncode:
            raise APIError(409, 'stale', 'Fixture target changed or is unavailable')
        return out.decode().strip()

    async def server_epoch(self):
        try:
            info = self.socket.stat()
        except OSError:
            raise APIError(409, 'stale', 'Fixture socket unavailable')
        if not stat.S_ISSOCK(info.st_mode):
            raise APIError(409, 'stale', 'Expected a dedicated tmux socket')
        parent = self.socket.parent.stat()
        if info.st_uid != os.getuid() or parent.st_uid != os.getuid() or parent.st_mode & 0o077:
            raise APIError(403, 'socket_owner', 'Fixture socket requires its owner and a private parent')
        pid, session_id = (await self.tmux('display-message', '-p', '-t', '=' + self.base + ':',
                                         '#{pid}\t#{session_id}')).split('\t')
        epoch = (info.st_dev, info.st_ino, pid, process_start(pid), session_id)
        if self.epoch is None:
            self.epoch = epoch
        if self.epoch != epoch:
            raise APIError(409, 'stale', 'Fixture server restarted; restart this adapter explicitly')
        return epoch

    @staticmethod
    def children(pid):
        try:
            return bool((Path('/proc') / str(pid) / 'task' / str(pid) / 'children').read_text().strip())
        except OSError:
            return True  # Unknown is never idle.

    async def targets(self):
        epoch = await self.server_epoch()
        output = await self.tmux('list-panes', '-s', '-t', '=' + self.base, '-F',
            '#{window_id}\t#{window_name}\t#{pane_id}\t#{pane_pid}\t#{pane_current_command}\t#{window_panes}')
        result = []
        for row in output.splitlines():
            wid, label, pane, pid, command, count = row.split('\t')
            generation = hashlib.sha256(json.dumps([epoch, wid, pane, pid, process_start(pid)]).encode()).hexdigest()
            busy = command.lstrip('-') not in {'bash', 'zsh', 'sh', 'dash', 'fish', 'ksh'} or self.children(pid)
            result.append({'id': wid + '.' + pane, 'label': label, 'hostId': self.host_id,
                'bed': self.base, 'windowId': wid, 'paneId': pane, 'generation': generation,
                'busy': busy, 'kind': 'fixture', 'singlePane': count == '1',
                'canEnd': self.owned.get(wid) == generation})
        return result

    async def resolve(self, target_id, generation):
        target = next((item for item in await self.targets() if item['id'] == target_id), None)
        if target is None or target['generation'] != generation:
            raise APIError(409, 'stale', 'Target changed; refresh and select it explicitly')
        return target

    async def create(self, name):
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9 _-]{0,47}', name):
            raise APIError(400, 'name', 'Use 1–48 letters, digits, spaces, hyphens or underscores')
        async with self.lock:
            await self.server_epoch()
            wid = await self.tmux('new-window', '-d', '-P', '-F', '#{window_id}',
                '-t', '=' + self.base + ':', '-n', name, '-c', str(self.socket.parent),
                'bash', '--noprofile', '--norc', '-i')
            target = next(item for item in await self.targets() if item['windowId'] == wid)
            self.owned[wid] = target['generation']
            return {**target, 'canEnd': True}

    async def end(self, target_id, generation):
        async with self.lock:
            target = await self.resolve(target_id, generation)
            if not target['canEnd']:
                raise APIError(403, 'protected', 'Only a workbench created by this host instance may be ended')
            if not target['singlePane'] or target['busy']:
                raise APIError(409, 'busy', 'End the process in its terminal before closing this workbench')
            targets = await self.targets()
            if len({item['windowId'] for item in targets}) <= 1:
                raise APIError(409, 'protected', 'The last base workbench is protected')
            latest = await self.resolve(target_id, generation)
            if latest['busy']:
                raise APIError(409, 'busy', 'Workbench became busy; nothing was closed')
            await self.tmux('kill-window', '-t', target['windowId'])
            self.owned.pop(target['windowId'], None)

    async def view(self, target):
        async with self.lock:
            await self.resolve(target['id'], target['generation'])
            if not target['singlePane']:
                raise APIError(501, 'multi_pane', 'Independent multi-pane views require owner review')
            name = 'pc-view-' + secrets.token_hex(10)
            session = await self.tmux('new-session', '-d', '-P', '-F', '#{session_id}',
                                      '-s', name, '-t', '=' + self.base)
            try:
                await self.tmux('select-window', '-t', session + ':' + target['windowId'])
                await self.tmux('set-option', '-t', session, 'mouse', 'on')
                await self.tmux('set-option', '-t', session, 'prefix', 'None')
                await self.tmux('set-option', '-t', session, 'prefix2', 'None')
                await self.tmux('set-option', '-t', session, 'status', 'off')
                await self.tmux('set-option', '-w', '-t', target['windowId'], 'window-size', 'smallest')
                await self.resolve(target['id'], target['generation'])
            except BaseException:
                await self.drop_view(session)
                raise
            return session

    async def validate_view(self, view):
        target = await self.resolve(view['target']['id'], view['target']['generation'])
        active = await self.tmux('display-message', '-p', '-t', view['session'] + ':',
                                 '#{window_id}.#{pane_id}')
        if active != target['id']:
            raise APIError(409, 'stale', 'View changed target; select it explicitly again')
        return target

    async def drop_view(self, session):
        # If the base disappeared, a surviving view might be the last process owner.
        await self.server_epoch()
        await self.tmux('kill-session', '-t', session)

    def attach_argv(self, session):
        return ['tmux', '-S', str(self.socket), 'attach-session', '-t', session]

    async def history(self, view, action):
        target = await self.validate_view(view)
        pane = view['session'] + ':' + target['windowId'] + '.' + target['paneId']
        if action == 'enter':
            await self.tmux('copy-mode', '-t', pane)
        elif action in {'leave', 'pageUp', 'pageDown'}:
            mode = await self.tmux('display-message', '-p', '-t', pane, '#{pane_mode}')
            if mode not in {'copy-mode', 'view-mode'}:
                if action == 'leave':
                    return {'history': False}
                raise APIError(409, 'history', 'Enter history mode first')
            command = {'leave': 'cancel', 'pageUp': 'page-up', 'pageDown': 'page-down'}[action]
            await self.tmux('send-keys', '-X', '-t', pane, command)
        else:
            raise APIError(400, 'history', 'Unknown history action')
        await self.validate_view(view)
        return {'history': action != 'leave'}
