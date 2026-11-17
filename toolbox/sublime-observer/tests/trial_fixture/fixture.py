"""TEST-ONLY fixture for the X1 disposable-profile trial. Never install in a real profile.

Activates only when X1_TRIAL_ROOT names a /tmp/sublime-observer-x1-trial-* directory AND
sublime.packages_path() is the disposable portable profile. Creates and drives synthetic
views only (it tracks the views it created and refuses any other; the one exception is the
step 2b `inventory` op, which lists window/view METADATA -- ids, names, paths, dirty and
scratch flags, never text -- of this disposable editor, e.g. views restored after a crash,
so an ignored exit can be explained). The command channel
is files (no socket): <root>/fixture/<plugin_host pid>/in/*.json -> out/*.json.
Pattern adapted from the X0 fixture (tests/fixture_plugin/fixture.py), socket removed.
"""
import json
import os
import statistics
import sys
import time

import sublime
import sublime_plugin

_EXPECTED_PACKAGES = '/tmp/nablarva-observer-4215/portable/Data/Packages'
_ROOT = None
_CHAN = None
_VIEWS = {}
_WINDOWS = {}
_ACTIVE = False
_BURST = {}


class SublimeObserverTrialTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, text, mode='replace'):
        if self.view.id() not in _VIEWS:
            raise ValueError('not a fixture view')
        if mode == 'replace':
            self.view.replace(edit, sublime.Region(0, self.view.size()), text)
        else:
            self.view.insert(edit, self.view.size(), text)


_EVENTS = {}


class SublimeObserverTrialEvents(sublime_plugin.EventListener):
    """Diagnostic: counts editor events for fixture views only."""

    def _count(self, view, name):
        if view.id() in _VIEWS:
            counts = _EVENTS.setdefault(view.id(), {})
            counts[name] = counts.get(name, 0) + 1

    def on_selection_modified(self, view):
        self._count(view, 'on_selection_modified')

    def on_modified(self, view):
        self._count(view, 'on_modified')


def _publisher():
    return sys.modules.get('SublimeObserver.publisher')


def _view(q):
    view = _VIEWS[q['view']]
    if not view.is_valid():
        raise ValueError('fixture view no longer valid')
    return view


def _snapshot():
    active = sublime.active_window()
    out = {'active_window': active.id() if active else None, 'windows': {}, 'views': {}}
    for wid, window in _WINDOWS.items():
        av = window.active_view()
        out['windows'][str(wid)] = {'active_view': av.id() if av else None}
    for vid, view in _VIEWS.items():
        if not view.is_valid():
            continue
        out['views'][str(vid)] = {
            'window': view.window().id() if view.window() else None,
            'sel': [[r.a, r.b] for r in view.sel()],
            'viewport_position': list(view.viewport_position()),
            'visible_region': [view.visible_region().begin(), view.visible_region().end()],
            'change_count': view.change_count(), 'status': view.get_status('sublime_observer')}
    return out


def _burst_step(vid, deadline, interval_ms):
    view = _VIEWS.get(vid)
    if not _ACTIVE or view is None or not view.is_valid():
        return
    now = time.time()
    if now >= deadline:
        _BURST[vid]['done'] = True
        return
    view.run_command('sublime_observer_trial_text', {'text': 'k', 'mode': 'append'})
    _BURST[vid]['edits'].append([time.time(), view.change_count()])
    sublime.set_timeout(lambda: _burst_step(vid, deadline, interval_ms), interval_ms)


def _dispatch(q):
    op = q['op']
    if op == 'hello':
        return {'pid': os.getpid(), 'ppid': os.getppid(), 'build': sublime.version(),
                'python': sys.version.split()[0], 'packages_path': sublime.packages_path(),
                'proc_visible': os.path.isdir('/proc/1')}
    if op == 'new_window':
        sublime.run_command('new_window')
        window = sublime.active_window()
        _WINDOWS[window.id()] = window
        return {'window': window.id()}
    if op == 'publisher':
        mod = _publisher()
        rt = getattr(mod, '_RT', None) if mod else None
        if rt is None:
            return {'loaded': mod is not None, 'runtime': None}
        return {'loaded': True, 'runtime': {
            'epoch': rt.epoch, 'publishing': rt.store is not None, 'refusal': rt.refusal,
            'shared_views': sorted(rt.shares), 'root': rt.store.root if rt.store else None}}
    if op == 'snapshot':
        return _snapshot()
    if op == 'events':
        return {'events': {str(k): v for k, v in _EVENTS.items()}}
    if op == 'close_all':      # fixture views only; scratch so exit never prompts
        for view in list(_VIEWS.values()):
            if view.is_valid():
                view.set_scratch(True)
                view.close()
        return {}
    if op == 'exit':
        sublime.set_timeout(lambda: sublime.run_command('exit'), 50)
        return {}
    if op == 'inventory':      # step 2b exit diagnostic: METADATA ONLY (never text) of every
        out = []               # window/view in this disposable, synthetic-only editor
        for window in sublime.windows():
            views = []
            for view in window.views():
                views.append({'view': view.id(), 'buffer': view.buffer_id(), 'fixture': view.id() in _VIEWS,
                              'file_name': view.file_name(), 'name': view.name(), 'dirty': view.is_dirty(),
                              'scratch': view.is_scratch(), 'loading': view.is_loading(), 'size': view.size()})
            out.append({'window': window.id(), 'fixture': window.id() in _WINDOWS, 'views': views,
                        'sheets': len(window.sheets())})
        return {'windows': out, 't': time.time()}
    window = _WINDOWS[q['window']]
    if op == 'create':
        path = q.get('path')
        if path:
            path = os.path.realpath(path)
            if not path.startswith(_ROOT + os.sep):
                raise ValueError('path escapes the trial root')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as handle:
                    handle.write(q.get('disk_text', 'SYNTHETIC DISK\n'))
            view = window.open_file(path)
        else:
            view = window.new_file()
            view.set_name(q.get('title', 'synthetic draft'))
            view.set_scratch(True)
        _VIEWS[view.id()] = view
        return {'view': view.id(), 'buffer': view.buffer_id(), 'path': view.file_name(),
                'loading': view.is_loading()}
    view = _view(q)
    if op == 'write':
        view.run_command('sublime_observer_trial_text', {'text': q['text'], 'mode': q.get('mode', 'replace')})
        return {'t_edit': time.time(), 'revision': view.change_count(), 'size': view.size()}
    if op == 'selection':
        view.sel().clear()
        for a, b in q['regions']:
            view.sel().add(sublime.Region(a, b))
        return {'sel': [[r.a, r.b] for r in view.sel()]}
    if op == 'scroll':
        view.set_viewport_position(tuple(q['viewport']), False)
        return {'viewport_position': list(view.viewport_position())}
    if op == 'focus':
        window.focus_view(view)
        return {}
    if op == 'share':          # the operator's act: focus the view, run the palette command
        window.focus_view(view)
        window.run_command('sublime_observer_toggle_share')
        rt = getattr(_publisher(), '_RT', None)
        return {'shared': bool(rt and view.id() in rt.shares), 'status': view.get_status('sublime_observer')}
    if op == 'open_same':      # same file in another window -> second view
        other = view.file_name()
        clone = window.open_file(other)
        _VIEWS[clone.id()] = clone
        return {'view': clone.id(), 'buffer': clone.buffer_id()}
    if op == 'close':
        view.set_scratch(True)
        view.close()
        return {}
    if op == 'probe_text':     # what the API says about this synthetic view's characters
        size = view.size()
        text = view.substr(sublime.Region(0, size))
        mod = _publisher()
        cap = q.get('cap', 2)
        cut = mod.capture_view(view, cap, lambda r: True)['text'] if mod else None
        return {'size': size, 'len_substr': len(text), 'codepoints_gt_ffff': sum(1 for c in text if ord(c) > 0xFFFF),
                'utf16_units': len(text.encode('utf-16-le')) // 2, 'capped_text': cut,
                'capped_len': len(cut) if cut is not None else None, 'cap': cap,
                'rowcol_end': list(view.rowcol(size))}
    if op == 'time_capture':   # main-thread cost of the real capture function on this view
        mod = _publisher()
        samples = []
        for _ in range(q.get('n', 30)):
            start = time.perf_counter()
            mod.capture_view(view, 200000, lambda r: True)
            samples.append((time.perf_counter() - start) * 1000)
        state_only = []
        for _ in range(q.get('n', 30)):
            start = time.perf_counter()
            mod.capture_view(view, 200000, lambda r: False)
            state_only.append((time.perf_counter() - start) * 1000)
        def summary(xs):
            xs = sorted(xs)
            return {'n': len(xs), 'median_ms': round(statistics.median(xs), 3),
                    'p95_ms': round(xs[int(0.95 * (len(xs) - 1))], 3), 'max_ms': round(xs[-1], 3)}
        return {'with_text': summary(samples), 'state_only': summary(state_only), 'size': view.size()}
    if op == 'burst':
        deadline = time.time() + q['duration_ms'] / 1000.0
        _BURST[view.id()] = {'edits': [], 'done': False}
        sublime.set_timeout(lambda: _burst_step(view.id(), deadline, q['interval_ms']), 0)
        return {'deadline': deadline}
    if op == 'burst_result':
        return _BURST.get(view.id(), {})
    raise ValueError('unsupported fixture op {}'.format(op))


def _write_json(directory, name, obj):
    tmp = os.path.join(directory, '.' + name + '.tmp')
    with open(tmp, 'w', encoding='utf-8') as handle:
        json.dump(obj, handle)
    os.replace(tmp, os.path.join(directory, name))


def _poll():
    if not _ACTIVE:
        return
    inbox = os.path.join(_CHAN, 'in')
    try:
        # skip the harness's '.NNNNNN.json' temp names: consuming one before its rename raced
        # the harness (step 2b, run 2: FileNotFoundError on os.replace in check 14)
        names = sorted(n for n in os.listdir(inbox) if n.endswith('.json') and not n.startswith('.'))
    except OSError:
        names = []
    for name in names:
        path = os.path.join(inbox, name)
        try:
            with open(path, encoding='utf-8') as handle:
                q = json.load(handle)
            os.unlink(path)
            result = dict(_dispatch(q), ok=True)
        except Exception as exc:
            result = {'ok': False, 'error': '{}: {}'.format(type(exc).__name__, exc)}
        _write_json(os.path.join(_CHAN, 'out'), name, result)
    sublime.set_timeout(_poll, 10)


def plugin_loaded():
    global _ROOT, _CHAN, _ACTIVE
    root = os.environ.get('X1_TRIAL_ROOT', '')
    if not root.startswith('/tmp/sublime-observer-x1-trial-'):
        return
    if os.path.realpath(sublime.packages_path()) != _EXPECTED_PACKAGES:
        return
    _ROOT = os.path.realpath(root)
    _CHAN = os.path.join(_ROOT, 'fixture', str(os.getpid()))
    for sub in ('in', 'out'):
        os.makedirs(os.path.join(_CHAN, sub), exist_ok=True)
    _ACTIVE = True
    _write_json(os.path.join(_ROOT, 'fixture'), 'hello-{}.json'.format(os.getpid()),
                {'pid': os.getpid(), 'ppid': os.getppid(), 'chan': _CHAN})
    sublime.set_timeout(_poll, 10)


def plugin_unloaded():
    global _ACTIVE
    _ACTIVE = False
