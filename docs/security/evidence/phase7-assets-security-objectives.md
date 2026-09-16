# Phase 7 Action 7.3 - Security Assets and Objectives

## Identity assets

Protected assets include:

- user identity;
- authentication state;
- session/token state;
- tenant identity;
- groups and roles;
- permission state;
- object ownership.

Security objectives:

- identities must not be confused or substituted;
- tenant identity must remain bound to requests and data operations;
- authorization must be enforced at each relevant object boundary;
- revoked privileges must stop granting effective access.

## Document and RAG assets

Protected assets include:

- uploaded documents;
- connector-ingested documents;
- chunks;
- embeddings;
- indexes;
- document metadata;
- ACL/access metadata;
- retrieved context;
- citations.

Security objectives:

- tenant and authorization metadata must remain associated with content;
- unauthorized content must not reach retrieval results;
- unauthorized content must not reach model-visible context;
- revocation/deletion must propagate to derived representations;
- retrieved content must be treated as potentially untrusted input.

## Conversation and model assets

Protected assets include:

- conversations;
- messages;
- prompts;
- system instructions;
- retrieved context;
- model configuration;
- model output;
- citations;
- persisted AI-generated state.

Security objectives:

- users must access only authorized conversations;
- private context must not cross authorization or tenant boundaries;
- untrusted content must not silently override higher-trust instructions;
- external model boundaries must not receive unauthorized sensitive data.

## Agent, tool and MCP assets

Protected assets include:

- tool definitions;
- MCP server configuration;
- credentials;
- tool arguments;
- execution permissions;
- tool results;
- code execution environments;
- external side effects.

Security objectives:

- model output alone must not create unrestricted authority;
- tools must operate under explicit authorization and least privilege;
- tool arguments must be validated;
- credentials must remain scoped;
- dangerous side effects must be controlled;
- execution must remain bounded and isolated.

## Persistence and lifecycle assets

Protected assets include:

- relational records;
- cache state;
- queues;
- search/vector state;
- file/object storage;
- credentials;
- logs;
- audit records.

Security objectives:

- authoritative permission changes must propagate;
- stale derived state must not preserve revoked access;
- deletion must reach security-relevant downstream representations;
- retries and asynchronous workers must not restore invalid state;
- security events must remain sufficiently observable.

## Availability and economic assets

Protected assets include:

- CPU;
- memory;
- storage;
- worker capacity;
- model/token budget;
- connector capacity;
- tool capacity.

Security objectives:

- user-controlled operations must remain bounded;
- expensive paths require limits;
- recursive or repeated AI/tool operations must not become uncontrolled.
