"""Stage 1 contract primitives."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Contract:
    name:str
    version:str="1.0"
