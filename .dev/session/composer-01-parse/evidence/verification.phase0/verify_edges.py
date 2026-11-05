#!/usr/bin/env python3
"""Fresh Phase 0 verifier probes derived from grammar v4, not parser tests."""

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


BED = Path("/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse")
FAMILY = Path("/home/hruzam/ia-sync/zsh/termbrana")
OUT = BED / "evidence/verification.phase0"
spec = importlib.util.spec_from_file_location("verified_composer", FAMILY / "composer.py")
composer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(composer)

REQUIRED = ("format", "id", "from", "to", "requested_scope")
ALLOWED = frozenset(REQUIRED + ("consult", "context", "in_reply_to", "expected_return", "stop"))
REASONS = {
    "invalid_utf8", "marker_syntax", "marker_order", "nonce_reused", "missing_body",
    "missing_end", "frame_eol", "no_packets", "header_line", "header_syntax",
    "unsupported_format", "required_absent", "empty_value", "unknown_key",
    "duplicate_key", "wrong_shape", "invalid_string", "invalid_list", "duplicate_id",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frame(body=b"x\n", nonce=b"a7b2", eol=b"\n", extra=b"", ident=b"id-one"):
    header = eol.join((
        b"<!-- composer:packet " + nonce + b" -->",
        b"format: request/0.1",
        b"id: " + ident,
        b"from: verifier",
        b"to: parser",
        b"requested_scope: read-only",
    )) + eol
    return header + extra + b"<!-- composer:body " + nonce + b" -->" + eol + body + b"<!-- composer:end " + nonce + b" -->" + eol


def expected(data, offset, code, reason, nonce="a7b2", field=None):
    before = data[:offset].split(b"\n")
    return {
        "code": code, "reason": reason, "byte_offset": offset,
        "line": len(before), "byte_column": len(before[-1]) + 1,
        "packet_nonce": nonce, "field": field,
    }


checks = []


def valid(name, data, body=None, packets=1):
    result = composer.parse(data)
    assert result.diagnostics == (), (name, [d.as_dict() for d in result.diagnostics])
    assert len(result.packets) == packets, name
    assert result.document.to_bytes() == data, name
    if body is not None:
        assert data[slice(*result.packets[0].body_span)] == body, name
    checks.append(name)
    return result


def invalid(name, data, objects):
    result = composer.parse(data)
    actual = [d.as_dict() for d in result.diagnostics]
    assert actual == objects, (name, objects, actual)
    assert result.document is None and result.packets == (), name
    exact = b"".join((json.dumps(o, ensure_ascii=True, separators=(",", ":")) + "\n").encode("ascii") for o in objects)
    assert composer.diagnostic_bytes(result.diagnostics) == exact, name
    checks.append(name)


assert composer.REQUIRED == REQUIRED
assert composer.ALLOWED == ALLOWED
source_text = (FAMILY / "composer.py").read_text()
observed_reasons = {reason for reason in REASONS if ('"' + reason + '"') in source_text}
assert observed_reasons == REASONS
assert all(token not in source_text for token in ("end_mismatch", "end_truncated", "body_bytes"))
checks.append("closed required/allowed/reason sets")

# Frozen corpus: independently read exact extents and compare actual bytes for LF/CRLF.
inventory = json.loads((BED / "evidence/corpus-inventory.cartan.json").read_text())["items"]
bodies = []
wrapped = []
for index, item in enumerate(inventory):
    raw = Path(item["source"]).read_bytes()
    assert sha(raw) == item["source_sha256"]
    start, end = item["body_byte_start_inclusive"], item["body_byte_end_exclusive"]
    body = raw[start:end]
    assert len(body) == item["body_bytes"] and sha(body) == item["body_sha256"] and body.endswith(b"\n")
    if index == 3:
        lines = raw.splitlines(keepends=True)
        assert b"".join(lines[38:407]) == body
        assert lines[407].startswith(b"# 2. JEV")
        assert (start, end) == (2061, 16595)
    bodies.append(body)
    for label, eol in (("lf", b"\n"), ("crlf", b"\r\n")):
        nonce = f"v{index}z9".encode()
        assert b"<!-- composer:end " + nonce + b" -->" not in body
        data = frame(body, nonce=nonce, eol=eol, ident=f"corpus-{index}".encode())
        result = valid(f"corpus-{index}-{label}", data, body)
        packet = result.packets[0]
        assert data[slice(*packet.body_span)] == body
        assert data[slice(*packet.span)] == data
        if (index + (label == "crlf")) % 2 == 0:
            wrapped.append(data)
mixed = b"\xef\xbb\xbfoutside\r\n" + b"between\n".join(wrapped) + b"tail\r"
result = valid("mixed corpus BOM/frame document", mixed, packets=4)
for index, packet in enumerate(result.packets):
    assert mixed[slice(*packet.body_span)] == bodies[index]
assert sum(map(len, bodies)) == 38799

handwritten = (BED / "evidence/fixtures/packet.handwritten.v4.md").read_bytes()
assert sha(handwritten) == "edea87bc07a1073b37afda9c52f68faaaac23ca63820f7a771f355848475e1a5"
hand = valid("saved handwritten fixture", handwritten)
assert handwritten[slice(*hand.packets[0].body_span)] == handwritten[
    handwritten.index(b"<!-- composer:body hand4z -->\n") + len(b"<!-- composer:body hand4z -->\n"):
    handwritten.index(b"\n<!-- composer:end hand4z -->") + 1]

# First exact closer controls; no fallback or usable prefix.
data = frame().replace(b"<!-- composer:end a7b2 -->\n", b"<!-- composer:end a7b2 -->\r\n<!-- composer:end a7b2 -->\n")
invalid("first closer wrong EOL", data, [expected(data, data.index(b"\r\n", data.index(b"<!-- composer:end")), "BOUNDARY_INVALID", "frame_eol")])
data = frame(b"alpha\n<!-- composer:end a7b2 -->\nomega\n")
invalid("inserted end and retained true end", data, [expected(data, data.rindex(b"<!-- composer:end"), "BOUNDARY_INVALID", "nonce_reused")])

# Removed-key precedence, repeats, and exactly five absent findings.
for key in (b"program", b"function"):
    line = key + b": [[unterminated\n"
    data = frame(extra=line + line)
    first = data.index(line)
    invalid(key.decode() + " unknown before value/repetition", data, [
        expected(data, first, "FIELD_INVALID", "unknown_key", field=key.decode()),
        expected(data, first + len(line), "FIELD_INVALID", "unknown_key", field=key.decode()),
    ])
    line = key + b": []\r\n"
    data = frame(extra=line)
    invalid(key.decode() + " wrong EOL first", data, [expected(data, data.index(b"\r", data.index(key)), "BOUNDARY_INVALID", "frame_eol")])
    line = b" " + key + b": []\n"
    data = frame(extra=line)
    invalid(key.decode() + " line shape first", data, [expected(data, data.index(line), "HEADER_INVALID", "header_line")])
    line = key + b":\n"
    data = frame(extra=line)
    invalid(key.decode() + " syntax first", data, [expected(data, data.index(line), "HEADER_INVALID", "header_syntax")])

data = frame()
for line in (b"format: request/0.1\n", b"id: id-one\n", b"from: verifier\n", b"to: parser\n", b"requested_scope: read-only\n"):
    data = data.replace(line, b"")
at = data.index(b"<!-- composer:body")
invalid("exactly five absent required", data, [
    expected(data, at, "FIELD_MISSING", "required_absent", field=k)
    for k in ("format", "from", "id", "requested_scope", "to")
])

# UTF-8 preflight suppresses every grammar finding; BOM coordinates stay byte-based.
data = frame(extra=b"program: []\n") + b"tail\xff"
invalid("invalid UTF-8 suppresses grammar", data, [expected(data, len(data)-1, "ENCODING_INVALID", "invalid_utf8", None)])
data = b"\xef\xbb\xbf" + frame(extra=b"program: []\n")
invalid("BOM original byte coordinate", data, [expected(data, data.index(b"program:"), "FIELD_INVALID", "unknown_key", field="program")])

# Unicode NEL/LS/PS are data, while bare CR differs by state.
body = "a\u0085b\u2028c\u2029d\n".encode()
data = frame(body, extra="stop: a\u0085b\u2028c\u2029d\n".encode())
r = valid("Unicode separators are not physical lines", data, body)
assert r.packets[0].fields["stop"] == "a\u0085b\u2028c\u2029d"
data = frame(extra=b"stop: x\ry\n")
invalid("bare CR in header is frame EOL error", data, [expected(data, data.index(b"\r"), "BOUNDARY_INVALID", "frame_eol")])
body = b"x\ry\n<!-- composer:end other4 -->\rmore\n"
valid("bare CR in body is preserved", frame(body), body)
prefix = frame().split(b"x\n", 1)[0]
data = prefix + b"<!-- composer:end a7b2 -->\r"
invalid("bare CR end at EOF stays body", data, [expected(data, len(data), "BOUNDARY_INVALID", "missing_end")])

# Scalar/list edges and structural aggregation boundary.
data = frame(extra=b'context: ["a,b", "[x]", no, 01234567, no]\nstop: "a\\u003ab"  \n')
r = valid("JSON/list/string valid edges", data)
assert r.packets[0].fields["context"] == ["a,b", "[x]", "no", "01234567", "no"]
assert r.packets[0].fields["stop"] == "a:b"
for value, reason in ((b'["x"oops]', "invalid_list"), (b"[a,]", "invalid_list")):
    data = frame(extra=b"context: " + value + b"\n")
    invalid("list edge " + value.decode(), data, [expected(data, data.index(b"context:"), "FIELD_INVALID", reason, field="context")])

first = frame(extra=b"program: []\n")
second = frame(nonce=b"bbb2", ident=b"two", extra=b"function: x\n")
third = frame(nonce=b"ccc3", ident=b"three").split(b"x\n", 1)[0] + b"unclosed\nformat: broken\n"
data = first + second + third
invalid("aggregate until structural stop", data, [
    expected(data, data.index(b"program:"), "FIELD_INVALID", "unknown_key", field="program"),
    expected(data, data.index(b"function:"), "FIELD_INVALID", "unknown_key", "bbb2", "function"),
    expected(data, len(data), "BOUNDARY_INVALID", "missing_end", "ccc3"),
])

# Literal non-execution through the real isolated zsh entry; input remains unchanged.
sentinel = OUT / "SENTINEL-MUST-NOT-EXIST"
if sentinel.exists():
    sentinel.unlink()
literal = ("$(touch " + str(sentinel) + ")\n`touch " + str(sentinel) + "`\n"
           "&& exec false\nprogram: body text\n\x1b[31mCONTROL\x00\n").encode()
data = frame(literal, extra=b"context: [/path/that/does/not/exist]\n")
input_path = OUT / "nonexecution.input.md"
input_path.write_bytes(data)
before = sha(input_path.read_bytes())
commands = []
for mode in ("check", "parse"):
    command = ["zsh", "-f", "-c", 'source "$1/base.zsh"; _tbc_"$2" "$3"', "verifier", str(FAMILY), mode, str(input_path)]
    for repeat in range(2):
        run = subprocess.run(command, capture_output=True)
        assert run.returncode == 0 and run.stderr == b""
        if mode == "check":
            assert run.stdout == b""
        else:
            assert run.stdout.isascii() and b"CONTROL" not in run.stdout and b"touch" not in run.stdout and b"\x1b" not in run.stdout
            parsed = json.loads(run.stdout)
            assert parsed["packets"][0]["body_span"]
        assert not sentinel.exists()
        commands.append({"argv": command, "mode": mode, "repeat": repeat + 1,
                         "exit": run.returncode, "stdout_sha256": sha(run.stdout), "stderr_bytes": len(run.stderr)})
assert sha(input_path.read_bytes()) == before
checks.append("real CLI literal non-execution/input preservation/safe output")

report = {
    "status": "PASS",
    "python": sys.version,
    "source_sha256": sha((FAMILY / "composer.py").read_bytes()),
    "checks": checks,
    "check_count": len(checks),
    "corpus_body_bytes": sum(map(len, bodies)),
    "mixed_serialized_bytes": len(mixed),
    "nonexecution_input_sha256": before,
    "sentinel_absent": not sentinel.exists(),
    "commands": commands,
}
(OUT / "edge-report.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": "PASS", "checks": len(checks), "corpus_body_bytes": sum(map(len, bodies))}))
