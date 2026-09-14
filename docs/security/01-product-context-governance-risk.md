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

Repository-supported governance evidence:
- CONTRIBUTING.md shows that proposed features or enhancements require approval before contribution.
- The contribution guide identifies Yuhong as a review contact for contribution approval.
- Design approval is performed by the Onyx team, which may provide or request a design document and PRD.
- Approved contribution work can involve design, product-management, and engineering resources from the Onyx team.
- SECURITY.md routes vulnerability reports to the repository maintainers through GitHub Private Vulnerability Reporting.

What this evidence does NOT establish:
- It does not prove that Yuhong is the accountable product owner for the entire Onyx product.
- It does not identify an accountable security owner.
- It does not identify accountable data owners.
- It does not establish lifecycle or end-of-life ownership.

Current status:
- System owner: NOT YET VERIFIED.
- Product owner: NOT YET VERIFIED.
- Engineering owner: NOT YET VERIFIED.
- Security owner: NOT YET VERIFIED.
- Data owner(s): NOT YET VERIFIED.
- Lifecycle owner: NOT YET VERIFIED.
- End-of-life owner: NOT YET VERIFIED.

Evidence source:
- CONTRIBUTING.md
- SECURITY.md
- docs/security/evidence/phase1-governance-context-evidence.md

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

Product prohibited-use evidence:
- No authoritative general product prohibited-use policy has been established from the local repository evidence reviewed so far.

Security-research policy exclusions identified in SECURITY.md:
- Do not report vulnerabilities through public GitHub issues, pull requests, or discussions.
- Third-party services and integrations are outside the upstream Onyx vulnerability-reporting scope.
- Findings requiring access to another user's account or device, social engineering, or physical attacks are outside that policy's scope.
- High-volume denial-of-service findings without additional exploitable impact are outside that policy's scope.
- Automated scanner output without demonstrated exploitable impact is outside that policy's scope.
- Safe-harbor expectations include avoiding privacy violations, data destruction, and service degradation.

Important distinction:
- These are vulnerability-research and disclosure constraints, not proof of a general end-user acceptable-use policy.
- Our local Phase 0 authorization remains stricter than the upstream policy and continues to control our testing.

Evidence source:
- SECURITY.md
- docs/security/evidence/phase1-governance-context-evidence.md

## 7. Foreseeable Misuse

Evidence basis:
- Onyx supports agents, actions, MCP integrations, web access, RAG, connectors, code execution, file generation, multiple model providers, collaboration, SSO, and RBAC.

Candidate foreseeable misuse scenarios derived from those capabilities:
- An agent could be induced to invoke an action or MCP capability outside the user's intended task.
- Retrieved or connected content could contain instructions intended to manipulate an agent or model.
- Code-execution functionality could be abused to access unintended files, resources, or network destinations if controls fail.
- Connector permissions or retrieval filtering failures could expose information to unauthorized users or tenants.
- Misconfigured RBAC or identity integration could grant capabilities to an unintended user or group.
- Generated files or artifacts could contain sensitive or misleading information.
- External model or integration providers could receive data that a user or organization did not intend to disclose.
- Web-retrieved content could influence agent behavior through untrusted instructions or data.

Classification:
- These are threat hypotheses derived from documented functionality.
- They are not confirmed vulnerabilities.
- Each hypothesis requires later architecture analysis, threat modeling, and bounded verification.

Evidence source:
- README.md
- docs/security/evidence/phase1-product-context-evidence.md
- docs/security/evidence/phase1-governance-context-evidence.md

## 8. Critical Workflows

Evidence-supported candidate critical workflows:
- User authentication and enterprise identity integration.
- Authorization and RBAC decisions for sensitive resources.
- Chat and LLM request processing.
- RAG ingestion, indexing, retrieval, and answer generation.
- Connector synchronization and knowledge ingestion.
- Custom-agent creation and execution.
- Action and MCP invocation.
- Web-search and web-content retrieval.
- Sandboxed code execution.
- File and artifact generation.
- Model-provider selection and request routing.
- Collaboration and sharing of chats or agents.
- Audit/query-history collection used for organizational oversight.

Security significance:
- Compromise of these workflows could affect confidentiality, integrity, availability, privacy, or delegated authority.
- Exact architecture, trust boundaries, data flows, and failure consequences remain to be established in later phases.

Evidence source:
- README.md
- docs/security/evidence/phase1-governance-context-evidence.md

## 9. AI-System Classification

Evidence-supported working classification:
- Onyx is an AI application/platform and orchestration layer for LLM-based functionality.
- It is not evidenced here as a foundation-model developer itself.
- It can consume both self-hosted and proprietary model providers.
- It combines conventional application components with AI-specific capabilities including RAG, agents, actions, MCP, web retrieval, code execution, and generated artifacts.
- It supports both Lite and Standard deployment profiles.

Working system categories:
- AI-enabled application platform.
- LLM application/orchestration layer.
- Retrieval-augmented application.
- Agent-capable application.
- Tool/action-capable application.
- Multi-provider model-consumer application.
- Enterprise knowledge and collaboration application.

Classification limitations:
- Exact deployed classification depends on enabled features, deployment mode, model providers, connectors, tools, data, tenants, and organizational use.
- This is a product-level working classification, not a legal or regulatory classification.

Evidence source:
- README.md
- docs/security/evidence/phase1-risk-context-evidence.md

## 10. Impact Classification

Evidence-supported impact analysis:

Confidentiality:
- Potentially material.
- RAG, connectors, organizational knowledge, chats, agents, provider requests, generated artifacts, and code execution may process information whose unintended disclosure could affect users or organizations.

Integrity:
- Potentially material.
- Agent instructions, retrieved content, actions, MCP calls, generated outputs, access-control decisions, and connected knowledge can influence system behavior and downstream decisions.

Availability:
- Potentially material.
- Chat, retrieval, indexing, connectors, model access, background workers, and other application services may become operational dependencies for users or organizations.

Privacy:
- Potentially material.
- User queries, documents, organizational knowledge, logs, provider requests, and generated content can involve personal or sensitive information depending on deployment.

Delegated-authority impact:
- Potentially material.
- Agents, actions, MCP, code execution, connectors, and enterprise permissions can allow AI-mediated operations beyond simple text generation.

Safety:
- Context dependent and NOT YET CLASSIFIED.
- Current repository evidence does not establish a specific safety-critical deployment such as medical, transportation, industrial-control, or other high-consequence use.

Affected parties potentially include:
- End users.
- Organization members.
- Administrators.
- Data subjects whose information is indexed or processed.
- Organizations operating the deployment.
- Connected-service owners and users where integrations are enabled.

Formal impact level:
- NOT YET ASSIGNED.
- A formal level requires an adopted impact methodology, deployment context, data classification, business criticality, and accountable approval.

Evidence source:
- README.md
- SECURITY.md
- docs/security/evidence/phase1-risk-context-evidence.md

## 11. Risk Tier

Formal risk tier:
- NOT YET ASSIGNED.

Reason:
- The current evidence does not establish an approved organizational risk-tier methodology or risk appetite.
- Assigning Low, Medium, High, Critical, or a numeric score without such a method would create false precision.

Working security posture:
- ELEVATED SECURITY ATTENTION WARRANTED.

Evidence-supported reasons:
- The product can process organizational knowledge.
- It supports identity and authorization controls.
- It supports external model providers.
- It supports connectors and external integrations.
- It supports autonomous or semi-autonomous agent functionality.
- It supports actions and MCP capabilities.
- It supports sandboxed code execution.
- It can operate in multi-user organizational environments.
- It includes audit/query-history and enterprise administration features.

Interpretation:
- These properties create multiple trust boundaries and delegated-capability surfaces.
- They justify substantial security engineering effort but do not by themselves define a formal enterprise risk tier.

Required before formal tier assignment:
- Approved risk methodology.
- Business criticality.
- Data classification.
- Deployment exposure.
- Tenant model.
- Regulatory and contractual applicability.
- Impact thresholds.
- Risk appetite.
- Accountable risk owner.

Evidence source:
- README.md
- docs/security/evidence/phase1-risk-context-evidence.md

## 12. Threat Environment

Evidence-supported candidate threat environment:

Potential threat actors:
- Unauthenticated external attackers where a deployment exposes reachable application surfaces.
- Malicious or compromised authenticated users.
- Users attempting to exceed their assigned authorization.
- Compromised user accounts or credentials.
- Malicious or compromised connected content sources.
- Untrusted web content encountered by web-search or retrieval capabilities.
- Malicious documents or retrieved content intended to influence AI behavior.
- Compromised or malicious connectors, MCP servers, tools, or external integrations.
- Compromised model-provider or dependency relationships.
- Software-supply-chain attackers affecting application dependencies, images, or deployment artifacts.
- Insiders with legitimate access but malicious or unsafe intent.

Relevant attacker objectives may include:
- Unauthorized information disclosure.
- Cross-user or cross-tenant access.
- Privilege or capability escalation.
- Unauthorized action or tool invocation.
- Manipulation of AI instructions, context, retrieval, or outputs.
- Abuse of code execution.
- Credential or token theft.
- Persistence through stored content or configuration.
- Availability degradation.
- Audit or monitoring evasion.

Important scope distinction:
- These are product threat hypotheses for threat modeling.
- They do not assert that the current local lab is Internet-exposed.
- Active testing remains restricted by the Phase 0 local, synthetic, loopback-only authorization.
- No threat hypothesis is a confirmed vulnerability without later evidence.

Evidence source:
- README.md
- SECURITY.md
- docs/security/evidence/phase1-risk-context-evidence.md

## 13. Risk Appetite

Upstream/product organizational risk appetite:
- NOT ESTABLISHED FROM CURRENT EVIDENCE.
- No claim is made about the risk appetite of the upstream Onyx organization.

Authorized local-assessment risk appetite:
- Very low tolerance for uncertainty about authorization or scope.
- Zero tolerance for intentional access to real customer data or production credentials.
- Zero tolerance for testing public or otherwise unapproved targets.
- Zero tolerance for unapproved external-service or paid-resource use.
- Zero tolerance for unbounded resource-consumption or denial-of-service testing.
- Low tolerance for unexpected instability; testing stops when instability appears.
- Active testing must remain within approved local, synthetic, bounded conditions.
- Material changes to scope, network boundaries, targets, data classification, external integrations, cost exposure, or test limits require review before continuation.

Risk decision principle:
- Safety, authorization, evidence integrity, and containment take priority over completing a test.
- When scope or impact is uncertain, stop rather than assume permission.

Evidence source:
- docs/security/00-scope-and-rules-of-engagement.md
- docs/security/evidence/phase1-governance-objectives-evidence.md

## 14. Security Objectives

Working assessment security objectives:

Identity and authorization:
- Ensure authenticated identities receive only intended permissions.
- Preserve least privilege across users, groups, agents, actions, connectors, and administrative capabilities.
- Prevent cross-user and cross-tenant authorization failures where tenant boundaries exist.

Data and retrieval:
- Protect organizational knowledge, documents, chats, prompts, retrieval results, logs, and generated artifacts from unauthorized disclosure or modification.
- Preserve authorization throughout ingestion, indexing, retrieval, caching, and answer generation.

Agent and delegated capability:
- Constrain agents to explicitly authorized tools, actions, MCP capabilities, resources, and destinations.
- Prevent untrusted instructions or retrieved content from silently expanding authority.

Code execution:
- Maintain effective sandbox boundaries.
- Prevent unintended filesystem, process, credential, or network access.

External integrations:
- Make data destinations and provider boundaries explicit.
- Prevent accidental transmission to unapproved model providers, connectors, tools, or third parties.

Auditability:
- Preserve sufficient evidence to reconstruct material security-sensitive actions and decisions.

Resilience:
- Bound time, retries, concurrency, resource consumption, and failure propagation.
- Fail safely where authorization or security-critical dependencies are uncertain.

Supply-chain integrity:
- Preserve traceability of source, dependencies, configuration, deployment artifacts, and security-relevant changes.

Classification:
- These are working security-assessment objectives.
- They are not represented as official upstream Onyx security commitments.

Evidence source:
- README.md
- SECURITY.md
- docs/security/evidence/phase1-governance-objectives-evidence.md

## 15. Privacy Objectives

Working privacy objectives:

Data minimization:
- Process and retain only information needed for the intended workflow.

Authorization:
- Restrict access to prompts, chats, documents, retrieval results, generated artifacts, logs, and administrative data according to intended identity and tenant boundaries.

Provider and integration privacy:
- Make external data destinations explicit.
- Prevent unintended disclosure to model providers, connectors, MCP servers, tools, web services, or other integrations.

Sensitive-data handling:
- Avoid unnecessary exposure of credentials, secrets, personal data, and confidential organizational information.
- Sanitize evidence before sharing.

Logging and evidence:
- Collect sufficient security evidence without unnecessarily duplicating sensitive content.

Lifecycle:
- Define retention, deletion, revocation, and cleanup behavior for security-relevant data where applicable.

Local-lab requirement:
- Current security-testing evidence and fixtures remain synthetic-only under Phase 0.

Limitations:
- These are assessment objectives.
- They do not establish an upstream privacy policy, legal basis, retention schedule, or regulatory conclusion.

Evidence source:
- docs/security/00-scope-and-rules-of-engagement.md
- README.md
- SECURITY.md
- docs/security/evidence/phase1-governance-objectives-evidence.md

## 16. Safety Objectives

Working safety objectives:

Delegated actions:
- Prevent AI-mediated actions from exceeding user intent or approved authority.

Human control:
- Preserve meaningful human control for security-sensitive decisions and irreversible or high-impact actions where applicable.

Failure behavior:
- Stop or fail safely when authorization, scope, destination, data classification, or system state is uncertain.

Resource safety:
- Prevent uncontrolled loops, resource exhaustion, runaway tool execution, and cascading failures.

Integration safety:
- Prevent untrusted content, tools, connectors, or external services from silently changing the effective security boundary.

Recovery:
- Maintain bounded rollback, teardown, and recovery procedures for local security work.

Formal safety classification:
- NOT YET ASSIGNED.
- No current evidence establishes that the assessed deployment is a regulated safety-critical system.

Evidence source:
- docs/security/00-scope-and-rules-of-engagement.md
- README.md
- docs/security/evidence/phase1-governance-objectives-evidence.md

## 17. Governance Roles

Local security-engagement roles:

Authorization owner:
- amaw535353-ai, as recorded in the approved Phase 0 authorization.

Authorized tester/local operator:
- Ahmed.

Local security decision owner:
- Ahmed is accountable for deciding whether testing remains within the approved local scope and for stopping when authorization, safety, cost, or scope becomes uncertain.

Upstream security-reporting recipient:
- Onyx maintainers through the project's private vulnerability-reporting process when a verified upstream finding requires disclosure.

Upstream organizational roles NOT established from current evidence:
- Product owner.
- Engineering owner.
- Security owner.
- Privacy owner.
- Legal/compliance owner.
- Data owner.
- Enterprise risk owner.
- Release approver.

Important boundary:
- Local repository ownership and local testing authorization do not make Ahmed an upstream Onyx product owner or upstream release authority.

Evidence source:
- docs/security/00-scope-and-rules-of-engagement.md
- SECURITY.md
- docs/security/evidence/phase1-governance-objectives-evidence.md

## 18. RACI

This RACI applies only to the authorized local learning/security engagement.
It does not assign roles inside the upstream Onyx organization.

| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Define local test scope | Ahmed | Ahmed as local authorization owner | Security references/tooling as needed | N/A |
| Approve material scope change | Ahmed | Ahmed as local authorization owner | Relevant evidence/reference material | N/A |
| Execute authorized local tests | Ahmed | Ahmed | Security tooling/AI assistance as applicable | N/A |
| Interpret security evidence | Ahmed | Ahmed | Security tooling/AI assistance as applicable | N/A |
| Implement local remediation | Ahmed | Ahmed | Engineering/security assistance as applicable | N/A |
| Retest local remediation | Ahmed | Ahmed | Security tooling/AI assistance as applicable | N/A |
| Accept residual local-lab risk | Ahmed | Ahmed | Relevant evidence/reference material | N/A |
| Stop unsafe or uncertain testing | Ahmed | Ahmed | N/A | N/A |
| Submit verified upstream finding | Ahmed | Ahmed | Upstream security policy | Onyx maintainers through private reporting |

Governance limitation:
- AI tools, scanners, scripts, and other automation may provide evidence or assistance but are not accountable risk owners or approval authorities.
- Upstream product release decisions remain outside this local RACI.

## 19. Security Champions

Upstream organizational security champion:
- NOT IDENTIFIED FROM CURRENT EVIDENCE.

Local engagement:
- Ahmed performs the local security-engineering role for this authorized learning project.
- This local role should not be represented as an official upstream Onyx organizational title.

Future real-world expectation:
- For an organizational engagement, identify named security champions or equivalent engineering contacts for affected product areas and record escalation paths.

Evidence source:
- Current local Phase 0 authorization.
- Current repository evidence does not identify an upstream security-champion program.

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
