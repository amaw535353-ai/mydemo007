# Phase 12 — Action 12.3 Data Classification, Ownership and Tenant Boundaries

## Classification

### Identity data

Examples:

- email;
- personal name;
- role;
- IdP organization fields;
- prior email aliases.

### User content

Examples:

- chat messages;
- prompts;
- uploaded files;
- generated files;
- memories;
- user preferences.

### Enterprise/source content

Examples:

- connector documents;
- permissions;
- retrieved chunks;
- citations.

### Authentication secrets

Examples:

- connector credentials;
- OAuth client secrets;
- OAuth user tokens;
- provider keys.

### Operational metadata

Examples:

- token usage;
- timestamps;
- indexing state;
- audit/security events.

## Ownership controls verified

Chat session lookup includes a user constraint for non-shared access.

Individual chat-message lookup compares the message session's user identity to
the requesting user.

Memory reads and memory updates are explicitly user scoped.

Credential retrieval applies user-aware credential filtering.

User-file processing contains explicit owner-scoped paths.

## Important trust-boundary note

`get_user_file_by_id()` is a low-level ID lookup rather than a complete
authorization API.

Its existence is not classified as a vulnerability by itself.

Every externally reachable consumer of low-level ID-only helpers must be
reviewed for authorization before Phase 12 can claim cross-user privacy
isolation.

That becomes direct negative testing in Action 12.11.

## Current conclusion

**NO CROSS-USER PRIVACY BYPASS CONFIRMED BY THIS ACTION**

Live cross-tenant runtime isolation is not yet claimed.

## Evidence

Results:

`docs/security/evidence/phase12-action-12.3-ownership-results.txt`

SHA-256:

`383d8ede7b003e72004dafb1e7c10c19e40973f2b290b72480e38bb57ce8d5b3`

Source trace:

`docs/security/evidence/phase12-action-12.3-ownership-source-trace.txt`

SHA-256:

`7d71686108ed7b136ac41cb1c9058b6687abcdb50f3771629688bf641f5cd91b`

Test:

`backend/tests/unit/onyx/db/test_phase12_data_ownership_boundaries.py`

## Completion

**ACTION 12.3: COMPLETE**

**RESULT=PHASE_12_ACTION_12_3_PASS**
