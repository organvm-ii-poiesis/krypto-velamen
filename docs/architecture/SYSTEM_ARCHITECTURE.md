# System Architecture: KRYPTO-VELAMEN Platform
## The Instrument v1.0

---

## 1. Overview
This document defines the architectural blueprint for transforming KRYPTO-VELAMEN from a static repository into a distributed, microservices-based platform ("The Instrument"). The system is designed to support collaborative knowledge-building, user-generated content, and "Double-Channel" communication.

## 2. High-Level Architecture (C4 Model)

```mermaid
graph TD
    User[User / Witness] --> Web[Web Platform (Next.js)]
    Web --> Gateway[API Gateway (Kong/Nginx)]
    
    Gateway --> Identity[Identity Service (Python/FastAPI)]
    Gateway --> Community[Community Service (Python/Django)]
    Gateway --> Graph[Knowledge Graph (Neo4j/NetworkX)]
    Gateway --> Archive[Archive Engine (Legacy/File-Based)]
    
    Identity --> AuthDB[(PostgreSQL: Users)]
    Community --> CommDB[(PostgreSQL: Threads/Journals)]
    Graph --> GraphDB[(Neo4j: Nodes/Edges)]
    Archive --> FileSys[(Markdown Corpus)]
```

---

## 3. Service Definitions

### A. Web Platform (`apps/web-platform`)
- **Stack**: Next.js (React), Tailwind CSS, Framer Motion.
- **Role**: The "Surface Story." A polished, responsive frontend that handles user interaction, content rendering, and the "Digital-First" aesthetic.
- **Key Features**:
    - **The Grid**: A visual interface for browsing fragments.
    - **The Terminal**: A "CLI-like" mode for advanced users.
    - **Journal Editor**: A rich-text editor with "Encoding" toggles.

### B. Identity Service (`services/identity-service`)
- **Stack**: Python (FastAPI), PostgreSQL, Auth0/OpenID Connect.
- **Role**: Manages user profiles, authentication, and the "Mask."
- **Key Features**:
    - **Pseudonym Management**: Users can maintain multiple "Handles."
    - **Risk Calibration**: Profile settings for visibility (Public/Community/Private).
    - **OAuth 2.0**: Secure login via external providers.

### C. Community Service (`services/community-service`)
- **Stack**: Python (Django REST Framework), PostgreSQL, Redis.
- **Role**: The "Substrate." Handles forums, direct messaging, and collaborative journals.
- **Key Features**:
    - **Threaded Discussions**: Context-aware forums linked to research topics.
    - **Signal Messaging**: End-to-end encrypted DMs.
    - **Co-Authoring**: Real-time collaboration on fragments.

### D. Knowledge Graph (`services/knowledge-graph`)
- **Stack**: Python (NetworkX for MVP, Neo4j for Scale), GraphQL.
- **Role**: The "Atlas." Maps connections between Authors, Mechanisms, Fragments, and Users.
- **Key Features**:
    - **Recommendation Engine**: "If you use *Negative Space*, try *Porpentine*."
    - **Visualization**: Interactive node-link diagrams of the archive.

### E. Archive Engine (`services/archive-engine`)
- **Stack**: Existing Python scripts (`orchestrator.py`), File System.
- **Role**: The "Core." Manages the canonical Markdown corpus.
- **Integration**: Exposed via a wrapper API to allow the Web Platform to read/write fragments.

---

## 4. Data Flow

### The "Publishing" Flow
1. **Drafting**: User drafts a fragment in the Web Editor.
2. **Encoding**: User selects "Dials" and "Mechanisms" (fetched from Knowledge Graph).
3. **Storage**: Draft saved to `Community Service` (private).
4. **Publishing**: User hits "Publish."
    - Text committed to `Archive Engine` (Git).
    - Metadata indexed in `Knowledge Graph`.
    - Activity logged in `Identity Service`.

### The "Discovery" Flow
1. **Query**: User searches for "Silence."
2. **Resolution**:
    - `Knowledge Graph` returns related authors (Feinberg, Lorde).
    - `Archive Engine` returns fragments tagged with "Silence."
    - `Community Service` returns active discussions on the topic.
3. **Presentation**: Web Platform aggregates results into a "Dossier."

---

## 5. Security & Privacy
- **Zero-Knowledge DMs**: Message content encrypted at rest.
- **Plausible Deniability**: UI features "False Front" modes (Topic 26).
- **Data Portability**: Full GDPR compliance; users can export their "Graph."

---

## 6. Future Expansion
- **Federation**: ActivityPub support to connect with Mastodon (Topic 28).
- **AR Layer**: Mobile app for "Augmented Hiding" (Topic 22).
