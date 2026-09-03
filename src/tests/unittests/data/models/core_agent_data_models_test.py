import pytest
from pydantic import ValidationError

from src.agent_core.data.models.agent import (
    Agent,
    AgentOrg,
    AgentGuardrails,
    AgentSkills,
    AgentTools,
    ToolPermissions
)

def test_agent_valid_inputs():
        agent = Agent(
            agent_id="A34WN4SQ",
            agent_name="testValidAgentInput",
            agent_org_id="25",
            tools=[AgentTools(
                    agent_id="A34WN4SQ",
                    tool_name="file_reader",
                    tool_permissions=ToolPermissions.READ
                    )
                    ],
            agent_org=AgentOrg(
                    org_id="25",
                    display_name="Test Valid Agent data model Input",
                    status="available",
                    agents=["testValidAgentInput"]
            ),
            status="available",
            guardrails=[AgentGuardrails(
                    guardrails_id="guard40f3kk",
                    name="Nosecrets",
                    agents=["testValidAgentInput"]
            )]
            )
        assert agent.tools[0].tool_permissions is ToolPermissions.READ


def test_agent_invalid_inputs():
        with pytest.raises(ValidationError):
                AgentTools(
                        agent_id="A34WN4SQ",
                        tool_name="file_reader",
                        tool_permissions="invalid"
                        )