import os
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from ... tools.agent_tools import save_to_file, get_current_date
from . import prompt as p

# Create report generation agent and use function tool to save report content in mark down format.
report_generation_agent = LlmAgent(
    model=os.getenv('MODEL'),
    name="report_generation_agent",
    instruction=p.REPORT_GENERATION_PROMPT,
    tools=[FunctionTool(save_to_file),
           FunctionTool(get_current_date)]
    )
