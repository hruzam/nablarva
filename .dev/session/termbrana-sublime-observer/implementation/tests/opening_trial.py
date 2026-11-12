#!/usr/bin/env python3
"""Exercise the real transcript opener with normal-editor IPC hidden by bwrap."""
import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
ENGINE = REPO / '.dev/session/termbrana-M0-markdown-test/implementation/termbrana'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--display', required=True)
    parser.add_argument('--xauthority', type=Path, required=True)
    parser.add_argument('--portable', type=Path, default=Path('/tmp/nablarva-observer-4215/portable'))
    args = parser.parse_args()
    if not args.display.startswith(':') or not args.display[1:].isdigit():
        parser.error('a local X11 display such as :1 is required')
    x11_socket = Path('/tmp/.X11-unix') / ('X' + args.display[1:])
    if not x11_socket.is_socket():
        parser.error('X11 filesystem socket is unavailable')
    trial = Path(tempfile.mkdtemp(prefix='nablarva-observer-opening-'))
    portable = trial / 'portable'
    shutil.copytree(args.portable, portable, ignore=shutil.ignore_patterns('Data'))
    packages = portable / 'Data/Packages'
    packages.mkdir(parents=True)
    (packages / 'Observer').symlink_to(ROOT / 'plugin', target_is_directory=True)
    runtime = trial / 'runtime'
    runtime.mkdir(mode=0o700)
    isolated_home = trial / 'home'
    isolated_home.mkdir()
    shutil.copyfile(args.xauthority, trial / 'xauthority')
    (trial / 'xauthority').chmod(0o600)
    bin_dir = trial / 'bin'
    bin_dir.mkdir()
    # The actual engine still calls subl -n PATH:LINE. Only command lookup is
    # redirected to the copied binary; no caret or content is set by a fixture.
    launcher = bin_dir / 'subl'
    launcher.write_text('#!/bin/sh\nexec "' + str(portable / 'sublime_text') + '" "$@"\n')
    launcher.chmod(0o700)
    env = dict(os.environ, HOME=str(isolated_home), XDG_RUNTIME_DIR=str(runtime),
               XDG_CONFIG_HOME=str(isolated_home / '.config'),
               XDG_CACHE_HOME=str(isolated_home / '.cache'), DISPLAY=args.display,
               XAUTHORITY=str(trial / 'xauthority'), PATH=str(bin_dir) + ':/usr/bin:/bin')
    env.pop('WAYLAND_DISPLAY', None)
    env.pop('DBUS_SESSION_BUS_ADDRESS', None)
    normal_config = Path.home() / '.config/sublime-text'
    bubble = ['bwrap', '--die-with-parent', '--ro-bind', '/', '/', '--dev', '/dev', '--unshare-net',
              '--tmpfs', '/tmp', '--tmpfs', '/run/user/' + str(os.getuid()),
              '--bind', str(trial), str(trial), '--dir', '/tmp/.X11-unix',
              '--ro-bind', str(x11_socket), str(x11_socket)]
    if normal_config.exists():
        bubble += ['--tmpfs', str(normal_config)]
    bubble += ['--']
    cli_base = [sys.executable, '-I', '-S', '-B', str(ROOT / 'observer.py'), '--runtime', str(runtime)]
    process = None
    report = {'trial_root': str(trial), 'normal_ipc_hidden': False,
              'actual_zsh_opener': True, 'fixture_plugin_installed': False, 'openings': []}

    def cli(*parts):
        result = subprocess.run(cli_base + list(parts), capture_output=True, text=True, timeout=7)
        assert result.returncode == 0, result.stderr
        return json.loads(result.stdout)

    def engine(function, *parts):
        command = ['zsh', '-f', '-c', 'source "$1"; shift; "$@"', 'opening-trial',
                   str(ENGINE / 'base.zsh'), function] + list(map(str, parts))
        result = subprocess.run(bubble + command, env=env, capture_output=True, text=True, timeout=15)
        assert result.returncode == 0, (result.stdout, result.stderr)
        return json.loads(result.stdout)

    def observe_open(instance, cache, record, expected_line):
        before = {w['id'] for w in cli('windows', '--instance', instance)['windows']}
        result = engine('_tbv_open', '--cache', cache, '--record', record)
        deadline = time.monotonic() + 8
        while time.monotonic() < deadline:
            windows = cli('windows', '--instance', instance)['windows']
            for window in windows:
                if window['id'] in before:
                    continue
                tabs = cli('tabs', '--instance', instance, '--window', str(window['id']))['views']
                for tab in tabs:
                    if tab['path'] != result['opened'].rsplit(':', 1)[0] or tab['loading']:
                        continue
                    captured = cli('read', '--instance', instance, '--window', str(window['id']),
                                   '--view', str(tab['view']))
                    caret = captured['selections'][0]
                    if caret['empty'] and caret['start'] == [expected_line - 1, 0]:
                        heading = captured['text'].splitlines()[expected_line - 1]
                        assert record in heading, heading
                        report['openings'].append({'record': record, 'window': window['id'],
                            'view': tab['view'], 'path': tab['path'], 'line': expected_line,
                            'heading': heading, 'new_window': True})
                        return captured
            time.sleep(.1)
        raise AssertionError('actual opener did not produce expected new view/caret: ' + repr(result))

    try:
        # Prove the normal IPC directories are hidden before launching any GUI.
        check = subprocess.run(bubble + ['python3', '-I', '-S', '-B', '-c',
            'from pathlib import Path; import os; '
            'assert not list(Path("/run/user/"+str(os.getuid())).iterdir()); '
            'assert set(p.name for p in Path("/tmp").iterdir()) == '
            'set([".X11-unix", "' + trial.name + '"]); '
            'print("normal IPC hidden")'], env=env, capture_output=True, text=True)
        assert check.returncode == 0, check.stderr
        report['normal_ipc_hidden'] = True
        log = open(trial / 'launch.log', 'ab')
        process = subprocess.Popen(bubble + ['dbus-run-session', '--', str(portable / 'sublime_text'),
                                   '--detached', '--new-window', '--background'], env=env,
                                   stdout=log, stderr=log, start_new_session=True)
        log.close()
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            found = [item for item in cli('instances')['instances'] if item['reachable']]
            if found:
                break
            assert process.poll() is None, 'disposable editor exited during startup'
            time.sleep(.1)
        else:
            raise AssertionError('disposable observer startup timed out')
        info = found[0]
        instance = info['instance']
        report.update({'instance': instance, 'sublime_build': info.get('sublime_build'),
                       'python_version': info.get('python_version')})
        cache = trial / 'cache'
        rendered = engine('_tbv_render', '--vendor', 'codex', '--vendor-version', '0.166.0',
            '--project', trial, '--source', ENGINE / 'fixtures/codex-0.166.synthetic.jsonl',
            '--out', cache)
        assert rendered['records'] == 4, rendered
        first = observe_open(instance, cache, 'item-user-003', 25)
        second = observe_open(instance, cache, 'item-user-001', 11)
        assert first['path'] == second['path'] and first['view'] != second['view']
        assert process.poll() is None, 'editor exited after actual opens'
        report['passed'] = True
    finally:
        if process is not None:
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                process.wait(timeout=6)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=3)
        report['disposable_process_stopped'] = process is None or process.poll() is not None
        (trial / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
