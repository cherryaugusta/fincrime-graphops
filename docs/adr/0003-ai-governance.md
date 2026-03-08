# ADR 0003: AI Governance Baseline for FinCrime GraphOps Day Zero

- Status: Accepted
- Date: 2026-03-08
- Deciders: Project Maintainer
- Technical Story: Establish a controlled governance baseline for present and future AI-assisted features in a sensitive financial-crime analysis domain

## Context

FinCrime GraphOps is a portfolio-grade demonstration project focused on sanctions, beneficial ownership exploration, graph-linked entities, and typed API engineering. The project is not a regulated AML, KYC, or sanctions decisioning platform, but it operates in a domain where misuse, overclaiming, hallucination, privacy mistakes, and automation bias can create serious harm.

Even at Day Zero, the repository includes AI governance scaffolding because:

- future features may use LLMs or other AI systems for analyst-support workflows
- the subject matter can involve personal data, organizational data, and sensitive investigative context
- outputs in this domain must not be treated as authoritative without review
- the project should demonstrate that governance is designed in from the start rather than bolted on later

The Day Zero codebase already includes:

- an `ai_governance` folder
- a prompt catalog artifact
- an evaluation artifact
- README disclosures stating that the system is educational and not for real-world decision making

The project therefore needs an architectural decision that defines how AI features are governed before those features expand.

## Decision

We will adopt an AI Governance baseline from Day Zero.

This means that any present or future AI-assisted capability in FinCrime GraphOps must be treated as a governed subsystem with explicit controls around purpose, inputs, outputs, review, evaluation, and disclosure.

The Day Zero governance baseline includes the following decisions.

### 1. AI features are analyst-support only

Any AI-assisted function in this repository must be framed as decision support, summarization, triage support, or explanatory assistance.

AI outputs must not be treated as final determinations of:

- sanctions matches
- beneficial ownership findings
- suspicious activity
- legal status
- compliance disposition
- escalation or filing decisions

The system must not present an AI output as an autonomous compliance decision.

### 2. Human review is mandatory for consequential use cases

If an AI-assisted feature touches identity resolution, sanctions screening, risk interpretation, escalation suggestion, or other consequential outputs, a human reviewer must validate the result before action is taken.

This is a core Day Zero principle and must remain visible in code, documentation, and prompt design.

### 3. Prompt assets must be cataloged

Prompts are treated as governed artifacts rather than hidden implementation details.

The repository will maintain a prompt catalog in:

- `ai_governance/prompt_catalog.json`

Each governed prompt should record, where applicable:

- identifier
- purpose
- category
- intended behavior
- input expectations
- output expectations
- constraints
- risk level
- whether PII may be involved
- whether human review is required
- lifecycle status

This makes AI behavior more reviewable, testable, and auditable.

### 4. Prompt behavior must be evaluated explicitly

AI-assisted behaviors must have evaluation artifacts rather than relying on intuition alone.

The repository will maintain evaluation examples in:

- `ai_governance/evaluations/`

These evaluations should include:

- the prompt or prompt identifier under test
- the test objective
- criteria for acceptable behavior
- sample inputs
- expected behaviors
- examples of passing and failing outputs
- summary judgement

This creates a baseline for future regression testing and governance review.

### 5. Data minimization and privacy protection are required

AI features in this project must follow a least-data principle.

This means:

- do not include secrets in prompts
- do not include unnecessary personal data in prompts
- redact or minimize sensitive data where feasible
- avoid retaining raw sensitive content unless there is a justified need
- avoid exposing internal credentials, tokens, connection strings, or private keys in model inputs or outputs

Where personal data is involved, processing must remain conservative and clearly bounded.

### 6. Hallucination risk must be handled explicitly

AI outputs must not invent facts, identities, relationships, legal conclusions, or investigative findings.

If evidence is missing, the system should say so plainly.

Prompt design and evaluations must reinforce these rules:

- distinguish observed facts from interpretation
- identify uncertainty clearly
- avoid overclaiming
- do not convert weak signals into definitive conclusions

### 7. Explanations must remain bounded and non-deceptive

If the system provides reasoning summaries, they must reflect the available evidence and not imply hidden certainty.

The project must avoid patterns such as:

- claiming confirmed matches without corroboration
- implying legal or regulatory authority
- presenting generated text as verified fact
- masking uncertainty behind confident language

### 8. Governance artifacts must be versioned with the repository

Prompt catalogs, evaluation artifacts, and AI governance ADRs are part of the repository baseline and should evolve under version control.

This supports:

- review in pull requests
- comparison across changes
- traceability of governance decisions
- demonstration of disciplined engineering practice

### 9. AI governance must be visible in repository documentation

The README and ADR set must disclose that:

- the repository is educational
- AI outputs are analyst-support only
- human review is required for consequential use cases
- evidence gaps must be acknowledged rather than inferred away

This helps reduce the risk of misuse or misunderstanding by future readers of the repository.

### 10. Higher-risk AI features require stronger controls before expansion

Day Zero establishes scaffolding, not production-grade governance.

Before the project expands into areas such as automated watchlist assistance, document extraction, entity matching, or case summarization, additional controls may be required, including:

- stronger evaluation coverage
- red-team tests
- access controls
- approval workflows
- logging and retention policies
- model/provider review
- legal and compliance review where appropriate

## Consequences

### Positive consequences

- AI-related risk is acknowledged early rather than deferred
- the repository demonstrates responsible engineering in a sensitive domain
- prompts become inspectable artifacts rather than opaque behavior
- evaluation discipline is encouraged before feature growth
- misuse risk is reduced through clear analyst-support boundaries
- future contributors have a governance baseline to follow

### Negative consequences

- initial setup includes additional documentation and artifacts
- governance maintenance adds process overhead
- some experimentation may feel slower because prompts and evaluations should be documented
- simple prototypes may require extra explanation to remain within governance boundaries

### Trade-offs accepted

- we accept governance overhead in exchange for safer and more credible AI experimentation
- we accept lightweight Day Zero artifacts now rather than pretending no governance is needed
- we accept that human review requirements reduce automation, because that is appropriate for this domain

## Alternatives considered

### 1. Add AI governance later when AI features become substantial

Rejected.

In a sensitive domain, delaying governance would normalize unstructured prompt usage and make later correction harder. Day Zero scaffolding creates better habits and clearer repository intent.

### 2. Treat prompts as ordinary code comments or internal implementation details

Rejected.

Prompts define system behavior and should therefore be reviewable, versioned, and evaluated as first-class artifacts.

### 3. Allow AI outputs to make operational recommendations without mandatory human review

Rejected.

The project domain is too sensitive for autonomous or quasi-autonomous decisioning. This would create unacceptable ambiguity around responsibility and reliability.

### 4. Avoid AI governance artifacts because the repository is only a demo

Rejected.

The project is specifically intended to demonstrate mature engineering practice. In this context, responsible governance is part of the demonstration.

## Implementation notes

The Day Zero implementation of this ADR is reflected in:

- `ai_governance/prompt_catalog.json`
- `ai_governance/evaluations/sample_eval.json`
- `docs/adr/0001-security-by-design.md`
- `README.md`

At Day Zero, these artifacts establish structure and expectations even if active AI features are still limited.

The prompt catalog records governed prompt definitions and constraints.

The evaluation artifact records sample acceptance criteria and pass/fail examples for a higher-risk compliance-assist prompt.

The README states that the repository is educational and must not be used to make real-world decisions about individuals or entities.

## Out of scope at Day Zero

This ADR does not yet define:

- a production model selection policy
- provider contracting requirements
- formal model risk management procedures
- full audit-log design for AI interactions
- data protection impact assessments
- role-based access control for AI features
- automatic policy enforcement in CI for all prompt changes

These may be introduced later if the project expands.

## Compliance and review notes

This project is not a production compliance system. This ADR defines governance posture for repository design and future feature development only. It does not claim legal, regulatory, or operational sufficiency.

This ADR should be revisited when any of the following occur:

- LLM calls are added to application runtime paths
- prompts begin processing real or realistic personal data
- external models or hosted AI providers are integrated
- AI outputs are stored, exported, or shown to end users
- automated case prioritization or matching features are introduced
- additional team members begin contributing prompt changes
