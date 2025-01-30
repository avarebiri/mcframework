import unittest
import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.insult_agent import InsultAgent

def get_server_url():
    """Get server URL from environment or use default."""
    return os.getenv('TEST_SERVER_URL', 'http://localhost:4711')

class TestInsultAgent(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        self.agent = InsultAgent()
        self.server_url = get_server_url()
    
    def test_generate_insults(self):
        """Test if InsultAgent generates a non-empty insult list."""
        self.assertGreater(len(self.agent.insults), 0, "Insult list should not be empty.")
    
    def test_lifecycle(self):
        """Test if InsultAgent follows lifecycle methods correctly."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")

    def test_insult_format(self):
        """Test if each insult is a non-empty string."""
        for insult in self.agent.insults:
            self.assertIsInstance(insult, str, "Each insult should be a string")
            self.assertGreater(len(insult), 0, "Each insult should be non-empty")

    def test_get_random_insult(self):
        """Test if get_random_insult returns a valid insult."""
        insult = self.agent.get_random_insult()
        self.assertIsInstance(insult, str, "Random insult should be a string")
        self.assertIn(insult, self.agent.insults, "Random insult should be from the insult list")

    def test_server_connection(self):
        """Test if agent can connect to the server."""
        try:
            response = requests.get(self.server_url)
            self.assertEqual(response.status_code, 200, "Server should return 200 OK")
        except requests.ConnectionError:
            if os.getenv('TEST_MODE') == 'ci':
                self.skipTest("Skipping server test in CI environment")
            else:
                raise

    def test_server_interaction(self):
        """Test if agent can interact with server endpoints."""
        try:
            # Replace with actual endpoint and expected data
            endpoint = f"{self.server_url}/api/test"
            response = requests.get(endpoint)
            self.assertEqual(response.status_code, 200, "API endpoint should be accessible")
            self.assertIsInstance(response.json(), dict, "Response should be JSON")
        except requests.ConnectionError:
            if os.getenv('TEST_MODE') == 'ci':
                self.skipTest("Skipping server interaction test in CI environment")
            else:
                raise

if __name__ == "__main__":
    unittest.main()
