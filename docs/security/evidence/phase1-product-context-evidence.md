# Phase 1 - Product Context Source Evidence

Captured: 2026-09-14T10:33:36+01:00
Commit: 7137a088a02e16ddae19404398d50c5be2229305
Branch: security/phase-1-product-context

## Source Hashes

```text
e39914852464f0e02b72f813876a62bb3ecca902b55a08201bc044dd17e9f375  README.md
0ed1f2a9c324b8ab2f6a17d8b4dd45875a6a4c9951f7240c99da21d1e1f0e729  SECURITY.md
8a0c6016e0cc913c6c1d5137b237618ffd2b78dda10cd38c1730ed8abb3da04a  CONTRIBUTING.md
d4847240794058c7ac3cfdf8e5d528fe8b0edf15b32a96612ecb9b3e182092b7  LICENSE
```

## README Product Evidence

```text
28:# Onyx - The Open Source AI Platform
30:**[Onyx](https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)** is the application layer for LLMs - bringing a feature-rich interface that can be easily hosted by anyone.
31:Onyx enables LLMs through advanced capabilities like RAG, web search, code execution, file creation, deep research and more.
47:- **🔍 Agentic RAG:** Get best in class search and answer quality based on hybrid index + AI Agents for information retrieval
49:- **🔬 Deep Research:** Get in depth reports with a multi-step research flow.
51:- **🤖 Custom Agents:** Build AI Agents with unique instructions, knowledge, and actions.
56:- **▶️ Actions & MCP:** Let Onyx agents interact with external applications, comes with flexible Auth options.
57:- **💻 Code Execution:** Execute code in a sandbox to analyze data, render graphs, or modify files.
61:Onyx supports all major LLM providers, both self-hosted (like Ollama, LiteLLM, vLLM, etc.) and proprietary (like Anthropic, OpenAI, Gemini, etc.).
67:## 🚀 Deployment Modes
74:#### Onyx Lite
79:#### Standard Onyx
82:- Vector + Keyword index for RAG.
94:Onyx is built for teams of all sizes, from individual users to the largest global enterprises:
95:- 👥 Collaboration: Share chats and agents with other members of your organization.
96:- 🔐 Single Sign On: SSO via Google OAuth, OIDC, or SAML. Group syncing and user provisioning via SCIM.
97:- 🛡️ Role Based Access Control: RBAC for sensitive resources like access to agents, actions, etc.
99:- 🕵️ Query History: Audit usage to ensure safe adoption of AI in your organization.
107:- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
```

## SECURITY.md

```text
# Security Policy

We take the security of Onyx and our users seriously. Thank you for helping
keep Onyx and its community safe by practicing responsible disclosure.

## Supported Versions

Security fixes are applied to the `main` branch and the latest tagged release.
We strongly recommend running the most recent release of Onyx. Older releases
are not guaranteed to receive backported security patches.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues,
pull requests, or discussions.** Public reports give attackers a head start
and put other users at risk before a fix is available.

Instead, please use **GitHub Private Vulnerability Reporting** to file a
report at
<https://github.com/onyx-dot-app/onyx/security/advisories/new>. This
creates a private advisory visible only to the maintainers and ensures
your report is tracked rather than landing in an individual inbox.

Please include as much of the following as you can — it helps us triage
faster:

- A description of the issue and the impact you believe it has.
- The Onyx version, deployment type (self-hosted, Onyx Cloud, Docker, Helm,
  etc.), and any relevant configuration.
- Step-by-step reproduction instructions or a proof-of-concept.
- Any logs, screenshots, or sample payloads that demonstrate the issue.
- Your name and a way to credit you in the advisory, if desired.

## Response Expectations

After you report a vulnerability:

- We will work with you to validate the issue and agree on a disclosure
  timeline. Typical investigations take **up to 90 days**, though many issues
  are resolved sooner.
- We will keep you informed of progress and let you know when a fix is
  released.
- Once a fix is available, we will coordinate public disclosure (release
  notes, GitHub Security Advisory, and CVE if applicable) and are happy to
  credit reporters who would like recognition.

## Scope

In scope:

- The Onyx application code in this repository (backend, web, desktop, CLI,
  connectors, deployment manifests).
- Official Onyx-published Docker images and Helm charts.

Out of scope:

- Third-party services and integrations (please report those to the
  respective vendors).
- Findings that require access to a user's account or device, social
  engineering, or physical attacks.
- Denial-of-service issues caused solely by sending high volumes of traffic.
- Automated scanner output without a demonstrated, exploitable impact.

## Safe Harbor

We will not pursue or support legal action against researchers who:

- Make a good-faith effort to follow this policy.
- Avoid privacy violations, data destruction, or service degradation.
- Give us a reasonable opportunity to remediate before any public
  disclosure.

Thank you for helping keep Onyx and our community secure.
```

## CONTRIBUTING.md

```text
# Contributing to Onyx

Hey there! We are so excited that you're interested in Onyx.

## Table of Contents

- [Contribution Opportunities](#contribution-opportunities)
- [Contribution Process](#contribution-process)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Backend: Python Requirements](#backend-python-requirements)
  - [Frontend: Node Dependencies](#frontend-node-dependencies)
  - [Formatting and Linting](#formatting-and-linting)
- [Running the Application](#running-the-application)
  - [VSCode Debugger (Recommended)](#vscode-debugger-recommended)
  - [Manually Running for Development](#manually-running-for-development)
  - [Running in Docker](#running-in-docker)
- [macOS-Specific Notes](#macos-specific-notes)
- [Engineering Best Practices](#engineering-best-practices)
  - [Principles and Collaboration](#principles-and-collaboration)
  - [Style and Maintainability](#style-and-maintainability)
  - [Performance and Correctness](#performance-and-correctness)
  - [Repository Conventions](#repository-conventions)
- [Release Process](#release-process)
- [Getting Help](#getting-help)
- [Enterprise Edition Contributions](#enterprise-edition-contributions)

---

## Contribution Opportunities

The [GitHub Issues](https://github.com/onyx-dot-app/onyx/issues) page is a great place to look for and share contribution ideas.

If you have your own feature that you would like to build, please create an issue and community members can provide feedback and upvote if they feel a common need.

---

## Contribution Process

To contribute, please follow the
["fork and pull request"](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow.

### 1. Get the feature or enhancement approved

Create a GitHub issue and see if there are upvotes. If you feel the feature is sufficiently value-additive and you would like approval to contribute it to the repo, tag [Yuhong](https://github.com/yuhongsun96) to review.

If you do not get a response within a week, feel free to email yuhong@onyx.app and include the issue in the message.

Not all small features and enhancements will be accepted as there is a balance between feature richness and bloat. We strive to provide the best user experience possible so we have to be intentional about what we include in the app.

### 2. Get the design approved

The Onyx team will either provide a design doc and PRD for the feature or request one from you, the contributor. The scope and detail of the design will depend on the individual feature.

### 3. IP attribution for EE contributions

If you are contributing features to Onyx Enterprise Edition, you are required to sign the [IP Assignment Agreement](contributor_ip_assignment/EE_Contributor_IP_Assignment_Agreement.md).

### 4. Review and testing

Your features must pass all tests and all comments must be addressed prior to merging.

### Implicit agreements

If we approve an issue, we are promising you the following:

- Your work will receive timely attention and we will put aside other important items to ensure you are not blocked.
- You will receive necessary coaching on eng quality, system design, etc. to ensure the feature is completed well.
- The Onyx team will pull resources and bandwidth from design, PM, and engineering to ensure that you have all the resources to build the feature to the quality required for merging.

Because this is a large investment from our team, we ask that you:

- Thoroughly read all the requirements of the design docs, engineering best practices, and try to minimize overhead for the Onyx team.
- Complete the feature in a timely manner to reduce context switching and an ongoing resource pull from the Onyx team.

---

## Development Setup

Onyx being a fully functional app, relies on some external software, specifically:

- [Postgres](https://www.postgresql.org/) (Relational DB)
- [OpenSearch](https://opensearch.org/) (Vector DB/Search Engine)
- [Redis](https://redis.io/) (Cache)
- [MinIO](https://min.io/) (File Store)
- [Nginx](https://nginx.org/) (Not needed for development flows generally)

> **Note:**
> This guide provides instructions to build and run Onyx locally from source with Docker containers providing the above external software.
> We believe this combination is easier for development purposes. If you prefer to use pre-built container images, see [Running in Docker](#running-in-docker) below.

### Prerequisites

- **Python 3.13** — Other versions may require code or dependency changes; 3.14 is not yet supported (some dependencies, e.g. `onnxruntime` and CUDA `torch`, do not yet ship 3.14 wheels).
- **Docker** — Required for running external services (Postgres, OpenSearch, Redis, MinIO).
- **Bun** — We use [bun](https://bun.sh) as the JavaScript package manager. Install it from https://bun.sh/docs/installation.

### Backend: Python Requirements

We use [uv](https://docs.astral.sh/uv/) and recommend creating a [virtual environment](https://docs.astral.sh/uv/pip/environments/#using-a-virtual-environment).

```bash
uv venv .venv --python 3.13
source .venv/bin/activate
```

_For Windows, activate the virtual environment using Command Prompt:_

```bash
.venv\Scripts\activate
```

If using PowerShell, the command slightly differs:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required Python dependencies:

```bash
uv sync
```

Install Playwright for Python (headless browser required by the Web Connector):

```bash
uv run playwright install
```

### Frontend: Node Dependencies

Navigate to `onyx/web` and run:

```bash
bun install
```

### Formatting and Linting

#### Backend

Set up pre-commit hooks (`ruff` / `ruff format`):

```bash
uv run pre-commit install
```

We also use `ty` for static type checking. Onyx is fully type-annotated, and we want to keep it that way! To run the ty checks manually:

```bash
uv run ty check
```

#### Frontend

We use `oxfmt` for formatting. The desired version will be installed via `bun install` from the `onyx/web` directory. To run the formatter:

```bash
bunx oxfmt .  # from onyx/web
```

Pre-commit will also run oxfmt automatically on files you've recently touched. If re-formatted, your commit will fail. Re-stage your changes and commit again.

We use `oxlint` for linting. The desired version will be installed via `bun install` from the `onyx/web` directory. To run the linter:

```bash
bunx oxlint  # from onyx/web
bunx oxlint --fix  # auto-fix what it can
```

Pre-commit will also run oxlint automatically. If it reports errors, fix them and commit again.

---

## Running the Application

### VSCode Debugger (Recommended)

We highly recommend using VSCode's debugger for development.
```
