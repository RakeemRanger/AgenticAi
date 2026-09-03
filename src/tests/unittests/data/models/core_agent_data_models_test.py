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

class TestAgentModels:
    def create_agent(self):
        agent_org = AgentOrg(
            org_id="25",
            display_name="Test Valid Agent data model Input",
            status="available",
            agents=["testValidAgentInput"]
            )
        agent_tools = AgentTools(
            agent_id="A34WN4SQ",
            tool_name="file_reader",
            tool_permissions=ToolPermissions.READ
            )
        agent_guardrails = AgentGuardrails(
                guardrails_id="guard40f3kk",
                name="Nosecrets",
                agents=["testValidAgentInput"]
                )
        return Agent(
            agent_id="A34WN4SQ",
            agent_name="testValidAgentInput",
            agent_org_id="25",
          tools=[agent_tools],
          agent_org=agent_org,
                status="available",
          guardrails=[agent_guardrails],
          skills=["skill1-test", "skill2-test"])

    def create_agent_skills(self):
        return AgentSkills(
            skills_id="skill4j45kl",
            skills_name="skill2-test",
            agents=[self.create_agent()],
            tools=[AgentTools(
                agent_id="A34WN4SQ",
                tool_name="file_reader",
                tool_permissions=ToolPermissions.READ
            )],
            enabled=True
        )

    def test_agent_valid_inputs(self):
        agent = self.create_agent()
        assert agent.tools[0].tool_permissions is ToolPermissions.READ

    def test_agent_invalid_inputs(self):
        with pytest.raises(ValidationError):
            AgentTools(
                agent_id="A34WN4SQ",
                tool_name="file_reader",
                tool_permissions="INVALID"
            )


    def test_agent_skills_data_model_invalid_inputs(self):
        with pytest.raises(ValidationError):
            AgentSkills(
                skills_id="skill4j45kl",
                skills_name="skill2-test",
                agents=["invalid-agent"],
                tools=[],
                enabled=True
            )

    def test_agent_skills_data_model_valid_input(self):
        assert self.create_agent_skills().skills_name is not None