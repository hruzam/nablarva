"""Reader-side helper used by tests: the read discipline a CLI agent follows (step 5).

1. publisher.json -> epoch; heartbeat older than stale_after_s means "not live".
2. Through `current`: resolve the link ONCE (readlink -> views/<share_id>) and read only from
   that one directory; never open `current/...` twice.
3. state.json -> text_file; then read exactly that file from the same directory.
4. state.json again: epoch, share_id and seq must equal the first read, else retry.
   (A pair that passes was the current capture at that instant; nothing more.)
5. If the named text file is gone, or step 4 differs, retry (bounded). No hashing.
"""
import json
import os
import time


class NotLive(Exception):
    pass


class Unavailable(Exception):
    pass


def _json(path):
    with open(path, 'rb') as handle:
        return json.loads(handle.read().decode('utf-8'))


def publisher(root, now=None):
    """Return publisher.json if the publisher is live, else raise NotLive."""
    try:
        info = _json(os.path.join(root, 'publisher.json'))
    except FileNotFoundError:
        raise NotLive('no publisher.json')
    now = time.time() if now is None else now
    if now - info['heartbeat_at'] > info['stale_after_s']:
        raise NotLive('heartbeat is stale')
    return info


def resolve_current(root):
    """Resolve `current` once. Returns (share_id, view_dir) or raises Unavailable."""
    try:
        target = os.readlink(os.path.join(root, 'current'))
    except FileNotFoundError:
        raise Unavailable('current is absent (zero or several shares)')
    except OSError:
        raise Unavailable('current is not a symlink')
    parts = target.split('/')
    if len(parts) != 2 or parts[0] != 'views' or parts[1] in ('', '.', '..'):
        raise Unavailable('current does not name views/<share_id>: {!r}'.format(target))
    return parts[1], os.path.join(root, 'views', parts[1])


def _identity(state):
    return (state.get('epoch'), state.get('share_id'), state.get('seq'))


def read_capture(view_dir, retries=5, between=None, share_id=None, after_text=None):
    """Return (state, text) read from one view directory. `between(state)` runs after the
    first state read and before the text is opened; `after_text(state)` runs before the
    second state read (test hooks that interleave publications). With `share_id`, the
    state must name that share."""
    for _ in range(retries):
        try:
            state = _json(os.path.join(view_dir, 'state.json'))
        except FileNotFoundError:
            raise Unavailable('view directory has no state (unshared or closed)')
        if share_id is not None and state.get('share_id') != share_id:
            raise Unavailable('state names share {!r}, not {!r}'.format(state.get('share_id'), share_id))
        if between is not None:
            between(state)
        text = None
        if state['text_file'] is not None:
            try:
                with open(os.path.join(view_dir, state['text_file']), 'rb') as handle:
                    text = handle.read().decode(state['text_file_encoding'])
            except FileNotFoundError:
                continue
        if after_text is not None:
            after_text(state)
        try:
            again = _json(os.path.join(view_dir, 'state.json'))
        except FileNotFoundError:
            raise Unavailable('view directory has no state (unshared or closed)')
        if _identity(again) != _identity(state):
            continue
        return state, text
    raise Unavailable('text kept moving; retries exhausted')


def read_current(root, now=None, retries=5, between=None, after_text=None):
    """Read the single shared view through `current` (resolved once), checking epochs agree."""
    info = publisher(root, now)
    share_id, view_dir = resolve_current(root)
    state, text = read_capture(view_dir, retries, between=between, share_id=share_id, after_text=after_text)
    if state['epoch'] != info['epoch']:
        raise Unavailable('state belongs to another epoch')
    return state, text
