# Cyber Threat Intelligence Internals

> A curated and classified field guide to Cyber Threat Intelligence (CTI): frameworks, standards, platforms, feeds, research, enrichment, hunting, vulnerability intelligence, government advisories, and analyst learning resources.

[![Link Check](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml)
![CTI](https://img.shields.io/badge/Focus-Cyber%20Threat%20Intelligence-111827)
![Curated](https://img.shields.io/badge/Resources-Classified-2563eb)

## Why this repository exists

A threat-intelligence resource list is only useful if an analyst can answer three questions quickly:

1. **What problem does this source solve?**
2. **How authoritative is it?**
3. **At what intelligence level should I use it?**

This repository therefore classifies resources by **source class**, **access model**, **intelligence level**, and **use case** instead of dumping hundreds of links into one undifferentiated list.

## Source classification

| Class | Meaning | Typical examples |
|---|---|---|
| **A** | Standards bodies, government, CERT/CSIRT, primary authoritative datasets | MITRE, NIST, FIRST, CISA, OASIS |
| **B** | Original vendor research or first-party intelligence | Mandiant, Unit 42, Talos, ESET Research |
| **C** | Community projects, aggregators, analyst-maintained collections | APTnotes, Detection.FYI, community feeds |

### Intelligence levels

- **Strategic**: trends, business impact, geopolitical or sector context.
- **Operational**: campaigns, threat actors, targeting, infrastructure and intrusion sets.
- **Tactical**: TTPs, procedures, detection opportunities and adversary behavior.
- **Technical**: IOCs, hashes, domains, URLs, IPs, certificates, malware metadata.

## Start here

| Need | Recommended starting points |
|---|---|
| Model adversary behavior | [MITRE ATT&CK](https://attack.mitre.org/) · [CAPEC](https://capec.mitre.org/) · [D3FEND](https://d3fend.mitre.org/) |
| Structure and exchange CTI | [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) · [TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) · [TLP 2.0](https://www.first.org/tlp/) |
| Build/manage a CTI knowledge base | [OpenCTI](https://www.opencti.io/) · [MISP](https://www.misp-project.org/) |
| Prioritize exploited vulnerabilities | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://www.first.org/epss/) · [NVD](https://nvd.nist.gov/) |
| Validate infrastructure/IOCs | [VirusTotal](https://www.virustotal.com/) · [urlscan.io](https://urlscan.io/) · [GreyNoise](https://viz.greynoise.io/) · [OTX](https://otx.alienvault.com/) |
| Track malware and botnet infrastructure | [ThreatFox](https://threatfox.abuse.ch/) · [URLhaus](https://urlhaus.abuse.ch/) · [MalwareBazaar](https://bazaar.abuse.ch/) · [Feodo Tracker](https://feodotracker.abuse.ch/) |
| Follow original threat research | [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence) · [Unit 42](https://unit42.paloaltonetworks.com/) · [Cisco Talos](https://blog.talosintelligence.com/) · [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/) |
| Brazil / LATAM | [CERT.br](https://cert.br/) · [CTIR Gov](https://www.gov.br/ctir/pt-br) · [CAIS/RNP](https://www.rnp.br/sistema-rnp/cais) |

## Full classified catalog

The main catalog is split by analyst workflow:

- [Frameworks, standards and models](docs/frameworks-standards.md)
- [Platforms, feeds and enrichment sources](docs/platforms-sources.md)
- [Research, CERTs, vendor intelligence and learning](docs/research-learning.md)

## Analyst workflow

```text
Requirements / PIRs
      ↓
Collection
      ↓
Source validation
      ↓
Normalization (STIX / MISP)
      ↓
Enrichment & correlation
      ↓
Actor / campaign / TTP analysis
      ↓
ATT&CK mapping
      ↓
Detection / hunting / prioritization
      ↓
Assessment + confidence
      ↓
Dissemination (TLP)
      ↓
Feedback
```

### Minimal source-validation rule

Before promoting an item into an intelligence assessment, capture:

- original source and publication date;
- whether the source is **primary**, **vendor-original**, or **secondary**;
- confidence level;
- corroborating evidence;
- observable expiry / last-seen data when applicable;
- ATT&CK mapping when behavior is known;
- TLP marking for dissemination;
- analyst note explaining **why it matters**.

**An IOC without context is an observable, not finished intelligence.**

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New resources should include a category, source class, access model, intelligence level, and a one-line analyst use case.

## Maintenance

A GitHub Actions workflow checks links on a schedule and on pull requests. Resources that become stale, unsafe, misleading, or abandoned should be removed or marked accordingly.

---

This repository is intended for defensive security, threat research, incident response, detection engineering, and authorized analysis.
