# Phase 9 Action 9.10 — Runtime Slice 1

## Result

**PASS**

Verified runtime properties:

- anonymous protected-route denial
- global-admin positive control
- chat owner positive control
- cross-user chat denial
- ordinary-user full-admin mutation denial

## Harness correction

An earlier runtime attempt used the incomplete path:

```text
/get-chat-session/{session_id}
```

Source verification established the actual composed route:

```text
/chat/get-chat-session/{session_id}
```

The earlier owner HTTP 404 was therefore a test-fixture defect,
not a demonstrated authorization defect.

## Runtime result

# Phase 9 Action 9.10 — Runtime Verification Result

Status: **INCOMPLETE — REQUIRED SYNTHETIC FIXTURES WERE SKIPPED**

## Immutable execution context

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- HEAD: `70a454dd53273f024319526db62ff047b8cf295a`
- UTC timestamp: `2026-09-18T09:54:55Z`
- Base URL: `http://127.0.0.1:8080`
- Runner SHA-256: `7907413b9fc99b7303e8e78905c84eb22bf8b0792c352d5a2acafb8bcc3b0cf2`
- Execute flag: `True`
- Timeout: `5.0` seconds

## Disposition counts

- PASS: **5**
- FAIL: **0**
- REVIEW: **6**
- SKIP: **15**

## Case results

| Case | Source | Disposition | Method | Path | HTTP | Assertions | Note |
|---|---|---|---|---|---:|---|---|
| P9-ANON-01 | baseline | PASS | GET | /manage/users | 403 | deny_status=True |  |
| P9-CTRL-01 | baseline-control | PASS | GET | /manage/users | 200 | success_status=True |  |
| P9-H11-01 | H9-11 | SKIP | GET | /manage/users |  |  | missing synthetic fixture(s): PHASE9_H11_IN_SCOPE_MARKER, PHASE9_H11_OUT_OF_SCOPE_MARKER, PHASE9_SCOPED_MANAGER_AUTH or PHASE9_SCOPED_MANAGER_COOKIE |
| P9-CHAT-01 | ownership-control | PASS | GET | /chat/get-chat-session/72a9a3cb-8d63-45c6-ae84-6d75f18df9b8 | 200 | success_status=True |  |
| P9-CHAT-02 | horizontal-authz | PASS | GET | /chat/get-chat-session/72a9a3cb-8d63-45c6-ae84-6d75f18df9b8 | 403 | deny_status=True |  |
| P9-ADMIN-01 | vertical-authz | PASS | PATCH | /manage/admin/users/admin-access | 403 | deny_status=True |  |
| P9-PAT-01 | token-scope | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_PAT_PROTECTED_PATH, PHASE9_UNDERSCOPED_PAT_AUTH or PHASE9_UNDERSCOPED_PAT_COOKIE |
| P9-H12-01 | H9-12 | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_H12_FOREIGN_FILE_ID |
| P9-H14-01 | H9-14 | SKIP | PATCH |  |  |  | missing synthetic fixture(s): PHASE9_H14_ATTACH_BODY_JSON, PHASE9_H14_ATTACH_PATH |
| P9-H14-02 | H9-14 | SKIP | POST |  |  |  | missing synthetic fixture(s): PHASE9_H14_INVOKE_BODY_JSON, PHASE9_H14_INVOKE_PATH |
| P9-H15-01 | H9-15 | SKIP | POST |  |  |  | missing synthetic fixture(s): PHASE9_H15_NEW_SESSION_BODY_JSON, PHASE9_H15_NEW_SESSION_PATH |
| P9-H15-02 | H9-15 | SKIP | POST |  |  |  | missing synthetic fixture(s): PHASE9_H15_EXISTING_SESSION_BODY_JSON, PHASE9_H15_EXISTING_SESSION_PATH |
| P9-H16-01 | H9-16 | SKIP | POST |  |  |  | missing synthetic fixture(s): PHASE9_H16_MESSAGE_BODY_JSON, PHASE9_H16_MESSAGE_PATH |
| P9-SA-01 | workload-authz | SKIP | POST |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_ADMIN_BODY_JSON, PHASE9_SERVICE_ADMIN_PATH |
| P9-SA-02 | workload-control | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_ALLOWED_PATH, PHASE9_SERVICE_LOW_AUTH or PHASE9_SERVICE_LOW_COOKIE |
| P9-SA-03 | workload-revocation | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_REVOKED_AUTH or PHASE9_SERVICE_REVOKED_COOKIE, PHASE9_SERVICE_REVOKED_PATH |
| P9-SA-04 | workload-rotation | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_OLD_AUTH or PHASE9_SERVICE_OLD_COOKIE, PHASE9_SERVICE_ROTATION_PATH |
| P9-SA-05 | workload-deletion | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_DELETED_AUTH or PHASE9_SERVICE_DELETED_COOKIE, PHASE9_SERVICE_DELETED_PATH |
| P9-SA-06 | workload-disable | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_INACTIVE_AUTH or PHASE9_SERVICE_INACTIVE_COOKIE, PHASE9_SERVICE_INACTIVE_PATH |
| P9-SA-07 | workload-tenant | SKIP | GET |  |  |  | missing synthetic fixture(s): PHASE9_SERVICE_CROSS_TENANT_HEADERS_JSON, PHASE9_SERVICE_CROSS_TENANT_PATH, PHASE9_SERVICE_TENANT_A_AUTH or PHASE9_SERVICE_TENANT_A_COOKIE |
| P9-H13-01 | H9-13 | REVIEW |  |  |  |  | instrumented integration/source-provenance evidence required |
| P9-H17-01 | H9-17 | REVIEW |  |  |  |  | product policy plus synthetic login/runtime evidence required |
| P9-H18-01 | H9-18 | REVIEW |  |  |  |  | isolated local DB byte inspection required |
| P9-H18-02 | H9-18 | REVIEW |  |  |  |  | isolated local DB mutation test required |
| P9-H19-01 | H9-19 | REVIEW |  |  |  |  | local/mock OAuth and DB inspection required |
| P9-H19-02 | H9-19 | REVIEW |  |  |  |  | lifecycle and DB evidence required |

## Evidence-integrity properties

- Raw HTTP bodies are not included; the runner records response length and SHA-256 only.
- Credential environment values are not included in this summary.
- A 404 denial is not automatically treated as proof of authorization enforcement.
- REVIEW cases remain unresolved until required policy, mock-receiver, DB, audit, or lifecycle evidence is attached.

## Action 9.11 promotion queue

- `P9-H13-01` / `H9-13` — REVIEW: instrumented integration/source-provenance evidence required
- `P9-H17-01` / `H9-17` — REVIEW: product policy plus synthetic login/runtime evidence required
- `P9-H18-01` / `H9-18` — REVIEW: isolated local DB byte inspection required
- `P9-H18-02` / `H9-18` — REVIEW: isolated local DB mutation test required
- `P9-H19-01` / `H9-19` — REVIEW: local/mock OAuth and DB inspection required
- `P9-H19-02` / `H9-19` — REVIEW: lifecycle and DB evidence required

## Completion decision

Action 9.10 must not be marked COMPLETE from this artifact unless the run used the authorized synthetic lab, required fixtures were executed, and every REVIEW item has supporting evidence or an explicit documented non-applicability disposition.

A FAIL is a reproducible candidate security failure, not automatically a final vulnerability. Action 9.11 must validate product intent, impact, root cause, remediation, and retest.

## Independent checks

- Alice own-chat direct control: HTTP 200.
- Bob remained non-admin after the denied mutation.
- Original synthetic password hashes were restored.
- Raw passwords and session cookies are excluded from repository evidence.
- Runtime requests were loopback-only.
- Synthetic users and resources only.

## Slice completion

- P9-ANON-01: PASS
- P9-CTRL-01: PASS
- P9-CHAT-01: PASS
- P9-CHAT-02: PASS
- P9-ADMIN-01: PASS

Action 9.10 remains IN PROGRESS because other runtime and
manual-review cases remain unresolved.
