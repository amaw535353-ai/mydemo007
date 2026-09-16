# Phase 8 TC8-007 Reproduction

## Classification

**REPRODUCIBLE_500_ROBUSTNESS_CANDIDATE**

## Runtime

- UTC: 2026-09-16T20:10:36Z
- Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Health: HTTP 200
- Attacker actor: Bob synthetic authenticated user
- Target: Alice synthetic private chat session

## Results

| Variant | HTTP |
|---|---:|
| No extra parameters | 403 |
| Unknown `foo=bar` | 403 |
| `user_id=<Alice>` | 403 |
| `tenant_id=public` | 403 |
| `tenant_id=default` | 500 |
| `user_id=<Alice>&tenant_id=default` | 500 |

## Integrity control

- Final Bob-to-Alice foreign read: HTTP 403
- Expected: 403

## Interpretation

The endpoint's documented runtime parameters do not include caller-controlled
`user_id` or `tenant_id` authorization selectors.

Any reproducible HTTP 500 is treated as a robustness candidate requiring
root-cause analysis. It is not classified as an authorization vulnerability
unless unauthorized access or state change is independently demonstrated.

## Safety

- Authorized Codespace only
- Synthetic identities/resources only
- Read-only requests
- Sequential requests
- No production data or credentials
