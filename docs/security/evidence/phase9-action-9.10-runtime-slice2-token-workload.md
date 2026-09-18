# Phase 9 Action 9.10 — Runtime Slice 2: Token and Workload Identity

## Overall disposition

**PARTIALLY VERIFIED / ENVIRONMENT-BLOCKED**

The scoped personal-access-token case was verified at runtime.

The service-account lifecycle cases cannot be executed in the active deployment
because the service-account API is protected by a Business-plan entitlement
gate.

This is an environment limitation, not an authorization PASS or FAIL.

## Assessed source state

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Source HEAD: `e116b71a61664af89e861d26dbe48db37016e010`
- Runtime: local loopback-only authorized laboratory
- Synthetic identities only
- Multi-tenant mode: false
- No paid service or license was enabled for testing

## P9-PAT-01 — PASS

Runtime verification:

- A synthetic administrator successfully created a PAT scoped only to `read:chat`.
- The PAT reached `GET /chat/get-user-chat-sessions` with HTTP 200.
- The same PAT attempted `GET /manage/users`.
- The request was denied with HTTP 403.
- The PAT was revoked.
- The revoked PAT was denied with HTTP 403.
- Active Phase 9 synthetic PAT count returned to zero.
- Repository remained clean.

Conclusion:

The active runtime enforced the PAT permission ceiling:
`read:chat` did not expand into `read:users`.

## Service-account entitlement gate

A runtime entitlement-control probe established:

- Synthetic administrator `GET /manage/users`: HTTP 200.
- Synthetic administrator `GET /admin/api-key`: HTTP 402.
- Error code: `FEATURE_NOT_AVAILABLE`.
- Runtime detail: service-account functionality requires the Business plan.

Because even the authorized synthetic administrator is stopped at the product
entitlement layer, the service-account authorization/lifecycle surface cannot
be exercised in this deployment.

No attempt was made to disable, bypass, patch, forge, or circumvent the
product's licensing controls.

## Service-account case dispositions

| Test | Disposition | Reason |
|---|---|---|
| P9-SA-01 | BLOCKED_BY_ENTITLEMENT | Bob's API-key creation request returned HTTP 402 before an authorization decision could be demonstrated |
| P9-SA-02 | BLOCKED_BY_ENTITLEMENT | Low-privilege service account cannot be created in this deployment |
| P9-SA-03 | BLOCKED_BY_ENTITLEMENT | Service-account privilege-removal lifecycle cannot be instantiated |
| P9-SA-04 | BLOCKED_BY_ENTITLEMENT | API-key regeneration lifecycle cannot be instantiated |
| P9-SA-05 | BLOCKED_BY_ENTITLEMENT | API-key deletion lifecycle cannot be instantiated |
| P9-SA-06 | BLOCKED_BY_ENTITLEMENT | Inactive service-account credential fixture cannot be instantiated |
| P9-SA-07 | NOT_APPLICABLE | Active deployment is single-tenant; Tenant-A to Tenant-B credential replay has no second tenant context |

## Deferred execution requirement

P9-SA-01 through P9-SA-06 remain reusable runtime tests.

They should be executed later only in an authorized environment where
service-account functionality is legitimately enabled.

No security conclusion about those runtime controls is claimed here.

## Security hygiene

- Synthetic identities only.
- Original temporary password hashes restored.
- Temporary PAT revoked.
- Active Phase 9 test PAT count returned to zero.
- No production data or credentials used.
- No external service contacted.
- No paid resource enabled.
- No product entitlement bypass attempted.
- No raw passwords, session cookies, PATs, or API keys stored in this evidence.

## Progress accounting

Two progress measurements are deliberately maintained.

### Runtime-verified cases

- Slice 1 verified: 5 cases.
- P9-PAT-01 verified: 1 case.
- Runtime-verified total: **6 / 26 = 23.1%**.

### Cases with documented disposition

- Runtime PASS: 6.
- BLOCKED_BY_ENTITLEMENT: 6.
- NOT_APPLICABLE: 1.
- Total dispositioned: **13 / 26 = 50.0%**.

Blocked cases are not counted as runtime PASS.

Phase 9 completed actions remain **9 / 14 = 64.3%**.

Action 9.10 remains **IN PROGRESS**.
