# Detection Engineering & Threat Hunting

Back to [README](../README.md).

This catalog separates **detection content**, **telemetry**, **validation/emulation**, **hunting platforms**, and **community collections**. A rule repository and a hunting platform solve different problems, despite the recurring industry tradition of calling both a “tool”.

## Core detection frameworks and content

| Resource | Class | Status | Use |
|---|---:|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | A | Active | Behavioral model for detection requirements |
| [Summiting the Pyramid](https://ctid.mitre.org/projects/summiting-the-pyramid) | A | Active | Measure detection implementation coverage and quality |
| [Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/) | A | Active | Design detections for behaviors that overlap with legitimate activity |
| [MITRE CAR](https://car.mitre.org/) | A | Reference | Detection analytic patterns |
| [Sigma](https://sigmahq.io/) | C | Active | Portable detection-rule format |
| [SigmaHQ](https://github.com/SigmaHQ/sigma) | C | Active | Community Sigma rules and tooling |
| [Detection.FYI](https://detection.fyi/) | C | Active | Search public detection repositories |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | B | Active | Elastic detection content and ATT&CK mappings |
| [Splunk Security Content](https://github.com/splunk/security_content) | B | Active | Splunk detections, stories and analytic content |
| [Microsoft Sentinel Content Hub](https://learn.microsoft.com/azure/sentinel/sentinel-solutions-deploy) | B | Active | Microsoft Sentinel analytics and hunting content |
| [Google Cloud Security detections](https://cloud.google.com/security) | B | Active | Cloud/SIEM security content and threat context |

## Endpoint and host telemetry

| Resource | Class | Status | Use |
|---|---:|---|---|
| [Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon) | B | Active | High-value Windows endpoint telemetry |
| [SwiftOnSecurity Sysmon Config](https://github.com/SwiftOnSecurity/sysmon-config) | C | Reference | Widely used Sysmon configuration reference |
| [osquery](https://www.osquery.io/) | C | Active | Query endpoint state using SQL-like syntax |
| [Velociraptor](https://docs.velociraptor.app/) | C | Active | Endpoint visibility, collection and DFIR |
| [Fleet](https://fleetdm.com/) | B | Active | osquery fleet management and endpoint visibility |

## Network telemetry

| Resource | Class | Status | Use |
|---|---:|---|---|
| [Zeek](https://zeek.org/) | C | Active | Rich network metadata and protocol visibility |
| [Suricata](https://suricata.io/) | C | Active | Network IDS/IPS and protocol logging |
| [Security Onion](https://securityonionsolutions.com/) | B | Active | Integrated network security monitoring and detection stack |
| [Arkime](https://arkime.com/) | C | Active | Full-packet capture indexing and investigation |

## Malware and file detection

| Resource | Class | Status | Use |
|---|---:|---|---|
| [YARA](https://virustotal.github.io/yara/) | B | Active | Pattern-based file and malware classification |
| [YARA-X](https://github.com/VirusTotal/yara-x) | B | Active | Modern YARA implementation and tooling |
| [Malpedia](https://malpedia.caad.fkie.fraunhofer.de/) | A | Active | Malware-family reference and YARA context |
| [VirusTotal](https://www.virustotal.com/) | B | Active | File/hash/URL enrichment and relationship pivots |

## Validation and adversary emulation

Use these for controlled defensive validation, not as substitutes for intelligence requirements.

| Resource | Class | Status | Use |
|---|---:|---|---|
| [MITRE Caldera](https://caldera.mitre.org/) | A | Active | ATT&CK-informed adversary emulation in authorized environments |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | B | Active | Small tests for validating telemetry and detections |
| [Stratus Red Team](https://github.com/DataDog/stratus-red-team) | B | Active | Cloud-focused defensive validation |
| [PurpleSharp](https://github.com/mvelazc0/PurpleSharp) | C | Reference | Windows purple-team simulation |

## Hunting and lab environments

| Resource | Status | Maintenance note | Best use |
|---|---|---|---|
| [HELK](https://github.com/Cyb3rWard0g/HELK) | **Legacy** | Last upstream commit observed in 2021 | Historical hunting architecture, learning and design reference |
| [DetectionLab](https://github.com/clong/DetectionLab) | **Legacy** | Last upstream commit observed in 2023 | Reproducible detection-lab concepts and historical training |
| [Security Onion](https://securityonionsolutions.com/) | Active | Maintained platform | Current NSM / detection lab deployments |
| [Velociraptor](https://docs.velociraptor.app/) | Active | Maintained | Endpoint hunting and DFIR labs |

**Do not confuse “not archived on GitHub” with “actively maintained.”** Repository metadata and recent commits should both be checked before recommending production adoption.

## Detection engineering collections

| Collection | Status | Notes |
|---|---|---|
| [Awesome Threat Detection — 0x4D31](https://github.com/0x4D31/awesome-threat-detection) | Active | Broad threat detection, hunting, datasets and research collection |
| [Awesome Detection Engineering — infosecB](https://github.com/infosecB/awesome-detection-engineering) | Active | Detection-engineering tools, content and practice |
| [Detection.FYI](https://detection.fyi/) | Active | Searchable detection corpus |
| [SigmaHQ](https://github.com/SigmaHQ) | Active | Sigma ecosystem |

## Detection workflow

```text
Threat / campaign intelligence
          ↓
ATT&CK behavior
          ↓
Required telemetry
          ↓
Detection hypothesis
          ↓
Rule / analytic
          ↓
Controlled validation
          ↓
False-positive analysis
          ↓
Implementation coverage
          ↓
Detection quality
          ↓
Continuous tuning
```

## Questions a mature detection program asks

1. Is the detection based on **behavior**, a brittle IOC, or both?
2. Which telemetry fields are mandatory?
3. What benign activity can produce the same signal?
4. Which implementations of the ATT&CK technique are actually observable?
5. What does the detection miss?
6. How easily can an adversary vary the behavior?
7. Is the rule portable across data sources and SIEMs?
8. Has it been validated in an authorized environment?
9. Does the alert provide enough context for triage?
10. Is its ATT&CK mapping evidence-based rather than decorative?

## CTI-to-detection handoff

A CTI report should not end at “T1059 observed.” A useful handoff includes:

- behavior and procedure;
- affected platforms;
- likely data sources;
- known variants;
- relevant infrastructure or malware context;
- analytic hypothesis;
- confidence and evidence;
- expiry criteria for technical indicators;
- links to source reporting.

That is the difference between tagging ATT&CK and actually using threat intelligence.
