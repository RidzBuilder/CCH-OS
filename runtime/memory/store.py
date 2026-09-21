"""Explicit agent memory boundary; memory is distinct from current state."""
from copy import deepcopy

class MemoryStore:
    def __init__(self):
        self._records=[]

    def remember(self, record):
        self._records.append(deepcopy(record))

    def all(self):
        return tuple(deepcopy(self._records))

    def last(self):
        return deepcopy(self._records[-1]) if self._records else None
