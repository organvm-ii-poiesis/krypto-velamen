# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

KRYPTO-VELAMEN — a distributed microservices platform and queer literary archive. "The Instrument v1.0": a living cultural operating system for double-channel text, concealment as compositional engine, and archival of lived interiority. Part of the ORGANVM system (Organ II — Art / POIESIS).

## Build & Run Commands

### Full Stack (Docker Compose)
```bash
cd infrastructure && docker-compose up --build
```

### Individual Services

| Service | Port | Run Command |
|---------|------|-------------|
| **web-platform** | 3000 | `cd apps/web-platform && npm run dev` |
| **identity-service** | 8000 | `cd services/identity-service && uvicorn main:app --reload` |
| **community-service** | 8001 | `cd services/community-service && python manage.py runserver 8001` |
| **knowledge-graph** | 8002 | `cd services/knowledge-graph && uvicorn main:app --port 8002 --reload` |
| **titan-governor** | 8003 | `cd services/titan-governor && uvicorn main:app --port 8003 --reload` |
| **atomizer-engine** | 8005 | `cd services/atomizer-engine && uvicorn main:app --port 8005 --reload` |
| **lens-engine** | 8006 | `cd services/lens-engine && uvicorn main:app --port 8006 --reload` |
| **agent-swarm** | — | `cd services/agent-swarm && python main.py` (long-running loop) |

### Frontend
```bash
cd apps/web-platform
npm install
npm run dev      # dev server
npm run build    # production build
npm run lint     # Next.js linting
```

### Orchestrator CLI (Archive Engine)
```bash
cd services/archive-engine
python tools/orchestrator.py dashboard                              # project stats + triforce balance
python tools/orchestrator.py scaffold --slug my-fragment --preset confessional-whisper
python tools/orchestrator.py validate drafts/2026-02-17-example.md  # schema integrity check
python tools/orchestrator.py display drafts/2026-02-17-example.md   # digital-first rendering
python tools/orchestrator.py flip drafts/2026-02-17-example.md      # suggest Field II transformation
python tools/orchestrator.py atomize drafts/2026-02-17-example.md   # semantic particle detection
```
Orchestrator requires `PyYAML`; optional `rich` for enhanced terminal UI.

### Python Dependencies (per service)
Each service has its own `requirements.txt`. Install with:
```bash
pip install -r requirements.txt
```

## Architecture

### Monorepo Layout
- **`apps/web-platform`** — Next.js 14 frontend (React, Tailwind CSS, Framer Motion). Routes: `/` (grid), `/terminal`, `/atlas`, `/community`, `/identity`.
- **`services/`** — Python microservices, each with its own Dockerfile.
- **`infrastructure/`** — `docker-compose.yml` orchestrates all services + databases (PostgreSQL, Neo4j, Redis).
- **`docs/`** — `architecture/` (system design, OpenAPI spec), `theory/` (theoretical frameworks).

### Service Map (Codenames)

| Service | Codename | Framework | Database | Role |
|---------|----------|-----------|----------|------|
| identity-service | The Mask | FastAPI + SQLModel | PostgreSQL | JWT auth, user profiles, privacy calibration |
| community-service | The Substrate | Django REST Framework | PostgreSQL + Redis | Threads, DMs, journals, co-authoring |
| knowledge-graph | The Atlas | Strawberry GraphQL + NetworkX | Neo4j | Recommendation engine, entity relationships |
| archive-engine | The Core | FastAPI wrapper around `orchestrator.py` | Filesystem (Markdown) | Canonical corpus, fragment scaffolding/validation |
| agent-swarm | The Spirit | Async Python (httpx) | — | Autonomous AI personas that post to community threads |
| titan-governor | The Law | FastAPI | — | Governance auditing from Organ IV (TAXIS) |
| atomizer-engine | The Molecular | FastAPI + spaCy/NLTK | — | Linguistic atomization (NLP analysis of fragments) |
| lens-engine | The Geometry | FastAPI + pysbd | — | Narratological lens analysis |

### Inter-Service Communication
Services communicate via HTTP REST. Key dependencies (defined in `docker-compose.yml`):
- `web-platform` → `identity-service`, `community-service`
- `agent-swarm` → `community-service` (posts to threads autonomously)
- `titan-governor` → `archive-engine`, `agent-swarm`
- `atomizer-engine`, `lens-engine` → `archive-engine`
- `knowledge-graph` → Neo4j

### Archive Engine Internals
- `tools/orchestrator.py` — CLI with subcommands: `dashboard`, `scaffold`, `validate`, `display`, `flip`, `atomize`
- `entropy.py` — Metabolic decay loop: unwatched fragments lose integrity over time (Phase 9)
- `deep_storage.py` — SHA-256 content-addressed storage simulation (IPFS-style CID hashing)
- `drafts/TEMPLATE.md` — Fragment template with 9-variable encoding schema
- `seed.yaml` — Automation contract defining agent triggers and event subscriptions

## Domain Concepts

### The Double-Channel Text
Every creative fragment operates on two frequencies:
- **Polarity A (Concealment)**: Surface story is legible; substrate story is queer-encoded beneath. Dials: `rimbaud_drift`, `wilde_mask`, `burroughs_control`.
- **Polarity B (Visibility)**: Everything announced; substrate is mythological excess. Dials: `lorde_voice`, `arenas_scream`, `acker_piracy`.

### The Artistic Triforce
Fragments are tagged with one of three intentionality poles: `conscious`, `subconscious`, `temporal`. The orchestrator tracks triforce balance across the corpus.

### 9-Variable Encoding Schema
All fragments in `drafts/` use YAML frontmatter: `surface_story`, `substrate_story`, `mask_type`, `signal_type`, `surveillance_pressure`, `plausible_deniability`, `affect_cost`, `multimedia_link`, `audience_projection`.

### Fragment Presets
9 named presets in orchestrator (e.g. `confessional-whisper`, `systems-dread`, `mythological-depth`) that pre-configure polarity, triforce, and dial values.

### Field Model
- **Field I (Present Waking)**: This repo (krypto-velamen)
- **Field II (Present Dreaming)**: Sibling repo (chthon-oneiros)
- The `flip` command suggests how a Field I fragment could transform into Field II

## Conventions

- **Git commits**: Conventional Commits (`feat:`, `fix:`, `infra:`)
- **Python**: PEP 8, Pydantic for validation, async endpoints where possible
- **Frontend**: Functional React components, Tailwind for layout, Framer Motion for animation
- **Creative fragments**: Must follow the encoding schema in `drafts/TEMPLATE.md`
- **No AI in creative identity**: AI assists process (tooling, research), not the creative product itself

## External Stores
- **Knowledge Graph MCP**: 106 entities, 118 relations
- **Neon DB**: project `snowy-moon-43700360` (13 tables)
- **Companion Neon DB**: project `plain-wind-21545579` (chthon-oneiros)

## ORGANVM Context
Organ II (Art) under `organvm-ii-poiesis` GitHub org.
- Registry: [`registry-v2.json`](https://github.com/meta-organvm/organvm-corpvs-testamentvm/blob/main/registry-v2.json)
- Corpus: [`organvm-corpvs-testamentvm`](https://github.com/meta-organvm/organvm-corpvs-testamentvm)
