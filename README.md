[![codecov](https://codecov.io/gh/avarebiri/mcframework/branch/main/graph/badge.svg)](https://codecov.io/gh/avarebiri/mcframework)
![Build Status](https://github.com/avarebiri/mcframework/actions/workflows/main.yml/badge.svg)


1. Introduction

The Minecraft Agent Framework provides a modular environment for creating AI-driven agents that interact with a Minecraft server. The framework is designed for extensibility, allowing third-party developers to create new agents easily by following a standard agent contract.

2. Framework Overview

Language: Python

Server Communication: mcpi.minecraft library

Core Components:

	-BaseAgent (Abstract class for all agents)

	-AgentFramework (Manages agent lifecycle)

	-OracleAgent, InsultAgent, TNTAgent (Example agents)

	-main.py (Registers and runs agents)

3. Agent Contract & API Guide

To create a new agent, you must adhere to the agent contract defined in BaseAgent.

Agent API

Every agent must inherit from BaseAgent and implement the following methods:

from abc import ABC, abstractmethod

class BaseAgent(ABC):
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
        """Cleanup logic for the agent."""
        pass
        
Creating a New Agent

To add a new agent:

3.1- Create a new Python file in agents/, e.g., example_agent.py.

3.2- Inherit from BaseAgent and implement the required methods.

Example: CustomAgent:

from mcpi.minecraft import Minecraft
from agents.base_agent import BaseAgent

class CustomAgent(BaseAgent):
    def __init__(self):
        self.mc = None

    def on_start(self):
        self.mc = Minecraft.create("localhost", 4711)
        self.mc.postToChat("CustomAgent has joined the game!")

    def on_tick(self):
        self.mc.postToChat("Hello from CustomAgent!")

    def on_stop(self):
        self.mc.postToChat("CustomAgent is leaving the game.")
       
3.3-Register the agent in main.py:

example:
from framework.framework import AgentFramework
from agents.custom_agent import CustomAgent

framework = AgentFramework()
framework.register_agent(CustomAgent)
framework.run()
        
4. Framework Lifecycle (Inversion of Control - IoC)

The framework follows the Inversion of Control (IoC) principle. The agent should not be run directly; instead, the framework manages its lifecycle:

4.1- Calls on_start() when the agent is registered.

4.2- Repeatedly calls on_tick() every execution cycle.

4.3- Calls on_stop() when stopping the framework.

5. UML Diagrams

Class Diagram

+-------------------+
|    BaseAgent     |
|-------------------|
| +on_start()      |
| +on_tick()       |
| +on_stop()       |
+-------------------+
        ^
        |
+-------------------+
| OracleAgent      |
| InsultAgent      |
| TNTAgent         |
+-------------------+
        |
+-------------------+
| AgentFramework   |
|-------------------|
| +register_agent()|
| +run()           |
+-------------------+


Sequence Diagram

User         Framework        Agent
  |              |              |
  | Start Main   |              |
  |------------->|              |
  |              | on_start()   |
  |              |------------->|
  |              |  Execution   |
  |              |<-------------|
  |              | on_tick()    |
  |              |------------->|
  |              |  Execution   |
  |              |<-------------|
  | Stop Signal  |              |
  |------------->| on_stop()    |
  |              |------------->|
  
Component Diagram

+--------------------+
|   Minecraft Server |
+--------------------+
          |
          v
+--------------------+
|  Agent Framework  |
+--------------------+
| - Manages Agents  |
| - Controls Cycle  |
+--------------------+
          |
          v
+---------------------+
|      Agents        |
+---------------------+
| OracleAgent        |
| InsultAgent        |
| TNTAgent           |
+---------------------+

6. Running the Framework

Installation & Setup

6.1- Install dependencies:

-pip install mcpi ollama

6.2- Run the framework:

-python main.py

7. Unit Testing & Code Coverage

To run tests:

-pytest --cov=agents

This ensures that all agents comply with the framework’s contract and maintain correctness.
