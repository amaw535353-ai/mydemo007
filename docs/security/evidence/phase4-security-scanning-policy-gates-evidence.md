# Phase 4 Action 4.11 - Security Scanning & Policy Gates Evidence

## Provenance
- Branch: `security/phase-4-cloud-devsecops`
- Baseline HEAD: `2095c1dc7085f4bcf54dd2df73e905c3f1327a23`

## Observation boundary

**STATIC CANDIDATES ONLY. EXECUTION AND ENFORCEMENT ARE UNVERIFIED.**

## Scope

SAST, dependency, container, IaC and secret scanning plus severity thresholds, failure behavior and security policy gates.

## Static results

- Candidate files: **60**
- Matching lines: **310**

## Representative candidates

- `backend/alembic/versions/f8048443da9e_add_notification_severity.py`
- `backend/ee/onyx/utils/license_notifications.py`
- `backend/onyx/background/error_logging.py`
- `backend/onyx/connectors/capability_checks/models.py`
- `backend/onyx/connectors/slack/capability_checks.py`
- `backend/onyx/db/connector_alerts.py`
- `backend/onyx/db/models.py`
- `backend/onyx/db/notification.py`
- `backend/onyx/server/features/build/scheduled_tasks/api.py`
- `backend/onyx/server/features/notifications/api.py`
- `backend/onyx/server/features/notifications/models.py`
- `backend/onyx/server/features/notifications/utils.py`
- `backend/onyx/skills/builtin/pptx/scripts/lint.py`
- `backend/tests/daily/connectors/salesforce/test_salesforce_data.json`
- `backend/tests/evals/connector_filter_eval/README.md`
- `backend/tests/evals/connector_filter_eval/test_filter_extraction_regression.py`
- `backend/tests/external_dependency_unit/db/test_notification.py`
- `backend/tests/unit/onyx/connectors/capability_checks/test_verdict_aggregation.py`
- `backend/tests/unit/onyx/connectors/slack/test_slack_capability_checks.py`
- `backend/tests/unit/onyx/skills/test_pptx_lint.py`

## Interpretation

Static matches are review targets, not proof of runtime enforcement.

## Safety

- No cloud resource created.
- No infrastructure provisioned.
- No CI/CD workflow triggered.
- No external scanner executed.
- No real credential used.
- No production telemetry accessed.
- No paid service used.

## Result

Action 4.11 static mapping result: **PASS**
