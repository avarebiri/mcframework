import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
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

    def test_agent_execution(self):
        """Test if framework properly starts and stops agents."""
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
