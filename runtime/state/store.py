class StateStore:
    """Authoritative current state; never used as an event ledger."""
    def __init__(self): self._state={}
    def get(self,key): return self._state.get(key)
    def set(self,key,value): self._state[key]=value
    def snapshot(self): return dict(self._state)
