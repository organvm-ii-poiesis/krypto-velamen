import hashlib
import json
from pathlib import Path
from datetime import datetime

# Simulation of IPFS Hashing
def commit_to_deep_storage(fragment_path: Path):
    if not fragment_path.exists():
        return None
    
    content = fragment_path.read_text(encoding="utf-8")
    
    # Calculate SHA-256 (simulating CID)
    ipfs_hash = hashlib.sha256(content.encode()).hexdigest()
    
    timestamp = datetime.utcnow().isoformat()
    
    record = {
        "fragment": fragment_path.name,
        "cid": ipfs_hash,
        "timestamp": timestamp,
        "status": "IMMUTABLE"
    }
    
    # Append to a local ledger
    ledger_path = fragment_path.parent / "DEEP_STORAGE_LEDGER.json"
    
    ledger = []
    if ledger_path.exists():
        with open(ledger_path, "r") as f:
            try:
                ledger = json.load(f)
            except json.JSONDecodeError:
                pass
    
    ledger.append(record)
    
    with open(ledger_path, "w") as f:
        json.dump(ledger, f, indent=2)
        
    print(f"Committed {fragment_path.name} to Deep Storage. CID: {ipfs_hash[:16]}...")
    return ipfs_hash

if __name__ == "__main__":
    # Test with a dummy file
    import sys
    if len(sys.argv) > 1:
        commit_to_deep_storage(Path(sys.argv[1]))
    else:
        print("Usage: python deep_storage.py <path_to_fragment>")
