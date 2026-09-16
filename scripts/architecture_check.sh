#!/usr/bin/env bash
set -euo pipefail

fail() { echo "ARCHITECTURE CHECK: FAIL — $1" >&2; exit 1; }

for d in core/semantic core/contracts core/identity runtime/state runtime/events runtime/lifecycle runtime/history runtime/persistence runtime/recovery agents orchestration workflows capabilities adapters domains governance observability app tests docs/architecture; do
  [[ -d "$d" ]] || fail "missing repository boundary: $d"
done

[[ -f AGENTS.md ]] || fail "missing AGENTS.md"
[[ -f docs/architecture/IMPLEMENTATION_BASELINE.md ]] || fail "missing implementation baseline"
[[ -f docs/architecture/CONTRACT_MATRIX.md ]] || fail "missing contract matrix"
[[ -f docs/architecture/DEPENDENCY_RULES.md ]] || fail "missing dependency rules"
[[ -f docs/architecture/VALIDATION_MATRIX.md ]] || fail "missing validation matrix"
[[ -f docs/architecture/CODEX_EXECUTION_PLAN.md ]] || fail "missing execution plan"

# L0 must not contain implementation-provider imports/references at Stage 0.
if grep -RniE '(^|[[:space:]])(import|from|require)[[:space:]]+.*(openai|google|gemini|anthropic|langchain|crewai|autogen)' core/ 2>/dev/null; then
  fail "provider/framework dependency detected under core/"
fi

echo "ARCHITECTURE CHECK: PASS — Stage 0 repository boundaries and kernel dependency guard are present."
