#include "common.hpp"
#include <sys/utsname.h>
namespace q {
const std::string frozen =
    "627e2e30e1434b8e27c277ffc2a21d8f6120ba92a9aca12d863459a65f9fcf7c";
static void verify_oracle(const fs::path &bed) {
  auto p = bed / "expected";
  check(hashfile(p / "manifest.json") == frozen, "frozen manifest changed");
  auto manifest = load(p / "manifest.json");
  for (auto &f : manifest.at("files").a) {
    auto name = f.at("path").str();
    auto file = p / name;
    check(fs::is_regular_file(file) && !fs::is_symlink(file),
          "oracle member type");
    check(hashfile(file) == f.at("sha256").str(),
          "oracle member changed " + name);
  }
}
static J argvjson(const std::vector<std::string> &args) {
  J j = J::arr();
  for (auto &s : args)
    j.push(s);
  return j;
}
struct Run {
  fs::path bed, root, dir, tmp;
  std::string mode, exe, socket;
  J m = J::obj();
  I begun = now(), deadline = begun + 13000000000LL;
  int commandNo = 0;
  std::vector<J> processes;
  std::vector<pid_t> observers;
  Run(fs::path b, fs::path rt, std::string mo)
      : bed(std::move(b)), root(std::move(rt)), mode(std::move(mo)),
        exe(self()) {
    verify_oracle(bed);
    check(
        hashfile("/usr/bin/tmux") ==
            "e79f47015e65b128767ae0d12d0804b088a2d5fb9f6e04194f9abdc1388c435f",
        "tmux binary drift");
    fs::create_directories(root);
    dir = root /
          (mode + "-" + std::to_string(now()) + "-" + std::to_string(getpid()));
    check(fs::create_directory(dir), "run directory collision");
    fs::create_directory(dir / "commands");
    m["phase"] = "allocated";
    m["mode"] = mode;
    m["run_directory"] = dir.string();
    m["expected_manifest_sha256"] = frozen;
    m["clock"] = "CLOCK_MONOTONIC; ns; same-host emitter and append clocks";
    timespec res{};
    clock_getres(CLOCK_MONOTONIC, &res);
    m["clock_resolution_ns"] = I(res.tv_sec) * 1000000000 + res.tv_nsec;
    m["start_ns"] = begun;
    m["watchdog_ns"] = 15000000000LL;
    m["active_deadline_ns"] = deadline;
    m["runner"] = ident(getpid());
    m["uid"] = int(getuid());
    m["boot_id"] = read("/proc/sys/kernel/random/boot_id");
    m["load_context"] = read("/proc/loadavg");
    utsname u{};
    uname(&u);
    m["host"] = u.nodename;
    m["kernel"] = u.release;
    m["tmux_sha256"] = hashfile("/usr/bin/tmux");
    m["helper_path"] = exe;
    m["helper_sha256"] = hashfile(exe);
    m["generations"] = J::arr();
    m["processes"] = J::arr();
    m["commands"] = J::arr();
    m["source_hashes"] = J::obj();
    for (auto subtree : {"fixture", "collect", "compare"})
      for (auto &e : fs::directory_iterator(bed / "src" / subtree))
        if (e.is_regular_file())
          m["source_hashes"][e.path().lexically_relative(bed).string()] =
              hashfile(e.path());
    m["input_hashes"] = J::obj();
    for (auto path : {"RUNBOOK.md", "raw/entry-and-release.md",
                      "_bus/05.cartan-termpanum-x1.point.md",
                      "expected/schedule.md", "expected/observations.ndjson"})
      m["input_hashes"][path] = hashfile(bed / path);
    m["environment"] = J::obj();
    for (auto kv :
         {std::pair<const char *, const char *>{"PATH", "/usr/bin:/bin"},
          {"LC_ALL", "C.UTF-8"},
          {"LANG", "C.UTF-8"},
          {"TERM", "xterm-256color"},
          {"SHELL", "/bin/sh"}})
      m["environment"][kv.first] = kv.second;
    persist();
    J index = fs::exists(root / "runtime-index.json")
                  ? load(root / "runtime-index.json")
                  : J::obj();
    if (index.t == J::Object && index.o.find("runs") == index.o.end())
      index["runs"] = J::arr();
    J entry = J::obj();
    entry["directory"] = dir.string();
    entry["ownership_manifest"] = (dir / "manifest.json").string();
    entry["mode"] = mode;
    index["runs"].push(entry);
    save(root / "runtime-index.json", index);
    std::string pattern = "/tmp/tq-" + std::to_string(getuid()) + "-" +
                          std::to_string(now()) + "-XXXXXX";
    std::vector<char> buf(pattern.begin(), pattern.end());
    buf.push_back(0);
    char *p = mkdtemp(buf.data());
    check(p, "mkdtemp");
    tmp = p;
    socket = (tmp / "tmux.sock").string();
    struct stat st{};
    check(lstat(tmp.c_str(), &st) == 0 && S_ISDIR(st.st_mode) &&
              st.st_uid == getuid() && (st.st_mode & 077) == 0,
          "temporary ownership mismatch");
    check(socket.size() < 108, "UNIX socket path too long");
    m["temporary_directory"] = tmp.string();
    m["socket"] = socket;
    m["environment"]["HOME"] = tmp.string();
    m["phase"] = "runtime_allocated";
    persist();
  }
  void persist() { save(dir / "manifest.json", m); }
  void guard() {
    check(now() < deadline,
          "run active watchdog reached (cleanup reserve retained)");
  }
  void wait(const fs::path &p) { waitfile(p, deadline); }
  void track(const J &id, const std::string &role) {
    J p = id;
    p["role"] = role;
    processes.push_back(p);
    m["processes"].push(p);
    persist();
  }
  std::string command(const std::vector<std::string> &args, bool must = true) {
    guard();
    std::string name = std::to_string(commandNo++);
    auto out = dir / "commands" / (name + ".stdout"),
         err = dir / "commands" / (name + ".stderr");
    int gate[2];
    check(pipe2(gate, O_CLOEXEC) == 0, "command gate");
    pid_t pid = fork();
    check(pid >= 0, "command fork");
    if (pid == 0) {
      close(gate[1]);
      char c;
      ssize_t n = ::read(gate[0], &c, 1);
      close(gate[0]);
      if (n != 1)
        _exit(125);
      int of = open(out.c_str(), O_CREAT | O_WRONLY | O_EXCL, 0600),
          ef = open(err.c_str(), O_CREAT | O_WRONLY | O_EXCL, 0600);
      if (of < 0 || ef < 0)
        _exit(125);
      dup2(of, 1);
      dup2(ef, 2);
      close(of);
      close(ef);
      int null = open("/dev/null", O_RDONLY);
      dup2(null, 0);
      close(null);
      std::vector<char *> av;
      for (auto &s : args)
        av.push_back(const_cast<char *>(s.c_str()));
      av.push_back(nullptr);
      std::vector<std::string> env;
      for (auto &kv : m["environment"].o)
        env.push_back(kv.first + "=" + kv.second.s);
      std::vector<char *> ep;
      for (auto &s : env)
        ep.push_back(s.data());
      ep.push_back(nullptr);
      chdir(tmp.c_str());
      execve(args[0].c_str(), av.data(), ep.data());
      _exit(127);
    }
    close(gate[0]);
    J id = ident(pid);
    J c = J::obj();
    c["argv"] = argvjson(args);
    c["identity"] = id;
    c["start_ns"] = now();
    c["stdout"] = out.string();
    c["stderr"] = err.string();
    m["commands"].push(c);
    persist();
    fullwrite(gate[1], "x", 1);
    close(gate[1]);
    int status = 0;
    bool timeout = false;
    while (waitpid(pid, &status, WNOHANG) == 0) {
      if (now() >= deadline) {
        timeout = true;
        if (alive(id))
          signal_owned(id, SIGKILL);
        while (waitpid(pid, &status, 0) < 0 && errno == EINTR) {
        }
        break;
      }
      poll(nullptr, 0, 2);
    }
    auto &saved = m["commands"].a.back();
    saved["end_ns"] = now();
    saved["wait_status"] = status;
    saved["timeout"] = timeout;
    persist();
    check(!timeout, "subprocess watchdog timeout");
    if (must)
      check(WIFEXITED(status) && WEXITSTATUS(status) == 0,
            "command failed; see " + err.string());
    return fs::exists(out) ? read(out) : "";
  }
  std::string tmux(std::vector<std::string> args, bool must = true) {
    std::vector<std::string> a = {"/usr/bin/tmux", "-S", socket, "-f",
                                  "/dev/null"};
    a.insert(a.end(), args.begin(), args.end());
    return command(a, must);
  }
  void waitbytes(const fs::path &p, I count) {
    while (!fs::exists(p) || I(fs::file_size(p)) < count) {
      guard();
      poll(nullptr, 0, 2);
    }
  }
  J binding(const std::string &pane) {
    auto s = tmux({"display-message", "-p", "-t", pane,
                   "#{pid} #{pane_id} #{pane_pid} #{pane_tty} #{window_index} "
                   "#{window_name}"});
    std::istringstream in(s);
    int server = 0, fixture = 0;
    std::string paneid, tty, index, name;
    check(bool(in >> server >> paneid >> fixture >> tty >> index >> name),
          "cannot bind server/pane identity");
    J j = J::obj();
    j["server"] = ident(server);
    j["pane_id"] = paneid;
    j["fixture"] = ident(fixture);
    j["tty"] = tty;
    j["window_index"] = index;
    j["window_name"] = name;
    track(j["server"], "tmux_server");
    track(j["fixture"], "fixture_supervisor");
    return j;
  }
  J start_sink(const fs::path &d, const fs::path &ctrl, const std::string &pane,
               const std::string &segment) {
    std::string cmd = "exec " + shell(exe) + " sink " + shell(d.string()) +
                      " " + shell(ctrl.string()) + " " + shell(segment) +
                      " 2>" +
                      shell((d / ("sink." + segment + ".stderr")).string());
    tmux({"pipe-pane", "-O", "-t", pane, cmd});
    wait(ctrl / ("sink." + segment + ".ready"));
    J id = load(ctrl / ("sink." + segment + ".ready"));
    track(id, "reader_sink_" + segment);
    check(tmux({"display-message", "-p", "-t", pane, "#{pane_pipe}"}) == "1\n",
          "pipe not active");
    J e = J::obj();
    e["reader"] = id;
    e["segment"] = segment;
    event(d / "coverage.ndjson", "capture_ready_bound", e);
    return id;
  }
  pid_t observer(const J &reader, const fs::path &ctrl) {
    int fd = int(syscall(SYS_pidfd_open, pid_t(reader.at("pid").num()), 0));
    check(fd >= 0 && same(reader), "observer target identity");
    pid_t pid = fork();
    check(pid >= 0, "observer fork");
    if (pid == 0) {
      try {
        waitfile(ctrl / "observe", deadline);
        pollfd p{fd, POLLIN, 0};
        while (now() < deadline) {
          int rc = poll(&p, 1, 10);
          if (rc > 0 && (p.revents & POLLIN)) {
            J e = J::obj();
            e["monotonic_ns"] = now();
            e["evidence"] = "pidfd reported actual sink exit";
            e["reader"] = reader;
            save(dir / "fault-detection.json", e);
            _exit(0);
          }
          if (rc < 0 && errno != EINTR)
            throw std::runtime_error("observer poll");
        }
        throw std::runtime_error("observer watchdog");
      } catch (const std::exception &e) {
        append(dir / "observer.stderr", std::string(e.what()) + "\n");
        _exit(1);
      }
    }
    close(fd);
    track(ident(pid), "fault_observer");
    observers.push_back(pid);
    return pid;
  }
  void fault(const fs::path &d, const fs::path &ctrl, const std::string &pane,
             J &reader) {
    wait(ctrl / "boundary");
    J boundary = load(ctrl / "boundary");
    check(boundary.at("frame").num() == (mode == "sink_loss" ? 2047 : 127),
          "unexpected fault boundary");
    save(dir / "fault-boundary.json", boundary);
    if (mode != "late_attach")
      waitbytes(d / "capture.bin",
                (mode == "sink_loss" ? 2048LL : 128LL) * 1024);
    if (mode == "late_attach") {
      poll(nullptr, 0, 25);
      reader = start_sink(d, ctrl, pane, "0");
      J e = J::obj();
      e["absent_start"] = 0;
      e["absent_end"] = 128 * 1024;
      event(d / "coverage.ndjson", "prefix_absent", e);
      write(ctrl / "continue", "");
      return;
    }
    J a = J::obj();
    a["reader"] = reader;
    a["monotonic_ns"] = now();
    a["action"] = mode;
    if (mode == "pause") {
      signal_owned(reader, SIGSTOP);
      while (ident(pid_t(reader.at("pid").num())).at("state").str() != "T") {
        guard();
        poll(nullptr, 0, 1);
      }
      a["monotonic_ns"] = now();
      save(dir / "fault-action.json", a);
      write(ctrl / "continue", "");
      I until = now() + 3000000000LL;
      while (now() < until) {
        guard();
        poll(nullptr, 0, 2);
      }
      signal_owned(reader, SIGCONT);
      J e = J::obj();
      e["monotonic_ns"] = now();
      e["reader"] = reader;
      save(dir / "resume.json", e);
      return;
    }
    observer(reader, ctrl);
    if (mode == "sink_loss")
      signal_owned(reader, SIGKILL);
    else
      tmux({"pipe-pane", "-t", pane});
    a["monotonic_ns"] = now();
    save(dir / "fault-action.json", a);
    write(ctrl / "observe", "");
    wait(dir / "fault-detection.json");
    if (mode == "disconnect") {
      J gap = J::obj();
      gap["detach_complete_ns"] = a["monotonic_ns"];
      reader = start_sink(d, ctrl, pane, "1");
      gap["rebind_complete_ns"] = now();
      gap["new_reader"] = reader;
      save(dir / "rebind.json", gap);
      event(d / "coverage.ndjson", "discontinuous_until_rebind", gap);
    }
    write(ctrl / "continue", "");
  }
  void generation(int n, bool newServer) {
    guard();
    std::string name = "g" + std::to_string(n);
    fs::path d = dir / name, ctrl = tmp / name;
    check(fs::create_directory(d), "generation exists");
    check(fs::create_directory(ctrl), "controls exist");
    std::string payloadMode =
        mode == "pane_recreate" || mode == "server_recreate" ? "screen" : mode;
    J g = J::obj();
    g["directory"] = name;
    g["control_directory"] = ctrl.string();
    g["start_ns"] = now();
    std::vector<std::string> args =
        newServer
            ? std::vector<std::string>{"new-session", "-d",
                                       "-s",          "tq",
                                       "-n",          "source",
                                       "-x",          "80",
                                       "-y",          "24",
                                       "-c",          tmp.string(),
                                       exe,           "fixture",
                                       payloadMode,   d.string(),
                                       ctrl.string()}
            : std::vector<std::string>{
                  "new-window", "-d",       "-t",         "tq:0", "-n",
                  "source",     "-c",       tmp.string(), exe,    "fixture",
                  payloadMode,  d.string(), ctrl.string()};
    g["intended_tmux_argv"] = argvjson(args);
    m["generations"].push(g);
    m["phase"] = "before_server_or_pane_spawn";
    persist();
    tmux(args);
    g = binding("tq:0.0");
    g["directory"] = name;
    g["control_directory"] = ctrl.string();
    g["start_ns"] = m["generations"].a.back().at("start_ns");
    g["intended_tmux_argv"] = argvjson(args);
    m["generations"].a.back() = g;
    persist();
    std::string pane = g["pane_id"].s;
    wait(ctrl / "supervisor.ready");
    wait(ctrl / "emitter.ready");
    J emitter = load(ctrl / "emitter.ready");
    track(emitter, "fixture_emitter");
    g["emitter"] = emitter;
    g["supervisor_ready"] = load(ctrl / "supervisor.ready");
    if (mode == "pane_recreate" && n == 0) {
      fs::path hc = tmp / "hold";
      fs::create_directory(hc);
      tmux({"new-window", "-d", "-t", "tq:1", "-n", "keeper", "-c",
            tmp.string(), exe, "hold", hc.string()});
      wait(hc / "ready");
      track(load(hc / "ready"), "synthetic_keeper");
    }
    J reader;
    if (mode != "late_attach")
      reader = start_sink(d, ctrl, pane, "0");
    g["ready_ns"] = now();
    g["reader_initial"] = reader;
    g["coverage_start_ns"] = now();
    m["generations"].a.back() = g;
    m["phase"] = "bound_before_emission";
    persist();
    write(ctrl / "go", "");
    if (mode == "sink_loss" || mode == "pause" || mode == "disconnect" ||
        mode == "late_attach")
      fault(d, ctrl, pane, reader);
    wait(ctrl / "fixture.exited");
    g["fixture_wait"] = load(ctrl / "fixture.exited");
    check(g["fixture_wait"].at("exit_code").num() == 0, "fixture child failed");
    I wanted = payloadMode == "screen"             ? 18
               : payloadMode == "false_completion" ? 19
               : payloadMode == "onlcr"            ? 262656
               : payloadMode == "burst"            ? 4194304
                                                   : 262144;
    if (mode == "late_attach")
      wanted = 131072;
    if (mode != "sink_loss")
      waitbytes(d / "capture.bin", wanted);
    if (payloadMode == "screen")
      write(d / "screen.txt",
            tmux({"capture-pane", "-p", "-S", "0", "-E", "1", "-t", pane}));
    // Detach only after independently confirmed source exit and expected append
    // coverage.
    if (mode != "sink_loss") {
      tmux({"pipe-pane", "-t", pane});
      wait(ctrl / ("sink." + std::string(mode == "disconnect" ? "1" : "0") +
                   ".exited"));
    }
    g["capture_end_ns"] = now();
    g["coverage_end_ns"] = now();
    g["reader_final"] = reader;
    m["generations"].a.back() = g;
    m["phase"] = "captured";
    persist();
  }
  void end_first(bool server) {
    auto &g = m["generations"].a.back();
    J a = J::obj();
    a["old_binding"] = g;
    a["before_ns"] = now();
    check(same(g.at("server")) && same(g.at("fixture")),
          "recreation ownership lost");
    if (server)
      tmux({"kill-server"});
    else
      tmux({"kill-pane", "-t", g.at("pane_id").str()});
    a["completed_ns"] = now();
    save(dir / "recreation-action.json", a);
    if (server) {
      while (alive(g.at("server"))) {
        guard();
        poll(nullptr, 0, 2);
      }
      check(!fs::exists(socket), "old server socket remains");
    }
    while (alive(g.at("fixture"))) {
      guard();
      poll(nullptr, 0, 2);
    }
  }
  void cleanup() {
    I stop = begun + 15000000000LL;
    J clean = J::obj();
    clean["started_ns"] = now();
    clean["identities"] = J::arr();
    // Only proven identities from this manifest; pidfd prevents PID reuse
    // races.
    for (auto it = processes.rbegin(); it != processes.rend(); ++it) {
      if (alive(*it)) {
        try {
          signal_owned(*it, SIGCONT);
          signal_owned(*it, SIGTERM);
        } catch (const std::exception &e) {
          append(dir / "cleanup.stderr", std::string(e.what()) + "\n");
        }
      }
    }
    I grace = std::min(stop, now() + 200000000);
    while (now() < grace) {
      bool any = false;
      for (auto &id : processes)
        any |= alive(id);
      if (!any)
        break;
      poll(nullptr, 0, 2);
    }
    for (auto &id : processes)
      if (alive(id)) {
        try {
          signal_owned(id, SIGKILL);
        } catch (const std::exception &e) {
          append(dir / "cleanup.stderr", std::string(e.what()) + "\n");
        }
      }
    for (auto pid : observers) {
      int status = 0;
      while (waitpid(pid, &status, WNOHANG) == 0 && now() < stop)
        poll(nullptr, 0, 1);
      J e = J::obj();
      e["pid"] = int(pid);
      e["wait_status"] = status;
      event(dir / "observer-waits.ndjson", "observer_wait", e);
    }
    bool all = false;
    while (now() < stop) {
      all = true;
      for (auto &id : processes)
        all &= !alive(id);
      if (all)
        break;
      poll(nullptr, 0, 2);
    }
    for (auto &id : processes) {
      J e = id;
      e["same_identity_present"] = same(id);
      e["live"] = alive(id);
      clean["identities"].push(e);
    }
    clean["all_processes_exited"] = all;
    // Preserve all control receipts before exact owned temporary removal.
    bool removed = false;
    // std::filesystem copy cannot retain a UNIX socket. Copy regular controls
    // only.
    if (all && !tmp.empty() && fs::exists(tmp)) {
      try {
        fs::create_directories(dir / "controls");
        for (auto &e : fs::recursive_directory_iterator(tmp)) {
          auto dest = dir / "controls" / e.path().lexically_relative(tmp);
          if (e.is_directory())
            fs::create_directories(dest);
          else if (e.is_regular_file() && !e.is_symlink())
            fs::copy_file(e.path(), dest, fs::copy_options::overwrite_existing);
        }
        struct stat st{};
        check(lstat(tmp.c_str(), &st) == 0 && st.st_uid == getuid() &&
                  S_ISDIR(st.st_mode) && !fs::is_symlink(tmp),
              "cleanup root changed");
        fs::remove_all(tmp);
        removed = !fs::exists(tmp);
      } catch (const std::exception &e) {
        append(dir / "cleanup.stderr", std::string(e.what()) + "\n");
      }
    }
    clean["temporary_directory_removed"] = removed;
    clean["finished_ns"] = now();
    m["cleanup"] = clean;
    m["phase"] = "finalized";
    m["end_ns"] = now();
    persist();
  }
  J execute() {
    try {
      if (fs::exists(root / "HOLD") && !fs::exists(root / "RELEASE")) {
        std::cout << "PREPARED " << (dir / "manifest.json").string()
                  << std::endl;
        waitfile(root / "RELEASE", now() + 60000000000LL);
        begun = now();
        deadline = begun + 13000000000LL;
        m["runtime_epoch_ns"] = begun;
        m["active_deadline_ns"] = deadline;
        persist();
      }
      m["tmux_version"] = tmux({"-V"});
      check(m["tmux_version"].s == "tmux 3.7c\n", "tmux version drift");
      persist();
      generation(0, true);
      if (mode == "pane_recreate" || mode == "server_recreate") {
        end_first(mode == "server_recreate");
        generation(1, mode == "server_recreate");
      }
    } catch (const std::exception &e) {
      m["runtime_error"] = e.what();
      append(dir / "runner.stderr", std::string(e.what()) + "\n");
      persist();
    }
    cleanup();
    J result = compare(dir, bed / "expected", mode);
    if (m.o.count("runtime_error")) {
      result["result"] = "reject";
      result["clean_success"] = false;
      result["reasons"].push(m["runtime_error"]);
    }
    save(dir / "comparison.json", result);
    std::ostringstream report;
    report << "Q pilot/case: " << mode << "\nResult: " << result["result"].s
           << "\n";
    for (auto &r : result["reasons"].a)
      report << "- " << r.s << "\n";
    report << "Semantic completion, acceptance and turn end remain unknown.\n";
    write(dir / "report.md", report.str());
    result["run_directory"] = dir.string();
    return result;
  }
};
static J negative(const fs::path &bed, const fs::path &root,
                  const fs::path &healthy, const std::string &mode) {
  fs::path d = root / (mode + "-" + std::to_string(now()));
  check(fs::create_directory(d), "negative collision");
  for (auto &e : fs::directory_iterator(healthy)) {
    auto target = d / e.path().filename();
    fs::copy(e.path(), target, fs::copy_options::recursive);
  }
  // Keep the original manifest and evidence intact except the specified input
  // mutation.
  fs::path capture = d / "g0/capture.bin";
  if (mode == "missing_capture")
    check(fs::remove(capture), "missing negative source capture");
  else
    write(capture, read(bed / "expected/cases" / mode / "wire.bin"));
  J result = compare(d, bed / "expected", mode);
  save(d / "negative-comparison.json", result);
  write(d / "negative-report.md", result.dump() + "\n");
  J index = load(root / "runtime-index.json"), entry = J::obj();
  entry["directory"] = d.string();
  entry["ownership_manifest"] = (d / "manifest.json").string();
  entry["mode"] = mode;
  entry["derived_from"] = healthy.string();
  entry["runtime_spawned"] = false;
  index["runs"].push(entry);
  save(root / "runtime-index.json", index);
  result["run_directory"] = d.string();
  return result;
}
static int suite(const fs::path &bed, const fs::path &root, bool matrix) {
  check(!fs::exists(root / "runtime-index.json"),
        "suite root must have no prior runtime index");
  fs::create_directories(root);
  J index = J::obj();
  index["runs"] = J::arr();
  index["scope"] =
      matrix ? "witness_full_frozen_matrix" : "builder_bounded_pilot";
  save(root / "runtime-index.json", index);
  std::vector<std::string> modes = {
      "normal",           "burst",       "onlcr",          "screen",
      "false_completion", "sink_loss",   "pause",          "disconnect",
      "delete",           "duplicate",   "reorder",        "pane_recreate",
      "server_recreate",  "late_attach", "missing_capture"};
  J results = J::arr();
  std::string healthy;
  bool complete = true;
  std::vector<I> maxima;
  I global = 0;
  for (auto &mode : modes) {
    int count = matrix ? ((mode == "normal" || mode == "burst" ||
                           mode == "false_completion")
                              ? 30
                          : mode == "missing_capture" ? 1
                                                      : 10)
                       : 1;
    for (int n = 0; n < count; ++n) {
      J r;
      if (mode == "delete" || mode == "duplicate" || mode == "reorder" ||
          mode == "missing_capture") {
        if (healthy.empty()) {
          J skip = J::obj();
          skip["mode"] = mode;
          skip["result"] = "blocked_no_healthy_normal";
          results.push(skip);
          complete = false;
          continue;
        }
        r = negative(bed, root, healthy, mode);
      } else {
        Run run(bed, root, mode);
        r = run.execute();
      }
      if (mode == "normal" && r["clean_success"].n) {
        if (healthy.empty())
          healthy = r["run_directory"].s;
        I max = r["maximum_latency_ns"].n;
        maxima.push_back(max);
        global = std::max(global, max);
      }
      bool rejection = mode == "sink_loss" || mode == "disconnect" ||
                       mode == "delete" || mode == "duplicate" ||
                       mode == "reorder" || mode == "missing_capture";
      bool outcome = r["clean_success"].n == !rejection;
      if (rejection && (mode == "sink_loss" || mode == "disconnect")) {
        outcome &= r.o.count("failure_detection_latency_ns") &&
                   r["failure_detection_latency_ns"].n >= 0 &&
                   r["failure_detection_latency_ns"].n <= 1000000000;
        auto man = load(fs::path(r["run_directory"].s) / "manifest.json");
        outcome &= man["cleanup"]["all_processes_exited"].n &&
                   man["cleanup"]["temporary_directory_removed"].n &&
                   !man.o.count("runtime_error");
      }
      r["expected_case_outcome_observed"] = outcome;
      complete &= outcome;
      results.push(r);
      save(root / "results.json", results);
      std::cout << mode << " " << r["result"].s
                << " expected_outcome=" << outcome << " "
                << r["run_directory"].s << std::endl;
    }
  }
  J summary = J::obj();
  summary["scope"] = matrix ? "full_matrix" : "pilot_only_not_qualification";
  summary["case_results"] = results;
  summary["normal_marker_samples"] = I(maxima.size()) * 256;
  summary["normal_global_maximum_ns"] = global;
  if (matrix && maxima.size() == 30) {
    std::sort(maxima.begin(), maxima.end());
    summary["normal_p95_of_run_maxima_ns"] = maxima[28];
    complete &= maxima[28] <= 500000000 && global <= 1000000000;
  } else
    summary["normal_p95_of_run_maxima_ns"] = J();
  summary["expected_outcomes_observed"] = complete;
  save(root / "summary.json", summary);
  return complete ? 0 : 2;
}
} // namespace q
int main(int argc, char **argv) {
  using namespace q;
  try {
    check(
        sha("") ==
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "SHA-256 empty selfcheck");
    check(
        sha("abc") ==
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        "SHA-256 abc selfcheck");
    check(argc >= 2,
          "usage: tq fixture MODE DATA CONTROL | sink DATA CONTROL SEGMENT | "
          "compare RUN EXPECTED MODE | suite BED FRESH_ROOT pilot|matrix | run "
          "BED ROOT MODE | hold CONTROL | verify BED");
    std::string cmd = argv[1];
    if (cmd == "fixture") {
      check(argc == 5, "fixture arguments");
      return fixture(argv[2], argv[3], argv[4]);
    }
    if (cmd == "sink") {
      check(argc == 5, "sink arguments");
      return sink(argv[2], argv[3], argv[4]);
    }
    if (cmd == "hold") {
      check(argc == 3, "hold arguments");
      fs::path c = argv[2];
      save(c / "ready", ident(getpid()));
      waitfile(c / "stop", now() + 14500000000LL);
      return 0;
    }
    if (cmd == "verify") {
      check(argc == 3, "verify arguments");
      verify_oracle(fs::absolute(argv[2]));
      std::cout << "frozen oracle verified\n";
      return 0;
    }
    if (cmd == "compare") {
      check(argc == 5, "compare arguments");
      J r = compare(fs::absolute(argv[2]), fs::absolute(argv[3]), argv[4]);
      std::cout << r.dump() << "\n";
      return r["clean_success"].n ? 0 : 2;
    }
    if (cmd == "suite") {
      check(argc == 5, "suite arguments");
      check(std::string(argv[4]) == "pilot" || std::string(argv[4]) == "matrix",
            "suite population");
      return suite(fs::absolute(argv[2]), fs::absolute(argv[3]),
                   std::string(argv[4]) == "matrix");
    }
    if (cmd == "run") {
      check(argc == 5, "run arguments");
      Run r(fs::absolute(argv[2]), fs::absolute(argv[3]), argv[4]);
      auto out = r.execute();
      std::cout << out.dump() << "\n";
      return out["clean_success"].n ? 0 : 2;
    }
    throw std::runtime_error("unknown command");
  } catch (const std::exception &e) {
    std::cerr << e.what() << "\n";
    return 2;
  }
}
