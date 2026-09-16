# Phase 8 Runtime External-Network Hardening

## Result

**PASS**

- UTC: 2026-09-16T19:53:30Z
- Backend: `onyxdotapp/onyx-backend:nightly-latest-20260915`
- API health: HTTP 200
- `DISABLE_MODEL_SERVER=true`
- `HF_HUB_OFFLINE=1`
- `HF_HUB_DISABLE_TELEMETRY=1`
- `TRANSFORMERS_OFFLINE=1`
- USER_AUTH_SECRET preserved at 64 characters
- USER_AUTH_SECRET value excluded from evidence
- Runtime override stored in local Git-excluded `.runtime/`
- Fresh-container tokenizer previously succeeded using `--network none`
- Running API tokenizer succeeded in offline mode
- New startup logs contained no detected Hugging Face Hub access warning

## Safety decision

Phase 8 execution was paused after startup logs indicated an unexpected
Hugging Face Hub access attempt.

The required tokenizer was proven to already exist locally using an isolated
container with Docker networking disabled.

The live API was then recreated with explicit offline-mode environment
controls before security testing resumed.
