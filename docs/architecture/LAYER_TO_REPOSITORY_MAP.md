# CCH-OS Layer → Repository Mapping v0.1

| Layer | Architectural responsibility | Repository boundary |
|---|---|---|
| L0 | semantic/structural foundation | `core/semantic`, `core/contracts`, `core/identity` |
| L1 | state, events, lifecycle, transitions, history, persistence interfaces, recovery | `runtime/state`, `runtime/events`, `runtime/lifecycle`, `runtime/recovery`, `runtime/history` |
| L2 | agent runtime, goals, context, interpretation/evaluation/decision/planning coordination | `agents/`, `orchestration/` |
| L3 | workflows, tasks, steps, dependencies, branching, parallelism, retry, pause/resume | `workflows/` |
| L4 | capability contracts, registry, adapter contracts, invocation normalization | `capabilities/`, `adapters/` |
| L5 | product/content/storyboard/generation/publishing/analytics domain services | `domains/` |
| L6 | application/API/UI experience | `app/` |
| L7 | external models, tools, platforms, storage, communications | `adapters/providers/`, deployment-specific integrations |

## Cross-cutting boundaries

- Governance: `governance/`
- Observability: `observability/`
- Persistence abstraction: `runtime/persistence/`
- Tests: `tests/`
- Documentation and architectural evidence: `docs/`

## Rule

The directory names are an implementation translation, not a new architectural layer model.

The repository must preserve the architecture's dependency direction and must not allow lower-level semantic contracts to depend on application or vendor implementations.

## Proposed topology

```text
CCH-OS/
├── core/
│   ├── semantic/
│   ├── contracts/
│   └── identity/
├── runtime/
│   ├── state/
│   ├── events/
│   ├── lifecycle/
│   ├── history/
│   ├── persistence/
│   └── recovery/
├── agents/
├── orchestration/
├── workflows/
├── capabilities/
├── adapters/
│   └── providers/
├── domains/
├── governance/
├── observability/
├── app/
├── tests/
└── docs/
    └── architecture/
```

This topology is the initial repository configuration. Concrete framework conventions may be added only after the implementation technology is explicitly selected.
