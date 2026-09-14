# Phase 1 - AI Classification and Risk Context Evidence

Captured: 2026-09-14T10:37:02+01:00
Commit: eb5991568cf3f8b4947b68950da210326edee687
Branch: security/phase-1-product-context

## Source Hashes

```text
e39914852464f0e02b72f813876a62bb3ecca902b55a08201bc044dd17e9f375  README.md
0ed1f2a9c324b8ab2f6a17d8b4dd45875a6a4c9951f7240c99da21d1e1f0e729  SECURITY.md
```

## AI-System Evidence

```text
28:# Onyx - The Open Source AI Platform
30:**[Onyx](https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)** is the application layer for LLMs - bringing a feature-rich interface that can be easily hosted by anyone.
31:Onyx enables LLMs through advanced capabilities like RAG, web search, code execution, file creation, deep research and more.
47:- **🔍 Agentic RAG:** Get best in class search and answer quality based on hybrid index + AI Agents for information retrieval
51:- **🤖 Custom Agents:** Build AI Agents with unique instructions, knowledge, and actions.
56:- **▶️ Actions & MCP:** Let Onyx agents interact with external applications, comes with flexible Auth options.
57:- **💻 Code Execution:** Execute code in a sandbox to analyze data, render graphs, or modify files.
61:Onyx supports all major LLM providers, both self-hosted (like Ollama, LiteLLM, vLLM, etc.) and proprietary (like Anthropic, OpenAI, Gemini, etc.).
74:#### Onyx Lite
79:#### Standard Onyx
82:- Vector + Keyword index for RAG.
107:- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
```

## Impact-Surface Evidence

```text
31:Onyx enables LLMs through advanced capabilities like RAG, web search, code execution, file creation, deep research and more.
33:Connect your applications with over 50+ indexing based connectors provided out of the box or via MCP.
47:- **🔍 Agentic RAG:** Get best in class search and answer quality based on hybrid index + AI Agents for information retrieval
56:- **▶️ Actions & MCP:** Let Onyx agents interact with external applications, comes with flexible Auth options.
57:- **💻 Code Execution:** Execute code in a sandbox to analyze data, render graphs, or modify files.
82:- Vector + Keyword index for RAG.
83:- Background containers to run job queues and workers for syncing knowledge from connectors.
95:- 👥 Collaboration: Share chats and agents with other members of your organization.
96:- 🔐 Single Sign On: SSO via Google OAuth, OIDC, or SAML. Group syncing and user provisioning via SCIM.
97:- 🛡️ Role Based Access Control: RBAC for sensitive resources like access to agents, actions, etc.
98:- 📊 Analytics: Usage graphs broken down by teams, LLMs, or agents.
99:- 🕵️ Query History: Audit usage to ensure safe adoption of AI in your organization.
100:- 💻 Custom code: Run custom code to remove PII, reject sensitive queries, or to run custom analysis.
107:- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
```

## Security-Exposure Evidence

```text
49:In scope:
51:- The Onyx application code in this repository (backend, web, desktop, CLI,
52:  connectors, deployment manifests).
53:- Official Onyx-published Docker images and Helm charts.
55:Out of scope:
69:- Avoid privacy violations, data destruction, or service degradation.
```
