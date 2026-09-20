# Phase 9 Action 9.11 — H9-14 Runtime Remediation Retest

## Status

**PASS — H9-14 foreign custom-action attachment remediation verified at the API boundary.**

## Assessed state

- Date: 2026-09-20
- Branch: `security/phase-9-identity-authorization-tenant-isolation`
- Assessed HEAD: `c7762ebec300b68af782ac51b7ce6b2078ac0ec3`
- Runtime: healthy rebuilt `onyx-api_server-1` container
- Network: API-container loopback only
- Data, identities and credentials: disposable synthetic fixtures only
- Maximum duration: `55` seconds
- Maximum HTTP requests: `4`
- Observed HTTP requests: `4`
- Maximum concurrency: `1`
- External requests: `0`
- LLM invocations: `0`
- Push performed: no

## Integrity

| Item | SHA-256, Git blob or size |
| --- | --- |
| Checkpoint helper | `42e44ba090c0a119ffdafab89064108203e333dce2bd1c3058fed0580a0632d7` |
| Runtime log | `c4a3d3fbb21ab4f856b251532b048e97f3697b1b89a3db4820af02a11ef7782f` |
| Runtime log bytes | `2979` |
| `backend/onyx/db/persona.py` SHA-256 | `5ed5083391531a19f456f498dd443b1e04400981c20da688da9340ce7351b12f` |
| `backend/onyx/db/persona.py` Git blob | `e16b4ffd38efc1c9258d8dfe7bb0486a87cffa88` |

The temporary runtime log is not committed. Before this evidence commit, the closeout
checkpoint verified its size, SHA-256, required result markers, absence of emitted raw
credential material, unchanged repository HEAD and clean worktree.

## Executed sequence

1. Created a disposable custom-action owner, scoped actor, foreign custom action and
   actor-owned persona.
2. Authenticated the scoped actor through the local mobile-session endpoint.
3. Performed an authenticated positive-control persona read.
4. Sent a persona update attempting to attach the other creator's custom action.
5. Verified denial and queried persistence state directly.
6. Logged out, revoked the session and removed every synthetic fixture row.

The custom action was never invoked, so no stored action header or delegated credential
was transmitted.

## HTTP observations

| Operation | Status | Sanitized evidence |
| --- | --- | --- |
| Synthetic mobile login | `200` | Token value not emitted |
| Positive-control persona read | `200` | `1009` bytes; SHA-256 `039b64afc9813a9734eceeac5bc32bee035e29fa03141915d60e5458a25f64b5` |
| Foreign custom-action attachment attempt | `403` | `122` bytes; SHA-256 `ff3b38123e8e02593da15110c8ee9b224bddb4dfd7e26c493721c89dba4652dd` |
| Synthetic mobile logout | `204` | Session revoked |

The denial response carried the standard error code `INSUFFICIENT_PERMISSIONS`.

## Persistence and cleanup verification

| Invariant | Result |
| --- | --- |
| Persona-to-action attachment count | `0` |
| Persona name unchanged | yes |
| Persona description unchanged | yes |
| Persona and action ownership intact | yes |
| Remaining synthetic fixture rows | `0` |
| Session revoked | yes |
| Worktree after execution | clean |
| Repository HEAD after execution | unchanged |

## Security disposition

`P9-H14-01`: **REMEDIATED IN THE HARDENED FORK**

New non-MCP custom-action attachments require creator or actions-administrator
authority. An unrelated scoped actor cannot attach another creator's action through
the API. Existing attachments remain preserved during ordinary persona edits, as
verified by the focused database regression.

## Additional runtime observation

The application emitted a warning that the laboratory object-storage service uses
well-known default credentials. H9-14 did not test object-storage reachability or
classify that separate configuration condition. These credentials are acceptable only
inside the isolated disposable laboratory and must be replaced before any production
deployment.

## Residual risk

- Actions administrators can intentionally attach another creator's action by policy.
- Existing foreign attachments are preserved for compatibility.
- The catalog may display an action that the attachment policy later rejects.
- This retest did not invoke a custom action or assess downstream action authorization.

## Progress

- H9-14 closure checkpoints: `4 / 4` (`100%`).
- Action 9.10 remains in progress while other matrix items await final dispositions.
- Action 9.11 remains in progress because H9-12 and other remediation work remain.
- Phase 9 completed actions: `9 / 14` (`64.3%`).

## Result

**H9-14_API_RUNTIME_REMEDIATION_VERIFIED**
