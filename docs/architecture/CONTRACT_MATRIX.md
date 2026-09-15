# CCH-OS Contract → Implementation Matrix v0.1

| Contract family | Must remain distinct from | Initial implementation boundary | Required proof |
|---|---|---|---|
| Semantic Model | representation, storage | `core/semantic` | representation-independence tests |
| Identity | ID, reference, version | `core/identity` | identity/reference/version tests |
| Component/Structure/Composition | storage representation | `core/semantic` | structural contract tests |
| Context | state/history | `core/contracts` | context isolation tests |
| State | event/history/trace/audit | `runtime/state` | authoritative transition tests |
| Event | state/history | `runtime/events` | event/state separation tests |
| History | state/event | `runtime/history` | historical reconstruction tests |
| Observation | interpretation/evaluation | `core/contracts` | semantic separation tests |
| Interpretation | evaluation/decision | `core/contracts` | semantic separation tests |
| Evaluation | decision/action | `core/contracts` | semantic separation tests |
| Decision | authorization/action | `orchestration`, `governance` | authority tests |
| Authorization | capability/tool/action | `governance` | unauthorized-operation tests |
| Action | execution/tool | `runtime` | action boundary tests |
| Agent | capability/tool/authority | `agents` | agent authority tests |
| Capability | tool/authority | `capabilities` | capability/tool separation tests |
| Tool | capability/authority | `adapters` | adapter invocation tests |
| Workflow | task/step/action | `workflows` | workflow boundary tests |
| Task | workflow/step/action | `workflows` | task execution tests |
| Step | task/action | `workflows` | step semantics tests |
| Provenance | lineage | `core/contracts`, `runtime/history` | provenance tests |
| Lineage | provenance | `runtime/history` | lineage continuity tests |
| Version | identity/reference | `core/identity` | version/reference tests |
| Failure | success | `runtime/recovery` | failure transparency tests |
| Recovery Authority | failure owner | `runtime/recovery`, `governance` | recovery authority tests |

## Rule

A shared data structure may contain multiple fields, but implementation must not erase semantic distinctions merely because values are serialized together.

Serialization is representation, not the semantic model.
