# Phase 12 — Action 12.9 Conversation, File and Memory Retention / Deletion

## Objective

Verify privacy-relevant retention and deletion semantics for conversation
content, files, memory and intentionally retained usage metadata.

## Verified deletion paths

Static/property review confirms:

- chat hard-deletion paths remove message records;
- file-store code contains physical object-deletion and FileRecord cleanup paths;
- memory rows use a user deletion cascade;
- chat sessions use a user deletion cascade.

## Action 12.5 retention exception

`UserUsage.user_id` uses:

`ON DELETE SET NULL`

Therefore UserUsage rows may intentionally survive deletion of the associated
user record while losing that direct foreign-key association.

## Retained schema classification

The current UserUsage schema contains usage/accounting fields including:

- model;
- flow;
- provider;
- input-token count;
- output-token count;
- cache-read token count;
- cache-creation token count;
- cost;
- usage window;
- timestamps.

The reviewed UserUsage class does not contain direct:

- chat-message content;
- prompt content;
- memory text;
- file content.

At this evidence level the retained rows are therefore classified as:

**INTENTIONAL POST-DELETE ACCOUNTING METADATA RETENTION**

This action does not claim that all retained metadata is anonymous in every
deployment or business context.

## Important limitation

Static/schema review does not prove deletion from:

- backups;
- external provider retention;
- every derived/indexed representation;
- production replicas;
- production telemetry stores.

Those broader runtime claims are not made here.

Bounded synthetic privacy runtime remains Action 12.13.

## Finding

**NO DELETION FAILURE CONFIRMED BY THIS ACTION**

## Evidence

Results:

`docs/security/evidence/phase12-action-12.9-results.txt`

SHA-256:

`bc57667c2f0b549c0bc41151233265ca2014b68af17a6c4972e9f0e7b4674aa5`

Source trace:

`docs/security/evidence/phase12-action-12.9-source-trace.txt`

SHA-256:

`54b481a96e79a1facbe915c28e81622f88302f7dd234de22f7279eb696e38f9d`

Test:

`backend/tests/unit/onyx/privacy/test_phase12_retention_deletion.py`

## Completion

**ACTION 12.9: COMPLETE**

**USER_USAGE_POST_DELETE_RETENTION=ACCOUNTING_METADATA_AT_SCHEMA_LEVEL**

**RESULT=PHASE_12_ACTION_12_9_PASS**
