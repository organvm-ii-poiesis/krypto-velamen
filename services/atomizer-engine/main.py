from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sys
import os

# Add framework to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from framework.core.atomizer import Atomizer
from framework.core.ontology import AtomLevel

app = FastAPI(title="KRYPTO-VELAMEN Atomizer Engine")

class AtomizeRequest(BaseModel):
    text: str
    slug: str
    level: str = "word"

@app.get("/")
def root():
    return {"status": "active", "service": "atomizer-engine", "framework": "LingFrame"}

@app.post("/atomize")
def atomize_text(req: AtomizeRequest):
    try:
        atomizer = Atomizer()
        # Map string level to AtomLevel
        level_map = {
            "theme": AtomLevel.THEME,
            "paragraph": AtomLevel.PARAGRAPH,
            "sentence": AtomLevel.SENTENCE,
            "word": AtomLevel.WORD,
            "letter": AtomLevel.LETTER,
        }
        
        target_level = level_map.get(req.level.lower(), AtomLevel.WORD)
        
        # Atomize the provided text
        atoms = atomizer.atomize_text(req.text, target_level)
        
        # Convert atoms to dict for response
        result = [a.to_dict() for a in atoms]
        
        return {
            "slug": req.slug,
            "level": target_level.value,
            "atom_count": len(result),
            "atoms": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze/fragment/{slug}")
def analyze_fragment(slug: str):
    # Heuristic: look for the fragment in the archive-engine directory
    fragment_path = Path(__file__).resolve().parent.parent / "archive-engine" / "drafts" / f"{slug}.md"
    
    # For now, let's assume it's in the same parent as services
    if not fragment_path.exists():
        # Try another path heuristic
        fragment_path = Path("/app/services/archive-engine/drafts") / f"{slug}.md"
        
    if not fragment_path.exists():
        raise HTTPException(status_code=404, detail=f"Fragment {slug} not found at {fragment_path}")
        
    text = fragment_path.read_text(encoding="utf-8")
    
    # We only want to atomize "The Fragment" section
    import re
    match = re.search(r"## The Fragment\s*\n(.*?)(?=\n---|\Z)", text, re.DOTALL)
    if not match:
        raise HTTPException(status_code=400, detail="Fragment content not found")
        
    content = match.group(1).strip()
    content = content.replace("_Write here._", "").strip()
    
    atomizer = Atomizer()
    atoms = atomizer.atomize_text(content, AtomLevel.WORD)
    
    return {
        "slug": slug,
        "mode": "atomic-analysis",
        "atoms": [a.to_dict() for a in atoms]
    }
