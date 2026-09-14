# Phase 1 — Engineering Workstation Baseline

## Evidence Metadata

Captured: 2026-09-14T10:22:36+01:00
Repository: /home/ahmed/projects/mydemo007
Phase 0 closure commit: 247cde6921c0fa1c770582b34874d7cb2608711c
Phase 1 branch: security/phase-1-foundations

## Operating Environment

Operating system: Debian GNU/Linux 13 (trixie)
Architecture: x86_64
Kernel: Linux DESKTOP-GQH7TL3 4.4.0-19041-Microsoft #5794-Microsoft Mon Apr 07 17:55:00 PST 2025 x86_64 GNU/Linux
User: ahmed
Shell: /bin/bash

## Hardware Baseline

CPU: Intel(R) Pentium(R) CPU        P6100  @ 2.00GHz
Logical processors available to WSL: 2

### Memory

```text
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       4.3Gi       3.4Gi        17Mi       223Mi       3.4Gi
Swap:           36Gi       250Mi        36Gi
```

### Storage

```text
Filesystem      Size  Used Avail Use% Mounted on
rootfs          103G   91G   12G  89% /
```

## Foundation Toolchain

- Python 3.13.5
- pip 25.1.1 from /usr/lib/python3/dist-packages/pip (python 3.13)
- git version 2.47.3
- gcc (Debian 14.2.0-19) 14.2.0
- GNU Make 4.4.1
- jq-1.7
- GNU Wget 1.25.0 built on linux-gnu.
- OpenSSL 3.5.6 7 Apr 2026 (Library: OpenSSL 3.5.6 7 Apr 2026)
- OpenSSH_10.0p2 Debian-7+deb13u4, OpenSSL 3.5.6 7 Apr 2026

## Executable Locations

```text
python3: /usr/bin/python3
pip3:    /usr/bin/pip3
gcc:     /usr/bin/gcc
make:    /usr/bin/make
jq:      /usr/bin/jq
wget:    /usr/bin/wget
file:    /usr/bin/file
tree:    /usr/bin/tree
git:     /usr/bin/git
curl:    /usr/bin/curl
openssl: /usr/bin/openssl
ssh:     /usr/bin/ssh
```

## Node.js / npm Boundary

Linux Node.js: NOT INSTALLED
npm path: /mnt/c/Users/AHMED/AppData/Roaming/npm/npm

Assessment: Linux Node.js is intentionally not installed yet. If npm resolves under /mnt/c/, it is a Windows executable or shim exposed through the WSL PATH and is not considered part of the Linux-native toolchain.

## Environment Constraints

- Full heavy Onyx deployment is not yet approved for this WSL environment.
- Docker is not installed at this stage.
- Heavy container workloads will be evaluated separately against CPU, memory, storage, and WSL compatibility.
- External services remain outside the active-testing boundary established in Phase 0.
- Paid or billable resources remain prohibited.
- Synthetic-only test data, identities, and credentials remain mandatory.

## Completion Criteria

- Linux-native Python development environment available.
- Compiler and build tools available.
- Core command-line engineering utilities available.
- Git repository integrity preserved.
- Windows npm exposure identified rather than mistaken for Linux Node.js.
- Phase 0 governance boundary preserved.
