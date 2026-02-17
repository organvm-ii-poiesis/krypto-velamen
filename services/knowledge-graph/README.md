# Knowledge Graph Service (`services/knowledge-graph`)

**The Atlas**: Maps connections between Authors, Mechanisms, Fragments, and Users.

## Tech Stack
- **Engine**: Python (NetworkX for MVP) -> Neo4j (Production)
- **API**: GraphQL (Strawberry or Graphene)

## Core Features (MVP)
1.  **Ingestion**: Parses the `archive-engine` Markdown corpus into nodes/edges.
2.  **Discovery**: "If you use *Negative Space*, try *Porpentine*."
3.  **Visualization**: JSON output for frontend node-link diagrams.

## Roadmap
- [ ] Implement graph ingestion script (port logic from `seed.yaml`).
- [ ] Define GraphQL schema.
- [ ] Build recommendation algorithm based on "Dial" similarity.
