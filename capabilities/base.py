class Capability:
    def __init__(self,name): self.name=name
    def invoke(self,request): return {"status":"success","capability":self.name,"request":request}
