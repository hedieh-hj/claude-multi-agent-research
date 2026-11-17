import asyncio

# Note: This is an educational script based on an Anthropic / Claude agentic loop example.
# It requires the appropriate SDK / packages (such as anthropic or the specific agent package being used in the tutorial).

async def run_search_agent(topic: str) -> None:
    max_budget_usd=4.00,
    model="claude-sonnet-5",
    fallback_model="claude-haiku-4-5-20251001",
    max_turns=10,
    )

    # Agentic loop: streams messages as Claude works
    async for message in query(prompt=topic, options=options):
        # Print human-readable output
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
        elif isinstance(message, ResultMessage):
            print(f"\nDone in {message.num_turns} turns.")
            print(f"Estimated cost: ${message.total_cost_usd:.4f}")

if __name__ == "__main__":
    asyncio.run(run_search_agent("The current state of quantum computing"))
