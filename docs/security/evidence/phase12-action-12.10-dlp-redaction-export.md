# Phase 12 — Action 12.10 DLP, Redaction, Export and Download Controls

## Objective

Test targeted sensitive-value redaction and review authorization boundaries on
privacy-sensitive administrative exports.

## Functional redaction test

Synthetic sensitive values were passed through the application redaction
helper.

The functional test verifies removal of:

- synthetic tenant email;
- fake API token;
- overlapping synthetic secret values.

The minimum-length guard is also verified so ordinary very-short strings are
not indiscriminately replaced.

## Export authorization

Static review confirms that the reviewed:

- administrative log-export download;
- administrative usage-report export

require:

`FULL_ADMIN_PANEL_ACCESS`

## DLP evidence boundary

Onyx contains targeted redaction and masking controls.

This action does not claim that Onyx provides a universal enterprise DLP engine
across every data-storage and data-egress boundary.

## Finding

**NO REDACTION OR REVIEWED EXPORT-AUTHORIZATION BYPASS CONFIRMED**

## Evidence

Results:

`docs/security/evidence/phase12-action-12.10-results.txt`

SHA-256:

`8caa5ab265274242bbabfb38d9f788200eb72a7ac1a47fbe755b323d10161198`

Source trace:

`docs/security/evidence/phase12-action-12.10-source-trace.txt`

SHA-256:

`9009212def920317bf1bd5ad3d016fff99d38a6a7778ed065a5062e6b82268be`

Test:

`backend/tests/unit/onyx/privacy/test_phase12_dlp_redaction_export.py`

## Completion

**ACTION 12.10: COMPLETE**

**GENERAL_PURPOSE_DLP_ENGINE=NOT_CLAIMED**

**RESULT=PHASE_12_ACTION_12_10_PASS**
