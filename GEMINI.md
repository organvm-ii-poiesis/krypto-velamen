# GEMINI.md — KRYPTO-VELAMEN Project Context

## Project Overview
**KRYPTO-VELAMEN** is a living cultural operating system and queer archive platform. It is a distributed, collaborative instrument designed to document, encode, and preserve queer interiority through the dialectic of the **Double-Channel Text**.

### Core Architecture
The project is organized as a **Monorepo** using a microservices architecture:

- **Apps**:
  - `apps/web-platform`: The "Surface Story." A Next.js (React) frontend featuring an interactive archive grid, a cyberpunk terminal interface, and collaborative journal tools.
- **Services**:
  - `services/identity-service`: The "Mask." A FastAPI service managing user profiles, JWT authentication, and privacy calibration.
  - `services/community-service`: The "Substrate." A Django REST Framework service for threaded discussions and collaborative co-authoring.
  - `services/knowledge-graph`: The "Atlas." A GraphQL engine (Strawberry) mapping connections between authors, mechanisms, and fragments using Neo4j.
  - `services/archive-engine`: The "Core." A Python-based engine (`orchestrator.py`) for scaffolding and validating creative fragments.
  - `services/agent-swarm`: The "Spirit." Autonomous AI agents embodying specific queer literary personas.
  - `services/titan-governor`: The "Law." A governance service (TAXIS) that audits repository health and enforces archival protocols.

---

## 🛠 Tech Stack
- **Languages**: Python 3.10+, TypeScript, SQL, Cypher (Neo4j).
- **Frameworks**: Next.js 14, FastAPI, Django, Strawberry (GraphQL).
- **Data**: PostgreSQL, Neo4j, Redis, SQLite (dev).
- **Infrastructure**: Docker Compose, GitHub Actions.
- **Styling**: Tailwind CSS, Framer Motion (glitch aesthetics).

---

## 🚀 Building and Running

### Full Stack (Docker)
The entire system can be orchestrated via Docker Compose:
```bash
cd infrastructure
docker-compose up --build
```

### Individual Services
- **Archive Engine**:
  ```bash
  cd services/archive-engine
  python tools/orchestrator.py dashboard
  ```
- **Web Platform**:
  ```bash
  cd apps/web-platform
  npm run dev
  ```
- **Identity Service**:
  ```bash
  cd services/identity-service
  uvicorn main:app --reload
  ```

---

## 📖 Development Conventions

### The Double-Channel Schema
Every creative fragment in `services/archive-engine/drafts/` must follow the 9-variable encoding schema:
1. `$SURFACE_STORY`: Legible layer.
2. `$SUBSTRATE_STORY`: Hidden queer layer.
3. `$MASK_TYPE`: Formal cover structure.
4. `$SIGNAL_TYPE`: How the substrate leaks.
5. `$SURVEILLANCE_PRESSURE`: External/internal threat level.
6. `$PLAUSIBLE_DENIABILITY`: 1-5 scale.
7. `$AFFECT_COST`: Emotional toll of hiding/exposure.
8. `$MULTIMEDIA_LINK`: ETCETER4 soundtrack/visual link.
9. `$AUDIENCE_PROJECTION`: Recorded witness recognition.

### Coding Style
- **Python**: PEP 8 compliance, Pydantic for data validation, asynchronous endpoints where possible.
- **Frontend**: Functional React components, Tailwind for layout, Framer Motion for interactive states.
- **Git**: Conventional Commits (e.g., `feat:`, `fix:`, `infra:`).

### The Field Model
- **Field I (Waking)**: `krypto-velamen` core.
- **Field II (Dreaming)**: `chthon-oneiros` (sibling project).
- **Migration**: Use `orchestrator.py flip` to suggest Field II transformations.

---

## 🤝 Contributing
Refer to `services/archive-engine/.github/CONTRIBUTING.md` for detailed guidelines on adding new author research or creative fragments.
