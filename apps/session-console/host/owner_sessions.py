"""Live discovery/lifecycle through public ovitmugen CLI; fixed read-only view checks."""
import asyncio
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import sys

from .security import APIError
from .sessions import process_start


class OwnerSessions:
    mode = 'live'

    def __init__(self, script, agents_socket):
        self.script = Path(script)
        if not self.script.is_absolute() or not self.script.is_file():
            raise ValueError('An absolute configured public ovitmugen script is required')
        if not isinstance(agents_socket, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+', agents_socket):
            raise ValueError('agents_socket must be a fixed tmux socket name')
        self.agents_socket = agents_socket
        self.host_id = os.uname().nodename
        self.records = {}
        self.env = dict(os.environ)
        self.env.pop('TMUX', None)
        self.env['OV_AGENTS_SOCKET'] = agents_socket
        self.env['OV_AGENTS_CONF'] = '/dev/null'
        self.env['OV_FRAME_SOCKET'] = 'ovitmugen' if agents_socket == 'default' else agents_socket + '-frame'

    async def _run(self, argv):
        child = await asyncio.create_subprocess_exec(*argv, env=self.env,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        try:
            out, _ = await asyncio.wait_for(child.communicate(), 10)
        except asyncio.TimeoutError:
            child.kill()
            await child.wait()
            raise APIError(503, 'owner_timeout', 'Owner interface did not respond')
        if child.returncode:
            raise APIError(409, 'stale', 'Owner target/view changed or was refused; refresh explicitly')
        return out.decode().strip()

    async def owner(self, *args):
        try:
            return json.loads(await self._run([sys.executable, str(self.script), *args]))
        except (ValueError, TypeError):
            raise APIError(503, 'owner_schema', 'Owner interface returned invalid JSON')

    async def _tmux_read(self, *args):
        return await self._run(['tmux', '-L', self.agents_socket, *args])

    async def targets(self):
        beds = await self.owner('ls', '--json')
        if not isinstance(beds, list):
            raise APIError(503, 'owner_schema', 'Expected owner bed list')
        result, records = [], {}
        for bed in beds:
            slug = bed['bed']
            report = await self.owner('targets', slug)
            if (report.get('schema') != 1 or report['server']['socket'] != self.agents_socket or
                    report['server']['host'] != self.host_id):
                raise APIError(503, 'owner_schema', 'Owner target server identity mismatch')
            tabs = {tab['id']: tab for tab in bed['tabs']}
            for row in report['targets']:
                if row['windowId'] not in tabs:
                    continue  # A newly created tab appears after the next explicit refresh.
                tab = tabs[row['windowId']]
                target_id = hashlib.sha256(json.dumps([slug, row['windowId'], row['paneId']]).encode()).hexdigest()[:32]
                target = {'id': target_id, 'label': f"{slug} / {tab['name']} · {row['command']}",
                    'hostId': self.host_id, 'bed': slug, 'windowId': row['windowId'],
                    'paneId': row['paneId'], 'generation': row['generation'], 'busy': row['busy'],
                    'kind': 'live', 'program': row['command'],
                    'singlePane': row['paneCount'] == 1, 'dead': row['dead'], 'canEnd': False}
                result.append(target)
                records[target_id] = {'report': report, 'row': row, 'target': target}
        self.records = records
        return result

    async def resolve(self, target_id, generation):
        cached = self.records.get(target_id)
        if cached is None:
            raise APIError(409, 'stale', 'Refresh the owner target list before attaching')
        target = cached['target']
        report = await self.owner('targets', target['bed'])
        row = next((row for row in report['targets'] if row['windowId'] == target['windowId'] and
                    row['paneId'] == target['paneId']), None)
        if row is None or row['generation'] != generation or report['server']['socket'] != self.agents_socket:
            raise APIError(409, 'stale', 'Target changed; refresh and select explicitly')
        target = {**target, 'generation': row['generation'], 'program': row['command'],
            'busy': row['busy'], 'dead': row['dead'], 'singlePane': row['paneCount'] == 1,
            'label': f"{target['bed']} / {row['name']} · {row['command']}"}
        self.records[target_id] = {'report': report, 'row': row, 'target': target}
        return target

    async def view(self, target):
        record = self.records[target['id']]
        if record['target']['generation'] != target['generation']:
            raise APIError(409, 'stale', 'Target changed before owner view creation')
        if not target['singlePane'] or target['dead']:
            raise APIError(501, 'target_unavailable', 'Attach requires a live single-pane window')
        capability = await self.owner('phone-view', 'create', target['bed'],
            '--window', target['windowId'], '--pane', target['paneId'], '--generation', target['generation'])
        name = capability.get('name', '')
        expected_argv = ['tmux', '-L', self.agents_socket, '-f', '/dev/null',
                         'attach-session', '-t', '=' + name]
        capability['_snapshot'] = record
        try:
            if (not re.fullmatch(re.escape(target['bed']) + r'--phone-[0-9a-f]{16}', name) or
                    capability.get('attachArgv') != expected_argv or
                    capability.get('serverGeneration') != record['report']['serverGeneration'] or
                    capability.get('target', {}).get('generation') != target['generation']):
                raise APIError(409, 'stale', 'Owner attachment capability changed; refusing to attach')
            await self.validate_view({'session': capability, 'target': target})
            return capability
        except BaseException:
            # The owner checks every marker again; changed or unverifiable views survive.
            if (isinstance(name, str) and
                    re.fullmatch(re.escape(target['bed']) + r'--phone-[0-9a-f]{16}', name) and
                    isinstance(capability.get('token'), str) and
                    isinstance(capability.get('serverGeneration'), str)):
                with contextlib.suppress(APIError):
                    await self.drop_view(capability)
            raise

    def attach_argv(self, capability):
        return list(capability['attachArgv'])

    async def validate_view(self, view):
        cap, target = view['session'], view['target']
        snapshot = cap['_snapshot']
        server, original = snapshot['report']['server'], snapshot['row']
        if target['generation'] != original['generation']:
            raise APIError(409, 'stale', 'Attachment generation mismatch')
        # One read-only tmux invocation: marked view AND still-owning base context.
        fmt = ('#{pid}\t#{session_id}\t#{session_name}\t#{socket_path}\t'
               '#{@ov-phone-base}\t#{@ov-phone-token}\t#{session_group}\t'
               '#{window_id}\t#{pane_id}\t#{pane_pid}\t#{pane_dead}\t#{window_panes}')
        output = await self._tmux_read('display-message', '-p', '-t', '=' + cap['name'] + ':', fmt,
            ';', 'display-message', '-p', '-t', '=' + target['bed'] + ':', '#{session_id}\t#{pid}')
        try:
            current, base = output.splitlines()
            fields = current.split('\t')
            pid, sid, name, socket_path, base_marker, token, group, wid, pane, pane_pid, dead, count = fields
            info = Path(socket_path).stat()
            valid = (pid == str(server['pid']) and process_start(pid) == server['start'] and
                socket_path == server['path'] and (info.st_dev, info.st_ino) == (server['device'], server['inode']) and
                sid == cap['viewId'] and name == cap['name'] and base_marker == server['sessionId'] and
                token == cap['token'] and group == target['bed'] and
                base == server['sessionId'] + '\t' + str(server['pid']) and
                wid == target['windowId'] and pane == target['paneId'] and pane_pid == str(original['panePid']) and
                process_start(pane_pid) == original['paneStart'] and dead == '0' and count == '1')
        except (OSError, ValueError):
            valid = False
        if not valid:
            raise APIError(409, 'stale', 'Owner view identity or selected target changed; reselect explicitly')
        return target

    async def drop_view(self, capability):
        snapshot = capability['_snapshot']
        await self.owner('phone-view', 'detach', snapshot['target']['bed'],
            '--view', capability['name'], '--token', capability['token'],
            '--server-generation', capability['serverGeneration'])

    async def history(self, view, action):
        target = await self.validate_view(view)
        cap = view['session']
        # Exact random name scopes the pane; never use a bare reusable numeric pane ID.
        pane = '=' + cap['name'] + ':' + target['windowId'] + '.' + target['paneId']
        if action == 'enter':
            await self._tmux_read('copy-mode', '-t', pane)
        elif action in {'leave', 'pageUp', 'pageDown'}:
            mode = await self._tmux_read('display-message', '-p', '-t', pane, '#{pane_mode}')
            if mode not in {'copy-mode', 'view-mode'}:
                if action == 'leave':
                    return {'history': False}
                raise APIError(409, 'history', 'Enter history mode first')
            command = {'leave': 'cancel', 'pageUp': 'page-up', 'pageDown': 'page-down'}[action]
            await self._tmux_read('send-keys', '-X', '-t', pane, command)
        else:
            raise APIError(400, 'history', 'Unknown history action')
        await self.validate_view(view)
        return {'history': action != 'leave'}

    async def create(self, name):
        raise APIError(501, 'live_lifecycle', 'Live workbench creation is not enabled')

    async def end(self, target_id, generation):
        raise APIError(501, 'live_lifecycle', 'Live process/workbench ending is not enabled')
