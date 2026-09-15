# Phase 6 Local Mock-Service Contract
## Purpose
Define deterministic, loopback-only mock services for later controlled Onyx
runtime security verification.
Action 6.12 defines the contract only.
No service is started by this action.
## Global Safety Rules
Every mock must:
- bind only to `127.0.0.1`;
- make no intentional outbound network connection;
- use synthetic data only;
- use synthetic credentials only;
- never proxy to a real external service;
- return deterministic responses;
- support clean startup and shutdown;
- expose a health check;
- produce bounded evidence logs;
- enforce bounded request and response sizes.
## Global Resource Limits
| Control | Maximum |
|---|---|
| Concurrent requests | 10 |
| Requests per test | 100 |
| Request body | 1 MB |
| Generated response | 1 MB |
| Test duration | 60 seconds |
| Network binding | 127.0.0.1 only |
| Outbound internet | prohibited |
| Production credentials | prohibited |
| Production/customer data | prohibited |
## Evidence Fields
Where applicable, each mock should record:
- timestamp;
- request ID;
- correlation ID;
- service name;
- HTTP method;
- path;
- content length;
- synthetic tenant identifier;
- synthetic user identifier;
- selected scenario;
- status code;
- elapsed time.
Secret values must not be logged.
## MOCK-LLM
Endpoint:
`http://127.0.0.1:18080`
Purpose:
Provide deterministic local generation without contacting a real LLM
provider.
Required concepts:
- `GET /health`;
- synthetic model identifier `mock-security-model`;
- minimum generation API required by the selected Onyx integration;
- deterministic streaming support when required.
Required scenarios:
- `normal-answer`;
- `echo-context-ids`;
- `request-tool-alpha`;
- `request-tool-beta`;
- `prompt-injection-follow`;
- `streaming-answer`;
- `model-error`;
- `slow-response`.
Security invariant:
Model output is not authorization.
The mock may request an unauthorized operation so that Onyx authorization can
be tested independently.
## MOCK-EMBEDDING
Endpoint:
`http://127.0.0.1:18081`
Purpose:
Return deterministic synthetic vectors without downloading or invoking a real
embedding model.
Requirements:
- `GET /health`;
- same normalized input produces same vector;
- fixed vector size;
- bounded input and batch size;
- no external model download;
- no external embedding provider.
## MOCK-RERANKER
Endpoint:
`http://127.0.0.1:18082`
Purpose:
Return deterministic ranking results.
Required scenarios:
- normal ranking;
- adversarial document ranked first;
- unauthorized candidate supplied;
- empty candidate set;
- duplicate candidate set.
Security invariant:
Reranker output must not create authorization.
## MOCK-MCP
Endpoint:
`http://127.0.0.1:18083`
Purpose:
Provide a local MCP capability boundary.
Synthetic servers:
- `MCP-ALPHA-001`;
- `MCP-BETA-001`.
Synthetic Alpha tools:
- `alpha.search`;
- `alpha.read_profile`;
- `alpha.create_local_ticket`.
Synthetic Beta tools:
- `beta.search`;
- `beta.read_profile`;
- `beta.create_local_ticket`.
Required protocol concepts:
- initialization;
- tool discovery;
- tool invocation.
Implement only the exact protocol surface required by the selected Onyx MCP
client path.
Required adversarial scenarios:
- `malicious-tool-description`;
- `malicious-tool-result`;
- `cross-tenant-tool-list`;
- `oversized-result`;
- `tool-error`.
State-changing actions may affect local synthetic state only.
## MOCK-WEBHOOK
Endpoint:
`http://127.0.0.1:18084`
Purpose:
Observe state-changing actions locally.
Required concepts:
- `GET /health`;
- local event receiver;
- bounded request recording.
The webhook acts as a tripwire.
If an operation is expected to be denied but an event arrives, that becomes
security evidence.
## MOCK-EMAIL
Endpoint:
`http://127.0.0.1:18085`
Purpose:
Capture synthetic email actions without using a real mail provider.
Allowed recipients must end in:
`.test`
Examples:
- `alice@tenant-alpha.test`;
- `bob@tenant-beta.test`.
Non-test recipients must fail closed.
No SMTP relay or external email provider is allowed.
## MOCK-FILE
Endpoint:
`http://127.0.0.1:18086`
Purpose:
Provide a controlled local file/object boundary.
Conceptual operations:
- health;
- create object;
- read object;
- delete object;
- list object identifiers.
Restrictions:
- temporary lab directory only;
- generated synthetic filenames;
- no caller-controlled absolute paths;
- no `..` traversal;
- maximum object size 1 MB;
- no host-sensitive directories.
## Correlation IDs
Later runtime tests should use identifiers such as:
`TEST-P6-<case>-<sequence>`
Where possible, propagate the same identifier through:
test runner -> Onyx -> mock service -> evidence log.
## Determinism
The same request and scenario should produce the same result.
If randomness is ever required:
- use a fixed seed;
- record the seed.
## Controlled Failure Modes
Mocks may explicitly simulate:
- HTTP error;
- timeout;
- malformed response;
- empty response;
- oversized but bounded response;
- duplicate result;
- stale synthetic result.
Failures must be intentionally selected, never random.
## Outbound-Network Invariant
Mock implementation must not intentionally forward traffic to:
- OpenAI;
- Anthropic;
- Google;
- Microsoft;
- AWS;
- external MCP servers;
- real webhook destinations;
- real email services;
- other internet hosts.
A localhost proxy that forwards externally is also prohibited.
## Stop Conditions
Stop immediately if:
- unexpected external connectivity occurs;
- a real credential appears;
- real customer or production data appears;
- request size exceeds 1 MB;
- concurrency exceeds 10;
- requests exceed 100;
- execution exceeds 60 seconds;
- scope becomes uncertain;
- a service binds beyond loopback.
## Implementation Gate
Before implementing any mock:
1. inspect the exact Onyx interface;
2. implement only the minimum required protocol;
3. bind to loopback;
4. add self-tests;
5. verify no intentional external forwarding;
6. start one service at a time;
7. verify listening address and process identity;
8. verify clean shutdown and port release.
## Runtime Evidence Required Later
For each implemented mock collect:
- source code;
- startup command;
- process ID;
- listening address;
- health-check result;
- self-test result;
- request log;
- outbound-network observation;
- shutdown command;
- post-shutdown port check.
## Result
The mock-service architecture is designed to increase test realism while
keeping external risk, cost and data exposure bounded.
