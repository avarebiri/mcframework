import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from unittest.mock import MagicMock, patch
from agents.oracle_agent import OracleAgent

class TestOracleAgent(unittest.TestCase):
    def setUp(self):
        self.agent = OracleAgent()
    
    @patch("agents.oracle_agent.Minecraft.create", return_value=MagicMock())
    def test_lifecycle(self, mock_minecraft):
        """Test if OracleAgent follows lifecycle methods correctly with mocked Minecraft."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")

    @patch("agents.oracle_agent.ollama.generate", return_value=[("response", "Paris")])
    def test_ask_ollama(self, mock_ollama):
        """Test if OracleAgent handles LLM responses correctly."""
        question = "What is the capital of France?"
        response = self.agent.ask_ollama(question)
        self.assertEqual(response, "Paris", "Response should be 'Paris'.")

if __name__ == "__main__":
    unittest.main()
