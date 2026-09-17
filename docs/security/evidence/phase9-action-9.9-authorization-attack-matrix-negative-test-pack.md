# Phase 9 Action 9.9 — Authorization Attack Matrix and Executable Negative-Test Pack

Status: **COMPLETE — TEST DESIGN AND EXECUTABLE PACK BUILT; RUNTIME EXECUTION DEFERRED TO ACTION 9.10**

## Objective

Convert the Phase 9 static authorization, tenant, agent/tool, workload-identity and secret-handling hypotheses into a bounded, reproducible negative-test suite with explicit actors, preconditions, expected outcomes, evidence requirements and stop conditions.

This action prepares the tests. It does **not** claim that the runtime properties have passed or failed.

## Safety contract

The executable runner is intentionally constrained to the authorized laboratory:

- loopback targets only: `localhost`, `127.0.0.1`, or `::1`;
- explicit `PHASE9_RUN=1` required before any HTTP request is sent;
- sequential execution only;
- maximum 50 cases per run;
- per-request timeout capped at 5 seconds;
- response body capped at 1 MiB;
- redirects are not followed;
- no credential values are printed;
- response bodies are not written to evidence; only status, length, SHA-256 and assertion results are retained;
- all users, tenants, documents, chats, files, agents, tools, credentials and tokens must be synthetic;
- any unexpected external destination, real credential, real customer data, or scope ambiguity is an immediate stop condition.

Executable runner:

`scripts/security/phase9_negative_authz_runner.py`

## Required synthetic principals

- `admin-alpha` — global administrative control user;
- `manager-a` — scoped manager for Group A only;
- `alice-alpha` — ordinary user in Tenant Alpha / Group A;
- `bob-alpha` — ordinary user outside Alice's ownership boundary;
- `carol-beta` — ordinary user in Tenant Beta when multi-tenant mode is available;
- `service-low` — low-privilege service-account API key;
- `service-rotated` — same service identity after API-key regeneration;
- under-scoped PAT for an otherwise privileged synthetic user;
- disabled/revoked synthetic identity where required.

## Decision rules

The runner emits one of four dispositions:

- **PASS** — observable result matches an explicit automatic assertion;
- **FAIL** — observable result contradicts the required security property;
- **REVIEW** — the request ran, but product policy, a paired positive control, mock-receiver evidence, DB evidence, or other non-HTTP evidence is required before classification;
- **SKIP** — required synthetic fixture or environment variable was not supplied.

A `404` denial is generally treated as **REVIEW**, not automatic PASS, unless a paired owner/control request proves the route/resource exists. This prevents invalid paths from producing false security passes.

## Attack matrix

| Test ID | Source | Actor | Target / transition | Expected property | Automated disposition |
|---|---|---|---|---|---|
| P9-ANON-01 | baseline | anonymous | `GET /manage/users` | protected route must reject unauthenticated request | PASS on 401/403 |
| P9-CTRL-01 | baseline control | global admin | `GET /manage/users` | known authorized route remains reachable | PASS on 200 |
| P9-H11-01 | H9-11 | `manager-a` | scoped `GET /manage/users` | unmanaged-group marker must not appear | PASS only when 200 + out-of-scope marker absent |
| P9-CHAT-01 | ownership control | Alice | Alice-owned chat read | ALLOW | PASS on configured success status |
| P9-CHAT-02 | horizontal authz | Bob | Alice-owned chat read | DENY | PASS on 401/403; 404 REVIEW |
| P9-ADMIN-01 | vertical authz | Bob | full-admin mutation | DENY | PASS on 401/403; 404 REVIEW |
| P9-PAT-01 | token scope | under-scoped PAT | operation outside PAT permission scope | DENY despite user privilege | PASS on 401/403 |
| P9-H12-01 | H9-12 | Bob | Alice `CHAT_IMAGE_GEN` file | DENY cross-user file retrieval | PASS on 401/403; 404 REVIEW; 200 FAIL |
| P9-H13-01 | H9-13 | untrusted caller | search ACL bypass provenance | caller must not cause `bypass_acl=True` | REVIEW: integration/source instrumentation required |
| P9-H14-01 | H9-14 | Bob | attach Alice's non-shared static-header custom action | DENY unauthorized attachment | PASS on 401/403; 404 REVIEW; success FAIL |
| P9-H14-02 | H9-14 | Bob | invoke foreign static-header action | Alice's stored synthetic credential must not reach receiver | REVIEW: local receiver evidence required |
| P9-H15-01 | H9-15 | Bob after revoke | create new chat with revoked agent | DENY | PASS on 401/403; 404 REVIEW |
| P9-H15-02 | H9-15 | Bob after revoke | continue pre-existing chat | revoked agent/tool capability must follow documented policy | REVIEW: policy + receiver/tool-list evidence required |
| P9-H16-01 | H9-16 | Bob | request-level `mcp_headers` | supplied headers must not exceed MCP server auth policy | REVIEW: local MCP receiver evidence required |
| P9-SA-01 | workload | unauthorized human | service-account API-key administration | DENY | PASS on 401/403 |
| P9-SA-02 | workload control | `service-low` | explicitly permitted endpoint | only group-derived privilege ALLOW | PASS on configured success status |
| P9-SA-03 | workload revocation | same key after group privilege removal | formerly permitted operation | DENY on next request | PASS on 401/403 |
| P9-SA-04 | workload rotation | old API key after regeneration | old credential invalid | DENY | PASS on 401/403 |
| P9-SA-05 | workload deletion | deleted API key | deleted credential invalid | DENY | PASS on 401/403 |
| P9-SA-06 | workload disable | key whose synthetic user is inactive | inactive workload principal rejected | DENY | PASS on 401/403 |
| P9-SA-07 | workload tenant | Tenant-A key in Tenant-B context | cross-tenant replay rejected | DENY | PASS on 401/403; 404 REVIEW |
| P9-H17-01 | H9-17 | service account | browser/mobile interactive session | must match documented machine-identity policy | REVIEW: product policy required |
| P9-H18-01 | H9-18 | local DB fixture | secret persistence with/without EE encryption key | actual at-rest confidentiality/integrity must match requirement | REVIEW: DB byte inspection required |
| P9-H18-02 | H9-18 | local DB fixture | synthetic ciphertext mutation | tampering behavior documented; AEAD requirement assessed | REVIEW: isolated DB test required |
| P9-H19-01 | H9-19 | local/mock OAuth login | login OAuth access/refresh token storage | storage treatment proven without exposing token | REVIEW: local DB inspection required |
| P9-H19-02 | H9-19 | local/mock OAuth login | logout/unlink/revocation lifecycle | stale token material must follow documented lifecycle | REVIEW |

## Runner environment contract

The runner uses full synthetic authorization-header values and/or cookie strings supplied only at runtime. No credentials are committed.

Common variables:

```text
PHASE9_RUN=1
PHASE9_BASE_URL=http://127.0.0.1:8080
PHASE9_TIMEOUT_SECONDS=5
PHASE9_RESULT_PATH=/tmp/phase9-negative-results.json

PHASE9_ADMIN_AUTH
PHASE9_ADMIN_COOKIE
PHASE9_SCOPED_MANAGER_AUTH
PHASE9_SCOPED_MANAGER_COOKIE
PHASE9_ALICE_AUTH
PHASE9_ALICE_COOKIE
PHASE9_BOB_AUTH
PHASE9_BOB_COOKIE
```

Case-specific fixture variables are intentionally required before higher-risk tests run. Examples:

```text
PHASE9_H11_IN_SCOPE_MARKER
PHASE9_H11_OUT_OF_SCOPE_MARKER
PHASE9_ALICE_CHAT_PATH
PHASE9_H12_FOREIGN_FILE_ID
PHASE9_H14_ATTACH_PATH
PHASE9_H14_ATTACH_BODY_JSON
PHASE9_H15_NEW_SESSION_PATH
PHASE9_H15_NEW_SESSION_BODY_JSON
PHASE9_H15_EXISTING_SESSION_PATH
PHASE9_H15_EXISTING_SESSION_BODY_JSON
PHASE9_H16_MESSAGE_PATH
PHASE9_H16_MESSAGE_BODY_JSON
PHASE9_ADMIN_MUTATION_PATH
PHASE9_ADMIN_MUTATION_METHOD
PHASE9_ADMIN_MUTATION_BODY_JSON
PHASE9_UNDERSCOPED_PAT_AUTH
PHASE9_PAT_PROTECTED_PATH
PHASE9_SERVICE_LOW_AUTH
PHASE9_SERVICE_ALLOWED_PATH
PHASE9_SERVICE_REVOKED_AUTH
PHASE9_SERVICE_REVOKED_PATH
PHASE9_SERVICE_OLD_AUTH
PHASE9_SERVICE_ROTATION_PATH
PHASE9_SERVICE_DELETED_AUTH
PHASE9_SERVICE_DELETED_PATH
PHASE9_SERVICE_INACTIVE_AUTH
PHASE9_SERVICE_INACTIVE_PATH
PHASE9_SERVICE_TENANT_A_AUTH
PHASE9_SERVICE_CROSS_TENANT_PATH
PHASE9_SERVICE_CROSS_TENANT_HEADERS_JSON
```

`*_AUTH` values are complete synthetic Authorization header values, for example `Bearer <synthetic-token>`. `*_COOKIE` values are complete synthetic Cookie header values. Neither is printed by the runner.

## H9-11 proof requirements

The scoped-user test is only automatically meaningful when both synthetic markers are supplied:

- `PHASE9_H11_IN_SCOPE_MARKER` — e.g. Alice's synthetic email;
- `PHASE9_H11_OUT_OF_SCOPE_MARKER` — e.g. Bob's synthetic email.

A PASS requires:

1. `manager-a` reaches `/manage/users` successfully;
2. the response contains the in-scope marker where policy expects it;
3. the response does **not** contain the out-of-scope marker.

If the out-of-scope marker appears, the test is a reproducible authorization failure candidate and must proceed to Action 9.11 for product-policy validation, root cause and remediation.

## H9-12 proof requirements

Use a file known to exist and owned/authorized to Alice. Establish the paired owner control first. Bob's retrieval must not succeed. A `404` alone is REVIEW until the owner control proves the same file route and identifier are valid.

## H9-14 / H9-16 mock-receiver rule

Custom-action and MCP tests must target only approved loopback mock receivers. The HTTP status returned by Onyx is insufficient to prove delegated-credential isolation. The evidence set must additionally record, with secret values redacted:

- whether the mock receiver was called;
- which synthetic principal initiated the call;
- whether a protected synthetic header arrived;
- whether managed credentials overrode caller-supplied headers as designed.

## H9-18 / H9-19 non-HTTP rule

Cryptographic/storage hypotheses are intentionally **not** forced into the HTTP runner. They require isolated local DB inspection using synthetic values. Action 9.10 may collect the evidence, but classification still waits for Action 9.11 and explicit security requirements.

## Evidence schema for Action 9.10

Every executed test must preserve:

- test ID and hypothesis ID;
- UTC timestamp;
- assessed branch and HEAD;
- synthetic actor role (never real identity data);
- request method and route with sensitive query/body material omitted or redacted;
- expected result;
- HTTP status when applicable;
- response length and SHA-256 rather than raw body;
- assertion results;
- mock-receiver / DB / audit evidence references when applicable;
- PASS / FAIL / REVIEW / SKIP disposition;
- interpretation and product-policy dependency;
- stop-condition events;
- root-cause link if promoted to a finding.

## Completion gate for Action 9.9

Action 9.9 is complete when:

- static hypotheses H9-11 through H9-19 are represented in the matrix;
- baseline horizontal, vertical, scoped, PAT and workload controls are represented;
- the executable runner exists and fails closed outside loopback;
- runtime credentials remain external to source control;
- false passes from `404`/missing fixtures are prevented;
- non-HTTP hypotheses are explicitly marked REVIEW rather than silently skipped as secure;
- Action 9.10 can execute the pack without redesigning the test model.

## Result

**PASS — authorization attack matrix and bounded executable negative-test pack produced. Runtime security effectiveness remains unproven until Action 9.10.**
