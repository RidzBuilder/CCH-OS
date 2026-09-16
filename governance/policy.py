class GovernancePolicy:
    def authorize(self,authority,action): return authority is True
    def authorize_execution(self,actor,action): return self.authorize(actor,action)
