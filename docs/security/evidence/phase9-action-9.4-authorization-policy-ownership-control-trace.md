# Phase 9 — Action 9.4 Authorization Policy and Ownership-Control Trace

## Status

**COMPLETE — STATIC TRACE**

Runtime authorization effectiveness has not yet been claimed by this artifact.

## Objective

Trace the source-backed authorization decision chain from authenticated subject to
permission classification, scoped authorization, ownership/ACL checks and resource
access. Identify concrete horizontal, vertical and scoped-manager test targets for
the executable negative-test pack.

## Assessed branch

`security/phase-9-identity-authorization-tenant-isolation`

## Starting Phase 9 head

`b8b9957286755e47b6de653dc9f7347352d04a93`

## Authorization decision model

The source establishes the following conceptual chain:

```text
credential / session
        |
        v
resolved User
        |
        v
required Permission
        |
        v
has_permission(user, permission)
        |
        +--> GLOBAL ---------------> unrestricted permission authority
        |
        +--> SCOPED ---------------> GATE 1 route admission only
        |                              |
        |                              v
        |                           GATE 2 resource-scope enforcement
        |
        +--> NONE -----------------> deny
        |
        v
PAT/token scope cap (when present)
        |
        v
resource-specific authorization
        |
        +--> ownership/user_id
        +--> managed group scope
        +--> resource ACL
        +--> sharing state
        +--> tenant-bound DB/session context
        |
        v
ALLOW / DENY
```

## 1. Permission expansion and privilege model

`backend/onyx/auth/permissions.py` stores direct grants and expands implied
permissions at read time.

Important implications include:

- `MANAGE_AGENTS` -> `ADD_AGENTS`, `READ_AGENTS`, `READ_DOCUMENT_SETS`,
  `READ_AGENT_ANALYTICS`;
- `MANAGE_DOCUMENT_SETS` -> `READ_DOCUMENT_SETS`, `READ_CONNECTORS`,
  `READ_USER_GROUPS`;
- `MANAGE_CONNECTORS` -> `READ_CONNECTORS`, `READ_USER_GROUPS`;
- `MANAGE_USER_GROUPS` -> `READ_CONNECTORS`, `READ_DOCUMENT_SETS`, `READ_AGENTS`,
  `READ_USERS`, `READ_USER_GROUPS`;
- `MANAGE_LLMS` -> `READ_USER_GROUPS`, `READ_AGENTS`, `READ_USERS`;
- `BASIC_ACCESS` -> chat/search/image/LLM-gateway abilities.

`FULL_ADMIN_PANEL_ACCESS` is an override that resolves all permissions.

### Security consequence

A test must distinguish the directly granted permission from implied permissions.
A subject may reach a read surface because a broader management grant implies the
read token even though that read token was never persisted directly.

## 2. GLOBAL / SCOPED / NONE authority

`has_permission()` classifies authority as:

- **GLOBAL** — direct/effective permission or full administrator;
- **SCOPED** — group manager for a permission in the expanded scoped-manager bundle;
- **NONE** — no authority.

This is deliberately not a boolean model.

## 3. GATE 1 — route admission

`require_permission()` is the route-level dependency.

Default behavior requires GLOBAL authority.

When `allow_scope=True`, a SCOPED group manager may reach the handler. The source
explicitly states that this is **reach only, never authorization**.

The dependency also caps a PAT-authenticated request by the PAT's token scopes.
Thus an otherwise privileged user may still be denied when the authenticating PAT
does not include/imply the required permission.

## 4. GATE 2 — scoped resource authorization

`backend/onyx/auth/scoped_permissions.py` defines the write-side scoped-manager
authorization primitives.

`within_scope()` / `assert_within_scope()` require a scoped manager's target to:

- be non-public;
- belong to at least one group;
- have every current/requested group contained in the manager's managed groups.

The gate fails closed for NONE authority, empty managed scope, out-of-scope groups
or public resources.

`assert_manages_group()` enforces single-group actions.

`assert_global()` provides an explicit global-only control for actions such as
delete operations where scoped authority must not be sufficient.

Denials emit audit events.

## 5. Read-side GATE 2

`backend/onyx/db/scoped_permissions.py` provides `within_managed_scope_clause()`.

The read-side predicate requires:

- a non-public resource;
- at least one relationship to a managed group;
- no relationship to an unmanaged group.

The permission framework explicitly states that every READ endpoint using
`allow_scope=True` must apply its own GATE 2 scope filter, otherwise the handler
could return all rows.

## 6. Confirmed owner-bound chat authorization pattern

`backend/onyx/server/query_and_chat/chat_backend.py` protects chat surfaces with
permission dependencies and passes the authenticated `user.id` into resource
lookups.

Examples:

- list chat sessions -> `READ_CHAT` and query by `user.id`;
- update temperature/reasoning/model -> `BASIC_ACCESS` plus
  `get_chat_session_by_id(..., user_id=user.id)`;
- get chat session -> `READ_CHAT`; non-shared access is bound to the authenticated
  user; explicitly shared access requires public sharing state;
- rename / patch / delete -> authenticated user ID is supplied to the database
  authorization path.

`backend/onyx/db/chat.py` applies the ownership predicate in
`get_chat_session_by_id()`:

- ordinary access limits the row to `ChatSession.user_id == user_id` or an
  unassigned session;
- shared access limits the row to `shared_status == PUBLIC`.

`get_chat_message()` separately compares the chat-session owner with the supplied
user ID and rejects mismatches.

### Runtime targets

- Alice session -> Alice: ALLOW;
- Alice session -> Bob: DENY;
- Alice private session -> anonymous/shared lookup: DENY;
- Alice public-shared session -> permitted shared-read flow: ALLOW;
- Bob update/delete against Alice session: DENY.

## 7. Confirmed global-admin control pattern

`backend/onyx/server/manage/users.py` applies
`require_permission(FULL_ADMIN_PANEL_ACCESS)` to high-impact user administration
including:

- changing administrator access;
- changing Craft access;
- listing accepted/invited users on admin-only endpoints;
- bulk invitation;
- invitation removal;
- user deactivation;
- user deletion.

### Runtime targets

- administrator -> admin mutation: ALLOW;
- normal user -> admin mutation: DENY;
- scoped group manager -> full-admin mutation: DENY;
- PAT belonging to admin but lacking required scope -> DENY where token scoping applies.

## 8. Confirmed scoped connector pattern

Connector administration provides examples of intended scoped-manager handling.

`backend/onyx/server/documents/connector.py` contains routes using
`allow_scope=True`, user-aware connector/cc-pair retrieval, and write-side
`assert_within_scope()`.

For example, connector creation with a mock credential performs GATE 2 with:

- `MANAGE_CONNECTORS`;
- requested group IDs;
- a requirement that the resource be non-public for scoped authority.

Connector indexing/status logic also separates editable and non-editable resources
for the current user and gives global connector administrators broader authority.

### Runtime targets

- scoped manager -> private connector fully inside managed groups: ALLOW;
- scoped manager -> connector assigned to unmanaged group: DENY;
- scoped manager -> public connector mutation requiring scoped authority: DENY unless
  an explicit global/public exception applies;
- global connector manager -> authorized global operation: ALLOW.

## 9. High-priority static hypothesis — scoped READ_USERS filtering

### Hypothesis ID

**H9-11 — Scoped manager may receive user rows outside managed groups**

### Static path

`GET /manage/users` in `backend/onyx/server/manage/users.py` uses:

```text
require_permission(Permission.READ_USERS, allow_scope=True)
```

`READ_USERS` is implied by `MANAGE_USER_GROUPS` and `MANAGE_LLMS`.
A group manager can therefore resolve SCOPED authority for this read token when the
permission falls within the expanded scoped-manager bundle.

The route body then calls `get_all_users(...)`, splits users into accepted/bot
collections, builds snapshots and returns them.

In the traced route body, no explicit `within_managed_scope_clause()`, managed-group
ID filter, or equivalent GATE 2 read filter is visible before serialization.

### Why this matters

The permission framework explicitly says a READ + `allow_scope=True` endpoint must
apply a GATE 2 scope filter or a scoped manager could receive all rows.

### Classification

**STATIC AUTHORIZATION HYPOTHESIS — NOT YET A CONFIRMED VULNERABILITY**

The runtime may contain additional behavior not proven by this static route trace.
No vulnerability is claimed until controlled testing demonstrates an out-of-scope
response.

### Required runtime test

Create synthetic groups and users:

- Group A managed by synthetic manager `manager-a`;
- Alice in Group A;
- Group B not managed by `manager-a`;
- Bob in Group B.

Expected security property:

```text
manager-a -> GET /manage/users
Alice / managed-scope rows: visible as intended
Bob / unmanaged-scope row: MUST NOT be disclosed if scoped READ_USERS is intended
                           to be group-limited
```

Capture exact response rows, HTTP status, permission state and group membership.

If Bob is returned, validate product requirements before classifying severity,
because the intended semantics of READ_USERS must be confirmed against the scoped
manager design.

## 10. Negative-test matrix produced by this trace

| ID | Subject | Resource/action | Expected |
|---|---|---|---|
| AUTHZ-01 | anonymous | protected ordinary chat | DENY |
| AUTHZ-02 | Alice | Alice private chat read | ALLOW |
| AUTHZ-03 | Bob | Alice private chat read | DENY |
| AUTHZ-04 | Bob | Alice chat update/delete | DENY |
| AUTHZ-05 | anonymous/other user | Alice public shared chat through shared flow | ALLOW if sharing contract permits |
| AUTHZ-06 | ordinary user | full-admin user mutation | DENY |
| AUTHZ-07 | scoped manager | full-admin user mutation | DENY |
| AUTHZ-08 | global admin | full-admin user mutation | ALLOW |
| AUTHZ-09 | scoped connector manager | in-scope private resource | ALLOW |
| AUTHZ-10 | scoped connector manager | out-of-scope group resource | DENY |
| AUTHZ-11 | scoped connector manager | public resource requiring scoped write | DENY unless explicit global/public exception |
| AUTHZ-12 | scoped group manager | `/manage/users` unmanaged-group visibility | DENY / scope-limited if design intent is group-limited |
| AUTHZ-13 | privileged user with under-scoped PAT | permission outside PAT scope | DENY |

## 11. Security interpretation

The assessed source contains multiple explicit authorization layers rather than a
single route-level role check:

```text
identity -> effective permission -> token scope -> authority kind ->
route gate -> resource scope / owner / ACL -> tenant-backed data path
```

This is a strong design pattern, but it also creates a predictable failure mode:
any route using scoped GATE 1 without the matching GATE 2 becomes a high-value
candidate for over-broad access.

The Phase 9 runtime suite must therefore test both known secure paths and each
`allow_scope=True` route for missing or inconsistent GATE 2 enforcement.

## Result

**PASS — authorization policy and ownership-control architecture traced.**

One high-priority static hypothesis (`H9-11`) has been promoted into the runtime
authorization test backlog. No new vulnerability is claimed by Action 9.4 alone.
