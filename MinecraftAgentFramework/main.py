from framework.framework import AgentFramework
from agents.oracle_agent import OracleAgent
from agents.insult_agent import InsultAgent
from agents.tnt_agent import TNTAgent

if __name__ == "__main__":
    framework = AgentFramework()

    # Register agents
    framework.register_agent(OracleAgent)
    framework.register_agent(InsultAgent)
    framework.register_agent(TNTAgent)

    # Run the framework (manages all agents)
    framework.run()
