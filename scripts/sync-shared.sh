#!/usr/bin/env bash
# Copy the shared artifact template and protocols into every plugin.
# Each plugin installs on its own, so each needs its own copy under shared/.
# Usage: scripts/sync-shared.sh          (copy)
#        scripts/sync-shared.sh --check  (exit 1 if any copy is out of date)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
status=0
for plugin in "$root"/plugins/*/; do
  dest="${plugin}shared"
  if [[ "${1:-}" == "--check" ]]; then
    diff -rq "$root/shared" "$dest" >/dev/null 2>&1 || { echo "out of date: ${dest#$root/}"; status=1; }
  else
    rm -rf "$dest" && mkdir -p "$dest" && cp "$root"/shared/* "$dest"/
  fi
done
exit $status
