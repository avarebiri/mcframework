import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from unittest.mock import MagicMock, patch
from agents.tnt_agent import TNTAgent

class TestTNTAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TNTAgent()

    @patch("agents.tnt_agent.Minecraft.create", return_value=MagicMock())
    def test_lifecycle(self, mock_minecraft):
        """Test if TNTAgent follows lifecycle methods correctly with mocked Minecraft."""
        self.agent.on_start()
        self.assertTrue(self.agent.should_run, "Agent should be running after on_start().")
        
        self.agent.on_stop()
        self.assertFalse(self.agent.should_run, "Agent should stop running after on_stop().")
    
    def test_set_block_type(self):
        """Test if TNTAgent correctly sets block type using reflection."""
        self.agent.set_block_type("STONE")
        self.assertEqual(self.agent.block_id, 1, "Block ID should be 1 (STONE).")

        self.agent.set_block_type("GOLD")
        self.assertEqual(self.agent.block_id, 41, "Block ID should be 41 (GOLD).")

if __name__ == "__main__":
    unittest.main()
