"""Local vault routes. The embedding host must enforce authentication and CSRF."""
import asyncio
import hashlib
import os
from pathlib import Path
import re
import sqlite3
import stat
import uuid
from urllib.parse import unquote, quote

from aiohttp import web

MAX_FILE = 20 * 1024 * 1024


def _uuid(value):
    try:
        parsed = uuid.UUID(value)
        if str(parsed) != value:
            raise ValueError
        return value
    except (ValueError, AttributeError):
        raise web.HTTPBadRequest(text="Invalid UUID")


def _item(row, root, detail=False):
    item = {k: row[k] for k in ("id", "kind", "name", "revision", "size", "sha256")}
    if row["kind"] == "file":
        item["path"] = str(root / row["id"])
        item["downloadUrl"] = f"/api/files/{row['id']}"
    elif detail:
        item["text"] = row["text"]
    return item


def install_vault(app, root: Path):
    root = Path(root)
    if not root.is_absolute() or root != root.resolve():
        raise ValueError("vault root must be absolute and contain no symlinks or traversal")
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    if root != root.resolve() or not root.is_dir():
        raise ValueError("invalid vault root")
    dbpath = root / "vault.sqlite3"
    for name in ("vault.sqlite3", "vault.sqlite3-journal", "vault.sqlite3-wal", "vault.sqlite3-shm"):
        entry = root / name
        if entry.is_symlink() or (entry.exists() and not entry.is_file()):
            raise ValueError("invalid vault database entry")
    # A private root is required: SQLite's sidecars and atomic blob moves rely on
    # other local users being unable to replace entries during an operation.
    if root.stat().st_mode & 0o077:
        raise ValueError("vault root must be private (mode 0700)")
    dirfd = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    db = sqlite3.connect(dbpath, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute("""CREATE TABLE IF NOT EXISTS items (
        id TEXT PRIMARY KEY, kind TEXT NOT NULL, name TEXT NOT NULL,
        revision INTEGER NOT NULL, text TEXT, size INTEGER NOT NULL,
        sha256 TEXT NOT NULL, upload_id TEXT UNIQUE)""")
    lock = asyncio.Lock()

    def lookup(id):
        return db.execute("SELECT * FROM items WHERE id=?", (id,)).fetchone()

    async def all_items(request):
        async with lock:
            return web.json_response({"items": [_item(row, root) for row in db.execute("SELECT * FROM items ORDER BY rowid")]})

    async def get_item(request):
        id = _uuid(request.match_info["id"])
        async with lock:
            row = lookup(id)
            if row is None:
                raise web.HTTPNotFound()
            return web.json_response(_item(row, root, True))

    async def payload(request):
        try:
            data = await request.json()
            if not isinstance(data, dict):
                raise ValueError
            revision = data.get("expectedRevision")
            if type(revision) is not int or revision < 0:
                raise ValueError
            return data, revision
        except (ValueError, TypeError):
            raise web.HTTPBadRequest(text="Invalid JSON or revision")

    def conflict(row):
        return web.json_response({"currentRevision": row["revision"] if row else 0, "error": {"code": "conflict", "message": "Revision or upload ID conflict"}}, status=409)

    async def put_item(request):
        id = _uuid(request.match_info["id"])
        data, revision = await payload(request)
        kind, name, value = data.get("kind"), data.get("name"), data.get("text")
        if kind not in ("prompt", "shortcut") or not isinstance(name, str) or not isinstance(value, str):
            raise web.HTTPBadRequest(text="Invalid item")
        raw = value.encode("utf-8")
        async with lock:
            db.execute("BEGIN IMMEDIATE")
            try:
                row = lookup(id)
                if (row["revision"] if row else 0) != revision or (row and row["kind"] != kind):
                    db.execute("ROLLBACK")
                    return conflict(row)
                db.execute("INSERT INTO items (id,kind,name,revision,text,size,sha256) VALUES (?,?,?,?,?,?,?) "
                           "ON CONFLICT(id) DO UPDATE SET name=excluded.name, revision=excluded.revision, text=excluded.text, size=excluded.size, sha256=excluded.sha256",
                           (id, kind, name, revision + 1, value, len(raw), hashlib.sha256(raw).hexdigest()))
                row = lookup(id)
                db.execute("COMMIT")
            except BaseException:
                db.execute("ROLLBACK")
                raise
            return web.json_response(_item(row, root, True))

    async def delete_item(request):
        id = _uuid(request.match_info["id"])
        _, revision = await payload(request)
        async with lock:
            db.execute("BEGIN IMMEDIATE")
            try:
                row = lookup(id)
                if row is None or row["revision"] != revision:
                    db.execute("ROLLBACK")
                    return conflict(row)
                db.execute("DELETE FROM items WHERE id=?", (id,))
                db.execute("COMMIT")
            except BaseException:
                db.execute("ROLLBACK")
                raise
            if row["kind"] == "file":
                try:
                    os.unlink(id, dir_fd=dirfd)
                except FileNotFoundError:
                    pass
            return web.json_response({"deleted": True})

    async def upload(request):
        upload_id = _uuid(request.headers.get("X-Upload-ID", ""))
        digest = request.headers.get("X-Content-SHA256", "")
        name_header = request.headers.get("X-File-Name")
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or name_header is None:
            raise web.HTTPBadRequest(text="Invalid file headers")
        try:
            name = unquote(name_header, encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            raise web.HTTPBadRequest(text="Invalid file name")
        async with lock:
            existing = db.execute("SELECT * FROM items WHERE upload_id=?", (upload_id,)).fetchone()
            # Even retries are streamed and hashed; the declared digest is not evidence.
            temp = "." + str(uuid.uuid4())
            fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=dirfd)
            size, hasher = 0, hashlib.sha256()
            final = None
            try:
                with os.fdopen(fd, "wb") as stream:
                    async for chunk in request.content.iter_chunked(65536):
                        size += len(chunk)
                        if size > MAX_FILE:
                            raise web.HTTPRequestEntityTooLarge(max_size=MAX_FILE, actual_size=size)
                        hasher.update(chunk)
                        stream.write(chunk)
                    stream.flush()
                    os.fsync(stream.fileno())
                if hasher.hexdigest() != digest:
                    raise web.HTTPUnprocessableEntity(text="Digest mismatch")
                if existing:
                    if existing["sha256"] != digest or existing["size"] != size or existing["name"] != name:
                        return conflict(existing)
                    try:
                        existing_fd = os.open(existing["id"], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dirfd)
                        with os.fdopen(existing_fd, "rb") as stored:
                            if not stat.S_ISREG(os.fstat(stored.fileno()).st_mode):
                                raise OSError("not a regular file")
                            stored_hash = hashlib.sha256()
                            stored_size = 0
                            for chunk in iter(lambda: stored.read(65536), b""):
                                stored_size += len(chunk)
                                if stored_size > MAX_FILE:
                                    raise OSError("stored file too large")
                                stored_hash.update(chunk)
                            if stored_size != size or stored_hash.hexdigest() != digest:
                                raise OSError("stored file changed")
                    except OSError:
                        raise web.HTTPInternalServerError(text="Stored file verification failed")
                    receipt = _item(existing, root)
                    receipt["verified"] = True
                    return web.json_response(receipt)
                final = str(uuid.uuid4())
                os.replace(temp, final, src_dir_fd=dirfd, dst_dir_fd=dirfd)
                os.fsync(dirfd)
                check = hashlib.sha256()
                readfd = os.open(final, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=dirfd)
                with os.fdopen(readfd, "rb") as stream:
                    for chunk in iter(lambda: stream.read(65536), b""):
                        check.update(chunk)
                if check.hexdigest() != digest:
                    raise web.HTTPInternalServerError(text="Stored file verification failed")
                db.execute("BEGIN IMMEDIATE")
                try:
                    db.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?)", (final, "file", name, 1, None, size, digest, upload_id))
                    row = lookup(final)
                    db.execute("COMMIT")
                except BaseException:
                    db.execute("ROLLBACK")
                    raise
                final = None
                receipt = _item(row, root)
                receipt["verified"] = True
                return web.json_response(receipt)
            finally:
                for filename in (temp, final):
                    if filename:
                        try:
                            os.unlink(filename, dir_fd=dirfd)
                        except FileNotFoundError:
                            pass

    async def download(request):
        id = _uuid(request.match_info["id"])
        async with lock:
            row = lookup(id)
            if row is None or row["kind"] != "file":
                raise web.HTTPNotFound()
            try:
                fd = os.open(id, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=dirfd)
                if not stat.S_ISREG(os.fstat(fd).st_mode):
                    os.close(fd)
                    raise OSError("not a regular file")
                with os.fdopen(fd, "rb") as stream:
                    data = stream.read(MAX_FILE + 1)
            except OSError:
                raise web.HTTPNotFound()
            return web.Response(body=data, headers={"Content-Disposition": "attachment; filename*=UTF-8''" + quote(row["name"], safe=""), "X-Content-Type-Options": "nosniff"})

    async def cleanup(app):
        db.close()
        os.close(dirfd)

    app.router.add_get("/api/vault", all_items)
    app.router.add_get("/api/vault/{id}", get_item)
    app.router.add_put("/api/vault/{id}", put_item)
    app.router.add_delete("/api/vault/{id}", delete_item)
    app.router.add_post("/api/files", upload)
    app.router.add_get("/api/files/{id}", download)
    app.on_cleanup.append(cleanup)
