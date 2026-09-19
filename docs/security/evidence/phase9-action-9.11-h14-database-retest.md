# Phase 9 Action 9.11 — H9-14 Database Retest

## Result

**PASS — 5/5 CASES**

## Runtime context

- Date: 2026-09-19
- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Runtime HEAD: `7496d92599f26d2e2050643832ef091aa6025493`
- Target: authorized GitHub Codespaces laboratory
- Database: local PostgreSQL container
- Data and identities: synthetic only
- HTTP requests: 0
- External service calls during the test: 0
- Duration: 2.97 seconds
- Worktree after execution: clean

## Command

```bash
timeout 60s .venv/bin/pytest -q \
  backend/tests/external_dependency_unit/db/test_custom_action_persona_guard.py
```

## Observed output

```text
.....                                                                    [100%]
5 passed in 2.97s
```

## Verified cases

| Case | Result |
| --- | --- |
| Unrelated user attaches another creator's custom action | DENY |
| Creator attaches the creator's custom action | ALLOW |
| Actions administrator attaches another creator's action | ALLOW |
| Existing foreign action survives an ordinary agent update | ALLOW and preserve |
| Removed foreign action is attached again | DENY |

## Persistence control

Each case ran inside an outer database transaction. The local test fixture rolled back
that transaction at teardown. The test did not invoke any action or transmit any stored
header.

## Disposition

The database-layer remediation is verified.

The rebuilt-container negative retest and API-level HTTP 403 verification remain pending.
Credential transmission remains unexecuted and unconfirmed.
