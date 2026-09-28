# Cyber Threat Intelligence Internals

> A curated, classified and analyst-oriented field guide to Cyber Threat Intelligence (CTI), threat-informed defense, detection engineering, ransomware intelligence, standards, platforms, feeds and research.

[![Link Check](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml)
![CTI](https://img.shields.io/badge/Focus-Cyber%20Threat%20Intelligence-111827)
![Curated](https://img.shields.io/badge/Resources-Classified-2563eb)
![Lifecycle](https://img.shields.io/badge/Lifecycle-Tracked-0f766e)

## Why this repository exists

A giant list is easy to build and surprisingly hard to use. This repository is organized around a simpler analyst question:

> **What source should I use for this intelligence problem, and how much trust should I place in it?**

Resources are therefore classified by **source class**, **intelligence level**, **access model**, **analyst use case**, and now **lifecycle status**.

## Classification model

| Dimension | Values |
|---|---|
| **Source class** | **A** authoritative/standards/government · **B** original vendor research · **C** community/aggregator |
| **Intelligence level** | Strategic · Operational · Tactical · Technical |
| **Lifecycle** | **Active** · **Reference** · **Legacy** · **Archived** |
| **Access** | Free · Open source · Freemium · Commercial |

### Lifecycle matters

A historically important project is not automatically a good choice for a new deployment. Resources marked **Legacy** or **Archived** remain useful for research, labs, historical context, or methodology, but should not be presented as current production defaults.

## Start here

| Analyst need | Recommended starting points |
|---|---|
| Model adversary behavior | [MITRE ATT&CK](https://attack.mitre.org/) · [D3FEND](https://d3fend.mitre.org/) · [CAPEC](https://capec.mitre.org/) |
| Understand attack sequences | [Attack Flow](https://ctid.mitre.org/projects/attack-flow/) · [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) |
| AI / ML threat modeling | [MITRE ATLAS](https://atlas.mitre.org/) |
| Embedded / IoT threat modeling | [MITRE EMB3D](https://emb3d.mitre.org/) |
| Threat-informed program maturity | [MITRE INFORM](https://ctid.mitre.org/projects/inform-your-defense/) |
| Improve detection quality | [Summiting the Pyramid](https://ctid.mitre.org/projects/summiting-the-pyramid) · [Sigma](https://sigmahq.io/) |
| Structure and exchange CTI | [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) · [TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) · [TLP 2.0](https://www.first.org/tlp/) |
| Build/manage a CTI knowledge base | [OpenCTI](https://www.opencti.io/) · [MISP](https://www.misp-project.org/) |
| Prioritize exploited vulnerabilities | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://www.first.org/epss/) · [NVD](https://nvd.nist.gov/) |
| Validate infrastructure/IOCs | [VirusTotal](https://www.virustotal.com/) · [urlscan.io](https://urlscan.io/) · [GreyNoise](https://viz.greynoise.io/) · [OTX](https://otx.alienvault.com/) |
| Track malware infrastructure | [ThreatFox](https://threatfox.abuse.ch/) · [URLhaus](https://urlhaus.abuse.ch/) · [MalwareBazaar](https://bazaar.abuse.ch/) · [Feodo Tracker](https://feodotracker.abuse.ch/) |
| Track ransomware ecosystem | [Ransomware.live](https://www.ransomware.live/) · [RansomLook](https://www.ransomlook.io/) · [CISA StopRansomware](https://www.cisa.gov/stopransomware) |
| Follow original threat research | [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence) · [Unit 42](https://unit42.paloaltonetworks.com/) · [Cisco Talos](https://blog.talosintelligence.com/) · [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |
| Brazil / LATAM | [CERT.br](https://cert.br/) · [CTIR Gov](https://www.gov.br/ctir/pt-br) · [CAIS/RNP](https://www.rnp.br/sistema-rnp/cais) |

## Analyst tracks

### CTI Core
- [Frameworks, standards and models](docs/frameworks-standards.md)
- [Platforms, feeds and enrichment sources](docs/platforms-sources.md)
- [Research, CERTs, vendor intelligence and learning](docs/research-learning.md)
- [Source selection & confidence](docs/source-selection.md)

### Threat-Informed Defense
- [MITRE & CTID ecosystem](docs/mitre-ecosystem.md)
- [Detection engineering & threat hunting](docs/detection-hunting.md)

### Specialized Intelligence
- [Ransomware intelligence](docs/ransomware-intelligence.md)
- [Curated community collections](docs/curated-collections.md)

### Automation layer
- [Machine-readable catalog](catalog/README.md)
- [Core resources YAML](catalog/core.yaml)

## Analyst workflow

```text
Intelligence Requirements / PIRs
            ↓
Collection Strategy
            ↓
Source Evaluation
            ↓
Normalization (STIX / MISP)
            ↓
Enrichment & Correlation
            ↓
Actor / Campaign / Infrastructure Analysis
            ↓
ATT&CK / ATLAS / D3FEND Mapping
            ↓
Attack Flow / Relationship Analysis
            ↓
Detection / Hunting / Vulnerability Prioritization
            ↓
Assessment + Confidence
            ↓
Dissemination (TLP)
            ↓
Feedback / Reassessment
```

## Minimum intelligence hygiene

Before promoting an item into an intelligence assessment, capture:

- original source and publication date;
- source class and provenance;
- lifecycle / last review date;
- analyst confidence;
- corroborating evidence;
- observable first-seen / last-seen when applicable;
- ATT&CK, ATLAS, D3FEND or other behavioral mapping when justified;
- dissemination marking such as TLP;
- a short note explaining **why the information matters to the intelligence requirement**.

> **An IOC without context is an observable, not finished intelligence.**

## Important taxonomy corrections

Some commonly repeated lists blur together MITRE projects, related standards and third-party tools. This repository keeps those distinctions explicit:

- **OCTAVE / OCTAVE Allegro** comes from Carnegie Mellon University's Software Engineering Institute, not MITRE.
- **Responder** is a third-party tool cataloged in ATT&CK as software **S0174**; it is not a MITRE-developed tool.
- **STIX and TAXII** are OASIS standards.
- **TLP** is maintained by FIRST.
- **MAEC** is a malware-description language maintained as a community effort with MITRE involvement; it is not a formal OASIS standard.

See [MITRE & CTID ecosystem](docs/mitre-ecosystem.md) for the full map.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New resources should include a category, source class, access model, intelligence level, lifecycle status and a one-line analyst use case.

## Maintenance

A GitHub Actions workflow checks links on pull requests and on a schedule. Resources that become stale, unsafe, misleading, abandoned or superseded should be reclassified rather than silently left to fossilize.

---

This repository is intended for defensive security, threat research, incident response, detection engineering and authorized analysis.
