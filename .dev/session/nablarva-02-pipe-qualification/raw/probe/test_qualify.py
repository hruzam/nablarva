"""Offline tests; the only connection is a fake server in a test-owned /tmp directory."""

import base64
import hashlib
import io
import json
import os
import socket
import stat
import struct
import sys
import tempfile
import threading
import time
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace

sys.dont_write_bytecode = True
import qualify


TARGET = "12345678-1234-1234-1234-123456789abc"


def launch_evidence(executable="codex"):
    return {
        "server_argv": [executable, *qualify.SERVER_ARGV_TAIL],
        "target_argv": [executable, *qualify.TARGET_ARGV_TAIL],
        "inherited_profile": None,
    }


class MemoryPaths:
    def __init__(self):
        self.nodes = {"/": (stat.S_IFDIR, b"")}

    def add_dir(self, path):
        current = ""
        for part in path.split("/")[1:]:
            current += "/" + part
            self.nodes.setdefault(current, (stat.S_IFDIR, b""))

    def add_file(self, path, data):
        self.add_dir(path.rsplit("/", 1)[0])
        self.nodes[path] = (stat.S_IFREG, data)

    def add_link(self, path):
        self.add_dir(path.rsplit("/", 1)[0])
        self.nodes[path] = (stat.S_IFLNK, b"")

    def lstat(self, path):
        if path not in self.nodes:
            raise FileNotFoundError(path)
        return SimpleNamespace(st_mode=self.nodes[path][0])

    def read_regular(self, path, limit):
        data = self.nodes[path][1]
        if len(data) > limit:
            raise qualify.Blocked("required file exceeds byte bound")
        return data


def blocked(action):
    try:
        action()
    except qualify.Blocked as error:
        return str(error)
    raise AssertionError("expected BLOCKED")


def case():
    fs = MemoryPaths()
    input_bytes = b"synthetic input\n"
    fs.add_file(qualify.INPUT_PATH, input_bytes)
    fixture = {
        "schema": qualify.FIXTURE_SCHEMA,
        "bed": qualify.BED,
        "from": "oraculum",
        "to": "probe_codex",
        "scope": "read fixture and synthetic input only",
        "done_when": "one exact return is written only after a matching challenge",
        "workspace": qualify.WORKSPACE,
        "thread_id": "12345678-1234-1234-1234-123456789abc",
        "host": qualify.HOST,
        "incarnation": "disposable-1",
        "generation": 3,
        "point_path": qualify.POINT_PATH,
        "input_path": qualify.INPUT_PATH,
        "return_to": qualify.RETURN_PATH,
        "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "challenge": "challenge-01",
    }
    fixture_path = qualify.POINT_PATH
    fixture_bytes = ("---\n" + json.dumps(fixture, sort_keys=True) + "\n---\nbody\n").encode()
    fs.add_file(fixture_path, fixture_bytes)
    tuple_value = {
        "schema": qualify.TUPLE_SCHEMA,
        "bed": qualify.BED,
        "seat": "probe_codex",
        "workspace": qualify.WORKSPACE,
        "thread_id": fixture["thread_id"],
        "host": fixture["host"],
        "incarnation": fixture["incarnation"],
        "generation": fixture["generation"],
        "fixture": fixture_path,
        "fixture_sha256": hashlib.sha256(fixture_bytes).hexdigest(),
        "input_path": qualify.INPUT_PATH,
        "input_sha256": fixture["input_sha256"],
        "return_to": qualify.RETURN_PATH,
        "challenge": fixture["challenge"],
    }
    return fs, fixture_path, fixture, tuple_value


def repack(fs, path, fixture, tuple_value):
    data = ("---\n" + json.dumps(fixture, sort_keys=True) + "\n---\nbody\n").encode()
    fs.add_file(path, data)
    tuple_value["fixture_sha256"] = hashlib.sha256(data).hexdigest()


def matching_fixture_blocked(field, value):
    fs, path, fixture, tuple_value = case()
    fixture[field] = value
    tuple_value[field] = value
    repack(fs, path, fixture, tuple_value)
    blocked(lambda: qualify.validate_fixture(path, json.dumps(tuple_value), fs))


def test_validator_refusals():
    fs, path, fixture, tuple_value = case()
    calls = []
    preview = qualify.validate_fixture(path, json.dumps(tuple_value), fs)
    assert preview.generation == 3 and preview.input_sha256 == fixture["input_sha256"] and dict(preview.frozen_tuple) == tuple_value
    try:
        preview.frozen_tuple[0] = ("bad", "bad")
    except TypeError:
        pass
    else:
        raise AssertionError("frozen tuple was mutable")
    for field, value in (("bed", "/wrong"), ("seat", "cartan"), ("return_to", "/tmp/wrong"), ("thread_id", "not-a-uuid")):
        changed = dict(tuple_value)
        changed[field] = value
        blocked(lambda changed=changed: qualify.validate_fixture(path, json.dumps(changed), fs))
    named = dict(tuple_value)
    named["name"] = "same-name-collision"
    blocked(lambda: qualify.validate_fixture(path, json.dumps(named), fs))
    duplicate = json.dumps(tuple_value)[:-1] + ',"bed":"/duplicate"}'
    blocked(lambda: qualify.validate_fixture(path, duplicate, fs))
    blocked(lambda: qualify.validate_fixture("/tmp/escape/qualification.point.md", json.dumps(tuple_value), fs))
    stale = dict(tuple_value)
    stale["generation"] += 1
    blocked(lambda: qualify.validate_fixture(path, json.dumps(stale), fs))
    fs.add_link(qualify.RETURN_PATH)
    blocked(lambda: qualify.validate_fixture(path, json.dumps(tuple_value), fs))
    escaped, escaped_path, _, escaped_tuple = case()
    escaped.add_link(qualify.WORKSPACE)
    blocked(lambda: qualify.validate_fixture(escaped_path, json.dumps(escaped_tuple), escaped))
    matching_fixture_blocked("host", "other-host")
    matching_fixture_blocked("thread_id", "00000000-0000-0000-0000-000000000000")
    for working_thread in qualify.WORKING_THREADS:
        matching_fixture_blocked("thread_id", working_thread)
    matching_fixture_blocked("thread_id", "01a092ed-f422-7051-ba69-f600009cea3c")
    for generation in (True, 3.5, -1):
        matching_fixture_blocked("generation", generation)
    fresh, fresh_path, fresh_fixture, fresh_tuple = case()
    changed_fixture = dict(fixture)
    changed_fixture["challenge"] = "{{CHALLENGE}}"
    changed_tuple = dict(tuple_value)
    changed_tuple["challenge"] = "{{CHALLENGE}}"
    repack(fresh, fresh_path, changed_fixture, changed_tuple)
    blocked(lambda: qualify.validate_fixture(fresh_path, json.dumps(changed_tuple), fresh))
    for field in ("scope", "done_when"):
        fresh, fresh_path, fresh_fixture, fresh_tuple = case()
        fresh_fixture[field] = "{{PLACEHOLDER}}"
        repack(fresh, fresh_path, fresh_fixture, fresh_tuple)
        blocked(lambda fresh=fresh, fresh_path=fresh_path, fresh_tuple=fresh_tuple: qualify.validate_fixture(fresh_path, json.dumps(fresh_tuple), fresh))
    fresh, fresh_path, fresh_fixture, fresh_tuple = case()
    bad_hash = dict(tuple_value)
    bad_hash["input_sha256"] = "0" * 64
    blocked(lambda: qualify.validate_fixture(fresh_path, json.dumps(bad_hash), fresh))
    for field, value in (("point_path", "/tmp/escape"), ("input_path", "/tmp/escape"), ("return_to", "/tmp/escape")):
        fresh, fresh_path, fresh_fixture, fresh_tuple = case()
        fresh_fixture[field] = value
        if field in fresh_tuple:
            fresh_tuple[field] = value
        repack(fresh, fresh_path, fresh_fixture, fresh_tuple)
        blocked(lambda fresh=fresh, fresh_path=fresh_path, fresh_tuple=fresh_tuple: qualify.validate_fixture(fresh_path, json.dumps(fresh_tuple), fresh))
    fresh, fresh_path, _, fresh_tuple = case()
    fresh.add_file(fresh_path, b'---\n{"schema":"x","schema":"x"}\n---\n')
    blocked(lambda: qualify.validate_fixture(fresh_path, json.dumps(fresh_tuple), fresh))
    oversized, oversized_path, _, oversized_tuple = case()
    oversized.add_file(qualify.INPUT_PATH, b"x" * (qualify.MAX_INPUT_BYTES + 1))
    blocked(lambda: qualify.validate_fixture(oversized_path, json.dumps(oversized_tuple), oversized))
    oversized, oversized_path, _, oversized_tuple = case()
    oversized.add_file(oversized_path, b"x" * (qualify.MAX_FIXTURE_BYTES + 1))
    blocked(lambda: qualify.validate_fixture(oversized_path, json.dumps(oversized_tuple), oversized))
    assert "mock_carrier" not in qualify.validate_fixture.__code__.co_names and not calls
    print("PASS offline_mock validator-refusals UNVERIFIED-native")


def test_offline_admission_fence():
    calls = []
    fence = qualify.OfflineAttemptFence()
    carrier = lambda: calls.append("mock")
    assert fence.attempt(3, 3, "idle", "idle", carrier) == "MOCK_SUBMITTED_UNVERIFIED-native"
    assert fence.attempt(3, 3, "idle", "idle", carrier) == "BLOCKED"
    assert calls == ["mock"]
    assert qualify.OfflineAttemptFence(restarted=True).attempt(3, 3, "idle", "idle", carrier) == "UNRECONCILED"
    race = qualify.OfflineAttemptFence()
    assert race.attempt(3, 3, "idle", "active", carrier) == "BLOCKED"
    assert calls == ["mock"]
    print("PASS offline_mock admission-fence UNVERIFIED-native")


def test_read_semantics_are_gated():
    messages = qualify.semantic_read_messages(TARGET)
    assert [message["method"] for message in messages] == ["initialize", "initialized", "thread/list", "thread/read"]
    assert all("jsonrpc" not in message for message in messages)
    assert messages[0]["params"]["clientInfo"] == {"name": "nablarva_qualification_probe", "version": "0.2.0"}
    assert messages[2]["params"] == {
        "cwd": qualify.WORKSPACE, "useStateDbOnly": True, "limit": 2,
        "sourceKinds": ["cli", "vscode", "appServer"],
    }
    assert messages[3]["params"] == {"threadId": TARGET, "includeTurns": False}
    qualify._parse_list({"data": [{"id": TARGET, "cwd": qualify.WORKSPACE}], "nextCursor": None}, TARGET)
    thread = qualify._parse_read({"thread": {
        "id": TARGET, "sessionId": "session-1", "cwd": qualify.WORKSPACE,
        "status": {"type": "idle"}, "updatedAt": 1,
    }}, TARGET)
    result = qualify.classify_read(thread, TARGET, "/tmp/test-owned.sock")
    assert result["label"] == "STOP_IDENTITY_UNKNOWN" and result["evidence"] == "offline_mock"
    assert not result["read_route_observed"] and result["id"] == TARGET and result["cwd"] == qualify.WORKSPACE
    assert qualify._notification_or_response('{"method":"thread/updated","params":{"hidden":"discarded"}}', 1) is None
    for malformed in (
        {"id": 9, "method": "approve", "params": {}},
        {"method": 3}, {"method": "notice", "result": {}},
        {"method": "notice", "params": []}, {"id": True, "result": {}},
        {"id": 1, "result": {}, "extra": True}, {"id": 2, "result": {}},
        {"id": 1, "error": {"message": "must not print"}},
    ):
        blocked(lambda malformed=malformed: qualify._notification_or_response(json.dumps(malformed), 1))
    for bad_list in (
        {"data": [], "nextCursor": None},
        {"data": [{"id": TARGET, "cwd": qualify.WORKSPACE}], "nextCursor": "more"},
        {"data": [{"id": "other", "cwd": qualify.WORKSPACE}], "nextCursor": None},
        {"data": [{"id": TARGET, "cwd": "/other"}], "nextCursor": None},
        {"data": [{"id": TARGET, "cwd": qualify.WORKSPACE}], "nextCursor": None, "extra": True},
    ):
        blocked(lambda bad_list=bad_list: qualify._parse_list(bad_list, TARGET))
    for unsafe in (
        {"settings": {"approvalPolicy": "never"}},
        {"settings": {"sandbox": "danger-full-access"}},
        {"settings": {"dangerouslyBypass": True}},
        {"settings": {"profile": "unsafe"}},
        {"status": {"type": "active", "activeFlags": ["dangerouslyBypass"]}},
    ):
        candidate = {"id": TARGET, "cwd": qualify.WORKSPACE, "status": {"type": "idle"}, **unsafe}
        blocked(lambda candidate=candidate: qualify._parse_read({"thread": candidate}, TARGET))
    for working_thread in qualify.WORKING_THREADS:
        blocked(lambda working_thread=working_thread: qualify.semantic_read_messages(working_thread))
    blocked(lambda: qualify.semantic_read_messages("01a092ed-f422-7051-ba69-f600009cea3c"))
    for kind in ("idle", "notLoaded", "systemError"):
        assert "thread status" in blocked(lambda kind=kind: qualify.classify_read(
            {"id": TARGET, "cwd": qualify.WORKSPACE, "status": {"type": kind, "activeFlags": []}},
            TARGET, "/tmp/test-owned.sock"))
    active = qualify.classify_read({
        "id": TARGET, "cwd": qualify.WORKSPACE,
        "status": {"type": "active", "activeFlags": ["waitingOnApproval"]},
    }, TARGET, "/tmp/test-owned.sock")
    assert active["label"] == "STOP_NOT_IDLE" and active["activeFlags"] == ["waitingOnApproval"]
    print("PASS offline_mock read-gated UNVERIFIED-native")


def test_cli_has_no_carrier_path():
    fs, fixture_path, _, tuple_value = case()
    calls = []
    original_view = qualify.OSPathView
    original_attempt = qualify.OfflineAttemptFence.attempt
    original_socket = qualify.socket.socket

    def forbidden_attempt(*args, **kwargs):
        calls.append("unexpected carrier path")
        raise AssertionError("read-only CLI reached attempt model")

    try:
        qualify.OSPathView = lambda: fs
        qualify.OfflineAttemptFence.attempt = forbidden_attempt
        qualify.socket.socket = lambda *args, **kwargs: calls.append("socket constructor")
        evidence_text = json.dumps(launch_evidence())
        for target in sorted(qualify.WORKING_THREADS) + [tuple_value["thread_id"]]:
            output = io.StringIO()
            with redirect_stdout(output):
                args = ["inspect", "--sock", qualify.PRIVATE_SOCKET, "--thread", target,
                        "--launch-evidence", evidence_text]
                if target == tuple_value["thread_id"]:
                    args.extend(["--allow-connect", "invalid"])
                code = qualify.main(args)
            assert code == 2 and json.loads(output.getvalue())["label"] == "BLOCKED"
        output = io.StringIO()
        with redirect_stdout(output):
            code = qualify.main(["inspect", "--sock", qualify.PRIVATE_SOCKET,
                                 "--thread", tuple_value["thread_id"], "--allow-connect", "é",
                                 "--launch-evidence", evidence_text])
        assert code == 2 and json.loads(output.getvalue())["label"] == "BLOCKED"
        output = io.StringIO()
        with redirect_stdout(output):
            code = qualify.main(["inspect", "--sock", qualify.PRIVATE_SOCKET,
                                 "--thread", tuple_value["thread_id"], "--launch-evidence", evidence_text])
        assert code == 2 and json.loads(output.getvalue())["label"] == "BLOCKED"
        output = io.StringIO()
        with redirect_stdout(output):
            code = qualify.main(["validate", "--fixture", "/does/not/matter", "--tuple", "{}"])
        assert code == 2 and json.loads(output.getvalue())["reason"] == "launch evidence is required"
        output = io.StringIO()
        secret = "DO_NOT_ECHO_THIS_KEY"
        with redirect_stdout(output):
            code = qualify.main(["validate", "--fixture", "/does/not/matter", "--tuple", "{}",
                                 "--launch-evidence", '{"' + secret + '":1,"' + secret + '":2}'])
        assert code == 2 and secret not in output.getvalue()
        output = io.StringIO()
        with redirect_stdout(output):
            code = qualify.main(["validate", "--fixture", fixture_path, "--tuple", json.dumps(tuple_value),
                                 "--launch-evidence", evidence_text])
        result = json.loads(output.getvalue())
        assert code == 0 and result["label"] == "PREPARED"
        assert result["preview"]["frozen_tuple"] == tuple_value
        assert len(result["preview"]["launch_evidence_sha256"]) == 64
        with redirect_stderr(io.StringIO()):
            try:
                qualify.main(["send", "--armed", "not-an-approval"])
            except SystemExit as error:
                assert error.code == 2
            else:
                raise AssertionError("send verb unexpectedly exists")
        assert calls == []
    finally:
        qualify.OSPathView = original_view
        qualify.OfflineAttemptFence.attempt = original_attempt
        qualify.socket.socket = original_socket
    print("PASS offline_mock cli-no-carrier UNVERIFIED-native")


def test_launch_evidence_refusals():
    for executable in sorted(qualify.ALLOWED_CODEX):
        evidence, digest = qualify.validate_launch_evidence(json.dumps(launch_evidence(executable)))
        assert evidence["inherited_profile"] is None and len(digest) == 64
    blocked(lambda: qualify.validate_launch_evidence(None))
    for bad in (
        {"server_argv": ["codex", *qualify.SERVER_ARGV_TAIL], "target_argv": ["codex", *qualify.TARGET_ARGV_TAIL]},
        {**launch_evidence(), "unknown": True},
        {**launch_evidence(), "inherited_profile": "default"},
        {**launch_evidence(), "inherited_profile": {}},
        {**launch_evidence(), "server_argv": ["/other/codex", *qualify.SERVER_ARGV_TAIL]},
    ):
        blocked(lambda bad=bad: qualify.validate_launch_evidence(json.dumps(bad)))
    extras = (
        ["--dangerously-bypass-approvals-and-sandbox"], ["--approve-for-me"],
        ["--model", "x"], ["--model=x"], ["-m", "x"], ["-mx"],
        ["--profile", "x"], ["--profile=x"], ["-p", "x"], ["-px"],
        ["--config", "x=y"], ["--config=x=y"], ["-c", "x=y"], ["-cx=y"],
        ["--ask-for-approval", "never"], ["--ask-for-approval=never"], ["-a", "never"], ["-anever"],
        ["--feature-enable", "x"], ["--feature-enable=x"],
        ["--sandbox", "danger-full-access"], ["--sandbox=danger-full-access"],
        ["--provider", "x"], ["--provider=x"],
    )
    for extra in extras:
        evidence = launch_evidence()
        evidence["target_argv"].extend(extra)
        blocked(lambda evidence=evidence: qualify.validate_launch_evidence(json.dumps(evidence)))
    duplicate = json.dumps(launch_evidence())[:-1] + ',"inherited_profile":null}'
    blocked(lambda: qualify.validate_launch_evidence(duplicate))
    secret = "DO_NOT_ECHO_THIS_KEY"
    message = blocked(lambda: qualify.strict_json('{"' + secret + '":1,"' + secret + '":2}'))
    assert secret not in message
    deeply_nested = "[" * 2000 + "]" * 2000
    blocked(lambda: qualify.strict_json(deeply_nested))
    print("PASS offline_mock launch-evidence-refusals UNVERIFIED-native")


def recv_exact(stream, count):
    chunks = []
    remaining = count
    while remaining:
        chunk = stream.recv(remaining)
        if not chunk:
            raise AssertionError("fake peer closed early")
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def recv_client_frame(stream):
    first, second = recv_exact(stream, 2)
    assert first & 0x80 and second & 0x80
    length = second & 0x7F
    if length == 126:
        length = struct.unpack("!H", recv_exact(stream, 2))[0]
    elif length == 127:
        length = struct.unpack("!Q", recv_exact(stream, 8))[0]
    mask = recv_exact(stream, 4)
    payload = recv_exact(stream, length)
    return first & 0x0F, bytes(value ^ mask[index % 4] for index, value in enumerate(payload))


def server_frame(payload, opcode=1, fin=True, masked=False):
    if isinstance(payload, str):
        payload = payload.encode("utf-8")
    first = (0x80 if fin else 0) | opcode
    length = len(payload)
    mask_bit = 0x80 if masked else 0
    if length < 126:
        header = bytes((first, mask_bit | length))
    elif length <= 0xFFFF:
        header = bytes((first, mask_bit | 126)) + struct.pack("!H", length)
    else:
        header = bytes((first, mask_bit | 127)) + struct.pack("!Q", length)
    if not masked:
        return header + payload
    mask = b"mask"
    encoded = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
    return header + mask + encoded


def test_fake_unix_websocket_roundtrip():
    owned_dir = tempfile.mkdtemp(prefix="nablarva-qualify-test-", dir="/tmp")
    owned_sock = os.path.join(owned_dir, "fake.sock")
    listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    errors = []
    worker = None

    def serve():
        try:
            connection, _ = listener.accept()
            with connection:
                connection.settimeout(2)
                header = bytearray()
                while b"\r\n\r\n" not in header:
                    chunk = connection.recv(17)
                    if not chunk:
                        raise AssertionError("fake client closed during HTTP Upgrade")
                    header.extend(chunk)
                    if len(header) > qualify.MAX_HTTP_HEADER_BYTES:
                        raise AssertionError("fake client Upgrade header exceeded bound")
                lines = bytes(header).decode("ascii").split("\r\n")
                key = next(line.split(":", 1)[1].strip() for line in lines if line.lower().startswith("sec-websocket-key:"))
                accept = base64.b64encode(hashlib.sha1(
                    (key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")
                ).digest()).decode("ascii")
                early_notice = server_frame('{"method":"server/ready","params":{}}')
                connection.sendall((
                    "HTTP/1.1 101 Switching Protocols\r\nuPgRaDe: WebSocket\r\n"
                    "cOnNeCtIoN: keep-alive, Upgrade\r\nSec-WebSocket-Accept: " + accept + "\r\n\r\n"
                ).encode("ascii") + early_notice)
                opcode, payload = recv_client_frame(connection)
                assert opcode == 1 and json.loads(payload) == qualify.semantic_read_messages(TARGET)[0]
                connection.sendall(server_frame('{"id":1,"result":{"serverInfo":{"version":"fake-1"}}}'))
                opcode, payload = recv_client_frame(connection)
                assert opcode == 1 and json.loads(payload) == qualify.semantic_read_messages(TARGET)[1]
                opcode, payload = recv_client_frame(connection)
                assert opcode == 1 and json.loads(payload) == qualify.semantic_read_messages(TARGET)[2]
                listed = json.dumps({"id": 2, "result": {"data": [
                    {"id": TARGET, "cwd": qualify.WORKSPACE, "ignored": "not output"},
                ], "nextCursor": None}})
                connection.sendall(server_frame(b"ping", opcode=9) + server_frame(
                    '{"method":"thread/updated","params":{"private":"discarded"}}') + server_frame(listed))
                opcode, payload = recv_client_frame(connection)
                assert opcode == 10 and payload == b"ping"
                opcode, payload = recv_client_frame(connection)
                assert opcode == 1 and json.loads(payload) == qualify.semantic_read_messages(TARGET)[3]
                read = json.dumps({"id": 3, "result": {"thread": {
                    "id": TARGET, "sessionId": "fake-session", "cwd": qualify.WORKSPACE,
                    "status": {"type": "idle"}, "updatedAt": 7, "private": "not output",
                }}})
                connection.sendall(server_frame(read))
        except BaseException as error:
            errors.append(error)

    try:
        listener.bind(owned_sock)
        listener.listen(1)
        listener.settimeout(2)
        worker = threading.Thread(target=serve)
        worker.start()
        thread, version = qualify.read_unix_websocket(owned_sock, TARGET)
        result = qualify.classify_read(thread, TARGET, owned_sock, evidence="unix_ws_read", version=version)
        assert result == {
            "native": "UNVERIFIED-native", "native_incarnation": "unknown",
            "effective_settings": "unknown", "evidence": "unix_ws_read", "read_route_observed": True,
            "route": {"sock": owned_sock, "version": "fake-1"}, "id": TARGET,
            "sessionId": "fake-session", "cwd": qualify.WORKSPACE, "status": "idle",
            "activeFlags": None, "updatedAt": 7, "label": "STOP_IDENTITY_UNKNOWN",
            "reason": "summary does not fence a living TUI incarnation",
        }
        worker.join(2)
        assert not worker.is_alive() and not errors
    finally:
        listener.close()
        if worker is not None and worker.is_alive():
            worker.join(1)
        if os.path.lexists(owned_sock):
            os.unlink(owned_sock)
        os.rmdir(owned_dir)
    print("PASS fake_unix_loopback ws-list-read UNVERIFIED-native")


class ScriptedSocket:
    def __init__(self, data=b"", *, times_out=False):
        self.data = bytearray(data)
        self.sent = bytearray()
        self.times_out = times_out
        self.closed = False

    def settimeout(self, value):
        assert value > 0

    def recv(self, maximum):
        if self.times_out:
            raise socket.timeout()
        if not self.data:
            return b""
        count = min(maximum, 3, len(self.data))
        result = bytes(self.data[:count])
        del self.data[:count]
        return result

    def sendall(self, data):
        self.sent.extend(data)

    def close(self):
        self.closed = True


class UpgradeSocket(ScriptedSocket):
    def __init__(self, *, wrong_accept=False, extension=False):
        super().__init__()
        self.wrong_accept = wrong_accept
        self.extension = extension

    def recv(self, maximum):
        if not self.data:
            request = bytes(self.sent).decode("ascii")
            key = next(line.split(":", 1)[1].strip() for line in request.split("\r\n")
                       if line.lower().startswith("sec-websocket-key:"))
            accept = "wrong" if self.wrong_accept else base64.b64encode(hashlib.sha1(
                (key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode("ascii")
            ).digest()).decode("ascii")
            extra = "Sec-WebSocket-Extensions: permessage-deflate\r\n" if self.extension else ""
            self.data.extend(("HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\n"
                              "Connection: Upgrade\r\nSec-WebSocket-Accept: " + accept + "\r\n" + extra + "\r\n").encode("ascii"))
        return super().recv(maximum)


def test_websocket_refusals_and_bounds():
    for stream in (UpgradeSocket(wrong_accept=True), UpgradeSocket(extension=True)):
        ws = qualify.WebSocket(stream, time.monotonic() + 1)
        blocked(ws.handshake)
        ws.close()
    malformed = (
        server_frame(b"x", masked=True), server_frame(b"x", fin=False),
        server_frame(b"x", opcode=2), server_frame(b"\xff"),
        bytes((0x81, 127)) + struct.pack("!Q", qualify.MAX_WS_FRAME_BYTES + 1),
        bytes((0x81, 126)) + struct.pack("!H", 1) + b"x",
    )
    for frame in malformed:
        ws = qualify.WebSocket(ScriptedSocket(frame), time.monotonic() + 1)
        blocked(ws.recv_text)
        ws.close()
    pongs = b"".join(server_frame(b"", opcode=10) for _ in range(qualify.MAX_WS_FRAMES + 1))
    ws = qualify.WebSocket(ScriptedSocket(pongs), time.monotonic() + 1)
    assert "frame count" in blocked(ws.recv_text)
    ws.close()
    max_text = server_frame(b"x" * qualify.MAX_WS_FRAME_BYTES)
    ws = qualify.WebSocket(ScriptedSocket(max_text * 5), time.monotonic() + 2)
    for _ in range(3):
        assert len(ws.recv_text()) == qualify.MAX_WS_FRAME_BYTES
    assert "total byte" in blocked(ws.recv_text)
    ws.close()
    ws = qualify.WebSocket(ScriptedSocket(times_out=True), time.monotonic() + 1)
    assert "deadline" in blocked(ws.recv_text)
    ws.close()
    close_stream = ScriptedSocket(server_frame(struct.pack("!H", 1000), opcode=8))
    ws = qualify.WebSocket(close_stream, time.monotonic() + 1)
    assert "server closed" in blocked(ws.recv_text)
    ws.close()
    assert close_stream.closed
    print("PASS offline_mock ws-refusals-bounds UNVERIFIED-native")


def test_os_adapter_walk_is_no_follow_and_bounded():
    calls = []
    original = qualify.os.open, qualify.os.fstat, qualify.os.read, qualify.os.close
    descriptors = iter((10, 11, 12, 13))
    reads = iter((b"data", b""))
    try:
        qualify.os.open = lambda path, flags, dir_fd=None: (calls.append(("open", path, flags, dir_fd)) or next(descriptors))
        qualify.os.fstat = lambda descriptor: SimpleNamespace(st_mode=stat.S_IFREG)
        qualify.os.read = lambda descriptor, size: next(reads)
        qualify.os.close = lambda descriptor: calls.append(("close", descriptor))
        assert qualify.OSPathView().read_regular("/one/two/file", 4) == b"data"
    finally:
        qualify.os.open, qualify.os.fstat, qualify.os.read, qualify.os.close = original
    opens = [call for call in calls if call[0] == "open"]
    assert [call[1] for call in opens] == ["/", "one", "two", "file"]
    assert all(call[2] & qualify.os.O_NOFOLLOW for call in opens)
    assert all(call[2] & qualify.os.O_DIRECTORY for call in opens[:3])
    assert opens[-1][2] & qualify.os.O_NONBLOCK and opens[-1][3] == 12
    print("PASS offline_mock os-adapter UNVERIFIED-native")


if __name__ == "__main__":
    test_validator_refusals()
    test_offline_admission_fence()
    test_read_semantics_are_gated()
    test_cli_has_no_carrier_path()
    test_launch_evidence_refusals()
    test_fake_unix_websocket_roundtrip()
    test_websocket_refusals_and_bounds()
    test_os_adapter_walk_is_no_follow_and_bounded()
    print("PASS offline_mock all-qualification-checks UNVERIFIED-native")
