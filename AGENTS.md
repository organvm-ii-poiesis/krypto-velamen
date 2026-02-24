# Repository Guidelines

Global policy: /Users/4jp/AGENTS.md applies and cannot be overridden.

## Project Structure & Module Organization
`krypto-velamen` is a monorepo:
- `apps/web-platform/`: Next.js 14 frontend (`app/`, `components/`, `lib/`).
- `services/`: Python services (`identity-service`, `community-service`, `knowledge-graph`, `archive-engine`, `agent-swarm`, `titan-governor`, `atomizer-engine`, `lens-engine`).
- `services/archive-engine/drafts/` and `services/archive-engine/research/`: canonical corpus content.
- `services/archive-engine/tools/orchestrator.py`: archive CLI for scaffold/validate/display workflows.
- `infrastructure/docker-compose.yml`: multi-service local orchestration.
- `docs/architecture/`, `docs/theory/`: design and domain docs.

## Build, Test, and Development Commands
Run from repo root unless noted:
```bash
cd infrastructure && docker-compose up --build     # full stack
cd apps/web-platform && npm install && npm run dev # frontend dev server
cd apps/web-platform && npm run build && npm run lint
cd services/identity-service && uvicorn main:app --reload
cd services/community-service && python manage.py runserver 8001
cd services/knowledge-graph && uvicorn main:app --port 8002 --reload
cd services/archive-engine && python tools/orchestrator.py dashboard
cd services/archive-engine && python tools/orchestrator.py validate drafts/<file>.md
```
Install Python deps per service using its `requirements.txt` (or `tools/requirements.txt` for archive tools).

## Coding Style & Naming Conventions
- Python: PEP 8, 4-space indentation, `snake_case` for functions/modules, type-aware FastAPI/Django code.
- TypeScript/React: functional components, `PascalCase` for component files (for example `ArchiveGrid.tsx`), route files as `app/**/page.tsx`.
- Keep API/service names aligned with existing folders and Docker service names.
- Commits follow Conventional Commit prefixes used in history: `feat:`, `docs:`, `infra:`, `fix:`.

## Testing Guidelines
- Current enforced check is fragment validation in `archive-engine`; run `orchestrator.py validate` before PRs that touch drafts/tools.
- There is no unified top-level unit test suite yet; for service changes, add focused tests in a local `tests/` package where practical.
- Suggested naming when adding tests: `test_<feature>.py` (Python) and `*.test.tsx` (frontend).

## Commit & Pull Request Guidelines
- Use imperative commit subjects and keep the first line concise (target ≤72 chars).
- PRs should include: summary, linked issue (`Fixes #...`), change type, and explicit test/validation evidence.
- Include before/after screenshots or short recordings for `apps/web-platform` UI changes.
- For archive/corpus or docs changes, update related documentation (for example catalog/index files) in the same PR.

## Security & Configuration Tips
- Do not rely on default secrets in committed config; prefer environment variables (`SECRET_KEY`, `DATABASE_URL`, `NEO4J_URI`, `REDIS_URL`).
- Keep local credentials in untracked env files and avoid hardcoding production values.

<!-- ORGANVM:AUTO:START -->
## Agent Context (auto-generated — do not edit)

This repo participates in the **ORGAN-II (Art)** swarm.

### Active Subscriptions
- *No active event subscriptions*

### Production Responsibilities
- *No production responsibilities*

### External Dependencies
- *No external dependencies*

### Governance Constraints
- Adhere to unidirectional flow: I→II→III
- Never commit secrets or credentials

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
