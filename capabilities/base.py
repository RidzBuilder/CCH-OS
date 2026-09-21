"""Capability contract boundary."""
class Capability:
    def __init__(self, name, allowed_actions=None):
        self.name=name
        self.allowed_actions=frozenset(allowed_actions or {name, "increment", "decrement", "stop", "process"})

    def invoke(self, request):
        action_name=request.get("name")
        if action_name not in self.allowed_actions:
            return {"status":"failure","error":"capability_contract_violation","capability":self.name}
        return {"status":"success","capability":self.name,"request":request}
