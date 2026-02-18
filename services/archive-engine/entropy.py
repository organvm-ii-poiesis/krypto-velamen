import asyncio
import httpx
import os
from datetime import datetime, timezone

# Configuration
COMMUNITY_SERVICE_URL = os.environ.get("COMMUNITY_SERVICE_URL", "http://community-service:8001/api")
DECAY_RATE = 0.05  # Increase decay by 5% every cycle

async def metabolize():
    """
    Scan all journals and apply entropy (decay).
    Fragments that are not 'witnessed' lose surface integrity.
    """
    print(f"[{datetime.now().isoformat()}] Entropy Engine: Pulsing...")
    
    async with httpx.AsyncClient() as client:
        try:
            # 1. Fetch all journals
            response = await client.get(f"{COMMUNITY_SERVICE_URL}/journals/")
            if response.status_code != 200:
                print("  -> Failed to fetch journals.")
                return
            
            journals = response.json()
            
            for journal in journals:
                current_decay = journal.get('decay_level', 0.0)
                
                # Check how long since last witnessed
                # (In this simulation, we just apply constant decay until a 'witness' event resets it)
                new_decay = min(1.0, current_decay + DECAY_RATE)
                
                if new_decay != current_decay:
                    # 2. Update the journal with new decay level
                    await client.patch(f"{COMMUNITY_SERVICE_URL}/journals/{journal['id']}/", json={
                        "decay_level": new_decay
                    })
                    print(f"  -> {journal['slug']} decayed to {new_decay:.2f}")
                    
                    if new_decay >= 1.0:
                        print(f"  -> CRITICAL: {journal['slug']} reach reality limit. TRIGGERING FLIP.")
                        # This would call the Titan Governor to flip the field
        
        except Exception as e:
            print(f"  -> Error during metabolism: {e}")

async def entropy_loop():
    while True:
        await metabolize()
        await asyncio.sleep(60) # Pulse every minute for simulation

if __name__ == "__main__":
    try:
        asyncio.run(entropy_loop())
    except KeyboardInterrupt:
        print("Entropy Engine stopped.")
