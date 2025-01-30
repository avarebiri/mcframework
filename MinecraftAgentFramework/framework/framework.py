import time

class AgentFramework:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent_class):
        """Dynamically instantiate agents using reflection."""
        agent_instance = agent_class() if isinstance(agent_class, type) else agent_class
        self.agents.append(agent_instance)


    def run(self):
        """Run all registered agents."""
        try:
            for agent in self.agents:
                print(f"Starting {agent.__class__.__name__}")
                agent.on_start()
            
            while True:
                for agent in self.agents:
                    agent.on_tick()  # IoC: Framework controls execution
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping all agents...")
            for agent in self.agents:
                agent.on_stop()
            print("All agents stopped.")
