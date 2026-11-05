// Fixture constructs pre-termios payload from the frozen specification. It
// never opens expected/ or collector files. Supervisor alone owns
// fixture-control.ndjson.
#include "../collect/common.hpp"
namespace q {
static std::string frame(int n) {
  char h[9];
  snprintf(h, sizeof h, "F%06d:", n);
  std::string b(h, 8);
  const unsigned char special[] = {0, 13, 10, 92, 27, 91, 51, 49, 109};
  b.append(reinterpret_cast<const char *>(special), 9);
  for (int i = 17; i < 1023; ++i)
    b += char('A' + (n + i) % 26);
  b += '\n';
  return b;
}
static void emit(const std::string &mode, const fs::path &d,
                 const fs::path &tmp) {
  termios t{};
  check(tcgetattr(1, &t) == 0, "initial tcgetattr");
  save(d / "termios.initial.json", term());
  t.c_oflag = mode == "onlcr" ? OPOST | ONLCR : 0;
  check(tcsetattr(1, TCSANOW, &t) == 0, "tcsetattr");
  save(d / "termios.before.json", term());
  save(tmp / "emitter.ready", ident(getpid()));
  waitfile(tmp / "go", now() + 14000000000LL);
  I epoch = now();
  std::string payload;
  if (mode == "screen")
    payload = "\033[2J\033[HAlpha\r\nBeta";
  else if (mode == "false_completion")
    payload = "Done\r\nuser@host:~$ ";
  else
    for (int n = 0; n < (mode == "burst" || mode == "sink_loss" ? 4096 : 256);
         ++n)
      payload += frame(n);
  J ph = J::obj();
  ph["bytes"] = I(payload.size());
  ph["sha256"] = sha(payload);
  save(d / "payload.json", ph);
  auto transmit = [&](const std::string &b, int n, I planned) {
    J e = J::obj();
    e["frame"] = n;
    e["planned_ns"] = planned;
    e["release_ns"] = now();
    if (n == 0 && b.size() == 1024) {
      fullwrite(1, b.data(), 12);
      fullwrite(1, b.data() + 12, 1);
      fullwrite(1, b.data() + 13, 1);
      fullwrite(1, b.data() + 14, b.size() - 14);
    } else
      fullwrite(1, b.data(), b.size());
    e["write_complete_ns"] = now();
    append(d / "emission.ndjson", e.dump() + "\n");
  };
  if (mode == "screen" || mode == "false_completion")
    transmit(payload, 0, epoch);
  else {
    int count = mode == "burst" || mode == "sink_loss" ? 4096 : 256;
    for (int n = 0; n < count; ++n) {
      bool paced = mode != "burst" && mode != "sink_loss";
      I planned = epoch + (paced ? I(n) * 10000000 : 0);
      if (paced) {
        timespec ts{time_t(planned / 1000000000), long(planned % 1000000000)};
        while (clock_nanosleep(CLOCK_MONOTONIC, TIMER_ABSTIME, &ts, nullptr) ==
               EINTR) {
        }
      }
      transmit(payload.substr(size_t(n) * 1024, 1024), n, planned);
      if ((n == 2047 && mode == "sink_loss") ||
          (n == 127 && (mode == "pause" || mode == "disconnect" ||
                        mode == "late_attach"))) {
        J b = J::obj();
        b["frame"] = n;
        b["emitter"] = ident(getpid());
        b["monotonic_ns"] = now();
        save(tmp / "boundary", b);
        waitfile(tmp / "continue", now() + 14000000000LL);
      }
    }
  }
  save(d / "termios.after.json", term());
  J done = J::obj();
  done["monotonic_ns"] = now();
  save(tmp / "emission.done", done);
  // The supervisor controls the known-alive quiet interval and proves child
  // exit.
  waitfile(tmp / "exit", now() + 14000000000LL);
}
int fixture(const std::string &mode, const fs::path &d, const fs::path &tmp) {
  fs::create_directories(d);
  fs::create_directories(tmp);
  auto log = d / "fixture-control.ndjson";
  J start = J::obj();
  start["supervisor"] = ident(getpid());
  event(log, "supervisor_start", start);
  pid_t child = fork();
  check(child >= 0, "fixture fork");
  if (child == 0) {
    try {
      emit(mode, d, tmp);
      _exit(0);
    } catch (const std::exception &e) {
      append(d / "fixture.stderr", std::string(e.what()) + "\n");
      _exit(1);
    }
  }
  J c = J::obj();
  c["child"] = ident(child);
  event(log, "child_start", c);
  save(tmp / "supervisor.ready", start);
  int status = 0;
  I deadline = now() + 14500000000LL;
  bool sent = false;
  I quiet = 0;
  while (true) {
    pid_t w = waitpid(child, &status, WNOHANG);
    if (w == child)
      break;
    check(w >= 0, "fixture waitpid");
    if (!sent && fs::exists(tmp / "emission.done")) {
      if (mode == "false_completion") {
        if (!quiet) {
          quiet = now();
          J x = J::obj();
          x["child"] = ident(child);
          x["emission_done_ns"] =
              load(tmp / "emission.done").at("monotonic_ns");
          event(log, "quiet_begin_known_alive", x);
        }
        if (now() - quiet >= 5000000000LL) {
          J x = J::obj();
          x["child"] = ident(child);
          x["quiet_begin_ns"] = quiet;
          event(log, "quiet_end_known_alive", x);
          write(tmp / "exit", "");
          sent = true;
        }
      } else {
        write(tmp / "exit", "");
        sent = true;
      }
    }
    if (now() > deadline) {
      auto id = ident(child);
      signal_owned(id, SIGKILL);
      waitpid(child, &status, 0);
      event(log, "watchdog_child_killed");
      break;
    }
    poll(nullptr, 0, 2);
  }
  J e = J::obj();
  e["child_pid"] = int(child);
  e["wait_status"] = status;
  e["exited"] = bool(WIFEXITED(status));
  e["exit_code"] = WIFEXITED(status) ? WEXITSTATUS(status) : -1;
  event(log, "direct_child_wait", e);
  save(tmp / "fixture.exited", e);
  // Keep the synthetic pane until the runner has taken its screen and drained
  // sink.
  waitfile(tmp / "stop", now() + 14500000000LL);
  return status == 0 ? 0 : 1;
}
} // namespace q
