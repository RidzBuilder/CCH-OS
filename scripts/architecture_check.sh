#!/usr/bin/env bash
set -euo pipefail
for p in core/semantic core/contracts core/identity runtime/state runtime/events runtime/history runtime/recovery agents capabilities adapters governance observability domain workflows tests; do test -d "$p" || { echo "MISSING: $p"; exit 1; }; done
if grep -R -nE 'import (google|openai|anthropic|langchain|crewai|autogen)|from (google|openai|anthropic|langchain|crewai|autogen)' core runtime 2>/dev/null; then echo "PROHIBITED PROVIDER/FRAMEWORK DEPENDENCY"; exit 1; fi
echo "FOUNDATION CHECK: PASS"
