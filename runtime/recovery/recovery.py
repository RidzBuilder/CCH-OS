class RecoveryPolicy:
    def classify(self,status):
        return status if status in {'success','failure','partial','unknown'} else 'unknown'
