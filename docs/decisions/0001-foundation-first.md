# ADR-0001: Start with a Portable Capability Model

Status: Accepted  
Date: 2026-11-11

## Context

SILIARCH will eventually investigate firmware integrity, FPGA logic, processor-specific interfaces, and hardware attestation. Starting with all of these at once would make failures difficult to isolate.

We first need a clear way to represent device claims, check their structure, and explain what an assessment does and does not prove.

## Options

1. Start with an FPGA implementation. This would teach RTL early but require simulation and timing decisions before the data model is established.
2. Build the entire architecture. This would create interfaces for components with no tested requirements.
3. Start with a small portable capability model. This lets us test the data contract and evaluation rules before adding hardware integrations.

## Decision

Choose option 3.

The first implementation will use Python and the standard library where practical. It will validate a declared device profile and evaluate explicit capability requirements. It will not claim physical device verification.

Platform adapters, RTL modules, and attestation mechanisms will be added as separate, testable pieces when their interfaces and requirements are understood.

## Consequences

Benefits:
- Small, inspectable changes
- Early tests for invalid and boundary inputs
- Clear separation between declarations and evidence
- Less coupling to one board or toolchain

Costs:
- Hardware experiments begin later
- The initial model cannot authenticate a real device
- Some interfaces may need revision after hardware testing

## Review

Revisit this decision if a hardware experiment reveals that the chosen profile format or interface boundaries cannot represent the required behavior.

Related documents: [System Overview](../architecture/SYSTEM_OVERVIEW.md), [Trust and Evidence](../architecture/TRUST_AND_EVIDENCE.md), [Roadmap](../ROADMAP.md).
