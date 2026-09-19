# Phase 9 Action 9.10 — Runtime Slice 8: H9-16

## Status

**RUNTIME REPRODUCTION PASS — SR-H9-16 POLICY EXPECTATION FAIL**

Hypothesis:

`H9-16 — Request-supplied MCP headers require explicit trust-policy verification`

This record confirms a policy gap under the security requirement adopted by this
assessment. It does not, by itself, classify the behavior as an upstream Onyx
vulnerability. Upstream impact depends on whether a configured MCP server assigns
authority to a caller-controlled header that Onyx forwards.

## Assessed baseline

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Runtime HEAD: `98a9d132c0e867b94390e8ad114599a9928706c4`
- Environment: authorized local Onyx laboratory
- Data and credentials: synthetic only
- Receiver: ephemeral loopback FastMCP service on `127.0.0.1`
- External requests: `0`
- LLM invocations: `0`
- Database mutations: `0`
- Repository mutations during reproduction: `0`
- Receiver request ceiling: `40`
- Runtime ceiling: `55` seconds inside a `60`-second batch bound

The application log displayed `09/19/2026 09:06:04 PM` through
`09/19/2026 09:06:05 PM`. The logger did not emit a timezone, so this record does
not assert that those displayed times are UTC.

## Evidence provenance

The original temporary runtime log and runner were no longer present when
repository preservation was attempted. The preservation gate stopped with
`RESULT=BLOCKED_RUNTIME_LOG_MISSING` before creating this file.

This Markdown record is therefore a **recovered evidence summary**, reconstructed
from the previously captured successful terminal execution transcript. The log
size and SHA-256 below are the values printed by that successful batch; they could
not be independently recomputed during repository preservation.

This record must not be represented as the original immutable runtime log.

## Recorded evidence metadata

- Runtime runner SHA-256:
  `72a56b02916862e3bacfb455cb34eaa82a531ddbb5592d0deb69df1e5652b906`
- Original temporary runtime log path:
  `/tmp/phase9-h16-runtime-policy-probe.txt`
- Recorded runtime log size: `2203` bytes
- Recorded runtime log SHA-256:
  `14fc249d5145a2e1ca60312af9d5d2a7e50dfca076d2b505d35f3cbc50a0568b`
- Runtime test return code: `0`
- Batch return code: `0`
- Worktree after execution: clean

Assessed runtime source SHA-256 values:

| Runtime source | SHA-256 |
|---|---|
| `onyx/server/query_and_chat/models.py` | `adfb0aeda7c2b0cb74f89b3c439a081fdf52d6a6d82d40c620d381385155b338` |
| `onyx/tools/tool_constructor.py` | `ab2a9593634ff5899c6f40d00c5cf7a31e2b0005641cf315268d7744848a539c` |
| `onyx/tools/tool_implementations/mcp/mcp_tool.py` | `682e94322c18990d0499ef71c47e7f7998fa1a96b86a075da4414e6bb8377cbb` |
| `onyx/server/features/mcp/credentials.py` | `3a6858231bf922843080a344910b24e13e5cb1ceabe6e0cced6487e54cb1e745` |

## Runtime observations

Controls that behaved as intended:

- request model accepted the bounded synthetic `mcp_headers` fixture;
- managed `Authorization` overrode a colliding caller value;
- a managed non-authorization header overrode a colliding caller value;
- caller `Host` override was filtered;
- passthrough OAuth credentials overrode caller authorization;
- a dead OAuth grant could not be bypassed with caller authorization;
- the receiver was called only on loopback and stayed within its request bound;
- the transcript recorded `RAW_HEADER_VALUES_EMITTED=NO`;
- the loopback receiver stopped successfully.

Policy-gap observations:

- a non-colliding request header reached the MCP receiver;
- the synthetic privilege-signaling header
  `X-H9-16-Privilege: synthetic-elevated` reached the receiver while an
  administrator-managed `Authorization` header was attached to the same MCP call;
- when no managed API-token credential was available, caller-supplied
  `Authorization` allowed the call to proceed and reached the receiver. The
  receiver did not validate that value as a credential, so downstream acceptance
  as authentication remains unproven.

Key markers:

```text
MANAGED_AUTHORIZATION_PRECEDENCE=PASS
MANAGED_HEADER_COLLISION_PRECEDENCE=PASS
CALLER_HOST_OVERRIDE_BLOCKED=PASS
CALLER_NONCOLLIDING_HEADER_FORWARDED=YES
CALLER_SYNTHETIC_PRIVILEGE_HEADER_FORWARDED=YES
MISSING_MANAGED_CREDENTIAL_CALLER_AUTH_FORWARDED=YES
PASSTHROUGH_OAUTH_PRECEDENCE=PASS
DEAD_OAUTH_CALLER_BYPASS_BLOCKED=PASS
RECEIVER_REQUEST_COUNT_WITHIN_BOUND=PASS
EXTERNAL_REQUESTS=0
RAW_HEADER_VALUES_EMITTED=NO
RESULT=H9_16_RUNTIME_POLICY_GAP_REPRODUCED
LOOPBACK_RECEIVER_STOPPED=YES
```

## Source-backed cause

The request model accepts an arbitrary `dict[str, str]` as `mcp_headers`. The chat
processing and tool-construction path forwards that dictionary into `MCPTool`.
At execution, `MCPTool.run` removes globally denylisted names, then merges the
remaining caller headers with resolved managed credential headers. Managed values
win case-insensitive collisions, but non-colliding caller headers remain. The same
path explicitly permits extra request headers to stand in when credentials are
missing, except for a dead OAuth grant.

The working controls therefore prevent direct collision-based replacement of
managed authentication, but they do not enforce a server-specific allowlist or an
explicit opt-in for delegated request headers.

## Disposition

`P9-H16-01`: **FAIL under SR-H9-16 — ACTION 9.11 REQUIRED**

The demonstrated property is broader than an authorization-header override:
arbitrary non-colliding caller headers can cross the Onyx-to-MCP trust boundary.
Real impact is conditional on the downstream MCP server interpreting such a header
as identity, role, tenant, routing, or privilege information. No external MCP
server and no production target were tested, so that impact remains unconfirmed.

## Remediation requirement for the hardened fork

Before implementation, Action 9.11 must record the intended delegated-header
contract. The security-preserving design is:

1. deny request-supplied MCP headers by default for each server;
2. require an administrator-controlled, server-specific case-insensitive allowlist;
3. require explicit opt-in before caller `Authorization` may replace missing
   per-user API-token credentials;
4. never permit `Host`, hop-by-hop headers, or managed-header collisions;
5. keep managed credentials authoritative;
6. regression-test ADMIN, PER_USER API token, passthrough OAuth, live OAuth,
   missing-credential, collision, case-variant, and denylisted-header paths.

## Safety and cleanup

- synthetic values only;
- loopback receiver only;
- no external or production system;
- bounded sequential execution;
- no LLM invocation;
- no database mutation;
- temporary runner removed after successful execution;
- temporary container copy removed by the cleanup trap;
- repository remained clean at the end of the reproduction.

## Result

**H9-16_RUNTIME_POLICY_GAP_CONFIRMED_RECOVERED_EVIDENCE**
