# Phase 10 — Action 10.9 Context Assembly and Citation Authorization

## Objective

Verify that content entering final LLM context and citation mappings remains
inside the authorization boundary after search-result context expansion.

## Reviewed flow

The active flow is:

authorized retrieval
→ post-query permission censoring
→ section selection
→ adjacent/full-document context expansion
→ context merge
→ LLM-facing document construction
→ citation mapping

## H10-03 — post-expansion permission-censoring gap

### Baseline

Initial search results already passed through the post-query censoring boundary.

Context expansion then performed additional direct ID-based chunk retrieval.

Those newly retrieved adjacent chunks were not passed through post-query
censoring before being added to the expanded section.

A bounded synthetic property test demonstrated that an unauthorized adjacent
content sentinel could enter the expanded section.

This is particularly relevant to permission models where access is finer than
the document itself, such as object/field-aware post-query censoring.

**H10-03 BASELINE: CONFIRMED**

This action does not claim a public production exploit.

### Remediation

A mandatory post-expansion re-censoring boundary was added.

All expanded chunks are now:

1. deduplicated;
2. submitted to the same post-query censoring implementation;
3. mapped back to their section;
4. dropped if the original center chunk no longer survives authorization;
5. rebuilt using only censored chunks.

The resulting safe sections are then used for:

- overlap merging;
- LLM-facing context;
- citation mapping.

### Regression

Verified:

- unauthorized adjacent chunk removed: **PASS**
- removed center chunk drops section: **PASS**
- LLM context contains only re-censored content: **PASS**
- a fully removed section creates no citation mapping: **PASS**

**H10-03: REMEDIATED**

## Citation authorization

Citation IDs are generated from the final sections supplied to
`convert_inference_sections_to_llm_string`.

The citation processor subsequently resolves citation IDs only against
SearchDocs in the tool response.

The new re-censor boundary executes before final section merge and context /
citation construction.

**PASS**

## Tenant boundary

Action 10.6 already established tenant isolation at the index layer.

This action does not replace that control.

Its purpose is specifically to restore fine-grained permission censoring after
additional context is fetched.

## Finding classification

**CONTEXT-EXPANSION POST-QUERY CENSORING BYPASS CONFIRMED IN A SYNTHETIC PROPERTY TEST AND REMEDIATED.**

**PUBLIC END-TO-END EXPLOIT: NOT CLAIMED.**

## Evidence

Results:

`docs/security/evidence/phase10-action-10.9-context-assembly-results.txt`

SHA-256:

`b2d604eec2f2db237123fbb08dba9ebb6c70a96ae52f4d3a1a55c5dd2130d283`

Source trace:

`docs/security/evidence/phase10-action-10.9-context-assembly-source-trace.txt`

SHA-256:

`db30b578b904a813ad5b98cb5bd5e166ff419e20e1beef324b889c2e99b674cf`

Regression:

`backend/tests/unit/onyx/tools/tool_implementations/search/test_context_assembly_authorization.py`

## Safety

- synthetic content only: **YES**
- synthetic user only: **YES**
- database mutations: **0**
- HTTP requests: **0**
- external network requests: **0**
- production targets: **0**
- real credentials/data: **0**

## Completion

**ACTION 10.9: COMPLETE**

Next:

**Action 10.10 — indirect prompt injection through retrieved content**
