# Phase 9 Action 9.11 — H9-16 Runtime Remediation Retest

## Status

**PASS — H9-16 MCP request-header trust-policy remediation verified.**

## Assessed state

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Remediation HEAD: `12e128031f490182d3fde6b2da13aa0f5c7bc9ac`
- Runtime: isolated container with network mode `none`
- Receiver: ephemeral loopback MCP service
- Data and credentials: synthetic only
- External requests: `0`
- LLM invocations: `0`
- Database mutations: `0`
- Live API mutations: `0`
- Maximum duration: `55` seconds
- Receiver request ceiling: `40`
- Observed receiver requests: `30`

## Integrity

| Item | SHA-256 or size |
|---|---|
| Runtime runner | `fd2ff1264c542e612af8b23b10a47a7f3fcae77484452b5325c0520eb58474ff` |
| Runtime log | `499dedd2d1d208df6c174d240829978a05c5d912d5539c50a227c8788fd4dca5` |
| Runtime log bytes | `3890` |
| `backend/onyx/server/features/mcp/models.py` | `c5841337a7c4f3f314e25513054497e82c8c031a532da579987af044d06c7e1d` |
| `backend/onyx/tools/tool_implementations/mcp/mcp_tool.py` | `5c26b93f38d023670c4060c4abdd53938d66e6f80ff919df088150ccc0f18e9b` |
| `backend/tests/unit/onyx/tools/test_mcp_request_header_policy.py` | `ee181a30670f1ddcbadcb0b53e21e2830ddb8ca24620c7480be62f4ea1bf55d7` |

The repository does not store the temporary runtime log. The checkpoint verified
its size, hash, required markers and raw-value guard before this evidence commit.

## Verified controls

| Control | Result |
|---|---|
| Unlisted request headers | Filtered |
| Managed authorization collision | Managed value retained |
| Managed custom-header collision | Managed value retained |
| Host and hop-by-hop override | Blocked |
| Explicit per-user API-token delegation | Preserved |
| Missing administrator template | Failed closed |
| Passthrough OAuth precedence | Preserved |
| Live OAuth precedence | Preserved |
| Dead OAuth caller bypass | Blocked |
| No-auth caller identity header | Filtered |
| Raw synthetic header values in log | Not emitted |

## Disposition

`P9-H16-01`: **REMEDIATED IN THE HARDENED FORK**

Request-supplied MCP headers now default to deny. Only header names in the
administrator-controlled server template can pass. Managed credentials keep final
case-insensitive collision precedence. Missing credentials can use request headers
only for explicit per-user API-token delegation with a complete template.

## Residual risk

- An administrator can still configure a high-impact delegated header. Review each
  server template against the downstream MCP server's authorization model.
- This retest exercised the MCP execution boundary. It did not invoke a browser,
  an LLM or a production MCP server.
- Downstream authorization semantics remain deployment-specific.

## Progress

- H9-16 closure checkpoints: `4 / 4` (`100%`).
- Action 9.10 remains in progress.
- Action 9.11 remains in progress because H9-12 and the H9-14 API retest remain.
- Phase 9 completed actions: `9 / 14` (`64.3%`).

## Result

**H9-16_RUNTIME_REMEDIATION_VERIFIED**
