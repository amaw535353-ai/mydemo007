# Phase 9 Action 9.10 — H9-12 Source Verification

Status: **SOURCE-CONFIRMED — RUNTIME HTTP PROOF PENDING**

## Scope

Authorized local Onyx security lab only. Synthetic data only.

Repository branch:

`security/phase-9-identity-authorization-tenant-isolation`

Assessed Onyx commit:

`160f9b143605ca45a85bd387b5bd173840bab15d`

Hypothesis:

`H9-12 — Generated chat image cross-user authorization exception`

## Source verification

At the assessed Onyx commit, the authenticated route:

`GET /chat/file/{file_id}`

requires:

`Permission.BASIC_ACCESS`

and then calls:

`user_can_access_chat_file(file_id, user, db_session)`

before reading the file bytes.

In `backend/onyx/access/access.py`, the helper checks several normal authorization paths first, including:

- user-file ownership;
- persona attachment access;
- chat-session ownership/public sharing;
- connector/document ACLs.

However, a `FileRecord` with:

`FileOrigin.CHAT_IMAGE_GEN`

takes a separate branch that returns `True` without binding the file to the requesting user, chat session, persona, or document ACL.

The relevant behavior is therefore:

1. requester has BASIC_ACCESS;
2. target file exists;
3. target file origin is CHAT_IMAGE_GEN;
4. `user_can_access_chat_file(...)` returns `True`;
5. the route proceeds to read and return the stored file.

This confirms the **source-level authorization exception** targeted by H9-12.

## Security interpretation

This evidence is sufficient to establish that the assessed code path does not enforce per-user ownership for CHAT_IMAGE_GEN records.

It is **not** recorded as runtime confirmation yet because this chat cannot reach the user's WSL/Codespace loopback interface and no external or billable runner is authorized as a substitute.

The remaining runtime proof is deliberately narrow:

- anonymous request -> DENY;
- Alice owner/control -> ALLOW;
- Bob ordinary authenticated user -> expected DENY under the project security property;
- direct predicate for Bob -> expected FALSE under the project security property.

A Bob HTTP 200 plus `BOB_CAN_ACCESS=TRUE` would provide reproducible runtime confirmation of the cross-user disclosure property.

## Existing bounded verifier

Runtime verifier:

`scripts/security/phase9_slice4_h12_runtime.sh`

Verified safety properties:

- loopback-only target;
- sequential execution;
- request ceiling: 20;
- response/file ceiling: 1 MiB;
- synthetic Alice/Bob actors only;
- temporary credential rollback;
- synthetic file cleanup;
- no external target required.

The verifier's cleanup path was corrected in commit:

`65272549cca243762081a174245c7afe6ea65986`

## Remediation property

Do not treat every CHAT_IMAGE_GEN record as globally readable to all authenticated users.

The generated file must be bound to an authorization context that can be evaluated at read time, such as the owning chat session/user (and tenant where applicable).

The Onyx source itself notes that generated images do not currently reach `ChatMessage.files` and that a durable fix requires stamping sufficient chat-session ownership context into `FileRecord.file_metadata` (or an equivalent normalized relation) when the file is saved.

A correct fix must preserve:

- owner access;
- deliberately shared/public chat semantics where intended;
- tenant isolation;
- fail-closed behavior when ownership context is absent;
- compatibility with generated-image creation timing.

## Required regression tests

1. Alice can read Alice's generated image.
2. Bob cannot read Alice's private generated image.
3. A user in another tenant cannot read the image where multi-tenant mode applies.
4. Anonymous access is denied.
5. Public/shared chat behavior follows explicit product policy.
6. Missing or malformed generated-image ownership metadata fails closed.
7. Existing non-CHAT_IMAGE_GEN file authorization behavior is unchanged.
8. The negative test remains bounded and reproducible.

## Decision

**H9-12 source path: CONFIRMED.**

**H9-12 live HTTP reproduction: PENDING.**

**Action 9.10 remains IN PROGRESS and Phase 9 remains at 64.3% until local runtime evidence is captured.**
