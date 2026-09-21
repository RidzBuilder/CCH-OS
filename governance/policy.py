"""Explicit authority and execution policy boundary."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Authority:
    subject: str
    actions: frozenset = frozenset()

    def permits(self, action_name):
        return action_name in self.actions

class GovernancePolicy:
    def authorize(self, authority, action):
        if isinstance(authority, Authority):
            name = action.get("name") if isinstance(action, dict) else getattr(action, "name", None)
            return authority.permits(name)
        return authority is True

    def authorize_execution(self, authority, action):
        return self.authorize(authority, action)
