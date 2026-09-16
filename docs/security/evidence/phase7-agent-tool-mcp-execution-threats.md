# Phase 7 Action 7.9 - Agent, Tool, MCP and Code-Execution Threats

## Classification

Phase 6 established static capability paths.

No MCP, tool or code-execution security property has yet been proven at
runtime.

---

## T7-09-01 - Model-to-tool authority escalation

### Scenario

A model-generated decision results in invocation of a capability beyond the
requesting user's effective authority.

### Security properties

- authorization;
- least privilege;
- capability isolation.

### Boundary

TB-E - Model -> Tool/MCP/Code Execution.

### Later verification

Use harmless local mock tools with explicit user/capability matrices.

---

## T7-09-02 - Tool argument injection

### Scenario

Untrusted user, document or model-controlled content reaches tool parameters
and changes the intended operation.

### Security properties

- input validation;
- integrity;
- safe execution.

### Later verification

Use local mock tools that record arguments without performing external effects.

---

## T7-09-03 - Malicious MCP metadata or tool description

### Scenario

A malicious or compromised MCP endpoint supplies adversarial tool metadata,
instructions or results intended to influence model behavior.

### Security properties

- provenance;
- trust isolation;
- instruction integrity.

### Later verification

Use the Phase 6 local synthetic MCP contract.

---

## T7-09-04 - Credential disclosure to tool or MCP server

### Scenario

A capability receives credentials, document data or other context beyond what
is required for its authorized purpose.

### Security properties

- least disclosure;
- credential scoping;
- confidentiality.

### Later verification

Use synthetic credential canaries and local loopback mocks.

---

## T7-09-05 - Unsafe code execution or sandbox boundary failure

### Scenario

Model/user-controlled code obtains filesystem, process, network or resource
access exceeding the intended execution boundary.

### Security properties

- sandbox isolation;
- integrity;
- confidentiality;
- availability.

### Later verification

Only in a separately approved bounded local sandbox.

No host-damaging payload is required.

---

## T7-09-06 - Recursive or chained capability exhaustion

### Scenario

Tool calls trigger further model/tool operations and consume uncontrolled
requests, execution time, memory or other resources.

### Security properties

- availability;
- economic security;
- bounded execution.

### Later verification

Use deterministic local mocks with:

- call-depth ceiling;
- request ceiling;
- time ceiling;
- concurrency ceiling.

---

# Result

Action 7.9:

**CAPABILITY THREAT MODEL COMPLETE - EXECUTION CONTROLS REMAIN UNVERIFIED**
