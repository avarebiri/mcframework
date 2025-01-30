import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.insult_agent import InsultAgent

class TestInsultAgent(unittest.TestCase):
    def setUp(self):
        self.agent = InsultAgent()

    def test_generate_insults(self):
        """Test if InsultAgent generates a non-empty insult list."""
        self.assertGreater(len(self.agent.insults), 0, "Insult list should not be empty.")
    
    def test_lifecycle(self):
        """Test if InsultAgent follows lifecycle methods correctly."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")

if __name__ == "__main__":
    unittest.main()
