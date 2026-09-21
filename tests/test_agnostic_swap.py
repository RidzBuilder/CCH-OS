import unittest
from cch_os import Runtime
from adapters.base import Adapter
from runtime.state.store import StateStore

class ProviderA(Adapter):
    def execute(self, request):
        return {"status":"success","provider":"A","request":request}

class ProviderB(Adapter):
    def execute(self, request):
        return {"status":"success","provider":"B","request":request}

class AlternateState(StateStore):
    def __init__(self):
        super().__init__()
        self.backend="alternate"

class AlternateEnvironment:
    def __init__(self):
        self.counter=0
    def apply(self, action):
        if action["name"]=="increment":
            self.counter += action["amount"]
        return {"status":"success"}
    def observe(self):
        return {"counter":self.counter}

class AgnosticSwapTests(unittest.TestCase):
    def run_with(self, adapter, state=None, environment=None):
        rt=Runtime(adapter=adapter, state=state, environment=environment)
        result=rt.execute({"target_counter":2})
        return result, rt.state.get("observation"), rt.memory.all()

    def test_adapter_swap_preserves_semantic_outcome(self):
        a=self.run_with(ProviderA())
        b=self.run_with(ProviderB())
        self.assertEqual(a[0]["status"], b[0]["status"])
        self.assertEqual(a[0]["verification"], b[0]["verification"])
        self.assertEqual(a[1], b[1])

    def test_storage_swap_preserves_semantic_outcome(self):
        result, observation, memory=self.run_with(ProviderB(), AlternateState())
        self.assertEqual(result["status"],"success")
        self.assertEqual(observation["counter"],2)
        self.assertGreaterEqual(len(memory),2)

    def test_environment_swap_preserves_contract(self):
        result, observation, _=self.run_with(ProviderA(), environment=AlternateEnvironment())
        self.assertEqual(result["status"],"success")
        self.assertEqual(observation["counter"],2)

if __name__=="__main__":
    unittest.main()
