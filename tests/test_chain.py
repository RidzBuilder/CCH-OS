import unittest
from cch_os import Runtime
from runtime.environment.controlled import ControlledEnvironment
from governance.policy import Authority

class ChainTests(unittest.TestCase):
    def test_e2e_authorized_multi_cycle_verified(self):
        rt=Runtime()
        result=rt.execute({"target_counter":2})
        self.assertEqual(result["status"],"success")
        self.assertGreaterEqual(result["cycle"],3)
        self.assertTrue(any(e.get("stage")=="verification" for e in rt.trace.events))

    def test_unauthorized_denied(self):
        rt=Runtime(authorized=False)
        result=rt.execute({"target_counter":1})
        self.assertEqual(result["status"],"failure")
        self.assertEqual(result["error"],"unauthorized")

    def test_state_event_history_trace_and_memory(self):
        rt=Runtime()
        rt.execute({"target_counter":1})
        self.assertEqual(rt.state.get("observation")["counter"],1)
        self.assertEqual(len(rt.events.events),1)
        self.assertGreaterEqual(len(rt.history.records),5)
        self.assertGreaterEqual(len(rt.trace.events),5)
        self.assertGreaterEqual(len(rt.memory.all()),2)

    def test_scoped_authority(self):
        allowed=Authority("agent", frozenset({"increment"}))
        denied=Authority("agent", frozenset())
        self.assertEqual(Runtime(authorized=allowed).execute({"target_counter":1})["status"],"success")
        result=Runtime(authorized=denied).execute({"target_counter":1})
        self.assertEqual(result["status"],"failure")
        self.assertEqual(result["error"],"unauthorized")

    def test_environment_failure_produces_recovery_evidence(self):
        env=ControlledEnvironment(counter=0, fail_on="increment")
        rt=Runtime(environment=env)
        result=rt.execute({"target_counter":1})
        self.assertEqual(result["status"],"failure")
        self.assertEqual(result["error"],"environment_failure")
        self.assertIn("recovery", result)
        self.assertTrue(any(e.get("stage")=="recovery" for e in rt.trace.events))

if __name__=="__main__":
    unittest.main()
