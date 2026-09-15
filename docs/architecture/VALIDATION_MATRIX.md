# CCH-OS Implementation Validation Matrix v0.1

The architecture specification requires contract tests, state tests, workflow tests, authority tests, adapter compatibility tests, recovery interruption tests, and end-to-end testability.

| Gate | Proof target | Minimum evidence |
|---|---|---|
| V-01 | semantic separation | contract tests |
| V-02 | identity/ID/reference/version | counterexample + unit tests |
| V-03 | state/event/history separation | transition + event tests |
| V-04 | observation→interpretation→evaluation→decision→action | pipeline boundary tests |
| V-05 | capability/tool/authority separation | unauthorized invocation tests |
| V-06 | workflow/task/step/action | workflow execution tests |
| V-07 | authoritative state mutation | mutation-path tests |
| V-08 | governance/authorization | allow/deny tests |
| V-09 | persistence independence | alternate persistence implementation tests |
| V-10 | adapter replaceability | contract compatibility tests |
| V-11 | failure transparency | failed operation cannot produce success state |
| V-12 | recovery | interruption/resume/retry tests |
| V-13 | provenance/lineage | source-to-derived trace tests |
| V-14 | observability | trace/history/audit separation tests |
| V-15 | extensibility | add/replace component without kernel change |
| V-16 | end-to-end | representative vertical slice |

## Status vocabulary

- NOT STARTED
- IN PROGRESS
- PASS
- FAIL
- BLOCKED
- NOT APPLICABLE

A test result must never be inferred from documentation alone.

## Required evidence

For every PASS:

```text
Contract
  ↓
Test
  ↓
Execution
  ↓
Result
  ↓
Evidence
```

Architecture claims remain claims until executable evidence exists.
