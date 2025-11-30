import os
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt as p

# Create web search agent using built-in google search tool
web_search_agent = LlmAgent(
    model=os.getenv('MODEL'),
    name="web_search_agent",
    instruction=p.WEB_RESEARCH_PROMPT,
    tools=[google_search],
    output_key='search_results'
)