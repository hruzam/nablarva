#!/usr/bin/env python3
"""X1 disposable-profile trial of SublimeObserver (synthetic views only).

Isolation (per editor instance): bwrap with its own network namespace (no abstract-socket
IPC with the operator's editor), tmpfs over /tmp, /run/user/<uid> and $HOME, the host
filesystem read-only, and the disposable portable binary from
/tmp/nablarva-observer-4215/portable with a FRESH Data directory (from this trial's /tmp
root) bound over its Data -- the portable profile on disk is never modified. Display: a
headless kwin_wayland --virtual compositor hosting a private Xwayland :71, so no window
reaches the operator's desktop. The chain exits by itself when the editor exits.

Signals: only to a process this trial started (pinned by pidfd, see "process identity") whose
/proc/<pid>/exe is under /tmp/nablarva-observer-4215/ AND whose environment carries this
trial's X1_TRIAL_ROOT; sent through the pidfd. Step 5b: no /proc entry of a process the trial
did not start is ever read, in any mode; the operator's editor is never probed.

Step 2b: the heartbeat interval and the stale bound come from the package settings file
(contract.STALE_FACTOR x heartbeat_s); X1_HEARTBEAT_S overrides it for the main run through the
disposable profile's User settings, and X1_ALT_HEARTBEAT_S (default 5 since step 3a, when the
package default became 1 s; '' disables) reruns the two crash cases at that interval.
X1_ONLY=exit2b runs the ignored-exit diagnostic only.
X1_NO_OPERATOR_PROBES=1 (step 5) skips the existence check of /run/user/<uid>/sublime-observer.
(The /proc probe of the operator's editor it also skipped is gone entirely since step 5b.)

Layout (step 3a): <root>/SublimeObserver is the installed payload, <root>/tests holds this file.
Evidence is written ONLY to X1_EVIDENCE_DIR (required; never inside the source tree) as
<X1_EVIDENCE_PREFIX, default disposable-trial>[suffix].<YYYY-MM-DD>.json.
"""
import ctypes
import json
import os
import re
import select
import shutil
import signal
import statistics
import struct
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from pathlib import Path

IMPL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(IMPL / 'tests'))
import reader  # noqa: E402
sys.dont_write_bytecode = True      # importing contract must never leave __pycache__ in the payload
sys.path.insert(0, str(IMPL / 'SublimeObserver'))
import contract  # noqa: E402  (pure Python, no sublime import)

PORTABLE = Path('/tmp/nablarva-observer-4215/portable')
BINARY = PORTABLE / 'sublime_text'
GUARD = '/tmp/nablarva-observer-4215/'
OPERATOR_BINARY = '/opt/sublime_text/sublime_text'
UID = os.getuid()
EVIDENCE_PREFIX = os.environ.get('X1_EVIDENCE_PREFIX') or 'disposable-trial'


def package_settings():
    """The shipped SublimeObserver.sublime-settings (comments and trailing commas stripped)."""
    text = (IMPL / 'SublimeObserver' / 'SublimeObserver.sublime-settings').read_text(encoding='utf-8')
    raw = re.sub(r'^\s*//.*$', '', text, flags=re.M)
    return json.loads(re.sub(r',\s*([\]}])', r'\1', raw))


def heartbeat_params(override=None):
    settings = package_settings()
    hb = float(settings['heartbeat_s']) if override is None else float(override)
    return {'heartbeat_s': hb, 'stale_after_s': contract.STALE_FACTOR * hb,
            'stale_factor': contract.STALE_FACTOR,
            'source': 'package settings' if override is None else 'User settings override in the disposable profile',
            'package_settings_heartbeat_s': settings['heartbeat_s']}


# --- inotify (ctypes, stdlib only): ordered record of directory events -------

_IN = {0x40: 'MOVED_FROM', 0x80: 'MOVED_TO', 0x100: 'CREATE', 0x200: 'DELETE', 0x400: 'DELETE_SELF',
       0x8000: 'IGNORED', 0x4000: 'Q_OVERFLOW', 0x40000000: 'ISDIR'}
_IN_MASK = 0x40 | 0x80 | 0x100 | 0x200 | 0x400


class Inotify(object):
    def __init__(self, base):
        self.base = str(base)
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)
        self.fd = self.libc.inotify_init1(os.O_NONBLOCK | os.O_CLOEXEC)
        if self.fd < 0:
            raise OSError(ctypes.get_errno(), 'inotify_init1')
        self.wds, self.events, self._stop = {}, [], threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def watch(self, path):
        wd = self.libc.inotify_add_watch(self.fd, os.fsencode(str(path)), _IN_MASK)
        if wd < 0:
            raise OSError(ctypes.get_errno(), 'inotify_add_watch {}'.format(path))
        self.wds[wd] = os.path.relpath(str(path), self.base)

    def start(self):
        self._thread.start()
        return self

    def _run(self):
        while not self._stop.is_set():
            if not select.select([self.fd], [], [], 0.02)[0]:
                continue
            try:
                data = os.read(self.fd, 65536)
            except BlockingIOError:
                continue
            at, off = time.time(), 0
            while off < len(data):
                wd, mask, _cookie, size = struct.unpack_from('iIII', data, off)
                name = data[off + 16:off + 16 + size].rstrip(b'\0').decode(errors='replace')
                off += 16 + size
                self.events.append({'n': len(self.events), 'read_at': at, 'dir': self.wds.get(wd, wd),
                                    'name': name, 'mask': [v for k, v in _IN.items() if mask & k]})

    def close(self):
        time.sleep(0.1)
        self._stop.set()
        self._thread.join(2)
        os.close(self.fd)
        return self.events


def tree(root):
    """Relative paths of everything under root (dirs end with '/'), symlinks marked."""
    out = []
    for dirpath, dirnames, filenames in os.walk(str(root)):
        rel = os.path.relpath(dirpath, str(root))
        for n in dirnames:              # os.walk lists a symlink to a directory here
            link = os.path.islink(os.path.join(dirpath, n))
            out.append(os.path.normpath(os.path.join(rel, n)) + ('@' if link else '/'))
        for n in filenames:
            p = os.path.join(rel, n)
            out.append(os.path.normpath(p) + ('@' if os.path.islink(os.path.join(dirpath, n)) else ''))
    return sorted(out)


def now():
    return time.time()


def wait_for(pred, timeout, interval=0.01, what='condition'):
    deadline = time.monotonic() + timeout
    last_exc = None
    while time.monotonic() < deadline:
        try:
            value = pred()
            if value:
                return value
        except (FileNotFoundError, KeyError, ValueError, IndexError) as exc:
            last_exc = exc
        time.sleep(interval)
    raise TimeoutError('timed out waiting for {} ({})'.format(what, last_exc))


def load(path):
    with open(path, 'rb') as handle:
        return json.loads(handle.read().decode('utf-8'))


# --- process identity (step 5b: confined to processes this trial started) -------------
#
# The trial never lists /proc and never reads a /proc/<pid> entry of a process it did not
# start. Discovery walks /proc/<pid>/task/<tid>/children from the trial's own pid only; each
# child found is pinned with a pidfd (os.pidfd_open) and confirmed still listed under its
# parent, so later reads, liveness checks and signals refer to that very process even after
# it is reparented. The trial is a child subreaper (PR_SET_CHILD_SUBREAPER), so a process
# that double-forks (e.g. the editor's crash_handler) or is orphaned (plugin host after
# kill -9 of the editor) stays in the trial's tree. Every /proc read goes through _proc_path,
# which refuses any pid that is neither the trial itself nor pinned; an audit hook records
# every /proc path opened or listed, and the report classifies them (`proc_access`).

_SELF = os.getpid()
_PIDFD = {}             # pid -> pidfd of a process this trial started
_PROC_SEEN = set()      # (pid-or-'self', first component) from the audit hook


def _audit(event, args):
    if event in ('open', 'os.listdir', 'os.scandir') and args:
        path = args[0]
        if isinstance(path, bytes):
            path = path.decode(errors='replace')
        if isinstance(path, str) and os.path.normpath(path) == '/proc':
            _PROC_SEEN.add('<listing of /proc>')        # a scan of every process: never done
        elif isinstance(path, str) and path.startswith('/proc/'):
            _PROC_SEEN.add(path.split('/')[2])


def set_child_subreaper():
    libc = ctypes.CDLL('libc.so.6', use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0) != 0:          # PR_SET_CHILD_SUBREAPER
        raise OSError(ctypes.get_errno(), 'prctl(PR_SET_CHILD_SUBREAPER)')


def _exited(fd):
    return bool(select.select([fd], [], [], 0)[0])      # a pidfd is readable once the process exits


def _proc_path(pid, *parts):
    if pid != _SELF and pid not in _PIDFD:
        raise RuntimeError('refusing to read /proc/{}: not a process this trial started'.format(pid))
    return '/'.join(('/proc', 'self' if pid == _SELF else str(pid)) + parts)


def _children(pid):
    out = []
    try:
        tasks = os.listdir(_proc_path(pid, 'task'))
    except OSError:
        return out
    for tid in tasks:
        try:
            with open(_proc_path(pid, 'task', tid, 'children')) as handle:
                out.extend(int(n) for n in handle.read().split())
        except OSError:
            pass
    return out


def walk():
    """Pin every live descendant of the trial; return their pids."""
    found, todo = [], [_SELF]
    while todo:
        parent = todo.pop()
        for child in _children(parent):
            if child in found:
                continue
            if child in _PIDFD and _exited(_PIDFD[child]):     # number reused by a new descendant
                os.close(_PIDFD.pop(child))
            if child not in _PIDFD:
                try:
                    fd = os.pidfd_open(child)
                except OSError:
                    continue
                if child not in _children(parent):     # gone between listing and pinning
                    os.close(fd)
                    continue
                _PIDFD[child] = fd
            found.append(child)
            todo.append(child)
    return found


def started_pids():
    """Running processes this trial started: its tree now, plus pinned ones still running."""
    walk()
    return [pid for pid, fd in _PIDFD.items() if not _exited(fd)]


def gone(pid):
    """True once a process this trial started has exited (pidfd, never /proc)."""
    fd = _PIDFD.get(pid)
    if fd is None:
        walk()
        fd = _PIDFD.get(pid)
    if fd is None:
        raise RuntimeError('pid {} is not a process this trial started'.format(pid))
    return _exited(fd)


def readlink(path):
    try:
        return os.readlink(path)
    except OSError:
        return None


def proc(pid, with_env=False):
    if pid not in _PIDFD:
        walk()
    if pid != _SELF and (pid not in _PIDFD or _exited(_PIDFD[pid])):
        return None
    info = {'pid': pid, 'exe': readlink(_proc_path(pid, 'exe')), 'ns_net': readlink(_proc_path(pid, 'ns', 'net')),
            'ns_mnt': readlink(_proc_path(pid, 'ns', 'mnt'))}
    try:
        with open(_proc_path(pid, 'cmdline'), 'rb') as handle:
            info['cmdline'] = handle.read().replace(b'\0', b' ').decode(errors='replace').strip()[:200]
        with open(_proc_path(pid, 'stat')) as handle:
            info['ppid'] = int(handle.read().rsplit(')', 1)[1].split()[1])
    except OSError:
        return None
    if with_env:
        try:
            with open(_proc_path(pid, 'environ'), 'rb') as handle:
                info['env'] = dict(kv.split(b'=', 1) for kv in handle.read().split(b'\0') if b'=' in kv)
        except OSError:
            info['env'] = {}
    if pid != _SELF and _exited(_PIDFD[pid]):
        return None             # exited while being read: the reads may not describe it
    return info


def mine(trial):
    """Processes this trial started whose exe is under the disposable path AND carry this trial's root."""
    out = []
    for pid in started_pids():
        info = proc(pid, with_env=True)
        if not info or not (info['exe'] or '').startswith(GUARD):
            continue
        if info['env'].get(b'X1_TRIAL_ROOT') == str(trial).encode():
            info.pop('env')
            out.append(info)
    return out


def operator_editors():
    """Step 5b: never probed. Finding the operator's editor needs a look at processes the trial
    did not start, which the trial no longer does in any mode."""
    return 'not probed (step 5b): the trial reads no process it did not start'


def proc_access_report():
    own = {'self', str(_SELF)}
    started = {str(p) for p in _PIDFD}
    other = sorted(k for k in _PROC_SEEN if k not in own and k not in started)
    return {'proc_entries_opened_or_listed': sorted(_PROC_SEEN, key=str),
            'pinned_started_pids': sorted(_PIDFD),
            'entries_not_self_and_not_started': other,
            'note': 'audit hook covers open/os.listdir/os.scandir; readlink is not an audit event, '
                    'every readlink goes through _proc_path (refuses unpinned pids)'}


def reap_orphans(exclude):
    """Reap exited processes that were reparented to this subreaper (never a Popen child)."""
    for pid, fd in list(_PIDFD.items()):
        if pid in exclude or not _exited(fd):
            continue
        try:
            os.waitid(os.P_PIDFD, fd, os.WEXITED | os.WNOHANG)
        except ChildProcessError:
            pass


def guarded_signal(trial, pid, sig):
    allowed = {p['pid'] for p in mine(trial)}
    if pid not in allowed:
        raise RuntimeError('refusing to signal pid {}: not a disposable process of this trial'.format(pid))
    signal.pidfd_send_signal(_PIDFD[pid], sig)


def plugin_hosts(trial, sublime_pid):
    """Disposable plugin_host* children of one disposable editor."""
    return [p for p in mine(trial) if p['ppid'] == sublime_pid
            and os.path.basename(p['exe'] or '').startswith('plugin_host')]


def kill_together(trial, sublime_pid):
    """Crash with no survivor: SIGSTOP the editor and all its plugin hosts (so nobody can react),
    then SIGKILL them. Every pid passes the same exe-under-/tmp + trial-env guard first."""
    hosts = plugin_hosts(trial, sublime_pid)
    targets = [p['pid'] for p in hosts] + [sublime_pid]
    allowed = {p['pid'] for p in mine(trial)}
    for pid in targets:
        if pid not in allowed:
            raise RuntimeError('refusing to signal pid {}: not a disposable process of this trial'.format(pid))
    for pid in reversed(targets):         # editor first, so it cannot notice a host dying
        signal.pidfd_send_signal(_PIDFD[pid], signal.SIGSTOP)
    for pid in targets:
        signal.pidfd_send_signal(_PIDFD[pid], signal.SIGKILL)
    return {'stopped_then_killed': targets, 'plugin_hosts': hosts}


# --- trial --------------------------------------------------------------

class Trial(object):
    def __init__(self):
        self.root_dir = Path(tempfile.mkdtemp(prefix='sublime-observer-x1-trial-', dir='/tmp'))
        os.chmod(str(self.root_dir), 0o700)
        self.pub_base = self.root_dir / 'pub'
        self.pub_base.mkdir(mode=0o700)
        self.root = self.pub_base / 'sublime-observer'
        self.syn = self.root_dir / 'synthetic'
        self.syn.mkdir()
        (self.root_dir / 'fixture').mkdir()
        self.report = {'trial_root': str(self.root_dir), 'publish_root': str(self.root),
                       'portable': str(PORTABLE), 'checks': {}, 'instances': [], 'notes': []}
        self.seq = 0

    # data dir with copied package + fixture + user settings
    def data_dir(self, tag, heartbeat_s=None):
        data = self.root_dir / ('data-' + tag)
        packages = data / 'Packages'
        shutil.copytree(str(IMPL / 'SublimeObserver'), str(packages / 'SublimeObserver'),
                        ignore=shutil.ignore_patterns('__pycache__'))
        if os.environ.get('X1_AB_NO_ON_EXIT') == '1':      # A/B diagnostic on the /tmp copy only
            copied = packages / 'SublimeObserver' / 'publisher.py'
            source = copied.read_text()
            hook = '    def on_exit(self):'
            assert hook in source
            copied.write_text(source.replace(hook, '    def _disabled_on_exit(self):'))
            self.report['notes'].append('A/B: on_exit disabled in the trial copy of publisher.py')
        fixture = packages / 'SublimeObserverTrialFixture'
        fixture.mkdir()
        shutil.copyfile(str(IMPL / 'tests/trial_fixture/fixture.py'), str(fixture / 'fixture.py'))
        (fixture / '.python-version').write_text('3.8\n')
        user = packages / 'User'
        user.mkdir()
        user_settings = {'root': str(self.root)}
        if heartbeat_s is not None:         # disposable-profile override only; package default untouched
            user_settings['heartbeat_s'] = heartbeat_s
        (user / 'SublimeObserver.sublime-settings').write_text(json.dumps(user_settings, indent=1))
        (user / 'Preferences.sublime-settings').write_text(json.dumps(
            {'update_check': False, 'hot_exit': 'disabled', 'remember_open_files': False,
             'close_windows_when_empty': False}, indent=1))
        return data

    def launch(self, tag, data):
        home = self.root_dir / ('home-' + tag)
        runtime = self.root_dir / ('runtime-' + tag)
        home.mkdir(exist_ok=True)
        runtime.mkdir(mode=0o700, exist_ok=True)
        script = self.root_dir / ('session-' + tag + '.sh')
        script.write_text(
            '#!/bin/sh\n'
            'Xwayland :71 -nolisten tcp -geometry 1280x800 >"$X1_TRIAL_ROOT/xwayland-{tag}.log" 2>&1 &\n'
            'i=0; while [ ! -S /tmp/.X11-unix/X71 ] && [ $i -lt 200 ]; do sleep 0.05; i=$((i+1)); done\n'
            'unset WAYLAND_DISPLAY\n'
            'export DISPLAY=:71 GDK_BACKEND=x11\n'
            'exec {binary} --multiinstance --new-window --background\n'.format(tag=tag, binary=BINARY))
        script.chmod(0o700)
        env_args = []
        for key, value in (('HOME', home), ('XDG_RUNTIME_DIR', runtime), ('XDG_CONFIG_HOME', home / '.config'),
                           ('XDG_CACHE_HOME', home / '.cache'), ('X1_TRIAL_ROOT', self.root_dir)):
            env_args += ['--setenv', key, str(value)]
        for key in ('WAYLAND_DISPLAY', 'DISPLAY', 'DBUS_SESSION_BUS_ADDRESS', 'XAUTHORITY'):
            env_args += ['--unsetenv', key]
        command = (['bwrap', '--die-with-parent', '--unshare-net', '--ro-bind', '/', '/', '--dev', '/dev',
                    '--dev-bind', '/dev/dri', '/dev/dri', '--proc', '/proc', '--tmpfs', '/tmp',
                    '--dir', '/tmp/.X11-unix', '--tmpfs', '/run/user/{}'.format(UID),
                    '--tmpfs', str(Path.home()),
                    '--bind', str(self.root_dir), str(self.root_dir),
                    '--ro-bind', '/tmp/nablarva-observer-4215', '/tmp/nablarva-observer-4215',
                    '--bind', str(data), str(PORTABLE / 'Data')] + env_args +
                   ['--', 'dbus-run-session', '--', 'kwin_wayland', '--virtual', '--no-lockscreen',
                    '--no-global-shortcuts', '--no-kactivities', '--socket', 'x1-wl',
                    '--width', '1280', '--height', '800', '--exit-with-session', str(script)])
        log = open(str(self.root_dir / ('launch-' + tag + '.log')), 'ab')
        started = time.monotonic()
        popen = subprocess.Popen(command, stdout=log, stderr=log, stdin=subprocess.DEVNULL)
        log.close()

        def editor():
            for p in mine(self.root_dir):
                if p['exe'] == str(BINARY) and '--multiinstance' in p['cmdline']:
                    if not any(i.get('sublime_pid') == p['pid'] and i.get('alive') for i in self.report['instances']):
                        return p
            if popen.poll() is not None:
                raise RuntimeError('sandbox exited during startup: {}'.format(popen.returncode))
            return None
        ed = wait_for(editor, 30, 0.05, 'disposable sublime_text')

        def hello():
            for name in os.listdir(str(self.root_dir / 'fixture')):
                if name.startswith('hello-'):
                    h = load(str(self.root_dir / 'fixture' / name))
                    if h['ppid'] == ed['pid']:
                        return h
            return None
        h = wait_for(hello, 40, 0.05, 'fixture hello')
        inst = {'tag': tag, 'popen': popen, 'sublime_pid': ed['pid'], 'plugin_host_pid': h['pid'],
                'chan': Path(h['chan']), 'alive': True, 'data': data, 'data_dir': str(data),
                'startup_ms': round((time.monotonic() - started) * 1000, 1)}
        host_ns = readlink(_proc_path(_SELF, 'ns', 'net'))
        inst['identity'] = {'sublime_text': proc(ed['pid']), 'plugin_host': proc(h['pid']),
                            'harness_ns_net': host_ns,
                            'separate_net_ns': proc(ed['pid'])['ns_net'] != host_ns,
                            'binary_inode_match': os.stat(_proc_path(ed['pid'], 'exe')).st_ino == os.stat(str(BINARY)).st_ino,
                            'bwrap_pid': popen.pid,
                            'disposable_processes_at_start': [{k: p[k] for k in ('pid', 'ppid', 'exe')}
                                                              for p in mine(self.root_dir)]}
        record = {k: v for k, v in inst.items() if k not in ('popen', 'chan', 'data')}
        self.report['instances'].append(record)
        inst['record'] = record
        return inst

    def call(self, inst, op, timeout=15, **fields):
        self.seq += 1
        name = '{:06d}.json'.format(self.seq)
        tmp = inst['chan'] / 'in' / ('.' + name)
        tmp.write_text(json.dumps(dict(fields, op=op)))
        os.replace(str(tmp), str(inst['chan'] / 'in' / name))
        out = inst['chan'] / 'out' / name
        result = wait_for(lambda: out.exists() and load(str(out)), timeout, 0.005, 'fixture ' + op)
        if not result.get('ok'):
            raise RuntimeError('fixture {} failed: {}'.format(op, result.get('error')))
        return result

    def stop(self, inst, graceful=True):
        if not inst['alive']:
            return
        if graceful:
            try:
                self.call(inst, 'close_all', timeout=5)
            except Exception:
                pass
            try:
                inst['record']['inventory_before_exit'] = self.call(inst, 'inventory', timeout=5)['windows']
            except Exception as exc:
                inst['record']['inventory_before_exit'] = 'no answer: {}'.format(exc)
            try:
                self.call(inst, 'exit', timeout=5)
            except Exception:
                pass
            exit_sent = time.monotonic()
            try:
                inst['popen'].wait(20)
                inst['record']['stopped_by'] = 'exit command'
                inst['record']['exit_s'] = round(time.monotonic() - exit_sent, 2)
            except subprocess.TimeoutExpired:
                # diagnostic only (no workaround): does the editor still run its loop, what is open?
                try:
                    inv = self.call(inst, 'inventory', timeout=3)['windows']
                except Exception as exc:
                    inv = 'no answer: {}'.format(exc)
                inst['record']['exit_ignored'] = {
                    'inventory_20s_after_exit': inv,
                    'processes': mine(self.root_dir),
                    'data_local': sorted(os.listdir(str(inst['data'] / 'Local'))) if (inst['data'] / 'Local').is_dir() else None,
                    'crash_reports': sorted(os.listdir(str(inst['data'] / 'Crash Reports'))) if (inst['data'] / 'Crash Reports').is_dir() else None}
                guarded_signal(self.root_dir, inst['sublime_pid'], signal.SIGTERM)
                inst['popen'].wait(20)
                inst['record']['stopped_by'] = 'SIGTERM after exit command did not finish in 20 s'
        elif graceful is None:              # crash with no survivor: editor + plugin hosts together
            inst['record']['kill_together'] = kill_together(self.root_dir, inst['sublime_pid'])
            inst['popen'].wait(30)
            inst['record']['stopped_by'] = 'SIGSTOP+SIGKILL of editor and plugin hosts together (crash check)'
        else:
            guarded_signal(self.root_dir, inst['sublime_pid'], signal.SIGKILL)
            inst['popen'].wait(30)
            inst['record']['stopped_by'] = 'SIGKILL of the editor only (crash check, orphan plugin host)'
        inst['alive'] = inst['record']['alive'] = False

    # publication helpers
    def index(self):
        return load(str(self.root / 'index.json'))

    def entry(self, view):
        for e in self.index()['shared']:
            if e['view'] == view:
                return e
        return None

    def vdir(self, sid):
        return self.root / 'views' / sid

    def state(self, sid):
        return load(str(self.vdir(sid) / 'state.json'))

    def texts(self, sid):
        return sorted(n for n in os.listdir(str(self.vdir(sid))) if n.startswith('text.'))

    def wait_shared(self, view, timeout=5):
        e = wait_for(lambda: self.entry(view), timeout, 0.01, 'index entry for view {}'.format(view))
        wait_for(lambda: self.state(e['share_id'])['text_file'], timeout, 0.01, 'text for view {}'.format(view))
        return e['share_id']

    def check(self, number, name, fn):
        started = time.monotonic()
        try:
            ok, observed = fn()
            result = 'pass' if ok else 'fail'
        except Exception as exc:
            result, observed = 'error', {'exception': '{}: {}'.format(type(exc).__name__, exc)}
        observed['elapsed_s'] = round(time.monotonic() - started, 3)
        self.report['checks'][str(number)] = {'name': name, 'result': result, 'observed': observed}
        print('check {:>2} {:<5} {}'.format(number, result, name), flush=True)
        return result == 'pass'


def modes(root):
    out = {}
    for dirpath, dirnames, filenames in os.walk(str(root)):
        rel = os.path.relpath(dirpath, str(root))
        out[rel + '/'] = oct(os.lstat(dirpath).st_mode & 0o777)
        for n in filenames:
            p = os.path.join(dirpath, n)
            st = os.lstat(p)
            out[os.path.join(rel, n)] = 'symlink' if os.path.islink(p) else oct(st.st_mode & 0o777)
    return out


def summary(xs):
    xs = sorted(xs)
    return {'n': len(xs), 'median_ms': round(statistics.median(xs), 2),
            'p95_ms': round(xs[int(0.95 * (len(xs) - 1))], 2), 'min_ms': round(xs[0], 2), 'max_ms': round(xs[-1], 2)}


def reader_timeline(root, killed_at, limit_s, settle_s=1.5, interval=0.05):
    """What a reader following tests/reader.py sees after a crash, sampled every `interval` s.
    Records only changes of outcome (plus the first sample). MEASURED, harness clock."""
    root = str(root)
    samples, last, first_not_live = [], None, None
    while True:
        at = now()
        elapsed = round(at - killed_at, 3)
        try:
            info = reader.publisher(root)
            verdict, age = 'live', round(at - info['heartbeat_at'], 3)
        except reader.NotLive as exc:
            verdict, age = 'not live: {}'.format(exc), None
        except Exception as exc:
            verdict, age = 'reader error: {}: {}'.format(type(exc).__name__, exc), None
        try:
            st, text = reader.read_current(root)
            current = 'capture presented: epoch {} revision {} text_chars {}'.format(
                st['epoch'][:8], st['revision'], None if text is None else len(text))
        except (reader.NotLive, reader.Unavailable) as exc:
            current = '{}: {}'.format(type(exc).__name__, exc)
        except Exception as exc:
            current = 'reader error: {}: {}'.format(type(exc).__name__, exc)
        naive = os.path.exists(os.path.join(root, 'current', 'state.json'))
        key = (verdict, current, naive)
        if key != last:
            samples.append({'t_after_kill_s': elapsed, 'publisher': verdict, 'heartbeat_age_s': age,
                            'read_current': current, 'current_state_json_on_disk': naive})
            last = key
        if verdict != 'live' and first_not_live is None:
            first_not_live = elapsed
        if first_not_live is not None and elapsed - first_not_live >= settle_s:
            break
        if elapsed > limit_s:
            break
        time.sleep(interval)
    return {'changes': samples, 'reader_first_not_live_s': first_not_live, 'sample_interval_s': interval}


def crash_case(t, holder, data, tag, hb, together, insts):
    """One crash of the instance in holder['inst'], then a restart on the same profile.

    together=False: SIGKILL the editor only (the plugin host is orphaned; step 2 behaviour).
    together=True : SIGSTOP+SIGKILL editor and plugin hosts together, so the files persist;
                    the restart must remove the dead epoch's residue before publishing anything.
    """
    inst = holder['inst']
    root = t.root
    w = t.call(inst, 'new_window')['window']
    S = t.call(inst, 'create', window=w, title='crash synthetic ' + tag)['view']
    t.call(inst, 'write', window=w, view=S, text='crash residue ' + tag + '\n')
    t.call(inst, 'share', window=w, view=S)
    sid = t.wait_shared(S)
    pub_before = load(str(root / 'publisher.json'))
    epoch0 = pub_before['epoch']
    old_ph = inst['plugin_host_pid']
    hosts = [p['pid'] for p in plugin_hosts(t.root_dir, inst['sublime_pid'])]
    # kill shortly after a beat would favour a long window; record where in the cycle we kill
    at_kill = load(str(root / 'publisher.json'))
    killed_at = now()
    t.stop(inst, graceful=None if together else False)
    tree_at_kill = tree(root) if root.exists() else None
    after_kill_procs = [{k: p[k] for k in ('pid', 'ppid', 'exe')} for p in mine(t.root_dir)]
    timeline = reader_timeline(root, killed_at, limit_s=hb['stale_after_s'] + 20)
    obs = {'mode': 'editor and plugin hosts killed together' if together else 'editor only killed (orphan plugin host)',
           'heartbeat_s': hb['heartbeat_s'], 'stale_after_s': hb['stale_after_s'],
           'publisher_json_interval': [pub_before.get('heartbeat_interval_s'), pub_before.get('stale_after_s')],
           'killed_sublime_pid': inst['sublime_pid'], 'plugin_hosts_at_kill': hosts, 'killed_at': killed_at,
           'heartbeat_age_at_kill_s': round(killed_at - at_kill['heartbeat_at'], 3),
           'inferred_live_window_s': round(at_kill['heartbeat_at'] + at_kill['stale_after_s'] - killed_at, 3),
           'disposable_processes_right_after_kill': after_kill_procs,
           'tree_right_after_kill': tree_at_kill, 'reader_timeline': timeline,
           'reader_still_live_window_s': timeline['reader_first_not_live_s']}
    obs['tree_after_reader_not_live'] = tree(root) if root.exists() else None
    if not together:
        def orphan_gone():
            return gone(old_ph)
        wait_for(orphan_gone, max(30, hb['stale_after_s'] + 15), 0.05, 'orphan plugin host exit')
        obs['orphan_plugin_host_exited_after_s'] = round(now() - killed_at, 2)
        obs['root_exists_after_orphan_exit'] = root.exists()
    else:
        obs['plugin_hosts_alive_after_kill'] = [p for p in hosts if not gone(p)]
        time.sleep(1.0)
        obs['tree_before_restart'] = tree(root) if root.exists() else None
    residue = obs['tree_before_restart'] if together else (tree(root) if root.exists() else [])
    obs['residue_before_restart'] = residue
    note = None
    if together and residue:
        st_old = load(str(root / 'views' / sid / 'state.json'))
        obs['residue_state_epoch'] = st_old['epoch']
        ino = Inotify(root)
        for d in [root] + ([root / 'views'] if (root / 'views').is_dir() else []) + \
                 [root / 'views' / n for n in os.listdir(str(root / 'views'))]:
            ino.watch(d)
        ino.start()
        note = ino
    restart_at = now()
    new = t.launch(tag + '-restart', data)
    insts.append(new)
    holder['inst'] = new
    info = wait_for(lambda: (lambda i: i if i['epoch'] != epoch0 else None)(load(str(root / 'publisher.json'))),
                    15, 0.02, 'restart epoch')
    time.sleep(0.3)
    obs['restart_started_after_kill_s'] = round(restart_at - killed_at, 2)
    obs['epoch_before'], obs['epoch_after_restart'] = epoch0, info['epoch']
    obs['new_publisher_pid'], obs['new_plugin_host_pid'] = info['pid'], new['plugin_host_pid']
    obs['tree_after_restart'] = tree(root)
    try:
        reader.read_current(str(root))
        obs['reader_after_restart'] = 'capture presented (unexpected)'
    except (reader.NotLive, reader.Unavailable) as exc:
        obs['reader_after_restart'] = '{}: {}'.format(type(exc).__name__, exc)
    obs['reader_publisher_after_restart'] = (lambda i: {'epoch': i['epoch'], 'pid': i['pid']})(reader.publisher(str(root)))
    clean = os.listdir(str(root / 'views')) == [] and t.index()['shared'] == [] and not os.path.lexists(str(root / 'current'))
    obs['restart_clean'] = clean
    ok = clean and info['epoch'] != epoch0 and info['pid'] == new['plugin_host_pid']
    ok = ok and timeline['reader_first_not_live_s'] is not None
    if note is not None:
        events = note.close()
        obs['inotify_events'] = events
        old = set(residue)
        deletes, first_new = {}, None
        for e in events:
            rel = os.path.normpath(os.path.join(e['dir'], e['name'])) if e['name'] else None
            if 'DELETE' in e['mask'] and rel is not None:
                key = rel + ('/' if 'ISDIR' in e['mask'] else '')
                if key in old or key + '@' in old:
                    deletes[key] = e['n']
            if first_new is None and ('CREATE' in e['mask'] or 'MOVED_TO' in e['mask']):
                first_new = e['n']
        # step 5: the dead holder's publisher.lock is reused (locked again), never deleted
        residue_paths = [p.rstrip('@') for p in residue if p != contract.LOCK_NAME]
        missing = [p for p in residue_paths if p not in deletes]
        last_delete = max(deletes.values()) if deletes else None
        obs['residue_removal'] = {
            'residue_paths': residue_paths, 'deleted_event_index': deletes, 'not_seen_deleted': missing,
            'lock_file_in_residue': contract.LOCK_NAME in residue,
            'last_residue_delete_event': last_delete, 'first_create_or_moved_to_event': first_new,
            'all_residue_removed_before_anything_new': (not missing and last_delete is not None
                                                        and first_new is not None and last_delete < first_new),
            'first_new_event': events[first_new] if first_new is not None else None}
        obs['residue_state_epoch_was_dead_epoch'] = obs['residue_state_epoch'] == epoch0
        ok = (ok and obs['residue_removal']['all_residue_removed_before_anything_new']
              and obs['residue_state_epoch_was_dead_epoch']
              and obs['tree_right_after_kill'] == obs['tree_before_restart']
              and 'publisher.json' in residue and 'current@' in residue and contract.LOCK_NAME in residue
              and 'views/{}/state.json'.format(sid) in residue
              and not obs['plugin_hosts_alive_after_kill']
              and timeline['changes'][-1]['current_state_json_on_disk'])
    elif together:
        ok = False
        obs['error'] = 'no residue persisted after the combined kill'
    return ok, obs


def unshared_scan(root, markers, forbidden_ids):
    """Every regular file under root: raw bytes for each marker; every JSON file: any
    'view'/'buffer' value equal to a forbidden id. Files vanishing mid-scan are skipped."""
    hits, files = [], 0

    def walk(obj, path):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in forbidden_ids and isinstance(v, int) and v in forbidden_ids[k]:
                    hits.append({'file': path, 'key': k, 'value': v})
                walk(v, path)
        elif isinstance(obj, list):
            for v in obj:
                walk(v, path)
    for dirpath, _, names in os.walk(str(root)):
        for n in names:
            p = os.path.join(dirpath, n)
            if os.path.islink(p):
                continue
            try:
                with open(p, 'rb') as handle:
                    raw = handle.read()
            except FileNotFoundError:
                continue
            files += 1
            for m in markers:
                if m.encode() in raw:
                    hits.append({'file': p, 'marker': m})
            if n.endswith('.json'):
                try:
                    walk(json.loads(raw.decode('utf-8')), p)
                except ValueError:
                    hits.append({'file': p, 'unparseable': True})
    return hits, files


def _local_listing(data):
    local = data / 'Local'
    if not local.is_dir():
        return None
    return {n: {'size': (local / n).stat().st_size, 'mtime': round((local / n).stat().st_mtime, 2)}
            for n in sorted(os.listdir(str(local)))}


def exit_diagnostic_2b(t, insts):
    """Time-boxed look at the ignored exit (no workaround): which start histories make the
    editor ignore `exit` for 20 s? Each scenario uses its own fresh profile."""
    runs = []

    def one_exit(inst, label):
        w = t.call(inst, 'new_window')['window']
        S = t.call(inst, 'create', window=w, title='exit synthetic')['view']
        t.call(inst, 'write', window=w, view=S, text='exit residue?\n')
        t.call(inst, 'share', window=w, view=S)
        t.wait_shared(S)
        started = time.monotonic()
        t.stop(inst)
        rec = inst['record']
        return {'label': label, 'stopped_by': rec['stopped_by'], 'exit_s': rec.get('exit_s'),
                'stop_total_s': round(time.monotonic() - started, 2),
                'inventory_before_exit': rec.get('inventory_before_exit'), 'exit_ignored': rec.get('exit_ignored')}

    def crash(inst, data, tag, file_backed, together, wait_s):
        w = t.call(inst, 'new_window')['window']
        if file_backed:
            F = t.call(inst, 'create', window=w, path=str(t.syn / tag / 'dirty.md'), disk_text='synthetic disk\n')['view']
            time.sleep(0.3)
            t.call(inst, 'write', window=w, view=F, text='unsaved synthetic edit\n', mode='append')
        S = t.call(inst, 'create', window=w, title='crash synthetic')['view']
        t.call(inst, 'write', window=w, view=S, text='crash\n')
        t.call(inst, 'share', window=w, view=S)
        t.wait_shared(S)
        time.sleep(wait_s)
        before = t.call(inst, 'inventory')['windows']
        ph = inst['plugin_host_pid']
        killed_at = now()
        t.stop(inst, graceful=None if together else False)
        wait_for(lambda: gone(ph), 30, 0.05, 'plugin host gone after crash')
        time.sleep(0.5)
        return {'inventory_before_crash': before, 'killed_at': killed_at, 'local_after_crash': _local_listing(data),
                'crash_reports': sorted(os.listdir(str(data / 'Crash Reports'))) if (data / 'Crash Reports').is_dir() else None}

    scenarios = [
        ('S1 fresh profile, exit', None),
        ('S2 crash (editor only) after a dirty file-backed view, restart, exit', dict(file_backed=True, together=False)),
        ('S3 crash (editor+hosts) after a dirty file-backed view, restart, exit', dict(file_backed=True, together=True)),
        ('S4 crash (editor+hosts) with scratch views only, restart, exit', dict(file_backed=False, together=True)),
        ('S5 clean exit, restart on the same profile, exit', 'clean'),
    ]
    for n, (label, how) in enumerate(scenarios, 1):
        tag = 'e{}'.format(n)
        data = t.data_dir(tag)
        run = {'scenario': label}
        try:
            inst = t.launch(tag, data)
            insts.append(inst)
            run['inventory_at_start'] = t.call(inst, 'inventory')['windows']
            if how is None:
                run['exit'] = one_exit(inst, 'first start')
            elif how == 'clean':
                run['first_exit'] = one_exit(inst, 'first start')
                run['local_after_clean_exit'] = _local_listing(data)
                wait_for(lambda: not (t.root / 'publisher.json').exists(), 30, 0.1, 'root free')
                again = t.launch(tag + 'r', data)
                insts.append(again)
                run['inventory_after_restart'] = t.call(again, 'inventory')['windows']
                run['exit'] = one_exit(again, 'restart after clean exit')
            else:
                run['crash'] = crash(inst, data, tag, how['file_backed'], how['together'],
                                     wait_s=float(os.environ.get('X1_EXIT2B_WAIT_S', '3')))
                run['crash']['pre_crash_wait_s'] = float(os.environ.get('X1_EXIT2B_WAIT_S', '3'))
                again = t.launch(tag + 'r', data)
                insts.append(again)
                time.sleep(1.0)
                run['inventory_after_restart'] = t.call(again, 'inventory')['windows']
                run['local_after_restart'] = _local_listing(data)
                run['exit'] = one_exit(again, 'restart after crash')
        except Exception as exc:
            run['error'] = '{}: {}'.format(type(exc).__name__, exc)
        runs.append(run)
        print('exit2b', label, '->', (run.get('exit') or {}).get('stopped_by'), (run.get('exit') or {}).get('exit_s'), flush=True)
        try:
            wait_for(lambda: not (t.root / 'publisher.json').exists(), 40, 0.1, 'root free after scenario')
        except TimeoutError as exc:
            run['root_not_free'] = str(exc)
    t.report['exit_diagnostic_2b'] = runs


def evidence_dir():
    raw = os.environ.get('X1_EVIDENCE_DIR')
    if not raw:
        raise SystemExit('X1_EVIDENCE_DIR is required (evidence never goes into the source tree)')
    path = Path(raw).resolve()
    if not path.is_dir():
        raise SystemExit('X1_EVIDENCE_DIR {} is not a directory'.format(path))
    if path == IMPL or IMPL in path.parents:
        raise SystemExit('X1_EVIDENCE_DIR {} is inside the source tree {}'.format(path, IMPL))
    return path


def main():
    evidence = evidence_dir()          # fail before any editor starts
    sys.addaudithook(_audit)           # step 5b: record every /proc path opened or listed
    set_child_subreaper()              # step 5b: double-forked and orphaned children stay ours
    t = Trial()
    T = t.root_dir
    print('trial root', T, flush=True)
    t.report['operator_editor_before'] = operator_editors()
    t.report['started_at'] = now()
    override = os.environ.get('X1_HEARTBEAT_S') or None
    hb = heartbeat_params(override)
    t.report['heartbeat'] = hb
    data_a = t.data_dir('a', heartbeat_s=None if override is None else hb['heartbeat_s'])
    t.report['source_root'] = str(IMPL)
    t.report['payload_files'] = sorted(os.listdir(str(IMPL / 'SublimeObserver')))
    t.report['installed_into_disposable_packages'] = sorted(os.listdir(str(data_a / 'Packages' / 'SublimeObserver')))
    t.report['installed_equals_payload'] = t.report['payload_files'] == t.report['installed_into_disposable_packages']
    insts = []
    try:
        if os.environ.get('X1_ONLY') == 'exit2b':
            exit_diagnostic_2b(t, insts)
            return
        if os.environ.get('X1_ONLY') == 'exit':         # diagnostic: graceful exit timing only
            runs = []
            for n in range(3):
                inst = t.launch('x{}'.format(n), data_a if n == 0 else t.data_dir('x{}'.format(n)))
                insts.append(inst)
                wx = t.call(inst, 'new_window')['window']
                S = t.call(inst, 'create', window=wx, title='exit synthetic')['view']
                t.call(inst, 'write', window=wx, view=S, text='exit residue?\n')
                t.call(inst, 'share', window=wx, view=S)
                t.wait_shared(S)
                ph, start = inst['plugin_host_pid'], now()
                t.call(inst, 'exit')
                marks = {}
                while now() - start < 25 and len(marks) < 3:
                    for key, done in (('sublime_exit_s', inst['popen'].poll() is not None),
                                      ('plugin_host_exit_s', gone(ph)),
                                      ('root_removed_s', not t.root.exists())):
                        if done and key not in marks:
                            marks[key] = round(now() - start, 2)
                    time.sleep(0.02)
                runs.append(marks)
                if inst['popen'].poll() is None:
                    t.stop(inst)
                inst['alive'] = inst['record']['alive'] = False
                wait_for(lambda: gone(ph), 20, 0.05, 'plugin host exit')
            t.report['exit_diagnostic'] = runs
            print(json.dumps(runs), flush=True)
            return
        a = t.launch('a', data_a)
        insts.append(a)
        hello = t.call(a, 'hello')
        pub_info = wait_for(lambda: load(str(t.root / 'publisher.json')), 10, 0.05, 'publisher.json')

        beats, end = [], now() + hb['stale_after_s'] + 1
        while now() < end:                      # idle heartbeat cadence, harness clock vs heartbeat_at
            info = load(str(t.root / 'publisher.json'))
            if not beats or info['heartbeat_at'] != beats[-1][1]:
                beats.append([now(), info['heartbeat_at']])
            time.sleep(0.05)
        t.report['heartbeat_cadence'] = {
            'beats': beats, 'intervals_s': [round(y[1] - x[1], 3) for x, y in zip(beats, beats[1:])],
            'write_lag_s': [round(b[0] - b[1], 3) for b in beats[1:]],
            'clock_offset_at_start_s': round(beats[0][0] - beats[0][1], 3)}

        def c18():
            iv = t.report['heartbeat_cadence']['intervals_s']
            ok = (pub_info['heartbeat_interval_s'] == hb['heartbeat_s'] and pub_info['stale_after_s'] == hb['stale_after_s']
                  and bool(iv) and all(abs(x - hb['heartbeat_s']) < 0.25 for x in iv))
            return ok, {'expected_from_settings': hb, 'publisher_json': {k: pub_info[k] for k in ('heartbeat_interval_s', 'stale_after_s')},
                        'measured_intervals_s': iv}
        t.check(18, 'heartbeat interval and stale bound read from the package settings (2b)', c18)

        def c1():
            ph = a['identity']['plugin_host']
            obs = {'fixture_build': hello['build'], 'fixture_python': hello['python'],
                   'publisher_json': pub_info, 'plugin_host_exe': ph['exe'],
                   'packages_path': hello['packages_path'], 'proc_visible_in_sandbox': hello['proc_visible'],
                   'python_version_pin': (data_a / 'Packages/SublimeObserver/.python-version').read_text().strip()}
            ok = (pub_info['sublime_build'] == '4215' and pub_info['plugin_python'].startswith('3.14')
                  and pub_info['pid'] == a['plugin_host_pid'] and ph['exe'].endswith('plugin_host-3.14'))
            return ok, obs
        t.check(1, 'build and plugin Python host', c1)

        w1 = t.call(a, 'new_window')['window']
        disk = ''.join('synthetic disk line {:03d}\n'.format(n) for n in range(400))
        A = t.call(a, 'create', window=w1, path=str(t.syn / 'A' / 'same.md'), disk_text=disk)['view']
        marker = 'UNSHARED-MARKER-' + uuid.uuid4().hex
        created_u = t.call(a, 'create', window=w1, title='unshared synthetic')
        U, u_buffer = created_u['view'], created_u['buffer']
        t.call(a, 'write', window=w1, view=U, text=marker + '\nnever published\n')
        time.sleep(0.5)
        share = t.call(a, 'share', window=w1, view=A)
        sid_a = t.wait_shared(A)

        def c2():
            st, text = reader.read_current(str(t.root))
            m = modes(t.root)
            dirs_ok = all(v == '0o700' for k, v in m.items() if k.endswith('/'))
            files_ok = all(v in ('0o600', 'symlink') for k, v in m.items() if not k.endswith('/'))
            return (share['shared'] and text == disk and st['path'] == str(t.syn / 'A' / 'same.md')
                    and dirs_ok and files_ok and os.readlink(str(t.root / 'current')) == 'views/' + sid_a), {
                'modes': m, 'current': os.readlink(str(t.root / 'current')), 'state_text_file': st['text_file'],
                'revision': st['revision'], 'dirty': st['dirty'], 'reader_text_matches_disk_text': text == disk,
                'index': t.index()}
        t.check(2, 'share a saved synthetic view', c2)

        def c16():
            snap = t.call(a, 'snapshot')
            return snap['views'][str(A)]['status'] == 'Observer: SHARED', {
                'status_api_value_A': snap['views'][str(A)]['status'],
                'status_api_value_unshared_U': snap['views'][str(U)]['status'],
                'rendering': 'not observed: headless virtual display, API value only'}
        t.check(16, 'status marker as the API reports it', c16)

        def c3():
            r0 = t.state(sid_a)['revision']
            t1 = 'edited once\n' + disk
            e1 = t.call(a, 'write', window=w1, view=A, text=t1)
            wait_for(lambda: t.state(sid_a)['revision'] == e1['revision'], 5, what='rev1')
            after1 = t.texts(sid_a)
            t2 = 'edited twice\n' + disk
            e2 = t.call(a, 'write', window=w1, view=A, text=t2)
            wait_for(lambda: t.state(sid_a)['revision'] == e2['revision'], 5, what='rev2')
            st, text = reader.read_capture(str(t.vdir(sid_a)))
            after2 = t.texts(sid_a)
            want = [contract.text_name(sid_a, e1['revision']), contract.text_name(sid_a, e2['revision'])]
            disk_now = (t.syn / 'A' / 'same.md').read_text()
            return (sorted(after2) == sorted(want) and text == t2 and st['dirty'] and disk_now == disk
                    and st['text_file'] == contract.text_name(sid_a, e2['revision'])), {
                'revisions': [r0, e1['revision'], e2['revision']], 'texts_after_first': after1,
                'texts_after_second': after2, 'state_text_file': st['text_file'], 'dirty': st['dirty'],
                'disk_unchanged': disk_now == disk}
        t.check(3, 'unsaved edit: new revision, retention', c3)

        def c4():
            st0 = t.state(sid_a)
            name = st0['text_file']
            ino = os.stat(str(t.vdir(sid_a) / name)).st_ino
            ev0 = t.call(a, 'events')['events'].get(str(A), {})
            sel_at = time.monotonic()
            t.call(a, 'selection', window=w1, view=A, regions=[[5, 5], [20, 40]])
            try:
                st1 = wait_for(lambda: (lambda s: s if s['seq'] > st0['seq'] and len(s['selections']) == 2 else None)(t.state(sid_a)), 2, what='caret state')
                caret_ms = round((time.monotonic() - sel_at) * 1000, 1)
            except TimeoutError:
                st1, caret_ms = None, None
            ev1 = t.call(a, 'events')['events'].get(str(A), {})
            caret = {'selection_event_count_before': ev0.get('on_selection_modified', 0),
                     'selection_event_count_after': ev1.get('on_selection_modified', 0),
                     'caret_to_state_ms': caret_ms, 'state_seq_after_2s': t.state(sid_a)['seq'],
                     'state_selections_after_2s': t.state(sid_a)['selections']}
            t.report['diag_check4'] = caret
            if st1 is None:
                raise RuntimeError('programmatic selection not published within 2 s: {}'.format(caret))
            ino1 = os.stat(str(t.vdir(sid_a) / name)).st_ino
            before_scroll = time.monotonic()
            scrolled = t.call(a, 'scroll', window=w1, view=A, viewport=[0, 900])
            st2 = wait_for(lambda: (lambda s: s if s['viewport_position'][1] != st1['viewport_position'][1] else None)(t.state(sid_a)), 3, what='viewport state')
            poll_delay = round((time.monotonic() - before_scroll) * 1000, 1)
            ino2 = os.stat(str(t.vdir(sid_a) / name)).st_ino
            return (st1['text_file'] == name and st2['text_file'] == name and ino == ino1 == ino2
                    and st1['revision'] == st0['revision']), {
                'seq': [st0['seq'], st1['seq'], st2['seq']], 'selections': st1['selections'],
                'viewport_before': st1['viewport_position'], 'viewport_after': st2['viewport_position'],
                'fixture_viewport': scrolled['viewport_position'], 'visible_region': st2['visible_region'],
                'text_inode_unchanged': ino == ino1 == ino2, 'scroll_to_state_ms': poll_delay,
                'texts': t.texts(sid_a), 'caret': caret}
        t.check(4, 'caret move and scroll rewrite state only', c4)

        w2 = t.call(a, 'new_window')['window']
        B = t.call(a, 'open_same', window=w2, view=A)['view']
        time.sleep(0.3)
        t.call(a, 'share', window=w2, view=B)

        def c5():
            sid_b = t.wait_shared(B)
            idx = t.index()['shared']
            ea, eb = t.entry(A), t.entry(B)
            return (len(idx) == 2 and not os.path.lexists(str(t.root / 'current')) and ea['view'] != eb['view']
                    and ea['share_id'] != eb['share_id'] and ea['window'] != eb['window']), {
                'index': idx, 'current_present': os.path.lexists(str(t.root / 'current')),
                'same_buffer': ea['buffer'] == eb['buffer'], 'sid_b': sid_b}
        t.check(5, 'two shared views (same file, two windows)', c5)

        def c8():
            before = t.call(a, 'snapshot')
            t.call(a, 'write', window=w1, view=A, text='appended by fixture\n', mode='append')
            time.sleep(1.6)                     # debounce + several viewport polls + publications
            after = t.call(a, 'snapshot')
            diffs = []
            if before['active_window'] != after['active_window']:
                diffs.append('active_window')
            if before['windows'] != after['windows']:
                diffs.append('active_views')
            for vid, v in before['views'].items():
                w = after['views'].get(vid)
                for key in ('sel', 'viewport_position', 'window'):
                    if w is None or v[key] != w[key]:
                        diffs.append('{}:{}'.format(vid, key))
            return not diffs, {'differences': diffs, 'before': before, 'after': after}
        t.check(8, 'publishing does not change focus, selection or viewport', c8)

        def c9():
            idx0 = t.index()['shared']
            views0 = sorted(os.listdir(str(t.root / 'views')))
            out = {}
            for rel in ('.majkee/x.md', 'proj/.env.test'):
                v = t.call(a, 'create', window=w1, path=str(t.syn / rel), disk_text='SYNTHETIC SEALED\n')['view']
                time.sleep(0.3)
                r = t.call(a, 'share', window=w1, view=v)
                out[rel] = {'view': v, 'shared': r['shared'], 'status': r['status']}
                t.call(a, 'close', window=w1, view=v)
            time.sleep(0.3)
            same = t.index()['shared'] == idx0 and sorted(os.listdir(str(t.root / 'views'))) == views0
            return same and not any(x['shared'] for x in out.values()), dict(out, index_unchanged=same)
        t.check(9, 'sealed-path refusal', c9)

        def c7():
            sid_b = t.entry(B)['share_id']
            r = t.call(a, 'share', window=w1, view=A)            # toggle again = unshare
            time.sleep(0.2)
            idx1 = t.index()['shared']
            cur1 = readlink(str(t.root / 'current'))
            gone_a = not t.vdir(sid_a).exists()
            t.call(a, 'close', window=w2, view=B)
            time.sleep(0.3)
            idx2 = t.index()['shared']
            snap = t.call(a, 'snapshot')
            return (not r['shared'] and gone_a and [e['view'] for e in idx1] == [B] and cur1 == 'views/' + sid_b
                    and idx2 == [] and not os.path.lexists(str(t.root / 'current')) and not t.vdir(sid_b).exists()
                    and not snap['views'][str(A)]['status']), {
                'after_unshare_index': idx1, 'after_unshare_current': cur1, 'a_dir_removed': gone_a,
                'after_close_index': idx2, 'b_dir_removed': not t.vdir(sid_b).exists(),
                'status_A_after_unshare': snap['views'][str(A)]['status'], 'views_dir': os.listdir(str(t.root / 'views'))}
        t.check(7, 'unshare and close cleanup', c7)

        def c13():
            text = 'A\U0001F600B\U0001D518C\n\U0001F469‍\U0001F4BB\n'
            E = t.call(a, 'create', window=w1, title='astral synthetic')['view']
            t.call(a, 'write', window=w1, view=E, text=text)
            t.call(a, 'share', window=w1, view=E)
            sid = t.wait_shared(E)
            st, published = reader.read_capture(str(t.vdir(sid)))
            p2 = t.call(a, 'probe_text', window=w1, view=E, cap=2)
            p3 = t.call(a, 'probe_text', window=w1, view=E, cap=3)
            t.call(a, 'share', window=w1, view=E)
            t.call(a, 'close', window=w1, view=E)
            return (st['size_chars'] == len(text) == len(published) == st['published_chars']
                    and p2['capped_text'] == text[:2]), {
                'python_len_input': len(text), 'utf16_units_input': len(text.encode('utf-16-le')) // 2,
                'size_chars': st['size_chars'], 'published_chars': st['published_chars'],
                'python_len_published': len(published), 'published_equals_input': published == text,
                'probe_cap2': p2, 'probe_cap3': p3, 'selections': st['selections']}
        t.check(13, 'non-BMP characters versus Python len', c13)

        def c14():
            big = ''.join('x' * 99 + '\n' for _ in range(1999))
            L = t.call(a, 'create', window=w1, title='large synthetic')['view']
            t.call(a, 'write', window=w1, view=L, text=big)
            t.call(a, 'share', window=w1, view=L)
            sid = t.wait_shared(L, timeout=10)
            cost = t.call(a, 'time_capture', window=w1, view=L, n=30, timeout=60)
            edit_to_state, observed_wall = [], []
            for _ in range(30):
                e = t.call(a, 'write', window=w1, view=L, text='y', mode='append')
                wait_for(lambda: t.state(sid)['revision'] >= e['revision'], 5, 0.002, 'large publish')
                mtime = os.stat(str(t.vdir(sid) / 'state.json')).st_mtime
                edit_to_state.append((mtime - e['t_edit']) * 1000)
                observed_wall.append((now() - e['t_edit']) * 1000)
                time.sleep(0.25)
            st = t.state(sid)
            t.call(a, 'share', window=w1, view=L)
            t.call(a, 'close', window=w1, view=L)
            return True, {'buffer_chars': cost['size'], 'main_thread_capture': cost,
                          'edit_to_state_replace_ms': summary(edit_to_state),
                          'edit_to_harness_observed_ms': summary(observed_wall),
                          'final_state': {k: st[k] for k in ('size_chars', 'published_chars', 'truncated', 'cap')},
                          'method': ('t_edit = time.time() in the editor right after the insert command; '
                                     'state replacement = st_mtime of state.json (tmpfs, coarse kernel clock); '
                                     'includes the 150 ms trailing debounce by design. Capture = perf_counter '
                                     'around publisher.capture_view on the plugin-host main thread, 30 runs.')}
        t.check(14, 'typing impact with a ~200k buffer', c14)

        def c15():
            K = t.call(a, 'create', window=w1, title='burst synthetic')['view']
            t.call(a, 'write', window=w1, view=K, text='burst\n')
            t.call(a, 'share', window=w1, view=K)
            sid = t.wait_shared(K)
            path = str(t.vdir(sid) / 'state.json')
            last_seq = t.state(sid)['seq']
            b = t.call(a, 'burst', window=w1, view=K, duration_ms=2600, interval_ms=50)
            samples = []
            end = now() + 4.0
            while now() < end:
                try:
                    s = load(path)
                except (FileNotFoundError, ValueError):
                    continue
                if s['seq'] != last_seq:
                    last_seq = s['seq']
                    samples.append([os.stat(path).st_mtime, s['revision']])
                time.sleep(0.003)
            res = t.call(a, 'burst_result', window=w1, view=K)
            edits = res['edits']
            first_edit, last_edit = edits[0][0], edits[-1][0]
            during = [m for m, _ in samples if first_edit <= m <= last_edit + 0.01]
            marks = [first_edit] + during + [last_edit]
            gaps = [round((y - x) * 1000, 1) for x, y in zip(marks, marks[1:])]
            final_rev = samples[-1][1] if samples else None
            trailing = round((samples[-1][0] - last_edit) * 1000, 1) if samples else None
            t.call(a, 'share', window=w1, view=K)
            t.call(a, 'close', window=w1, view=K)
            return (bool(during) and max(gaps) <= 1100 and final_rev == edits[-1][1]), {
                'edits': len(edits), 'burst_s': round(last_edit - first_edit, 3),
                'publications_during_burst': len(during), 'max_gap_ms': max(gaps) if gaps else None,
                'gaps_ms': gaps, 'final_revision_published': final_rev, 'last_edit_revision': edits[-1][1],
                'trailing_publish_after_last_edit_ms': trailing}
        t.check(15, 'continuous edits: maximum delay holds', c15)

        def c6():
            # 2b: view P is shared and publishing continuously (a burst of edits) while an
            # unshared view Q is opened, edited, re-selected and scrolled.
            base_p = 'publishing synthetic P\n'
            P = t.call(a, 'create', window=w1, title='shared publishing synthetic')['view']
            t.call(a, 'write', window=w1, view=P, text=base_p)
            t.call(a, 'share', window=w1, view=P)
            sid_p = t.wait_shared(P)
            marker_q = 'UNSHARED-Q-MARKER-' + uuid.uuid4().hex
            assert marker_q not in base_p
            burst = t.call(a, 'burst', window=w1, view=P, duration_ms=5000, interval_ms=50)
            time.sleep(0.4)
            p_states, scans, files_scanned = [], [], 0

            def sample(label, scan=True):
                nonlocal files_scanned
                try:
                    s = t.state(sid_p)
                    p_states.append({'label': label, 't': now(), 'seq': s['seq'], 'revision': s['revision']})
                except (FileNotFoundError, ValueError):
                    pass
                if scan:
                    found, n = unshared_scan(t.root, [marker, marker_q], ids)
                    files_scanned += n
                    scans.append({'label': label, 'hits': found, 'files': n})
            ids = {'view': {U}, 'buffer': {u_buffer}}
            sample('before Q opened')
            created = t.call(a, 'create', window=w1, title='unshared synthetic Q')
            Q, q_buffer = created['view'], created['buffer']
            ids['view'].add(Q)
            ids['buffer'].add(q_buffer)
            q_window_start = now()
            sample('Q opened')
            q_text = ''.join('{} line {:03d}\n'.format(marker_q, n) for n in range(300))
            t.call(a, 'write', window=w1, view=Q, text=q_text)
            sample('Q written')
            t.call(a, 'write', window=w1, view=Q, text='edited ' + marker_q + '\n', mode='append')
            sample('Q edited')
            t.call(a, 'selection', window=w1, view=Q, regions=[[10, 10], [50, 80]])
            sample('Q selection moved')
            scrolled = t.call(a, 'scroll', window=w1, view=Q, viewport=[0, 2000])
            sample('Q scrolled')
            settle_end = now() + 2.5                # > debounce + several viewport polls
            n_settle = 0
            while now() < settle_end:
                n_settle += 1
                sample('Q settling', scan=n_settle % 5 == 0)
                time.sleep(0.1)
            sample('Q settled')
            q_window_end = now()
            wait_for(lambda: t.call(a, 'burst_result', window=w1, view=P).get('done'), 10, 0.1, 'P burst done')
            res = t.call(a, 'burst_result', window=w1, view=P)
            time.sleep(1.2)
            sample('final, after P burst')
            final_p = t.state(sid_p)
            _, p_text = reader.read_capture(str(t.vdir(sid_p)))
            index_views = [e['view'] for e in t.index()['shared']]
            view_dirs = sorted(os.listdir(str(t.root / 'views')))
            q_events = t.call(a, 'events')['events'].get(str(Q), {})
            in_window = [s for s in p_states if q_window_start <= s['t'] <= q_window_end]
            seq_start = max([s['seq'] for s in p_states if s['t'] <= q_window_start] or [0])
            seq_end = min([s['seq'] for s in p_states if s['t'] >= q_window_end] or [0])
            all_hits = [h for s in scans for h in s['hits']]
            p_text_ok = p_text is not None and p_text.startswith(base_p) and set(p_text[len(base_p):]) <= {'k'}
            kept_publishing = seq_end - seq_start >= 2 and len({s['seq'] for s in in_window}) >= 2
            ok = (not all_hits and index_views == [P] and view_dirs == [sid_p] and p_text_ok and kept_publishing
                  and final_p['revision'] == res['edits'][-1][1] and Q != P and q_buffer != t.entry(P)['buffer'])
            observed = {'shared_view_P': P, 'share_id_P': sid_p, 'unshared_view_Q': Q, 'unshared_buffer_Q': q_buffer,
                        'old_unshared_view_U': U, 'markers': [marker, marker_q], 'forbidden_ids': {k: sorted(v) for k, v in ids.items()},
                        'scans': scans, 'files_scanned_total': files_scanned, 'hits': all_hits,
                        'index_views': index_views, 'view_dirs': view_dirs,
                        'q_editor_events_seen_by_fixture': q_events, 'q_scroll': scrolled,
                        'p_text_is_only_P_content': p_text_ok,
                        'p_seq_before_Q_window': seq_start, 'p_seq_after_Q_window': seq_end,
                        'q_window_s': round(q_window_end - q_window_start, 3),
                        'p_distinct_seqs_inside_Q_window': sorted({s['seq'] for s in in_window}),
                        'p_states': p_states, 'p_burst_edits': len(res['edits']),
                        'p_final_revision': final_p['revision'], 'p_last_edit_revision': res['edits'][-1][1],
                        'burst_deadline': burst['deadline']}
            t.call(a, 'share', window=w1, view=P)
            t.call(a, 'close', window=w1, view=P)
            t.call(a, 'close', window=w1, view=Q)
            return ok, observed
        t.check(6, 'unshared view publishes nothing while another view publishes (2b)', c6)

        def c10():
            S = t.call(a, 'create', window=w1, title='reload synthetic')['view']
            t.call(a, 'write', window=w1, view=S, text='reload me\n')
            t.call(a, 'share', window=w1, view=S)
            sid = t.wait_shared(S)
            epoch0 = load(str(t.root / 'publisher.json'))['epoch']
            target = data_a / 'Packages/SublimeObserver/publisher.py'
            target.write_bytes((IMPL / 'SublimeObserver/publisher.py').read_bytes())   # same content, new mtime
            info = wait_for(lambda: (lambda i: i if i['epoch'] != epoch0 else None)(load(str(t.root / 'publisher.json'))),
                            15, 0.05, 'new epoch after reload')
            time.sleep(0.5)
            pubst = t.call(a, 'publisher')
            snap = t.call(a, 'snapshot')
            views_left = os.listdir(str(t.root / 'views'))
            t.call(a, 'close', window=w1, view=S)
            return (info['epoch'] != epoch0 and pubst['runtime']['shared_views'] == [] and views_left == []
                    and t.index()['shared'] == [] and not snap['views'][str(S)]['status']), {
                'epoch_before': epoch0, 'epoch_after': info['epoch'], 'runtime_after': pubst['runtime'],
                'views_dir_after': views_left, 'old_share_dir_exists': t.vdir(sid).exists(),
                'status_after_reload': snap['views'][str(S)]['status']}
        t.check(10, 'plugin reload', c10)

        holder = {'inst': a}

        def c11():
            ok, obs = crash_case(t, holder, data_a, 'a', hb, False, insts)
            return ok and obs['reader_timeline']['reader_first_not_live_s'] is not None, obs
        t.check(11, 'crash: kill -9 of the editor only (orphan plugin host), restart', c11)
        a = holder['inst']

        def c11b():
            return crash_case(t, holder, data_a, 'a2', hb, True, insts)
        t.check('11b', 'crash: editor and plugin hosts killed together, residue persists, restart removes it before publishing (2b)', c11b)
        a = holder['inst']

        def c12():
            data_b = t.data_dir('b')
            info0 = load(str(t.root / 'publisher.json'))
            b = t.launch('b', data_b)
            insts.append(b)
            pub_b = t.call(b, 'publisher')
            wb = t.call(b, 'new_window')['window']
            V = t.call(b, 'create', window=wb, title='second instance synthetic')['view']
            t.call(b, 'write', window=wb, view=V, text='must not publish\n')
            r = t.call(b, 'share', window=wb, view=V)
            info1 = load(str(t.root / 'publisher.json'))
            t.stop(b)
            time.sleep(0.5)
            info2 = load(str(t.root / 'publisher.json'))
            beat = wait_for(lambda: (lambda i: i if i['heartbeat_at'] > info2['heartbeat_at'] else None)(load(str(t.root / 'publisher.json'))),
                            8, 0.1, 'first instance heartbeat after second stopped')
            return (not pub_b['runtime']['publishing'] and not r['shared'] and info0['epoch'] == info1['epoch'] == info2['epoch']
                    and t.index()['shared'] == []), {
                'second_runtime': pub_b['runtime'], 'second_share_attempt': r,
                'epoch_kept': info0['epoch'] == info1['epoch'] == info2['epoch'],
                'first_heartbeat_continues': beat['heartbeat_at'] > info2['heartbeat_at'],
                'second_pids': {'sublime': b['sublime_pid'], 'plugin_host': b['plugin_host_pid']}}
        t.check(12, 'second instance beside a live publisher refuses', c12)

        # graceful exit of the restarted first instance: does unload clean the root?
        def c17():
            wx = t.call(a, 'new_window')['window']           # `a` is the restarted instance here
            S = t.call(a, 'create', window=wx, title='exit synthetic')['view']
            t.call(a, 'write', window=wx, view=S, text='exit residue?\n')
            t.call(a, 'share', window=wx, view=S)
            t.wait_shared(S)
            ph = a['plugin_host_pid']
            exit_at = now()
            t.stop(a)                       # close_all + sublime 'exit' command
            editor_gone_s = round(now() - exit_at, 2)
            try:
                wait_for(lambda: not t.root.exists(), 15, 0.02, 'root removal after exit')
            except TimeoutError:
                pass
            removed_s = round(now() - exit_at, 2)
            wait_for(lambda: gone(ph), 20, 0.05, 'plugin host exit')
            return not t.root.exists(), {'root_exists_after_graceful_exit': t.root.exists(),
                                         'sandbox_exited_after_s': editor_gone_s,
                                         'root_removed_after_s': removed_s,
                                         'plugin_host_exited_after_s': round(now() - exit_at, 2)}
        t.check(17, 'graceful editor exit removes the publication (extra)', c17)

        # 2b: the two crash cases again at an alternative heartbeat (disposable-profile override)
        alt = os.environ.get('X1_ALT_HEARTBEAT_S', '5')
        if alt and float(alt) != hb['heartbeat_s']:
            hb_alt = heartbeat_params(float(alt))
            t.report['heartbeat_alt'] = hb_alt
            sfx = '@hb{:g}'.format(hb_alt['heartbeat_s'])
            wait_for(lambda: not (t.root / 'publisher.json').exists(), 30, 0.1, 'publish root free before the alt run')
            data_h = t.data_dir('h', heartbeat_s=hb_alt['heartbeat_s'])
            h = t.launch('h', data_h)
            insts.append(h)
            hold = {'inst': h}

            def c18_alt():
                info = wait_for(lambda: load(str(t.root / 'publisher.json')), 10, 0.05, 'alt publisher.json')
                seen, end = [], now() + hb_alt['stale_after_s'] + 1
                while now() < end:
                    beat = load(str(t.root / 'publisher.json'))['heartbeat_at']
                    if not seen or beat != seen[-1]:
                        seen.append(beat)
                    time.sleep(0.02)
                iv = [round(y - x, 3) for x, y in zip(seen, seen[1:])]
                ok = (info['heartbeat_interval_s'] == hb_alt['heartbeat_s'] and info['stale_after_s'] == hb_alt['stale_after_s']
                      and bool(iv) and all(abs(x - hb_alt['heartbeat_s']) < 0.25 for x in iv))
                return ok, {'expected': hb_alt, 'publisher_json': {k: info[k] for k in ('heartbeat_interval_s', 'stale_after_s')},
                            'measured_intervals_s': iv}
            t.check('18' + sfx, 'heartbeat override reaches the publisher (2b)', c18_alt)

            def c11_alt():
                ok, obs = crash_case(t, hold, data_h, 'h', hb_alt, False, insts)
                return ok and obs['reader_timeline']['reader_first_not_live_s'] is not None, obs
            t.check('11' + sfx, 'crash: editor only killed, at the alternative heartbeat (2b)', c11_alt)
            t.check('11b' + sfx, 'crash: editor and plugin hosts together, at the alternative heartbeat (2b)',
                    lambda: crash_case(t, hold, data_h, 'h2', hb_alt, True, insts))
            t.stop(hold['inst'])
    finally:
        for inst in insts:
            try:
                t.stop(inst)
            except Exception as exc:
                t.report['notes'].append('stop {} failed: {}'.format(inst['tag'], exc))
        time.sleep(1.0)
        left = mine(t.root_dir)
        for p in left:          # e.g. an orphaned plugin_host after kill -9: guarded SIGTERM
            try:
                guarded_signal(t.root_dir, p['pid'], signal.SIGTERM)
            except Exception as exc:
                t.report['notes'].append('cleanup signal {} failed: {}'.format(p['pid'], exc))
        time.sleep(0.5)
        reap_orphans({i['popen'].pid for i in insts})
        t.report['cleanup'] = {'disposable_processes_before_cleanup_signal': left,
                               'disposable_processes_after': mine(t.root_dir),
                               'started_processes_still_running': [
                                   {k: (proc(pid) or {}).get(k) for k in ('pid', 'exe')} for pid in started_pids()],
                               'operator_editor_after': operator_editors(),
                               'run_user_sublime_observer_exists': ('skipped: X1_NO_OPERATOR_PROBES=1'
                                                                    if os.environ.get('X1_NO_OPERATOR_PROBES') == '1'
                                                                    else os.path.exists('/run/user/{}/sublime-observer'.format(UID))),
                               'portable_data_packages_after': sorted(os.listdir(str(PORTABLE / 'Data' / 'Packages')))}
        t.report['proc_access'] = proc_access_report()
        t.report['finished_at'] = now()
        t.report['summary'] = {k: v['result'] for k, v in t.report['checks'].items()}
        suffix = ''
        if os.environ.get('X1_ONLY') == 'exit':
            suffix = '.exit-diagnostic' + ('-ab-no-on-exit' if os.environ.get('X1_AB_NO_ON_EXIT') == '1' else '')
        elif os.environ.get('X1_ONLY') == 'exit2b':
            suffix = '.exit-diagnostic'
        if os.environ.get('X1_RUN_LABEL'):
            suffix += '.' + re.sub(r'[^A-Za-z0-9_-]', '', os.environ['X1_RUN_LABEL'])
        out = evidence / (EVIDENCE_PREFIX + suffix + '.' + time.strftime('%Y-%m-%d') + '.json')
        out.write_text(json.dumps(t.report, indent=1, default=str) + '\n')
        print('report', out, flush=True)
        if os.environ.get('X1_KEEP_TRIAL') != '1':
            shutil.rmtree(str(T), ignore_errors=True)
        print('trial root removed:', not T.exists(), flush=True)


if __name__ == '__main__':
    main()
