#!/usr/bin/env bash
# Mutation check: each mutation must make the suite FAIL. Runs in a fresh /tmp copy.
set -u
SRC=/home/hruzam/unikuklatrix/nablarva/.dev/session/sublime-observer-X1-file-publish/implementation
M=$(mktemp -d /tmp/sublime-observer-mutation.XXXXXX)
trap 'rm -rf "$M"' EXIT
run() {
  rm -rf "$M/impl"; cp -r "$SRC" "$M/impl"; find "$M/impl" -name __pycache__ -prune -exec rm -rf {} +
  python3 -I -S -B - "$M/impl/SublimeObserver/$2" "$3" "$4" <<'PY'
import sys; p, old, new = sys.argv[1:4]; s = open(p).read()
assert old in s, ('pattern missing', old); open(p, 'w').write(s.replace(old, new, 1))
PY
  out=$(timeout 30 python3 -I -S -B -m unittest discover -s "$M/impl/tests" 2>&1 | tail -1)
  echo "$1 => ${out:-TIMEOUT}"
}
run "baseline-noop"       contract.py "CONTRACT_VERSION = 1" "CONTRACT_VERSION = 1"
run "no-max-delay"        contract.py "return min(entry[1] + self.debounce, entry[0] + self.max_delay)" "return entry[1] + self.debounce"
run "state-before-text"   contract.py "                atomic_write(vdir, name, text.encode(TEXT_FILE_ENCODING, 'replace'))" "                atomic_write(vdir, 'state.json', ('{\"text_file\": \"%s\"}' % name).encode()); atomic_write(vdir, name, text.encode(TEXT_FILE_ENCODING, 'replace'))"
run "keep-only-current"   contract.py "        if share['prev']:" "        if False:"
run "no-share-guard"      publisher.py "        if not self.active or view.id() not in self.shares:" "        if not self.active:"
run "current-for-many"    contract.py "if len(self._shares) == 1 else None" "if self._shares else None"
run "no-seal-check"       publisher.py "        reason = contract.sealed_reason(view.file_name())
        if reason:
            sublime.status_message" "        reason = None
        if reason:
            sublime.status_message"
run "always-read-text"    publisher.py "lambda revision: store.text_rev.get(share_id) != revision" "lambda revision: True"
run "live-ignored"        contract.py "            if verdict == 'live':" "            if False:"
run "no-revision-guard"   publisher.py "    if view.change_count() != revision:
        return None" "    pass"
run "no-fchmod"           contract.py "            os.fchmod(fd, 0o600)" "            pass"
run "no-resurrect-guard"  contract.py "            if not self.live or share_id in self._removed:" "            if not self.live:"
# Step 2 fixes (trial-exposed defects)
run "poll-ignores-selection" publisher.py "    return (tuple(view.viewport_position()), visible.begin(), visible.end(), view.file_name(),
            len(selection), regions)" "    return (tuple(view.viewport_position()), visible.begin(), visible.end(), view.file_name(), 0, ())"
run "no-on-exit"          publisher.py "so run the same cleanup.\"\"\"
        plugin_unloaded()" "so run the same cleanup.\"\"\"
        pass"
