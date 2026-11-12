#!/usr/bin/env python3
"""Qualify the real read-only plugin using a separate, guarded fixture writer."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import shutil
import signal
import socket
import statistics
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--display', required=True)
    parser.add_argument('--xauthority', required=True)
    parser.add_argument('--portable', type=Path, default=Path('/tmp/nablarva-observer-4215/portable'))
    args = parser.parse_args()
    trial = Path(tempfile.mkdtemp(prefix='nablarva-observer-audit-'))
    portable = trial / 'portable'
    shutil.copytree(args.portable, portable, ignore=shutil.ignore_patterns('Data'))
    packages = portable / 'Data' / 'Packages'
    packages.mkdir(parents=True)
    (packages / 'Observer').symlink_to(ROOT / 'plugin', target_is_directory=True)
    (packages / 'ObserverFixture').symlink_to(ROOT / 'tests' / 'fixture_plugin', target_is_directory=True)
    runtime = trial / 'runtime'
    runtime.mkdir(mode=0o700)
    (trial / 'home').mkdir()
    env = dict(os.environ, HOME=str(trial / 'home'), XDG_RUNTIME_DIR=str(runtime),
               DISPLAY=args.display, XAUTHORITY=args.xauthority, OBSERVER_TRIAL_ROOT=str(trial))
    env.pop('WAYLAND_DISPLAY', None)
    base = [sys.executable, '-I', '-S', '-B', str(ROOT / 'observer.py'), '--runtime', str(runtime)]
    report = {'trial_root': str(trial), 'checks': {}}
    process = None

    def cli(*parts, success=True):
        run = subprocess.run(base + list(parts), text=True, capture_output=True, timeout=35)
        assert (run.returncode == 0) == success, (parts, run.stdout, run.stderr)
        return json.loads(run.stdout if success else run.stderr)

    def fixture(operation, **fields):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as conn:
            conn.settimeout(6)
            conn.connect(str(runtime / 'fixture.sock'))
            conn.sendall((json.dumps(dict(fields, operation=operation)) + '\n').encode())
            data = bytearray()
            while b'\n' not in data:
                chunk = conn.recv(65536)
                if not chunk:
                    raise RuntimeError('fixture closed without response')
                data.extend(chunk)
        result = json.loads(bytes(data).split(b'\n')[0])
        assert result.get('ok'), result
        return result

    def launch():
        nonlocal process
        start = time.monotonic()
        log = open(trial / 'launch.log', 'ab')
        process = subprocess.Popen(['dbus-run-session', '--', str(portable / 'sublime_text'),
                                    '--multiinstance', '--new-window', '--background'],
                                   env=env, stdout=log, stderr=log, start_new_session=True)
        log.close()
        deadline = start + 20
        while time.monotonic() < deadline:
            found = [i for i in cli('instances')['instances'] if i['reachable']]
            if found and (runtime / 'fixture.sock').exists():
                return found[0], round((time.monotonic() - start) * 1000, 2)
            assert process.poll() is None, 'portable editor exited during startup'
            time.sleep(.1)
        raise RuntimeError('portable plugin startup deadline expired')

    def stop():
        nonlocal process
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
            process = None

    try:
        info, cold_ms = launch()
        instance = info['instance']
        report.update({'instance': instance, 'sublime_build': info.get('sublime_build'),
                       'python_version': info.get('python_version'), 'cold_ms': cold_ms})
        w1 = fixture('new_window')['window']
        w2 = fixture('new_window')['window']
        def common(w, v):
            return ['--instance', instance, '--window', str(w), '--view', str(v)]
        def create(w, **kw):
            view = fixture('create', window=w, **kw)['view']
            deadline = time.monotonic() + 5
            while True:
                run = subprocess.run(base + ['read'] + common(w, view), text=True, capture_output=True)
                if run.returncode == 0:
                    return view
                assert time.monotonic() < deadline, run.stderr
                time.sleep(.05)
        a = create(w1, path='A/same.md', disk_text='DISK A\n')
        b = create(w2, path='B/same.md', disk_text='DISK B\n')
        draft = create(w1, title='same.md')
        text = 'Unicode α😀\nsecond line\n' + '\n'.join('line %d' % n for n in range(100))
        fixture('write', window=w1, view=a, text=text)
        fixture('write', window=w1, view=draft, text='unnamed live draft\n')
        fixture('selection', window=w1, view=a, regions=[[0, 0], [8, 10]], viewport=[0, 120])
        fixture('focus', window=w2, view=b)
        before = cli('state', *common(w1, a))
        windows_before = cli('windows', '--instance', instance)
        captured = cli('read', *common(w1, a))
        assert captured['text'] == text, 'fixture live text mismatch'
        assert captured['dirty'], 'edited named view should be dirty'
        assert (trial/'A/same.md').read_text() == 'DISK A\n', 'fixture changed disk content'
        assert cli('read', *common(w1, draft))['text'] == 'unnamed live draft\n'
        assert len(captured['selections']) == 2 and captured['selections'][0]['empty']
        assert cli('read', *common(w1, a), '--lines', '1:1')['text'] == 'Unicode α😀\n'
        assert cli('read', *common(w1, a), '--max-chars', '3')['truncated']
        after = cli('state', *common(w1, a))
        windows_after = cli('windows', '--instance', instance)
        assert windows_before['active_window'] == windows_after['active_window']
        for key in ('selections', 'viewport_position', 'active_view'):
            assert before[key] == after[key], key
        order_before = fixture('order', window=w1)['tabs']
        original_index = next(tab['index'] for tab in order_before if tab['view'] == a)
        destination_index = 0 if original_index != 0 else len(order_before) - 1
        assert destination_index != original_index, 'reorder fixture needs multiple tabs'
        fixture('reorder', window=w1, view=a, index=destination_index)
        order_after = fixture('order', window=w1)['tabs']
        assert [tab['view'] for tab in order_before] != [tab['view'] for tab in order_after], 'tab order did not change'
        assert next(tab['index'] for tab in order_after if tab['view'] == a) == destination_index
        reordered = cli('read', *common(w1, a))
        assert reordered['text'] == text and reordered['view'] == a
        report['reorder_evidence'] = {'before': order_before, 'after': order_after,
                                      'target_view': a, 'destination_index': destination_index,
                                      'explicit_read_view': reordered['view']}
        clone = fixture('clone', window=w1, view=a)['view']
        fixture('selection', window=w1, view=clone, regions=[[20, 20]])
        cloned = cli('state', *common(w1, clone))
        original = cli('state', *common(w1, a))
        assert cloned['buffer'] == original['buffer'] and clone != a
        assert cloned['selections'] != original['selections']
        fixture('write', window=w1, view=a, text=text+'changed\n')
        conflict = cli('read', *common(w1, a), '--expected-revision', str(captured['revision']), success=False)
        assert conflict['error']['code'] == 'revision_conflict'
        fixture('close', window=w1, view=draft)
        assert cli('read', *common(w1, draft), success=False)['error']['code'] == 'invalid_view'
        assert process.poll() is None, 'close unexpectedly killed editor'
        with ThreadPoolExecutor(max_workers=8) as pool:
            captures = list(pool.map(lambda _: cli('state', *common(w1, a)), range(20)))
        assert len({c['request_id'] for c in captures}) == 20
        assert all(c['view'] == a for c in captures)
        large = create(w1, title='large synthetic draft')
        fixture('write', window=w1, view=large, text='x'*220000)
        bounded = cli('read', *common(w1, large))
        assert bounded['truncated'] and len(bounded['text']) == 200000
        fixture('close', window=w1, view=large)
        report['checks'].update(dict.fromkeys(['unnamed', 'unsaved_vs_disk', 'duplicate_titles_windows',
            'focus_selection_scroll_preserved', 'unicode_ranges', 'multiple_selections', 'truncation',
            'reorder', 'clone_selection_identity', 'revision_conflict', 'closed_view', 'concurrent_20',
            'large_buffer_bounded'], 'pass'))

        # A shell-run experiment chooses a destination; the test writer merely opens its result.
        script = trial/'experiment.py'
        script.write_text("import json,sys\ndestination='A'\nr=sys.argv[1]\nprint(json.dumps({'destination':destination,'text':'RUN:'+r+':BEGIN\\noutput\\nRUN:'+r+':END\\n'}))\n")
        runs = []
        for corrected in (False, True):
            if corrected:
                script.write_text(script.read_text().replace("destination='A'", "destination='B'"))
            run_id = cli('new-run', '--instance', instance, '--window', str(w2))['run_id']
            execution = subprocess.run([sys.executable, '-I', '-S', '-B', str(script), run_id],
                                       text=True, capture_output=True, check=True)
            generated = json.loads(execution.stdout)
            target_w, target_v = (w1, a) if generated['destination'] == 'A' else (w2, b)
            fixture('write', window=target_w, view=target_v, text=generated['text'])
            observed = cli('read', *common(target_w, target_v))
            matches = observed['window'] == w2 and observed['path'] == str(trial/'B/same.md')
            assert matches == corrected
            if corrected:
                assert cli('wait', *common(w2, b), '--run-id', run_id)['run_id'] == run_id
            runs.append({'run_id': run_id, 'script_exit': execution.returncode,
                         'observed_window': observed['window'], 'observed_view': observed['view'],
                         'target_matches': matches})
        report['experiment_runs'] = runs
        run_id = cli('new-run', '--instance', instance, '--window', str(w2))['run_id']
        fixture('write', window=w2, view=b, text='RUN:'+run_id+':BEGIN\npartial\n')
        waiting = subprocess.Popen(base+['--timeout','3','wait']+common(w2,b)+['--run-id',run_id],
                                   text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(.25)
        assert waiting.poll() is None, 'partial output was prematurely accepted'
        fixture('write', window=w2, view=b, text='RUN:'+run_id+':BEGIN\ncomplete\nRUN:'+run_id+':END\n')
        stdout, stderr = waiting.communicate(timeout=5)
        assert waiting.returncode == 0, stderr
        assert json.loads(stdout)['run_id'] == run_id
        assert cli('wait', *common(w2,b), '--run-id', run_id, success=False)['error']['code'] == 'request_failed'
        report['checks']['incremental_readiness_and_consumption'] = 'pass'
        incomplete = cli('new-run', '--instance', instance, '--window', str(w2))['run_id']
        fixture('write', window=w2, view=b, text='RUN:'+incomplete+':BEGIN\nincomplete\n')
        started = time.monotonic()
        failure = cli('--timeout', '.3', 'wait', *common(w2,b), '--run-id', incomplete, success=False)
        assert 'deadline expired' in failure['error']['message']
        assert time.monotonic()-started < 1.5
        report['checks']['incomplete_output_deadline'] = 'pass'

        # Copy the original synthetic renderer output; no live _tbv_open/subl dispatch.
        renderer = REPO/'.dev/session/termbrana-M0-markdown-test/implementation/termbrana/transcript.py'
        source = renderer.parent/'fixtures/codex-0.166.synthetic.jsonl'
        if renderer.is_file():
            rendered = subprocess.run([sys.executable,'-I','-S','-B',str(renderer),'render',
                '--vendor','codex','--vendor-version','0.166.0','--project',str(REPO),
                '--source',str(source),'--out',str(trial/'transcript-cache')], text=True,capture_output=True,check=True)
            published = json.loads(rendered.stdout)
            markdown = Path(published['read']).read_text()
            metadata = json.loads(Path(published['map']).read_text())
            tv = create(w2, path='transcript/read.md', disk_text=markdown)
            rows = []
            for record in ('item-user-001','item-user-003'):
                line = metadata['pins'][record]['markdown_line']
                point = sum(len(x) for x in markdown.splitlines(keepends=True)[:line-1])
                fixture('selection', window=w2, view=tv, regions=[[point,point]])
                state = cli('state', *common(w2,tv))
                assert state['selections'][0]['start'] == [line-1,0]
                rows.append({'record':record,'line':line,'view':tv})
            assert rows[0]['line'] != rows[1]['line']
            frozen = cli('read', *common(w2,tv))['text']
            fixture('write', window=w2, view=tv, text=markdown+'\nSYNTHETIC REFRESH MARKER\n')
            refreshed = cli('read', *common(w2,tv))['text']
            assert 'SYNTHETIC REFRESH MARKER' not in frozen and 'SYNTHETIC REFRESH MARKER' in refreshed
            report['transcript_observation'] = {'duplicate_prompt_selections':rows,
                'explicit_fixture_refresh_observed':True,'real_open_navigation_exercised':False,
                'scope':'copied rendered fixture; fixture directly positions caret and changes buffer'}

        samples=[]
        for _ in range(30):
            start=time.monotonic(); cli('state', *common(w2,b)); samples.append((time.monotonic()-start)*1000)
        report['latency']={'samples':30,'median_ms':round(statistics.median(samples),2),
                           'p95_ms':round(sorted(samples)[28],2),
                           'read_response_bytes':len(json.dumps(captured,ensure_ascii=False).encode())}
        old_instance=instance
        stop()
        # Private fixture socket may remain after process-group termination.
        (runtime/'fixture.sock').unlink(missing_ok=True)
        info, restart_ms = launch()
        assert info['instance'] != old_instance
        cli('windows','--instance',old_instance,success=False)
        report['checks']['restart_invalidates_instance']='pass'
        report['restart_ms']=restart_ms
    finally:
        stop()
        report['disposable_process_stopped']=True
        (trial/'report.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
