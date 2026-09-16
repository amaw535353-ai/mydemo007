# Phase 8 Action 8.4 - Executable Runtime Readiness Gate

## Timestamp

`2026-09-16T11:10:26Z`

## Baseline

- Onyx path: `/home/ahmed/projects/onyx-phase6`
- Onyx SHA: `160f9b143605ca45a85bd387b5bd173840bab15d`
- Onyx source clean: YES

## Tool availability

- python3: AVAILABLE - Python 3.13.5 - path: /usr/bin/python3
- curl: AVAILABLE - curl 8.14.1 (x86_64-pc-linux-gnu) libcurl/8.14.1 OpenSSL/3.5.6 zlib/1.3.1 brotli/1.1.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.2 libssh2/1.11.1 nghttp2/1.64.0 nghttp3/1.8.0 librtmp/2.3 OpenLDAP/2.6.10 - path: /usr/bin/curl
- git: AVAILABLE - git version 2.47.3 - path: /usr/bin/git
- docker: NOT AVAILABLE
- node: NOT AVAILABLE
- npm: PATH ENTRY PRESENT BUT UNUSABLE - exit 127 - /mnt/c/Users/AHMED/AppData/Roaming/npm/npm: 15: exec: node: not found - path: /mnt/c/Users/AHMED/AppData/Roaming/npm/npm
- pnpm: NOT AVAILABLE
- uv: NOT AVAILABLE
- poetry: NOT AVAILABLE

## Docker Compose

- docker compose: NOT AVAILABLE

## Current listening TCP sockets

```text
State Recv-Q Send-Q Local Address:Port Peer Address:Port
```

## Important environment observation

The Debian environment contains a Windows npm PATH entry:

`/mnt/c/Users/AHMED/AppData/Roaming/npm/npm`

while the Debian environment currently has no usable node executable.

Therefore npm presence alone must not be interpreted as a usable
Node.js/npm toolchain.

## Interpretation

Tool availability does not prove that Onyx is running.

A listening socket does not prove that the listener is Onyx.

No active request against Onyx was made during this readiness gate.

No dependency installation or service startup was performed.

Docker absence means the previously identified Compose runtime path
remains unavailable on this Debian host.

## Decision rule

Live Phase 8 HTTP testing may begin only after:

1. an approved local Onyx runtime is established;
2. the target endpoint is positively identified as Onyx;
3. external egress remains controlled;
4. synthetic identities/data are loaded;
5. test bounds are enforced.

# Result

**RUNTIME READINESS ASSESSED - LIVE ONYX TESTING REMAINS BLOCKED ON THIS HOST**
