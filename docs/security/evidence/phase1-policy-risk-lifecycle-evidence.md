# Phase 1 - Policy, Risk and Lifecycle Evidence

Captured: 2026-09-14T11:07:03+01:00
Commit: 1a7388f26c78722fc2d2391de001acd24536add1
Branch: security/phase-1-product-context

## Source Hashes

```text
3f7862e5ff019e4696a5658c6472c58ccc4ad57929ab907df2c4f31c4daa50a2  docs/security/00-scope-and-rules-of-engagement.md
e39914852464f0e02b72f813876a62bb3ecca902b55a08201bc044dd17e9f375  README.md
0ed1f2a9c324b8ab2f6a17d8b4dd45875a6a4c9951f7240c99da21d1e1f0e729  SECURITY.md
8a0c6016e0cc913c6c1d5137b237618ffd2b78dda10cd38c1730ed8abb3da04a  CONTRIBUTING.md
d4847240794058c7ac3cfdf8e5d528fe8b0edf15b32a96612ecb9b3e182092b7  LICENSE
```

## Security Policy

```text
1:# Security Policy
6:## Supported Versions
12:## Reporting a Vulnerability
34:## Response Expectations
47:## Scope
64:## Safe Harbor
```

## Contribution Governance

```text
8:- [Contribution Process](#contribution-process)
24:- [Release Process](#release-process)
38:## Contribution Process
43:### 1. Get the feature or enhancement approved
51:### 2. Get the design approved
59:### 4. Review and testing
507:## Release Process
```

## Licensing

```text
103:## 📚 Licensing
107:- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
108:- Onyx Enterprise Edition (EE) includes extra features that are primarily useful for larger organizations.

Copyright (c) 2023-present DanswerAI, Inc.

Portions of this software are licensed as follows:

- All content that resides under "ee" directories of this repository is licensed under the Onyx Enterprise License. Each ee directory contains an identical copy of this license at its root:
  - backend/ee/LICENSE
  - web/src/app/ee/LICENSE
  - web/src/ee/LICENSE
- All third party components incorporated into the Onyx Software are licensed under the original license provided by the owner of the applicable component.
- Content outside of the above mentioned directories or restrictions above is available under the "MIT Expat" license as defined below.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Local Risk Governance

```text
18:Authorization owner: amaw535353-ai — owner of the GitHub repository
19:Authorized tester: Ahmed — local lab operator
62:Memory limits: Intentional memory-exhaustion testing is prohibited. Stop immediately if testing creates host instability or abnormal memory pressure.
65:Cost restrictions: No paid APIs, billable cloud resources, paid SaaS, metered external services, or other activity that can create an unapproved charge. Stop immediately if a test may create a charge.
69:Stop immediately if a test reaches an external or out-of-scope service; encounters real customer data or a real production credential; exceeds approved request, concurrency, time, token, memory, storage, or network limits; may create an unapproved charge; causes unexpected instability; or if authorization or scope becomes uncertain.
79:Rollback procedure: Restore changed tracked files from Git or revert the security change commit; stop affected local services; remove temporary synthetic test artifacts only after required evidence is preserved; and verify the repository and lab return to the approved baseline.
80:Teardown procedure: Stop local test services and containers; remove temporary synthetic credentials and test data when no longer needed; verify no unintended listeners or external connections remain; preserve sanitized evidence and reports; and confirm the Git working state.
119:Authorization owner approval: amaw535353-ai — repository owner
120:Authorized tester acknowledgement: Ahmed — local lab operator
126:Reapproval requirement: Any material change to scope, network boundary, targets, data classification, external integrations, cost exposure, or testing limits requires review before testing continues.
134:Authorization owner approval: amaw535353-ai — repository owner
135:Authorized tester acknowledgement: Ahmed — local lab operator
```
