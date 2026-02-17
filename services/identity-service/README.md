# Identity Service (`services/identity-service`)

**The Mask**: Manages user identity, authentication, and profile visibility.

## Tech Stack
- **Framework**: Python (FastAPI)
- **Database**: PostgreSQL (Users, Profiles)
- **Auth**: OAuth 2.0 / OpenID Connect (via Auth0 or Keycloak)

## Core Features (MVP)
1.  **User Registration**: Sign up with "Handle" (no real names required).
2.  **Profile Management**: "Public" vs "Community" visibility toggles.
3.  **Risk Calibration**: Users set their own "Surveillance Pressure" level.

## Roadmap
- [ ] Scaffold FastAPI project.
- [ ] Define User SQL models.
- [ ] Implement JWT token issuance.
