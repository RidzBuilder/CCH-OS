"""Deterministic recovery and resume boundary."""
class RecoveryManager:
    def recover(self, failure, checkpoint):
        return {
            "status": "recovery_required",
            "failure": failure,
            "checkpoint": checkpoint,
            "action": "resume"
        }
