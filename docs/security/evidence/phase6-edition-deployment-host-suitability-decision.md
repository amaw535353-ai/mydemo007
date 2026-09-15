# Phase 6 Action 6.13 - Edition, Deployment Mode and Host Suitability Decision
## Verified Target
- Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source modified: NO
- Evidence parent: `97bf9e961f856fe49b1acca9895759bc368c6f97`
## Host Facts
- Kernel: `4.4.0-19041-Microsoft`
- WSL indicator: `DETECTED`
- CPU: `Intel(R) Pentium(R) CPU        P6100  @ 2.00GHz`
- Logical processors: `2`
- Memory: approximately `7.68 GiB`
- Free disk at Onyx path: `12G`
- Docker client: `NOT_INSTALLED`
No Docker daemon was started or queried by this action.
## Deployment Files
Standard compose:
`deployment/docker_compose/docker-compose.yml`
Lite compose:
`deployment/docker_compose/docker-compose.onyx-lite.yml`
## Raw Service Counts
- Standard compose services: 11
- Lite compose services: 7
### Standard raw services
```
api_server
background
cache
code-interpreter
indexing_model_server
inference_model_server
minio
nginx
opensearch
relational_db
web_server
```
### Lite raw services
```
api_server
background
cache
indexing_model_server
inference_model_server
minio
opensearch
```
## Lite Invocation Evidence
Repository references found: 21
Classification:
`COMPOSE_OVERRIDE_COMBINATION_OBSERVED`
This classification is based on static repository evidence only.
## Host Suitability Decision
### Full Standard local runtime
**DEFERRED**
Reason:
The local host has limited memory/CPU resources relative to the number of
Onyx services and AI/indexing dependencies observed during Phase 6.
Running the complete Standard topology is therefore not selected as the first
baseline.
### Selective local baseline
**APPROVED**
A minimal/selective service set may be used after the reproducible-build
requirement is completed and exact dependencies are verified.
### Mock-assisted baseline
**APPROVED**
Local deterministic mocks are the preferred substitute for external LLM,
embedding, reranking, MCP and other external dependencies where technically
compatible with the selected Onyx path.
### Full application startup
**NOT AUTHORIZED YET**
This action does not authorize application startup.
The next requirement must establish a reproducible installation/build plan,
exact prerequisites, commands, versions, external-call controls and rollback
before startup.
## Security Reasoning
The selected baseline optimizes for:
- reproducibility;
- zero paid APIs;
- synthetic data;
- bounded resource use;
- loopback-controlled dependencies;
- observable security behavior;
- preservation of the pinned Onyx source.
It intentionally sacrifices production-scale realism that this local host
cannot safely reproduce.
## Requirement Mapping
This action closes original Phase 6 requirement:
**R6.5 - Edition / Deployment-Mode Decision + Local Resource Suitability**
## Result
Action 6.13 deployment-mode and host-suitability decision: **PASS**.
