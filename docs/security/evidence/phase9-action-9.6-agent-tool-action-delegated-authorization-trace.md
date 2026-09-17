# Phase 9 — Action 9.6 Agent, Tool, Action and Delegated-Authorization Trace

## Status

**STATIC TRACE COMPLETE**

Runtime authorization effectiveness is not inferred from this artifact. Candidate gaps remain hypotheses until reproduced in the authorized synthetic laboratory.

## Objective

Trace whether an authenticated human, agent/persona, tool, custom OpenAPI action, MCP server, delegated credential, file reader, and tool-execution path preserve the initiating user's authorization boundary.

The security property under test is:

> An agent or tool must not gain authority, credentials, resources, or side effects that the initiating user is not authorized to exercise, except where a documented product policy deliberately grants a workspace-level capability.

## Source-backed authorization chain

```text
Authenticated user
    |
    v
Chat-session ownership / agent access
    |
    v
Persona / agent configuration
    |
    +--> tool associations
    +--> document / file knowledge
    +--> sharing / ownership / managed scope
    |
    v
Tool construction
    |
    +--> enabled state
    +--> allowed_tool_ids per-turn narrowing
    +--> built-in availability
    +--> custom action auth material
    +--> MCP credential resolution
    |
    v
Tool runner
    |
    +--> only constructed tool names dispatched
    +--> concurrency cap
    |
    v
External/local side effect or data read
```

## 1. Agent/persona access boundary

`create_chat_session_from_request` validates both project ownership and non-default persona access before creating a new session. A user who cannot access the selected persona is rejected.

Persona database access is separately filtered through owner, direct share, public/listed visibility, group relationships, administrator authority, and scoped-manager rules. Editable operations use a stronger editable view and scoped-manager GATE 2 checks.

For scoped managers, persona create/update re-reads the existing resource, locks it, derives current/requested group state, and calls the managed-scope authorization gate before mutation.

### Positive security pattern

A model-provided persona ID is not accepted as authority by itself. New chat creation and persona mutation both rely on server-side authorization state.

## 2. Persona-to-tool association boundary

`upsert_persona` resolves requested tool IDs from the database and validates tool definitions before assignment.

For newly attached MCP tools, the code explicitly checks `user_can_access_mcp_server(...)` and rejects an MCP server the acting user cannot access.

However, the same function does not show an equivalent owner/group/connected-action authorization check for a non-MCP custom OpenAPI tool before assigning it to the persona. Non-MCP tools have `mcp_server_id == None`, so they skip the MCP attachment check.

This is important because custom-action management itself *does* have an explicit owner/admin boundary: `can_manage_own_tool` permits a GLOBAL actions administrator or the scoped creator, and `can_manage_tool` is used by edit/delete/toggle management APIs.

### Candidate hypothesis H9-14

**Foreign custom action attachment may delegate creator-stored credentials.**

Static preconditions observed:

1. custom actions have creator ownership and management boundaries;
2. the general enabled-tool catalog includes custom tools for authenticated users, while MCP tools receive a separate accessible-server filter;
3. custom actions are selectable for agent creation;
4. persona attachment explicitly validates newly added MCP server access but does not show an equivalent custom-action owner/access check;
5. once attached, enabled custom actions are constructed for the persona;
6. custom-action runtime can use stored custom headers and issue the configured HTTP request.

This can become a security issue only if a synthetic non-owner can actually attach another user's credential-bearing custom action and successfully invoke it. OAuth-config and passthrough-auth tools must be evaluated separately because those paths may resolve the current user's own OAuth credential rather than another user's credential.

**Classification: runtime-verification hypothesis, not a confirmed vulnerability.**

## 3. Tool catalog and management controls

The management API uses `_get_manageable_custom_tool` / `can_manage_tool` for custom action edit/delete/toggle operations. OAuth-config linkage has a second authorization check so a user cannot arbitrarily link another creator's shared OAuth configuration.

The basic tool catalog applies user-specific MCP-server filtering. Built-ins are also checked for runtime availability. Custom tools, however, are broadly exposed by the general catalog and the visibility helper declares non-built-in custom tools frontend-visible, chat-selectable, and agent-creation-selectable.

Visibility alone is not a vulnerability; the decisive property is whether attachment and execution re-authorize the capability.

## 4. Per-turn narrowing and tool dispatch

`construct_tools` provides several useful enforcement points:

- disabled tools are skipped even if still attached to a persona;
- when `allowed_tool_ids` is supplied, tools outside the allowlist are skipped;
- built-in tools must report themselves available;
- SearchTool receives the current authenticated user;
- FileReaderTool receives a bounded set of file IDs;
- MCP credentials are resolved for the current user;
- custom OAuth uses the current user's token manager / login token where configured.

The tool runner then builds a map only from the constructed tool instances. Unknown model-requested tool names are dropped. A maximum-concurrent-tools cap can also bound the batch.

### Security implication

There is no independent authorization engine at the final dispatch line. Correct security therefore depends heavily on the correctness of persona access, tool attachment, credential resolution, and `construct_tools` filtering.

## 5. Custom OpenAPI delegated authorization

Custom OpenAPI tools are constructed from the stored schema and headers. Dynamic placeholders may be substituted with current chat/session/user identifiers. A per-tool OAuth configuration uses an OAuth token manager scoped to the current user ID; passthrough authentication uses the current user's login OAuth token.

If neither of those modes supplies the authorization credential, stored custom headers remain part of the request configuration. At runtime, `CustomTool.run` constructs the configured URL, path/query/body, and executes the HTTP method using the tool's headers.

### Required negative tests

- non-owner attempts to attach another creator's static-header custom action;
- non-owner attempts to invoke it through their own persona;
- disabled custom action remains non-callable even if associated;
- foreign OAuth-backed action does not inherit another user's OAuth grant;
- foreign passthrough-auth action uses only the acting user's token;
- foreign MCP action attachment is denied as the control case.

All action endpoints for runtime testing must point only at approved loopback mock receivers.

## 6. MCP delegated credentials

MCP credential resolution distinguishes:

- no-auth servers;
- per-user API-token configuration;
- admin-provided shared credentials;
- OAuth credentials;
- passthrough OAuth using the current user's login OAuth token.

Anonymous users are rejected from passthrough OAuth. Generated authentication headers take precedence when effective credentials are built. Stored credential headers are also filtered for denylisted header names.

At MCP execution time, request-supplied additional headers are filtered and merged with resolved credentials. Resolved/generated credential headers are merged later and therefore take precedence over same-named request headers.

OAuth credentials may be refreshed before execution, and authentication failure is surfaced distinctly from an ordinary tool error.

### Candidate hypothesis H9-16

**Request-supplied MCP headers require an explicit trust-policy verification.**

`SendMessageRequest` exposes `mcp_headers` as a request-controlled dictionary, with Authorization shown as a supported example. MCP execution allows additional headers to participate in the connection and notes that extra headers can stand in for missing credentials in some states.

This can be legitimate delegated-auth functionality. Phase 9 must nevertheless prove that a server whose policy requires managed/admin/per-user credentials cannot be transformed into an unintended capability merely by supplying arbitrary message-level headers.

**Classification: policy/runtime-verification hypothesis, not a confirmed vulnerability.**

## 7. Existing-session revocation boundary

New chat creation checks current persona access. Existing chats follow a different path: the session loader checks the requesting user's ownership of the chat session, eager-loads its persona and tools, and the message-processing flow then constructs tools from that loaded persona.

The traced existing-session path does not show a fresh persona-share/access decision before tool construction.

### Candidate hypothesis H9-15

**Agent access revocation may not invalidate an already-created chat session's capabilities.**

Controlled sequence required:

1. Alice creates an agent with a harmless local mock action.
2. Alice shares the agent with Bob.
3. Bob creates a chat session using the agent — expected ALLOW.
4. Alice revokes Bob's agent access.
5. Bob attempts to create a new chat with the same agent — expected DENY.
6. Bob sends another message to the existing owned chat session — expected DENY or privileged tools stripped according to policy.
7. If the old session still constructs and executes the revoked agent's action, record the exact residual capability and intended product policy before classification.

**Classification: runtime-verification hypothesis, not a confirmed vulnerability.**

## 8. File-reader capability narrowing

FileReaderTool receives only the precomputed user-file and chat-file IDs available to the current chat context. The model-provided file UUID is rejected unless it belongs to one of those sets. Individual reads are also length-bounded.

This is a useful example of capability-style authorization: the model can choose only among server-authorized file handles rather than presenting an arbitrary file identifier as authority.

## 9. Memory-tool special case

MemoryTool is deliberately injected when the current user has memory enabled, bypassing persona associations and `allowed_tool_ids` filtering. This is a documented construction behavior rather than evidence of privilege escalation.

Its persistence path was traced in Action 9.5 as user-ID-bound. Phase 9 runtime tests should ensure the per-turn tool allowlist semantics intentionally exclude or include MemoryTool and that the tool cannot mutate another user's memory.

## 10. Delegated authorization test matrix additions

| ID | Actor | Capability | Expected security property |
|---|---|---|---|
| AT-01 | Bob | Alice's private agent ID | DENY new-session use |
| AT-02 | Bob | Alice's custom action ID | DENY unauthorized attachment if action is not shared/authorized |
| AT-03 | Bob | Alice static-header action | DENY creator credential delegation |
| AT-04 | Bob | Alice OAuth-backed action | no Alice OAuth token delegation |
| AT-05 | Bob | Alice MCP tool/server | DENY attachment without server access |
| AT-06 | Bob | disabled attached action | DENY execution |
| AT-07 | Bob | allowed_tool_ids excludes action | DENY execution for that turn |
| AT-08 | model | unknown tool name | DROP / no execution |
| AT-09 | Bob after agent-share revocation | existing session | DENY or remove revoked capability per policy |
| AT-10 | Bob | arbitrary FileReader UUID | DENY unless present in server-authorized file set |
| AT-11 | Bob | arbitrary mcp_headers | must not exceed documented MCP credential policy |
| AT-12 | Bob | MemoryTool | current-user memory only |

## 11. Root-cause targets if hypotheses reproduce

### H9-14

Likely control gap to examine: asymmetry between MCP attachment authorization and custom OpenAPI action attachment authorization inside persona upsert.

Required remediation shape if confirmed:

- define an explicit `can_attach_tool(user, tool, persona, db_session)` policy;
- distinguish built-in, owned custom, explicitly shared/connected custom, and MCP tools;
- require authorization before new tool association;
- preserve legitimate existing associations only according to documented revocation policy;
- add regression tests for foreign static-header actions.

### H9-15

Likely control gap to examine: access checked at session creation but not revalidated before continuing an existing session.

Required remediation shape if confirmed:

- define whether agent-share revocation is immediate or session-pinned;
- if immediate, revalidate persona usability or derive a fresh authorized capability set before each turn;
- ensure tool/knowledge access is removed even if chat history remains owner-readable;
- add revocation regression tests.

### H9-16

Required design decision:

- document which MCP authentication modes may consume request-level headers;
- reject/strip Authorization or other security-sensitive request headers when the server policy does not explicitly permit caller-supplied delegation;
- regression-test header precedence and no-credential states.

## 12. Evidence classification

Confirmed by static source trace:

- server-side agent access exists for new-session creation;
- scoped agent mutation gates exist;
- custom action management has creator/admin authorization;
- MCP attachment performs an explicit accessible-server check;
- disabled and per-turn-excluded tools are skipped during construction;
- unknown tool names are not dispatched;
- custom action OAuth/passthrough paths can bind to the current user;
- MCP supports per-user/admin/delegated credential modes and header precedence;
- FileReaderTool uses a server-authorized file capability set.

Not yet proven:

- H9-14 foreign custom-action attachment and credential use;
- H9-15 existing-session behavior after agent access revocation;
- H9-16 whether request-level MCP headers can exceed intended server policy;
- any cross-user/cross-role/cross-tenant side effect.

## Result

**PASS — agent/tool/action/delegated-authorization architecture and runtime hypotheses captured. No vulnerability is claimed from static evidence alone.**
