"""Contract primitives and explicit interface boundaries."""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Contract:
    name: str
    version: str = "1.0"

@dataclass(frozen=True)
class Result:
    status: str
    value: Any = None
    error: Any = None

VALID_STATUSES = frozenset({"success","failure","partial","unknown"})
