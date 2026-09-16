"""Minimal executable CCH-OS runtime for experimental validation."""
from datetime import datetime, timezone
from core.semantic.model import Observation, Interpretation, Evaluation, Decision, Plan, Action
from runtime.state.store import StateStore
from runtime.events.bus import EventBus
from runtime.history.ledger import HistoryLedger
from governance.policy import GovernancePolicy
from agents.base import Agent
from capabilities.base import Capability
from adapters.base import Adapter
from observability.trace import Trace

class Runtime:
    def __init__(self, authorized=True):
        self.state=StateStore(); self.events=EventBus(); self.history=HistoryLedger()
        self.governance=GovernancePolicy(); self.trace=Trace(); self.authorized=authorized
        self.agent=Agent("runtime-agent"); self.capability=Capability("process"); self.adapter=Adapter("default")
    def execute(self,payload):
        obs=Observation(payload); interp=Interpretation({"input":obs.data})
        evaluation=Evaluation({"accepted":True,"basis":interp.data})
        decision=Decision({"action":"process","evaluation":evaluation.data})
        plan=Plan((Action("process",payload),))
        self.trace.record(("observation",obs)); self.history.append({"stage":"observation","value":obs})
        if not self.governance.authorize_execution(self.authorized,plan.steps[0]):
            result={"status":"failure","error":"unauthorized"}
            self.events.emit({"type":"execution_denied","payload":result}); self.history.append({"stage":"result","value":result}); return result
        proposal=self.agent.propose(plan.steps[0].name,payload)
        result=self.adapter.execute(self.capability.invoke(proposal))
        self.state.set("last_result",result)
        event={"type":"result","payload":result,"occurred_at":datetime.now(timezone.utc).isoformat()}
        self.events.emit(event); self.history.append({"stage":"result","value":result}); self.trace.record(event)
        return result
