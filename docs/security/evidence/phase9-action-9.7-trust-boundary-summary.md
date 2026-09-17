# Phase 9 Action 9.7 — Trust Boundary Summary

- Service-account API-key management requires `MANAGE_SERVICE_ACCOUNT_API_KEYS` and is documented in source as admin-equivalent because the holder may assign any group, including Admin.
- API-key identities are synthetic `SERVICE_ACCOUNT` users, with permissions inherited through group membership.
- Multi-tenant API-key generation encodes the current tenant and tenant-aware SQL sessions select the tenant schema using `schema_translate_map`.
- API-key authentication resolves back to a concrete user principal.
- Service-account key update/rotation recomputes authorization state; deletion removes the key and associated synthetic user.
- `SERVICE_ACCOUNT` is classified as web-login capable, creating H9-17 for policy/runtime verification.
- No application-level SPIFFE/SPIRE or workload mTLS mechanism was established in the source trace; infrastructure controls remain outside this action's evidence and must be verified separately.

No vulnerability is confirmed by this static trace.
