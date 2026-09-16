import unittest
from cch_os import Runtime

class ChainTests(unittest.TestCase):
    def test_e2e_authorized(self):
        self.assertEqual(Runtime().execute({"topic":"CCH-OS"})["status"],"success")
    def test_unauthorized_denied(self):
        self.assertEqual(Runtime(authorized=False).execute({"topic":"CCH-OS"})["status"],"failure")
    def test_state_event_history_trace(self):
        rt=Runtime(); rt.execute({"topic":"CCH-OS"})
        self.assertIsNotNone(rt.state.get("last_result")); self.assertEqual(len(rt.events.events),1)
        self.assertEqual(len(rt.history.records),2); self.assertEqual(len(rt.trace.events),2)

if __name__=="__main__": unittest.main()
