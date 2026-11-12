"""Read-only, explicitly addressed Sublime observation for experimental use."""
import concurrent.futures
import json
import os
import socket
import sys
import threading
import time
import uuid

import sublime
import sublime_plugin

_INSTANCE = uuid.uuid4().hex
_SERVER = None
_THREAD = None
_POOL = None
_STOP = threading.Event()
_SLOTS = threading.BoundedSemaphore(32)
_MAX_REQUEST = 65536
_MAX_CHARS = 200000


def _registry():
    base = os.environ.get('XDG_RUNTIME_DIR')
    if not base or not os.path.isabs(base):
        raise RuntimeError('XDG_RUNTIME_DIR must identify a private runtime directory')
    st = os.stat(base)
    if st.st_uid != os.getuid() or st.st_mode & 0o077:
        raise RuntimeError('XDG_RUNTIME_DIR must be owned by this user and private')
    path = os.path.join(base, 'sublime-observer')
    os.makedirs(path, mode=0o700, exist_ok=True)
    st = os.lstat(path)
    if not os.path.isdir(path) or os.path.islink(path) or st.st_uid != os.getuid() or st.st_mode & 0o077:
        raise RuntimeError('observer registry is not a private directory')
    return path


def _error(code, message):
    return {'ok': False, 'error': {'code': code, 'message': message}}


def _capture(req):
    operation = req.get('operation')
    if req.get('instance') != _INSTANCE:
        return _error('expired_instance', 'instance does not match the running plugin')
    if operation == 'windows':
        active_window = sublime.active_window()
        return {'ok': True, 'instance': _INSTANCE,
                'active_window': active_window.id() if active_window else None, 'windows': [
            {'id': w.id(), 'folders': w.folders(), 'active_view': w.active_view().id() if w.active_view() else None}
            for w in sublime.windows()]}
    window_id = req.get('window')
    window = next((w for w in sublime.windows() if w.id() == window_id), None)
    if window is None:
        return _error('invalid_window', 'window not found')
    if operation == 'tabs':
        views = [{'view': v.id(), 'buffer': v.buffer_id(), 'path': v.file_name(), 'title': v.name(),
                  'dirty': v.is_dirty(), 'loading': v.is_loading(), 'revision': v.change_count()} for v in window.views()]
        unsupported = []
        for sheet in window.sheets():
            if sheet.view() is None:
                unsupported.append({'sheet': sheet.id(), 'type': type(sheet).__name__})
        return {'ok': True, 'instance': _INSTANCE, 'window': window_id, 'views': views, 'unsupported_sheets': unsupported}
    if operation not in ('read', 'state', 'selection'):
        return _error('invalid_operation', 'only windows, tabs, read, state and selection are supported')
    view_id = req.get('view')
    view = next((v for v in window.views() if v.id() == view_id), None)
    if view is None:
        return _error('invalid_view', 'view not found in requested window')
    revision = view.change_count()
    expected = req.get('expected_revision')
    if expected is not None and expected != revision:
        return _error('revision_conflict', 'buffer changed since the previous capture')
    if view.is_loading():
        return _error('loading', 'buffer is still loading')
    size = view.size()
    active = window.active_view()
    selections = list(view.sel())
    if len(selections) > 256:
        return _error('response_too_large', 'more than 256 selections cannot be returned safely')
    metadata = {'ok': True, 'instance': _INSTANCE, 'window': window_id, 'view': view.id(),
                'buffer': view.buffer_id(), 'path': view.file_name(), 'title': view.name(),
                'dirty': view.is_dirty(), 'loading': view.is_loading(), 'revision': revision,
                'captured_at': time.time(), 'size_points': size,
                'active_view': active.id() if active else None,
                'selections': [{'a': r.a, 'b': r.b, 'empty': r.empty(),
                                'start': list(view.rowcol(r.begin())), 'end': list(view.rowcol(r.end()))}
                               for r in selections],
                'visible_region': {'begin': view.visible_region().begin(), 'end': view.visible_region().end()},
                'viewport_position': list(view.viewport_position()), 'viewport_extent': list(view.viewport_extent()),
                'coordinate_units': 'Sublime points; row and column are zero-based'}
    if operation == 'read':
        start_line, end_line = req.get('start_line', 1), req.get('end_line')
        if type(start_line) is not int or start_line < 1 or (end_line is not None and (type(end_line) is not int or end_line < start_line)):
            return _error('invalid_range', 'lines must be one-based inclusive with start <= end')
        total = view.rowcol(size)[0] + 1
        if start_line > total:
            return _error('invalid_range', 'start line is beyond EOF')
        requested_end = total if end_line is None else end_line
        actual_end = min(requested_end, total)
        begin = view.text_point(start_line - 1, 0)
        end = view.full_line(view.text_point(actual_end - 1, 0)).end()
        max_chars = req.get('max_chars', _MAX_CHARS)
        if type(max_chars) is not int or max_chars < 1 or max_chars > _MAX_CHARS:
            return _error('invalid_limit', 'max_chars must be between 1 and 200000')
        stop = min(end, begin + max_chars)
        metadata.update({'text': view.substr(sublime.Region(begin, stop)),
                         'requested_lines': [start_line, end_line],
                         'returned_points': [begin, stop], 'returned_through_line': view.rowcol(max(begin, stop - 1))[0] + 1,
                         'truncated': stop < end, 'eof_clamped': requested_end > total})
    if view.change_count() != revision:
        return _error('revision_conflict', 'buffer changed during capture')
    return metadata


def _handle(conn):
    try:
        conn.settimeout(5)
        data = bytearray()
        while b'\n' not in data and len(data) <= _MAX_REQUEST:
            chunk = conn.recv(4096)
            if not chunk:
                break
            data.extend(chunk)
        if len(data) > _MAX_REQUEST or b'\n' not in data:
            result = _error('invalid_request', 'request is missing or oversized')
        else:
            req = json.loads(bytes(data).split(b'\n', 1)[0].decode('utf-8'))
            if not isinstance(req, dict):
                raise ValueError('request must be an object')
            request_id = req.get('request_id')
            event, box = threading.Event(), []
            def capture():
                try:
                    box.append(_capture(req))
                except Exception as exc:
                    box.append(_error('capture_failed', str(exc)))
                finally:
                    event.set()
            sublime.set_timeout(capture, 0)
            result = box[0] if event.wait(4) else _error('timeout', 'editor did not respond before deadline')
            result['request_id'] = request_id
        conn.sendall((json.dumps(result, ensure_ascii=False) + '\n').encode('utf-8'))
    except Exception:
        try:
            conn.sendall(b'{"ok":false,"error":{"code":"invalid_request","message":"invalid request"}}\n')
        except OSError:
            pass
    finally:
        conn.close()


def _serve():
    while not _STOP.is_set():
        try:
            conn, _ = _SERVER.accept()
        except socket.timeout:
            continue
        except OSError:
            break
        if not _SLOTS.acquire(False):
            try:
                conn.sendall(b'{"ok":false,"error":{"code":"busy","message":"too many requests"}}\n')
            except OSError:
                pass
            finally:
                conn.close()
            continue
        def serve_one(connection):
            try:
                _handle(connection)
            finally:
                _SLOTS.release()
        try:
            _POOL.submit(serve_one, conn)
        except RuntimeError:
            _SLOTS.release()
            conn.close()


def plugin_loaded():
    global _SERVER, _THREAD, _POOL
    try:
        root = _registry()
        path = os.path.join(root, _INSTANCE + '.sock')
        _SERVER = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        _SERVER.bind(path)
        os.chmod(path, 0o600)
        _SERVER.listen(16)
        _SERVER.settimeout(0.5)
        info = {'instance': _INSTANCE, 'socket': path, 'pid': os.getpid(), 'version': 1,
                'sublime_build': sublime.version(), 'python_version': sys.version.split()[0]}
        descriptor = os.path.join(root, _INSTANCE + '.json')
        with open(descriptor, 'x', encoding='utf-8') as handle:
            os.chmod(descriptor, 0o600)
            json.dump(info, handle)
        _POOL = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        _THREAD = threading.Thread(target=_serve, daemon=True)
        _THREAD.start()
    except Exception as exc:
        print('sublime-observer failed to start: {}'.format(exc))
        plugin_unloaded()


def plugin_unloaded():
    _STOP.set()
    if _SERVER:
        _SERVER.close()
    if _POOL:
        _POOL.shutdown(wait=False)
    try:
        root = _registry()
        for extension in ('.json', '.sock'):
            try:
                os.unlink(os.path.join(root, _INSTANCE + extension))
            except FileNotFoundError:
                pass
    except Exception:
        pass
