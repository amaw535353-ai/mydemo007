# Phase 8 Action 8.13 - P1 Executable Authorization Test Pack

## Status

**PREPARED - NOT EXECUTED**

## Purpose

Reduce the broad Phase 8 route inventory to the first bounded authorization tests to execute once an approved local Onyx runtime is positively identified.

P1 fixtures selected: **24**

| ID | Score | Method | Path candidate | Function | First verification | Reasons | Source |
|---|---:|---|---|---|---|---|---|
| P8-001 | 88 | POST | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/sync-groups | sync_cc_pair_groups | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, group, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/ee/onyx/server/documents/cc_pair.py:135 |
| P8-002 | 85 | PUT | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/status | update_cc_pair_status | owner update ALLOW -> foreign update DENY | admin, connector, credential, document, path-object-reference, permission, session, state-changing, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:470 |
| P8-003 | 83 | GET | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id} | get_cc_pair_full_info | owner ALLOW -> foreign user DENY -> cross-tenant DENY | admin, connector, credential, document, group, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:338 |
| P8-004 | 82 | POST | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/sync-permissions | sync_cc_pair | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/ee/onyx/server/documents/cc_pair.py:56 |
| P8-005 | 82 | POST | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/prune | prune_cc_pair | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:685 |
| P8-006 | 82 | POST | <unresolved-parent-prefix>/manage/admin/credential/{credential_id}/capability-check | trigger_capability_check | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/credential_capabilities.py:134 |
| P8-007 | 80 | POST | <unresolved-parent-prefix>/manage/admin/connector/indexing-status | get_connector_indexing_status | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, group, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:966 |
| P8-008 | 77 | POST | <unresolved-parent-prefix>/manage/admin/connector/{connector_id}/files/update | update_connector_files | anonymous/ordinary/privileged authorization matrix | admin, connector, document, file, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:559 |
| P8-009 | 77 | POST | <unresolved-parent-prefix>/manage/admin/deletion-attempt | create_deletion_attempt_for_connector_id | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, file, group, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/manage/administrative.py:150 |
| P8-010 | 75 | PUT | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/name | update_cc_pair_name | owner update ALLOW -> foreign update DENY | admin, connector, credential, document, path-object-reference, permission, session, state-changing, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:577 |
| P8-011 | 75 | PUT | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/property | update_cc_pair_property | owner update ALLOW -> foreign update DENY | admin, connector, credential, document, path-object-reference, permission, session, state-changing, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:611 |
| P8-012 | 75 | PUT | <unresolved-parent-prefix>/manage/connector/{connector_id}/credential/{credential_id} | associate_credential_to_connector | owner update ALLOW -> foreign update DENY | connector, credential, document, path-object-reference, permission, session, state-changing, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:797 |
| P8-013 | 75 | DELETE | <unresolved-parent-prefix>/manage/admin/document-set/{document_set_id} | delete_document_set | owner delete ALLOW -> foreign delete DENY | admin, destructive, document, group, path-object-reference, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/features/document_set/api.py:182 |
| P8-014 | 74 | POST | <unresolved-parent-prefix>/manage/admin/connector-with-mock-credential | create_connector_with_mock_credential | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:1499 |
| P8-015 | 74 | POST | <unresolved-parent-prefix>/manage/admin/connector/run-once | connector_run_once | anonymous/ordinary/privileged authorization matrix | admin, connector, credential, document, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:1664 |
| P8-016 | 73 | GET | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/sync-groups | get_cc_pair_latest_group_sync | owner ALLOW -> foreign user DENY -> cross-tenant DENY | admin, connector, credential, document, group, path-object-reference, permission, session, unresolved-parent-prefix, user, visible-security-signal | backend/ee/onyx/server/documents/cc_pair.py:112 |
| P8-017 | 73 | PATCH | <unresolved-parent-prefix>/manage/admin/user-group/{user_group_id}/document-sets | update_group_document_sets | owner update ALLOW -> foreign update DENY | admin, document, group, path-object-reference, permission, session, state-changing, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/ee/onyx/server/user_group/api.py:527 |
| P8-018 | 72 | PUT | <unresolved-parent-prefix>/manage/admin/credential/private-key/{credential_id} | update_credential_private_key | owner update ALLOW -> foreign update DENY | admin, credential, document, file, path-object-reference, permission, session, state-changing, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/credential.py:329 |
| P8-019 | 69 | DELETE | <unresolved-parent-prefix>/manage/admin/credential/{credential_id} | delete_credential_by_id_admin | owner delete ALLOW -> foreign delete DENY | admin, credential, destructive, document, path-object-reference, permission, session, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/credential.py:103 |
| P8-020 | 69 | POST | <unresolved-parent-prefix>/onyx-api/ingestion | upsert_ingestion_doc | anonymous/ordinary/privileged authorization matrix | connector, credential, document, file, permission, session, tenant, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/onyx_api/ingestion.py:102 |
| P8-021 | 67 | GET | <unresolved-parent-prefix>/manage/admin/cc-pair/{cc_pair_id}/sync-permissions | get_cc_pair_latest_sync | owner ALLOW -> foreign user DENY -> cross-tenant DENY | admin, connector, credential, document, path-object-reference, permission, session, unresolved-parent-prefix, user, visible-security-signal | backend/ee/onyx/server/documents/cc_pair.py:33 |
| P8-022 | 67 | DELETE | <unresolved-parent-prefix>/manage/connector/{connector_id}/credential/{credential_id} | dissociate_credential_from_connector | owner delete ALLOW -> foreign delete DENY | connector, credential, destructive, document, path-object-reference, permission, session, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/cc_pair.py:925 |
| P8-023 | 67 | PUT | <unresolved-parent-prefix>/manage/admin/connector/google-drive/service-account-credential | upsert_service_account_credential | owner update ALLOW -> foreign update DENY | admin, connector, credential, document, permission, session, state-changing, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:183 |
| P8-024 | 67 | PUT | <unresolved-parent-prefix>/manage/admin/connector/gmail/service-account-credential | upsert_gmail_service_account_credential | owner update ALLOW -> foreign update DENY | admin, connector, credential, document, permission, session, state-changing, unresolved-parent-prefix, user, visible-security-signal | backend/onyx/server/documents/connector.py:203 |

## Mandatory runtime preconditions

Before any fixture is executed:

1. positively identify the local Onyx HTTP endpoint;
2. verify the target is loopback/local and authorized;
3. verify the pinned source/runtime relationship;
4. establish synthetic Alice, Bob and cross-tenant identities;
5. create synthetic owned resources;
6. preserve explicit ALLOW/DENY expectations;
7. enforce <=100 requests, <=10 concurrency and <=60 seconds;
8. preserve raw request/response evidence;
9. stop on external traffic, real data or real credentials.

## Result interpretation

A failed expectation is a candidate finding only after it is reproduced and alternative explanations such as route mismatch, fixture error or incorrect runtime identity are excluded.

# Result

**P1 EXECUTABLE TEST PACK PREPARED - EXECUTION BLOCKED UNTIL APPROVED LOCAL RUNTIME EXISTS**
