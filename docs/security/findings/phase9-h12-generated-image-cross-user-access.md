# Finding — Generated Chat Image Accessible Cross-User

## Finding ID

P9-H12-01

## Status

**CONFIRMED**

## Component

`GET /chat/file/{file_id}`

## Security boundary

Authenticated cross-user file authorization.

## Expected behavior

A private generated chat image belonging to Alice should not be readable by an
unrelated ordinary authenticated Bob unless an explicit sharing policy grants
access.

## Observed behavior

1. A synthetic `CHAT_IMAGE_GEN` file was created and marked for Alice.
2. Anonymous access returned HTTP 403.
3. Alice retrieved the object with HTTP 200.
4. Bob, an unrelated ordinary non-superuser, requested the same file ID.
5. Bob also received HTTP 200.
6. Alice and Bob received identical 38-byte responses with identical SHA-256.
7. `user_can_access_chat_file(...)` returned TRUE for both Alice and Bob.

## Root cause

The assessed authorization helper contains a special `CHAT_IMAGE_GEN` path that
returns authorization success without resolving ownership through user, chat,
persona, document ACL, or an equivalent owner-bound relation.

## Required remediation property

Generated images must carry sufficient authorization context to establish their
owner and sharing state at read time.

Authorization should:

- allow the legitimate owner;
- deny unrelated authenticated users;
- preserve explicitly intended shared/public-chat semantics;
- enforce tenant isolation where applicable;
- fail closed when ownership metadata is absent or malformed.

## Required regression tests

1. Alice can retrieve Alice's generated image.
2. Bob cannot retrieve Alice's private generated image.
3. Anonymous access remains denied.
4. Cross-tenant access is denied where multi-tenant mode applies.
5. Explicit public/shared-chat behavior follows documented product policy.
6. Missing ownership metadata fails closed.
7. Existing non-CHAT_IMAGE_GEN file authorization remains unchanged.

## Evidence

`docs/security/evidence/phase9-action-9.10-runtime-slice4-h12.md`
