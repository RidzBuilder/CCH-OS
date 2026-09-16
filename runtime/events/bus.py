class EventBus:
    """Occurrence stream; events do not become authoritative state automatically."""
    def __init__(self): self.events=[]
    def emit(self,event): self.events.append(event); return event
