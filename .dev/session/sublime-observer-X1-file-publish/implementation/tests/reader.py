"""Reader-side helper used by tests: the read discipline a CLI agent follows.

1. publisher.json -> epoch; heartbeat older than stale_after_s means "not live".
2. state.json -> text_file; then read exactly that file.
3. If the named text file is gone, re-read state (bounded retries). No hashing.
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


def read_capture(view_dir, retries=5, between=None):
    """Return (state, text). `between(state)` is a test hook run after state is read
    and before the text is opened (lets a test interleave publications)."""
    for _ in range(retries):
        try:
            state = _json(os.path.join(view_dir, 'state.json'))
        except FileNotFoundError:
            raise Unavailable('view directory has no state (unshared or closed)')
        if between is not None:
            between(state)
        if state['text_file'] is None:
            return state, None
        try:
            with open(os.path.join(view_dir, state['text_file']), 'rb') as handle:
                text = handle.read().decode(state['text_file_encoding'])
        except FileNotFoundError:
            continue
        return state, text
    raise Unavailable('text kept moving; retries exhausted')


def read_current(root, now=None, retries=5):
    """Read the single shared view through `current`, checking epochs agree."""
    info = publisher(root, now)
    link = os.path.join(root, 'current')
    if not os.path.islink(link):
        raise Unavailable('current is absent (zero or several shares)')
    state, text = read_capture(link, retries)
    if state['epoch'] != info['epoch']:
        raise Unavailable('state belongs to another epoch')
    return state, text
