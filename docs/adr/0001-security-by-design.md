# ADR 0001: Security by Design for FinCrime GraphOps Day Zero

- Status: Accepted
- Date: 2026-03-08
- Deciders: Project Maintainer
- Technical Story: Establish the Day Zero security baseline for a portfolio-grade sanctions and beneficial ownership risk exploration platform

## Context

FinCrime GraphOps is a portfolio-grade demonstration project for a London FinTech context. The project is intended to showcase engineering discipline in a sensitive problem domain that involves sanctions screening, beneficial ownership exploration, graph relationships, and AI governance patterns.

Even at Day Zero, the project must assume that it operates in a high-sensitivity environment. The system is not a regulated AML platform and must not be used for real-world decisions about individuals or entities, but its architecture, defaults, and developer workflow should reflect a security-first approach.

The initial stack consists of:

- Django REST API
- PostgreSQL
- Redis
- Angular client
- Docker and Docker Compose for local orchestration
- Git and GitHub for source control
- Pre-commit hooks and local linting/audit tooling
- AI governance scaffolding for future LLM-assisted workflows

The project must therefore define a clear baseline for secure defaults, traceability, dependency hygiene, and secret handling from the first commit onward.

## Decision

We will adopt a Security-by-Design baseline from Day Zero with the following controls and design choices.

### 1. Secrets must not be committed to the repository

Configuration secrets must be externalized from source code and excluded from version control.

- `.env` files are ignored by Git
- `.env.example` is committed as a non-secret template only
- credentials, API keys, tokens, and private keys must never be hard-coded into source files
- pre-commit includes secret-detection controls, including built-in checks and a mock PowerShell secret scan

### 2. Development and runtime configuration must default to explicit environment variables

Sensitive and deployment-dependent settings must be configured using environment variables.

This includes at minimum:

- Django secret key
- debug mode
- allowed hosts
- database host, port, username, password, and database name
- Redis connection URL
- SSL redirect behavior where applicable

Development defaults may exist for local bootstrapping, but they must be clearly unsafe for production and easy to override.

### 3. HTTP request traceability must be included by default

The API must support correlation identifiers for request tracing.

- inbound `X-Correlation-ID` values are accepted when provided
- a new correlation ID is generated when absent
- the resolved correlation ID is attached to the response
- tracing support is implemented in middleware rather than ad hoc per endpoint

This supports observability, debugging, and future auditability.

### 4. Secure HTTP-related defaults must be enabled where practical

The Django application must use conservative security defaults.

This includes:

- clickjacking protection via `X_FRAME_OPTIONS = "DENY"`
- MIME sniff protection via `SECURE_CONTENT_TYPE_NOSNIFF = True`
- secure referrer policy
- secure cookie flags when not in debug mode
- optional SSL redirect support via environment variable

These controls reduce common web application exposure while remaining practical for local development.

### 5. Cross-origin access must be explicit and minimal

Because the Angular client runs on a different local port than the Django API during development, CORS must be enabled deliberately rather than bypassed.

The initial allowlist is restricted to local frontend origins only:

- `http://127.0.0.1:4200`
- `http://localhost:4200`

This allows local developer productivity without opening unrestricted cross-origin access.

### 6. Dependency hygiene must be part of normal development workflow

Security-related dependency checks must be included from the beginning.

The repository includes:

- `pip-audit`
- `safety`
- `flake8`
- `pre-commit`

These tools do not guarantee absence of vulnerabilities, but they reduce avoidable risk and establish a disciplined engineering workflow.

### 7. Containerization must prefer minimal and non-root runtime posture

Docker images must follow reasonably hardened defaults for a portfolio project.

This includes:

- slim Python base images
- multi-stage builds where practical
- non-root runtime user for the application container
- exclusion of unnecessary files through `.dockerignore`

This reduces attack surface and improves deployment hygiene.

### 8. The system must not make autonomous compliance decisions

Because the domain touches sanctions and financial crime risk, the software must not present itself as a real compliance decision engine.

Therefore:

- outputs must be framed as analyst-support only
- any future AI-assisted features must require human review for consequential decisions
- uncertainty must be stated explicitly
- the project README and governance artifacts must disclose the educational and non-production nature of the system

### 9. Logging and future AI features must follow data-minimization principles

As the project evolves, sensitive data handling must remain conservative.

At Day Zero, the baseline principle is:

- avoid storing secrets in logs
- avoid unnecessary logging of sensitive personal data
- require prompt and output governance for future LLM workflows
- prefer redaction and minimization over broad retention

## Consequences

### Positive consequences

- Security expectations are defined from the first commit
- common mistakes such as committing secrets become less likely
- local development remains practical while preserving disciplined defaults
- observability and audit-oriented features can build on an existing correlation ID mechanism
- future AI features inherit explicit governance and human-review constraints
- the repository better demonstrates mature engineering practice for a sensitive domain

### Negative consequences

- local setup is slightly more complex because configuration must be externalized
- developers must maintain `.env.example`, hook configurations, and audit tooling
- some defaults require explanation to avoid confusion during local development
- dependency scans may produce noisy findings that need interpretation rather than blind action

### Trade-offs accepted

- we accept light local-development friction in exchange for safer defaults
- we accept mock secret-scanning initially, with the expectation that stronger scanners may be adopted later
- we accept development fallback values only where necessary to keep Day Zero onboarding practical

## Alternatives considered

### 1. Add security controls later after functional milestones

Rejected.

Delaying security posture would create rework, weaken the portfolio value of the repository, and normalize unsafe early habits such as hard-coded secrets or permissive defaults.

### 2. Use permissive CORS and unrestricted debug-first settings

Rejected.

This would make local development simpler but would set a poor baseline for a sensitive domain and increase the likelihood of insecure carryover into later phases.

### 3. Treat the project purely as a demo with minimal safeguards

Rejected.

Even as a portfolio project, the subject matter involves regulated-adjacent workflows and sensitive data patterns. The project should demonstrate seriousness about security and governance from the start.

## Implementation notes

The Day Zero implementation of this ADR is reflected in:

- `.env.example`
- `.gitignore`
- `.pre-commit-config.yaml`
- `scripts/verify-structure.ps1`
- `api/config/settings.py`
- `api/core/middleware.py`
- `Dockerfile`
- `docker-compose.yml`
- `README.md`
- `ai_governance/prompt_catalog.json`
- `ai_governance/evaluations/sample_eval.json`

## Compliance and review notes

This project is not a production AML, sanctions, or KYC system. This ADR defines engineering controls and development posture only. It does not claim regulatory sufficiency.

This ADR should be revisited when any of the following occur:

- authentication or authorization is introduced
- personal data ingestion is expanded
- external sanctions or watchlist data sources are integrated
- LLM-supported workflows move beyond scaffolding into active use
- cloud deployment replaces local-only development
