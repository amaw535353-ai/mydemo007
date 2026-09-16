# Phase 8 Action 8.23 - Live Standard API Runtime

## Result

**PASS**

- UTC: 2026-09-16T19:00:23Z
- Onyx source SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Image tag: `nightly-latest-20260915`
- Runtime: Onyx Standard API core
- PostgreSQL: enabled
- Redis: enabled
- OpenSearch: enabled
- Model server: disabled for Phase 8
- File store: PostgreSQL
- Authentication: basic
- USER_AUTH_SECRET: set, value not recorded
- Secret fingerprint: `ec98c2d5b3a3`
- Health endpoint: HTTP 200
- OpenAPI endpoint: HTTP 404
- Live OpenAPI paths: 

## Scope note

The model-server subsystem is intentionally disabled because Phase 8 covers web,
API and business-logic security. AI/RAG/model-server runtime behavior is tested
in later dedicated phases.

## Runtime decision

The live API runtime is ready for bounded Phase 8 security testing.
