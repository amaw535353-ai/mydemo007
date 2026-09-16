# Phase 8 Action 8.28 — TC8-007 Trust-Boundary Remediation

## Status

**PATCHED — RUNTIME HTTP REGRESSION PENDING**

## Metadata

- UTC: 2026-09-16T22:07:12Z
- Parent/root-cause commit: `2130e1d5d6b0686f54f8f145eb7bc68dc576f651`
- Branch: `security/phase-8-web-api-business-logic`
- Validation runtime: `onyx-api_server-1`
- Validation Python: Python 3.13.15

## Root cause

The FastAPI asynchronous database dependency exposed the request-bindable
parameter:

```python
tenant_id: str | None = None
```

The value could reach SQLAlchemy schema translation and therefore influence
database schema selection.

## Remediation

The interface is separated into distinct trust levels.

### Request-facing dependency

`get_async_session()`

- exposes zero request-bindable parameters;
- cannot receive `tenant_id` from FastAPI query binding;
- obtains tenant context through trusted server-side state.

### Explicit internal interface

`get_async_session_context_manager(tenant_id=None)`

remains available for controlled internal callers that intentionally require
tenant-specific database access.

### Internal implementation

`_get_async_session_for_tenant(tenant_id=None)`

contains tenant-specific engine and schema-selection logic.

## Verification completed

- Branch gate: PASS
- Parent commit gate: PASS
- Clean working-tree gate: PASS
- Existing direct-caller inventory: PASS
- Candidate modified only under container `/tmp`: PASS
- AST dependency-boundary validation: PASS
- Python compilation: PASS
- Three self-contained regression tests using Python `unittest`: PASS
- Validated-candidate SHA-256 equality after promotion: PASS
- Git diff validation: PASS

## Local test-environment note

The running API image does not include pytest.

No packages were installed.

The regression test therefore uses Python's standard-library
`unittest`, while remaining compatible with pytest-based CI discovery.

## Runtime verification still required

TC8-007 is not closed yet.

Action 8.29 must restart/rebuild the API from the patched source and prove:

1. `tenant_id=default` can no longer cause request-controlled schema
   selection.
2. The previously observed HTTP 500 no longer occurs.
3. Internal SQL/schema details are not disclosed.
4. Foreign chat-session access remains denied.
5. Normal legitimate behavior remains functional.

## Integrity

- Patched source SHA-256:
  `2323f63a524f2da64108f2024097cbb4bafbe2d6c9ae0466ef8017c42599bcc9`
- Regression-test SHA-256:
  `84dc9eab42d4cee20de778b77ec7ed14ce80eb7eca094884bc8001631d15d78d`
- Regression output:
  `/tmp/phase8-action-8.28/unittest.txt`
- Patch diff:
  `/tmp/phase8-action-8.28/patch.diff`

## Safety

- Authorized synthetic project only
- Candidate patch validated under container `/tmp`
- Running application source was not modified in place
- No production systems
- No real customer data
- No external-service testing
