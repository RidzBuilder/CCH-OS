# CCH-OS Dependency Rules v0.1

## Direction

```text
L7 External Systems
        ↑
L6 Application Experience
        ↑
L5 Domain Services
        ↑
L4 Capability / Tool
        ↑
L3 Workflow / Task
        ↑
L2 Agent Orchestration
        ↑
L1 Core Runtime
        ↑
L0 Semantic / Structural Foundation
```

Dependencies point toward foundational contracts. Outbound integration occurs through controlled adapter boundaries.

## Prohibited dependencies

### L0

Must not directly depend on:

- UI/application code;
- external tools;
- AI vendors/models;
- database technology;
- application-specific workflows.

### L1

Must not directly depend on:

- UI;
- concrete external tools/providers.

### L2

Must not own concrete external tool implementations.

### L3

Must not bypass governance or capability boundaries to invoke providers directly.

### L4

External systems may be reached only through adapter boundaries.

### L5/L6

Domain/application code must consume stable contracts rather than redefine them.

## Kernel protection

The kernel must remain protected from:

- vendor lock-in;
- semantic drift;
- ontology collapse;
- hidden authority;
- uncontrolled mutation;
- undocumented dependencies.

## Enforcement

When the selected implementation language is finalized, these rules should be enforced through:

1. package/module boundaries;
2. dependency checks;
3. static analysis where available;
4. architecture tests;
5. CI failure on prohibited imports/dependencies.

## Exception policy

An exception requires:

- documented reason;
- affected boundary;
- explicit approval;
- test coverage;
- expiration/review condition where practical.

No exception may silently change the semantic architecture.
