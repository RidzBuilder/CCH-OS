"""CCH-OS runtime with explicit AAFA conformance and replaceable boundaries."""
from runtime.state.store import StateStore
from runtime.events.bus import EventBus
from runtime.history.ledger import HistoryLedger
from runtime.memory.store import MemoryStore
from runtime.environment.controlled import ControlledEnvironment
from runtime.recovery.manager import RecoveryManager
from runtime.verification.verifier import Verifier
from core.agentic.loop import AgentLoop
from governance.policy import GovernancePolicy
from agents.base import Agent
from capabilities.base import Capability
from adapters.base import Adapter
from observability.trace import Trace

class Runtime:
    """Runtime composition root; semantic behavior is independent of concrete adapters/storage."""
    def __init__(self, authorized=True, environment=None, adapter=None,
                 state=None, memory=None, events=None, history=None):
        self.state=state or StateStore()
        self.events=events or EventBus()
        self.history=history or HistoryLedger()
        self.memory=memory or MemoryStore()
        self.governance=GovernancePolicy()
        self.trace=Trace()
        self.authorized=authorized
        self.agent=Agent("runtime-agent")
        self.capability=Capability("process")
        self.adapter=adapter or Adapter("default")
        self.environment=environment or ControlledEnvironment(counter=0)
        self.verifier=Verifier()
        self.recovery=RecoveryManager()

    def execute(self, payload):
        goal={"target_counter": payload.get("target_counter", 1)}
        loop=AgentLoop(
            state=self.state, memory=self.memory, environment=self.environment,
            capability=self.capability, adapter=self.adapter,
            governance=self.governance, verifier=self.verifier,
            recovery=self.recovery, trace=self.trace,
            history=self.history, events=self.events, max_cycles=10
        )
        return loop.run(goal, authorized=self.authorized)
