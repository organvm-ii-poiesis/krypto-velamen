import networkx as nx
import json
from pathlib import Path

GRAPH_PATH = Path("graph_dump.json")

def get_recommendations(node_id: str, top_n: int = 3):
    if not GRAPH_PATH.exists():
        return []
    
    with open(GRAPH_PATH, "r") as f:
        data = json.load(f)
    
    G = nx.node_link_graph(data)
    
    if node_id not in G:
        return []
    
    # Simple recommendation: find nodes that share the same neighbors
    # (e.g., authors who share the same mechanisms)
    recommendations = {}
    neighbors = set(G.neighbors(node_id))
    
    for other_node in G.nodes():
        if other_node == node_id:
            continue
        
        other_neighbors = set(G.neighbors(other_node))
        shared = neighbors.intersection(other_neighbors)
        
        if shared:
            recommendations[other_node] = len(shared)
            
    # Sort by number of shared neighbors
    sorted_recs = sorted(recommendations.items(), key=lambda x: -x[1])
    return sorted_recs[:top_n]

if __name__ == "__main__":
    # Test recommendation for a mechanism or author
    print(f"Recommendations for 'Negative Space': {get_recommendations('Negative Space')}")
