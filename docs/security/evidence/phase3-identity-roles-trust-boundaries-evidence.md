# Phase 3 Action 3.10 - Identity, Roles, Permissions & Trust Boundaries Evidence

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME BEHAVIOR IS UNVERIFIED.**

- Branch: `security/phase-3-foundations`
- HEAD: `6fc0036337451916c5471fb390b54f0645f5e08c`
- Candidate files: **3198**
- Matching lines: **40168**

## Review scope

Human/service identities, principals, roles, permissions, tenants, trust boundaries, delegation, impersonation and external identity providers.

## Representative candidates

- `AGENTS.md`
- `backend/AGENTS.md`
- `backend/alembic/env.py`
- `backend/alembic.ini`
- `backend/alembic/README.md`
- `backend/alembic/run_multitenant_migrations.py`
- `backend/alembic_tenants/versions/14a83a331951_create_usertenantmapping_table.py`
- `backend/alembic_tenants/versions/34e3630c7f32_lowercase_multi_tenant_user_auth.py`
- `backend/alembic_tenants/versions/3b45e0018bf1_add_new_available_tenant_table.py`
- `backend/alembic_tenants/versions/3b9f09038764_add_read_only_kg_user.py`
- `backend/alembic_tenants/versions/8f3d2c7b91ae_add_user_tenant_mapping_oauth_account.py`
- `backend/alembic_tenants/versions/a4f6ee863c47_mapping_for_anonymous_user_path.py`
- `backend/alembic_tenants/versions/a754e4f72e60_add_tenant_sso_domain_routing.py`
- `backend/alembic_tenants/versions/ac842f85f932_new_column_user_tenant_mapping.py`
- `backend/alembic_tenants/versions/b1c4e9d72f38_add_tenant_shard_map.py`
- `backend/alembic_tenants/versions/d4e7a92c1b38_add_tenant_invite_counter.py`
- `backend/alembic/versions/03d085c5c38d_backfill_account_type.py`
- `backend/alembic/versions/03d710ccf29c_add_permission_sync_attempt_tables.py`
- `backend/alembic/versions/0816326d83aa_add_federated_connector_tables.py`
- `backend/alembic/versions/0cd424f32b1d_user_file_data_preparation_and_backfill.py`

## Interpretation

Static candidates do not prove runtime security enforcement.

## Safety

- No credential submitted.
- No token replayed.
- No authorization bypass attempted.
- No role/session/cookie modified.
- No private-key contents displayed.
- No external service contacted.
