# Phase 9 Action 9.11 — H9-16 Policy and Root-Cause Decision

## Status

**POLICY DECIDED — ROOT CAUSE CONFIRMED — REMEDIATION NOT YET IMPLEMENTED**

Finding:

`H9-16 — Request-supplied MCP headers can exceed the configured server trust policy`

This is a confirmed failure of assessment requirement SR-H9-16 in the
security-hardened fork. It is not classified here as an upstream Onyx
vulnerability because real downstream authorization impact was not demonstrated
and the request-header feature may intentionally support delegated per-user
authentication.

## Decision baseline

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Decision parent: `582f36a7c33fdf0462f8f3c2f9f4352fa7d0c947`
- Runtime evidence:
  `docs/security/evidence/phase9-action-9.10-runtime-slice8-h16.md`
- Runtime evidence provenance: recovered terminal transcript, not the original
  immutable log
- Data and credentials: synthetic only
- External or production target testing: none

## Security requirement

Request-time MCP headers must not grant a caller authority beyond the
administrator-configured policy for the selected MCP server.

The hardened fork must preserve legitimate per-user delegation without treating
an arbitrary request dictionary as a trusted extension of an administrator-managed
MCP identity.

## Reproduced behavior

The bounded loopback test established that:

- managed headers win case-insensitive collisions;
- caller `Host` is filtered;
- passthrough OAuth and dead-OAuth protections behave as intended;
- non-colliding caller headers remain on an administrator-authenticated MCP call;
- an unconfigured synthetic privilege-signaling header reached the receiver;
- caller `Authorization` allowed a per-user API-token call to proceed when no
  stored user credential was available.

The receiver did not validate any synthetic header as a real credential or grant
a real privilege. Downstream exploitability therefore remains conditional and
unconfirmed.

## Source-backed root cause

At the decision parent:

1. `SendMessageRequest.mcp_headers` accepts an arbitrary `dict[str, str]` and
   documents request-time user JWT and user-ID forwarding.
2. Chat processing carries the dictionary into `CustomToolConfig`.
3. `construct_tools` passes the dictionary to every selected `MCPTool` for the
   corresponding server without applying a server-specific policy.
4. `MCPTool.run` removes only globally denylisted names and then merges all
   remaining request headers with resolved credential headers.
5. Managed credential headers correctly win collisions, but non-colliding request
   headers remain.
6. The authentication gate treats the mere presence of additional request headers
   as sufficient to attempt a call when ordinary credentials are missing, except
   for a dead OAuth grant.

This is a trust-policy omission rather than a collision-precedence defect.

## Existing control that will be reused

`MCPAuthTemplate` already provides an administrator-controlled, per-server map of
validated header names to value templates. `get_mcp_auth_template` resolves that
template from the server's administrator connection configuration, including the
legacy per-user API-token representation.

The remediation will reuse the configured template header names as the
case-insensitive allowlist for request-time delegated headers. This is a design
inference from the existing model and avoids adding a database column, migration,
or separate UI policy field.

## Hardened-fork policy decision

### Default

Request-supplied MCP headers are denied by default.

An absent or empty administrator `MCPAuthTemplate` therefore permits zero
request-supplied headers.

### Server-controlled allowlist

Only header names present in the selected server's administrator-controlled
`MCPAuthTemplate.headers` may be sourced from `mcp_headers`.

Matching is case-insensitive. Values remain request scoped and are never stored by
this path.

### Credential fallback

Request headers may stand in for missing stored credentials only when all of the
following are true:

1. the server uses `API_TOKEN` authentication;
2. the authentication performer is `PER_USER`;
3. an administrator-controlled authentication template exists;
4. every request header used for credential fallback is allowlisted after case
   normalization;
5. the final merged header set covers the header names required by the template;
6. the credential state is not a dead OAuth grant.

Request headers must never satisfy missing administrator-managed, OAuth,
passthrough-OAuth, or unauthenticated-server identity state.

### Precedence and protocol safety

- resolved managed credentials remain the final merge source and win collisions;
- globally denied names remain forbidden even if a malformed legacy template
  contains them;
- `Host` and standard hop-by-hop header names must be denied;
- filtering and logging operate on header names only and never emit values;
- case variants cannot bypass allowlist, denylist, or collision behavior.

## Implementation boundary

The minimal remediation is limited to:

- request-header policy helpers in the MCP model/tool layer;
- the `MCPTool.run` merge and missing-credential decision;
- focused unit tests for policy and precedence;
- the bounded loopback regression probe;
- evidence and Phase 9 status updates after tests pass.

No database migration, UI change, LLM invocation, external MCP call, or production
configuration change is required for this remediation design.

## Required regression cases

| Case | Expected result |
|---|---|
| ADMIN credential plus unlisted caller privilege header | caller header removed; managed call may proceed |
| Caller and managed header collision with case variation | managed value wins |
| `Host` or hop-by-hop request header | removed regardless of template |
| PER_USER API token, no template, no stored credential | authentication error; no call |
| PER_USER API token, template allows `Authorization`, caller supplies it | delegated call allowed |
| PER_USER API token, template does not allow caller header | header removed; missing-credential call denied |
| PER_USER API token, incomplete required template header set | authentication error; no call |
| Passthrough OAuth plus caller `Authorization` | login OAuth token wins; caller value cannot stand in |
| Live OAuth plus caller `Authorization` | generated OAuth token wins |
| Dead OAuth plus caller `Authorization` | authentication error; no call |
| No-auth server plus caller identity/privilege header | caller header removed |
| Mixed-case allowlist and denylist names | same result as normalized names |

## Completion criteria

H9-16 remediation is complete only when:

1. regression tests fail against the vulnerable behavior and pass against the
   patch;
2. the bounded loopback receiver no longer observes unlisted request headers;
3. explicitly allowlisted per-user delegation still works;
4. managed precedence and OAuth protections remain intact;
5. source, test and runtime evidence contain no raw credential values;
6. the exact remediation commit and runtime source hashes are preserved;
7. residual downstream-policy risk is documented.

## Result

**H9-16_POLICY_ROOT_CAUSE_READY**
