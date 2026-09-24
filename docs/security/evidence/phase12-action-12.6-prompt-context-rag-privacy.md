# Phase 12 — Action 12.6 Prompt, Context and RAG Privacy Leakage

## Objective

Trace privacy boundaries before retrieved or personalized information becomes
LLM-visible context.

## Verified boundaries

Static/property evidence confirms:

- retrieval ACLs are derived from the requesting user;
- user-selected document sets are permission checked;
- search filters carry ACL information;
- multi-tenant search carries the current tenant identifier;
- post-query censoring exists for sources requiring field-level filtering.

## Prompt privacy surface

System-prompt construction may intentionally include:

- user name;
- user email;
- user role;
- organization profile;
- preferences;
- persistent memories;
- organization/company context.

This is an explicit privacy-sensitive prompt surface.

Its existence is not itself classified as a leak because the information is
used intentionally for personalization.

Provider egress of this context is reviewed in Action 12.8.

## Finding

**NO UNAUTHORIZED RAG PRIVACY DISCLOSURE CONFIRMED BY THIS ACTION**

## Limitation

This action verifies source/property boundaries.

Cross-user negative testing remains Action 12.11 and bounded runtime remains
Action 12.13.

## Evidence

Results:

`docs/security/evidence/phase12-action-12.6-results.txt`

SHA-256:

`0c02b7af5061e0a6a2f6856e6e002bf7b8f591ad75fdf2c02a9f33650f47471e`

Source trace:

`docs/security/evidence/phase12-action-12.6-source-trace.txt`

SHA-256:

`98ec493a594917ffe2ab1241f3edc70b75236950a6fd5f611c3de9d43c38f54a`

Test:

`backend/tests/unit/onyx/privacy/test_phase12_prompt_rag_privacy_boundaries.py`

## Completion

**ACTION 12.6: COMPLETE**

**RESULT=PHASE_12_ACTION_12_6_PASS**
