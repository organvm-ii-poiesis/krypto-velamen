# Community Service (`services/community-service`)

**The Substrate**: Handles social interaction, messaging, and collaborative writing.

## Tech Stack
- **Framework**: Python (Django REST Framework)
- **Database**: PostgreSQL (Threads, Messages)
- **Cache**: Redis (Real-time presence)

## Core Features (MVP)
1.  **Threaded Forums**: Context-aware discussions linked to `research/` topics.
2.  **Journals**: Private/Public writing spaces for users.
3.  **Direct Messaging**: Encrypted "Signal" messaging between users.

## Roadmap
- [ ] Scaffold Django project.
- [ ] Define "Journal" and "Thread" data models.
- [ ] Implement "Co-Authoring" WebSocket logic.
