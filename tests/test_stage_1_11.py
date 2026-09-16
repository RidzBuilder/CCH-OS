import unittest
from core.semantic.model import Identity, Reference, Version, Observation, Interpretation, Evaluation, Decision, Action
from runtime.state.store import StateStore
from runtime.events.bus import EventBus
from runtime.recovery.recovery import RecoveryPolicy
from governance.policy import GovernancePolicy
from agents.base import Agent
from capabilities.base import Capability
from adapters.base import Adapter

class StageTests(unittest.TestCase):
    def test_semantic_boundaries(self):
        self.assertNotEqual(Identity("x"),Reference("x")); self.assertNotEqual(Identity("x"),Version("x"))
        self.assertNotEqual(Observation({"x":1}),Interpretation({"x":1}))
        self.assertNotEqual(Evaluation({"x":1}),Decision({"x":1})); self.assertNotEqual(Decision({"x":1}),Action("x",{"x":1}))
    def test_state_event_separation(self):
        s=StateStore(); e=EventBus(); s.set("x",1); e.emit({"type":"changed"})
        self.assertEqual(s.get("x"),1); self.assertEqual(len(e.events),1)
    def test_governance(self):
        p=GovernancePolicy(); self.assertTrue(p.authorize(True,"execute")); self.assertFalse(p.authorize(False,"execute"))
    def test_recovery_transparency(self):
        p=RecoveryPolicy()
        for s in ("success","failure","partial","unknown"): self.assertEqual(p.classify(s),s)
        self.assertEqual(p.classify("invalid"),"unknown")
    def test_component_boundaries(self):
        self.assertEqual(Agent("a").name,"a"); self.assertEqual(Capability("c").name,"c"); self.assertEqual(Adapter("a").name,"a")

if __name__=="__main__": unittest.main()
