# CCH-OS Codex Execution Plan v0.1

## Objective

Translate the accepted repository configuration into executable implementation incrementally, preserving architectural boundaries and producing evidence at every stage.

## Stage 0 — Repository foundation

Create the configured topology, package/module boundaries, test harness, documentation links, and CI architecture checks.

**Exit:** repository structure exists and prohibited dependency checks are executable.

## Stage 1 — L0 semantic foundation

Implement:

- component;
- structure;
- composition;
- context;
- reference;
- identity;
- ID;
- version.

**Exit:** semantic contracts compile and distinction tests pass.

## Stage 2 — L1 core runtime

Implement:

- state model;
- state transitions;
- event model;
- lifecycle;
- history;
- persistence interfaces;
- recovery primitives.

**Exit:** authoritative state mutation and state/event/history tests pass.

## Stage 3 — governance + orchestration foundations

Implement:

- authorization contract;
- decision boundary;
- action request;
- agent runtime contract;
- orchestration interfaces.

**Exit:** unauthorized execution is rejected and authority cannot be inferred from capability.

## Stage 4 — workflow/task runtime

Implement:

- workflow;
- task;
- step;
- action request;
- dependencies;
- branching/parallelism;
- retry;
- pause/resume.

**Exit:** workflow tests and recovery tests pass.

## Stage 5 — capability/tool/adapter layer

Implement:

- capability contract;
- registry;
- tool contract;
- adapter contract;
- provider boundary;
- compatibility checks.

**Exit:** provider replacement can occur without changing core semantic contracts.

## Stage 6 — domain services

Add content-domain services only through stable runtime/capability contracts.

Potential domains from the architecture include product, content, storyboard, generation, publishing, and analytics.

**Exit:** domain vertical slice runs without violating dependency rules.

## Stage 7 — application experience

Add API/UI/application orchestration as a consumer of the core system.

**Exit:** application cannot bypass runtime/governance boundaries.

## Stage 8 — vertical proof

Build one representative end-to-end CCH-OS workflow.

Required evidence:

input → context → observation → interpretation/evaluation → decision → authorization → action → result → state update → event/history → output.

## Stage 9 — validation

Run the complete validation matrix and record failures rather than masking them.

## Stage 10 — expansion

Only after the first vertical slice is proven:

- additional agents;
- additional workflows;
- additional capabilities;
- additional adapters;
- additional domains;
- optional candidate architecture such as ECLB-01 after its own validation/adoption gate.

## Codex behavior

Codex should work in small, reviewable increments.

For each increment:

1. inspect current repository;
2. identify governing contract;
3. implement minimal change;
4. add tests;
5. run tests;
6. report files changed;
7. report architectural invariants exercised;
8. report unresolved risks;
9. stop if an architectural contradiction is discovered.

Do not generate the entire OS in one unreviewed pass.
