# Engineering Roadmap

Status: Planned. No implementation milestone is complete.

This roadmap lists deliverables and exit criteria, not release promises. Progress will be recorded when results can be reproduced.

## F0. Repository foundation

Goal: establish a readable architecture, a controlled development process, and explicit security boundaries.

Deliverables:
- System overview and trust model
- Architecture decision records
- A documented, reviewable Git history
- Local environment checks

Exit criteria: links resolve, documents agree on scope, and a clean checkout contains the expected files.

## F1. Device capability prototype

Goal: assess a declared hardware profile against explicit requirements.

Deliverables:
- Versioned profile format
- Parser and field validation
- Capability evaluation with predictable outcomes
- Command-line interface
- Positive, negative, and boundary tests
- Repeatable execution instructions

Exit criteria: all documented test cases pass, invalid input fails clearly, and results do not claim device authenticity.

## R1. Secure register controller

Goal: build and verify a small RTL module.

Deliverables:
- Register and access-control specification
- Clock and reset behavior
- SystemVerilog module and testbench
- Waveform inspection notes
- Assertions for selected properties

Exit criteria: a repeatable simulation demonstrates specified behavior, with assumptions and coverage limits recorded. Hardware implementation is a separate milestone.

## H1. Firmware assurance research

Goal: evaluate integrity measurement, device identity, and secure boot design options in controlled environments.

Exit criteria: experiments identify their trust assumptions, methods, evidence, and limitations.

## P1. Platform adapters

Goal: investigate selected ARM and RISC-V targets without coupling the portable core to a particular board.

Exit criteria: each claimed target has an implemented adapter, reproducible compatibility tests, and a documented support boundary.

## First 30 days

| Period | Focus | Expected artifact |
|---|---|---|
| Days 1-7 | Git, Python, bits, binary representation, device fields | First profile and review notes |
| Days 8-14 | Types, validation, capability requirements | Validator and unit tests |
| Days 15-21 | Module boundaries, CLI, errors | Repeatable foundation prototype |
| Days 22-30 | Boolean logic, registers, clock, reset | Initial RTL experiment |

The schedule can change when tests expose gaps in the foundations.

## Immediate backlog

| Priority | Work item | Status |
|---|---|---|
| P0 | Finish architecture documentation | In progress |
| P0 | Define profile schema version 0.1 | Planned |
| P0 | Implement strict profile validation | Planned |
| P0 | Evaluate declared capabilities | Planned |
| P0 | Add deterministic unit tests | Planned |
| P1 | Record test provenance | Planned |
| P1 | Set up basic CI | Planned |
| P1 | Write first RTL testbench | Planned |

Do not mark a work item complete from a commit message alone. Review the artifact and its evidence.

See [System Overview](architecture/SYSTEM_OVERVIEW.md), [Trust and Evidence](architecture/TRUST_AND_EVIDENCE.md), and [ADR-0001](decisions/0001-foundation-first.md).
