# Phase 9 — Action 9.10 — H9-13 ACL-Bypass Caller Provenance

## Security question

Can a production caller cause search execution with `bypass_acl=True`, thereby suppressing document ACL filtering?

## Authorization sink

The search pipeline treats `bypass_acl` as security-sensitive.

When `bypass_acl=True`:

- user ACL filters are not constructed;
- document-set permission validation is skipped in affected paths;
- `SearchTool` propagates the value into `ChunkSearchRequest` and the search pipeline.

Therefore a reachable untrusted `True` source would require further security testing.

## Production provenance result

- All identified function defaults are `False`.
- Search API constructs `SearchTool(..., bypass_acl=False)`.
- Slack regular-answer handling calls `handle_stream_message_objects(..., bypass_acl=False)`.
- Standard chat backend callers omit the argument and receive the default `False`.
- Evaluation callers likewise receive the default `False`.
- Multi-model chat receives the default `False`.
- No production literal `bypass_acl=True` assignment or call was identified.
- `PRODUCTION_LITERAL_TRUE_COUNT=0`.

## Positional/reachability census

- Relevant production call sites examined: **10**.
- Suspicious explicit-true, positional-true, or variable-positional callers: **0**.
- `SUSPICIOUS_CALL_COUNT=0`.
- No identified user request model exposes `bypass_acl` as request-controlled input.

## Classification

**H9-13 — PASS / NOT CURRENTLY REACHABLE FROM IDENTIFIED PRODUCTION CALLERS**

The ACL-bypass mechanism remains a privileged internal capability, but the reviewed production call graph does not currently provide a source that enables it.

No runtime exploitation test was performed because source and call-site provenance did not identify a reachable production `True` source.

## Future security invariant

Any future production caller that sets or propagates `bypass_acl=True` must receive explicit security review. Such a change can intentionally suppress document ACL filtering and document-set authorization checks.

Recommended review rule:

`bypass_acl=True` in production code requires a documented trusted-system justification, bounded identity context, negative authorization tests, and reviewer approval.

## Analysis artifacts

- Provenance analysis SHA-256: `20a5ca4472c4068d0f780fdc63137fb2ee933d0d96a70a699acff5b4b320d554`
- Call-site census SHA-256: `1f48b5aa3a80f00188c80c1f4687654e6ccf65811cd2f44cc139b36fd4f673a8`

- HTTP requests: 0
- External network requests: 0
- Repository source changes during analysis: 0
