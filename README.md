# KRYPTO-VELAMEN: The Platform

<div align="center">
  <p align="center">
    <strong>The Instrument v1.0 — A Living Cultural Operating System</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Architecture-Monorepo-blueviolet" alt="Monorepo">
    <img src="https://img.shields.io/badge/Services-Microservices-blue" alt="Services">
    <img src="https://img.shields.io/badge/Status-Active--Development-green" alt="Status">
    <img src="https://img.shields.io/badge/Organ-II--POIESIS-magenta" alt="Organ II">
  </p>
</div>

---

**KRYPTO-VELAMEN** has evolved from a static archive into a distributed, collaborative platform. It is a digital instrument designed to facilitate queer knowledge-building, authentic expression, and community survival through "Double-Channel" communication.

## 🏗 System Architecture

The repository is organized as a Monorepo housing distinct microservices:

```mermaid
graph TD
    Root --> Apps
    Root --> Services
    Root --> Infrastructure
    
    Apps --> Web[web-platform (Next.js)]
    
    Services --> Identity[identity-service (FastAPI)]
    Services --> Community[community-service (Django)]
    Services --> Graph[knowledge-graph (Neo4j)]
    Services --> Archive[archive-engine (The Core Corpus)]
    Services --> Swarm[agent-swarm (The Spirit)]
    Services --> Titan[titan-governor (The Law)]
    Services --> Atomizer[atomizer-engine (The Molecular)]
```

### 📂 Directory Structure

| Path | Service | Description |
|------|---------|-------------|
| **`apps/web-platform`** | **The Surface** | The user-facing frontend (Grid, Terminal, Journal). |
| **`services/archive-engine`** | **The Core** | The original research/creative corpus and `orchestrator.py`. |
| **`services/identity-service`** | **The Mask** | User profiles, authentication, and privacy calibration. |
| **`services/community-service`** | **The Substrate** | Forums, DMs, and collaborative co-authoring tools. |
| **`services/knowledge-graph`** | **The Atlas** | Recommendation engine mapping connections across the archive. |
| **`services/agent-swarm`** | **The Spirit** | AI agents based on researched author clusters. |
| **`services/titan-governor`** | **The Law** | Governance and auditing from Organ IV (TAXIS). |
| **`services/atomizer-engine`** | **The Molecular** | Linguistic atomization from Organ I (THEORIA). |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker

### The Archive Engine (Legacy Core)
To interact with the original research and creative tools:
```bash
cd services/archive-engine
python tools/orchestrator.py dashboard
```

---

## 🔮 Roadmap: The Awakening

1.  **Phase 7: Automated Animism** — Launched the `agent-swarm`.
2.  **Phase 8: Titan Governance** — Installed the `titan-governor`.
3.  **Phase 9: The Metabolic Awakening** — Fragments now decay if not witnessed.
4.  **Phase 10: The Semantic Particle** — **[ACTIVE]** Integrating LingFrame for molecular analysis.

---

## 🤝 Contributing

We welcome contributions to both the **Code** (Platform) and the **Corpus** (Archive).
Please read [`services/archive-engine/.github/CONTRIBUTING.md`](services/archive-engine/.github/CONTRIBUTING.md) for guidelines.

---

<div align="center">
  <sub>Managed by Organ II — POIESIS. Companion to <a href="https://github.com/organvm-ii-poiesis/chthon-oneiros">CHTHON-ONEIROS</a>.</sub>
</div>
