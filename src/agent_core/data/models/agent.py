from typing import Any
from enum import Enum

from pydantic.dataclasses import dataclass

class ToolPermissions(Enum):
    READ = "Read"
    READ_WRITE = "ReadWrite"
    READ_WRITE_EX = "ReadWriteExecute"

@dataclass
class AgentTools:
    agent_id: str
    tool_name: str
    tool_permissions: ToolPermissions

@dataclass
class AgentGuardrails:
    guardrails_id: str
    name: str
    agents: list[str]

@dataclass
class AgentOrg:
    org_id: str
    display_name: str
    status: str
    agents: list[str, Any]


@dataclass
class Agent:
    agent_id: str
    agent_name: str
    agent_org: AgentOrg
    tools: list[AgentTools]
    guardrails: list[AgentGuardrails]
    status: str


@dataclass
class AgentSkills:
    skills_id: str
    skills_name: str
    agents: list[Agent]
    tools: list[AgentTools]
    enabled: bool
