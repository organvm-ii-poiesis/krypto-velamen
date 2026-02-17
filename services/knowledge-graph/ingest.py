import os
import re
from pathlib import Path
import networkx as nx
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ARCHIVE_DIR = PROJECT_ROOT / "services" / "archive-engine" / "research"

def parse_frontmatter(text):
    match = re.search(r"```yaml\s*
(.*?)```", text, re.DOTALL)
    if match:
        # Simplified parser for MVP to avoid pyyaml dependency here if not needed
        # But we installed pyyaml in the container, so we can use it.
        try:
            import yaml
            return yaml.safe_load(match.group(1))
        except ImportError:
            return {}
    return {}

def ingest_archive():
    G = nx.DiGraph()
    
    print(f"Scanning {ARCHIVE_DIR}...")
    
    for root, _, files in os.walk(ARCHIVE_DIR):
        for file in files:
            if file.endswith(".md"):
                path = Path(root) / file
                text = path.read_text(encoding="utf-8")
                
                # Create Node for Document
                doc_id = file
                G.add_node(doc_id, type="document", path=str(path))
                
                # Extract Authors (heuristic)
                if "deep-research" in file:
                    author_name = file.replace("-deep-research.md", "").title()
                    G.add_node(author_name, type="author")
                    G.add_edge(doc_id, author_name, relation="focuses_on")
                
                # Extract Mechanisms from synthesis
                if file == "MECHANISM-ATLAS.md":
                    # Parse mechanism headers
                    mechanisms = re.findall(r"### \d+\.\s+(.+)", text)
                    for mech in mechanisms:
                        mech_id = mech.strip()
                        G.add_node(mech_id, type="mechanism")
                        G.add_edge(doc_id, mech_id, relation="defines")

    print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")
    
    # Export for visualization
    data = nx.node_link_data(G)
    with open("graph_dump.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Graph dumped to graph_dump.json")

if __name__ == "__main__":
    ingest_archive()
