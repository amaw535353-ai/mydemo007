# Phase 7 Action 7.5 - Web, API and Business-Logic Threats

## Evidence classification

The scenarios in this document are:

**THREAT HYPOTHESES**

They are not confirmed vulnerabilities.

Phase 6 established relevant application/API and request paths statically.
Runtime enforcement remains unverified.

---

## T7-05-01 - Missing authentication enforcement

### Scenario

A route intended for authenticated use may fail to enforce authentication
under some request path or configuration.

### Security properties

- authentication;
- confidentiality;
- integrity.

### Boundary

TB-A - User/Browser -> Application.

### Later verification

Compare authenticated and unauthenticated requests against selected protected
routes using synthetic accounts.

---

## T7-05-02 - Broken object-level authorization

### Scenario

An authenticated user changes an object identifier belonging to another user
and the application fails to enforce ownership or access policy.

Possible objects include:

- conversations;
- documents;
- connectors;
- files;
- sessions;
- configuration objects.

### Security properties

- authorization;
- ownership;
- confidentiality;
- integrity.

### Boundary

TB-A / TB-B.

### Later verification

Use synthetic Alice/Bob objects and explicit expected ALLOW/DENY outcomes.

---

## T7-05-03 - Request parameter or state manipulation

### Scenario

A client modifies parameters that the application assumes were produced by a
trusted UI workflow.

Possible targets:

- tenant identifiers;
- owner identifiers;
- permission fields;
- resource identifiers;
- feature state;
- model/tool configuration.

### Security properties

- integrity;
- authorization;
- business-logic integrity.

### Later verification

Capture legitimate synthetic requests and mutate security-relevant fields.

---

## T7-05-04 - Workflow sequencing bypass

### Scenario

A user directly invokes a later API operation without completing an expected
earlier authorization or validation step.

### Security properties

- authorization;
- workflow integrity.

### Later verification

Map multi-step workflows and execute operations out of sequence.

---

## T7-05-05 - Cross-request state confusion

### Scenario

User, conversation, tenant, model, connector or permission context may become
incorrectly associated across request boundaries.

### Security properties

- isolation;
- authorization;
- integrity.

### Later verification

Interleave bounded requests using multiple synthetic users and tenants.

---

## T7-05-06 - Web/API resource exhaustion

### Scenario

A valid client repeatedly invokes expensive API functions or submits oversized
inputs that consume disproportionate application resources.

### Security properties

- availability;
- bounded resource consumption.

### Later verification

Use approved limits:

- maximum 100 requests;
- maximum 10 concurrent requests;
- maximum 60-second test;
- maximum 1 MB test file.

---

# Result

Action 7.5:

**THREAT MODEL COMPLETE - RUNTIME VERIFICATION DEFERRED**
