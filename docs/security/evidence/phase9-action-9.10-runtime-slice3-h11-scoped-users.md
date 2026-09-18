# Phase 9 Action 9.10 — P9-H11-01 Scoped READ_USERS

## Result

**CONFIRMED_AUTHORIZATION_DEFECT**

A scoped group manager reached `GET /manage/users` with HTTP 200 and received
the synthetic Bob record even though Bob belonged only to an unmanaged group.

## Runtime evidence

- HTTP: 200
- In-scope manager marker present: YES
- Out-of-scope Bob marker present: YES
- Synthetic/local-only fixture: yes
- Fixture fully rolled back: yes

## Source-policy confirmation

`require_permission(..., allow_scope=True)` explicitly defines scoped authority
as Gate 1 only.

The authorization contract states that handlers using scoped authority must
perform Gate 2 resource filtering.

`GET /manage/users` uses:

`Permission.READ_USERS, allow_scope=True`

but then obtains users through `get_all_users(...)` without applying a managed
group filter before serialization.

## Conclusion

The previous H9-11 static hypothesis is confirmed at runtime.

A scoped group manager can receive an out-of-scope user row.

This is a confirmed authorization-scope defect.

Severity is intentionally not assigned here; impact and product-risk
classification remain separate steps.

## Progress

- Runtime PASS cases: 6 / 26
- Confirmed security defects: 1
- Dispositioned cases: 14 / 26 = 53.8%
- Phase 9 completed actions: 9 / 14 = 64.3%
- Action 9.10 remains IN PROGRESS.
