# Phase 6 Action 6.14 - Reproducible Installation and Build Plan
## Verified Target
- Onyx pinned SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Parent evidence commit: `75fabca832b38a41c3808285c5e854204031f353`
- Onyx source modified: NO
## Purpose
Establish a reproducible installation/build procedure before authorizing any
Onyx runtime startup.
No dependency was installed and no application component was built or started
during this action.
## Reproducibility Inputs
Tracked reproducibility-related files discovered: 50.
Examples and exact paths were derived from the pinned repository and include
available package manifests, lockfiles, Dockerfiles and Compose definitions.
## Version Signals
```
===== pyproject.toml =====
requires-python = ">=3.13"
    "python-json-logger==4.1.0",
    "atlassian-python-api==4.0.7",
    "google-api-python-client==2.86.0",
    # GPT4All library has issues running on Macs and python:3.11.4-slim-bookworm
    "Office365-REST-Python-Client==2.6.2",
    # `crypt` module, which was removed in Python 3.13.
    "python-dateutil==2.9.0.post0",
    "python-docx==1.1.2",
    "python-gitlab==5.6.0",
    "python-pptx==0.6.23",
    "python-dotenv==1.2.2",
    "python-slugify==8.0.4",
    "python3-saml==1.15.0",
    "types-python-dateutil==2.8.19.13",
# PYTHONPATH conventions (see backend/pytest.ini).
python-version = "3.13"
# when PYTHONPATH contains another checkout (e.g. when working in a git worktree
===== web/package.json =====
    "clean": "rm -rf .next node_modules/.cache *.tsbuildinfo",
    "types:check": "next typegen && node tools/type-check/index.ts",
    "test:debug": "node --inspect-brk node_modules/.bin/jest --runInBand",
    "@types/node": "24.12.2",
    "typescript-7": "npm:typescript@^7.0.2",
===== package.json =====
  "packageManager": "bun@1.3.13",
===== .python-version =====
```
These are repository observations.
They must be preferred over guessing current dependency versions.
## Install / Build Evidence
Repository command references discovered: 405.
Lite Compose command references discovered: 6.
Dockerfiles discovered: 9.
## Selected Deployment Procedure
The approved future baseline remains:
**Standard full local topology: DEFERRED**
**Lite/selective baseline: APPROVED FOR CONTROLLED VALIDATION**
**Mock-assisted external dependencies: APPROVED**
The Lite deployment is an override composition rather than an independent
standalone topology.
The repository contains invocation evidence combining:
`docker-compose.yml`
with:
`docker-compose.onyx-lite.yml`
Any actual command used later must be copied from or verified against the
pinned source before execution.
## Reproducible Future Workflow
The controlled future workflow is:
1. verify evidence repository and pinned Onyx SHA;
2. verify host prerequisites and versions;
3. verify sufficient free disk and memory;
4. verify Docker/Compose availability if Compose is selected;
5. inspect the merged Lite configuration before startup;
6. disable or replace unapproved external dependencies;
7. use synthetic credentials and data only;
8. route approved AI/MCP boundaries to local mocks where compatible;
9. perform the smallest feasible build/pull step;
10. capture command, version, exit status and resource observations;
11. verify no unexpected external service is contacted;
12. start only the minimum approved services;
13. collect health and startup evidence;
14. shut down cleanly;
15. verify process/port cleanup.
## Network and Dependency Boundary
This action did not authorize:
- package registry downloads;
- container image downloads;
- model downloads;
- external LLM API access;
- external MCP access;
- real SaaS integrations.
External/download-related source references observed: 3304.
Their presence means later setup must distinguish legitimate software
dependency acquisition from prohibited runtime external-service access.
## Host Constraint
The previous host assessment established:
- WSL environment;
- 2 logical processors;
- approximately 7.68 GiB RAM;
- limited free disk;
- Docker unavailable at that time.
Therefore a full Standard build/runtime is not the initial baseline.
## Rollback Plan
For a later controlled build:
- stop only components started by the test;
- remove only test-specific temporary containers/files;
- preserve evidence before cleanup;
- do not delete the pinned source clone;
- do not delete evidence commits;
- restore configuration changes from version control;
- verify listening ports and processes terminate.
## Completion Interpretation
The reproducible **procedure** is now documented from pinned-source evidence.
Actual build/runtime reproducibility is **not yet proven** because this action
intentionally performed no dependency installation, image pull, build or
startup.
## Requirement Mapping
Original Phase 6 R6.6:
**Reproducible installation/build**
Status:
**PROCEDURE COMPLETE - EXECUTION VALIDATION PENDING**
## Result
Action 6.14 reproducible installation/build plan: **PASS**.
