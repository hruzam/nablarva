# Transcript view engine: source-relative, quiet, and inert until invoked.
# Native rollouts require an explicit matching --input-format codex-rollout-0.166 or codex-rollout-0.167.
if (( ! ${+_tbv_dir} )); then
  typeset -gr _tbv_dir="${${(%):-%N}:A:h}"
fi
_tbv_render() {
  python3 -I -S -B "$_tbv_dir/transcript.py" render "$@"
}

_tbv_pin() {
  python3 -I -S -B "$_tbv_dir/transcript.py" pin "$@"
}

_tbv_select() {
  python3 -I -S -B "$_tbv_dir/transcript.py" select "$@"
}

_tbv_open() {
  python3 -I -S -B "$_tbv_dir/transcript.py" open "$@"
}

_tbv_collect() {
  python3 -I -S -B "$_tbv_dir/collector.py" collect "$@"
}

_tbv_refresh() {
  python3 -I -S -B "$_tbv_dir/collector.py" refresh "$@"
}

_tbv_status() {
  python3 -I -S -B "$_tbv_dir/collector.py" status "$@"
}

_tbv_watch() {
  python3 -I -S -B "$_tbv_dir/collector.py" watch "$@"
}
