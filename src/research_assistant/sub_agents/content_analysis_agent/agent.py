import os
from google.adk.agents import LlmAgent

from . import prompt as p

# Create content analysis agent.
content_analysis_agent = LlmAgent(
    model=os.getenv('MODEL'),
    name="content_analysis_agent",
    instruction=p.CONTENT_ANALYSIS_PROMPT,
    output_key='content_analysis'
)