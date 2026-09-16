# Phase 6 Action 6.16 - Local Build Feasibility Closure

## Verified Baseline

- Parent evidence commit: `4ef0b37442c57198efe7d20f133cfb084bf3fcf5`
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source modified: NO

## Purpose

Complete the maximum safe reproducibility validation available on the current
Debian/WSL host without installing dependencies, downloading packages,
starting Docker, or starting Onyx.

## Repository Version Requirements

```
requires-python=>=3.13
packageManager=bun@1.3.13
PASS: pinned version requirements verified
```

## Current Build Tools

```
python3=AVAILABLE
uv=MISSING
bun=MISSING
node=MISSING
npm=AVAILABLE
docker=MISSING
docker_compose=MISSING
```

## Structured Configuration Validation

The following classes were parsed successfully using already-installed Python:

- root Python project configuration;
- CLI Python project configuration;
- root JavaScript package configuration;
- web package configuration;
- devcontainer JSON configuration.

No dependency installation was required.

## Python Source Validation

Pinned backend Python files parsed:

500

Result:

**PASS**

The validation compiled source in memory and did not write bytecode or modify
the pinned source tree.

## Shell Script Validation

Shell scripts checked with `bash -n`:

3

Result:

**PASS**

## Reproducibility Input Hashes

```
25e28070f70656e82710024daa4f8c9fa8288ef8dbd5c7f5837d98ecc2a3b063  uv.lock
96599229fba386c9268987794da072036c3f16443f7b828004fc56c8d9b00b27  backend/uv.lock
6e1c7daa3a1ce53eede22d9a864e660c9ca4a35eb2579b402acfb1b236a55c46  package.json
```

These hashes identify the exact local reproducibility inputs associated with
the pinned Onyx revision.

## Lite Deployment Contract

The pinned repository contains:

- `deployment/docker_compose/docker-compose.yml`
- `deployment/docker_compose/docker-compose.onyx-lite.yml`

The Lite file documents merged Compose invocation with the base Compose file.

Static contract validation:

**PASS**

## Actual Build Limitation

A real dependency/container build was not executed.

Current host lacks required build/runtime tooling including some combination
of:

- `uv`;
- `bun`;
- Node.js;
- Docker;
- Docker Compose.

Installing these tools was outside this action's approved no-install boundary.

The host is also resource constrained relative to a complete Onyx topology.

## Remote Build Limitation

A Codespace was considered for build execution.

GitHub CLI authentication could not be completed reliably during setup, and
repeated authentication attempts were intentionally stopped.

No new credential was created and no paid resource was authorized.

Therefore remote build execution is:

**DEFERRED**

## R6.6 Interpretation

Original R6.6 requires reproducible installation/build.

Evidence now proves:

- pinned source: YES;
- version requirements identified: YES;
- manifests/lockfiles identified: YES;
- Lite invocation identified: YES;
- structured configuration parsing: YES;
- bounded Python source execution: YES;
- shell syntax checks: YES;
- reproducibility input hashes: YES;
- actual dependency synchronization: NO;
- container/image build: NO;
- complete application build: NO.

Status:

**MAXIMUM CURRENT-HOST VALIDATION COMPLETE — ACTUAL BUILD DEFERRED**

This is a documented environmental limitation, not evidence that a real build
succeeded.

## Result

Action 6.16 local build-feasibility closure: **PASS**.
