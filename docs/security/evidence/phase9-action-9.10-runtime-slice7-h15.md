# Phase 9 Action 9.10 — Runtime Slice 7: H9-15

## Status

**RUNTIME BEHAVIOR REPRODUCED — POLICY REVIEW REQUIRED**

Hypothesis:

`H9-15 — Agent access revocation may not invalidate an existing chat-session capability`

No vulnerability classification is assigned by this evidence record alone.

## Assessed baseline

- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Runtime HEAD: `8e179134b89afa51e6cba97f32a86fb24d90d91f`
- Environment: authorized local Onyx laboratory
- Identities/data: synthetic only
- Network boundary: loopback only
- External target execution: none intended
- Tool invocation in the H9-15B2 execution slice: none

## Evidence-provenance note

The original temporary H9-15 runtime logs and runner were no longer present
when final repository preservation was attempted.

This Markdown record is therefore a **recovered evidence summary**, reconstructed
from the previously captured terminal execution transcript.

It must not be represented as the original immutable runtime log.

The preserved execution transcript recorded the H9-15B2R2 runner SHA-256 as:

`7796149cde3ca06c6ba8955a0d2210c608464ef4bdd318227aff0f1415895d8b`

The later preservation-preflight script remained independently available with SHA-256:

`e801122e26c088f0792dcda9e05a237f4f9916e06d04dedb8e29990f9cc1f794`

## H9-15A — revocation/session-layer verification

Controlled sequence:

1. synthetic Alice created a private persona;
2. Alice shared the persona with synthetic Bob;
3. Bob successfully created a session before revocation;
4. Alice revoked Bob's persona access;
5. Bob attempted a new session using the revoked persona;
6. Bob attempted to access the previously created session;
7. runtime authorization state and source provenance were inspected;
8. synthetic fixtures were removed.

Observed facts:

- `BOB_ACCESS_BEFORE_REVOKE=YES`
- `CREATE_BEFORE_REVOKE_HTTP=200`
- `SESSION_CREATED_BEFORE_REVOKE=YES`
- `BOB_ACCESS_AFTER_REVOKE=NO`
- `CREATE_AFTER_REVOKE_HTTP=403`
- `NEW_SESSION_AFTER_REVOKE=DENIED`
- `NEW_SESSION_REVOCATION_CONTROL=PASS`
- `EXISTING_SESSION_GET_HTTP=200`
- `EXISTING_SESSION_METADATA=ACCESSIBLE_AFTER_REVOKE`
- `CURRENT_PERSONA_ACCESS=NO`
- `EXISTING_SESSION_RUNTIME_LOAD=ALLOWED`
- `EXISTING_SESSION_PERSONA_MATCH=YES`
- `BUILD_CHAT_TURN_SESSION_LOADS=2`
- `BUILD_CHAT_TURN_PERSONA_RECHECKS=0`
- `EXISTING_SESSION_PERSONA_RECHECK=NO`
- `RESULT=H15A_EXISTING_SESSION_PERSISTENCE_VERIFIED`
- `FIXTURE_CLEANUP=PASS`

### P9-H15-01 disposition

**PASS**

After persona-share revocation, Bob's attempt to create a new chat session using
the revoked persona was denied with HTTP `403`.

This demonstrates that the new-session authorization control observed in the
assessed runtime enforced the revocation.

## H9-15B2R2 — existing-session core execution verification

A second bounded slice tested whether the already-created session could still
perform core message processing after persona access had been revoked.

Source/isolation gates recorded:

- `CHILD_INTEGRATION_TESTS_MODE=TRUE`
- `LOOPBACK_TCP_PREFLIGHT=PASS`
- `HTTP_HANDLER_CORE_CALLS=2`
- `HTTP_HANDLER_PERSONA_RECHECKS=0`
- `SOURCE_PROVENANCE=PASS`
- `RESIDUAL_FIXTURE_GATE=PASS`

Positive control:

- `BOB_ACCESS_BEFORE_REVOKE=YES`
- `PERSONA_TOOL_COUNT=0`
- `CREATE_SESSION_HTTP=200`
- `PRE_REVOKE_CORE_EXECUTION=PASS`
- synthetic/mock LLM response used
- no persistent synthetic LLM provider created

After revocation:

- `BOB_ACCESS_AFTER_REVOKE=NO`
- `POST_REVOKE_EXCEPTION_TYPE=NONE`
- `POST_REVOKE_DENIAL_EXCEPTION=NO`
- `POST_REVOKE_PACKET_COUNT=15`
- `POST_REVOKE_ERROR_PACKET=NO`
- `POST_REVOKE_ERROR_STATUS_CODES=NONE`
- `POST_REVOKE_MESSAGE_DELTA=2`
- `POST_REVOKE_MARKER_PERSISTED=YES`
- `POST_REVOKE_TOTAL_SYNTHETIC_LLM_RESOLUTIONS=2`

Decision:

- `SECURE_EXPECTATION=DENY_POST_REVOKE_EXECUTION`
- `H15B2_DISPOSITION=REVIEW_REQUIRED`
- `EXISTING_SESSION_EXECUTION=PERSISTS_AFTER_REVOKE`
- `RESULT=H15B2_EXISTING_SESSION_EXECUTION_PERSISTENCE_VERIFIED`

Safety/cleanup observations:

- `HTTP_REQUESTS_SENT=2`
- `LOOPBACK_TCP_PROBES=1`
- `HTTP_TARGET=LOOPBACK_ONLY`
- `HTTP_CONCURRENCY=1`
- `REQUEST_FILE_BYTES=0`
- `CORE_EXECUTION_CONCURRENCY=1`
- `MOCK_LLM_RESPONSE_USED=YES`
- `ALLOWED_TOOL_IDS=EMPTY`
- `EXTERNAL_REQUESTS_INTENDED=0`
- non-local network attempts were blocked by the runtime guard
- `CORE_NETWORK_GUARD_ENABLED=YES`
- `RUNNING_API_CONFIGURATION_CHANGED=NO`
- `SYNTHETIC_DATA_ONLY=YES`
- `FIXTURE_CLEANUP=PASS`

## P9-H15-02 disposition

**REVIEW**

The runtime evidence establishes a concrete distinction:

- persona authorization was revoked;
- new-session creation was denied;
- the previously owned chat session remained loadable;
- that existing session continued core message execution after revocation;
- the assessed path did not perform a fresh persona-access check;
- this particular execution slice used no persona tools.

This establishes **post-revocation existing-session capability persistence** for
core chat processing.

It does **not** by itself establish that a revoked privileged tool, credential,
knowledge source, or external side effect remained executable, because the B2
fixture deliberately used an empty tool set.

## Security interpretation

The observed behavior is security-relevant because authorization changes and
session capabilities have different lifetimes in the assessed path.

Classification depends on the intended product revocation contract.

If persona-share revocation is intended to take effect immediately for active
sessions, the observed behavior is a candidate authorization-control gap and
should proceed to Action 9.11 for root-cause analysis and remediation.

If the documented product contract deliberately allows already-created sessions
to retain some capability, the permitted residual capabilities must be explicitly
defined and tested, particularly tools, delegated credentials, files, knowledge
sources and other privileged agent resources.

Existing-session continuation alone is therefore not labeled a vulnerability in
this record.

## Root-cause direction

Static and runtime provenance are consistent with the previously recorded H9-15
hypothesis:

- new-session creation evaluates current persona access;
- an existing chat session can be loaded based on session ownership;
- the observed existing-session message path did not perform an equivalent fresh
  persona-access decision before core execution.

Required policy decision:

**Is persona-share revocation immediate for existing sessions, or are existing
sessions intentionally session-pinned?**

If immediate revocation is required, remediation should revalidate persona
usability or reconstruct a currently authorized capability set before each turn.

## Completion state

- P9-H15-01: **PASS**
- P9-H15-02: **REVIEW**
- H9-15 runtime behavior: **REPRODUCED**
- vulnerability classification: **NOT YET ASSIGNED**
- product-policy decision: **REQUIRED**
- Action 9.10: **IN PROGRESS**
- Phase 9 completion remains **64.3%** pending the broader Action 9.10 completion gate.

## Evidence limitation

Because the original temporary runtime artifact disappeared before repository
preservation, this record has weaker provenance than an evidence file committed
directly from the original runtime output.

That limitation is explicitly retained rather than silently reconstructing an
"original" log.
