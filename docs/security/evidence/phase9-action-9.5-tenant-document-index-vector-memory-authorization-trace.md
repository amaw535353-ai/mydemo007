# Phase 9 — Action 9.5 Tenant, Document, Index, Vector and Memory Authorization Trace

## Status

**STATIC AUTHORIZATION TRACE COMPLETE**

No vulnerability is confirmed by this artifact alone. Runtime verification remains mandatory.

## Objective

Trace authorization continuity across the AI data path:

`authenticated subject -> tenant context -> PostgreSQL schema -> document/user-file ACL -> search IndexFilters -> vector/index query -> returned knowledge -> user memory`

The goal is to determine whether identity and authorization properties remain attached to data as it moves from transactional storage into retrieval and AI-facing context.

## Assessed source surfaces

- `backend/shared_configs/contextvars.py`
- `backend/onyx/auth/users.py`
- `backend/onyx/db/engine/sql_engine.py`
- `backend/onyx/access/access.py`
- `backend/onyx/context/search/models.py`
- `backend/onyx/context/search/preprocessing/access_filters.py`
- `backend/onyx/context/search/pipeline.py`
- `backend/onyx/context/search/retrieval/search_runner.py`
- `backend/onyx/document_index/factory.py`
- `backend/onyx/document_index/FILTER_SEMANTICS.md`
- `backend/onyx/document_index/opensearch/search.py`
- `backend/onyx/server/query_and_chat/chat_backend.py`
- `backend/onyx/db/user_preferences.py`
- `backend/onyx/server/manage/users.py`
- `backend/onyx/tools/tool_implementations/memory/memory_tool.py`

## 1. Tenant-context boundary

### Source-backed design

`CURRENT_TENANT_ID_CONTEXTVAR` is the per-request tenant context. In multi-tenant mode its default is `None`, while single-tenant mode defaults to the configured PostgreSQL schema.

`get_current_tenant_id()` fails closed in multi-tenant mode when no tenant has been established.

A separate `SESSION_TENANT_OVERRIDE_CONTEXTVAR` exists for session issuance. The source comment explicitly distinguishes it from the current request tenant because request-carried workspace context must not by itself decide where a session is issued.

Authentication code binds tenant context for tenant-specific user/session work and resets the context after the operation/request scope.

### Database enforcement

`get_session_with_current_tenant()` resolves the current tenant and delegates to `get_session_with_tenant(tenant_id=...)`.

`get_session_with_tenant`:

- validates the tenant/schema name;
- selects the tenant-aware engine/shard path;
- binds the SQLAlchemy connection with `schema_translate_map={None: tenant_id}` in multi-tenant operation.

Therefore the database access path has an explicit tenant-to-schema binding rather than relying on callers to qualify every table manually.

## 2. Vector/index tenant boundary

`backend/onyx/document_index/factory.py` builds `TenantState` from `get_current_tenant_id()`.

The search pipeline also writes the current tenant into `IndexFilters.tenant_id` when multi-tenant mode is enabled.

The documented active OpenSearch filter semantics require tenant filtering as a top-level AND condition.

The OpenSearch query builder independently adds a `tenant_id == tenant_state.tenant_id` term whenever `tenant_state.multitenant` is true.

### Security interpretation

Tenant isolation is represented in both:

1. PostgreSQL schema selection; and
2. vector/index query filtering.

Runtime testing must verify that both layers receive the same authenticated tenant and cannot be desynchronized by request input, stale credentials, alternate credential types, or background/internal search paths.

## 3. Document ACL construction

`get_acl_for_user()` constructs the retrieval ACL for the authenticated user.

Observed behavior:

- anonymous users receive only the public-document marker;
- authenticated users receive their prefixed email identity;
- prior email aliases are included to preserve access during rename transitions;
- public documents are also included.

For documents missing access metadata, the access layer explicitly falls back to least-permissive `DocumentAccess` rather than public access.

## 4. User-file and attached-resource authorization

User-file access is built from resource relationships rather than a global file list.

The traced access model includes:

- direct owner access;
- access through a public persona;
- access through a persona owned by the user;
- access through direct persona sharing;
- public/shared chat-session file access where applicable;
- connector-file access by mirroring document retrieval ACLs.

For connector-backed files, the code resolves representative document IDs and checks the requesting user's ACL against the documents' access controls.

## 5. Chat-file read boundary

`GET /chat/file/{file_id}` requires `Permission.BASIC_ACCESS` and calls `user_can_access_chat_file(...)` before reading bytes from the file store.

A failed authorization check is returned as `404 File not found` rather than `403`, reducing cross-user file-existence probing.

Most asset classes are checked against owner, sharing, persona or document ACL relationships before read.

### H9-12 — generated chat image cross-user authorization hypothesis

The access function contains an explicit exception for `FileOrigin.CHAT_IMAGE_GEN`:

- a matching generated-image file record returns `True` without an owner, chat-session, persona or document-ACL check;
- the source comment states this is because the bytes are written before the linking tool-call row is available.

Security property to verify at runtime:

> A synthetic user must not be able to fetch another synthetic user's generated chat image solely by knowing its file ID unless product policy explicitly defines that asset as workspace-public.

Required runtime matrix:

- owner -> own generated image: expected ALLOW;
- same-tenant non-owner -> owner's generated image: expected DENY unless documented sharing policy says otherwise;
- cross-tenant user -> owner's generated image: expected DENY;
- random/unknown file ID -> expected 404;
- verify response body, cache headers and server audit/log behavior.

Static status: **HYPOTHESIS / DESIGN EXCEPTION — NOT YET A CONFIRMED VULNERABILITY**.

## 6. Search ACL propagation

`build_access_filters_for_user()` converts the user ACL into `IndexFilters.access_control_list`.

`_build_index_filters()` in the search pipeline:

- validates user-supplied document-set names against the user's accessible document sets;
- derives the requesting user's ACL unless an explicitly supplied trusted ACL is used;
- writes ACL values into `IndexFilters.access_control_list`;
- writes the active tenant into `IndexFilters.tenant_id` in multi-tenant mode;
- preserves assistant/project/document/hierarchy knowledge-scope restrictions.

`search_chunks()` forwards the final `IndexFilters` into the document-index retrieval implementation.

## 7. OpenSearch ACL enforcement

The active OpenSearch query builder applies ACL visibility as:

- public document; OR
- at least one matching entry from the requesting user's ACL.

That ACL visibility predicate is then ANDed with the other search restrictions.

In multi-tenant mode the OpenSearch query also ANDs the tenant term.

The result is an intended retrieval predicate equivalent to:

```text
NOT hidden
AND tenant == authenticated_tenant
AND (public == true OR document_acl intersects user_acl)
AND knowledge/filter restrictions
```

This must still be tested dynamically because static filter construction does not prove every search/retrieval caller uses the safe path.

## 8. H9-13 — ACL-bypass provenance hypothesis

`ChunkSearchRequest` includes a `bypass_acl: bool = False` field.

When `bypass_acl` is true, `_build_index_filters()` intentionally sets the user ACL filter to `None`, and the OpenSearch layer treats an explicitly absent ACL list as no ACL restriction.

`SearchTool` also accepts a `bypass_acl` constructor argument defaulting to `False`.

This can be legitimate for trusted internal/system flows, but Phase 9 must prove that untrusted users cannot cause this flag to become true through a public API, agent/tool parameter, alternate request model or delegated execution path.

Security property:

> Only explicitly trusted server-side flows may bypass document ACL enforcement, and the bypass authority must not be derivable from user-controlled request data.

Static status: **TRUST-BOUNDARY HYPOTHESIS — CALLER PROVENANCE NOT YET FULLY VERIFIED**.

## 9. Memory authorization boundary

Memory persistence is user-keyed in PostgreSQL.

`get_memories_for_user(user_id, ...)` selects memories by `Memory.user_id`.

`update_user_personalization(...)`:

- loads existing memories scoped to the supplied `user_id`;
- deletes only rows matching both selected memory IDs and the same `user_id`;
- updates only memories loaded from that user's scoped set;
- creates new memories with that `user_id`.

The public personalization endpoint requires `Permission.BASIC_ACCESS` and always passes the authenticated `user.id`; it does not accept a target user ID from the request.

`GET /me` likewise returns memories using the authenticated `user.id`.

The Memory Tool receives the current user's existing memories through server-provided override kwargs and emits an add/update result; persistence remains tied to the user-specific personalization path.

### Runtime properties to verify

- User A can read/update/delete only User A memories.
- User B cannot reference User A memory IDs to update or delete them.
- tenant switching cannot expose another tenant's memories.
- incognito/non-persisting chat modes do not persist memory unexpectedly.

## 10. Authorization-continuity model

```text
Authenticated credential
        |
        v
resolved user + authenticated tenant
        |
        +------------------------------+
        |                              |
        v                              v
PostgreSQL tenant schema        user ACL construction
        |                              |
        |                              v
        |                       IndexFilters ACL
        |                              |
        |                              +---- tenant_id
        |                              +---- knowledge scope
        |                              |
        |                              v
        |                       vector/index query
        |                              |
        +------------------------------+
                       |
                       v
            authorized AI context
                       |
                       v
             user-specific memory
```

The security goal is continuity: the subject and tenant authorized at request entry must remain the subject and tenant used for database, document, vector and memory decisions.

## 11. Runtime test targets carried forward

### T9-05A — tenant/schema consistency

For Tenant Alpha and Tenant Beta synthetic identities, verify the authenticated tenant, PostgreSQL schema and vector/index tenant predicate remain identical for the same request.

### T9-05B — document ACL isolation

Create private synthetic documents for Alice and Bob and verify owner/public/unauthorized retrieval outcomes.

### T9-05C — vector retrieval isolation

Use identical unique marker text in authorized and unauthorized synthetic documents and verify search/RAG returns only ACL-allowed chunks.

### T9-05D — generated image ownership

Verify H9-12 using two synthetic users and a generated-image file ID.

### T9-05E — ACL bypass provenance

Trace every construction of `ChunkSearchRequest(..., bypass_acl=True)` and every `SearchTool(..., bypass_acl=True)` and prove the call path is trusted/system-only.

### T9-05F — memory isolation

Attempt cross-user memory-ID substitution and verify another user's memory cannot be read, changed or deleted.

## 12. Current conclusion

Source analysis shows deliberate tenant isolation at the SQL and vector-index layers, explicit document/user-file ACL construction, owner-bound memory persistence, and authorization-aware file serving for most asset classes.

Two high-priority properties require follow-up:

- **H9-12:** generated chat images use a deliberate file-authorization exception;
- **H9-13:** the search pipeline contains an explicit ACL-bypass mode whose caller provenance must be proven trusted.

Neither is classified as a confirmed vulnerability by this static trace alone.

## Result

**PASS — Action 9.5 static authorization continuity trace captured.**
