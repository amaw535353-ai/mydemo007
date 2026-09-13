# Phase 0: Scope and Rules of Engagement

## Document control

- Status: Draft for Ahmed's review
- Repository owner: `amaw535353-ai`
- Authorized repository: `amaw535353-ai/mydemo007`
- Working branch: `security/phase-0-scope`
- Baseline branch: `main`
- Baseline commit: `10835c149c730c4de4dbf379483bc00ec3ff914a`
- Effective date: 2026-09-13
- Expiry: When Ahmed revokes or replaces this authorization

## Purpose

Use this repository as a controlled learning lab for AI application and product security.

The work will build practical skill in architecture review, threat modeling, testing, mitigation, and verification.

## Authorized people and roles

- Ahmed owns the lab and makes scope, safety, risk, and approval decisions.
- ChatGPT may inspect code, explain risks, draft artifacts, propose tests, and prepare reviewed changes.
- Ahmed reviews and approves security conclusions, test expansion, destructive actions, and final publication.
- Repository changes use a separate branch before merge into `main`.

## Authorized targets

- Source code in `amaw535353-ai/mydemo007`.
- A local clone of the authorized repository.
- A local Onyx instance built from the recorded baseline.
- A local PostgreSQL database in an approved Docker container.
- Local mock LLM and MCP services.
- Local endpoints and ports created for this lab.
- Synthetic test accounts, credentials, documents, logs, and tenant data.

## Required configuration record

Record these values before runtime testing:

- Onyx edition: Not confirmed.
- Deployment mode: Not confirmed.
- Application version: Not confirmed.
- Source commit: `10835c149c730c4de4dbf379483bc00ec3ff914a`.
- Local operating system: Not confirmed.
- Local container configuration: Not confirmed.

Do not start runtime security tests until the missing values are recorded.

## Explicit exclusions

This authorization does not include:

- `onyx-dot-app/onyx` or any other repository not owned or separately authorized by Ahmed.
- Public Onyx websites, cloud services, demonstrations, or third-party deployments.
- Public IP addresses or systems outside the local lab.
- Real external MCP servers, APIs, connectors, identity providers, or data sources.
- `api.openai.com` or a local proxy that forwards requests to an external service.
- Real Google Drive accounts, employee accounts, customer data, production backups, or production logs.
- Real passwords, tokens, keys, certificates, sessions, or other production credentials.
- Social engineering against real people.
- Public disclosure before responsible private reporting.

## Cost and network rules

- Use no paid API, billable cloud resource, paid SaaS, or credit-card trial.
- Disable external APIs and connectors.
- Permit outbound traffic only to an explicitly approved local lab service.
- Stop before any action that could reach a real external service or create a charge.

## Test limits

Allowed actions include:

- Read-only source and configuration inspection.
- Local port inspection against the approved lab.
- Static analysis of the authorized repository.
- Synthetic authentication and authorization tests.
- Controlled tests with a maximum of 10 concurrent requests.
- Controlled load tests lasting no more than 60 seconds.
- Test files no larger than 1 MB unless Ahmed approves a new limit.
- Controlled teardown of temporary lab resources.

Prohibited actions include:

- Scanning public targets.
- Testing another organization's deployment.
- Phishing or deceiving real people.
- Unbounded recursion, concurrency, runtime, token use, storage use, or traffic.
- Deliberate disk, memory, network, or service exhaustion.
- Persistence, backdoors, malware deployment, or destructive payloads.

## Stop conditions

Stop work immediately if:

- An action leaves the approved local boundary.
- A request attempts to use an external API or connector.
- Real customer data or personal data appears.
- A real production credential appears.
- A cost could be created.
- A resource, time, token, or concurrency limit is reached.
- The next action's authorization is unclear.
- Unexpected behavior could damage data or reduce service availability.

Preserve evidence and ask Ahmed before continuing after a stop condition.

## Evidence requirements

For each practical action, record:

- Date and time.
- Exact repository, branch, commit, file, service, endpoint, and environment.
- Command and argument breakdown.
- Expected result.
- Actual result.
- Relevant logs, screenshots, diffs, and test output.
- Synthetic tenant and user identifiers.
- Security interpretation.
- Completion decision and reviewer.

Never store real secrets or personal data in evidence.

## Change and recovery rules

- Make code and documentation changes on a dedicated branch.
- Review each diff before merge.
- Use small, reversible commits.
- Restore a known-good configuration after a failed change.
- Restore an approved local database snapshot when required.
- Remove temporary containers, synthetic credentials, datasets, and test artifacts after use.
- Do not rewrite or delete shared Git history.

## Responsible disclosure

- Reproduce findings only with synthetic data in the authorized lab.
- Preserve enough evidence for independent verification.
- Report possible upstream vulnerabilities through the upstream private reporting channel.
- Do not create a public issue, pull request, or discussion for an undisclosed vulnerability.
- Give maintainers reasonable time to investigate and fix the issue.
- Coordinate any later public disclosure with the maintainers.

## Practical-step format

Every practical step must include:

1. What
2. Where
3. Why
4. When
5. How
6. Who

Each step should also state its prerequisites, safety boundary, prediction, evidence, and completion criteria.

## Approval gate

This document permits documentation and read-only repository inspection.

Ahmed must approve this draft before active runtime security testing begins.
