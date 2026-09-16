"""CCH-OS semantic primitives. Representation is intentionally independent from storage."""
from dataclasses import dataclass
from typing import Any

class SemanticBoundaryError(ValueError): pass

@dataclass(frozen=True)
class Identity: value: str
@dataclass(frozen=True)
class Reference: value: str
@dataclass(frozen=True)
class Version: value: str
@dataclass(frozen=True)
class Observation: data: Any
@dataclass(frozen=True)
class Interpretation: data: Any
@dataclass(frozen=True)
class Evaluation: data: Any
@dataclass(frozen=True)
class Decision: data: Any
@dataclass(frozen=True)
class Plan: steps: tuple
@dataclass(frozen=True)
class Action: name: str; payload: Any

def require_distinct(*values):
    if len(values) != len({(type(v), repr(v)) for v in values}):
        raise SemanticBoundaryError("Distinct semantic values collapsed")
