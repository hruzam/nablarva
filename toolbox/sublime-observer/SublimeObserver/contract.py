"""SublimeObserver file contract v1 -- pure Python, no `sublime` import.

Owns everything that touches the publication directory: root resolution and the
private-directory check, sealed-path refusal, state building, atomic writes,
text-file retention, index and `current`, cleanup and publisher ownership.
Also holds the trailing-debounce scheduler and the single writer thread.

Ownership (step 5): the publisher holds an exclusive flock on <root>/publisher.lock for its
whole life. The kernel drops it when the process dies, so there is no takeover logic: a
publisher that cannot take the lock publishes nothing.

Python 3.8 syntax and stdlib only (Sublime plugin hosts 3.8 and 3.14).
"""
import fcntl        # flock on the lock file only (Linux; ownership of the root)
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
    'heartbeat_s': 1.0,
}
_TMP_PREFIX = '.tmp-'
LOCK_NAME = 'publisher.lock'
_KNOWN = ('current', 'index.json', 'views', 'publisher.json')     # never the lock file
_LOCK_ATTEMPTS = 3


class ContractError(Exception):
    """The publication directory cannot be used safely."""


class Stopped(ContractError):
    """Revocation could not be completed; this publisher has stopped publishing."""


def text_name(share_id, revision):
    """Text file name. It carries the share id, so a reader that follows a `current` which
    switched to another share finds no such file (and retries) instead of a wrong pairing."""
    return 'text.{}.{}'.format(share_id, revision)


# --- trust boundary -------------------------------------------------------

def sealed_reason(path):
    """Return why `path` must never be shared, or None. Untitled (None) is allowed.

    Checks the path as given and its resolved form, so a symlink into a vault
    is refused as well. A path that cannot be resolved is refused (fail closed).
    """
    if path is None:
        return None
    try:
        candidates = [os.path.normpath(path)]
        resolved = os.path.realpath(path)
    except (OSError, ValueError, TypeError) as exc:
        return 'path cannot be resolved ({})'.format(type(exc).__name__)
    if resolved not in candidates:
        candidates.append(resolved)
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


# --- ownership ------------------------------------------------------------

def acquire_lock(root, uid):
    """Take the exclusive non-blocking flock on root/publisher.lock.

    Returns the locked fd, or None when another holder has it. Raises FileNotFoundError when
    the root vanished under us (a holder finishing its shutdown removed it; caller retries).

    A holder unlinks the lock file at shutdown while still holding it. A process that opened
    the path before that unlink would then lock a dead inode while a third process locks a
    fresh file at the same path: two holders. So after locking, the fd must still be the file
    at the path (same st_dev and st_ino); otherwise it is closed and the open is retried.
    """
    path = os.path.join(root, LOCK_NAME)
    flags = os.O_RDWR | os.O_CREAT | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_CLOEXEC', 0)
    for _ in range(_LOCK_ATTEMPTS):
        fd = os.open(path, flags, 0o600)
        keep = False
        try:
            st = os.fstat(fd)
            if not stat.S_ISREG(st.st_mode) or st.st_uid != uid:
                raise ContractError('{} is not a regular file owned by uid {}'.format(path, uid))
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                return None
            try:
                at_path = os.lstat(path)
            except FileNotFoundError:
                at_path = None
            if at_path is not None and (at_path.st_dev, at_path.st_ino) == (st.st_dev, st.st_ino):
                keep = True
                return fd
        finally:
            if not keep:
                os.close(fd)
    raise ContractError('{} kept being replaced while locking; not publishing'.format(path))


def _holds_path(fd, path):
    """True when `path` is still the file open on fd."""
    try:
        a, b = os.fstat(fd), os.lstat(path)
    except OSError:
        return False
    return (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)


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


# --- state ----------------------------------------------------------------

def build_state(epoch, seq, share_id, capture, text_info, cap, error):
    """Assemble state.json. text_info: dict(file, chars, truncated, replaced) or None."""
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
        # True when characters UTF-8 cannot encode (e.g. lone surrogates) were written as '?'
        'text_encoding_replaced': bool(text_info and text_info.get('replaced')),
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
    """All disk effects for one publisher epoch. Every method except revoke() is serialised
    by a lock; call them from the writer thread. `text_rev` and `live` are read lock-free by
    the capture side; revoke() is the one main-thread entry (no I/O)."""

    def __init__(self, root, epoch, pid, uid, info, cap, heartbeat_s, clock=time.time):
        self.root = root
        self.views_dir = os.path.join(root, 'views')
        self.lock_path = os.path.join(root, LOCK_NAME)
        self.epoch = epoch
        self.pid = pid
        self.uid = uid
        self.cap = cap
        self.heartbeat_s = heartbeat_s
        self._info = dict(info)
        self._clock = clock
        self._lock = threading.Lock()
        self._lock_fd = None    # the held flock; None when not owning the root
        self._revoke_lock = threading.Lock()
        self._revoked = set()   # share ids that must never be written again
        self._pending = set()   # revoked share ids whose removal has not completed: no heartbeat
        self._shares = {}       # share_id -> {'text', 'prev', 'meta', 'order'}
        self._order = 0
        self._current = None    # share id `current` points at, as last written
        self.seq = 0
        self.live = False
        self.closed = False
        self.stopped = None     # reason, once revocation failed and publishing stopped
        self.text_rev = {}      # share_id -> revision of the current text file

    def start(self):
        """Return (True, None or note) when publishing, else (False, one-line reason)."""
        with self._lock:
            fd = None
            for _ in range(_LOCK_ATTEMPTS):
                _mkdir_private(self.root, self.uid)
                try:
                    fd = acquire_lock(self.root, self.uid)
                except FileNotFoundError:
                    continue        # root removed by a holder finishing its shutdown
                break
            else:
                raise ContractError('{} kept disappearing; not publishing'.format(self.root))
            info, error = read_publisher(self.root)
            if fd is None:
                holder = ' (publisher.json names pid {})'.format(info['pid']) if info else ''
                return False, ('another publisher holds {}{}; this instance does not publish'
                               ).format(self.lock_path, holder)
            self._lock_fd = fd
            try:
                if error is not None:
                    self._release()
                    return False, '{} in {}; not publishing, not cleaning'.format(error, self.root)
                remove_publication(self.root)       # residue: we hold the lock, its writer is gone
                _mkdir_private(self.views_dir, self.uid)
                now = self._clock()
                self._info.update({'contract_version': CONTRACT_VERSION, 'epoch': self.epoch, 'pid': self.pid,
                                   'started_at': now, 'heartbeat_at': now,
                                   'heartbeat_interval_s': self.heartbeat_s,
                                   'stale_after_s': STALE_FACTOR * self.heartbeat_s})
                atomic_write(self.root, 'publisher.json', _json_bytes(self._info))
                self._write_index()
            except BaseException:
                self._release()
                raise
            self.live = True
            return True, ('residue of a dead publisher (epoch {}) removed'.format(info['epoch']) if info else None)

    def revoke(self, share_id):
        """Main thread, no I/O: publish() for this share is a no-op from now on (pending
        captures queued before an unshare, a close or a sealed path are discarded), and no
        heartbeat is written until its removal completes (remove_share)."""
        with self._revoke_lock:
            self._revoked.add(share_id)
            self._pending.add(share_id)

    def _is_revoked(self, share_id):
        with self._revoke_lock:
            return share_id in self._revoked

    def _revocation_pending(self):
        with self._revoke_lock:
            return bool(self._pending)

    def heartbeat(self):
        """Refresh liveness, unless a revocation is pending (decided here, at execution time).

        The time is read BEFORE the pending check: a heartbeat that passes the check started
        it before revoke() ran, so every heartbeat_at written while a revocation is pending
        (including one write already executing at that instant) is earlier than the revoke.
        Fail closed: while a removal waits, other shares stop looking live too."""
        with self._lock:
            now = self._clock()
            if not self.live or self._revocation_pending():
                return
            self._info['heartbeat_at'] = now
            atomic_write(self.root, 'publisher.json', _json_bytes(self._info))

    def publish(self, share_id, capture):
        """Write text (only on a new revision), then state, then sweep, then index/current."""
        with self._lock:
            if not self.live or self._is_revoked(share_id):
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
                name = text_name(share_id, revision)
                try:
                    data, replaced = text.encode(TEXT_FILE_ENCODING), False
                except UnicodeEncodeError:
                    data, replaced = text.encode(TEXT_FILE_ENCODING, 'replace'), True
                atomic_write(vdir, name, data)
                share['prev'] = current['file'] if current else share['prev']
                current = share['text'] = {'rev': revision, 'file': name, 'chars': len(text),
                                           'truncated': bool(capture.get('truncated')), 'replaced': replaced}
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
                self._update_listing()
            return True

    def remove_share(self, share_id):
        """`current` off this share first, then the index, then the view directory, then
        `current` to a remaining single share. On any failure: stop publishing (Stopped).
        Only a completed removal ends the share's pending revocation (heartbeats resume)."""
        self.revoke(share_id)
        with self._lock:
            self.text_rev.pop(share_id, None)
            self._shares.pop(share_id, None)
            if not self.live:
                return
            try:
                self._update_listing(between=lambda: _remove_tree(os.path.join(self.views_dir, share_id)))
            except Exception as exc:
                reason = 'removing share {} failed ({}: {})'.format(share_id[:8], type(exc).__name__, exc)
                self._stop_publishing(reason)
                raise Stopped(reason)
            with self._revoke_lock:
                self._pending.discard(share_id)     # removed: heartbeats may resume

    def shutdown(self):
        """Remove this epoch's files and release the lock. Leaves another epoch's publication alone."""
        with self._lock:
            if self.closed:
                return
            self.closed = True
            self.live = False
            if self._lock_fd is None:
                return
            try:
                info, _ = read_publisher(self.root)
                if info is None or info.get('epoch') == self.epoch:
                    remove_publication(self.root)
                # unlink while still holding the lock (see acquire_lock), then rmdir, then release
                if _holds_path(self._lock_fd, self.lock_path):
                    os.unlink(self.lock_path)
                try:
                    os.rmdir(self.root)
                except OSError:
                    pass
            finally:
                self._release()

    # internal, lock held
    def _release(self):
        fd, self._lock_fd = self._lock_fd, None
        if fd is not None:
            os.close(fd)        # closing the only descriptor drops the flock

    def _stop_publishing(self, reason):
        """Fail closed: no further write of any kind (the heartbeat stops with `live`), and
        best effort so readers see "not live" at once rather than after the stale bound."""
        self.live = False
        self.stopped = reason
        for remove in (lambda: set_current(self.root, None),
                       lambda: os.unlink(os.path.join(self.root, 'publisher.json'))):
            try:
                remove()
            except OSError:
                pass

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

    def _update_listing(self, between=None):
        """Index and `current` in a reader-safe order: a `current` that must change is
        removed before the index is replaced (so it never names a share while the index
        disagrees), and set only after the index and `between` (directory removal) are done."""
        target = next(iter(self._shares)) if len(self._shares) == 1 else None
        if self._current is not None and self._current != target:
            set_current(self.root, None)
            self._current = None
        self._write_index()
        if between is not None:
            between()
        if target is not None and self._current != target:
            set_current(self.root, target)
            self._current = target

    def _write_index(self):
        shared = []
        for share_id, share in sorted(self._shares.items(), key=lambda item: item[1]['order']):
            entry = {'share_id': share_id, 'state': 'views/{}/state.json'.format(share_id)}
            entry.update(share['meta'] or {})
            shared.append(entry)
        atomic_write(self.root, 'index.json', _json_bytes({
            'contract_version': CONTRACT_VERSION, 'epoch': self.epoch,
            'updated_at': self._clock(), 'shared': shared}))


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
