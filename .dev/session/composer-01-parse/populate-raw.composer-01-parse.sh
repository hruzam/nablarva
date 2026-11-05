#!/bin/sh
# Majkee's one-shot reference import. The builder never writes raw/.
# REPOSOMA selects the reposoma checkout; BED selects the installed packet.
# Verify a private staging tree before publishing; refuse to replace different raw/.
set -eu
repo=${REPOSOMA:-$HOME/reposoma}
bed=${BED:-$HOME/unikuklatrix/nablarva/.dev/session/composer-01-parse}
repo=$(cd "$repo" && pwd)
bed=$(cd "$bed" && pwd)
src=$repo/.majkee
test -f "$bed/SHA256SUMS"
stage=$(mktemp -d "$bed/.populate-raw.XXXXXX")
trap 'rm -rf "$stage"' EXIT
trap 'exit 1' HUP INT TERM
mkdir "$stage/raw"
cp -R "$src/projects/unikuklatrix_nablarva-termbrana-X0-prompt-collection/." "$stage/raw/"
for f in 01_SYNC_METHOD 02_PARSER_GATE 04_REGISTRY 05_WAY_OF_THINKING; do
  cp "$src/projects/unikuklatrix_nablarva/$f.md" "$stage/raw/"
done
cp "$src/journal/2026-10-13.md" "$stage/raw/journal.2026-10-13.md"
# This committed snapshot exactly matches the supplied manifest. The live journal does not.
git -C "$repo" show 9fd4cf2b7ad171c49e357a1a44d01ef4e40f6333:.majkee/journal/2026-10-16.md > "$stage/raw/journal.2026-10-16.md"
(
  cd "$stage"
  find raw -type f -print | LC_ALL=C sort > actual-files
  sed 's/^[0-9a-f]*  //' "$bed/SHA256SUMS" | LC_ALL=C sort > expected-files
  cmp expected-files actual-files
  test -z "$(find raw -type l -print)"
  sha256sum -c "$bed/SHA256SUMS"
)
if [ -L "$bed/raw" ]; then
  printf '%s\n' 'Refusing a symlink at raw/.' >&2
  exit 1
fi
if [ -d "$bed/raw" ]; then
  if diff -qr "$stage/raw" "$bed/raw" >/dev/null; then
    printf '%s\n' 'raw/ already matches the verified import; unchanged.'
    exit 0
  fi
  if [ -n "$(find "$bed/raw" -mindepth 1 -print -quit)" ]; then
    printf '%s\n' 'Refusing to replace a different populated raw/.' >&2
    exit 1
  fi
elif [ -e "$bed/raw" ]; then
  printf '%s\n' 'Refusing a non-directory at raw/.' >&2
  exit 1
fi
# GNU coreutils: rename replaces an empty destination, never nests raw/ inside it.
mv -T "$stage/raw" "$bed/raw"
printf '%s\n' 'Published verified raw/.'
