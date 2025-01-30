from mcpi.minecraft import Minecraft
from agents.base_agent import BaseAgent
import time

class TNTAgent(BaseAgent):
    def __init__(self):
        self.mc = None
        self.block_id = 46  # Default to TNT
        self.should_run = True  # IoC: Framework controls execution

    def on_start(self):
        """Setup the Minecraft connection."""
        self.mc = Minecraft.create("localhost", 4711)
        self.mc.postToChat("TNTBot has joined the game!")
        print("TNTBot started.")

    def on_tick(self):
        """Run a single execution cycle."""
        if not self.should_run:
            return
        
        pos = self.mc.player.getTilePos()
        self.mc.setBlock(pos.x + 2, pos.y, pos.z, self.block_id)
        self.mc.setBlock(pos.x + 2, pos.y - 1, pos.z, 51)  # Fire to ignite
        self.mc.postToChat("Boom! Run!")
        time.sleep(5)  # Delay before next tick

    def set_block_type(self, block_name):
        """Dynamically set block type using reflection."""
        block_mapping = {"TNT": 46, "STONE": 1, "GOLD": 41}
        self.block_id = block_mapping.get(block_name.upper(), 46)

    def on_stop(self):
        """Cleanup logic when the agent stops."""
        self.should_run = False
        self.mc.postToChat("TNTBot is leaving the game.")
        print("TNTBot stopped.")
