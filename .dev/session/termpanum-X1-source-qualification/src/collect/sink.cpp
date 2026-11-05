#include "common.hpp"
namespace q {
int sink(const fs::path &d, const fs::path &tmp, const std::string &segment) {
  int out = open((d / "capture.bin").c_str(),
                 O_CREAT | O_WRONLY | O_APPEND | O_CLOEXEC, 0600);
  check(out >= 0, "capture open");
  off_t off = lseek(out, 0, SEEK_END);
  check(off >= 0, "capture offset");
  save(tmp / ("sink." + segment + ".ready"), ident(getpid()));
  I deadline = now() + 14500000000LL;
  char buf[65536];
  I seq = 0;
  while (now() < deadline) {
    pollfd p{0, POLLIN | POLLHUP, 0};
    int rc = poll(&p, 1, 25);
    if (rc < 0 && errno == EINTR)
      continue;
    check(rc >= 0, "sink poll");
    if (!rc)
      continue;
    I observed = now();
    ssize_t n = ::read(0, buf, sizeof buf);
    if (n < 0 && errno == EINTR)
      continue;
    check(n >= 0, "sink read");
    if (n == 0) {
      close(out);
      J x = J::obj();
      x["bytes"] = I(off);
      x["sequence"] = seq;
      save(tmp / ("sink." + segment + ".exited"), x);
      return 0;
    }
    fullwrite(out, buf, size_t(n));
    I complete = now();
    J j = J::obj();
    j["segment"] = segment;
    j["sequence"] = seq++;
    j["start"] = I(off);
    off += n;
    j["end"] = I(off);
    j["observed_ns"] = observed;
    j["append_complete_ns"] = complete;
    j["received_ns"] = complete;
    append(d / "records.ndjson", j.dump() + "\n");
  }
  close(out);
  throw std::runtime_error("sink watchdog timeout");
}
} // namespace q
