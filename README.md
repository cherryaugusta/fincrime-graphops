# FinCrime GraphOps — Sanctions + Beneficial Ownership Risk Explorer

**Educational Purpose & Skills Showcase:**
This repository is a portfolio-grade demonstration of Security-by-Design, typed API contracts, OpenAPI-first development, and AI Governance patterns for a London FinTech context.
It is **not a regulated AML system** and must **not be used to make real-world decisions about individuals or entities.**

## Overview

FinCrime GraphOps is a portfolio-grade full-stack project designed to demonstrate how sanctions screening and beneficial ownership risk exploration can be presented through a typed frontend, documented backend APIs, dependency-aware health checks, and governance-aware engineering controls.

The repository emphasizes:

- security-by-design implementation patterns
- typed Angular-to-API integration
- OpenAPI-first backend delivery
- operational health visibility across PostgreSQL and Redis
- request tracing through correlation IDs
- DevSecOps-oriented repository hygiene
- AI governance scaffolding for future assisted workflows

It is intentionally framed as an **educational and engineering showcase**, not as a live compliance platform, sanctions decision engine, or production AML system.

---

## What it does (Day Zero scope)

- Django REST API with OpenAPI schema and Swagger UI
- Health endpoint validating PostgreSQL and Redis connectivity
- `X-Correlation-ID` middleware for request tracing
- Angular strict-mode typed client calling the health endpoint
- DevSecOps guardrails with pre-commit, mock secret scanning, and dependency audit commands
- AI governance scaffolding for prompt cataloging and evaluation structure

---

## Why this repository matters

This project is designed to show engineering signals that are relevant to security-aware FinTech and regulated-adjacent software delivery:

- **OpenAPI-first development** with explicit schema and Swagger visibility
- **typed frontend contracts** through Angular strict mode and typed service integration
- **traceable backend behavior** through correlation ID middleware
- **dependency-aware operations** via PostgreSQL and Redis health validation
- **governance-aware scaffolding** for future AI-assisted workflows
- **repository discipline** through ADRs, scripts, linting, and pre-commit controls

---

## Core technical themes

### Security by design

The project demonstrates safe defaults, explicit environment handling, request tracing, and dependency scanning as baseline engineering controls.

### Contract-aware delivery

The frontend and backend are structured around typed contracts and OpenAPI visibility rather than ad hoc integration.

### Governance-aware AI scaffolding

AI-related artifacts are included to demonstrate governance structure, disclosure discipline, and evaluation intent, without claiming production AI decision capability.

### Portfolio-grade reproducibility

The repository is structured to be reviewable, runnable, and explainable by another engineer using local development or Docker.

---

## Screenshots

## Frontend Application

Angular client running locally.

![Frontend](screenshots/frontend-home.png)

---

## API Documentation

OpenAPI documentation served through Swagger UI.

![API Docs](screenshots/api-docs-browser.png)

---

## Health Endpoint

Operational health endpoint validating backend dependency status.

![Health Endpoint](screenshots/api-health-browser.png)

> Note: In local development, PostgreSQL or Redis may be unavailable depending on how the environment is started. This is expected in some Day Zero setups and demonstrates dependency-aware health reporting rather than silent failure.

---

## Security-by-Design (Day Zero controls)

- **No secrets in repo:** `.env` files are ignored; use `.env.example` as the template.
- **Correlation IDs:** Every request receives an `X-Correlation-ID` echoed back for traceability.
- **Secure defaults:** Secure cookie flags when not in debug mode, plus clickjacking and MIME-sniff protections.
- **Dependency hygiene:** `pip-audit` and `safety` commands included for vulnerability scanning.
- **Container safety:** Docker images use minimal base images where possible.

---

## AI Ethics and Disclosure

### PII scrubbing

- Inputs to any LLM process must be sanitized.
- Logs must store redacted prompt and output records plus model metadata only.

### Human-in-the-loop (HITL)

- Any match decision, escalation recommendation, or filing suggestion requires analyst review.

### Hallucination mitigation

- If evidence is missing, outputs must explicitly state this rather than infer unsupported conclusions.

---

## Architecture summary

### Backend responsibilities

The Django API is responsible for:

- serving REST endpoints
- publishing OpenAPI schema and Swagger UI
- exposing dependency-aware health reporting
- applying `X-Correlation-ID` middleware to requests and responses
- providing a stable platform for typed frontend consumption

### Frontend responsibilities

The Angular client is responsible for:

- consuming the health endpoint through a typed service
- demonstrating strict-mode typed integration
- surfacing backend availability in a lightweight UI
- serving as the frontend contract consumer for future feature expansion

### Governance and delivery responsibilities

The repository also includes:

- ADRs for architectural decisions
- AI governance artifacts for prompt and evaluation structure
- PowerShell scripts for verification and local workflow support
- linting and audit commands for engineering hygiene

---

## Repository structure

```text
fincrime-graphops/
│  .dockerignore
│  .env.example
│  .flake8
│  .gitignore
│  .pre-commit-config.yaml
│  docker-compose.yml
│  Dockerfile
│  LICENSE
│  README.md
│
├─ai_governance/
│  │  prompt_catalog.json
│  └─evaluations/
│     └─sample_eval.json
│
├─api/
│  │  manage.py
│  │  requirements.txt
│  │  requirements-dev.txt
│  │
│  ├─config/
│  │  │  __init__.py
│  │  │  asgi.py
│  │  │  settings.py
│  │  │  urls.py
│  │  └─wsgi.py
│  │
│  └─core/
│     │  __init__.py
│     │  admin.py
│     │  apps.py
│     │  middleware.py
│     │  models.py
│     │  serializers.py
│     │  tests.py
│     │  urls.py
│     │  views.py
│     └─migrations/
│        └─__init__.py
│
├─client/
│  ├─angular.json
│  ├─package.json
│  ├─tsconfig.json
│  └─src/
│     ├─index.html
│     ├─main.ts
│     └─app/
│        ├─app.ts
│        ├─app.config.ts
│        ├─app.routes.ts
│        └─contracts/
│           ├─entity.ts
│           └─typed-api.service.ts
│
├─docs/
│  └─adr/
│     ├─0001-security-by-design.md
│     ├─0002-openapi-first.md
│     └─0003-ai-governance.md
│
├─infra/
│  └─postgres/
│     └─init.sql
│
├─scripts/
│  ├─dev.ps1
│  ├─lint.ps1
│  └─verify-structure.ps1
│
└─screenshots/
   ├─api-docs-browser.png
   ├─api-health-browser.png
   └─frontend-home.png
````

---

## Prerequisites

Make sure the following tools are installed:

* Git
* Python 3 (`py -3`)
* Node.js and npm
* Docker
* VS Code

Recommended checks:

```powershell
git --version
py -3 --version
node --version
npm --version
docker --version
docker compose version
```

---

## Local development

### Backend

```powershell
Set-Location .\api
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Backend endpoints:

* Health: [http://127.0.0.1:8000/api/health/](http://127.0.0.1:8000/api/health/)
* Swagger UI: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
* OpenAPI schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

### Frontend

```powershell
Set-Location .\client
npm install
npx ng serve --host 127.0.0.1 --port 4200
```

Frontend URL:

* [http://127.0.0.1:4200/](http://127.0.0.1:4200/)

If any running command needs to be stopped, press:

```text
CTRL + C
```

---

## Docker

Start the full stack:

```powershell
docker compose up --build
```

This starts:

* PostgreSQL
* Redis
* Django application

To stop the containers:

```powershell
docker compose down
```

If Docker output hangs or you need to stop foreground execution, press:

```text
CTRL + C
```

---

## Quality gates

### Python lint

```powershell
Set-Location .\
.\api\.venv\Scripts\Activate.ps1
flake8
```

### Frontend lint

```powershell
Set-Location .\client
npm run lint
```

### Pre-commit checks

```powershell
Set-Location .\
.\api\.venv\Scripts\Activate.ps1
pre-commit run --all-files
```

### Dependency audit

```powershell
Set-Location .\api
.\.venv\Scripts\Activate.ps1
pip-audit
safety check
```

If `safety check` is deprecated in your version:

```powershell
safety scan
```

---

## Day Zero verification checklist

The Day Zero baseline is complete when all of the following work:

* [http://127.0.0.1:8000/api/health/](http://127.0.0.1:8000/api/health/)
* [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
* [http://127.0.0.1:4200/](http://127.0.0.1:4200/)

And development checks pass:

* `pre-commit run --all-files`
* `flake8`
* `npm run lint`
* `pip-audit`
* `safety check` or `safety scan`

---

## AI governance artifacts

The repository includes baseline governance artifacts for future AI-assisted features:

* `ai_governance/prompt_catalog.json`
* `ai_governance/evaluations/sample_eval.json`
* `docs/adr/0001-security-by-design.md`
* `docs/adr/0002-openapi-first.md`
* `docs/adr/0003-ai-governance.md`

These artifacts demonstrate governance structure but **do not make the system suitable for regulated or autonomous compliance use.**

---

## Suggested repository metadata

For a stronger GitHub presentation, configure the repository with:

* **repository name:** `fincrime-graphops`
* **description:** `Sanctions and beneficial ownership risk explorer demonstrating security-by-design, typed API contracts, OpenAPI-first delivery, and AI governance scaffolding`
* **topics:** `django`, `angular`, `typescript`, `openapi`, `swagger`, `postgresql`, `redis`, `security-by-design`, `fintech`, `aml`, `sanctions-screening`, `beneficial-ownership`, `ai-governance`

---

## Operational and compliance disclaimer

This repository is intended for:

* educational use
* portfolio demonstration
* engineering review
* architecture discussion

This repository is **not** intended for:

* regulated AML operations
* sanctions determinations
* beneficial ownership adjudication
* filing decisions
* autonomous risk scoring in real production settings

Any future real-world implementation would require legal, compliance, privacy, model governance, auditability, and operational controls beyond this repository’s scope.

---

## Secrets and environment handling

Do not commit:

* real `.env` files
* API keys
* credentials
* tokens
* secrets of any kind

Use `.env.example` as the safe template and keep local secrets untracked.

---

## License

This project is licensed under the MIT License.

Copyright (c) 2026 Cherry Augusta

This repository is provided for educational and portfolio purposes only. The MIT License governs copying, modification, distribution, and reuse, but the repository remains unsuitable for regulated or production compliance use.

See the [LICENSE](./LICENSE) file for full details.

---
