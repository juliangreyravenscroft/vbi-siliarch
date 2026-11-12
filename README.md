# SILIARCH

**Adaptive Trusted Hardware & Computing Platform**

VanceBlackwood Industries | RAVENSCROFT Engineering Research

SILIARCH is a hardware and systems engineering research project. Its goal is to make device capabilities, security assumptions, and verification results easier to describe, test, and review across different computing platforms.

The project is at the foundation stage. The architecture below is a design direction, not a claim that the hardware security features have been implemented.

## The problem

A device profile may say that a board has a particular processor, amount of memory, or security feature. Software can check whether that description matches an application's requirements, but the description alone cannot prove what is present on the board.

SILIARCH will keep three questions separate:

1. What does a device or manifest claim?
2. Does that claim satisfy a defined requirement?
3. What has been verified through tests, measurements, or trusted evidence?

The first milestone addresses the first two questions. The third requires additional mechanisms and careful documentation of their limitations.

## Documentation

| Document | What it covers |
|---|---|
| [System Overview](docs/architecture/SYSTEM_OVERVIEW.md) | Data flow, planned components, and module boundaries |
| [Trust and Evidence](docs/architecture/TRUST_AND_EVIDENCE.md) | Input trust, test evidence, and assurance limitations |
| [Device Profile v0.1](docs/architecture/DEVICE_PROFILE_V0_1.md) | Proposed input format and first validation test cases |
| [Engineering Roadmap](docs/ROADMAP.md) | Milestones, deliverables, and acceptance criteria |
| [ADR-0001](docs/decisions/0001-foundation-first.md) | Why the project starts with a portable software model |

Read the system overview first if you want to understand how the components will fit together.

## First milestone

The first deliverable is a small hardware capability evaluator.

It will:

- Read a versioned device profile
- Validate fields, types, and value ranges
- Compare declared capabilities with explicit requirements
- Return a clear outcome or validation error
- Include repeatable tests for normal and invalid inputs

The prototype will not inspect a physical device or establish the authenticity of a profile. A matching result means only that the supplied data meets the specified conditions.

The follow-up milestone, SILIARCH-001, will introduce a secure register controller as an RTL verification exercise. It will cover binary logic, clock and reset behavior, register access rules, simulation, and assertions.

## Research direction

Future work may include FPGA development, embedded firmware, RISC-V and ARM platform adapters, secure boot, device identity, hardware roots of trust, attestation, formal verification, and accelerator integrity.

These are research areas. Platform support and security properties will be reported only when backed by tests or other appropriate evidence.

## How work is organized

The design separates device declarations, portable evaluation logic, hardware-specific adapters, verification, and evidence records. AI-assisted analysis is a possible later extension, not a trust anchor.

Development starts with Python and small, testable components. Hardware-specific tools will be added when a milestone needs them.

The working setup is Visual Studio Code on Apple Silicon, with terminal commands for filesystem, Git, builds, and tests. Source code and technical documents are edited in the VS Code editor.

Each change should have a clear purpose, a reviewable diff, and an appropriate test or documentation check. A simulation result must not be presented as a physical hardware result.

## Current status

**Foundation documentation published. No working capability evaluator or hardware security implementation is published yet.**

Completed work and test results will be linked here as they become available. Planned milestones are tracked in the [roadmap](docs/ROADMAP.md).

## Scope and licensing

SILIARCH covers trusted hardware and computing. General cyber defense, intelligence, and quantitative finance remain separate projects in the RAVENSCROFT research program.

Security experiments are limited to authorized, controlled environments.

A license has not yet been selected. Public visibility does not automatically grant redistribution rights.

