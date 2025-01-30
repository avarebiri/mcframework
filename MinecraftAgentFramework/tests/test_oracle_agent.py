import unittest
from agents.oracle_agent import OracleAgent

class TestOracleAgent(unittest.TestCase):
    def setUp(self):
        self.agent = OracleAgent()

    def test_ask_ollama(self):
        """Test if OracleAgent gets a valid response from Ollama."""
        question = "What is the capital of France?"
        response = self.agent.ask_ollama(question)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0, "Response should not be empty.")

    def test_lifecycle(self):
        """Test if OracleAgent follows lifecycle methods correctly."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")

if __name__ == "__main__":
    unittest.main()
