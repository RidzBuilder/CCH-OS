class StateStore:
    def __init__(self): self._state={}
    def get(self,key): return self._state.get(key)
    def set(self,key,value): self._state[key]=value
