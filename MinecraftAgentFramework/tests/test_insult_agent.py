import unittest
from unittest.mock import MagicMock, patch
from agents.insult_agent import InsultAgent

class TestInsultAgent(unittest.TestCase):
    def setUp(self):
        self.agent = InsultAgent()
    
    @patch("agents.insult_agent.Minecraft.create", return_value=MagicMock())
    def test_lifecycle(self, mock_minecraft):
        """Test if InsultAgent follows lifecycle methods correctly with mocked Minecraft."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")
    
    def test_generate_insults(self):
        """Test if InsultAgent generates a non-empty insult list."""
        self.assertGreater(len(self.agent.insults), 0, "Insult list should not be empty.")

if __name__ == "__main__":
    unittest.main()
