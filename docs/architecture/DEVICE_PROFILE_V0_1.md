# Device Profile v0.1

Status: Proposed for the first implementation. No parser is published yet.

## Purpose

A device profile describes claimed capabilities. It does not authenticate a device, measure hardware, or establish a security state.

The first prototype will read one JSON object and validate its fields before comparing it with a separate set of requirements.

## Example profile

```json
{
  "schema_version": "0.1",
  "device_id": "lab-board-01",
  "architecture": "riscv64",
  "memory_bytes": 65536,
  "capabilities": ["uart", "spi"]
}
```

The values are fictional test data.

## Field definitions

| Field | Type | Rule |
|---|---|---|
| `schema_version` | string | Must equal `0.1` |
| `device_id` | string | 1 to 64 ASCII letters, digits, periods, underscores, or hyphens; starts with a letter or digit |
| `architecture` | string | One of `arm64`, `riscv64`, `x86_64` |
| `memory_bytes` | integer | From 1 to 9,223,372,036,854,775,807 |
| `capabilities` | array of strings | Unique values drawn from `uart`, `spi`, and `i2c` |

All five keys are required. Unknown keys are rejected in this version. An empty capabilities array is valid.

A boolean is not an integer for this contract, even though Python treats booleans as a subtype of integers.

The JSON reader must reject duplicate keys rather than silently keeping one value. Input-size limits will be established for the command-line interface before accepting untrusted files.

## Example requirement

```json
{
  "architecture": "riscv64",
  "min_memory_bytes": 32768,
  "required_capabilities": ["uart"]
}
```

The requirement is evaluated only after its structure and the device profile have been validated. Requirement validation rules will be finalized with the evaluator module.

## Outcomes

| Outcome | Meaning |
|---|---|
| Invalid input | The profile or requirement violates its format or field rules |
| Match | The declared profile satisfies the validated requirement |
| No match | At least one declared value fails a requirement |

A match never means hardware verification.

## Test cases for the first implementation

1. A complete example profile is accepted.
2. A missing required field is rejected.
3. An extra field is rejected.
4. A boolean memory value is rejected.
5. A zero or negative memory value is rejected.
6. A repeated capability is rejected.
7. A duplicate JSON object key is rejected.
8. An unsupported schema version is rejected.
9. A matching requirement produces Match.
10. A requirement for an absent capability produces No match.

The tests must be repeatable and must not require network access or physical hardware.

## Implementation order

1. Define a pure profile validator.
2. Add tests for valid and invalid profiles.
3. Parse JSON with duplicate-key detection.
4. Define and validate requirement objects.
5. Implement deterministic capability evaluation.
6. Add a minimal command-line entry point.
7. Record what the results prove and what they do not prove.

See [System Overview](SYSTEM_OVERVIEW.md) and [Trust and Evidence](TRUST_AND_EVIDENCE.md).
