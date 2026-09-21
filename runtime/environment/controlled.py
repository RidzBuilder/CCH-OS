"""Deterministic environment used to prove action→observation causality and recovery."""
from copy import deepcopy
from .base import Environment

class ControlledEnvironment(Environment):
    def __init__(self, counter=0, fail_on=None, fail_once=False):
        self.counter=counter; self.fail_on=fail_on; self.fail_once=fail_once
        self._failed=False; self.actions=[]

    def apply(self, action):
        self.actions.append(action)
        if self.fail_on == action.get("name") and (not self._failed or not self.fail_once):
            self._failed=True
            return {"status":"failure","error":"controlled_environment_failure"}
        if action.get("name")=="increment":
            self.counter += int(action.get("amount",1))
        elif action.get("name")=="decrement":
            self.counter -= int(action.get("amount",1))
        return {"status":"success"}

    def observe(self):
        return {"counter":self.counter}

    def snapshot(self):
        return deepcopy({"counter":self.counter,"actions":self.actions})
