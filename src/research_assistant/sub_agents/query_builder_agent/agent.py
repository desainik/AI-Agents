import os
from google.adk.agents import LlmAgent

from . import prompt as p

# Create query builder agent.
query_builder_agent = LlmAgent(
    model=os.getenv('MODEL'),
    name="query_builder_agent",
    instruction=p.QUERY_FORMAT_PROMPT,
    output_key='search_queries'
)