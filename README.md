# FinCrime GraphOps — Sanctions + Beneficial Ownership Risk Explorer

**Educational Purpose & Skills Showcase:** This repository is a portfolio-grade demonstration of Security-by-Design, typed API contracts, OpenAPI-first development, and AI Governance patterns for a London FinTech context. It is not a regulated AML system and must not be used to make real-world decisions about individuals or entities.

## What it does (Day Zero scope)

- Django REST API with OpenAPI schema and Swagger UI
- Health endpoint validating PostgreSQL and Redis connectivity
- `X-Correlation-ID` middleware for request tracing
- Angular strict-mode typed client calling the health endpoint
- DevSecOps guardrails with pre-commit, mock secret scanning, and dependency audit commands
- AI governance scaffolding for prompt cataloging and evaluation structure

## Security-by-Design (Day Zero controls)

- **No secrets in repo:** `.env` files are ignored; use `.env.example` as the template.
- **Correlation IDs:** Every request gets an `X-Correlation-ID` echoed back for traceability.
- **Tight defaults:** Secure cookie flags when not in debug mode, plus clickjacking and MIME-sniff protections.
- **Dependency hygiene:** `pip-audit` and `safety` commands are included; Docker uses minimal base images.

## AI Ethics and Disclosure

### PII scrubbing

- Inputs to any LLM process must be sanitized.
- Logs must store redacted prompt and output records plus model metadata only.

### Human-in-the-loop (HITL)

- Any match decision, escalation recommendation, or filing suggestion requires analyst review.

### Hallucination mitigation

- If evidence is missing, outputs must say so rather than infer.

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
└─scripts/
   ├─dev.ps1
   ├─lint.ps1
   └─verify-structure.ps1
```

## Prerequisites

Make sure the following tools are installed on Windows:

- Git
- Python 3 via `py -3`
- Node.js and npm
- Docker
- VS Code

## Local development

### Backend

```powershell
Set-Location .\api
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Backend endpoints:

- Health: `http://127.0.0.1:8000/api/health/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`

### Frontend

```powershell
Set-Location .\client
npm install
ng serve --host 127.0.0.1 --port 4200
```

Frontend URL:

- App: `http://127.0.0.1:4200/`

### Docker

```powershell
docker compose up --build
```

This starts:

- PostgreSQL
- Redis
- Django app

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

### Pre-commit

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

If `safety check` is deprecated in your installed version:

```powershell
safety scan
```

## Git workflow

- Run Git commands from repo root: `D:\Projects\fincrime-graphops`
- Create feature branches from `develop`
- Run lint and pre-commit before committing
- Merge into `develop`
- Merge `develop` into `main` only when stable

## Important constraints

- Do not commit `.env`
- Do not create `core\migrations.py`
- Do not run Git from `api` or `client` unless intentional
- Do not skip CORS when Angular calls Django on another port
- Do not push before `pre-commit run --all-files` passes

## AI governance artifacts

The repository includes baseline AI governance artifacts:

- `ai_governance/prompt_catalog.json`
- `ai_governance/evaluations/sample_eval.json`
- `docs/adr/0001-security-by-design.md`
- `docs/adr/0002-openapi-first.md`
- `docs/adr/0003-ai-governance.md`

These exist to demonstrate governance structure for future AI-assisted features. They do not make the system suitable for regulated or autonomous compliance use.

## Day Zero success criteria

The Day Zero baseline is complete when all of the following are true:

- `http://127.0.0.1:8000/api/health/` works
- `http://127.0.0.1:8000/api/docs/` works
- `http://127.0.0.1:4200/` works
- `pre-commit run --all-files` passes
- `flake8` passes
- `npm run lint` passes
- `pip-audit` completes
- `safety check` or `safety scan` completes
- `develop` is pushed
- `main` is pushed

## License
This repository is intended for educational and portfolio purposes.

