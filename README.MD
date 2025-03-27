# Agent Trust Policy Language (ATPL)

## Executive Summary

As AI continues to reshape industries, so too must the security paradigms governing it. The Agent Trust Policy Language (ATPL) redefines how trust is codified, enforced, and audited in AI-driven systems. Designed as a declarative, schema-bound trust language for agent-based architectures, ATPL transforms Zero Trust from a conceptual model into a functional and enforceable policy layer.

By leveraging ATPL, organizations can implement composable, identity-aware, and behavior-scored trust policies, fully aligned with Zero Trust principles and inspired by the NIST AI RMF. Each agent becomes a policy-bound entity whose actions, access, and privileges are governed not by static assumptions but by contextual evaluation.

## The Urgency of Zero Trust for AI Systems

Zero Trust has become a cornerstone of modern cybersecurity, emphasizing the principle of "trust no one, verify everything." However, the application of these principles to AI presents unique opportunities and challenges:

- **Dynamic Threats**: AI systems face novel attack vectors, such as adversarial inputs and data poisoning.
- **Ethical Accountability**: AI models can inadvertently perpetuate biases or make opaque decisions.
- **Evolving Compliance Needs**: Regulations may require dynamic safeguards not pertinent to all agentic systems.

ATPL attempts to address these risks by creating a dynamic language to support resolving these issues programmatically.

## Core Concepts

This paper introduces:

- **Zero Trust Access Tokens (ZTATs)** – time- and situationally-aware access tokens with limited temporal or operational lifetimes.
- **Composability** – operations can require ZTATs that reflect runtime behavior or system states.
- **Dynamic Delegation** – authority can be revoked or reassigned by agents or human monitors based on risk scores.

> Access may be limited to systems only during “break glass” operations, but Zero Trust should apply at all times.

## Core Objectives

ATPL addresses key gaps in traditional Zero Trust:

- Enables **granular trust enforcement per agent**
- Supports **capability composition** for scoped access
- Provides a **trust scoring engine** (identity, provenance, behavior, runtime)
- Allows for **ZTAT delegation**

### Principles

1. **Continuous validation** of entities and interactions.
2. **Lifecycle tracking** of decisions and behaviors.
3. **Access minimization** based on agent identity.
4. **Observable outcomes** with defined decision boundaries.

## Zero Trust for Agents

AI introduces new risk dimensions:

- **Adversarial Manipulation**: Controlled via input validation, suspicious behavior isolation, or HITL intervention.
- **Data Vulnerabilities**: Enforced through provenance, signatures, and access control.
- **Opaque Decision-Making**: ATPL mandates explainability, logging, and uncertainty reporting.

ATPL enforces real-time policies, allowing for proactive, auditable, and contextual enforcement strategies.

## Applying Zero Trust to AI

ATPL addresses agent-specific challenges with:

- Granular trust enforcement
- Composable capabilities
- Trust scoring engines
- ZTAT delegation

## Analysis of Alternatives (AoA): Why ATPL Stands Apart

| Approach                        | Pros | Cons | ATPL Advantage |
|-------------------------------|------|------|----------------|
| RBAC & Static Policies        | Simplicity | Inflexible for dynamic AI | Conditional, identity-aware |
| Sandboxing & Isolation        | Contains code | Limited visibility | Behavior-aware scoped control |
| AI Runtime Monitoring         | Real-time alerts | Not preemptive | Declarative, auditable actions |
| Custom In-House Engines       | Tailored logic | High complexity | Standards-aligned, extensible |

## Alignment with Existing Frameworks

### NIST AI RMF Mapping

- **Govern**: Versioned, enforceable policies
- **Map**: Metadata, cryptographic classification
- **Measure**: Trust scoring, audit logs
- **Manage**: ZTAT enforcement, policy evolution

## Technical Foundations: ATPL Policy Schema

**Note**: Schema available at:  
[https://sentrius.io/schemas/atpl.schema.json](https://sentrius.io/schemas/atpl.schema.json)

### Key Sections

```yaml
policy_id: "example-policy"
version: "1.0"
description: "Trust policy for data agents"

match:
  agent_tags:
    - "env:prod"
    - "classification:data-transformer"

identity:
  issuer: "ca.example.com"
  subject_prefix: "agent-"
  mfa_required: true
  certificate_authority: "sha256:abc123..."

provenance:
  source: "github.com/org/repo"
  signature_required: true
  approved_committers:
    - "dev@example.com"

runtime:
  enclave_required: true
  attestation_type: "intel-sgx"
  verified_at_boot: true

behavior:
  minimum_positive_runs: 10
  max_incidents: 2
  incident_types: ["denylist"]

capabilities:
  primitives:
    - id: "readLogs"
      description: "Read access to logs"
  composed:
    - id: "observe"
      includes: ["readLogs", "streamMetrics"]

trust_score:
  minimum: 75
  weightings:
    identity: 0.3
    provenance: 0.2
    runtime: 0.3
    behavior: 0.2

actions:
  on_success: "allow"
  on_marginal:
    action: "require_ztat"
    ztat_provider: "ztat-service.internal.svc"
  on_failure: "deny"

ztat:
  provider: "ztat-service.internal.svc"
  ttl: "5m"
  approved_issuers:
    - "sentrius"
    - "trust-oracle"
  key_binding: "RSA2048"
  approval_required: true

