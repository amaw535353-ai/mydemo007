# Phase 9 H9-17 — Service-account Interactive-Session Policy Question

Status: **OPEN POLICY/RUNTIME QUESTION**

Static source establishes that:

- API-key service identities are represented as `SERVICE_ACCOUNT` users;
- service-account provisioning creates a random password hash that is not exposed as a human login credential;
- `AccountType.is_web_login()` returns false only for `BOT` and `EXT_PERM_USER`, so `SERVICE_ACCOUNT` is web-login eligible.

Static source does **not** establish whether the product intentionally supports interactive service-account sessions, nor whether an operator can obtain usable interactive credentials through an authorized management path.

Before H9-17 can be classified, obtain or establish the intended service-account policy and execute the bounded SA-08 test from `phase9-action-9.7-runtime-test-pack.md`.

A finding requires reproducible unauthorized or policy-violating impact, not merely the presence of a web-login-capable enum value.
