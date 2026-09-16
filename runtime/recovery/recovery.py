from core.contracts.contracts import VALID_STATUSES

class RecoveryPolicy:
    def classify(self,status):
        return status if status in VALID_STATUSES else "unknown"
    def retryable(self,status):
        return status in {"failure","partial","unknown"}
