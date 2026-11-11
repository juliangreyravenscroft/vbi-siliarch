# Trust and Evidence

Status: Design specification. No hardware trust mechanism is implemented yet.

## Purpose

SILIARCH separates three things: a device claim, a software assessment of that claim, and evidence from a test or measurement. They answer different questions and must not be confused.

A profile can be well formed and still be false. A matching capability requirement does not establish that the physical device supports the feature.

## Boundaries

| Boundary | Input | What SILIARCH can conclude |
|---|---|---|
| Profile ingestion | Externally supplied device data | Whether the data meets the defined schema |
| Capability evaluation | Valid profile and explicit requirements | Whether declared values meet the requirements |
| Verification | Test output and execution context | Whether specific checks passed under stated conditions |
| Attestation, future | Signed measurements and verification policy | Whether evidence satisfies a policy with trusted anchors |

Attestation requires more than a signature. The signing identity, trust anchor, freshness, scope, and measurement semantics all matter.

## Initial threat model

| Failure or misuse | Required response |
|---|---|
| Malformed profile | Reject with a specific validation error |
| Missing or unexpected fields | Apply the published schema policy |
| Contradictory claims | Report the conflict rather than guessing |
| Falsified capabilities | Treat the profile as untrusted |
| Missing test evidence | Report the property as unverified |
| Replayed measurements, future | Check freshness and policy requirements |
| Compromised firmware, future | Investigate authenticated measurement and recovery controls |

This table is not a complete threat assessment. Each implementation will document its own assumptions and abuse cases.

## Evidence records

When executable tests are introduced, an evidence record should include:

- Record format version and test identifier
- Source revision and tool version
- Input identity or digest when applicable
- Test conditions and expected result
- Observed result and outcome
- Known limitations and failures

Sensitive identifiers, credentials, and internal secrets must not be published in evidence files.

## Levels of confidence

- Declared: a source asserted a property.
- Validated: the declaration passed structural checks.
- Evaluated: the declaration met a defined requirement.
- Simulated: a particular model passed specified tests.
- Measured: a property was observed on identified hardware.
- Attested: evidence met a defined cryptographic verification policy.

These are descriptions of different kinds of evidence, not a single universal ranking. A simulation result does not substitute for a hardware measurement, and a signature alone does not prove that a platform is secure.

## Review questions

Every verification result should state what was tested, the environment, the expected outcome, the observed outcome, and what the result does not establish.

See [System Overview](SYSTEM_OVERVIEW.md) and [Engineering Roadmap](../ROADMAP.md).

## Reference

[NIST SP 800-193: Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final) is a research reference for later firmware assurance work. No compliance is claimed.
