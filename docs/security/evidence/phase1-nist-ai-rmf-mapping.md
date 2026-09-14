# Phase 1 - NIST AI RMF Function-Level Mapping

Captured: 2026-09-14T11:54:26+01:00

Repository branch: security/phase-1-product-context

Source commit before mapping: 8ebefda8d361010b121e6683fdb12d32eb2caa2d

## Mapping Scope

This is a function-level working mapping for the authorized local
AI Application and Product Security training engagement.

It maps Phase 0 and Phase 1 evidence to:

- Govern
- Map
- Measure
- Manage

This document is not a certification, legal-compliance determination,
or assertion that the upstream Onyx organization has adopted these
local governance decisions.

## Govern

Local evidence mapped to Govern:

- written authorization and scope;
- local risk appetite;
- governance roles and local RACI;
- security, privacy, and safety objectives;
- policy applicability tracking;
- legal, regulatory, and contractual applicability tracking;
- risk-exception process;
- risk-acceptance process;
- lifecycle and end-of-life responsibilities;
- responsible-disclosure requirements;
- evidence-handling requirements.

Primary artifacts:

- docs/security/00-scope-and-rules-of-engagement.md
- docs/security/01-product-context-governance-risk.md

Known limitations:

- upstream organizational risk appetite is not established;
- upstream product, security, privacy, legal, and risk owners are not verified;
- deployment-specific legal and regulatory applicability is not established.

## Map

Local evidence mapped to Map:

- product mission;
- business value;
- stakeholders;
- intended uses;
- prohibited-use evidence and limitations;
- foreseeable misuse;
- critical workflows;
- AI-system classification;
- affected parties;
- impact analysis;
- threat environment;
- external-provider and integration context.

Primary artifact:

- docs/security/01-product-context-governance-risk.md

Known limitations:

- exact production deployment context is not established;
- complete asset, service, identity, data, model, tool, connector,
  and supply-chain inventories belong to later roadmap phases;
- exact trust boundaries and data flows require later reverse engineering.

## Measure

Local evidence mapped to Measure:

- evidence-supported confidentiality impact analysis;
- integrity impact analysis;
- availability impact analysis;
- privacy impact analysis;
- delegated-authority impact analysis;
- safety-classification limitations;
- working elevated-security-attention posture;
- explicit refusal to invent a formal numeric risk tier;
- reproducible evidence collection;
- immutable Git history;
- SHA-256 evidence fingerprints;
- documented assumptions and uncertainty.

Known limitations:

- no formal organizational risk-scoring methodology has been adopted;
- no formal product risk tier has been assigned;
- no production metrics are available;
- no statistical AI security evaluation has been performed in Phase 1;
- later phases must provide test results, detection evidence,
  and quantitative evaluation where appropriate.

## Manage

Local evidence mapped to Manage:

- stop conditions;
- material-change reapproval;
- bounded test limits;
- risk-exception handling;
- explicit risk-acceptance process;
- remediation and retest expectations;
- rollback procedures;
- teardown procedures;
- disclosure handling;
- residual-risk documentation;
- lifecycle refresh expectations;
- local end-of-life responsibilities.

Primary artifacts:

- docs/security/00-scope-and-rules-of-engagement.md
- docs/security/01-product-context-governance-risk.md

Known limitations:

- Ahmed can make risk decisions only for the authorized local lab;
- no upstream Onyx product risk is accepted by this mapping;
- production monitoring, business release decisions, and genuine
  incident-response authority remain outside the local engagement.

## Mapping Conclusion

Govern, Map, Measure, and Manage are represented at the Phase 1
function level with explicit evidence and limitations.

More detailed control and requirement mappings should be added in
later phases when architecture, assets, controls, tests, findings,
and deployment state are known.
