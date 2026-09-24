# Phase 11 — Action 11.4 MCP Authentication, Credential and SSRF Boundaries

## Verified controls

- protocol-sensitive MCP headers are denied;
- request MCP headers are restricted by the administrator template;
- managed credentials override caller collisions;
- caller credential fallback is limited to explicit per-user API-token mode;
- MCP clients use the guarded HTTP transport;
- redirects pass through the guarded transport;
- sandbox MCP credential injection rechecks user access;
- ungated non-plumbing MCP calls fail closed before credentialed forwarding.

## Finding classification

**NO MCP AUTHORIZATION OR CREDENTIAL BYPASS CONFIRMED**

## Evidence

Results:

`docs/security/evidence/phase11-action-11.4-mcp-security-results.txt`

SHA-256:

`468988ffd2bc3156e922b7003addd47e5b707387d5ca029435d3ec0762a045fb`

Source trace:

`docs/security/evidence/phase11-action-11.4-mcp-security-source-trace.txt`

SHA-256:

`cf296735dad7636eb71a87cd69b219c2f7e66c97a91da034e63aaaffbaecb256`

Regression:

`backend/tests/unit/onyx/server/features/mcp/test_phase11_mcp_security_boundaries.py`

## Completion

**ACTION 11.4: COMPLETE**

**RESULT=PHASE_11_ACTION_11_4_PASS**
