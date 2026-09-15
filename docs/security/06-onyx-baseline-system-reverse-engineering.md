# Phase 6 - Onyx Baseline and System Reverse Engineering
Phase 6 status: **IN PROGRESS**.
## Objective
Establish a reproducible Onyx source and runtime baseline, reverse engineer
the system architecture and security-relevant flows, identify trust and
privilege boundaries, and preserve evidence before later threat modeling
and security testing.
## Safety boundary
- Authorized local learning environment only.
- Synthetic data only.
- No production/customer data.
- No production credentials.
- No paid APIs or billable services.
- No external AI provider invocation.
- No active vulnerability testing during baseline reverse engineering.
- Active testing must remain bounded and separately authorized.
## Phase 5 parent
- Branch: `security/phase-5-ai-foundations`
- Closure SHA: `c1725814f8825681c9d3f739d62ba55300489d85`
## Action 6.1 - Establish and Pin Onyx Target Baseline
Status: **COMPLETE**.
### Target provenance
- Repository: `https://github.com/onyx-dot-app/onyx.git`
- Target branch: `main`
- Pinned commit: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Commit date: `2026-09-15T02:03:45Z`
- Commit subject: `chore(dev): upgrade onyx-devtools to 0.13.7 (#14725)`
- Local target path: `/home/ahmed/projects/onyx-phase6`
- Acquisition mode: shallow clone, depth 1
### License boundary
- Source under `ee` directories: Onyx Enterprise License.
- Source outside documented enterprise/restricted directories: MIT Expat.
- LICENSE SHA256: `d4847240794058c7ac3cfdf8e5d528fe8b0edf15b32a96612ecb9b3e182092b7`
### Current limitations
- Deployment edition/mode has not yet been established.
- Onyx has not been built or started.
- Runtime architecture has not yet been verified.
- Authentication and authorization flows have not yet been traced.
- RAG, agent, tool, MCP, queue, cache, logging and deletion flows remain unverified.
- Git history outside the pinned shallow revision was not acquired.
### Evidence
`docs/security/evidence/phase6-target-provenance-evidence.md`
