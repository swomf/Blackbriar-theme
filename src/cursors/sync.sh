#!/usr/bin/env bash

set -euo pipefail

repo="https://github.com/vinceliuice/Qogir-icon-theme.git"
revision="${1:-master}"
cursor_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
checkout="$cursor_dir/sparse-checkout"

cleanup() {
  rm -rf "$checkout"
}
trap cleanup EXIT HUP INT TERM

if [[ $# -gt 1 ]]; then
  echo "Usage: ./src/cursors/sync.sh [optional ref]" >&2
  exit 1
fi

mkdir -p "$checkout"
git -C "$checkout" init --quiet
git -C "$checkout" sparse-checkout set "src/cursors/dist-Dark/"
git -C "$checkout" fetch --quiet --depth=1 --filter=blob:none "$repo" "$revision"
git -C "$checkout" checkout --quiet --detach FETCH_HEAD

resolved_revision="$(git -C "$checkout" rev-parse HEAD)"
upstream_cursors="${checkout}/src/cursors/dist-Dark/cursors"

if [[ ! -f "${upstream_cursors}/default" ]]; then
  echo "ERROR: qogir cursors not found at ${resolved_revision}"
  exit 1
fi

if [[ -n "$(find -L "$upstream_cursors" -type l -print -quit)" ]]; then
  echo "ERROR: qogir cursors have broken symlink (upstream's fault)"
  exit 1
fi

rm -rf "${cursor_dir}/cursors"
cp -a "$upstream_cursors" "${cursor_dir}/cursors"
printf '%s\n' "$resolved_revision" >"${cursor_dir}/UPSTREAM_REVISION"

echo "synced Qogir cursors at ${resolved_revision}."
