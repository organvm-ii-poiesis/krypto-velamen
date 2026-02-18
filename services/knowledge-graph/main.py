import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from neo4j import GraphDatabase
import os

# Configuration
NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "password")

@strawberry.type
class Node:
    id: str
    type: str
    path: Optional[str] = None

@strawberry.type
class Query:
    @strawberry.field
    def nodes(self, label: str) -> List[Node]:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            # Query by label (Author, Mechanism, Document)
            result = session.run(f"MATCH (n:{label}) RETURN n")
            nodes = []
            for record in result:
                n = record["n"]
                nodes.append(Node(
                    id=n.get("name") or n.get("id"),
                    type=label,
                    path=n.get("path")
                ))
        driver.close()
        return nodes

    @strawberry.field
    def connections(self, node_id: str) -> List[Node]:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            query = (
                "MATCH (n {name: $id})--(m) RETURN m, labels(m)[0] as lbl "
                "UNION "
                "MATCH (n {id: $id})--(m) RETURN m, labels(m)[0] as lbl"
            )
            result = session.run(query, {"id": node_id})
            nodes = []
            for record in result:
                m = record["m"]
                nodes.append(Node(
                    id=m.get("name") or m.get("id"),
                    type=record["lbl"],
                    path=m.get("path")
                ))
        driver.close()
        return nodes

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"service": "knowledge-graph", "db": "neo4j", "status": "active"}
