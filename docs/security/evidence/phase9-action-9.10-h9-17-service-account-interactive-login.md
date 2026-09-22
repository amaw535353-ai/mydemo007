# Phase 9 — Action 9.10 — H9-17 Service-Account Interactive Login

## Finding

`SERVICE_ACCOUNT` identities were classified as supporting interactive web login.

The pre-remediation runtime proof confirmed that a synthetic service account could authenticate through the normal password login flow, receive an authentication cookie, and establish an authenticated `/me` session.

Pre-remediation result:

- `SERVICE_ACCOUNT_IS_WEB_LOGIN=TRUE`
- interactive login HTTP: **204**
- authentication cookie: **present**
- authenticated `/me`: **200**
- session identity matched the synthetic service account
- session account type: `SERVICE_ACCOUNT`
- classification: **CONFIRMED**

## Root cause

`AccountType.is_web_login()` excluded `BOT` and `EXT_PERM_USER`, but did not exclude `SERVICE_ACCOUNT`.

Service-account creation stores a password hash, so the regular password authenticator treated service accounts as valid interactive identities.

## Remediation

`AccountType.SERVICE_ACCOUNT` is now explicitly excluded from `is_web_login()`.

This preserves interactive login for `STANDARD` users while retaining the existing non-interactive behavior for `BOT` and `EXT_PERM_USER`.

## Regression coverage

A focused regression test verifies:

- `STANDARD.is_web_login()` remains `True`;
- `SERVICE_ACCOUNT.is_web_login()` is `False`;
- `BOT.is_web_login()` remains `False`;
- `EXT_PERM_USER.is_web_login()` remains `False`.

Focused unit regression: **PASS — 3 tests**.

## Patched runtime verification

- `SERVICE_ACCOUNT_IS_WEB_LOGIN=FALSE`
- patched policy gate: **PASS**
- interactive login HTTP: **403**
- authentication cookie: **NO**
- `H9_17=SERVICE_ACCOUNT_INTERACTIVE_LOGIN_BLOCKED`
- synthetic service account removed after test: **YES**
- external network requests: **0**
- persistent database fixtures: **0**

## Classification

**H9-17 — PASS / REMEDIATED**

Service accounts remain machine identities and can no longer establish normal interactive password sessions.

## Evidence identities

- Runtime evidence SHA-256: `7a76b36d7e5a13477e3d3cf4295033861dbd39859d82c59869625895460dba55`
- Patched enum SHA-256: `8e514547fdffdb0872c5844ee5b20146b2adf2b9b417ac84a945533beabab40e`
- Regression-test SHA-256: `17421dd6fd17c42af15e48e65925f1dac6f67616488a8eb6a80f07618d5f2318`
