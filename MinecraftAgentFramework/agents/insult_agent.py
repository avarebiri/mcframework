import random
from mcpi.minecraft import Minecraft
from agents.base_agent import BaseAgent
import time

def generate_insults():
    return [
        "You call that building? My grandma builds better!",
        "Why are you so slow?",
        "Did you even *try* to survive?",
        "Are you sure you know how to play this game?",
        "I've seen chickens with better skills!",
    ]

def choose_random_item(items):
    return random.choice(items)

class InsultAgent(BaseAgent):
    def __init__(self):
        self.mc = None
        self.insults = generate_insults()
        self.should_run = True  # IoC: Framework controls execution

    def on_start(self):
        """Setup the Minecraft connection."""
        self.mc = Minecraft.create("localhost", 4711)
        self.mc.postToChat("InsultBot has joined the game!")
        print("InsultBot started.")

    def on_tick(self):
        """Run a single execution cycle."""
        if not self.should_run:
            return
        
        insult = choose_random_item(self.insults)
        self.mc.postToChat(insult)
        time.sleep(10)  # Delay before next tick

    def on_stop(self):
        """Cleanup logic when the agent stops."""
        self.should_run = False
        self.mc.postToChat("InsultBot is leaving the game.")
        print("InsultBot stopped.")
