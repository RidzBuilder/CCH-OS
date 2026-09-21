"""Deterministic recovery and resume boundary."""
class RecoveryManager:
    def recover(self, failure, checkpoint):
        return {
            "status":"recovery_ready",
            "failure":failure,
            "checkpoint":checkpoint,
            "action":"resume",
            "retry_allowed":True
        }
