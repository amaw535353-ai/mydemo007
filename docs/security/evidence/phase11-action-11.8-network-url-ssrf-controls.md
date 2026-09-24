# Phase 11 — Action 11.8 Network / URL / SSRF Controls

## H11-02 — custom-action outbound SSRF surface

### Baseline

Custom OpenAPI schema validation accepted a synthetic cloud-metadata URL.

The execution path then used the schema-derived URL through
`requests.request()`.

No network request was performed during reproduction.

### Mitigation

Custom actions now apply the same administrator-controlled outbound SSRF
protection model immediately before execution.

The policy preserves the project's intended behavior:

- VALIDATE levels block private/internal targets;
- ALLOW_PRIVATE_NETWORK permits explicitly trusted RFC1918 services while
  retaining stronger floors;
- DISABLED permits trusted local/loopback testing;
- cloud metadata/link-local remains blocked as an always-on floor.

Automatic redirects are disabled for custom actions so a credential-bearing
request cannot silently follow a server-controlled redirect to another origin.

## Residual risk

The generic requests path still contains a DNS-validation-to-connect timing
window.

Therefore H11-02 is classified:

**MITIGATED WITH RESIDUAL DNS TOCTOU RISK**

The stronger MCP transport performs validation at the transport layer; a future
custom-action transport could adopt equivalent IP pinning for arbitrary HTTP
methods.

## Other network controls

The Craft sandbox additionally performs destination checks at request and
connection setup.

## Evidence

Results:

`docs/security/evidence/phase11-action-11.8-network-ssrf-results.txt`

SHA-256:

`01efc95b718d65983012bba7186966ceeab55386ba30fc08558c2871d3f80a8e`

Source trace:

`docs/security/evidence/phase11-action-11.8-network-ssrf-source-trace.txt`

SHA-256:

`1989aae1e01593c47b90b9ffda66d8d5e79015596632f51385640309f3b26cf1`

Regression:

`backend/tests/unit/onyx/tools/tool_implementations/custom/test_phase11_custom_tool_ssrf.py`

## Completion

**ACTION 11.8: COMPLETE**

**H11-02: MITIGATED — RESIDUAL DNS TOCTOU DOCUMENTED**

**RESULT=PHASE_11_ACTION_11_8_PASS**
