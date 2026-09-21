"""Controlled environment contract for AAFA conformance tests."""
from abc import ABC, abstractmethod

class Environment(ABC):
    @abstractmethod
    def apply(self, action):
        raise NotImplementedError

    @abstractmethod
    def observe(self):
        raise NotImplementedError

    def snapshot(self):
        raise NotImplementedError
