# Phase 12 — Action 12.5 Sensitive Storage, Secrets and PII Inventory

## Objective

Identify privacy-relevant persistent stores and distinguish content, identity,
credentials and intentionally retained operational metadata.

## Storage inventory

### User/account data

May include:

- email;
- personal name;
- personal role;
- prior emails;
- identity-provider metadata;
- account status;
- user preferences.

### Chat data

Persistent chat storage may include:

- session metadata;
- prompts/messages;
- model responses;
- tool calls;
- search-document associations;
- file descriptors;
- titles/descriptions.

Content-free incognito operation follows a separate storage policy.

### Persistent memory

Memory stores:

- user-scoped memory text;
- user preferences;
- identity/profile context used for personalization.

The implementation bounds memory rows per user.

### Files

Files can exist in several forms:

- UserFile ownership/lifecycle rows;
- FileRecord metadata;
- object/blob storage;
- Postgres FileContent/Large Object representation;
- indexed/chunk-derived representations.

Deletion testing must therefore consider more than one table.

### Connector credentials

Connector credential records contain high-sensitivity credential JSON and are
user/permission scoped.

### OAuth

OAuth storage includes:

- client identity;
- client secret;
- per-user OAuth token data;
- granted scopes/configuration.

Current repository history includes explicit token/credential encryption
migrations, but later Phase-12 actions still verify disclosure paths rather
than assuming encrypted-at-rest means privacy-safe.

### Telemetry identifiers

Telemetry uses persistent instance/customer identifiers and can send metadata to
a telemetry endpoint when enabled.

Telemetry therefore remains an egress and secondary-storage boundary.

## Important retention exception

Repository migration:

`0d9c7b6a5e4f_retain_user_usage_after_user_deletion.py`

intentionally changes user-usage deletion behavior from CASCADE to SET NULL.

This means historical usage data is intentionally retained after deletion of
the associated user record while the direct user foreign-key association is
removed.

This is currently classified as:

**DOCUMENTED RETENTION EXCEPTION — PURPOSE / MINIMIZATION REVIEW REQUIRED**

It is not automatically classified as a vulnerability.

Action 12.9 must verify whether the retained rows contain content or only the
intended usage/accounting metadata and whether deletion semantics remain
accurately communicated.

## High-sensitivity classes

Highest sensitivity for Phase 12:

1. credentials and authentication tokens;
2. private uploaded/document content;
3. private chat/prompt/model content;
4. persistent memory/personalization;
5. personally identifying account/profile attributes.

## Evidence level

**STATIC / STORAGE INVENTORY VERIFIED**

Source trace:

`docs/security/evidence/phase12-action-12.5-sensitive-storage-source-trace.txt`

SHA-256:

`b9d38cd7c09ca5608c46ea2a7f8c80a6a9cd9c29eca0654a11a031e2a9bee2cf`

## Completion

**ACTION 12.5: COMPLETE**

**USER_USAGE_POST_DELETE_RETENTION=DOCUMENTED_FOR_12_9**

**RESULT=PHASE_12_ACTION_12_5_PASS**
