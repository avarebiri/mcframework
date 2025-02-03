import unittest
from unittest.mock import MagicMock, patch
from framework.framework import AgentFramework
from agents.oracle_agent import OracleAgent
from agents.insult_agent import InsultAgent
from agents.tnt_agent import TNTAgent

class TestAgentFramework(unittest.TestCase):
    def setUp(self):
        self.framework = AgentFramework()
    
    def test_register_agents(self):
        """Test if agents are registered correctly."""
        self.framework.register_agent(OracleAgent)
        self.framework.register_agent(InsultAgent)
        self.framework.register_agent(TNTAgent)
        self.assertEqual(len(self.framework.agents), 3, "Framework should have 3 registered agents.")

    @patch("agents.oracle_agent.Minecraft.create", return_value=MagicMock())
    @patch("agents.insult_agent.Minecraft.create", return_value=MagicMock())
    @patch("agents.tnt_agent.Minecraft.create", return_value=MagicMock())
    def test_agent_execution(self, mock_minecraft_oracle, mock_minecraft_insult, mock_minecraft_tnt):
        """Test if framework properly starts and stops agents with mocked Minecraft connection."""
        self.framework.register_agent(OracleAgent)
        self.framework.register_agent(InsultAgent)
        self.framework.register_agent(TNTAgent)
        
        for agent in self.framework.agents:
            agent.on_start()
            self.assertTrue(agent.should_run, f"{agent.__class__.__name__} should be running after on_start().")
            
            agent.on_stop()
            self.assertFalse(agent.should_run, f"{agent.__class__.__name__} should stop running after on_stop().")

if __name__ == "__main__":
    unittest.main()
