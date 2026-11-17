"""SublimeObserver file contract v1 -- pure Python, no `sublime` import.

Owns everything that touches the publication directory: root resolution and the
private-directory check, sealed-path refusal, state building, atomic writes,
text-file retention, index and `current`, cleanup and publisher liveness.
Also holds the trailing-debounce scheduler and the single writer thread.

Python 3.8 syntax and stdlib only (Sublime plugin hosts 3.8 and 3.14).
"""
import json
import os
import queue
import shutil
import stat
import threading
import time
import uuid

CONTRACT_VERSION = 1
DIR_NAME = 'sublime-observer'
COORDINATE_UNITS = 'Sublime points (characters from buffer start); row and column zero-based'
TEXT_FILE_ENCODING = 'utf-8'
MAX_SELECTIONS = 256
SEALED_COMPONENTS = ('.majkee', '.hlm')
SEALED_BASENAME_PREFIXES = ('.env',)
STALE_FACTOR = 3
DEFAULTS = {
    'root': None,
    'cap_chars': 200000,
    'debounce_ms': 150,
    'max_delay_ms': 1000,
    'viewport_poll_ms': 500,
    'heartbeat_s': 5.0,
}
_TMP_PREFIX = '.tmp-'
_KNOWN = ('current', 'index.json', 'views', 'publisher.json')


class ContractError(Exception):
    """The publication directory cannot be used safely."""


# --- trust boundary -------------------------------------------------------

def sealed_reason(path):
    """Return why `path` must never be shared, or None. Untitled (None) is allowed.

    Checks the path as given and its resolved form, so a symlink into a vault
    is refused as well.
    """
    if path is None:
        return None
    candidates = [os.path.normpath(path)]
    try:
        resolved = os.path.realpath(path)
        if resolved not in candidates:
            candidates.append(resolved)
    except (OSError, ValueError):
        pass
    for candidate in candidates:
        parts = [p for p in candidate.split(os.sep) if p]
        for part in parts:
            if part in SEALED_COMPONENTS:
                return 'path is inside an operator vault ({})'.format(part)
        if parts and any(parts[-1].startswith(p) for p in SEALED_BASENAME_PREFIXES):
            return 'file name starts with .env'
    return None


# --- directories ----------------------------------------------------------

def is_private_dir(path, uid):
    """True when `path` is a real directory (not a symlink), owned by uid, mode 0700."""
    try:
        st = os.lstat(path)
    except OSError:
        return False
    return (stat.S_ISDIR(st.st_mode) and st.st_uid == uid
            and (st.st_mode & 0o777) == 0o700)


def resolve_root(setting, environ, uid):
    """Resolve the publication root. Creates nothing.

    setting None -> $XDG_RUNTIME_DIR/sublime-observer when that variable is an
    absolute private directory, else /run/user/<uid>/sublime-observer.
    An explicit setting must be absolute; its parent is the base.
    The base must be a 0700 directory owned by uid, or ContractError.
    """
    if setting is not None:
        if not isinstance(setting, str) or not setting.strip():
            raise ContractError('setting "root" must be an absolute path or null')
        root = os.path.normpath(os.path.expanduser(setting))
        if not os.path.isabs(root):
            raise ContractError('setting "root" must be an absolute path: {!r}'.format(setting))
        base = os.path.dirname(root)
    else:
        xdg = environ.get('XDG_RUNTIME_DIR')
        if xdg and os.path.isabs(xdg) and is_private_dir(xdg, uid):
            base = os.path.normpath(xdg)
        else:
            base = '/run/user/{}'.format(uid)
        root = os.path.join(base, DIR_NAME)
    if not is_private_dir(base, uid):
        raise ContractError('base {} is not a 0700 directory owned by uid {}; not publishing'.format(base, uid))
    return root


def _mkdir_private(path, uid):
    try:
        os.mkdir(path, 0o700)
        os.chmod(path, 0o700)
    except FileExistsError:
        pass
    if not is_private_dir(path, uid):
        raise ContractError('{} is not a private 0700 directory owned by uid {}'.format(path, uid))


# --- atomic writes --------------------------------------------------------

def atomic_write(directory, name, data):
    """Write bytes to directory/name via a 0600 temp file in the same directory + os.replace."""
    tmp = os.path.join(directory, '{}{}-{}'.format(_TMP_PREFIX, name, uuid.uuid4().hex))
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_CLOEXEC', 0)
    fd = os.open(tmp, flags, 0o600)
    try:
        try:
            os.fchmod(fd, 0o600)
            view = memoryview(data)
            while view:
                written = os.write(fd, view)
                view = view[written:]
        finally:
            os.close(fd)
        os.replace(tmp, os.path.join(directory, name))
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _json_bytes(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=1) + '\n').encode('utf-8')


def set_current(root, share_id):
    """`current` -> views/<share_id> (atomic replace), or remove it when share_id is None."""
    link = os.path.join(root, 'current')
    if share_id is None:
        try:
            os.unlink(link)
        except FileNotFoundError:
            pass
        return
    tmp = os.path.join(root, '{}current-{}'.format(_TMP_PREFIX, uuid.uuid4().hex))
    os.symlink(os.path.join('views', share_id), tmp)
    try:
        os.replace(tmp, link)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _remove_tree(path):
    """Remove a file, symlink or real directory tree without following symlinks."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return
    if stat.S_ISDIR(st.st_mode):
        shutil.rmtree(path)
    else:
        os.unlink(path)


def remove_publication(root):
    """Remove every contract file in root (current first, publisher.json last)."""
    for name in _KNOWN:
        _remove_tree(os.path.join(root, name))
    try:
        names = os.listdir(root)
    except FileNotFoundError:
        return
    for name in names:
        if name.startswith(_TMP_PREFIX):
            _remove_tree(os.path.join(root, name))


# --- liveness -------------------------------------------------------------

def pid_alive(pid):
    """Linux: /proc/<pid> exists. Sends no signal. Without /proc, assume alive
    (conservative: the heartbeat then decides)."""
    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 0:
        return False
    if not os.path.isdir('/proc'):
        return True
    return os.path.exists('/proc/{}'.format(pid))


def read_publisher(root):
    """Return (info, error). info None + error None means no publisher.json."""
    try:
        with open(os.path.join(root, 'publisher.json'), 'rb') as handle:
            raw = handle.read()
    except FileNotFoundError:
        return None, None
    except OSError as exc:
        return None, str(exc)
    try:
        info = json.loads(raw.decode('utf-8'))
    except ValueError as exc:
        return None, 'unparseable publisher.json: {}'.format(exc)
    if not isinstance(info, dict) or not isinstance(info.get('pid'), int) or not isinstance(info.get('epoch'), str):
        return None, 'publisher.json lacks pid or epoch'
    return info, None


def assess_existing(info, error, now, own_pid, own_epoch, alive, default_heartbeat_s):
    """Classify what is already in the root: 'none' | 'residue' | 'live' | 'foreign'."""
    if error is not None:
        return 'foreign'
    if info is None:
        return 'none'
    if info.get('epoch') == own_epoch:
        return 'residue'
    if info.get('pid') == own_pid:
        return 'residue'        # a previous load inside this same plugin host
    if not alive(info['pid']):
        return 'residue'
    interval = info.get('heartbeat_interval_s')
    if not isinstance(interval, (int, float)) or interval <= 0:
        interval = default_heartbeat_s
    beat = info.get('heartbeat_at')
    if not isinstance(beat, (int, float)):
        return 'residue'
    if now - beat <= STALE_FACTOR * max(interval, default_heartbeat_s):
        return 'live'
    return 'residue'            # alive pid but stale heartbeat: pid reuse or hung publisher


# --- state ----------------------------------------------------------------

def build_state(epoch, seq, share_id, capture, text_info, cap, error):
    """Assemble state.json. text_info: dict(file, chars, truncated) or None."""
    return {
        'contract_version': CONTRACT_VERSION,
        'epoch': epoch,
        'seq': seq,
        'share_id': share_id,
        'window': capture.get('window'),
        'view': capture.get('view'),
        'buffer': capture.get('buffer'),
        'path': capture.get('path'),
        'title': capture.get('title'),
        'dirty': capture.get('dirty'),
        'loading': capture.get('loading'),
        'revision': capture.get('revision'),
        'captured_at': capture.get('captured_at'),
        'encoding': capture.get('encoding'),
        'text_file_encoding': TEXT_FILE_ENCODING,
        'size_chars': capture.get('size_chars'),
        'text_file': text_info['file'] if text_info else None,
        'published_chars': text_info['chars'] if text_info else 0,
        'cap': cap,
        'truncated': text_info['truncated'] if text_info else False,
        'selection_count': capture.get('selection_count'),
        'selections_truncated': capture.get('selections_truncated'),
        'selections': capture.get('selections'),
        'visible_region': capture.get('visible_region'),
        'viewport_position': capture.get('viewport_position'),
        'viewport_extent': capture.get('viewport_extent'),
        'coordinate_units': COORDINATE_UNITS,
        'error': error,
    }


def _index_meta(capture):
    return {'path': capture.get('path'), 'title': capture.get('title'), 'window': capture.get('window'),
            'view': capture.get('view'), 'buffer': capture.get('buffer')}


class Store:
    """All disk effects for one publisher epoch. Every method is serialised by a lock;
    call them from the writer thread. `text_rev` is read lock-free by the capture side."""

    def __init__(self, root, epoch, pid, uid, info, cap, heartbeat_s, clock=time.time, alive=pid_alive):
        self.root = root
        self.views_dir = os.path.join(root, 'views')
        self.epoch = epoch
        self.pid = pid
        self.uid = uid
        self.cap = cap
        self.heartbeat_s = heartbeat_s
        self._info = dict(info)
        self._clock = clock
        self._alive = alive
        self._lock = threading.Lock()
        self._shares = {}       # share_id -> {'text', 'prev', 'meta', 'order'}
        self._removed = set()
        self._order = 0
        self.seq = 0
        self.live = False
        self.closed = False
        self.text_rev = {}      # share_id -> revision of the current text file

    def start(self):
        """Return (True, None) when publishing, else (False, one-line reason)."""
        with self._lock:
            _mkdir_private(self.root, self.uid)
            info, error = read_publisher(self.root)
            verdict = assess_existing(info, error, self._clock(), self.pid, self.epoch,
                                      self._alive, self.heartbeat_s)
            if verdict == 'live':
                return False, ('another publisher (pid {}, epoch {}) is live in {}; '
                               'this instance does not publish').format(info['pid'], info['epoch'], self.root)
            if verdict == 'foreign':
                return False, '{} in {}; not publishing, not cleaning'.format(error, self.root)
            remove_publication(self.root)
            _mkdir_private(self.views_dir, self.uid)
            now = self._clock()
            self._info.update({'contract_version': CONTRACT_VERSION, 'epoch': self.epoch, 'pid': self.pid,
                               'started_at': now, 'heartbeat_at': now,
                               'heartbeat_interval_s': self.heartbeat_s,
                               'stale_after_s': STALE_FACTOR * self.heartbeat_s})
            atomic_write(self.root, 'publisher.json', _json_bytes(self._info))
            self._write_index()
            self.live = True
            return True, ('residue of a dead publisher removed' if verdict == 'residue' and info else None)

    def heartbeat(self):
        with self._lock:
            if not self.live:
                return
            self._info['heartbeat_at'] = self._clock()
            atomic_write(self.root, 'publisher.json', _json_bytes(self._info))

    def publish(self, share_id, capture):
        """Write text (only on a new revision), then state, then sweep, then index/current."""
        with self._lock:
            if not self.live or share_id in self._removed:
                return False
            share = self._shares.get(share_id)
            vdir = os.path.join(self.views_dir, share_id)
            new = share is None
            if new:
                _mkdir_private(vdir, self.uid)
                share = {'text': None, 'prev': None, 'meta': None, 'order': self._order + 1}
            revision = capture.get('revision')
            text = capture.get('text')
            loading = bool(capture.get('loading'))
            error = capture.get('error')
            current = share['text']
            if text is not None and not loading and (current is None or current['rev'] != revision):
                name = 'text.{}'.format(revision)
                atomic_write(vdir, name, text.encode(TEXT_FILE_ENCODING, 'replace'))
                share['prev'] = current['file'] if current else share['prev']
                current = share['text'] = {'rev': revision, 'file': name, 'chars': len(text),
                                           'truncated': bool(capture.get('truncated'))}
            text_info = current if (current is not None and current['rev'] == revision and not loading) else None
            if text_info is None and error is None:
                if loading:
                    error = {'code': 'loading', 'message': 'buffer is still loading; no text published'}
                else:
                    error = {'code': 'text_missing', 'message': 'no text file for this revision yet'}
            self.seq += 1
            state = build_state(self.epoch, self.seq, share_id, capture, text_info, self.cap, error)
            atomic_write(vdir, 'state.json', _json_bytes(state))
            if current is not None:
                self.text_rev[share_id] = current['rev']
            self._sweep(vdir, share)
            if new:
                self._order += 1
                self._shares[share_id] = share
            meta = _index_meta(capture) if (new or error is None) else share['meta']
            if new or meta != share['meta']:
                share['meta'] = meta
                self._write_index()
            if new:
                self._fix_current()
            return True

    def remove_share(self, share_id):
        """Index entry, then `current`, then the view directory."""
        with self._lock:
            self._removed.add(share_id)
            self.text_rev.pop(share_id, None)
            self._shares.pop(share_id, None)
            if not self.live:
                return
            self._write_index()
            self._fix_current()
            _remove_tree(os.path.join(self.views_dir, share_id))

    def shutdown(self):
        """Remove this epoch's files. Leaves another epoch's publication alone."""
        with self._lock:
            if self.closed:
                return
            self.closed = True
            was_live, self.live = self.live, False
            if not was_live:
                return
            info, _ = read_publisher(self.root)
            if info is not None and info.get('epoch') != self.epoch:
                return
            remove_publication(self.root)
            try:
                os.rmdir(self.root)
            except OSError:
                pass

    # internal, lock held
    def _sweep(self, vdir, share):
        keep = set()
        if share['text']:
            keep.add(share['text']['file'])
        if share['prev']:
            keep.add(share['prev'])
        for name in os.listdir(vdir):
            if name.startswith('text.') and name not in keep:
                try:
                    os.unlink(os.path.join(vdir, name))
                except FileNotFoundError:
                    pass

    def _write_index(self):
        shared = []
        for share_id, share in sorted(self._shares.items(), key=lambda item: item[1]['order']):
            entry = {'share_id': share_id, 'state': 'views/{}/state.json'.format(share_id)}
            entry.update(share['meta'] or {})
            shared.append(entry)
        atomic_write(self.root, 'index.json', _json_bytes({
            'contract_version': CONTRACT_VERSION, 'epoch': self.epoch,
            'updated_at': self._clock(), 'shared': shared}))

    def _fix_current(self):
        set_current(self.root, next(iter(self._shares)) if len(self._shares) == 1 else None)


# --- scheduling -----------------------------------------------------------

class Debouncer:
    """Trailing debounce with a maximum delay, per key, clock-agnostic.

    touch(key, now) -> delay in seconds to arm a timer, or None when one is armed.
    fire(key, now)  -> None: publish now (state cleared); else delay to re-arm.
    """

    def __init__(self, debounce_s, max_delay_s):
        self.debounce = debounce_s
        self.max_delay = max(max_delay_s, debounce_s)
        self._pending = {}      # key -> [first_touch, last_touch, armed]

    def touch(self, key, now):
        entry = self._pending.get(key)
        if entry is None:
            entry = self._pending[key] = [now, now, False]
        entry[1] = now
        if entry[2]:
            return None
        entry[2] = True
        return max(0.0, self._deadline(entry) - now)

    def fire(self, key, now):
        entry = self._pending.get(key)
        if entry is None:
            return None
        if now >= self._deadline(entry) - 1e-9:
            del self._pending[key]
            return None
        return max(0.0, self._deadline(entry) - now)

    def pending(self, key):
        return key in self._pending

    def cancel(self, key):
        self._pending.pop(key, None)

    def _deadline(self, entry):
        return min(entry[1] + self.debounce, entry[0] + self.max_delay)


class Writer:
    """One daemon thread executing submitted calls in order (keeps file I/O off the
    plugin host's main thread and preserves write order)."""

    def __init__(self, on_error):
        self._queue = queue.Queue()
        self._stop = threading.Event()
        self._on_error = on_error
        self._thread = threading.Thread(target=self._run, name='sublime-observer-writer', daemon=True)
        self._thread.start()

    def submit(self, fn, *args):
        if not self._stop.is_set():
            self._queue.put((fn, args))

    def close(self, timeout):
        """Discard queued work, wait for the running call; True when the thread ended."""
        self._stop.set()
        self._queue.put(None)
        self._thread.join(timeout)
        return not self._thread.is_alive()

    def _run(self):
        while True:
            item = self._queue.get()
            if item is None:
                return
            if self._stop.is_set():
                continue
            fn, args = item
            try:
                fn(*args)
            except Exception as exc:     # never kill the writer
                self._on_error(exc)
