class HistoryLedger:
    """Append-only execution history."""
    def __init__(self): self.records=[]
    def append(self,record): self.records.append(record); return record
    def all(self): return tuple(self.records)
