from dataclasses import dataclass

from agent.Agent import Agent
from environment.Environment import Environment


@dataclass
class AgentState:
    environment: Environment
    agent: Agent



