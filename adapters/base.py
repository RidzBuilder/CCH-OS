class Adapter:
    def __init__(self,name): self.name=name
    def execute(self,request): return {"status":"success","adapter":self.name,"request":request}
