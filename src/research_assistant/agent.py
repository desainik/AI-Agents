# Core ADK components
from google.adk.agents import SequentialAgent
from .sub_agents.query_builder_agent import query_builder_agent
from .sub_agents.research_agent import web_search_agent
from .sub_agents.content_analysis_agent import content_analysis_agent
from .sub_agents.report_generation_agent import report_generation_agent


# Create the Sequential Agent that combines all sub-agents and executes them in the order they are
# specified in the list.
research_assistant = SequentialAgent(
    name="research_assistant",
    description="A comprehensive research assistant that finds and analyzes information on topics",
    sub_agents=[
        query_builder_agent,
        web_search_agent,
        content_analysis_agent,
        report_generation_agent
    ]
)

# Root agent is the entry point for the research assistant agent.
root_agent = research_assistant
