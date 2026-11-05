#include "../collect/common.hpp"
namespace q {
J compare(const fs::path &run, const fs::path &expected,
          const std::string &mode) {
  J r = J::obj();
  r["mode"] = mode;
  r["semantic_completion"] = "unknown";
  r["acceptance"] = "unknown";
  r["turn_end"] = "unknown";
  r["reasons"] = J::arr();
  r["markers"] = J::arr();
  bool ok = true;
  auto require = [&](bool b, const std::string &s) {
    if (!b) {
      ok = false;
      r["reasons"].push(s);
    }
  };
  try {
    auto m = load(run / "manifest.json");
    require(m.at("expected_manifest_sha256").str() ==
                hashfile(expected / "manifest.json"),
            "oracle manifest identity mismatch");
    require(m.at("phase").str() == "finalized",
            "bundle incomplete/not finalized");
    require(m.at("cleanup").at("all_processes_exited").n == 1,
            "owned cleanup unproven");
    require(m.at("cleanup").at("temporary_directory_removed").n == 1,
            "temporary controls remain");
    std::string kind = mode == "onlcr" ? "onlcr"
                       : mode == "screen" || mode == "pane_recreate" ||
                               mode == "server_recreate"
                           ? "screen"
                       : mode == "false_completion" ? "false_completion"
                       : mode == "burst" || mode == "sink_loss" ? "burst"
                                                                : "normal";
    require(
        m.at("generations").a.size() ==
            ((mode == "pane_recreate" || mode == "server_recreate") ? 2 : 1),
        "required source incarnation absent");
    for (auto &g : m.at("generations").a) {
      fs::path d = run / g.at("directory").str();
      std::string actual = read(d / "capture.bin");
      std::string want = read(expected / "cases" / kind / "wire.bin");
      if (mode == "late_attach")
        want = want.substr(128 * 1024);
      require(actual == want, "byte mismatch: expected " +
                                  std::to_string(want.size()) + " actual " +
                                  std::to_string(actual.size()));
      r["capture_sha256"] = sha(actual);
      r["capture_bytes"] = I(actual.size());
      auto before = load(d / "termios.before.json"),
           after = load(d / "termios.after.json");
      require(before.dump() == after.dump(), "termios changed during emission");
      require(before.at("oflag").num() ==
                  (mode == "onlcr" ? I(OPOST | ONLCR) : 0),
              "unexpected output flags");
      require(before.at("columns").num() == 80 && before.at("rows").num() == 24,
              "terminal dimensions mismatch");
      auto control = lines(d / "fixture-control.ndjson");
      bool exited = false;
      I quietStart = 0, quietEnd = 0;
      for (auto &e : control) {
        auto k = e.at("kind").str();
        if (k == "direct_child_wait") {
          exited = e.at("exited").n && e.at("exit_code").num() == 0;
        }
        if (k == "quiet_begin_known_alive")
          quietStart = e.at("monotonic_ns").num();
        if (k == "quiet_end_known_alive")
          quietEnd = e.at("monotonic_ns").num();
      }
      require(exited, "missing successful independent direct child wait");
      auto emissions = lines(d / "emission.ndjson"),
           chunks = lines(d / "records.ndjson");
      I end = 0;
      for (auto &e : chunks) {
        require(e.at("start").num() == end, "append offset discontinuity");
        end = e.at("end").num();
        require(e.at("append_complete_ns").num() >= e.at("observed_ns").num(),
                "append time precedes receipt");
      }
      require(end == I(actual.size()),
              "append coverage does not match capture length");
      if (mode == "normal" || mode == "onlcr") {
        require(emissions.size() == 256, "missing marker releases");
        I max = 0;
        for (size_t n = 0; n < 256; ++n) {
          I start = I(n) * (mode == "onlcr" ? 1026 : 1024),
            finish = start + (mode == "onlcr" ? 1026 : 1024);
          I completed = 0;
          for (auto &c : chunks)
            if (c.at("end").num() >= finish) {
              completed = c.at("append_complete_ns").num();
              break;
            }
          if (n >= emissions.size() || !completed) {
            require(false, "missing marker append " + std::to_string(n));
            continue;
          }
          auto &e = emissions[n];
          require(e.at("frame").num() == I(n), "marker sequence mismatch");
          I release = e.at("release_ns").num(), latency = completed - release;
          require(latency >= 0, "negative marker latency");
          max = std::max(max, latency);
          J sample = J::obj();
          sample["frame"] = I(n);
          sample["start"] = start;
          sample["end"] = finish;
          sample["release_ns"] = release;
          sample["append_complete_ns"] = completed;
          sample["latency_ns"] = latency;
          r["markers"].push(sample);
        }
        r["maximum_latency_ns"] = max;
        if (mode == "normal")
          require(max <= 1000000000,
                  "marker visibility maximum exceeds 1000ms");
      }
      if (kind == "screen")
        require(read(d / "screen.txt") ==
                    read(expected / "cases/screen/screen.txt"),
                "rendered screen mismatch");
      if (mode == "false_completion") {
        require(quietStart > 0 && quietEnd - quietStart >= 5000000000LL,
                "five-second known-alive quiet proof missing");
        require(emissions.size() == 1, "writes during quiet interval");
        r["quiet_ns"] = quietEnd - quietStart;
      }
      require(g.at("ready_ns").num() - g.at("start_ns").num() <= 1500000000,
              "source ready exceeds 1500ms");
      I duration = g.at("capture_end_ns").num() - g.at("start_ns").num();
      if (mode == "normal")
        require(duration <= 6000000000LL, "normal capture exceeds 6s");
      if (mode == "burst")
        require(duration <= 10000000000LL, "burst capture exceeds 10s");
      require(g.at("fixture").at("start_ticks").str().size() > 0 &&
                  g.at("emitter").at("start_ticks").str().size() > 0,
              "source incarnation missing");
    }
    if (mode == "sink_loss" || mode == "disconnect") {
      auto a = load(run / "fault-action.json"),
           d = load(run / "fault-detection.json");
      require(d.at("evidence").str() == "pidfd reported actual sink exit" &&
                  d.at("reader").dump() == a.at("reader").dump(),
              "independent sink exit evidence does not match injection target");
      I latency = d.at("monotonic_ns").num() - a.at("monotonic_ns").num();
      r["failure_detection_latency_ns"] = latency;
      require(latency >= 0 && latency <= 1000000000,
              "supervised failure detection exceeds 1s or invalid");
      require(false,
              mode == "sink_loss"
                  ? "incomplete: pidfd observed bound sink exit"
                  : "gap: old sink exited; interval uncovered until new bind");
    }
    if (mode == "pause") {
      auto a = load(run / "fault-action.json"), b = load(run / "resume.json");
      require(b.at("monotonic_ns").num() - a.at("monotonic_ns").num() >=
                  3000000000LL,
              "reader pause shorter than 3s");
      r["coverage"] = "measured_complete_after_three_second_reader_pause";
      r["failure_detection_latency_ns"] = J();
    }
    if (mode == "late_attach")
      r["coverage"] = "prefix_absent_frames_0_through_127";
    if (mode == "pane_recreate" || mode == "server_recreate") {
      auto &gs = m.at("generations").a;
      require(gs.size() == 2, "second incarnation missing");
      if (gs.size() == 2) {
        auto &a = gs[0];
        auto &b = gs[1];
        require(a.at("fixture").dump() != b.at("fixture").dump(),
                "inherited fixture incarnation");
        require(a.at("pane_id").str() != b.at("pane_id").str() ||
                    a.at("server").dump() != b.at("server").dump(),
                "pane/server binding did not change");
        if (mode == "server_recreate")
          require(a.at("server").dump() != b.at("server").dump(),
                  "server incarnation reused");
        require(b.at("ready_ns").num() > a.at("capture_end_ns").num(),
                "new binding reused prior freshness");
      }
      r["inherited_freshness"] = false;
    }
  } catch (const std::exception &e) {
    require(false, e.what());
  }
  r["result"] = ok ? "supported_case" : "reject";
  r["clean_success"] = ok;
  return r;
}
} // namespace q
