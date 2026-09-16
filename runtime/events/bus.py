class EventBus:
    def __init__(self): self.events=[]
    def emit(self,event): self.events.append(event)
