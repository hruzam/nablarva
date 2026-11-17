"""SublimeObserver -- publish operator-shared Sublime views as plain files.

Observation only: no socket, no notification of any other process, no command
that changes a view, focus, selection or scroll, and no listing or reading of a
view the operator has not shared. Sharing is a live act (one toggle command);
shares never survive a plugin reload or editor restart.

Threading: the capture (API reads of one shared view) runs on the plugin host's
main thread inside sublime.set_timeout callbacks, guarded by change_count before
and after. All file I/O runs on one dedicated writer thread (contract.Writer).
"""
import itertools
import os
import sys
import time
import uuid

import sublime
import sublime_plugin

from . import contract

STATUS_KEY = 'sublime_observer'
STATUS_TEXT = 'Observer: SHARED'
SETTINGS_FILE = 'SublimeObserver.sublime-settings'
_PREFIX = 'sublime-observer: '
_MAX_ERROR_LINES = 5

_RT = None          # the live _Runtime for this plugin load


def _log(message):
    print(_PREFIX + message)


def _number(value, default, minimum):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < minimum:
        return default
    return value


def read_settings(get):
    """Validated settings from a get(key, default) callable."""
    d = contract.DEFAULTS
    return {
        'root': get('root', d['root']),
        'cap_chars': int(_number(get('cap_chars', d['cap_chars']), d['cap_chars'], 1)),
        'debounce_s': _number(get('debounce_ms', d['debounce_ms']), d['debounce_ms'], 0) / 1000.0,
        'max_delay_s': _number(get('max_delay_ms', d['max_delay_ms']), d['max_delay_ms'], 0) / 1000.0,
        'poll_s': _number(get('viewport_poll_ms', d['viewport_poll_ms']), d['viewport_poll_ms'], 50) / 1000.0,
        'heartbeat_s': float(_number(get('heartbeat_s', d['heartbeat_s']), d['heartbeat_s'], 0.5)),
    }


def capture_view(view, cap, need_text):
    """Read one shared view. Returns a capture dict, or None when the buffer changed
    during the capture (caller retries). need_text(revision) -> bool decides whether
    the text must be read (caret/scroll-only changes skip the substr)."""
    revision = view.change_count()
    loading = view.is_loading()
    window = view.window()
    path = view.file_name()
    size = view.size()
    text = None
    truncated = size > cap
    if not loading and need_text(revision):
        text = view.substr(sublime.Region(0, min(size, cap)))
    selection = view.sel()
    count = len(selection)
    selections = []
    for region in itertools.islice(selection, contract.MAX_SELECTIONS):
        start, end = view.rowcol(region.begin()), view.rowcol(region.end())
        selections.append({'a': region.a, 'b': region.b, 'empty': region.empty(),
                           'start': [start[0], start[1]], 'end': [end[0], end[1]]})
    visible = view.visible_region()
    position = view.viewport_position()
    extent = view.viewport_extent()
    title = view.name() or (os.path.basename(path) if path else None)
    capture = {
        'window': window.id() if window is not None else None,
        'view': view.id(), 'buffer': view.buffer_id(), 'path': path, 'title': title,
        'dirty': view.is_dirty(), 'loading': loading, 'revision': revision,
        'captured_at': time.time(), 'encoding': view.encoding(), 'size_chars': size,
        'text': text, 'truncated': truncated,
        'selection_count': count, 'selections_truncated': count > contract.MAX_SELECTIONS,
        'selections': selections,
        'visible_region': {'begin': visible.begin(), 'end': visible.end()},
        'viewport_position': [position[0], position[1]],
        'viewport_extent': [extent[0], extent[1]],
        'error': None,
    }
    if view.change_count() != revision:
        return None
    return capture


def _poll_key(view):
    """What the poll compares for a shared view: viewport, visible region, path and the
    selection. Selection is included because API-driven selection changes (other plugins,
    goto) fire no on_selection_modified -- observed in the 4215 disposable trial."""
    visible = view.visible_region()
    selection = view.sel()
    regions = tuple((r.a, r.b) for r in itertools.islice(selection, contract.MAX_SELECTIONS))
    return (tuple(view.viewport_position()), visible.begin(), visible.end(), view.file_name(),
            len(selection), regions)


def _capture_key(capture):
    return (tuple(capture['viewport_position']), capture['visible_region']['begin'],
            capture['visible_region']['end'], capture['path'], capture['selection_count'],
            tuple((s['a'], s['b']) for s in capture['selections']))


class _Share(object):
    def __init__(self, view):
        self.view = view
        self.share_id = uuid.uuid4().hex
        self.viewport = None


class _Runtime(object):
    """One plugin load. Timer callbacks check `active`, so a reload stops old timers."""

    def __init__(self, settings, clock=time.monotonic, wall=time.time, writer_factory=contract.Writer,
                 environ=None, uid=None, pid=None):
        self.settings = settings
        self.clock = clock
        self.wall = wall
        self.environ = os.environ if environ is None else environ
        self.uid = os.getuid() if uid is None else uid
        self.pid = os.getpid() if pid is None else pid
        self.epoch = uuid.uuid4().hex
        self.active = True
        self.store = None
        self.refusal = None
        self.shares = {}            # view id -> _Share
        self.debouncer = contract.Debouncer(settings['debounce_s'], settings['max_delay_s'])
        self.poll_armed = False
        self.errors = 0
        self.writer = writer_factory(self._write_error)

    # lifecycle
    def start(self):
        try:
            root = contract.resolve_root(self.settings['root'], self.environ, self.uid)
            store = contract.Store(root, self.epoch, self.pid, self.uid,
                                   {'sublime_build': sublime.version(),
                                    'plugin_python': sys.version.split()[0]},
                                   self.settings['cap_chars'], self.settings['heartbeat_s'], clock=self.wall)
            ok, message = store.start()
        except (contract.ContractError, OSError) as exc:
            self.refusal = str(exc)
            _log('not publishing: {}'.format(exc))
            return False
        if not ok:
            self.refusal = message
            _log(message)
            return False
        if message:
            _log(message)
        self.store = store
        self._arm_heartbeat()
        return True

    def stop(self):
        self.active = False
        for share in list(self.shares.values()):
            try:
                share.view.erase_status(STATUS_KEY)
            except Exception:
                pass
        self.shares = {}
        self.writer.close(2.0)
        if self.store is not None:
            try:
                self.store.shutdown()
            except Exception as exc:
                _log('cleanup failed: {}'.format(exc))

    # sharing
    def toggle(self, view):
        if not self.active:
            return
        if view is None:
            sublime.status_message('Sublime Observer: no view to share')
            return
        if view.id() in self.shares:
            self.unshare(view.id(), 'unshared')
            return
        if self.store is None:
            sublime.status_message('Sublime Observer: not publishing ({})'.format(self.refusal))
            return
        element = getattr(view, 'element', None)
        if element is not None and element() is not None:
            sublime.status_message('Sublime Observer: panels and widgets cannot be shared')
            return
        reason = contract.sealed_reason(view.file_name())
        if reason:
            sublime.status_message('Sublime Observer: refused to share, {}'.format(reason))
            return
        share = _Share(view)
        self.shares[view.id()] = share
        view.set_status(STATUS_KEY, STATUS_TEXT)
        sublime.status_message('Sublime Observer: shared (share {})'.format(share.share_id[:8]))
        self.publish(view.id())
        self._arm_poll()

    def unshare(self, view_id, why):
        share = self.shares.pop(view_id, None)
        if share is None:
            return
        self.debouncer.cancel(view_id)
        try:
            share.view.erase_status(STATUS_KEY)
        except Exception:
            pass
        if why != 'closed':
            sublime.status_message('Sublime Observer: {}'.format(why))
        if self.store is not None:
            self.writer.submit(self.store.remove_share, share.share_id)

    # events (only view.id() is ever read from an unshared view)
    def touched(self, view):
        if not self.active or view.id() not in self.shares:
            return
        view_id = view.id()
        delay = self.debouncer.touch(view_id, self.clock())
        if delay is not None:
            self._arm(view_id, delay)

    def loaded(self, view):
        if self.active and view.id() in self.shares:
            self.debouncer.cancel(view.id())
            self.publish(view.id())

    def closed(self, view):
        if self.active and view.id() in self.shares:
            self.unshare(view.id(), 'closed')

    # publication
    def publish(self, view_id):
        share = self.shares.get(view_id)
        if share is None or self.store is None:
            return
        view = share.view
        is_valid = getattr(view, 'is_valid', None)
        if is_valid is not None and not is_valid():
            self.unshare(view_id, 'closed')
            return
        reason = contract.sealed_reason(view.file_name())
        if reason:
            self.unshare(view_id, 'unshared, {}'.format(reason))
            return
        store, share_id = self.store, share.share_id
        try:
            capture = capture_view(view, self.settings['cap_chars'],
                                   lambda revision: store.text_rev.get(share_id) != revision)
        except Exception as exc:
            capture = {'view': view_id, 'error': {'code': 'capture_failed', 'message': str(exc)}}
        if capture is None:                 # changed during capture: retry after the debounce
            self.touched(view)
            return
        if capture.get('error') is None:
            share.viewport = _capture_key(capture)
        self.writer.submit(store.publish, share_id, capture)

    # timers
    def _arm(self, view_id, delay):
        sublime.set_timeout(lambda: self._fire(view_id), int(round(delay * 1000)))

    def _fire(self, view_id):
        if not self.active:
            return
        if view_id not in self.shares:
            self.debouncer.cancel(view_id)
            return
        delay = self.debouncer.fire(view_id, self.clock())
        if delay is None:
            self.publish(view_id)
        else:
            self._arm(view_id, delay)

    def _arm_poll(self):
        if self.poll_armed or not self.shares:
            return
        self.poll_armed = True
        sublime.set_timeout(self._poll, int(self.settings['poll_s'] * 1000))

    def _poll(self):
        self.poll_armed = False
        if not self.active:
            return
        for view_id, share in list(self.shares.items()):
            view = share.view
            is_valid = getattr(view, 'is_valid', None)
            if is_valid is not None and not is_valid():
                self.unshare(view_id, 'closed')
                continue
            try:
                key = _poll_key(view)
            except Exception:
                continue
            if key != share.viewport:
                self.touched(view)
        self._arm_poll()

    def _arm_heartbeat(self):
        sublime.set_timeout(self._heartbeat, int(self.settings['heartbeat_s'] * 1000))

    def _heartbeat(self):
        if not self.active or self.store is None:
            return
        self.writer.submit(self.store.heartbeat)
        self._arm_heartbeat()

    def _write_error(self, exc):
        self.errors += 1
        if self.errors <= _MAX_ERROR_LINES:
            _log('write failed: {}{}'.format(exc, ' (further errors suppressed)' if self.errors == _MAX_ERROR_LINES else ''))


# --- Sublime entry points ---------------------------------------------------

def plugin_loaded():
    global _RT
    if _RT is not None:
        _RT.stop()
    settings = sublime.load_settings(SETTINGS_FILE)
    _RT = _Runtime(read_settings(settings.get))
    _RT.start()


def plugin_unloaded():
    global _RT
    runtime, _RT = _RT, None
    if runtime is not None:
        runtime.stop()


class SublimeObserverToggleShareCommand(sublime_plugin.WindowCommand):
    """Share or unshare the active view of this window. Never changes the view."""

    def run(self):
        if _RT is None:
            sublime.status_message('Sublime Observer: not loaded')
            return
        _RT.toggle(self.window.active_view())


class SublimeObserverListener(sublime_plugin.EventListener):

    def on_modified(self, view):
        if _RT is not None:
            _RT.touched(view)

    def on_selection_modified(self, view):
        if _RT is not None:
            _RT.touched(view)

    def on_reload(self, view):
        if _RT is not None:
            _RT.touched(view)

    def on_revert(self, view):
        if _RT is not None:
            _RT.touched(view)

    def on_post_save(self, view):
        if _RT is not None:
            _RT.touched(view)

    def on_load(self, view):
        if _RT is not None:
            _RT.loaded(view)

    def on_close(self, view):
        if _RT is not None:
            _RT.closed(view)

    def on_exit(self):
        """Graceful editor exit: Sublime does not call plugin_unloaded here (observed in
        the 4215 disposable trial), so run the same cleanup."""
        plugin_unloaded()
