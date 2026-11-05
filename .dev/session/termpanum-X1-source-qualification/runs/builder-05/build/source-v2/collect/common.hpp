// Q-local experimental helpers; not a product interface. Linux/POSIX, C++17.
#pragma once
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <fcntl.h>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <poll.h>
#include <signal.h>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <termios.h>
#include <unistd.h>
#include <vector>
namespace q {
namespace fs = std::filesystem;
using I = long long;
inline I now() {
  timespec t{};
  clock_gettime(CLOCK_MONOTONIC, &t);
  return I(t.tv_sec) * 1000000000 + t.tv_nsec;
}
inline void check(bool b, const std::string &s) {
  if (!b)
    throw std::runtime_error(s);
}
inline std::string read(const fs::path &p) {
  std::ifstream f(p, std::ios::binary);
  check(bool(f), "missing/unreadable " + p.string());
  return {std::istreambuf_iterator<char>(f), {}};
}
inline void write(const fs::path &p, const std::string &s) {
  std::ofstream f(p, std::ios::binary);
  f << s;
  check(bool(f), "write " + p.string());
}
inline void append(const fs::path &p, const std::string &s) {
  std::ofstream f(p, std::ios::binary | std::ios::app);
  f << s;
  check(bool(f), "append " + p.string());
}
inline std::string quote(const std::string &s) {
  std::string o = "\"";
  for (unsigned char c : s) {
    if (c == '"' || c == '\\')
      o += '\\', o += c;
    else if (c < 32) {
      char b[7];
      snprintf(b, sizeof b, "\\u%04x", c);
      o += b;
    } else
      o += c;
  }
  return o + '"';
}
struct J {
  enum T { Null, Number, String, Boolean, Object, Array } t = Null;
  I n = 0;
  std::string s;
  std::map<std::string, J> o;
  std::vector<J> a;
  J() = default;
  J(I x) : t(Number), n(x) {}
  J(int x) : J(I(x)) {}
  J(bool x) : t(Boolean), n(x) {}
  J(const std::string &x) : t(String), s(x) {}
  J(const char *x) : J(std::string(x)) {}
  static J obj() {
    J j;
    j.t = Object;
    return j;
  }
  static J arr() {
    J j;
    j.t = Array;
    return j;
  }
  J &operator[](const std::string &k) {
    if (t == Null)
      t = Object;
    check(t == Object, "JSON object required");
    return o[k];
  }
  const J &at(const std::string &k) const {
    auto it = o.find(k);
    check(it != o.end(), "missing JSON field " + k);
    return it->second;
  }
  void push(J j) {
    if (t == Null)
      t = Array;
    check(t == Array, "JSON array required");
    a.push_back(std::move(j));
  }
  std::string str() const {
    check(t == String, "JSON string required");
    return s;
  }
  I num() const {
    check(t == Number, "JSON integer required");
    return n;
  }
  std::string dump() const {
    if (t == Null)
      return "null";
    if (t == Number)
      return std::to_string(n);
    if (t == String)
      return quote(s);
    if (t == Boolean)
      return n ? "true" : "false";
    std::string z = t == Array ? "[" : "{";
    bool first = true;
    if (t == Array)
      for (auto &v : a) {
        if (!first)
          z += ',';
        first = false;
        z += v.dump();
      }
    else
      for (auto &v : o) {
        if (!first)
          z += ',';
        first = false;
        z += quote(v.first) + ':' + v.second.dump();
      }
    return z + (t == Array ? "]" : "}");
  }
  static J parse(const std::string &s) {
    size_t p = 0;
    auto ws = [&] {
      while (p < s.size() && isspace(static_cast<unsigned char>(s[p])))
        ++p;
    };
    auto rec = [&](auto &&self) -> J {
      ws();
      check(p < s.size(), "JSON EOF");
      char c = s[p++];
      if (c == '{' || c == '[') {
        J j = c == '{' ? obj() : arr();
        ws();
        if (p < s.size() && s[p] == (c == '{' ? '}' : ']')) {
          ++p;
          return j;
        }
        while (true) {
          if (c == '{') {
            J k = self(self);
            check(k.t == String, "JSON key");
            ws();
            check(p < s.size() && s[p++] == ':', "JSON colon");
            j[k.s] = self(self);
          } else
            j.push(self(self));
          ws();
          check(p < s.size(), "JSON close");
          char d = s[p++];
          if (d == (c == '{' ? '}' : ']'))
            break;
          check(d == ',', "JSON comma");
        }
        return j;
      }
      if (c == '"') {
        std::string v;
        while (true) {
          check(p < s.size(), "JSON string EOF");
          char d = s[p++];
          if (d == '"')
            break;
          if (d == '\\') {
            check(p < s.size(), "JSON escape EOF");
            d = s[p++];
            if (d == 'n')
              d = '\n';
            else if (d == 'r')
              d = '\r';
            else if (d == 't')
              d = '\t';
            else if (d == 'u') {
              check(p + 4 <= s.size(), "JSON unicode EOF");
              int u = std::stoi(s.substr(p, 4), nullptr, 16);
              p += 4;
              check(u < 128, "JSON non-ASCII escape unsupported");
              d = char(u);
            } else
              check(d == '"' || d == '\\' || d == '/', "JSON escape");
          }
          v += d;
        }
        return J(v);
      }
      if (c == 't') {
        check(s.substr(p, 3) == "rue", "JSON true");
        p += 3;
        return J(true);
      }
      if (c == 'f') {
        check(s.substr(p, 4) == "alse", "JSON false");
        p += 4;
        return J(false);
      }
      if (c == 'n') {
        check(s.substr(p, 3) == "ull", "JSON null");
        p += 3;
        return J();
      }
      --p;
      size_t start = p;
      if (s[p] == '-')
        ++p;
      while (p < s.size() && isdigit(static_cast<unsigned char>(s[p])))
        ++p;
      check(p > start, "JSON integer");
      return J(std::stoll(s.substr(start, p - start)));
    };
    J j = rec(rec);
    ws();
    check(p == s.size(), "JSON trailing data");
    return j;
  }
};
inline J load(const fs::path &p) { return J::parse(read(p)); }
inline void save(const fs::path &p, const J &j) {
  auto tmp = p;
  tmp += ".new";
  write(tmp, j.dump() + "\n");
  fs::rename(tmp, p);
}
inline std::vector<J> lines(const fs::path &p) {
  std::istringstream in(read(p));
  std::string s;
  std::vector<J> v;
  while (std::getline(in, s))
    if (!s.empty())
      v.push_back(J::parse(s));
  return v;
}
inline void event(const fs::path &p, const std::string &kind, J j = J::obj()) {
  j["kind"] = kind;
  j["monotonic_ns"] = now();
  append(p, j.dump() + "\n");
}
inline J ident(pid_t pid) {
  J j = J::obj();
  j["pid"] = int(pid);
  std::string s = read("/proc/" + std::to_string(pid) + "/stat");
  auto x = s.rfind(')');
  check(x != std::string::npos, "proc stat");
  std::istringstream in(s.substr(x + 2));
  std::string v;
  for (int n = 3; n <= 22; ++n) {
    check(bool(in >> v), "proc start");
    if (n == 3)
      j["state"] = v;
    if (n == 22)
      j["start_ticks"] = v;
  }
  j["uid"] = int(getuid());
  return j;
}
inline bool same(const J &id) {
  try {
    auto a = ident(pid_t(id.at("pid").num()));
    return a.at("start_ticks").s == id.at("start_ticks").s;
  } catch (...) {
    return false;
  }
}
inline bool alive(const J &id) {
  if (!same(id))
    return false;
  auto s = ident(pid_t(id.at("pid").num())).at("state").s;
  return s != "Z" && s != "X";
}
inline void signal_owned(const J &id, int sig) {
  int fd = int(syscall(SYS_pidfd_open, pid_t(id.at("pid").num()), 0));
  check(fd >= 0, "owned pidfd_open failed");
  if (!same(id)) {
    close(fd);
    throw std::runtime_error("PID incarnation no longer owned");
  }
  int rc = int(syscall(SYS_pidfd_send_signal, fd, sig, nullptr, 0));
  close(fd);
  check(rc == 0, "owned pidfd_send_signal failed");
}
inline void waitfile(const fs::path &p, I deadline) {
  while (!fs::exists(p)) {
    check(now() < deadline, "timeout waiting " + p.string());
    poll(nullptr, 0, 2);
  }
}
inline void fullwrite(int fd, const char *b, size_t n) {
  while (n) {
    ssize_t k = ::write(fd, b, n);
    if (k < 0 && errno == EINTR)
      continue;
    check(k > 0, "write(2) failed");
    b += k;
    n -= size_t(k);
  }
}
inline std::string shell(const std::string &s) {
  std::string z = "'";
  for (char c : s)
    z += c == '\'' ? "'\\''" : std::string(1, c);
  return z + '\'';
}
inline std::string self() {
  char b[4096];
  ssize_t n = readlink("/proc/self/exe", b, sizeof b);
  check(n > 0 && size_t(n) < sizeof b, "self exe");
  return std::string(b, size_t(n));
}
// Small self-contained SHA-256; used on actual source/config/artifacts, no
// subprocess.
inline std::string sha(const std::string &input) {
  static const uint32_t k[] = {
      0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
      0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
      0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
      0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
      0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
      0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
      0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
      0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
      0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
      0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2};
  auto r = [](uint32_t x, int n) { return (x >> n) | (x << (32 - n)); };
  std::vector<unsigned char> b(input.begin(), input.end());
  uint64_t len = uint64_t(b.size()) * 8;
  b.push_back(128);
  while (b.size() % 64 != 56)
    b.push_back(0);
  for (int i = 7; i >= 0; --i)
    b.push_back(static_cast<unsigned char>(len >> (8 * i)));
  uint32_t h[] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                  0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};
  for (size_t p = 0; p < b.size(); p += 64) {
    uint32_t w[64];
    for (int i = 0; i < 16; ++i)
      w[i] = (uint32_t(b[p + 4 * i]) << 24) |
             (uint32_t(b[p + 4 * i + 1]) << 16) |
             (uint32_t(b[p + 4 * i + 2]) << 8) | b[p + 4 * i + 3];
    for (int i = 16; i < 64; ++i)
      w[i] = w[i - 16] +
             (r(w[i - 15], 7) ^ r(w[i - 15], 18) ^ (w[i - 15] >> 3)) +
             w[i - 7] + (r(w[i - 2], 17) ^ r(w[i - 2], 19) ^ (w[i - 2] >> 10));
    uint32_t a = h[0], c = h[2], d = h[3], e = h[4], f = h[5], g = h[6],
             hh = h[7], bb = h[1];
    for (int i = 0; i < 64; ++i) {
      uint32_t t1 = hh + (r(e, 6) ^ r(e, 11) ^ r(e, 25)) +
                    ((e & f) ^ (~e & g)) + k[i] + w[i],
               t2 = (r(a, 2) ^ r(a, 13) ^ r(a, 22)) +
                    ((a & bb) ^ (a & c) ^ (bb & c));
      hh = g;
      g = f;
      f = e;
      e = d + t1;
      d = c;
      c = bb;
      bb = a;
      a = t1 + t2;
    }
    uint32_t v[] = {a, bb, c, d, e, f, g, hh};
    for (int i = 0; i < 8; ++i)
      h[i] += v[i];
  }
  std::ostringstream o;
  for (auto x : h)
    o << std::hex << std::setw(8) << std::setfill('0') << x;
  return o.str();
}
inline std::string hashfile(const fs::path &p) { return sha(read(p)); }
inline J term() {
  termios t{};
  check(tcgetattr(STDOUT_FILENO, &t) == 0, "tcgetattr");
  winsize w{};
  check(ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) == 0, "TIOCGWINSZ");
  J j = J::obj();
  j["iflag"] = I(t.c_iflag);
  j["oflag"] = I(t.c_oflag);
  j["cflag"] = I(t.c_cflag);
  j["lflag"] = I(t.c_lflag);
  j["ispeed"] = I(cfgetispeed(&t));
  j["ospeed"] = I(cfgetospeed(&t));
  j["cc"] = J::arr();
  for (auto c : t.c_cc)
    j["cc"].push(int(c));
  j["columns"] = int(w.ws_col);
  j["rows"] = int(w.ws_row);
  return j;
}
int fixture(const std::string &, const fs::path &, const fs::path &);
int sink(const fs::path &, const fs::path &, const std::string &);
J compare(const fs::path &, const fs::path &, const std::string &);
} // namespace q
