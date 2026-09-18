#!/usr/bin/env python3
"""Read-only qualification probe for the bounded Nablarva B-entry route.

Exit status: 0 is a static PREPARED preview; 2 is BLOCKED or any STOP result.
Labels: PREPARED, BLOCKED, STOP_IDENTITY_UNKNOWN, STOP_NOT_IDLE, and
STOP_ROUTE_UNKNOWN.  `inspect` performs only initialize, thread/list, and
thread/read over a directly connected Unix WebSocket.  It has no send command.

The required ``--allow-connect`` value is an operator interlock, not
authentication, expiry, server-instance proof, or authorization:
``nablarva-inspect-v1:<sha256(sock UTF-8 + NUL + canonical thread UUID)>``.
This module intentionally exposes no command that mints it.  Launch evidence
asserts only the supplied argv/profile fields; it cannot prove effective defaults.
No static source/destination check is an atomic admission or destination reservation.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import socket
import stat
import struct
import sys
import time
from dataclasses import dataclass
from typing import Any, Iterable, Protocol


BED = "/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification"
WORKSPACE = "/tmp/nablarva-b-entry-20260913-01"
POINT_PATH = WORKSPACE + "/qualification.point.md"
INPUT_PATH = WORKSPACE + "/qualification.input.txt"
RETURN_PATH = WORKSPACE + "/qualification.return.md"
HOST = "hruzam-120922"
PRIVATE_SOCKET = "/run/user/1000/nablarva-b-entry-20260913-01.sock"
REMOTE_URI = "unix://" + PRIVATE_SOCKET
ALLOWED_CODEX = {"codex", "/home/hruzam/.local/bin/codex"}
SERVER_ARGV_TAIL = ("app-server", "--listen", REMOTE_URI)
TARGET_ARGV_TAIL = ("--remote", REMOTE_URI, "-C", WORKSPACE)
LAUNCH_EVIDENCE_KEYS = {"server_argv", "target_argv", "inherited_profile"}
CLIENT_INFO = {"name": "nablarva_qualification_probe", "version": "0.2.0"}
SOURCE_KINDS = ["cli", "vscode", "appServer"]
CONNECT_TOKEN_PREFIX = "nablarva-inspect-v1:"
WS_DEADLINE_SECONDS = 5.0
MAX_HTTP_HEADER_BYTES = 8192
MAX_WS_FRAME_BYTES = 65536
MAX_WS_TOTAL_BYTES = 262144
MAX_WS_FRAMES = 32
MAX_FIXTURE_BYTES = 65536
MAX_INPUT_BYTES = 65536
FIXTURE_SCHEMA = "nablarva-qualification-fixture/v1"
TUPLE_SCHEMA = "nablarva-qualification-tuple/v1"
WORKING_THREADS = {
    "01a092ed-f422-7051-ba69-f6c1d47c57d8",
    "0a27e884-b106-48e6-b56a-71dcb271ab6f",
}
UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

FIXTURE_KEYS = {
    "schema", "bed", "from", "to", "scope", "done_when", "workspace",
    "thread_id", "host", "incarnation", "generation", "point_path",
    "input_path", "return_to", "input_sha256", "challenge",
}
TUPLE_KEYS = {
    "schema", "bed", "seat", "workspace", "thread_id", "host",
    "incarnation", "generation", "fixture", "fixture_sha256", "input_path",
    "input_sha256", "return_to", "challenge",
}


class Blocked(ValueError):
    """A closed validation or protocol refusal, never a partial pass."""


class PathView(Protocol):
    def lstat(self, path: str) -> Any: ...
    def read_regular(self, path: str, limit: int) -> bytes: ...


class OSPathView:
    def lstat(self, path: str) -> os.stat_result:
        return os.lstat(path)

    def read_regular(self, path: str, limit: int) -> bytes:
        nofollow = getattr(os, "O_NOFOLLOW", None)
        directory = getattr(os, "O_DIRECTORY", None)
        nonblock = getattr(os, "O_NONBLOCK", None)
        if nofollow is None or directory is None or nonblock is None:
            raise Blocked("safe no-follow directory reads are unavailable")
        parts = path.split("/")[1:]
        if not parts or any(not part for part in parts):
            raise Blocked("required file path is malformed")
        directory_flags = os.O_RDONLY | directory | nofollow | getattr(os, "O_CLOEXEC", 0)
        parent = os.open("/", directory_flags)
        try:
            for part in parts[:-1]:
                child = os.open(part, directory_flags, dir_fd=parent)
                os.close(parent)
                parent = child
            descriptor = os.open(parts[-1], os.O_RDONLY | nofollow | nonblock | getattr(os, "O_CLOEXEC", 0), dir_fd=parent)
            try:
                if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                    raise Blocked("required file changed type during read")
                chunks: list[bytes] = []
                remaining = limit + 1
                while remaining:
                    chunk = os.read(descriptor, min(8192, remaining))
                    if not chunk:
                        break
                    chunks.append(chunk)
                    remaining -= len(chunk)
                data = b"".join(chunks)
            finally:
                os.close(descriptor)
        finally:
            os.close(parent)
        if len(data) > limit:
            raise Blocked("required file exceeds byte bound")
        return data


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise Blocked("duplicate JSON key")
        result[key] = value
    return result


def _constant(value: str) -> None:
    raise Blocked("non-finite JSON number: " + value)


def strict_json(text: str) -> Any:
    try:
        value = json.loads(text, object_pairs_hook=_pairs, parse_constant=_constant)
    except Blocked:
        raise
    except (json.JSONDecodeError, UnicodeDecodeError, TypeError, ValueError, RecursionError) as error:
        raise Blocked("invalid strict JSON") from error
    stack = [(value, 0)]
    nodes = 0
    while stack:
        item, depth = stack.pop()
        nodes += 1
        if depth > 64 or nodes > 10000:
            raise Blocked("JSON structure bound exceeded")
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)
    return value


def _object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise Blocked(label + " must be a JSON object")
    return value


def _exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise Blocked(label + " has missing or unknown fields")


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise Blocked(label + " must be a nonempty string")
    return value


def _absolute(value: Any, label: str) -> str:
    path = _string(value, label)
    if not os.path.isabs(path) or os.path.normpath(path) != path:
        raise Blocked(label + " must be a normalized absolute path")
    return path


def _uuid(value: Any, label: str) -> str:
    text = _string(value, label)
    if not UUID_RE.fullmatch(text) or text == "00000000-0000-0000-0000-000000000000":
        raise Blocked(label + " must be a canonical lowercase UUID")
    return text


def _sha256(value: Any, label: str) -> str:
    text = _string(value, label)
    if not SHA256_RE.fullmatch(text):
        raise Blocked(label + " must be a lowercase SHA-256")
    return text


def _materialized(value: Any, label: str) -> str:
    text = _string(value, label)
    if "{{" in text or "}}" in text:
        raise Blocked(label + " is not materialized")
    return text


def _frontmatter(data: bytes) -> dict[str, Any]:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise Blocked("fixture is not UTF-8") from error
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise Blocked("fixture lacks JSON frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise Blocked("fixture frontmatter is unterminated") from error
    return _object(strict_json("\n".join(lines[1:end])), "fixture frontmatter")


def _ancestors(path: str) -> Iterable[str]:
    current = os.path.dirname(path)
    parts: list[str] = []
    while current and current != "/":
        parts.append(current)
        current = os.path.dirname(current)
    yield "/"
    yield from reversed(parts)


def _safe_ancestors(path: str, view: PathView) -> None:
    for ancestor in _ancestors(path):
        try:
            info = view.lstat(ancestor)
        except FileNotFoundError as error:
            raise Blocked("missing destination ancestor") from error
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
            raise Blocked("destination ancestor is not a real directory")


def _regular_file(path: str, view: PathView, limit: int) -> bytes:
    _safe_ancestors(path, view)
    try:
        info = view.lstat(path)
    except FileNotFoundError as error:
        raise Blocked("required file is absent") from error
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
        raise Blocked("required file is not a regular non-symlink")
    return view.read_regular(path, limit)


def _absent(path: str, view: PathView) -> None:
    _safe_ancestors(path, view)
    try:
        view.lstat(path)
    except FileNotFoundError:
        return
    raise Blocked("return destination already exists or is a dangling symlink")


@dataclass(frozen=True)
class Preview:
    fixture_sha256: str
    input_sha256: str
    generation: int
    thread_id: str
    return_to: str
    challenge: str
    frozen_tuple: tuple[tuple[str, Any], ...]


def validate_fixture(fixture_path: str, tuple_text: str, view: PathView | None = None) -> Preview:
    """Static validation only; source mutation and destination TOCTOU remain unqualified."""
    view = view or OSPathView()
    fixture_path = _absolute(fixture_path, "fixture")
    if fixture_path != POINT_PATH:
        raise Blocked("fixture must be the fixed scratch POINT path")
    fixture_bytes = _regular_file(fixture_path, view, MAX_FIXTURE_BYTES)
    fixture = _frontmatter(fixture_bytes)
    tuple_value = _object(strict_json(tuple_text), "tuple")
    _exact_keys(fixture, FIXTURE_KEYS, "fixture")
    _exact_keys(tuple_value, TUPLE_KEYS, "tuple")

    if fixture["schema"] != FIXTURE_SCHEMA or tuple_value["schema"] != TUPLE_SCHEMA:
        raise Blocked("unknown schema")
    if fixture["bed"] != BED or tuple_value["bed"] != BED:
        raise Blocked("wrong bed")
    if fixture["from"] != "oraculum" or fixture["to"] != "probe_codex":
        raise Blocked("wrong fixture seats")
    if tuple_value["seat"] != "probe_codex":
        raise Blocked("wrong tuple seat")
    if fixture["workspace"] != WORKSPACE or tuple_value["workspace"] != WORKSPACE:
        raise Blocked("wrong workspace")
    if fixture["host"] != HOST or tuple_value["host"] != HOST:
        raise Blocked("wrong host")
    if fixture["point_path"] != POINT_PATH or fixture["input_path"] != INPUT_PATH:
        raise Blocked("wrong fixed fixture paths")
    if fixture["return_to"] != RETURN_PATH or tuple_value["return_to"] != RETURN_PATH:
        raise Blocked("wrong return destination")
    if tuple_value["fixture"] != fixture_path:
        raise Blocked("tuple fixture path differs")
    _materialized(fixture["scope"], "scope")
    _materialized(fixture["done_when"], "done_when")
    challenge = _materialized(fixture["challenge"], "challenge")
    if not isinstance(fixture["generation"], int) or isinstance(fixture["generation"], bool) or fixture["generation"] < 0:
        raise Blocked("generation must be a nonnegative integer")
    for field in ("thread_id", "host", "incarnation"):
        left = _uuid(fixture[field], field) if field == "thread_id" else _materialized(fixture[field], field)
        right = _uuid(tuple_value[field], field) if field == "thread_id" else _materialized(tuple_value[field], field)
        if left != right:
            raise Blocked(field + " differs from tuple")
    if fixture["thread_id"] in WORKING_THREADS or fixture["thread_id"].endswith("9cea3c"):
        raise Blocked("target thread is excluded")
    if not isinstance(tuple_value["generation"], int) or isinstance(tuple_value["generation"], bool):
        raise Blocked("tuple generation must be a nonnegative integer")
    if tuple_value["generation"] != fixture["generation"]:
        raise Blocked("generation differs from tuple")
    if tuple_value["challenge"] != challenge:
        raise Blocked("challenge differs from tuple")
    input_hash = _sha256(fixture["input_sha256"], "input_sha256")
    if tuple_value["input_path"] != INPUT_PATH or tuple_value["input_sha256"] != input_hash:
        raise Blocked("tuple input differs")
    if hashlib.sha256(_regular_file(INPUT_PATH, view, MAX_INPUT_BYTES)).hexdigest() != input_hash:
        raise Blocked("input hash differs")
    fixture_hash = hashlib.sha256(fixture_bytes).hexdigest()
    if _sha256(tuple_value["fixture_sha256"], "fixture_sha256") != fixture_hash:
        raise Blocked("fixture hash differs")
    _absent(RETURN_PATH, view)
    frozen_tuple = tuple((key, tuple_value[key]) for key in sorted(tuple_value))
    return Preview(fixture_hash, input_hash, fixture["generation"], fixture["thread_id"], RETURN_PATH, challenge, frozen_tuple)


def validate_launch_evidence(text: Any) -> tuple[dict[str, Any], str]:
    """Validate supplied argv claims without inspecting configuration or process state."""
    if text is None:
        raise Blocked("launch evidence is required")
    evidence = _object(strict_json(text), "launch evidence")
    _exact_keys(evidence, LAUNCH_EVIDENCE_KEYS, "launch evidence")
    server = evidence["server_argv"]
    target = evidence["target_argv"]
    if not isinstance(server, list) or any(not isinstance(item, str) for item in server):
        raise Blocked("server_argv must be a string array")
    if not isinstance(target, list) or any(not isinstance(item, str) for item in target):
        raise Blocked("target_argv must be a string array")
    if len(server) != 4 or server[0] not in ALLOWED_CODEX or tuple(server[1:]) != SERVER_ARGV_TAIL:
        raise Blocked("server_argv differs from the canonical private-server command")
    if len(target) != 5 or target[0] not in ALLOWED_CODEX or tuple(target[1:]) != TARGET_ARGV_TAIL:
        raise Blocked("target_argv differs from the canonical target command")
    if evidence["inherited_profile"] is not None:
        raise Blocked("inherited_profile must be the supplied absent claim null")
    canonical = json.dumps(evidence, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return evidence, hashlib.sha256(canonical).hexdigest()


def semantic_read_messages(thread_id: str) -> tuple[dict[str, Any], ...]:
    """The exact bounded request sequence; each object occupies one text frame."""
    thread_id = _uuid(thread_id, "thread")
    if thread_id in WORKING_THREADS or thread_id.endswith("9cea3c"):
        raise Blocked("working-session exclusion")
    return (
        {"id": 1, "method": "initialize", "params": {"clientInfo": dict(CLIENT_INFO)}},
        {"method": "initialized", "params": {}},
        {"id": 2, "method": "thread/list", "params": {
            "cwd": WORKSPACE, "useStateDbOnly": True, "limit": 2,
            "sourceKinds": list(SOURCE_KINDS),
        }},
        {"id": 3, "method": "thread/read", "params": {"threadId": thread_id, "includeTurns": False}},
    )


def _notification_or_response(text: str, expected_id: int) -> dict[str, Any] | None:
    message = _object(strict_json(text), "response")
    if "method" in message:
        if "id" in message:
            raise Blocked("server-initiated request refused")
        if set(message) - {"method", "params"}:
            raise Blocked("notification envelope is malformed")
        _string(message["method"], "notification method")
        if "params" in message:
            _object(message["params"], "notification params")
        return None
    if type(message.get("id")) is not int:
        raise Blocked("response id is missing or invalid")
    if set(message) != {"id", "result"}:
        raise Blocked("response envelope is malformed or reports an error")
    if message["id"] != expected_id:
        raise Blocked("response id is unexpected or duplicated")
    return _object(message["result"], "response result")


class WebSocket:
    """Small RFC 6455 client: text plus bounded ping/pong, no fragmentation."""

    def __init__(self, stream: socket.socket, deadline: float) -> None:
        self.stream = stream
        self.deadline = deadline
        self.buffer = bytearray()
        self.total_bytes = 0
        self.frame_count = 0
        self.upgraded = False
        self.closed = False

    def _timeout(self) -> float:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise Blocked("WebSocket deadline exceeded")
        self.stream.settimeout(remaining)
        return remaining

    def _recv_more(self, maximum: int) -> bytes:
        self._timeout()
        try:
            chunk = self.stream.recv(maximum)
        except socket.timeout as error:
            raise Blocked("WebSocket deadline exceeded") from error
        if not chunk:
            raise Blocked("WebSocket closed unexpectedly")
        return chunk

    def _recv_exact(self, count: int) -> bytes:
        while len(self.buffer) < count:
            self.buffer.extend(self._recv_more(max(4096, count - len(self.buffer))))
        result = bytes(self.buffer[:count])
        del self.buffer[:count]
        self.total_bytes += count
        if self.total_bytes > MAX_WS_TOTAL_BYTES:
            raise Blocked("WebSocket total byte bound exceeded")
        return result

    def _sendall(self, data: bytes) -> None:
        self._timeout()
        try:
            self.stream.sendall(data)
        except socket.timeout as error:
            raise Blocked("WebSocket deadline exceeded") from error

    def handshake(self) -> None:
        key = base64.b64encode(secrets.token_bytes(16)).decode("ascii")
        request = (
            "GET / HTTP/1.1\r\nHost: localhost\r\nUpgrade: websocket\r\n"
            "Connection: Upgrade\r\nSec-WebSocket-Key: " + key +
            "\r\nSec-WebSocket-Version: 13\r\n\r\n"
        ).encode("ascii")
        self._sendall(request)
        marker = b"\r\n\r\n"
        while marker not in self.buffer:
            if len(self.buffer) >= MAX_HTTP_HEADER_BYTES:
                raise Blocked("HTTP Upgrade header bound exceeded")
            self.buffer.extend(self._recv_more(MAX_HTTP_HEADER_BYTES + 1 - len(self.buffer)))
            if len(self.buffer) > MAX_HTTP_HEADER_BYTES and marker not in self.buffer[:MAX_HTTP_HEADER_BYTES]:
                raise Blocked("HTTP Upgrade header bound exceeded")
        end = self.buffer.index(marker) + len(marker)
        if end > MAX_HTTP_HEADER_BYTES:
            raise Blocked("HTTP Upgrade header bound exceeded")
        raw = bytes(self.buffer[:end])
        del self.buffer[:end]
        try:
            lines = raw[:-4].decode("ascii").split("\r\n")
        except UnicodeDecodeError as error:
            raise Blocked("HTTP Upgrade response is not ASCII") from error
        if not lines or lines[0] != "HTTP/1.1 101 Switching Protocols":
            raise Blocked("HTTP Upgrade did not return 101")
        headers: dict[str, list[str]] = {}
        for line in lines[1:]:
            if not line or line[:1].isspace() or ":" not in line:
                raise Blocked("HTTP Upgrade header is malformed")
            name, value = line.split(":", 1)
            if not name or not re.fullmatch(r"[!#$%&'*+.^_`|~0-9A-Za-z-]+", name):
                raise Blocked("HTTP Upgrade header name is malformed")
            headers.setdefault(name.lower(), []).append(value.strip())
        if headers.get("upgrade", [""])[0].lower() != "websocket" or len(headers.get("upgrade", [])) != 1:
            raise Blocked("HTTP Upgrade response lacks websocket upgrade")
        connection = ",".join(headers.get("connection", [])).lower().split(",")
        if "upgrade" not in {token.strip() for token in connection}:
            raise Blocked("HTTP Upgrade response lacks Connection upgrade")
        accepts = headers.get("sec-websocket-accept", [])
        expected = base64.b64encode(hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")).digest()).decode("ascii")
        if len(accepts) != 1 or not hmac.compare_digest(accepts[0], expected):
            raise Blocked("WebSocket accept proof differs")
        if "sec-websocket-extensions" in headers or "sec-websocket-protocol" in headers:
            raise Blocked("WebSocket server selected an unoffered extension or subprotocol")
        self.upgraded = True

    def _send_frame(self, opcode: int, payload: bytes) -> None:
        if len(payload) > MAX_WS_FRAME_BYTES or (opcode & 0x8 and len(payload) > 125):
            raise Blocked("outgoing WebSocket frame bound exceeded")
        first = 0x80 | opcode
        length = len(payload)
        if length < 126:
            header = bytes((first, 0x80 | length))
        elif length <= 0xFFFF:
            header = bytes((first, 0x80 | 126)) + struct.pack("!H", length)
        else:
            header = bytes((first, 0x80 | 127)) + struct.pack("!Q", length)
        mask = secrets.token_bytes(4)
        masked = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
        self._sendall(header + mask + masked)

    def send_json(self, value: dict[str, Any]) -> None:
        payload = json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        self._send_frame(0x1, payload)

    def recv_text(self) -> str:
        while True:
            self.frame_count += 1
            if self.frame_count > MAX_WS_FRAMES:
                raise Blocked("WebSocket frame count bound exceeded")
            first, second = self._recv_exact(2)
            if first & 0x70 or not first & 0x80:
                raise Blocked("WebSocket RSV or fragmentation is unsupported")
            opcode = first & 0x0F
            if second & 0x80:
                raise Blocked("masked server WebSocket frame refused")
            length = second & 0x7F
            if length == 126:
                length = struct.unpack("!H", self._recv_exact(2))[0]
                if length < 126:
                    raise Blocked("non-canonical WebSocket length")
            elif length == 127:
                encoded = self._recv_exact(8)
                if encoded[0] & 0x80:
                    raise Blocked("invalid WebSocket 64-bit length")
                length = struct.unpack("!Q", encoded)[0]
                if length < 65536:
                    raise Blocked("non-canonical WebSocket length")
            if length > MAX_WS_FRAME_BYTES or (opcode & 0x8 and length > 125):
                raise Blocked("WebSocket frame byte bound exceeded")
            payload = self._recv_exact(length)
            if opcode == 0x9:
                self._send_frame(0xA, payload)
                continue
            if opcode == 0xA:
                continue
            if opcode == 0x8:
                if len(payload) == 1:
                    raise Blocked("malformed WebSocket close frame")
                if payload:
                    code = struct.unpack("!H", payload[:2])[0]
                    if code < 1000 or code in {1004, 1005, 1006, 1015} or code >= 5000:
                        raise Blocked("invalid WebSocket close code")
                    try:
                        payload[2:].decode("utf-8")
                    except UnicodeDecodeError as error:
                        raise Blocked("WebSocket close reason is not UTF-8") from error
                raise Blocked("WebSocket server closed the bounded read")
            if opcode != 0x1:
                raise Blocked("unsupported WebSocket opcode")
            try:
                return payload.decode("utf-8")
            except UnicodeDecodeError as error:
                raise Blocked("WebSocket text frame is not UTF-8") from error

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            if self.upgraded and time.monotonic() < self.deadline:
                self._send_frame(0x8, struct.pack("!H", 1000))
        except (Blocked, OSError):
            pass
        finally:
            self.stream.close()


def _rpc_response(ws: WebSocket, expected_id: int) -> dict[str, Any]:
    while True:
        result = _notification_or_response(ws.recv_text(), expected_id)
        if result is not None:
            return result


def _server_version(initialize: dict[str, Any]) -> str | None:
    server_info = initialize.get("serverInfo")
    if server_info is None:
        return None
    server_info = _object(server_info, "initialize serverInfo")
    version = server_info.get("version")
    if version is None:
        return None
    return _string(version, "initialize server version")


def _unsafe_effective_hint(value: Any, key: str = "") -> None:
    normalized = re.sub(r"[^a-z0-9]", "", key.lower())
    if normalized == "activeflags" and isinstance(value, str) and any(
        marker in re.sub(r"[^a-z0-9]", "", value.lower())
        for marker in ("dangerously", "approveforme", "override")
    ):
        raise Blocked("unsafe active flag reported")
    if normalized.startswith("dangerously") and value not in (None, False, "", [], {}):
        raise Blocked("unsafe effective setting reported")
    if normalized in {"approveforme", "override", "overrides", "profile"} and value not in (None, False, "", [], {}):
        raise Blocked("override setting reported")
    if normalized in {"approvalpolicy", "askforapproval"} and isinstance(value, str) and value.lower() == "never":
        raise Blocked("unsafe approval setting reported")
    if normalized in {"sandbox", "sandboxpolicy", "sandboxmode"} and isinstance(value, str) and value.lower() in {
        "danger-full-access", "dangerously-bypass-approvals-and-sandbox",
    }:
        raise Blocked("unsafe sandbox setting reported")
    if isinstance(value, dict):
        for child_key, child in value.items():
            _unsafe_effective_hint(child, str(child_key))
    elif isinstance(value, list):
        for child in value:
            _unsafe_effective_hint(child, key)


def _parse_list(result: dict[str, Any], thread_id: str) -> None:
    _exact_keys(result, {"data", "nextCursor"}, "thread/list result")
    if result["nextCursor"] is not None:
        raise Blocked("thread/list pagination refused")
    data = result["data"]
    if not isinstance(data, list) or len(data) != 1:
        raise Blocked("thread/list must return exactly one thread")
    listed = _object(data[0], "thread/list item")
    if listed.get("id") != thread_id or listed.get("cwd") != WORKSPACE:
        raise Blocked("thread/list did not return the exact requested thread and cwd")


def _parse_read(result: dict[str, Any], thread_id: str) -> dict[str, Any]:
    _exact_keys(result, {"thread"}, "thread/read result")
    thread = _object(result["thread"], "thread/read thread")
    if thread.get("id") != thread_id or thread.get("cwd") != WORKSPACE:
        raise Blocked("thread/read returned another thread or cwd")
    _unsafe_effective_hint(thread)
    return thread


def read_unix_websocket(
    sock_path: str, thread_id: str, expected_identity: tuple[int, int, int] | None = None,
) -> tuple[dict[str, Any], str | None]:
    """Direct lower-level client used by inspect and test-owned Unix loopbacks."""
    thread_id = _uuid(thread_id, "thread")
    messages = semantic_read_messages(thread_id)
    deadline = time.monotonic() + WS_DEADLINE_SECONDS
    stream = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    ws = WebSocket(stream, deadline)
    try:
        ws._timeout()
        stream.connect(sock_path)
        if expected_identity is not None:
            if _socket_identity(sock_path) != expected_identity:
                raise Blocked("private socket identity changed while connecting")
            _peer_same_user(stream)
        ws.handshake()
        ws.send_json(messages[0])
        initialized = _rpc_response(ws, 1)
        version = _server_version(initialized)
        ws.send_json(messages[1])
        ws.send_json(messages[2])
        _parse_list(_rpc_response(ws, 2), thread_id)
        ws.send_json(messages[3])
        thread = _parse_read(_rpc_response(ws, 3), thread_id)
        return thread, version
    finally:
        ws.close()


def classify_read(
    thread: dict[str, Any], thread_id: str, sock: str, *,
    evidence: str = "offline_mock", version: str | None = None,
) -> dict[str, Any]:
    """A read summary cannot prove a living TUI incarnation."""
    thread_id = _uuid(thread_id, "thread")
    if thread.get("id") != thread_id:
        raise Blocked("thread summary id differs")
    if thread.get("cwd") != WORKSPACE:
        raise Blocked("thread summary cwd differs")
    status = _object(thread.get("status"), "thread status")
    status_type = status.get("type")
    if not isinstance(status_type, str) or status_type not in {"idle", "active", "notLoaded", "systemError"}:
        raise Blocked("thread status type is malformed")
    flags = status.get("activeFlags")
    if status_type == "active" and flags is None:
        raise Blocked("activeFlags are absent")
    expected_status_keys = {"type", "activeFlags"} if status_type == "active" else {"type"}
    _exact_keys(status, expected_status_keys, "thread status")
    if flags is not None and (not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags)):
        raise Blocked("activeFlags are malformed")
    updated_at = thread.get("updatedAt")
    if updated_at is not None and (not isinstance(updated_at, int) or isinstance(updated_at, bool)):
        raise Blocked("updatedAt is malformed")
    session_id = thread.get("sessionId")
    if session_id is not None and not isinstance(session_id, str):
        raise Blocked("sessionId is malformed")
    _unsafe_effective_hint(thread)
    base = {
        "native": "UNVERIFIED-native",
        "native_incarnation": "unknown",
        "effective_settings": "unknown",
        "evidence": evidence,
        "read_route_observed": evidence == "unix_ws_read",
        "route": {"sock": sock, "version": version},
        "id": thread_id,
        "sessionId": session_id,
        "cwd": WORKSPACE,
        "status": status_type,
        "activeFlags": flags,
        "updatedAt": updated_at,
    }
    if status_type == "active":
        return {**base, "label": "STOP_NOT_IDLE", "reason": "active summary"}
    if status_type == "idle":
        return {**base, "label": "STOP_IDENTITY_UNKNOWN", "reason": "summary does not fence a living TUI incarnation"}
    return {**base, "label": "STOP_ROUTE_UNKNOWN", "reason": "unknown or unavailable thread state"}


def _connect_token_matches(sock: str, thread_id: str, supplied: Any) -> bool:
    if not isinstance(supplied, str) or not re.fullmatch(r"nablarva-inspect-v1:[0-9a-f]{64}", supplied):
        return False
    digest = hashlib.sha256(sock.encode("utf-8") + b"\0" + thread_id.encode("ascii")).hexdigest()
    return hmac.compare_digest(supplied, CONNECT_TOKEN_PREFIX + digest)


def _socket_identity(sock: str) -> tuple[int, int, int]:
    _safe_ancestors(sock, OSPathView())
    try:
        info = os.lstat(sock)
    except FileNotFoundError as error:
        raise Blocked("private socket is absent") from error
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISSOCK(info.st_mode):
        raise Blocked("private socket path is not a Unix socket")
    if info.st_uid != os.getuid():
        raise Blocked("private socket owner differs from current user")
    return info.st_dev, info.st_ino, info.st_uid


def _peer_same_user(stream: socket.socket) -> None:
    peercred = getattr(socket, "SO_PEERCRED", None)
    if peercred is None:
        return
    try:
        raw = stream.getsockopt(socket.SOL_SOCKET, peercred, struct.calcsize("3i"))
        _, uid, _ = struct.unpack("3i", raw)
    except (OSError, struct.error):
        return
    if uid != os.getuid():
        raise Blocked("Unix peer owner differs from current user")


def inspect_bounded(sock: str, thread_id: str, allow_connect: Any) -> dict[str, Any]:
    """Validate the fixed endpoint and run the lower-level bounded read exactly once."""
    sock = _absolute(sock, "sock")
    thread_id = _uuid(thread_id, "thread")
    if sock != PRIVATE_SOCKET:
        raise Blocked("inspect socket differs from the fixed private path")
    if thread_id in WORKING_THREADS or thread_id.endswith("9cea3c"):
        raise Blocked("working-session exclusion")
    if not _connect_token_matches(sock, thread_id, allow_connect):
        raise Blocked("connect interlock is missing or invalid")
    if socket.gethostname() != HOST:
        raise Blocked("inspect host differs from the expected host")
    before = _socket_identity(sock)
    thread, version = read_unix_websocket(sock, thread_id, before)
    after = _socket_identity(sock)
    if before != after:
        raise Blocked("private socket identity changed during read")
    return classify_read(thread, thread_id, sock, evidence="unix_ws_read", version=version)


class OfflineAttemptFence:
    """Test-only admission model; it is not a carrier and has no CLI route."""

    def __init__(self, restarted: bool = False) -> None:
        self.restarted = restarted
        self.used = False

    def attempt(self, generation: int, observed_generation: int, preview_state: str, submit_state: str, mock_carrier: Any) -> str:
        if self.restarted:
            return "UNRECONCILED"
        if self.used or generation != observed_generation or preview_state != "idle" or submit_state != "idle":
            return "BLOCKED"
        self.used = True
        mock_carrier()
        return "MOCK_SUBMITTED_UNVERIFIED-native"


def _emit(value: dict[str, Any], exit_code: int) -> int:
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    command = parser.add_subparsers(dest="command", required=True)
    inspect = command.add_parser("inspect", help="bounded read from the fixed private Unix WebSocket")
    inspect.add_argument("--sock", required=True)
    inspect.add_argument("--thread", required=True)
    inspect.add_argument("--allow-connect")
    inspect.add_argument("--launch-evidence")
    validate = command.add_parser("validate", help="static fixture preview only")
    validate.add_argument("--fixture", required=True)
    validate.add_argument("--tuple", required=True)
    validate.add_argument("--launch-evidence")
    args = parser.parse_args(argv)
    try:
        _, evidence_hash = validate_launch_evidence(args.launch_evidence)
        if args.command == "inspect":
            return _emit(inspect_bounded(args.sock, args.thread, args.allow_connect), 2)
        preview = validate_fixture(args.fixture, args.tuple)
        output = {
            "fixture_sha256": preview.fixture_sha256,
            "input_sha256": preview.input_sha256,
            "generation": preview.generation,
            "thread_id": preview.thread_id,
            "return_to": preview.return_to,
            "challenge": preview.challenge,
            "frozen_tuple": dict(preview.frozen_tuple),
            "launch_evidence_sha256": evidence_hash,
        }
        return _emit({"label": "PREPARED", "native": "UNVERIFIED-native", "preview": output}, 0)
    except Blocked as error:
        return _emit({"label": "BLOCKED", "native": "UNVERIFIED-native", "reason": str(error)}, 2)
    except OSError:
        return _emit({
            "label": "BLOCKED", "native": "UNVERIFIED-native",
            "reason": "transport or filesystem operation failed",
        }, 2)


if __name__ == "__main__":
    raise SystemExit(main())
