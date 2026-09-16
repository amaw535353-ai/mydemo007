# Phase 8 Final Closure — Onyx Web, API and Business-Logic Security

## Status

**COMPLETE**

## Closure timestamp

2026-09-16T22:18:12Z

## Scope

Phase 8 converted the Phase 7 web, API and business-logic threat hypotheses
into static analysis, executable fixtures and authorized runtime verification
against the synthetic Onyx laboratory.

## Major outcomes

### Static security work

Completed:

- API route reconnaissance;
- high-value endpoint selection;
- router-composition analysis;
- authentication and permission dependency tracing;
- ownership and tenant-control tracing;
- object-authorization surface analysis;
- privileged-operation surface analysis;
- executable authorization fixtures;
- explicit ALLOW/DENY expectations.

### Runtime security work

Authorized synthetic runtime testing was subsequently established.

Runtime testing verified:

- authenticated low-privilege controls;
- owner-access positive controls;
- foreign-object access denial;
- request-parameter manipulation cases;
- API health after security changes;
- regression behavior after remediation.

## TC8-007 lifecycle

### Discovery

A request-bindable `tenant_id` parameter reached the asynchronous database
session dependency.

### Confirmed root cause

`tenant_id` could reach SQLAlchemy:

```python
schema_translate_map = {None: tenant_id}
```

Observed behavior included:

- request-controlled schema selection;
- HTTP 500 for `tenant_id=default`;
- SQL/database implementation-detail disclosure.

Unauthorized data access was **not** demonstrated.

Authorization bypass was **not** demonstrated.

### Remediation

The database interface was separated into:

- zero-argument request-facing `get_async_session()`;
- explicit internal `get_async_session_context_manager(tenant_id=None)`;
- internal tenant-specific `_get_async_session_for_tenant(...)`.

### Regression verification

Runtime verification demonstrated:

| Security property | Result |
|---|---|
| Bob legitimate owner access | PASS / HTTP 200 |
| Bob owner + `tenant_id=default` | PASS / HTTP 200 |
| Bob → Alice foreign access | DENIED / HTTP 403 |
| `user_id=Alice` manipulation | DENIED / HTTP 403 |
| `tenant_id=public` manipulation | DENIED / HTTP 403 |
| `tenant_id=default` manipulation | DENIED / HTTP 403 |
| combined user + tenant manipulation | DENIED / HTTP 403 |
| former HTTP 500 | NOT REPRODUCED |
| client SQL/schema disclosure | ABSENT |
| server default-schema error | ABSENT |
| API health after remediation | PASS |

## Evidence chain

- Root cause:
  `docs/security/evidence/phase8-action-8.27-tc8-007-root-cause.md`
- Remediation:
  `docs/security/evidence/phase8-action-8.28-tc8-007-remediation.md`
- Runtime regression:
  `docs/security/evidence/phase8-action-8.29-tc8-007-runtime-regression.md`

Relevant commits:

- root-cause record:
  `2130e1d5d6b0686f54f8f145eb7bc68dc576f651`
- remediation:
  `4ebd7a06be5fe0238f264d298ad19b342116d357`
- runtime verification:
  `07ae7c1695350f795116227aa1465311ebc36ba6`

## Residual risk / limitation

Runtime verification was performed in the authorized Phase 8 laboratory by
overlaying the committed patched source into the existing API container and
restarting that container.

Therefore Phase 8 demonstrates the application-level security property in the
controlled laboratory.

It does **not** independently prove that every future production image,
deployment pipeline or downstream release artifact contains the remediation.

Release/CI verification remains a deployment assurance responsibility.

## Security conclusion

Within the authorized Phase 8 laboratory scope:

**TC8-007 is CLOSED — FIX VERIFIED.**

No unauthorized cross-user data access was demonstrated during TC8-007.

The confirmed defect was request-controlled tenant/schema selection combined
with robustness failure and internal-error disclosure.

The demonstrated defect was remediated and its original runtime behavior was
not reproducible after the patch.

## Phase decision

**PHASE 8 COMPLETE**

Next phase:

**Phase 9 — Onyx Identity, Authorization and Tenant Isolation**
