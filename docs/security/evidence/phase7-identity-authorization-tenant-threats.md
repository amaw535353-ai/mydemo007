# Phase 7 Action 7.6 - Identity, Authorization and Tenant-Isolation Threats

## Classification

All scenarios are threat hypotheses until executable evidence exists.

---

## T7-06-01 - Tenant-context confusion

### Scenario

A valid identity from Tenant Alpha causes an operation to execute using Tenant
Beta context because tenant resolution and user identity become inconsistent.

### Impact

Potential cross-tenant confidentiality or integrity failure.

### Boundary

TB-B - Identity/Tenant Context -> Protected Data.

### Later verification

Use deterministic Tenant Alpha and Tenant Beta synthetic identities.

---

## T7-06-02 - Horizontal privilege escalation

### Scenario

One ordinary user accesses another ordinary user's protected resource.

Examples:

- conversation;
- document;
- file;
- connector;
- saved configuration.

### Security properties

- object authorization;
- ownership.

### Later verification

Alice -> Alice resource: expected ALLOW.

Alice -> Bob resource: expected DENY.

---

## T7-06-03 - Vertical privilege escalation

### Scenario

An ordinary account reaches administrative or privileged functionality by
direct request, manipulated state or missing permission enforcement.

### Security properties

- least privilege;
- authorization.

### Later verification

Build a route/operation permission matrix and test synthetic low-privilege
identities against privileged operations.

---

## T7-06-04 - Group or ACL propagation failure

### Scenario

A user removed from a group or document ACL continues to receive effective
access through stale derived state.

### Security properties

- revocation;
- lifecycle consistency;
- authorization.

### Boundaries

TB-B and TB-F.

### Later verification

Measure authorization before and after synthetic permission revocation.

---

## T7-06-05 - Tenant-scoping omission in a data-access path

### Scenario

A query or lookup enforces resource identity but fails to bind the operation
to the active tenant.

### Security properties

- tenant isolation;
- confidentiality;
- integrity.

### Later verification

Test identical object classes across Alpha/Beta fixtures and verify tenant
filters at every relevant layer.

---

## T7-06-06 - Privileged configuration overreach

### Scenario

Administrative configuration grants wider model, connector, tool, document or
tenant capabilities than intended.

### Security properties

- least privilege;
- administrative control;
- configuration integrity.

### Later verification

Create explicit privilege expectations for administrative roles and inspect
effective authorization.

---

# Result

Action 7.6:

**THREAT MODEL COMPLETE - TENANT ENFORCEMENT NOT YET VERIFIED**
