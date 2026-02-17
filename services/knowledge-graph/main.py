import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
import networkx as nx
import json
from pathlib import Path

# Load the graph built by ingest.py
GRAPH_PATH = Path("graph_dump.json")

@strawberry.type
class Node:
    id: str
    type: str
    path: Optional[str] = None

@strawberry.type
class Query:
    @strawberry.field
    def nodes(self, type: Optional[str] = None) -> List[Node]:
        if not GRAPH_PATH.exists():
            return []
        with open(GRAPH_PATH, "r") as f:
            data = json.load(f)
        
        result = []
        for n in data["nodes"]:
            if type is None or n.get("type") == type:
                result.append(Node(id=n["id"], type=n.get("type"), path=n.get("path")))
        return result

    @strawberry.field
    def connections(self, node_id: str) -> List[Node]:
        if not GRAPH_PATH.exists():
            return []
        # In a real app, we'd use nx.read_json or similar
        with open(GRAPH_PATH, "r") as f:
            data = json.load(f)
        
        # Simple adjacency lookup
        neighbors = []
        for edge in data["links"]:
            if edge["source"] == node_id:
                neighbors.append(edge["target"])
            elif edge["target"] == node_id:
                neighbors.append(edge["source"])
        
        result = []
        for n in data["nodes"]:
            if n["id"] in neighbors:
                result.append(Node(id=n["id"], type=n.get("type"), path=n.get("path")))
        return result

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"service": "knowledge-graph", "status": "active"}
