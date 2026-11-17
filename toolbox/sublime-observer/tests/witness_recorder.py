#!/usr/bin/env python3
"""Read-only witness recorder for the SublimeObserver publication directory (step 4a).

Watches <root> (default /run/user/<uid>/sublime-observer) and writes a JSONL timeline that a
verifier analyses afterwards. It never touches the editor: no socket, no signal, no process
query, no write under the root. It reads only under the root, and its own --out is the only
file it writes. `current` and every file it opens must resolve inside the root.

    python3 -I -B .../tests/witness_recorder.py --out <file.jsonl> --forbid <s> [--forbid <s> ...]
                  [--root <dir>] [--interval-ms 100]

Records (one JSON object per line, flushed per line; every record has kind, n, wall, mono, iso):
  start      config: root, out, forbid strings, interval, pid, python
  sample     snapshot (see snapshot()); written when it differs from the last written sample
             (heartbeat age excluded from the comparison), else at least once a second
  stamp      {"stamp": "<line typed on stdin>"}
  stdin_eof  stdin reached end of file (recording continues)
  end        reason, records, stamps, forbidden hit count
Stored per text file: character count and sha256 of the bytes on disk, never the text.

Standard library only. Python 3.8 syntax.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import os
import select
import signal
import stat
import sys
import time

sys.dont_write_bytecode = True      # importing reader.py must never leave __pycache__ behind

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDER_VERSION = 1
KEEPALIVE_S = 1.0
STATE_FIELDS = ('share_id', 'epoch', 'seq', 'revision', 'dirty', 'loading', 'path', 'title',
                'size_chars', 'published_chars', 'truncated', 'text_file', 'text_file_encoding',
                'text_encoding_replaced',
                'selections', 'visible_region', 'viewport_position')
PUBLISHER_FIELDS = ('contract_version', 'epoch', 'pid', 'started_at', 'heartbeat_at',
                    'heartbeat_interval_s', 'stale_after_s', 'sublime_build', 'plugin_python')
INDEX_ENTRY_FIELDS = ('share_id', 'path', 'title', 'window', 'view', 'buffer', 'state')


class OutsideRoot(Exception):
    """A read would leave the root (symlink or path outside it)."""


# --- guarded reads ------------------------------------------------------------

def inside(root_real, path):
    real = os.path.realpath(path)
    return real == root_real or real.startswith(root_real + os.sep)


def read_bytes(root_real, path):
    """Read a regular file whose resolved path is inside the root. Never follows a final
    symlink, never blocks on a FIFO, refuses anything that is not a regular file."""
    if not inside(root_real, path):
        raise OutsideRoot('{} resolves outside the root'.format(path))
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_CLOEXEC', 0) | getattr(os, 'O_NONBLOCK', 0)
    fd = os.open(path, flags)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OutsideRoot('{} is not a regular file'.format(path))
        chunks = []
        while True:
            chunk = os.read(fd, 1 << 20)
            if not chunk:
                break
            chunks.append(chunk)
        return b''.join(chunks)
    finally:
        os.close(fd)


def load_reader(root):
    """A private instance of tests/reader.py whose `open` is guarded to the root, so the
    contract reader itself can never be led outside it (e.g. by a text_file of '../x').
    Step 5: it follows reader.py's rule as is (resolve `current` once, state, text, state
    again); text names now carry the share id (text.<share_id>.<revision>)."""
    root_real = os.path.realpath(root)

    def guarded_open(path, mode='r', *args, **kwargs):
        if mode != 'rb':
            raise OutsideRoot('reader asked for mode {!r}'.format(mode))
        return io.BytesIO(read_bytes(root_real, path))

    spec = importlib.util.spec_from_file_location('witness_contract_reader', os.path.join(HERE, 'reader.py'))
    module = importlib.util.module_from_spec(spec)
    module.open = guarded_open
    spec.loader.exec_module(module)
    return module


def describe_error(exc):
    if isinstance(exc, FileNotFoundError):
        return 'vanished'
    if isinstance(exc, OutsideRoot):
        return 'refused: {}'.format(exc)
    if isinstance(exc, (ValueError, UnicodeDecodeError)):
        return 'bad json: {}'.format(exc)
    return '{}: {}'.format(type(exc).__name__, exc)


# --- snapshot -----------------------------------------------------------------

def _kind(mode):
    if stat.S_ISLNK(mode):
        return 'symlink'
    if stat.S_ISDIR(mode):
        return 'dir'
    if stat.S_ISREG(mode):
        return 'file'
    return 'other'


def list_entries(root, errors):
    """All names under root (relative), without following symlinks."""
    out = []

    def onerror(exc):
        errors.append({'path': os.path.relpath(getattr(exc, 'filename', root) or root, root),
                       'op': 'list', 'error': describe_error(exc)})

    for dirpath, dirnames, filenames in os.walk(root, onerror=onerror, followlinks=False):
        for name in sorted(dirnames) + sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            try:
                st = os.lstat(full)
            except OSError as exc:
                errors.append({'path': rel, 'op': 'lstat', 'error': describe_error(exc)})
                continue
            entry = {'name': rel, 'type': _kind(st.st_mode), 'mode': oct(st.st_mode & 0o7777)}
            if entry['type'] == 'symlink':
                try:
                    entry['target'] = os.readlink(full)
                except OSError as exc:
                    entry['target_error'] = describe_error(exc)
            elif entry['type'] == 'file':
                entry['size'] = st.st_size
            out.append(entry)
    out.sort(key=lambda e: e['name'])
    return out


def load_json(root_real, path):
    return json.loads(read_bytes(root_real, path).decode('utf-8'))


def pick(obj, fields):
    return {k: obj.get(k) for k in fields if k in obj}


def publisher_part(root, root_real, wall, reader, errors, volatile):
    path = os.path.join(root, 'publisher.json')
    part = {'present': os.path.lexists(path)}
    if part['present']:
        try:
            info = load_json(root_real, path)
            if isinstance(info, dict):
                part['fields'] = pick(info, PUBLISHER_FIELDS)
                extra = sorted(set(info) - set(PUBLISHER_FIELDS))
                if extra:
                    part['other_keys'] = extra
            else:
                part['fields'] = None
                errors.append({'path': 'publisher.json', 'op': 'parse', 'error': 'not a JSON object'})
        except Exception as exc:
            errors.append({'path': 'publisher.json', 'op': 'read', 'error': describe_error(exc)})
    try:
        info = reader.publisher(root, wall)
        part['reader'] = 'live'
        beat = info.get('heartbeat_at')
        if isinstance(beat, (int, float)):
            volatile['heartbeat_age_s'] = round(wall - beat, 3)
    except reader.NotLive as exc:
        part['reader'] = 'not live: {}'.format(exc)
    except Exception as exc:
        part['reader'] = 'reader error: {}'.format(describe_error(exc))
    return part


def index_part(root, root_real, errors):
    path = os.path.join(root, 'index.json')
    if not os.path.lexists(path):
        return {'present': False}
    part = {'present': True}
    try:
        data = load_json(root_real, path)
        part['epoch'] = data.get('epoch')
        part['shared'] = [pick(e, INDEX_ENTRY_FIELDS) if isinstance(e, dict) else {'malformed': True}
                          for e in (data.get('shared') or [])]
    except Exception as exc:
        errors.append({'path': 'index.json', 'op': 'read', 'error': describe_error(exc)})
    return part


def current_part(root, root_real):
    link = os.path.join(root, 'current')
    try:
        st = os.lstat(link)
    except FileNotFoundError:
        return {'present': False}
    except OSError as exc:
        return {'present': None, 'error': describe_error(exc)}
    part = {'present': True, 'type': _kind(st.st_mode)}
    if part['type'] == 'symlink':
        try:
            part['target'] = os.readlink(link)
        except OSError as exc:
            part['target_error'] = describe_error(exc)
        part['resolves_inside_root'] = inside(root_real, link)
    else:
        part['resolves_inside_root'] = False
    return part


def text_digest(data, encoding):
    out = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    try:
        out['chars'] = len(data.decode(encoding or 'utf-8'))
    except (UnicodeDecodeError, LookupError) as exc:
        out['chars'] = None
        out['decode_error'] = type(exc).__name__
    return out


def read_current_part(root, wall, reader, current):
    if current.get('present') and not current.get('resolves_inside_root'):
        return {'ok': False, 'reason': 'not called: current does not resolve inside the root; not followed'}
    try:
        state, text = reader.read_current(root, wall)
    except (reader.NotLive, reader.Unavailable) as exc:
        return {'ok': False, 'reason': '{}: {}'.format(type(exc).__name__, exc)}
    except Exception as exc:
        return {'ok': False, 'reason': 'reader error: {}'.format(describe_error(exc))}
    part = {'ok': True}
    if isinstance(state, dict):
        part.update(pick(state, ('share_id', 'epoch', 'seq', 'revision', 'text_file', 'published_chars')))
    if text is None:
        part['text'] = None
    else:
        part['text_chars'] = len(text)
        part['text_sha256_utf8'] = hashlib.sha256(text.encode('utf-8', 'surrogatepass')).hexdigest()
        part['chars_equal_published'] = isinstance(state, dict) and len(text) == state.get('published_chars')
    return part


def plain_name(name):
    return isinstance(name, str) and name not in ('', '.', '..') and '/' not in name and '\0' not in name


def views_part(root, root_real, errors):
    vroot = os.path.join(root, 'views')
    try:
        st = os.lstat(vroot)
    except FileNotFoundError:
        return {'present': False}
    except OSError as exc:
        return {'present': None, 'error': describe_error(exc)}
    if not stat.S_ISDIR(st.st_mode):
        return {'present': True, 'type': _kind(st.st_mode), 'note': 'not a real directory; not entered'}
    try:
        names = sorted(os.listdir(vroot))
    except OSError as exc:
        errors.append({'path': 'views', 'op': 'list', 'error': describe_error(exc)})
        return {'present': True, 'dirs': {}}
    dirs = {}
    for name in names:
        vdir = os.path.join(vroot, name)
        rel = os.path.join('views', name)
        try:
            vst = os.lstat(vdir)
        except OSError as exc:
            errors.append({'path': rel, 'op': 'lstat', 'error': describe_error(exc)})
            continue
        if not stat.S_ISDIR(vst.st_mode):
            dirs[name] = {'type': _kind(vst.st_mode), 'note': 'not a real directory; not entered'}
            continue
        view = {}
        spath = os.path.join(vdir, 'state.json')
        try:
            state = load_json(root_real, spath)
        except Exception as exc:
            view['state'] = None
            view['state_error'] = describe_error(exc)
            if not isinstance(exc, FileNotFoundError):
                errors.append({'path': os.path.join(rel, 'state.json'), 'op': 'read', 'error': describe_error(exc)})
            dirs[name] = view
            continue
        if not isinstance(state, dict):
            view['state'] = None
            view['state_error'] = 'not a JSON object'
            dirs[name] = view
            continue
        view['state'] = pick(state, STATE_FIELDS)
        err = state.get('error')
        view['state']['error_code'] = err.get('code') if isinstance(err, dict) else err
        tname = state.get('text_file')
        if tname is None:
            view['text'] = None
        elif not plain_name(tname):
            view['text'] = {'exists': None, 'note': 'text_file is not a plain file name; not opened'}
        else:
            tpath = os.path.join(vdir, tname)
            try:
                tst = os.lstat(tpath)
            except FileNotFoundError:
                view['text'] = {'exists': False}
            except OSError as exc:
                view['text'] = {'exists': None, 'error': describe_error(exc)}
            else:
                if not stat.S_ISREG(tst.st_mode):
                    view['text'] = {'exists': True, 'type': _kind(tst.st_mode), 'note': 'not a regular file; not opened'}
                else:
                    try:
                        data = read_bytes(root_real, tpath)
                    except Exception as exc:
                        view['text'] = {'exists': not isinstance(exc, FileNotFoundError), 'error': describe_error(exc)}
                    else:
                        digest = text_digest(data, state.get('text_file_encoding'))
                        digest['exists'] = True
                        digest['chars_equal_published'] = digest['chars'] == state.get('published_chars')
                        view['text'] = digest
        dirs[name] = view
    return {'present': True, 'dirs': dirs}


def forbidden_forms(strings):
    """Byte forms searched for each string: UTF-8 as is, and as it appears inside JSON."""
    forms = []
    for s in strings:
        variants = {s.encode('utf-8', 'surrogatepass'),
                    json.dumps(s, ensure_ascii=False)[1:-1].encode('utf-8', 'surrogatepass'),
                    json.dumps(s)[1:-1].encode('ascii')}
        forms.append(sorted(variants))
    return forms


def forbidden_scan(root, root_real, entries, forms, errors):
    hits = []
    for entry in entries:
        if entry['type'] != 'file':
            continue
        path = os.path.join(root, entry['name'])
        try:
            data = read_bytes(root_real, path)
        except Exception as exc:
            if not isinstance(exc, FileNotFoundError):
                errors.append({'path': entry['name'], 'op': 'scan', 'error': describe_error(exc)})
            continue
        found = [i for i, variants in enumerate(forms) if any(v in data for v in variants)]
        if found:
            hits.append({'file': entry['name'], 'forbid': found})
    return hits


def snapshot(root, forms, reader, wall=None):
    """One sample of the root. Returns a dict; `volatile` holds values excluded from change
    detection (heartbeat age moves every sample)."""
    wall = time.time() if wall is None else wall
    errors, volatile = [], {}
    snap = {'root': {'exists': False}}
    try:
        st = os.lstat(root)
    except FileNotFoundError:
        snap.update(volatile=volatile, errors=errors)
        return snap
    except OSError as exc:
        snap['root'] = {'exists': None, 'error': describe_error(exc)}
        snap.update(volatile=volatile, errors=errors)
        return snap
    snap['root'] = {'exists': True, 'type': _kind(st.st_mode), 'mode': oct(st.st_mode & 0o7777),
                    'owned_by_me': st.st_uid == os.getuid()}
    if not stat.S_ISDIR(st.st_mode):
        snap['root']['note'] = 'not a real directory; nothing under it is read'
        snap.update(volatile=volatile, errors=errors)
        return snap
    root_real = os.path.realpath(root)
    entries = list_entries(root, errors)
    snap['entries'] = entries
    snap['publisher'] = publisher_part(root, root_real, wall, reader, errors, volatile)
    snap['index'] = index_part(root, root_real, errors)
    snap['current'] = current_part(root, root_real)
    snap['read_current'] = read_current_part(root, wall, reader, snap['current'])
    snap['views'] = views_part(root, root_real, errors)
    snap['forbidden_hits'] = forbidden_scan(root, root_real, entries, forms, errors)
    snap.update(volatile=volatile, errors=errors)
    return snap


def comparable(snap):
    return {k: v for k, v in snap.items() if k != 'volatile'}


# --- CLI ----------------------------------------------------------------------

def default_root():
    return '/run/user/{}/sublime-observer'.format(os.getuid())


def clock():
    wall, mono = time.time(), time.monotonic()
    iso = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(wall)) + '.{:03d}'.format(int(wall * 1000) % 1000)
    return wall, mono, iso


def say(line):
    try:
        sys.stderr.write('[witness] {}\n'.format(line))
        sys.stderr.flush()
    except (OSError, ValueError):     # terminal gone (SIGHUP): the JSONL still gets the record
        pass


class Out(object):
    def __init__(self, path):
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_CLOEXEC', 0)
        self.fd = os.open(path, flags, 0o600)
        os.fchmod(self.fd, 0o600)
        self.records = 0

    def write(self, kind, **fields):
        wall, mono, iso = clock()
        rec = {'kind': kind, 'n': self.records, 'wall': wall, 'mono': mono, 'iso': iso}
        rec.update(fields)
        data = (json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n').encode('utf-8', 'surrogatepass')
        view = memoryview(data)
        while view:
            view = view[os.write(self.fd, view):]
        self.records += 1
        return rec

    def close(self):
        try:
            os.fsync(self.fd)
        except OSError:
            pass
        os.close(self.fd)


def parse_args(argv):
    p = argparse.ArgumentParser(description='Read-only witness recorder for the SublimeObserver publication directory.')
    p.add_argument('--out', required=True, help='JSONL output file; must not exist and must not be under the root')
    p.add_argument('--forbid', action='append', required=True, help='string that must never appear under the root (repeatable)')
    p.add_argument('--root', default=None, help='publication root (default /run/user/<uid>/sublime-observer)')
    p.add_argument('--interval-ms', type=int, default=100, help='sample interval in ms (default 100)')
    return p.parse_args(argv)


def check_config(args):
    """Return (root, out, error)."""
    root = os.path.abspath(args.root if args.root is not None else default_root())
    out = os.path.abspath(args.out)
    if any(s == '' for s in args.forbid):
        return root, out, 'an empty --forbid string would match everything'
    if not 10 <= args.interval_ms <= 10000:
        return root, out, '--interval-ms must be between 10 and 10000'
    if os.path.lexists(out):
        return root, out, '--out {} already exists; refusing to overwrite'.format(out)
    for r, o in ((root, out), (os.path.realpath(root), os.path.realpath(out))):
        if o == r or o.startswith(r.rstrip(os.sep) + os.sep):
            return root, out, '--out {} is under the root {}; refusing'.format(out, root)
    if not os.path.isdir(os.path.dirname(out)):
        return root, out, 'the directory of --out does not exist: {}'.format(os.path.dirname(out))
    return root, out, None


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root, out_path, error = check_config(args)
    if error:
        say('refused: ' + error)
        return 2
    reader = load_reader(root)
    forms = forbidden_forms(args.forbid)
    try:
        out = Out(out_path)
    except OSError as exc:
        say('refused: cannot create --out {}: {}'.format(out_path, exc))
        return 2

    stop = {'reason': None}

    def on_signal(signum, _frame):
        stop['reason'] = signal.Signals(signum).name

    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
        signal.signal(sig, on_signal)

    say('root   {}'.format(root))
    say('out    {}'.format(out_path))
    for i, s in enumerate(args.forbid):
        say('forbid #{} {!r}'.format(i, s))
    xdg = os.environ.get('XDG_RUNTIME_DIR')
    if args.root is None and xdg and os.path.normpath(xdg) != os.path.dirname(root):
        say('WARNING: XDG_RUNTIME_DIR={} differs; the publisher would use that base, not {}'.format(xdg, os.path.dirname(root)))
    say('sampling every {} ms; type a line + Enter to stamp; Ctrl-C to stop'.format(args.interval_ms))
    out.write('start', recorder_version=RECORDER_VERSION, root=root, out=out_path, forbid=list(args.forbid),
              interval_ms=args.interval_ms, pid=os.getpid(), python=sys.version.split()[0])

    interval = args.interval_ms / 1000.0
    stdin_fd = 0
    try:
        os.fstat(stdin_fd)
    except OSError:
        stdin_fd = None
    pending = b''
    stamps = 0
    hit_pairs, active_hits = set(), set()
    last_snap, last_written = None, None
    samples = 0
    next_at = time.monotonic()

    def stamp(raw):
        text = raw.decode('utf-8', 'replace').rstrip('\r')
        rec = out.write('stamp', stamp=text)
        say('{} stamp {}'.format(rec['iso'], text))

    while stop['reason'] is None:
        now = time.monotonic()
        if now >= next_at:
            started = time.monotonic()
            try:
                snap = snapshot(root, forms, reader)
            except Exception as exc:        # never fatal
                snap = {'sample_error': describe_error(exc), 'volatile': {}}
            samples += 1
            took = round((time.monotonic() - started) * 1000, 2)
            current_hits = set()
            for hit in snap.get('forbidden_hits') or []:
                for i in hit['forbid']:
                    current_hits.add((hit['file'], i))
            for pair in sorted(current_hits - active_hits):
                say('!!! FORBIDDEN STRING FOUND: {} contains --forbid #{} {!r} !!!'.format(pair[0], pair[1], args.forbid[pair[1]]))
            hit_pairs |= current_hits
            active_hits = current_hits
            key = comparable(snap)
            changed = key != last_snap
            if changed or last_written is None or started - last_written >= KEEPALIVE_S:
                out.write('sample', changed=changed, sample_n=samples, sample_ms=took, snapshot=snap)
                last_snap, last_written = key, started
            next_at += interval
            if next_at < time.monotonic():          # fell behind: do not burst
                next_at = time.monotonic() + interval
        wait = max(0.0, next_at - time.monotonic())
        if stdin_fd is None:
            time.sleep(wait)
            continue
        try:
            ready = select.select([stdin_fd], [], [], wait)[0]
        except OSError:
            stdin_fd = None
            continue
        if not ready:
            continue
        try:
            chunk = os.read(stdin_fd, 4096)
        except OSError:
            chunk = b''
        if not chunk:
            if pending:
                stamp(pending)
                stamps += 1
                pending = b''
            out.write('stdin_eof')
            say('stdin closed; still recording (Ctrl-C to stop)')
            stdin_fd = None
            continue
        pending += chunk
        while b'\n' in pending:
            line, pending = pending.split(b'\n', 1)
            stamp(line)
            stamps += 1

    if pending:
        stamp(pending)
        stamps += 1
    out.write('end', reason=stop['reason'], samples=samples, records=out.records + 1, stamps=stamps,
              forbidden_hits=[{'file': f, 'forbid': i} for f, i in sorted(hit_pairs)])
    records = out.records
    out.close()
    say('stopped by {}: {} records, {} samples, {} stamps, {} forbidden hit(s){}'.format(
        stop['reason'], records, samples, stamps, len(hit_pairs), ' !!!' if hit_pairs else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
