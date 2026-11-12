"""Test-only writer, enabled solely inside an explicitly marked disposable profile."""
import json
import os
import socket
import threading

import sublime
import sublime_plugin

_SERVER = None
_VIEWS = {}
_WINDOWS = {}
_ROOT = None


class ObserverFixtureTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        if self.view.id() not in _VIEWS:
            raise ValueError('not a fixture view')
        self.view.replace(edit, sublime.Region(0, self.view.size()), text)


def _dispatch(q):
    operation = q['operation']
    if operation == 'new_window':
        sublime.run_command('new_window')
        window = sublime.active_window()
        _WINDOWS[window.id()] = window
        return {'window': window.id()}
    window = _WINDOWS[q['window']]
    if operation == 'order':
        return {'tabs': sorted([
            {'view': view.id(), 'group': window.get_view_index(view)[0],
             'index': window.get_view_index(view)[1]} for view in window.views()
        ], key=lambda tab: (tab['group'], tab['index']))}
    if operation == 'create':
        relative = q.get('path')
        if relative:
            path = os.path.realpath(os.path.join(_ROOT, relative))
            if not path.startswith(_ROOT + os.sep):
                raise ValueError('path escapes disposable root')
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(q.get('disk_text', 'DISK\n'))
            view = window.open_file(path)
        else:
            view = window.new_file()
            view.set_name(q.get('title', 'synthetic draft'))
        _VIEWS[view.id()] = view
        return {'view': view.id(), 'buffer': view.buffer_id(), 'path': view.file_name()}
    view = _VIEWS[q['view']]
    if view.window() != window:
        raise ValueError('view does not belong to fixture window')
    if operation == 'write':
        if view.is_loading():
            raise ValueError('fixture loading')
        view.run_command('observer_fixture_text', {'text': q['text']})
    elif operation == 'focus':
        window.focus_view(view)
        window.bring_to_front()
    elif operation == 'reorder':
        window.set_view_index(view, 0, q['index'])
    elif operation == 'close':
        view.set_scratch(True)
        view.close()
    elif operation == 'clone':
        window.focus_view(view)
        window.run_command('clone_file')
        clone = window.active_view()
        if clone.id() == view.id() or clone.buffer_id() != view.buffer_id():
            raise ValueError('clone command did not create expected view')
        _VIEWS[clone.id()] = clone
        return {'view': clone.id(), 'buffer': clone.buffer_id()}
    elif operation == 'selection':
        view.sel().clear()
        for a, b in q['regions']:
            view.sel().add(sublime.Region(a, b))
        view.set_viewport_position(tuple(q.get('viewport', [0, 0])), False)
    else:
        raise ValueError('unsupported fixture operation')
    return {}


def _serve():
    while _SERVER is not None:
        try:
            conn, _ = _SERVER.accept()
        except OSError:
            return
        with conn:
            try:
                conn.settimeout(5)
                data = bytearray()
                while b'\n' not in data and len(data) < 1000000:
                    chunk = conn.recv(65536)
                    if not chunk:
                        break
                    data.extend(chunk)
                q = json.loads(bytes(data).split(b'\n')[0])
                done, box = threading.Event(), []
                def capture():
                    try:
                        box.append(dict(_dispatch(q), ok=True))
                    except Exception as exc:
                        box.append({'ok': False, 'error': str(exc)})
                    finally:
                        done.set()
                sublime.set_timeout(capture, 0)
                if not done.wait(4):
                    raise ValueError('fixture UI timeout')
                conn.sendall((json.dumps(box[0]) + '\n').encode())
            except Exception as exc:
                conn.sendall((json.dumps({'ok': False, 'error': str(exc)}) + '\n').encode())


def plugin_loaded():
    global _SERVER, _ROOT
    root = os.environ.get('OBSERVER_TRIAL_ROOT', '')
    if not root.startswith('/tmp/nablarva-observer-audit-'):
        return
    _ROOT = os.path.realpath(root)
    expected = os.path.join(_ROOT, 'portable', 'Data', 'Packages')
    if os.path.realpath(sublime.packages_path()) != expected:
        return
    _SERVER = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    path = os.path.join(_ROOT, 'runtime', 'fixture.sock')
    _SERVER.bind(path)
    os.chmod(path, 0o600)
    _SERVER.listen(8)
    threading.Thread(target=_serve, daemon=True).start()


def plugin_unloaded():
    global _SERVER
    if _SERVER:
        _SERVER.close()
        _SERVER = None
        try:
            os.unlink(os.path.join(_ROOT, 'runtime', 'fixture.sock'))
        except OSError:
            pass
