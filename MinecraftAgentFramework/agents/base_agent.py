from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @abstractmethod
    def on_start(self):
        """Setup logic for the agent."""
        pass

    @abstractmethod
    def on_tick(self):
        """Execution logic per tick (controlled by the framework)."""
        pass

    def run(self):
        """Default implementation to support abstract requirement."""
        while True:
            self.on_tick()
    
    @abstractmethod
    def on_stop(self):
        pass
