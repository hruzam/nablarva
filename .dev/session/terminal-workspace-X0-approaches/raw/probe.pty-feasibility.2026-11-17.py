"""Synthetic feasibility only; no broker, native agent, container or user terminal.

Each shell starts without profiles/rc and with a tiny nonsecret environment.
Only this process's new PTY and children are addressed. Output markers synchronize
this controlled fixture; they are not a production command-completion protocol.
"""
import fcntl
import json
import os
import pty
import select
import shlex
import signal
import struct
import subprocess
import sys
import tempfile
import termios
import time


def main():
    report = {"scope": "synthetic owned PTY only", "checks": {}, "qualified": False,
              "python": sys.version, "pid_namespace": os.readlink("/proc/self/ns/pid")}
    env = {"PATH": "/usr/bin:/bin", "TERM": "xterm-256color", "LC_ALL": "C.UTF-8",
           "PS1": "OWNED-PROBE> ", "PS2": "CONTINUE> ", "HISTFILE": "/dev/null"}
    transcript = bytearray()
    with tempfile.TemporaryDirectory(prefix="terminal-workspace-probe-") as temp:
        report["temporary_root"] = temp
        os.mkdir(os.path.join(temp, "task-a"))
        first = os.path.join(temp, "request-1.sh")
        second = os.path.join(temp, "request-2.sh")
        with open(first, "x") as handle:
            handle.write("cd task-a\nexport TASK_TOKEN=synthetic-state\n"
                         "task_function() { printf 'FUNCTION_RETAINED\\n'; }\n")
        with open(second, "x") as handle:
            handle.write("printf 'FILE_STATE:%s:%s:%s\\n' \"$PWD\" \"$TASK_TOKEN\" \"$$\"\n"
                         "task_function\n")
        child_pid = None
        master = None
        reaped = False
        try:
            child_pid, master = pty.fork()
            if child_pid == 0:
                os.chdir(temp)
                os.execve("/usr/bin/bash", ["bash", "--noprofile", "--norc", "-i"], env)
            report["owned_shell_pid"] = child_pid

            def read_until(marker, timeout=4.0):
                deadline = time.monotonic() + timeout
                start = len(transcript)
                while marker not in bytes(transcript[start:]).replace(b"\r\n", b"\n"):
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise RuntimeError("fixture timed out waiting for " + repr(marker))
                    ready, _, _ = select.select([master], [], [], remaining)
                    if not ready:
                        continue
                    data = os.read(master, 65536)
                    if not data:
                        raise RuntimeError("PTY closed before expected fixture output")
                    transcript.extend(data)
                return bytes(transcript[start:]).replace(b"\r\n", b"\n")

            def send(data):
                while data:
                    written = os.write(master, data)
                    data = data[written:]

            read_until(b"OWNED-PROBE> ")
            send(b"stty -echo; printf '\\nFIXTURE_READY\\n'\n")
            read_until(b"\nFIXTURE_READY\n")
            send(("source " + shlex.quote(first) + "; printf '\\nFIRST_FILE_DONE\\n'\n").encode())
            read_until(b"\nFIRST_FILE_DONE\n")
            send(("source " + shlex.quote(second) + "; printf '\\nSECOND_FILE_DONE\\n'\n").encode())
            output = read_until(b"\nSECOND_FILE_DONE\n")
            wanted = "FILE_STATE:{}:synthetic-state:{}".format(os.path.join(temp, "task-a"), child_pid)
            report["checks"]["same_shell_file_requests_retain_cwd_env_function"] = (
                wanted.encode() in output and b"FUNCTION_RETAINED\n" in output)

            # Independent new shell processes are the negative comparison.
            subprocess.run(["/usr/bin/bash", "--noprofile", "--norc", first],
                           cwd=temp, env=env, check=True, capture_output=True, timeout=3)
            independent = subprocess.run(
                ["/usr/bin/bash", "--noprofile", "--norc", "-c",
                 "printf '%s:%s' \"$PWD\" \"${TASK_TOKEN-unset}\""],
                cwd=temp, env=env, check=True, capture_output=True, timeout=3)
            report["checks"]["fresh_process_does_not_retain_prior_cwd_env"] = (
                independent.stdout.decode() == temp + ":unset")

            send(b"test -t 0 && test -t 1 && printf '\\nTTY_CONFIRMED\\n'; "
                 b"IFS= read -r -p 'SYNTHETIC_REPLY? ' reply; printf '\\nREPLY:%s\\n' \"$reply\"\n")
            waiting = read_until(b"SYNTHETIC_REPLY? ")
            send(b"human-fixture-reply\n")
            reply = read_until(b"\nREPLY:human-fixture-reply\n")
            report["checks"]["tty_and_interactive_line_reply"] = b"TTY_CONFIRMED\n" in waiting

            send(b"python3 -I -S -B -c 'import os, signal; "
                 b"signal.signal(signal.SIGINT, lambda *_: os._exit(42)); "
                 b"print(\"FOREGROUND_READY\", flush=True); signal.pause()'; "
                 b"rc=$?; printf '\\nAFTER_INTERRUPT:%s\\n' \"$rc\"\n")
            read_until(b"FOREGROUND_READY\n")
            send(b"\x03")
            interrupted = read_until(b"\nAFTER_INTERRUPT:42\n")
            send(b"printf '\\nSHELL_SURVIVED:%s:%s\\n' \"$$\" \"$TASK_TOKEN\"\n")
            alive = read_until(("\nSHELL_SURVIVED:{}:synthetic-state\n".format(child_pid)).encode())
            report["checks"]["ctrl_c_signals_foreground_child_shell_survives"] = bool(interrupted and alive)

            fcntl.ioctl(master, termios.TIOCSWINSZ, struct.pack("HHHH", 37, 101, 0, 0))
            send(b"printf '\\nSIZE:'; stty size; printf '\\nSIZE_DONE\\n'\n")
            size = read_until(b"\nSIZE_DONE\n")
            report["checks"]["pty_dimensions_change"] = b"SIZE:37 101\n" in size

            # Leave the PTY open but stop reading: this is NOT viewer detach/reconnect.
            send(b"sleep 0.1; printf '\\nUNOBSERVED_INTERVAL_FINISHED\\n'\n")
            time.sleep(0.2)
            read_until(b"\nUNOBSERVED_INTERVAL_FINISHED\n")
            report["checks"]["open_pty_survives_brief_unobserved_interval"] = True
            send(b"exit\n")
            deadline = time.monotonic() + 3
            while time.monotonic() < deadline:
                waited, status = os.waitpid(child_pid, os.WNOHANG)
                if waited:
                    reaped = True
                    report["shell_exit_status"] = os.waitstatus_to_exitcode(status)
                    break
                time.sleep(0.02)
            if not reaped:
                raise RuntimeError("owned shell failed to exit")
            report["unproven"] = ["native CLI attachment/permissions", "human client attachment",
                "actual detach/reconnect", "input ownership/takeover", "container isolation",
                "rendered screen/TUI correctness", "raw single-key mode", "restart/replay safety"]
            report["all_feasibility_checks_pass"] = all(report["checks"].values())
        except (OSError, RuntimeError) as exc:
            report["error"] = "{}: {}".format(type(exc).__name__, exc)
        finally:
            if child_pid and not reaped:
                # The session/process group was created by this probe's pty.fork only.
                try:
                    os.killpg(child_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                os.waitpid(child_pid, 0)
                reaped = True
            if master is not None:
                os.close(master)
            report["owned_shell_reaped"] = reaped
            report["transcript"] = bytes(transcript).decode("utf-8", "replace")
    report["temporary_root_removed"] = not os.path.exists(temp)
    print(json.dumps(report, indent=2))
    return 0 if report.get("all_feasibility_checks_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
