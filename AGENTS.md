# CCH-OS — Codex Implementation Constitution

## Authority

The primary architectural source is:

- `CCH-OS_Architecture_Specification_v1.0.md`

Supporting sources may clarify intent, but must not silently redefine the architecture.

The recovered v1.0 specification is implementation-independent, contract-driven, modular, extensible, testable, and technology-agnostic. It defines the semantic model, layers, contracts, runtime, governance, persistence abstraction, observability, recovery, lineage, security, extensibility, dependency rules, testing architecture, and invariant validation.

## Implementation posture

Codex is an implementation executor, not the architectural authority.

Before changing architecture-level behavior:

1. Identify the affected contract.
2. Identify the affected layer/module.
3. State the reason for the change.
4. Add or update tests that prove the invariant.
5. Do not silently introduce vendor/framework semantics into the core.
6. If the requested change contradicts an architectural invariant, stop and surface the conflict.

## Protected semantic boundaries

Do not collapse:

- Semantic Model != Representation != Storage
- Identity != ID != Reference != Version
- State != Event != History
- Observation != Interpretation != Evaluation != Decision != Action
- Agent != Capability != Tool != Authority
- Workflow != Task != Step != Action
- Provenance != Lineage

The structural-correction evidence additionally distinguishes authorization, execution, trace/audit, failure ownership, recovery authority, and transformation. These are implementation guardrails pending final architectural re-validation.

## Layer rule

The repository must preserve the eight-layer architecture:

L0 Semantic / Structural Foundation
L1 Core Runtime
L2 Intelligence / Agent Orchestration
L3 Workflow / Task
L4 Capability / Tool
L5 Domain Services
L6 Application Experience
L7 External Systems

Dependency direction is toward foundational contracts, with controlled outbound integration through adapters.

## External provider rule

AI models, generation engines, databases, storage systems, publishing platforms, analytics platforms, communication services, and other external implementations belong behind explicit interfaces/adapters.

No external provider may redefine CCH-OS semantic or workflow contracts.

## State and mutation rule

Authoritative state must not be mutated directly by UI, agents, tools, adapters, or external providers.

Mutations must pass through the runtime/state-transition boundary.

Failures must never silently become successful state.

## Test-first invariant rule

Implementation is incomplete when code exists without executable proof.

At minimum, tests must cover:

- core contract integrity;
- state transitions;
- event/state separation;
- workflow execution;
- agent authority;
- capability/tool/adapter boundaries;
- adapter compatibility;
- failure/recovery;
- persistence independence;
- end-to-end behavior.

## Candidate architecture rule

The Execution Compiler Layer (ECLB-01) remains a candidate/future architecture element. Do not silently promote it into the canonical architecture until its validation/adoption gate is satisfied.

## Change discipline

Prefer additive, minimal changes.

Do not:

- introduce framework-specific dependencies into the kernel;
- couple core semantics to a vendor;
- use database schemas as the semantic model;
- let UI become an authority;
- hide failures;
- erase lineage during regeneration;
- replace architectural contracts with implementation convenience.

Every implementation change should leave a traceable relationship:

Architecture Contract -> Module -> Code -> Test -> Evidence.
