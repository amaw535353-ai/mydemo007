# Phase 4 Action 4.5 - Container Privilege, Filesystem & Isolation Evidence

## Provenance

- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `2243a7b871d60fa6f7ebc682aba092e8d671f951`

## Observation class

**STATIC SOURCE CANDIDATES ONLY. RUNTIME/DEPLOYMENT BEHAVIOR IS UNVERIFIED.**

## Review scope

Runtime privilege, root/non-root users, Linux capabilities, privilege escalation, host namespaces, host paths, writable filesystems, device access, seccomp/AppArmor/SELinux and resource isolation candidates.

## Static observations

- Candidate files: **40**
- Matching lines: **263**

## Representative candidate files

- `backend/ee/onyx/server/scim/api.py`
- `backend/onyx/connectors/capability_checks/models.py`
- `backend/onyx/connectors/source_operations.py`
- `backend/onyx/db/llm.py`
- `backend/onyx/db/persona.py`
- `backend/onyx/server/features/build/sandbox/docker/docker_sandbox_manager.py`
- `backend/onyx/server/features/build/sandbox/image/browser-cli.sh`
- `backend/onyx/server/features/build/sandbox/image/firewall-init.sh`
- `backend/onyx/server/features/build/sandbox/README.md`
- `backend/onyx/server/features/mcp/client.py`
- `backend/onyx/server/gateway/models.py`
- `backend/onyx/server/manage/llm/models.py`
- `backend/onyx/server/manage/models.py`
- `backend/tests/external_dependency_unit/redis/test_incognito_context.py`
- `backend/tests/integration/tests/craft/k8s/test_browser.py`
- `backend/tests/integration/tests/mcp/test_mcp_server_search.py`
- `backend/tests/integration/tests/reindex_port/test_reindex_port.py`
- `backend/tests/integration/tests/search/test_search_api.py`
- `backend/tests/unit/ee/onyx/server/gateway/fixtures/codex_responses_request.json`
- `backend/tests/unit/onyx/server/features/craft/sandbox/test_docker_manager_config.py`

## Security interpretation

The matches identify source/configuration review candidates only.

They do not prove:

- that a container is actually built or executed;
- that a workload is deployed;
- that Kubernetes or Docker is reachable;
- that privilege controls are effective at runtime;
- that images are trusted or vulnerability-free.

## Safety

- No container started.
- No image pulled.
- No image pushed.
- No Kubernetes cluster contacted.
- No deployment executed.
- No registry contacted.
- No cloud resource created.
- No secret value displayed.
- No billable resource used.

## Result

Action 4.5 static mapping result: **PASS**
