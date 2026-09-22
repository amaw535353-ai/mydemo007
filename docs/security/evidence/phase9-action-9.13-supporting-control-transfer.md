# Phase 9 — Action 9.13 Supporting-Control Transfer Assessment

## Objective

Identify which identity and authorization responsibilities may be delegated
to external supporting controls and which must remain enforced by the
application.

This is an architecture/control-responsibility assessment.

It does not claim that a production Keycloak or OpenFGA deployment was
implemented in this Phase 9 laboratory.

## Repository signals

- Keycloak references: **15**
- OpenFGA references: **3**

Reference counts are discovery signals only and are not treated as evidence
of deployed enforcement.

## Responsibility matrix

| Control | Appropriate authority | Decision |
|---|---|---|
| Primary authentication/federation | Identity provider | Transfer candidate |
| MFA/upstream authentication policy | Identity provider | Transfer candidate |
| Coarse role/group claims | Identity provider | Transfer candidate |
| Service-account login restrictions | IdP + application | Defense in depth |
| Fine-grained relationships | External policy engine | Transfer candidate |
| Conversation/resource ownership | Application | Must remain enforced |
| Tenant isolation | Application/data layer | Must remain enforced |
| Action attachment authority | Application | Must remain enforced |
| MCP delegated-header policy | Application/tool boundary | Must remain enforced |
| RAG/document access authorization | Application/data layer | Must remain enforced |
| Secret encryption | Application/database | Must remain local control |
| OAuth token encryption | Application/database | Must remain local control |
| Provider-side OAuth revocation | OAuth provider integration | Provider lifecycle control |

## Transfer principle

External identity claims are inputs to authorization decisions.

They do not replace application verification of:

- tenant context;
- resource ownership;
- action/resource relationships;
- delegated authority;
- data-path authorization.

## Future deployment assurance

Any Keycloak/OpenFGA or equivalent deployment should verify:

1. token issuer/audience/signature validation;
2. subject-to-local-user binding;
3. group/role mapping;
4. tenant-context derivation;
5. policy fail-closed behavior;
6. stale relationship/cache behavior;
7. revocation propagation;
8. unavailable-policy-service behavior;
9. parity between application and external authorization policy.

## Residual transfer risks

The Action 9.14 residual-risk register must retain:

- incorrect identity-role mapping;
- stale authorization relationships;
- policy-engine fail-open behavior;
- untrusted tenant claims;
- application/external-policy divergence.

## Evidence identity

Transfer inventory SHA-256:

`9d0bb209f44a61782f65a8ca5737dcd21bbac330fb2e26554752d080cfee7e28`

## Completion

**ACTION 9.13: COMPLETE**
