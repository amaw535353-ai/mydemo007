# Phase 9 Action 9.10 — Runtime Slice 4: H9-12

## Result

**CONFIRMED_AUTHORIZATION_DEFECT**

## Runtime context

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Runtime HEAD: `3e48c712ead09d7be2efe81c92432a0bf57ba968`
- Onyx pin: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Target: loopback-only local Onyx laboratory
- Data: synthetic only
- Execution: sequential
- File size: 38 bytes

## Runtime evidence

- Anonymous request: HTTP 403
- Alice owner/control request: HTTP 200
- Bob cross-user request: HTTP 200
- Alice response size: 38 bytes
- Bob response size: 38 bytes
- Alice SHA-256: `abfdb8d4b8f5247a86f4de23cf39858d3f78c21b323a742dda665309edf8686b`
- Bob SHA-256: `abfdb8d4b8f5247a86f4de23cf39858d3f78c21b323a742dda665309edf8686b`
- Direct Alice predicate: TRUE
- Direct Bob predicate: TRUE

## Interpretation

The anonymous control proves the route remains authentication protected.

The Alice control proves the synthetic generated-image object was valid and
retrievable.

Bob, an ordinary authenticated non-superuser, retrieved the same object and
received the same byte length and SHA-256 as Alice.

The direct authorization predicate independently returned TRUE for Bob.

Therefore H9-12 is confirmed at runtime: the assessed CHAT_IMAGE_GEN
authorization path does not enforce the expected cross-user ownership boundary.

## Cleanup

The verifier executed its automatic cleanup trap after the test, including
logout, synthetic-file deletion attempt, and restoration of temporary password
hashes.

## Harness observation

`REQUESTS_USED=0` is an accounting defect in the verifier. Request calls execute
inside shell command substitutions, so shell-variable increments do not propagate
to the parent process.

This does not change the H9-12 result. The executed path was structurally bounded
and sequential, but the counter must be corrected before relying on it as
request-ceiling evidence.

## Progress

- Runtime PASS cases: 6 / 26
- Confirmed security defects: 2
- Dispositioned cases: 15 / 26 = 57.7%
- Phase 9 completed actions: 9 / 14 = 64.3%
- Action 9.10 remains IN PROGRESS.
