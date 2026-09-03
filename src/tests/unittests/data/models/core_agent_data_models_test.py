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
    def create_agent_org(self):
        return AgentOrg(
            org_id="25",
            display_name="Test Valid Agent data model Input",
            status="available",
            agents=["testValidAgentInput"]
        )

    def create_agent_tools(self):
        return AgentTools(
            agent_id="A34WN4SQ",
            tool_name="file_reader",
            tool_permissions=ToolPermissions.READ
        )

    def create_agent_guardrails(self):
        return AgentGuardrails(
            guardrails_id="guard40f3kk",
            name="Nosecrets",
            agents=["testValidAgentInput"]
        )

    def create_agent(self):
        return Agent(
            agent_id="A34WN4SQ",
            agent_name="testValidAgentInput",
            agent_org_id="25",
            tools=[self.create_agent_tools()],
            agent_org=self.create_agent_org(),
            status="available",
            guardrails=[self.create_agent_guardrails()],
            skills=["skill1-test", "skill2-test"]
        )

    def create_agent_skills(self):
        return AgentSkills(
            skills_id="skill4j45kl",
            skills_name="skill2-test",
            agents=[self.create_agent()],
            tools=[self.create_agent_tools()],
            enabled=True
        )

    def test_agent_org_valid_inputs(self):
        assert self.create_agent_org().status == "available"

    def test_agent_org_invalid_inputs(self):
        with pytest.raises(ValidationError):
            AgentOrg(
                org_id="25",
                display_name="Invalid organization",
                status="available"
            )

    def test_agent_tools_valid_inputs(self):
        assert self.create_agent_tools().tool_permissions is ToolPermissions.READ

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

    def test_agent_guardrails_valid_inputs(self):
        assert self.create_agent_guardrails().name == "Nosecrets"

    def test_agent_guardrails_invalid_inputs(self):
        with pytest.raises(ValidationError):
            AgentGuardrails(
                guardrails_id="guard40f3kk",
                name="Invalid guardrail"
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