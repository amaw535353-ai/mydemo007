# Phase 3 - Networking, Web, API, Identity, and Cryptography Foundations

## Phase status

Phase 3 status: **IN PROGRESS**.

## Baseline

- Phase 3 starting commit: `349dee89221347306180917645f6e9ba2e24eb9b`
- Working branch: `security/phase-3-foundations`
- Phase 2 static inventory: COMPLETE

## Action 3.2 - Network Architecture and Protocol Foundations

Status: **COMPLETE**.

### What

Identify source-level network architecture and protocol candidates and connect them to security engineering concepts.

### Where

Tracked project source and configuration files, excluding `docs/security/` evidence content.

### Why

An AI application security engineer must understand how clients, services, APIs, data stores, model providers, agents, tools, and infrastructure communicate before evaluating trust boundaries, authentication, encryption, exposure, SSRF, request routing, tenant isolation, or network-based attack paths.

### Network model

The following conceptual layers will be used during later security analysis:

- **Name resolution:** DNS converts names into reachable targets.
- **Network layer:** IP identifies network endpoints.
- **Transport layer:** TCP and UDP carry application traffic.
- **Application layer:** HTTP, HTTPS, WebSocket, gRPC, SMTP and service-specific protocols carry application semantics.
- **Transport protection:** TLS protects confidentiality and integrity when correctly configured.
- **Exposure controls:** bind addresses, listeners, ports, proxies, ingress and egress determine reachability.
- **Trust boundaries:** every transition between clients, services, tenants, tools, data stores and external providers must eventually be validated rather than assumed.

### Static observations

- HTTP: 1128 candidate files, 2962 matching lines.
- HTTPS: 916 candidate files, 8082 matching lines.
- TCP: 86 candidate files, 176 matching lines.
- UDP: 4 candidate files, 10 matching lines.
- WebSocket: 42 candidate files, 380 matching lines.
- gRPC: 11 candidate files, 87 matching lines.
- DNS: 98 candidate files, 229 matching lines.
- TLS_SSL: 127 candidate files, 552 matching lines.
- SMTP: 11 candidate files, 28 matching lines.
- PostgreSQL: 488 candidate files, 1454 matching lines.
- Redis: 356 candidate files, 1866 matching lines.

Network-control candidates:

- bind_listen: 182 candidate files, 603 matching lines.
- port: 420 candidate files, 2087 matching lines.
- proxy_upstream: 375 candidate files, 1568 matching lines.
- ingress: 38 candidate files, 108 matching lines.
- egress: 102 candidate files, 230 matching lines.
- network: 246 candidate files, 600 matching lines.
- loopback: 240 candidate files, 623 matching lines.
- wildcard_bind: 216 candidate files, 1098 matching lines.

### Security interpretation

These results establish where network and protocol concepts appear in source, but they do not prove which services are running, which ports are reachable, which protocol versions are negotiated, whether TLS is enforced, whether ingress/egress controls are effective, or whether any specific trust boundary is secure.

Runtime behavior remains deliberately unverified and will be tested only in later controlled local-lab actions.

### Evidence

`docs/security/evidence/phase3-network-protocol-foundations-evidence.md`

### Completion criteria

- Static protocol candidates enumerated: PASS
- Network-control candidates enumerated: PASS
- Candidate configuration surfaces identified: PASS
- Source-vs-runtime distinction preserved: PASS
- No external active testing performed: PASS

## Phase 3 Completion Gate

Phase 3 remains **IN PROGRESS**.
