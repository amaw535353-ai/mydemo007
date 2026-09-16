# Phase 6 Action 6.17 - Startup / Runtime Baseline Assessment

## Verified Baseline

- Parent evidence commit: `9a85c16e342408d6f8b27cb969d3a88af5e7a2da`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source modified: NO

## Purpose

Establish the maximum defensible startup/runtime baseline possible on the
current host without Docker, dependency installation, image downloads or an
Onyx application startup.

## Raw Deployment Topology

Standard Compose raw service count:

11

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

Lite override raw service count:

7

```
api_server
background
cache
indexing_model_server
inference_model_server
minio
opensearch
```

The Lite file is an override used with the base Compose definition.

Raw service declarations must therefore not be treated as the fully rendered
runtime topology.

## Startup-Control Evidence

Standard Compose startup-control signals:

47

Lite override startup-control signals:

2

Observed control classes include applicable:

- image/build declarations;
- commands and entrypoints;
- dependency declarations;
- health checks;
- published/listening port configuration;
- restart behavior.

## Health / Readiness Contract

Health/readiness source references observed:

534

Result:

**STATIC HEALTH CONTRACT MAPPED**

This does not prove that any endpoint successfully responded at runtime.

## Dependency Configuration

Deployment dependency/configuration references observed:

487

Observed architecture includes dependencies involving database, cache/search,
model-server and object-storage roles.

These are configuration/static architecture observations.

## Lite Startup Contract

Pinned-source Lite startup command references:

6

The repository provides evidence for merged Compose invocation involving:

`docker-compose.yml`

and:

`docker-compose.onyx-lite.yml`

## Current Runtime Tool State

```
docker=MISSING
uv=MISSING
bun=MISSING
node=MISSING
docker_compose=MISSING
```

## Startup Decision

### Static deployment topology

**PASS**

### Startup relationship / sequence mapping

**COMPLETE**

### Health/readiness contract mapping

**COMPLETE**

### Actual Onyx startup

**DEFERRED - ENVIRONMENT LIMIT**

### Live service health

**NOT OBSERVED**

### Runtime port/listener baseline

**NOT OBSERVED**

## Interpretation Boundary

This action does not claim:

- containers were created;
- images were pulled;
- dependencies were installed;
- Onyx processes executed;
- health endpoints responded;
- database migrations succeeded;
- background workers became ready;
- model servers became ready;
- browser traffic reached the API;
- runtime authorization worked.

## Original R6.7 Status

Original R6.7:

**Startup / service baseline**

Status:

**STATIC STARTUP BASELINE COMPLETE - LIVE RUNTIME PROOF DEFERRED**

The deferred portion is caused by the already documented execution
environment limitation.

## Result

Action 6.17 startup/runtime baseline assessment: **PASS**.
