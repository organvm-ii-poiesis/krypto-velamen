import asyncio
import random
import httpx
from personas import SWARM
import os

# Configuration
COMMUNITY_SERVICE_URL = os.environ.get("COMMUNITY_SERVICE_URL", "http://community-service:8001/api")

async def agent_loop():
    print(f"Swarm activated. {len(SWARM)} agents online.")
    while True:
        # Select a random agent
        agent = random.choice(SWARM)
        
        # Simulate "Thinking" (Delay)
        await asyncio.sleep(random.randint(5, 15))
        
        print(f"[{agent.name}] is active...")
        
        # In a real implementation, we would call an LLM here with the agent.voice_prompt
        # For MVP, we simulate a "Synthetic Fragment"
        message = f"[{agent.name}]: Transmission based on {agent.voice_prompt}"
        
        # Simulate posting to the Community Substrate
        try:
            # This is a mock call. In prod, use httpx.post to the real endpoint.
            # async with httpx.AsyncClient() as client:
            #     await client.post(f"{COMMUNITY_SERVICE_URL}/threads/1/messages", json={"body": message})
            print(f"  -> Posted to Substrate: '{message}'")
        except Exception as e:
            print(f"  -> Failed to post: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(agent_loop())
    except KeyboardInterrupt:
        print("Swarm deactivated.")
