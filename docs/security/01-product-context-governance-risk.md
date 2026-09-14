# Phase 1 - Product Context, Governance, and Risk Management

## Evidence Metadata

Captured: 2026-09-14T10:31:28+01:00
Repository: https://github.com/amaw535353-ai/mydemo007.git
Local path: /home/ahmed/projects/mydemo007
Phase 0 closure commit: 247cde6921c0fa1c770582b34874d7cb2608711c
Phase 1 starting commit: 247cde6921c0fa1c770582b34874d7cb2608711c
Phase 1 branch: security/phase-1-product-context

Preparation evidence retained separately:
- Branch: security/phase-1-foundations
- Commit: 14f1e92b19bdac3551b0bd6cea7315ca75689edd
- Purpose: workstation/laboratory preparation evidence for later baseline work

## Evidence Discipline

Separate:
1. directly observed evidence;
2. evidence-supported conclusions;
3. assumptions requiring verification;
4. decisions requiring an accountable owner.

Do not present unsupported product, legal, regulatory, contractual,
privacy, safety, or risk conclusions as facts.

## 1. Product Mission

Evidence:
- README identifies Onyx as an open-source AI platform and the application layer for LLMs.
- README states that it provides a feature-rich interface that can be self-hosted.
- Supported capabilities include RAG, web search, custom agents, deep research, code execution, file/artifact creation, actions, MCP, voice, and image generation.
- README states that Onyx can connect applications through more than 50 indexing-based connectors or MCP.

Evidence-supported interpretation:
- Onyx's product mission is to provide a deployable application layer through which individuals and organizations can use LLM capabilities, enterprise knowledge, agents, tools, and external integrations.

Limitations:
- This interpretation is derived from repository documentation and is not a substitute for an authoritative internal product-strategy statement.

Evidence source:
- README.md
- docs/security/evidence/phase1-product-context-evidence.md

## 2. Business Value

Evidence:
- Lite mode provides a lower-resource chat and agent experience for quick evaluation or limited use.
- Standard Onyx provides the broader feature set, including RAG indexing, connector synchronization workers, inference services, caching, and object storage.
- Enterprise-oriented capabilities include collaboration, SSO, SCIM-related provisioning, RBAC, analytics, query history, and custom code controls.
- Community Edition provides core Chat, RAG, Agent, and Action capabilities.

Evidence-supported interpretation:
- Onyx creates value by providing one application layer for organizational LLM use, enterprise knowledge retrieval, agent workflows, integrations, governance-related controls, and multiple deployment profiles.
- Its deployment choices allow use cases ranging from individual experimentation to larger organizational deployments.

Unresolved business questions:
- Revenue model and commercial priorities are not established by this local evidence.
- Customer segments beyond the README descriptions require additional evidence.
- Business-critical workflows and quantitative business impact remain to be determined.

Evidence source:
- README.md
- docs/security/evidence/phase1-product-context-evidence.md

## 3. Stakeholders

Evidence-supported stakeholder categories:
- End users: individual users and members of organizational teams using chat, agents, RAG, research, tools, and other AI capabilities.
- Organizational customers/operators: teams ranging from small groups to large enterprises deploying or operating Onyx.
- Administrators: organizational roles managing authentication, provisioning, permissions, agents, actions, and enterprise configuration.
- AI/model providers: self-hosted and proprietary model-provider ecosystems supported by the application.
- Integration providers: connector, MCP, web-search, and other external-service ecosystems.
- Open-source contributors: contributors interacting through the repository contribution process.

Not yet established from current evidence:
- Accountable product owner.
- Accountable engineering owner.
- Accountable security owner.
- Data owner(s).
- Specific data-subject categories.
- Named commercial, legal, privacy, or compliance stakeholders.

Evidence source:
- README.md
- CONTRIBUTING.md where applicable
- docs/security/evidence/phase1-product-context-evidence.md

## 4. Ownership

- System owner: TO VERIFY
- Security owner: TO VERIFY
- Data owner(s): TO VERIFY
- Lifecycle owner: TO VERIFY
- End-of-life owner: TO VERIFY

## 5. Intended Uses

Evidence-supported intended uses:
- LLM chat and assistant interaction.
- Retrieval-augmented generation over indexed knowledge.
- Deep research and multi-step research workflows.
- Custom agent creation with instructions, knowledge, and actions.
- Web search and web-content retrieval.
- Actions and MCP-based application interaction.
- Sandboxed code execution for analysis and file manipulation.
- Artifact and document generation.
- Voice interaction.
- Image generation.
- Organizational collaboration and controlled enterprise AI adoption.
- Self-hosted or organization-managed deployments using supported model providers.

Limitations:
- These are documented product capabilities, not permission for unrestricted security testing.
- Phase 0 authorization and synthetic/local testing restrictions remain controlling.

Evidence source:
- README.md
- docs/security/evidence/phase1-product-context-evidence.md

## 6. Prohibited Uses

- TO IDENTIFY FROM POLICY OR PRODUCT EVIDENCE

## 7. Foreseeable Misuse

- TO THREAT-MODEL AFTER INTENDED USE IS ESTABLISHED

## 8. Critical Workflows

- TO IDENTIFY

## 9. AI-System Classification

Classification:
- TO DETERMINE

Evidence:
- TO RECORD

## 10. Impact Classification

Impact level:
- TO DETERMINE

Affected parties:
- TO IDENTIFY

Confidentiality impact:
- TO DETERMINE

Integrity impact:
- TO DETERMINE

Availability impact:
- TO DETERMINE

Privacy impact:
- TO DETERMINE

Safety impact:
- TO DETERMINE

## 11. Risk Tier

Risk tier:
- TO DETERMINE

Rationale:
- TO DOCUMENT

## 12. Threat Environment

- Relevant threat actors: TO IDENTIFY
- Capabilities: TO IDENTIFY
- Motives: TO IDENTIFY
- Preconditions: TO IDENTIFY
- Exposure assumptions: TO VERIFY

## 13. Risk Appetite

- TO BE DEFINED BY ACCOUNTABLE OWNER

## 14. Security Objectives

- TO DEFINE

## 15. Privacy Objectives

- TO DEFINE

## 16. Safety Objectives

- TO DEFINE

## 17. Governance Roles

- Product owner: TO VERIFY
- Engineering owner: TO VERIFY
- Security owner: TO VERIFY
- Reviewer: TO VERIFY
- Approver: TO VERIFY

## 18. RACI

| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Product decisions | TBD | TBD | TBD | TBD |
| Security requirements | TBD | TBD | TBD | TBD |
| Risk acceptance | TBD | TBD | TBD | TBD |
| Remediation | TBD | TBD | TBD | TBD |
| Release decision | TBD | TBD | TBD | TBD |
| Incident response | TBD | TBD | TBD | TBD |

## 19. Security Champions

- TO IDENTIFY OR MARK NOT APPLICABLE FOR LOCAL TRAINING

## 20. Policy Requirements

- TO IDENTIFY

## 21. Legal Requirements

- TO IDENTIFY APPLICABLE REQUIREMENTS
- Do not infer applicability without evidence.

## 22. Regulatory Requirements

- TO IDENTIFY APPLICABLE REQUIREMENTS
- Do not infer applicability without evidence.

## 23. Contractual Requirements

- TO IDENTIFY IF APPLICABLE
- No customer contract is assumed for this local training environment.

## 24. Risk Exceptions

Future exceptions must record:
- exception ID;
- affected asset/control;
- reason;
- compensating controls;
- owner;
- approver;
- start date;
- expiry date;
- residual risk;
- retest requirement.

## 25. Risk Acceptance

Risk acceptance must record:
- risk;
- evidence;
- severity;
- owner;
- accountable accepter;
- expiry/review date;
- residual risk;
- release consequence.

## 26. Lifecycle Ownership

- TO DEFINE

## 27. End-of-Life Ownership

- TO DEFINE

## 28. NIST AI RMF - Govern

- TO MAP

## 29. NIST AI RMF - Map

- TO MAP

## 30. NIST AI RMF - Measure

- TO MAP

## 31. NIST AI RMF - Manage

- TO MAP

## Current Evidence Sources

Root README:
- README.md

Repository remote:
- https://github.com/amaw535353-ai/mydemo007.git

Starting commit:
- 247cde6921c0fa1c770582b34874d7cb2608711c

## Phase 1 Completion Gate

Phase 1 is not complete until:
- product mission and business value are evidence-backed;
- stakeholders and ownership are recorded;
- intended and prohibited uses are defined;
- foreseeable misuse and critical workflows are identified;
- AI-system and impact classifications are justified;
- risk tier and threat environment are documented;
- security, privacy, and safety objectives are defined;
- governance roles and RACI are established;
- applicable policy/legal/regulatory/contractual requirements are recorded with evidence;
- risk exception and acceptance processes are defined;
- lifecycle and end-of-life ownership are recorded;
- NIST AI RMF Govern, Map, Measure, and Manage mappings are completed;
- assumptions, limitations, and unresolved questions remain explicit.
