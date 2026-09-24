# Phase 12 — Action 12.8 Connector, Tool, MCP and Provider Egress

## Objective

Identify privacy-sensitive outbound boundaries without contacting real external
providers.

## Verified controls

Custom-tool execution:

- validates outbound URLs through the shared outbound policy;
- does not automatically follow server-controlled redirects.

MCP execution:

- filters caller-provided request headers;
- merges filtered request headers with managed credentials;
- uses the MCP SSRF-aware HTTP client factory;
- applies a bounded tool-call timeout.

LLM provider construction explicitly carries configured provider identity,
API base and provider credential information.

## Privacy interpretation

External model providers, MCP servers, connectors and custom tools are explicit
data-egress boundaries.

This action does not treat intended configured provider use as exfiltration.

## Finding

**NO UNEXPECTED EXTERNAL EGRESS CONFIRMED**

No real provider, MCP server or connector was contacted.

## Evidence

Results:

`docs/security/evidence/phase12-action-12.8-results.txt`

SHA-256:

`9589d76ce5c4b734577e6827fadfec15074608c2df0cc7315fa0f4eb11a95ce9`

Source trace:

`docs/security/evidence/phase12-action-12.8-source-trace.txt`

SHA-256:

`c85ff6490f2a513f70d13143d3788fe72d485b2a25284b88101fba88507319c0`

Test:

`backend/tests/unit/onyx/privacy/test_phase12_external_egress_boundaries.py`

## Completion

**ACTION 12.8: COMPLETE**

**RESULT=PHASE_12_ACTION_12_8_PASS**
