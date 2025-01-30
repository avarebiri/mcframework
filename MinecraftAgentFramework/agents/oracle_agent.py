import ollama
from mcpi.minecraft import Minecraft
from agents.base_agent import BaseAgent
from functools import reduce
import time

class OracleAgent(BaseAgent):
    def __init__(self, model="llama2"):
        self.mc = None
        self.model = model
        self.should_run = True  # IoC: Framework controls execution

    def on_start(self):
        """Setup the Minecraft connection."""
        self.mc = Minecraft.create("localhost", 4711)
        self.mc.postToChat("OracleBot has joined the game!")
        print("OracleBot started.")

    def on_tick(self):
        """Process a single tick cycle (called by the framework)."""
        messages = self.mc.events.pollChatPosts()
        for message in messages:
            if message.message.lower().startswith("oraclebot"):
                question = message.message[len("oraclebot"):].strip()
                self.mc.postToChat("Thinking...")
                answer = self.ask_ollama(question)
                self.mc.postToChat(f"OracleBot says: {answer}")

    def ask_ollama(self, question):
        """Query the Ollama model for an answer using functional programming."""
        try:
            response = ollama.generate(model=self.model, prompt=question)
            return reduce(lambda acc, chunk: acc + chunk[1] if isinstance(chunk, tuple) and chunk[0] == "response" else acc, response, "").strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def set_model(self, model_name):
        """Dynamically change the model using reflection."""
        if hasattr(self, "model"):
            setattr(self, "model", model_name)
            self.mc.postToChat(f"OracleBot switched to model: {model_name}")
        else:
            self.mc.postToChat("Failed to change model.")

    def on_stop(self):
        """Cleanup logic when the agent stops."""
        self.should_run = False
        self.mc.postToChat("OracleBot is leaving the game.")
        print("OracleBot stopped.")
