# Phase 10 — Action 10.10 Indirect Prompt Injection Through Retrieved Content

## Objective

Assess instruction integrity when attacker-controlled or otherwise untrusted
retrieved document content is supplied to LLM-facing search stages.

The tests use deterministic harmless synthetic injection markers.

## Threat linkage

Phase 7:

**T7-07-03 — Indirect prompt injection from retrieved content**

## Baseline

Synthetic instruction-like retrieved content reached:

1. document-selection prompts;
2. context-expansion prompts;
3. final internal-search LLM context.

The baseline surfaces lacked a strong explicit instruction/data boundary.

**ARCHITECTURAL PROMPT-INJECTION EXPOSURE: CONFIRMED**

This does not prove that a particular model would obey the malicious content.

**MODEL INSTRUCTION-FOLLOWING EXPLOIT: NOT CLAIMED**

## Hardening

Explicit retrieved-content trust boundaries were added to:

- system-level search/tool guidance;
- document-selection prompts;
- context-expansion prompts;
- final internal-search LLM-facing payloads.

Retrieved content is explicitly classified as:

- untrusted data;
- evidence rather than instructions;
- unable to authorize tool calls;
- unable to override higher-priority instructions;
- unable to authorize secret disclosure.

## Final context structure

The internal-search payload now places:

`security_notice`

before:

`results`

A corrected structural test verifies this using source positions rather than
lexicographic string comparison.

## JSON integrity

A synthetic JSON-shaped injection payload remained serialized inside document
content.

It did not replace the trusted top-level security notice.

**PASS**

## Security interpretation

Prompt-level instruction hierarchy reduces indirect prompt-injection risk but
does not guarantee immunity for every model.

Later dynamic red-team testing should evaluate actual model behavior,
tool-enabled workflows and multi-turn injection persistence.

## H10-04

**PROMPT-BOUNDARY HARDENING: PASS**

## Evidence

Results:

`docs/security/evidence/phase10-action-10.10-prompt-injection-results.txt`

SHA-256:

`b3e668797a55c17a71651e9d3eadf48f33cd72b62349784053da0dcdcf056418`

Source trace:

`docs/security/evidence/phase10-action-10.10-prompt-injection-source-trace.txt`

SHA-256:

`e6b0426ac5a6bde69ac502f4dbbf62fb5337cd27361fe854c8c3be8bd25c5e12`

Regression:

`backend/tests/unit/onyx/prompts/test_retrieved_content_security_boundary.py`

## Safety

- synthetic attack marker: **YES**
- LLM calls: **0**
- tool actions triggered: **0**
- HTTP requests: **0**
- external network requests: **0**
- production targets: **0**
- real data/credentials: **0**

## Completion

**ACTION 10.10: COMPLETE**

Next:

**Action 10.11 — RAG poisoning and provenance**
