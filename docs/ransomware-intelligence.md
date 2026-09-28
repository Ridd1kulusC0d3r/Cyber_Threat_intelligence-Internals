# Ransomware Intelligence

Back to [README](../README.md).

Ransomware intelligence should separate **victim/leak monitoring**, **incident-derived technical reporting**, **government advisories**, **historical datasets**, and **vendor analysis**. Leak-post counts alone are not a complete measure of incident volume.

## Primary operational sources

| Resource | Class | Status | Best use |
|---|---:|---|---|
| [CISA StopRansomware](https://www.cisa.gov/stopransomware) | A | Active | Government advisories, mitigations, IOCs and TTPs |
| [Ransomware.live](https://www.ransomware.live/) | C | Active | Aggregate public ransomware-group/victim monitoring |
| [RansomLook](https://www.ransomlook.io/) | C | Active | Open ransomware intelligence, search, statistics and API |
| [The DFIR Report](https://thedfirreport.com/reports/) | B/C | Active | Incident-derived intrusion timelines and ATT&CK-mapped behavior |
| [No More Ransom](https://www.nomoreransom.org/) | A | Active | Ransomware awareness and decryption resources |
| [ID Ransomware](https://id-ransomware.malwarehunterteam.com/) | C | Active | Identify likely ransomware families from artifacts |

## Community and historical projects

| Resource | Status | Analyst note |
|---|---|---|
| [RansomWatch — joshhighet](https://github.com/joshhighet/ransomwatch) | **Archived** | Valuable historical dataset/project; do not present as a current maintained default |
| [Ransomware Tool Matrix — BushidoUK](https://github.com/BushidoUK/Ransomware-Tool-Matrix) | Active | Tracks tools observed in ransomware operations by functional stage |
| [RansomLook](https://www.ransomlook.io/) | Active | Useful for group/victim monitoring and longitudinal pivots |
| [Ransomware.live](https://www.ransomware.live/) | Active | Useful for public leak-site aggregation and statistics |

## Vendor and incident-response research

| Source | Class | Focus |
|---|---:|---|
| [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence) | B | Actors, malware, initial access and campaigns |
| [Unit 42](https://unit42.paloaltonetworks.com/) | B | Ransomware, incident response and actor activity |
| [Sophos X-Ops](https://news.sophos.com/en-us/category/threat-research/) | B | Ransomware tradecraft and incident-derived research |
| [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) | B | Identity, access, actor and ecosystem analysis |
| [Cisco Talos](https://blog.talosintelligence.com/) | B | Malware and infrastructure research |
| [SentinelLabs](https://www.sentinelone.com/labs/) | B | Malware, operators and campaign analysis |
| [ESET Research](https://www.welivesecurity.com/en/eset-research/) | B | Malware and regional threat research |
| [Group-IB](https://www.group-ib.com/blog/) | B | Cybercrime ecosystem, affiliates and infrastructure |
| [The DFIR Report](https://thedfirreport.com/) | B/C | End-to-end intrusion evidence from observed cases |

## What to collect for a ransomware profile

```text
Group / cluster aliases
        ↓
First / last observed
        ↓
Victimology
        ↓
Initial access patterns
        ↓
Privilege / lateral movement
        ↓
Defense evasion
        ↓
Exfiltration
        ↓
Impact / encryption
        ↓
Tooling and infrastructure
        ↓
ATT&CK techniques
        ↓
Detection opportunities
        ↓
Confidence + source provenance
```

## Victim-post data caveats

A leak-site post can indicate extortion activity, but it does **not automatically prove**:

- successful encryption;
- confirmed data theft;
- the date of initial compromise;
- the full scope of impact;
- the identity of the affiliate;
- a one-to-one mapping between post count and incident count.

Treat these datasets as **observations requiring corroboration**, not as ground truth.

## Ransomware intelligence questions

| Question | Best source type |
|---|---|
| Is this group currently posting victims? | Ransomware.live / RansomLook |
| What behaviors were observed in actual intrusions? | DFIR reports / vendor IR research |
| What does government reporting say? | CISA / FBI / national CERTs |
| Which vulnerabilities are actively exploited? | CISA KEV + incident reporting |
| Which tools recur across operations? | Ransomware Tool Matrix + original reports |
| Which malware family is associated with an artifact? | Malpedia / VirusTotal / sandbox reporting |
| What detections should be prioritized? | Original incident evidence + ATT&CK + detection repositories |

## Recommended evidence hierarchy

1. Incident evidence or affected-organization disclosure.
2. Government / CERT advisory.
3. Original vendor incident or malware research.
4. Maintained ransomware aggregator.
5. Community list or social-media lead.
6. Unattributed repost.

The farther down the list, the more corroboration is required.
