#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

required=(
  AGENTS.md
  README.md
  docs/architecture/IMPLEMENTATION_BASELINE.md
  docs/architecture/LAYER_TO_REPOSITORY_MAP.md
  docs/architecture/CONTRACT_MATRIX.md
  docs/architecture/DEPENDENCY_RULES.md
  docs/architecture/VALIDATION_MATRIX.md
  docs/architecture/CODEX_EXECUTION_PLAN.md
)

for f in "${required[@]}"; do
  test -f "$ROOT/$f" || { echo "MISSING: $f"; exit 1; }
done

for d in core/semantic core/contracts core/identity runtime/state runtime/events runtime/lifecycle runtime/history runtime/persistence runtime/recovery agents orchestration workflows capabilities adapters/providers domains governance observability app tests; do
  test -d "$ROOT/$d" || { echo "MISSING DIRECTORY: $d"; exit 1; }
done

# Foundation-level dependency guardrails. This is intentionally conservative until
# the implementation language is selected; it checks obvious upward/vendor coupling.
if grep -RInE '(^|/)(core|runtime)/.*(import|require).*(@|vendor|provider|react|next|fastapi|django|openai|google|anthropic)' "$ROOT/core" "$ROOT/runtime" 2>/dev/null; then
  echo "Potential prohibited foundation dependency detected. Review required."
  exit 1
fi

echo "CCH-OS repository foundation validation: PASS"
