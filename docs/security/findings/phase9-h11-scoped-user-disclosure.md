# Finding — Scoped Manager Can Read Users Outside Managed Groups

## Finding ID

P9-H11-01

## Status

**CONFIRMED**

## Component

`GET /manage/users`

## Security boundary

Scoped group-manager authorization.

## Expected behavior

A scoped manager should only receive user information within the groups the
manager is authorized to manage.

## Observed behavior

A synthetic scoped manager:

1. managed temporary Group A;
2. did not manage temporary Group B;
3. requested `GET /manage/users`;
4. received HTTP 200;
5. received Bob, who belonged only to Group B.

## Root cause

The route uses scoped Gate-1 authorization:

`require_permission(Permission.READ_USERS, allow_scope=True)`

The authorization framework explicitly states that `allow_scope=True` only
allows a scoped manager to reach the handler and that the handler must apply
Gate-2 resource scoping.

The route calls `get_all_users(...)` and serializes the resulting users without
a managed-group restriction.

## Security consequence

A scoped manager can read user records outside the manager's authorized group
boundary.

Only the demonstrated disclosure is claimed. No broader impact is assumed
without additional testing.

## Reproduction

Synthetic/local-only reproduction:

- manager -> manager of Group A
- Bob -> member of Group B only
- manager -> `GET /manage/users`
- result -> HTTP 200
- Bob marker -> present

## Required remediation property

For `SCOPED` authority:

- identify the groups actually managed by the requesting user;
- return only users within the permitted group scope;
- do not return users belonging exclusively to unmanaged groups;
- preserve unrestricted behavior for legitimate GLOBAL authority;
- fail closed when no managed scope exists.

## Required regression tests

1. Global administrator sees authorized organization-wide users.
2. Scoped manager sees an in-scope user.
3. Scoped manager does not see an out-of-scope user.
4. User belonging only to unmanaged groups is excluded.
5. Manager with no managed groups cannot obtain organization-wide visibility.
6. Pagination/search cannot reintroduce out-of-scope rows.
7. API-key/service identities do not bypass the same policy where applicable.

## Evidence

See:

`docs/security/evidence/phase9-action-9.10-runtime-slice3-h11-scoped-users.md`

## Cleanup

Temporary groups, memberships, password changes, and manager-cache changes were
rolled back after testing.
