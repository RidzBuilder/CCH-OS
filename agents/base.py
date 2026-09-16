class Agent:
    def __init__(self,name,capabilities=(),authority=None):
        self.name=name; self.capabilities=tuple(capabilities); self.authority=authority
    def propose(self,task,context): return {"agent":self.name,"task":task,"context":context}
