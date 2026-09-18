# Phase 9 Action 9.10 — Runtime Cross-User, Cross-Role and Cross-Tenant Verification Runbook

Status: **READY FOR AUTHORIZED LOCAL EXECUTION — NOT YET COMPLETE**

## Why this action is not marked complete yet

Action 9.10 requires live evidence from the authorized Onyx laboratory. The connected GitHub integration can read and modify repository state but cannot enter the user’s WSL/Codespace process or reach that lab’s loopback interface. GitHub Actions is deliberately not substituted because the project’s cost boundary prohibits tests that may consume unapproved billable cloud resources.

Therefore this artifact prepares and gates the real execution without misrepresenting static or repository evidence as runtime proof.

## Immutable runtime baseline

- Required branch: `security/phase-9-identity-authorization-tenant-isolation`
- Minimum completed ancestor: `5d7a602680200e50134b5048fc79f27c8f32e41b`
- Action 9.9 runner: `scripts/security/phase9_negative_authz_runner.py`
- Action 9.10 wrapper: `scripts/security/phase9_runtime_verify.sh`
- Sanitizer/summarizer: `scripts/security/phase9_results_to_markdown.py`

The wrapper records the actual runtime HEAD dynamically. It refuses the wrong branch, missing Action 9.9 ancestry, a dirty working tree, a non-loopback target, or an unreachable local API.

## Safety properties

- local loopback HTTP(S) only;
- no GitHub Actions or external test target;
- explicit `PHASE9_RUN=1` required before HTTP execution;
- sequential requests;
- five-second maximum request timeout;
- one-MiB response ceiling;
- redirects disabled;
- raw response bodies excluded from evidence;
- authorization/cookie values never printed by the harness;
- synthetic users, groups, tenants, files, chats, agents, credentials and tokens only;
- stop immediately on external calls, real data/credentials, unexpected scope, or unbounded behavior.

## Execution sequence

### Gate A — synchronize the branch

Pull the current Phase 9 branch into the authorized lab and confirm the worktree is clean.

### Gate B — prepare synthetic fixtures

Populate only the environment variables for fixtures that actually exist in the current local lab. The executable pack intentionally reports missing fixtures as `SKIP` rather than inventing data or treating an invalid path as secure.

Minimum high-value fixtures:

- global admin credential;
- scoped Group-A manager credential;
- Alice and Bob ordinary-user credentials;
- Alice-owned valid chat path;
- Group-A in-scope user marker and Group-B out-of-scope user marker;
- under-scoped PAT and a protected route outside its scope;
- Alice-owned generated-image file ID if H9-12 is applicable;
- harmless loopback custom action / MCP mock receiver for H9-14 through H9-16;
- low-privilege service-account API key plus rotation/revocation fixtures.

Credentials remain shell environment values and must never be committed.

### Gate C — dry run

Run the wrapper without `PHASE9_RUN=1`. This checks branch lineage, clean state, tooling, API reachability and fixture availability while sending no authorization-test requests.

Command:

```bash
bash scripts/security/phase9_runtime_verify.sh
```

Expected: a sanitized result with HTTP cases marked `SKIP` for dry run and manual cases marked `REVIEW`.

### Gate D — bounded execution

After the synthetic fixtures are confirmed:

```bash
export PHASE9_RUN=1
export PHASE9_BASE_URL=http://127.0.0.1:8080
bash scripts/security/phase9_runtime_verify.sh
```

Default evidence outputs:

- `/tmp/phase9-action-9.10-results.json`
- `/tmp/phase9-action-9.10-summary.md`
- `/tmp/phase9-action-9.10-metadata.txt`

The JSON and summary contain no raw HTTP bodies or credential values. Review them before any evidence is copied into the repository.

## Runtime decision rules

- `PASS`: explicit automated security expectation matched.
- `FAIL`: explicit security expectation was contradicted or the harness encountered an execution error.
- `REVIEW`: HTTP status alone is insufficient; policy, receiver, DB, audit or lifecycle evidence is required.
- `SKIP`: required synthetic fixture was not supplied.

A `404` denial is not an automatic PASS unless paired evidence proves the same route/resource is valid for an authorized principal.

## Hypothesis execution map

| Hypothesis | Runtime proof required in Action 9.10 |
|---|---|
| H9-11 | scoped manager `/manage/users` contains expected in-scope marker and excludes out-of-scope marker |
| H9-12 | Alice owner control succeeds; Bob retrieval of same generated-image file is denied |
| H9-13 | instrumented/source-provenance proof that no untrusted request path can set `bypass_acl=True` |
| H9-14 | Bob cannot attach/use Alice’s non-shared credential-bearing custom action; receiver sees no delegated Alice credential |
| H9-15 | after share revocation, new chat is denied and existing-session behavior matches documented revocation policy |
| H9-16 | request-level MCP headers do not override or exceed configured server authentication policy |
| H9-17 | service-account interactive-session behavior matches documented machine-identity policy |
| H9-18 | synthetic DB inspection proves actual secret-at-rest confidentiality and tamper/integrity behavior for assessed edition/config |
| H9-19 | mock-login OAuth tokens’ storage and logout/unlink/revocation lifecycle are proven without exposing token values |

## Manual evidence required in addition to the HTTP runner

### H9-13

Instrument the search construction path or use a controlled test hook to record whether an untrusted request can cause ACL bypass. Do not modify production behavior merely to make the test pass.

### H9-14 and H9-16

Use only loopback mock receivers. Record whether the receiver was invoked and whether a protected synthetic header arrived. Store redacted observations only.

### H9-15

Record the product’s intended revocation semantics before severity classification. Existing-session continuation is not automatically a vulnerability unless it violates the intended authorization boundary.

### H9-18

Inspect only synthetic credential rows in the local DB. Evidence should record ciphertext/plaintext characteristics, lengths/hashes and configuration state without the secret value. Ciphertext mutation must occur only on a disposable synthetic row with rollback/recreation available.

### H9-19

Use a local/mock OAuth provider. Record only storage type/state, lifecycle events and redacted hashes/lengths—never access or refresh token contents.

## Completion gate

Action 9.10 may be marked **COMPLETE** only when all of the following are true:

1. the test pack was executed against the authorized local Onyx lab;
2. horizontal, vertical and scoped-manager controls have live evidence;
3. applicable cross-tenant/service-account controls have live evidence;
4. every H9-11 through H9-19 item is PASS, FAIL, or has a documented REVIEW/non-applicability disposition backed by evidence;
5. no required test remains SKIP without an explicit non-applicability rationale;
6. candidate FAIL results are promoted to Action 9.11 rather than prematurely labeled vulnerabilities;
7. evidence contains no real credentials, real customer data or raw secret values;
8. the exact runtime branch/HEAD and UTC timestamp are preserved.

## Current decision

**READY — repository-side Action 9.10 execution tooling is prepared. Runtime verification itself remains pending until the authorized loopback lab executes the wrapper. Phase 9 completion must remain at 64.3% until that evidence exists.**
