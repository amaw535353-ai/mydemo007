# Phase 9 Action 9.10 — P9-H11-01 Scoped READ_USERS

## Result

**REVIEW_SECURITY_PROPERTY**

Scoped manager received out-of-scope Bob. Runtime confirms the static over-broad-read hypothesis; product intent must be confirmed before vulnerability classification.

## Runtime

- Assessed HEAD: `d75b7573e7f86b562b19bc951dda01be55a536d0`
- Route: `GET /manage/users`
- HTTP: 200
- In-scope manager marker present: YES
- Out-of-scope Bob marker present: YES
- Synthetic/local-only fixture: yes
- Fixture rolled back: yes

## Security interpretation

The test evaluates whether a scoped group manager can receive user records
outside its managed group.

If the out-of-scope Bob marker is present, this confirms the previously
documented static over-broad-read hypothesis at runtime. Product requirements
must still be confirmed before assigning vulnerability classification or
severity.

## Progress

- Runtime PASS: 6 / 26
- Dispositioned: 14 / 26 = 53.8%
- Phase 9: 9 / 14 = 64.3%
- Action 9.10 remains IN PROGRESS.
