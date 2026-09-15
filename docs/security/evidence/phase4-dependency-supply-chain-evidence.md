# Phase 4 Action 4.8 - Dependency & Software Supply-Chain Foundations Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `a220664c2883f9cb0c82dff9d544f3fb33b427fa`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. EXECUTION AND ENFORCEMENT ARE UNVERIFIED.**

## Review scope

Package manifests, lockfiles, version constraints, hashes, package installation, dependency update automation, source dependencies and third-party software trust.

## Static observations

- Candidate files: **535**
- Matching lines: **11220**

## Representative candidate files

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/versions/2e0b2b146de1_backfill_notion_external_app.py`
- `backend/alembic/versions/3a78dba1080a_user_file_legacy_data_cleanup.py`
- `backend/alembic/versions/7cc3fcc116c1_user_file_uuid_primary_key_swap.py`
- `backend/alembic/versions/7f5b159041be_skill_built_in_id_discriminator.py`
- `backend/alembic/versions/989bc57562e4_seed_browser_built_in_skill.py`
- `backend/alembic/versions/b4950827c0dd_encrypt_external_app_credentials.py`
- `backend/alembic/versions/b6d184cfdaf3_skills.py`
- `backend/alembic/versions/c5d9662b3c50_seed_craft_documentation_built_in_skill.py`
- `backend/alembic/versions/ea9771dd828c_associate_external_apps_with_skills.py`
- `backend/alembic/versions/f3a9c1d4b7e2_provision_built_in_external_apps.py`
- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `backend/ee/onyx/auth/sso_domain_verification.py`
- `backend/ee/onyx/db/license.py`
- `backend/ee/onyx/server/gateway/anthropic_passthrough.py`
- `backend/ee/onyx/server/gateway/openai_passthrough.py`
- `backend/ee/onyx/server/scim/auth.py`
- `backend/ee/onyx/utils/license.py`

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

Action 4.8 static mapping result: **PASS**
