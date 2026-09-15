# Phase 4 Action 4.9 - SBOM, Signing & Provenance Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `8cabf210641f3c74736c4a199bb1cd6bf9c6abd8`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. EXECUTION AND ENFORCEMENT ARE UNVERIFIED.**

## Review scope

Software bills of materials, package inventories, artifact digests, signing, signature verification, attestations, build provenance and SLSA-related supply-chain evidence.

## Static observations

- Candidate files: **328**
- Matching lines: **10523**

## Representative candidate files

- `backend/AGENTS.md`
- `backend/alembic/versions/2020d417ec84_single_onyx_craft_migration.py`
- `backend/alembic/versions/34fe28843029_craft_artifact_index_and_receipts.py`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/auth/users.py`
- `backend/ee/onyx/background/celery/tasks/license_notifications/tasks.py`
- `backend/ee/onyx/background/celery/tasks/log_export/tasks.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/db/tenant_sso_domain.py`
- `backend/ee/onyx/secondary_llm_flows/query_expansion.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/api.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/license/api.py`
- `backend/ee/onyx/server/license/models.py`
- `backend/ee/onyx/server/log_export/storage.py`
- `backend/ee/onyx/server/scim/auth.py`
- `backend/ee/onyx/server/tenants/proxy.py`

## Security interpretation

These are review candidates only.

Static matches do not prove:

- that a CI/CD workflow actually executes;
- that a discovered credential is real;
- that a dependency is vulnerable;
- that dependency pinning is complete;
- that an SBOM is actually produced;
- that signatures or attestations are verified;
- that provenance is trustworthy;
- that build permissions are least-privileged.

## Safety

- No workflow triggered.
- No secret value printed.
- No credential used.
- No package installed.
- No dependency scanner executed.
- No artifact uploaded.
- No artifact signed.
- No registry contacted.
- No cloud resource used.
- No paid service used.

## Result

Action 4.9 static mapping result: **PASS**
