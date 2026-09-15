# CCH-OS Implementation Baseline v0.1

## Status

**Repository Configuration — Initial Baseline**

This document translates the recovered CCH-OS Architecture Specification v1.0 into implementation constraints. It does not replace the architecture specification.

### Source hierarchy

1. CCH-OS Architecture Specification v1.0 — primary architecture source.
2. Approved structural-correction evidence — implementation guardrails where applicable.
3. Blueprint and research artifacts — supporting context.
4. New implementation decisions — must remain explicitly implementation-level unless separately authorized.

## Current architectural state

The architecture specification is explicitly implementation-independent and technology-agnostic. It defines eight layers from L0 Semantic/Structural Foundation through L7 External Systems.

The structural-correction record describes RC-01 through RC-10 as applied to a v1.1 candidate, while that v1.1 artifact itself remains pending structural re-validation. Therefore this repository baseline must not claim Architecture Lock.

## Translation objective

Create a repository in which architecture boundaries can be enforced and tested rather than merely documented.

Target chain:

Architecture
-> Contracts
-> Module topology
-> Runtime
-> Capabilities/adapters
-> Domain services
-> Application
-> Tests
-> Executable evidence

## Non-goals

This baseline does not:

- select a programming language;
- select a frontend/backend framework;
- select a database;
- select an AI model vendor;
- define production deployment;
- promote ECLB-01 to canonical architecture;
- declare the architecture validated or locked.

## Initial implementation priority

P0:
1. semantic/core contracts;
2. identity/reference/version primitives;
3. state/event/history model;
4. runtime lifecycle and authoritative state transition;
5. governance/authorization boundaries;
6. invariant test harness.

P1:
7. workflow/task/action runtime;
8. agent runtime;
9. capability registry and adapter contracts;
10. persistence abstraction;
11. observability and trace interfaces;
12. failure/recovery primitives.

P2:
13. domain services;
14. application experience;
15. concrete external adapters;
16. public/demo surface.

## Definition of done for each module

A module is not considered implemented merely because files compile.

It must have:

- explicit responsibility;
- explicit dependency direction;
- stable contract;
- implementation;
- automated tests;
- failure behavior;
- observability/trace behavior where applicable;
- no prohibited dependency;
- evidence linked to the relevant architecture contract.
