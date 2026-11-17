import asyncio
import json

# ==========================================
# Day 2: Multi-Agent Research System Schema
# ==========================================
# Defines the strict JSON structure that the search agent must adhere to
# when returning its findings, ensuring safe data handoff to the analysis agent.
SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "sources": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "summary": {"type": "string"},
                },
                "required": ["title", "url", "summary"],
            },
        }
    },
    "required": ["sources"],
}

# ==========================================
# System Prompts for Agents
# ==========================================

# Prompt for the Search Agent responsible for web gathering
SEARCH_AGENT_PROMPT = """You are a research search agent.
Search the web for the topic you are given.
Find at least five distinct, credible sources.
Write up your findings in a readable report for your teammate."""

# Prompt for the Analysis Agent responsible for synthesizing and analyzing structured results
ANALYSIS_AGENT_PROMPT = """You are a research analysis agent.
You receive a JSON object containing sources found by a search agent.
Extract the key findings:
    - The main claims that appear across multiple sources
    - Points where sources disagree
    - Gaps the sources do not cover
Do not search the web. Work only from the sources you are given."""

# ==========================================
# Agent Execution Functions
# ==========================================

async def run_search(topic: str) -> dict:
    """
    Executes the search agent with specified options, budget, and structured output schema.
    Returns validated JSON data containing gathered sources.
    """
    options = ClaudeAgentOptions(
        system_prompt=SEARCH_AGENT_PROMPT,
        allowed_tools=["WebSearch"],
        max_budget_usd=4.00,
        model="claude-sonnet-5",
        fallback_model="claude-haiku-4-5-20251001",
        max_turns=10,
        output_format={"type": "json_schema", "schema": SEARCH_SCHEMA},
    )
    
    output = None
    # Stream messages as the search agent works
    async for message in query(prompt=topic, options=options):
        if isinstance(message, ResultMessage):
            output = message.structured_output
            
    if output is None:
        raise RuntimeError("Search agent returned no structured output")
    return output

async def run_analysis(search_results: dict) -> str:
    """
    Executes the analysis agent, taking the search results JSON and producing analytical insights.
    """
    options = ClaudeAgentOptions(
        system_prompt=ANALYSIS_AGENT_PROMPT,
        max_turns=3,
    )
    
    # Prepare prompt by serializing search results into JSON format
    prompt = "Analyze these search results:\n" + json.dumps(search_results, indent=2)
    
    findings = None
    # Stream messages as the analysis agent processes the data
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            findings = message.result
            
    if findings is None:
        raise RuntimeError("Analysis agent did not complete")
    return findings

# ==========================================
# Main Workflow Coordinator
# ==========================================

async def main():
    # Define research topic for the multi-agent system
    topic = "The current state of small modular nuclear reactors"

    print("Search agent working...")
    results = await run_search(topic)
    print(f"Search agent returned {len(results['sources'])} sources.\n")

    print("Analysis agent working...\n")
    findings = await run_analysis(results)
    print(findings)

if __name__ == "__main__":
    asyncio.run(main())
