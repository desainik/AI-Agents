import asyncio
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.runners import Runner
from research_assistant.agent import root_agent

async def run_agent(topic):
    app_name="research_assistant"
    user_id="user1"
    session_id="research_session_1"

    # Set up session service
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )

    # Create a runner to execute the agent
    runner = Runner(
        agent=root_agent,
        app_name="research_assistant",
        session_service=session_service
    )

    # Create user message
    user_message = types.Content(
        role='user',
        parts=[types.Part(text=f"Please research this topic: {topic}")]
    )

    # Track which agent is currently running
    current_agent = None
    final_report = None

 # The runner automatically calls the root_agent internally
    events = runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=user_message
    )

    # Get the events
    async for event in events:
        # Detect when a new agent starts
        if event.author != current_agent:
            current_agent = event.author
            print(f"\n----- Now running: {current_agent} -----")

        # Show final response from each sub-agent
        if event.is_final_response() and event.author != "research_assistant":
            print(f"\n===== Output from {event.author} =====")
            if event.content and event.content.parts:
                print(event.content.parts[0].text[:500] + "..." if len(event.content.parts[0].text) > 500 else
                      event.content.parts[0].text)
                print("\n")

                # Also show the state update
                if event.author == "query_builder_agent":
                    print("Search queries saved to state.")
                elif event.author == "web_search_agent":
                    print("Search results saved to state.")
                elif event.author == "content_analysis_agent":
                    print("Content analysis saved to state.")
                elif event.author == "report_generation_agent":
                    print("Report is saved.")

    current_session = await session_service.get_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )

    # Display state keys
    print("State keys:", list(current_session.state.keys()))


if __name__ == "__main__":
    asyncio.run(run_agent("Advancements in biomedical engineering and personalized medicine"))