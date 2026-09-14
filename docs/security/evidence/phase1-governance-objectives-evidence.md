# Phase 1 - Governance and Security Objectives Evidence

Captured: 2026-09-14T10:50:57+01:00
Commit: 10101219493932f3d1a4d146a72a6a5343d1b01e
Branch: security/phase-1-product-context

## Source Hashes

```text
3f7862e5ff019e4696a5658c6472c58ccc4ad57929ab907df2c4f31c4daa50a2  docs/security/00-scope-and-rules-of-engagement.md
e39914852464f0e02b72f813876a62bb3ecca902b55a08201bc044dd17e9f375  README.md
0ed1f2a9c324b8ab2f6a17d8b4dd45875a6a4c9951f7240c99da21d1e1f0e729  SECURITY.md
```

## Phase 0 Local Risk-Governance Evidence

```text
18:Authorization owner: amaw535353-ai — owner of the GitHub repository
19:Authorized tester: Ahmed — local lab operator
31:Agents: Onyx agent and persona functionality and its authorization boundaries are in scope for local synthetic testing. Only agents operating inside the approved local lab are in scope.
32:Tools and actions: Onyx custom tools and actions, including OpenAPI and MCP-associated actions, are in scope only when configured against approved local synthetic services. External actions and real third-party side effects are prohibited.
34:Connectors: Onyx connector framework, mock connector, and federated-connector code are in scope for source review. Active connector testing is limited to local mock or synthetic connectors; real third-party connectors and accounts remain out of scope.
42:Permitted techniques include read-only source-code and configuration review; architecture and data-flow analysis; threat modeling; local static analysis; dependency, SBOM, and secret-pattern scanning; and creation of defensive patches, tests, and documentation. After the Approval Gate is satisfied, bounded dynamic security testing is permitted only against approved local loopback services using synthetic identities, synthetic data, and fake or locally generated credentials.
46:Prohibited techniques include testing public, LAN, production, third-party, or otherwise out-of-scope systems; use of real customer data or production credentials; intentional denial-of-service or unbounded resource exhaustion; destructive modification or deletion of non-synthetic data; persistence, malware deployment, or lateral movement outside the approved local lab; social engineering of real people; attempts to access real third-party accounts; uncontrolled credential attacks; bypassing the approved loopback network boundary; and any technique whose scope, impact, cost, or authorization is uncertain.
50:Synthetic-data requirements: All test documents, prompts, records, conversations, files, and datasets must be synthetic.
51:Synthetic-identity requirements: All test users, tenants, organizations, email addresses, and identities must be synthetic lab identities.
56:Test windows: Active security testing is permitted only during attended local-lab sessions under the authorized tester's supervision. Unattended or overnight active testing is prohibited unless separately reviewed and approved. Each individual active test remains subject to the documented 60-second maximum.
58:Rate limits: Maximum 100 requests per individual active security test unless a lower test-specific ceiling is defined.
59:Concurrency limits: Maximum 10 simultaneous requests during active security testing.
60:Token limits: No unbounded token-generation or agent loops. Test-specific token ceilings must be defined before model or agent stress testing.
61:Time limits: Maximum 60 seconds per individual active security test unless stopped earlier.
62:Memory limits: Intentional memory-exhaustion testing is prohibited. Stop immediately if testing creates host instability or abnormal memory pressure.
63:Storage limits: Maximum 1 MB per individual test file unless a smaller test-specific limit is defined. Unbounded disk writes are prohibited.
64:External-network restrictions: Active security testing is restricted to the local loopback lab. No active testing against LAN systems, public Internet targets, or external services.
65:Cost restrictions: No paid APIs, billable cloud resources, paid SaaS, metered external services, or other activity that can create an unapproved charge. Stop immediately if a test may create a charge.
69:Stop immediately if a test reaches an external or out-of-scope service; encounters real customer data or a real production credential; exceeds approved request, concurrency, time, token, memory, storage, or network limits; may create an unapproved charge; causes unexpected instability; or if authorization or scope becomes uncertain.
71:Escalation contacts: Primary local escalation contact is Ahmed — repository owner and local lab operator. Testing must stop and be escalated to the authorization owner if scope, authorization, safety, data classification, network exposure, cost, or system stability becomes uncertain. Upstream or third-party security issues must be escalated through the project's verified official private security-reporting channel.
75:Preserve reproducible commands, timestamps, relevant logs, synthetic identifiers, diffs, test outputs, and screenshots with sufficient context. Evidence must not contain real credentials, production secrets, real customer data, or unnecessary personal data. Sanitize sensitive values before sharing or publishing.
79:Rollback procedure: Restore changed tracked files from Git or revert the security change commit; stop affected local services; remove temporary synthetic test artifacts only after required evidence is preserved; and verify the repository and lab return to the approved baseline.
80:Teardown procedure: Stop local test services and containers; remove temporary synthetic credentials and test data when no longer needed; verify no unintended listeners or external connections remain; preserve sanitized evidence and reports; and confirm the Git working state.
84:Security findings that affect an upstream or third-party project must be reported privately through its official security or vulnerability-reporting channel after checking the applicable disclosure policy. Preserve a synthetic reproduction and evidence, avoid public exploit details during the private investigation window, coordinate remediation and retesting, and document residual risk. Findings confined to this authorized local learning copy may remain private portfolio evidence after sanitization.
119:Authorization owner approval: amaw535353-ai — repository owner
120:Authorized tester acknowledgement: Ahmed — local lab operator
124:Approval boundary: Local loopback lab only; synthetic identities, data, and credentials only; no real external providers, third-party accounts, public targets, paid services, or unapproved costs.
125:Approval limits: Maximum 100 requests per individual active test, maximum 10 concurrent requests, maximum 60 seconds per individual active test, maximum 1 MB individual test file, and no unbounded resource or agent loops.
126:Reapproval requirement: Any material change to scope, network boundary, targets, data classification, external integrations, cost exposure, or testing limits requires review before testing continues.
134:Authorization owner approval: amaw535353-ai — repository owner
135:Authorized tester acknowledgement: Ahmed — local lab operator
```

## Product-Control Evidence

```text
31:Onyx enables LLMs through advanced capabilities like RAG, web search, code execution, file creation, deep research and more.
33:Connect your applications with over 50+ indexing based connectors provided out of the box or via MCP.
47:- **🔍 Agentic RAG:** Get best in class search and answer quality based on hybrid index + AI Agents for information retrieval
51:- **🤖 Custom Agents:** Build AI Agents with unique instructions, knowledge, and actions.
56:- **▶️ Actions & MCP:** Let Onyx agents interact with external applications, comes with flexible Auth options.
57:- **💻 Code Execution:** Execute code in a sandbox to analyze data, render graphs, or modify files.
77:It is great for users who want to test out Onyx quickly or for teams who are only interested in the Chat UI and Agents functionalities.
82:- Vector + Keyword index for RAG.
83:- Background containers to run job queues and workers for syncing knowledge from connectors.
95:- 👥 Collaboration: Share chats and agents with other members of your organization.
96:- 🔐 Single Sign On: SSO via Google OAuth, OIDC, or SAML. Group syncing and user provisioning via SCIM.
97:- 🛡️ Role Based Access Control: RBAC for sensitive resources like access to agents, actions, etc.
99:- 🕵️ Query History: Audit usage to ensure safe adoption of AI in your organization.
100:- 💻 Custom code: Run custom code to remove PII, reject sensitive queries, or to run custom analysis.
107:- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
```

## Security-Governance Evidence

```text
4:keep Onyx and its community safe by practicing responsible disclosure.
18:Instead, please use **GitHub Private Vulnerability Reporting** to file a
21:creates a private advisory visible only to the maintainers and ensures
38:- We will work with you to validate the issue and agree on a disclosure
43:- Once a fix is available, we will coordinate public disclosure (release
64:## Safe Harbor
69:- Avoid privacy violations, data destruction, or service degradation.
71:  disclosure.
```
