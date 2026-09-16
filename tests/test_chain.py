import unittest
from cch_os import Runtime, Observation, Event, Capability, Authority
class ChainTests(unittest.TestCase):
    def test_e2e_chain(self): self.assertEqual(Runtime().execute({"topic":"CCH-OS"})["status"],"success")
    def test_semantic_types_distinct(self): self.assertNotEqual(Observation,Event); self.assertNotEqual(Capability,Authority)
    def test_unauthorized_denied(self): self.assertFalse(Authority().authorize("unauthorized","execute"))
if __name__ == "__main__": unittest.main()
