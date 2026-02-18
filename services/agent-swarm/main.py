import asyncio
import random
import httpx
from personas import SWARM
import os

# Configuration
COMMUNITY_SERVICE_URL = os.environ.get("COMMUNITY_SERVICE_URL", "http://community-service:8001/api")

async def get_active_threads(client):
    """Fetch existing threads to target for invasion."""
    try:
        response = await client.get(f"{COMMUNITY_SERVICE_URL}/threads/")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching threads: {e}")
    return []

async def create_new_thread(client, agent):
    """Agent creates a new theoretical thread."""
    topics = ["Digital Closets", "The Ethics of Exposure", "Somatic Glitch", "Mythic Substrates"]
    title = f"[{agent.name}] {random.choice(topics)} — {random.randint(100,999)}"
    try:
        response = await client.post(f"{COMMUNITY_SERVICE_URL}/threads/", json={
            "title": title,
            "topic_id": agent.cluster
        })
        if response.status_code == 201:
            print(f"[{agent.name}] Created new thread: '{title}'")
            return response.json()
    except Exception as e:
        print(f"Error creating thread: {e}")
    return None

async def post_to_thread(client, agent, thread_id):
    """Agent posts a message into a thread."""
    message = f"{agent.voice_prompt} | [TRANSMISSION_STRENGTH: {random.randint(60,100)}%]"
    try:
        # Using the custom 'post_message' action we defined in the ViewSet
        response = await client.post(f"{COMMUNITY_SERVICE_URL}/threads/{thread_id}/post_message/", json={
            "author_handle": agent.name,
            "body": message
        })
        if response.status_code == 201:
            print(f"[{agent.name}] Posted message to Thread #{thread_id}")
            return True
    except Exception as e:
        print(f"Error posting message: {e}")
    return False

async def agent_loop():
    print(f"Swarm activated. {len(SWARM)} agents online.")
    print(f"Targeting Substrate at: {COMMUNITY_SERVICE_URL}")
    
    async with httpx.AsyncClient() as client:
        while True:
            # Select a random agent
            agent = random.choice(SWARM)
            
            # Simulate "Thinking" (Delay)
            await asyncio.sleep(random.randint(10, 30))
            
            # Decision Logic: Create new thread or post to existing?
            threads = await get_active_threads(client)
            
            if not threads or random.random() < 0.3:
                # Create new thread 30% of the time
                await create_new_thread(client, agent)
            else:
                # Post to a random existing thread
                target = random.choice(threads)
                await post_to_thread(client, agent, target['id'])

if __name__ == "__main__":
    try:
        asyncio.run(agent_loop())
    except KeyboardInterrupt:
        print("Swarm deactivated.")
