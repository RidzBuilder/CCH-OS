"""Explicit verification contract."""
class Verifier:
    def verify(self, goal, observation):
        target = goal.get("target_counter")
        if target is None:
            return {"verified": True, "basis": "no_target"}
        return {
            "verified": observation.get("counter") == target,
            "basis": {"target_counter": target, "observed_counter": observation.get("counter")}
        }
