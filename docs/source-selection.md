# Source Selection & Confidence

Back to [README](../README.md).

The objective is not to find the source with the most impressive logo. It is to choose evidence appropriate to the intelligence requirement.

## Source class

| Class | Definition | Examples | Default treatment |
|---|---|---|---|
| **A** | Standards body, government, CERT/CSIRT, primary authoritative dataset | CISA, NIST, FIRST, OASIS, MITRE knowledge bases | Strong provenance, but still verify scope and date |
| **B** | Original vendor or research-team reporting | Unit 42, Talos, GTI, Microsoft, ESET | Valuable primary research; preserve vendor naming and confidence |
| **C** | Community, aggregator, index, secondary collection | Ransomware.live, OTX pulses, awesome lists | Useful for discovery/corroboration; trace claims upstream |

## Reliability and credibility are different

**Source reliability** asks whether the source has a history of producing dependable information.

**Information credibility** asks whether this specific claim is supported by direct evidence and corroboration.

A usually reliable source can publish an uncertain claim. An unknown source can occasionally provide authentic primary evidence. Do not collapse both questions into one “confidence score.”

## Practical confidence model

Use qualitative confidence only after recording evidence.

| Confidence | Suggested meaning |
|---|---|
| **High** | Multiple independent high-quality sources or strong direct evidence; limited plausible alternatives |
| **Moderate** | Credible evidence exists, but important gaps, dependencies or alternative explanations remain |
| **Low** | Limited evidence, weak provenance, unresolved contradictions or single-source dependency |

Avoid fake precision such as “83% confidence” unless a real statistical model justifies that number.

## Selection matrix

| Intelligence question | Prefer | Use cautiously |
|---|---|---|
| Is a CVE actively exploited? | CISA KEV, original incident reporting | Generic vulnerability blogs |
| What is the exploit probability? | FIRST EPSS | CVSS interpreted as probability |
| What did an actor do? | Original research + ATT&CK mapping | Alias-only actor databases |
| Is an IOC still useful? | Recent first/last-seen enrichment + internal telemetry | Old blocklists with no timestamps |
| Is a domain part of malicious infrastructure? | Passive DNS, CT logs, scanning/enrichment, original reporting | One reputation score |
| Did a ransomware group claim a victim? | Maintained aggregators + source corroboration | Screenshots reposted without provenance |
| How should data be shared? | TLP 2.0 + organizational policy | Informal color labels |
| How should CTI be represented? | STIX 2.1 / MISP models | Ad-hoc JSON without schema |
| Which TTPs matter? | Incident evidence + ATT&CK | Heatmaps copied without source context |
| How mature is detection coverage? | Summiting the Pyramid + validation evidence | Count of ATT&CK tags alone |

## Source evaluation worksheet

For each material claim, capture:

```yaml
claim:
source:
source_class:
original_or_secondary:
published:
observed_period:
last_reviewed:
evidence_type:
corroboration:
contradictions:
intelligence_level:
confidence:
analyst_note:
```

## Expiry is part of CTI

Technical intelligence decays at different rates:

- IP addresses can change ownership or role quickly.
- Domains may be sinkholed, parked or re-registered.
- Certificates expire or are replaced.
- File hashes remain stable but their operational relevance changes.
- TTPs are generally more durable than infrastructure.
- Strategic assessments can age as geopolitical or business conditions change.

A mature catalog therefore asks not only **“is this true?”** but also **“is this still relevant?”**

## Stoplight for analyst use

| Status | Meaning |
|---|---|
| 🟢 **Use** | Current, maintained, provenance understood |
| 🟡 **Verify** | Useful but secondary, aging, limited, or vendor-specific |
| 🔴 **Reference only** | Archived, abandoned, superseded or historical |

This is a workflow aid, not a universal rating of the organization behind the source.
