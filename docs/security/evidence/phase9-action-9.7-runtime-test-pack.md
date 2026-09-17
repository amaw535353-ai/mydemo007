# Phase 9 Action 9.7 — Workload Identity Runtime Test Pack

Status: **QUEUED FOR ACTIONS 9.9–9.10**

All tests are limited to the authorized local/synthetic Onyx laboratory.

| ID | Test | Expected result |
| --- | --- | --- |
| SA-01 | Unauthorized actor attempts service-account API-key administration | DENY |
| SA-02 | Low-privilege service-account key calls permitted and non-permitted endpoints | Only group-derived permissions ALLOW |
| SA-03 | Remove a group privilege while keeping the same key | Formerly permitted operation DENY on next request |
| SA-04 | Regenerate key | Old key DENY; new key ALLOW |
| SA-05 | Delete key | Deleted key DENY |
| SA-06 | Deactivate associated service-account user | Key DENY |
| SA-07 | Replay a tenant-A key in tenant-B context | DENY |
| SA-08 | Attempt interactive login as service account | Outcome must match documented product policy; evaluate H9-17 |
| SA-09 | Local/mock OAuth link attempt for service account if applicable | No unintended identity or privilege amplification |
| SA-10 | Review audit attribution for key lifecycle and workload requests | Actor/key identity remains attributable where designed |

## H9-17 decision gate

Do **not** classify a vulnerability merely because `SERVICE_ACCOUNT` is web-login eligible in source.

Classification requires all of the following:

1. a controlled reproducible interactive service-account session;
2. a documented or source-backed intended boundary that the behavior violates, or demonstrable privilege amplification compared with the intended workload credential path;
3. evidence of the resulting authorization impact;
4. a root cause and regression test.
