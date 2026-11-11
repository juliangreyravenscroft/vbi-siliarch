# ADR-0001: Establish a Portable Foundation Before Hardware Integration

**Status:** Proposed  
**Date:** 2026-11-11  
**Project:** SILIARCH

## Context

SILIARCH aims to investigate secure computing across different processor architectures, firmware environments, and hardware platforms.

Beginning with a complete FPGA, secure boot, or device-attestation implementation would introduce many dependencies before the core data contracts and verification expectations are understood.

The project requires a development sequence that supports learning, portability, testability, and reproducible evidence.

## Options Considered

### Option A: Begin with an FPGA implementation

Provides early RTL experience but introduces synthesis, simulation, timing, and hardware-specific constraints before the core capability and assurance model exists.

### Option B: Implement the complete proposed architecture

Establishes broad interfaces early but risks premature abstraction, unnecessary dependencies, and unverified assumptions.

### Option C: Develop a small portable software foundation

Allows capability modeling, validation, contract design, and automated testing to be established before hardware integration.

## Proposed Decision

Begin SILIARCH with a minimal, portable Hardware Capability & Assurance Prototype.

The initial implementation will use Python and its standard library where practical.

Hardware-specific adapters, RTL verification components, and cryptographic attestation mechanisms will be introduced as independently testable extensions.

Interfaces will remain small and will receive explicit versioning when stable data contracts are introduced.

## Rationale

This approach provides:

- A low-complexity starting point
- Early verification of core assumptions
- Clear separation between declarations and hardware evidence
- Easier debugging and test reproducibility
- A controlled route toward heterogeneous hardware support

## Consequences

### Positive

The project can establish meaningful tests before hardware dependencies accumulate.

The portable evaluation core can evolve independently of individual boards.

### Negative

Physical hardware verification is deferred.

The initial software model provides limited assurance about real devices.

Future hardware integration may expose assumptions requiring architectural changes.

## Acceptance Criteria

This decision may be accepted when the first foundation milestone and its verification boundaries are approved.

Implementation results will be recorded separately rather than treated as proof that the architectural decision was correct in every context.

## Related Documents

- [System Architecture](../architecture/SYSTEM_OVERVIEW.md)
- [Trust and Evidence Model](../architecture/TRUST_AND_EVIDENCE.md)
- [Engineering Roadmap](../ROADMAP.md)

---

**Decision principle:** Prefer validated simplicity over premature complexity.
