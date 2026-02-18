import os
import re
from pathlib import Path
from neo4j import GraphDatabase
import yaml
import json

# Configuration
NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "password")

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ARCHIVE_DIR = PROJECT_ROOT / "services" / "archive-engine" / "research"

class KnowledgeGraphIngest:
    def __init__(self):
        try:
            self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        except Exception:
            self.driver = None
            print("Warning: Neo4j not available. Falling back to dry-run.")

    def close(self):
        if self.driver:
            self.driver.close()

    def run_query(self, query, parameters=None):
        if not self.driver: return
        with self.driver.session() as session:
            session.run(query, parameters)

    def parse_frontmatter(self, text):
        match = re.search(r"```yaml\s*\n(.*?)```", text, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except Exception:
                return {}
        return {}

    def ingest(self):
        print(f"Ingesting from {ARCHIVE_DIR}...")
        
        # Clear existing graph (CAUTION: MVP mode)
        self.run_query("MATCH (n) DETACH DELETE n")

        for root, _, files in os.walk(ARCHIVE_DIR):
            for file in files:
                if file.endswith(".md"):
                    path = Path(root) / file
                    text = path.read_text(encoding="utf-8")
                    
                    # Create Node for Document
                    self.run_query(
                        "MERGE (d:Document {id: $id, path: $path})",
                        {"id": file, "path": str(path)}
                    )
                    
                    # Author extraction
                    if "deep-research" in file:
                        author_name = file.replace("-deep-research.md", "").title()
                        self.run_query(
                            "MERGE (a:Author {name: $name})",
                            {"name": author_name}
                        )
                        self.run_query(
                            "MATCH (d:Document {id: $doc_id}), (a:Author {name: $author_name}) "
                            "MERGE (d)-[:FOCUSES_ON]->(a)",
                            {"doc_id": file, "author_name": author_name}
                        )

                    # Mechanism extraction
                    if file == "MECHANISM-ATLAS.md":
                        mechanisms = re.findall(r"### \d+\.\s+(.+)", text)
                        for mech in mechanisms:
                            mech_name = mech.strip()
                            self.run_query(
                                "MERGE (m:Mechanism {name: $name})",
                                {"name": mech_name}
                            )
                            self.run_query(
                                "MATCH (d:Document {id: $doc_id}), (m:Mechanism {name: $mech_name}) "
                                "MERGE (d)-[:DEFINES]->(m)",
                                {"doc_id": file, "mech_name": mech_name}
                            )

        print("Ingestion complete.")

if __name__ == "__main__":
    ingester = KnowledgeGraphIngest()
    ingester.ingest()
    ingester.close()
