# Phase 9 Action 9.10 — Runtime Slice 6: H9-14

## Result

**CONFIRMED BUSINESS-LOGIC AUTHORIZATION FAILURE**

Credential transmission was not tested and remains unconfirmed.

## Runtime context

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Runtime HEAD: `46b852e8c3283d13af0b3a023617269890676504`
- Onyx pin: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Target: local Onyx laboratory
- Data and identities: synthetic only
- Execution: sequential
- HTTP requests: 0
- External calls: 0
- Persistent database changes: 0

## Security requirement

A user must not attach another creator's custom action without owner or actions-administrator authority.

Existing attachments can remain during ordinary agent edits. Removal revokes the ability to reattach the action.

## Observed evidence

The transactional test created these temporary objects:

- one Alice-owned custom OpenAPI action;
- one synthetic static header;
- one Bob-owned persona.

The test called `upsert_persona` as Bob with Alice's custom-action identifier.

The observed markers were:

- `ALICE_TOOL_CREATED_IN_TRANSACTION=PASS`
- `ALICE_TOOL_OWNER_MATCH=PASS`
- `BOB_PERSONA_OWNER_MATCH=PASS`
- `FOREIGN_ALICE_TOOL_ATTACHED=TRUE`
- `EXPECTED=FOREIGN_ATTACHMENT_REJECTED`
- `OBSERVED=FOREIGN_ATTACHMENT_ACCEPTED`
- `RESULT=P9_H14_01_CANDIDATE_FAIL`

The cleanup markers were:

- `ROLLBACK_EXECUTED=YES`
- `REMAINING_TEST_TOOLS=0`
- `REMAINING_TEST_PERSONAS=0`
- `ROLLBACK_VERIFIED=PASS`

No header value was printed. The test did not invoke the action.

## Interpretation

The runtime result confirms unauthorized attachment at the business-logic layer under the selected fork policy.

It does not confirm that Bob received or transmitted Alice's stored header value.

The assessed source shows that custom-action construction can consume stored static headers. That source property increases potential impact.

## Product-policy decision

The assessed Onyx source treats custom actions as a tenant-wide selectable catalog.

The security-hardened fork uses a stricter policy for new attachments:

- creator or actions administrator: allow;
- unrelated user: deny;
- existing attachment during an update: preserve;
- removed foreign attachment: deny reattachment.

This decision changes the current tenant-wide attachment behavior. It does not change existing attachments automatically.

## Disposition

`P9-H14-01`: **FAIL — REMEDIATION IMPLEMENTED, DATABASE RETEST PENDING**

`P9-H14-02`: **NOT EXECUTED — CREDENTIAL TRANSMISSION UNCONFIRMED**
