"""Fake `sublime` / `sublime_plugin` modules, a manual clock, and a synchronous writer.

Pattern copied from the X0 bed (tests/test_observer.py): fake modules are put in
sys.modules before the plugin is imported. Nothing here talks to a real editor.
"""
import importlib
import os
import sys
import types

# Source root: <root>/SublimeObserver (the installed payload) and <root>/tests (this folder).
IMPL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True     # importing the package must never leave __pycache__ in the payload


class Region(object):
    def __init__(self, a, b=None):
        self.a, self.b = a, (a if b is None else b)

    def begin(self):
        return min(self.a, self.b)

    def end(self):
        return max(self.a, self.b)

    def empty(self):
        return self.a == self.b


class Clock(object):
    """Monotonic test clock with a timer queue (sublime.set_timeout stand-in)."""

    def __init__(self, start=1000.0):
        self.now = start
        self.timers = []
        self._seq = 0

    def __call__(self):
        return self.now

    def add_timer(self, callback, ms):
        self._seq += 1
        self.timers.append((self.now + ms / 1000.0, self._seq, callback))

    def advance(self, seconds):
        """Move time forward, running every timer that falls due, in order."""
        target = self.now + seconds
        while True:
            due = sorted(t for t in self.timers if t[0] <= target + 1e-9)
            if not due:
                break
            item = due[0]
            self.timers.remove(item)
            self.now = max(self.now, item[0])
            item[2]()
        self.now = target


class Window(object):
    def __init__(self, ident):
        self.ident = ident
        self.active = None

    def id(self):
        return self.ident

    def active_view(self):
        return self.active


_READS = ('id', 'buffer_id', 'file_name', 'name', 'is_dirty', 'is_loading', 'change_count', 'size',
          'substr', 'sel', 'rowcol', 'visible_region', 'viewport_position', 'viewport_extent',
          'encoding', 'window', 'is_valid', 'element')
_STATUS = ('set_status', 'erase_status')


class View(object):
    """Synthetic view. Records every method call; anything that is neither a known read
    nor a status-bar call is recorded in `forbidden` (e.g. sel().add, show, run_command)."""

    def __init__(self, ident, text='', path=None, window=None, buffer_id=None, rev=1):
        d = self.__dict__
        d['ident'], d['text'], d['path'], d['win'] = ident, text, path, window
        d['buf'] = ident + 1000 if buffer_id is None else buffer_id
        d['rev'], d['loading'], d['valid'], d['dirty'] = rev, False, True, True
        d['selection'] = [Region(0, 0)]
        d['viewport'] = (0.0, 0.0)
        d['visible'] = (0, min(len(text), 500))
        d['calls'], d['forbidden'], d['status'] = [], [], {}
        d['on_substr'] = None

    def __getattr__(self, name):
        self.__dict__['forbidden'].append(name)
        return lambda *a, **k: None

    def _log(self, name):
        self.calls.append(name)

    def edit(self, text):
        self.__dict__['text'] = text
        self.__dict__['rev'] += 1

    def id(self):
        return self.ident

    def buffer_id(self):
        self._log('buffer_id'); return self.buf

    def file_name(self):
        self._log('file_name'); return self.path

    def name(self):
        self._log('name'); return '' if self.path else 'untitled synthetic'

    def is_dirty(self):
        self._log('is_dirty'); return self.dirty

    def is_loading(self):
        self._log('is_loading'); return self.loading

    def change_count(self):
        self._log('change_count'); return self.rev

    def size(self):
        self._log('size'); return len(self.text)

    def substr(self, region):
        self._log('substr')
        if self.on_substr:
            self.on_substr()
        return self.text[region.begin():region.end()]

    def sel(self):
        self._log('sel'); return list(self.selection)

    def rowcol(self, point):
        pre = self.text[:point]
        return (pre.count('\n'), len(pre.rsplit('\n', 1)[-1]))

    def visible_region(self):
        self._log('visible_region'); return Region(*self.visible)

    def viewport_position(self):
        self._log('viewport_position'); return self.viewport

    def viewport_extent(self):
        return (800.0, 600.0)

    def encoding(self):
        return 'UTF-8'

    def window(self):
        return self.win

    def is_valid(self):
        return self.valid

    def element(self):
        return None

    def set_status(self, key, value):
        self.status[key] = value

    def erase_status(self, key):
        self.status.pop(key, None)


class TrapView(View):
    """An unshared view: only id() is permitted; any other access is recorded."""

    def __getattribute__(self, name):
        if name in _READS[1:] or name in _STATUS or name in ('substr', 'sel'):
            object.__getattribute__(self, '__dict__')['forbidden'].append(name)
        return object.__getattribute__(self, name)


class SyncWriter(object):
    """Runs submitted calls immediately (tests drive ordering deterministically)."""

    def __init__(self, on_error):
        self.on_error = on_error
        self.closed = False

    def submit(self, fn, *args):
        if self.closed:
            return
        try:
            fn(*args)
        except Exception as exc:
            self.on_error(exc)

    def close(self, timeout):
        self.closed = True
        return True


class QueueWriter(SyncWriter):
    """Holds submitted calls until drain() (tests interleave main-thread acts with queued work)."""

    def __init__(self, on_error):
        SyncWriter.__init__(self, on_error)
        self.queue = []

    def submit(self, fn, *args):
        if not self.closed:
            self.queue.append((fn, args))

    def drain(self):
        while self.queue and not self.closed:
            fn, args = self.queue.pop(0)
            SyncWriter.submit(self, fn, *args)

    def close(self, timeout):
        self.queue = []
        return SyncWriter.close(self, timeout)


class Settings(object):
    def __init__(self, values):
        self.values = values

    def get(self, key, default=None):
        return self.values.get(key, default)


def install(clock, settings_values=None):
    """Install fake modules and (re)import the package. Returns (publisher, fake_sublime)."""
    sub = types.ModuleType('sublime')
    sub.Region = Region
    sub.messages = []
    sub.set_timeout = clock.add_timer
    sub.set_timeout_async = clock.add_timer
    sub.status_message = sub.messages.append
    sub.version = lambda: '4215'
    sub.settings_values = settings_values or {}
    sub.load_settings = lambda name: Settings(sub.settings_values)
    plug = types.ModuleType('sublime_plugin')
    plug.EventListener = type('EventListener', (object,), {})
    plug.WindowCommand = type('WindowCommand', (object,), {'__init__': lambda self, w: setattr(self, 'window', w)})
    sys.modules['sublime'] = sub
    sys.modules['sublime_plugin'] = plug
    if IMPL not in sys.path:
        sys.path.insert(0, IMPL)
    for name in ('SublimeObserver.publisher', 'SublimeObserver.contract'):
        sys.modules.pop(name, None)
    publisher = importlib.import_module('SublimeObserver.publisher')
    return publisher, sub


def load_contract():
    if IMPL not in sys.path:
        sys.path.insert(0, IMPL)
    return importlib.import_module('SublimeObserver.contract')
