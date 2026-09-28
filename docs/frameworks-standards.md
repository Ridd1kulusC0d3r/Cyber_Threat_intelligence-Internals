# Frameworks, Standards & Models

Back to [README](../README.md).

**Legend:** Class **A** = authoritative/standards/government, **B** = original vendor research, **C** = community.  
**Levels:** Strategic · Operational · Tactical · Technical.

## Core CTI frameworks

| Resource | Class | Level | Use |
|---|---:|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | A | Operational / Tactical | Model adversary tactics, techniques, software, groups and campaigns |
| [MITRE ATT&CK Groups](https://attack.mitre.org/groups/) | A | Operational | Pivot from named groups to observed behavior |
| [MITRE ATT&CK Campaigns](https://attack.mitre.org/campaigns/) | A | Operational | Track campaign-level behavior |
| [MITRE ATT&CK Software](https://attack.mitre.org/software/) | A | Tactical | Map malware/tools to techniques |
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | A | Tactical | Visualize and compare ATT&CK coverage |
| [ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data) | A | Technical | Consume ATT&CK programmatically as STIX 2.1 |
| [MITRE D3FEND](https://d3fend.mitre.org/) | A | Tactical | Map defensive techniques and countermeasures |
| [MITRE CAPEC](https://capec.mitre.org/) | A | Tactical | Common attack-pattern taxonomy |
| [MITRE CAR](https://car.mitre.org/) | A | Tactical | Analytic patterns for detecting adversary behavior |
| [Lockheed Martin Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) | B | Strategic / Operational | Stage intrusions across a lifecycle |
| [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) | C | Tactical | Measure ATT&CK visibility, data sources and detection coverage |

## CTI standards and information sharing

| Resource | Class | Level | Use |
|---|---:|---|---|
| [OASIS STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) | A | Technical | Represent CTI objects and relationships |
| [OASIS TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) | A | Technical | Exchange CTI over a standardized API |
| [FIRST TLP 2.0](https://www.first.org/tlp/) | A | All | Define dissemination boundaries |
| [NIST SP 800-150](https://csrc.nist.gov/pubs/sp/800/150/final) | A | Strategic | Threat-information sharing guidance |
| [MISP Taxonomies](https://github.com/MISP/misp-taxonomies) | C | Operational / Tactical | Classification and tagging vocabularies |
| [MISP Galaxies](https://github.com/MISP/misp-galaxy) | C | Operational | Structured clusters for actors, malware, tools and sectors |
| [MISP Warning Lists](https://github.com/MISP/misp-warninglists) | C | Technical | Reduce false positives during IOC handling |
| [CVE](https://www.cve.org/) | A | Technical | Canonical vulnerability identifiers |
| [CWE](https://cwe.mitre.org/) | A | Tactical / Technical | Software weakness taxonomy |
| [CPE](https://nvd.nist.gov/products/cpe) | A | Technical | Standardized product naming |
| [FIRST CVSS](https://www.first.org/cvss/) | A | Tactical | Vulnerability severity scoring |
| [FIRST EPSS](https://www.first.org/epss/) | A | Tactical | Estimate probability of exploitation |
| [VERIS](https://verisframework.org/) | C | Strategic / Operational | Structured incident and breach classification |
| [CSAF](https://oasis-open.github.io/csaf-documentation/) | A | Technical | Machine-readable security advisories |
| [CycloneDX VEX](https://cyclonedx.org/capabilities/vex/) | C | Tactical / Technical | Express exploitability status for components |

## Vulnerability intelligence and prioritization

| Resource | Class | Access | Use |
|---|---:|---|---|
| [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | A | Free | Prioritize vulnerabilities with evidence of exploitation |
| [NIST NVD](https://nvd.nist.gov/) | A | Free | CVE enrichment, CPE and CVSS metadata |
| [CISA Vulnrichment](https://github.com/cisagov/vulnrichment) | A | Free | Enriched CVE records and exploitation context |
| [GitHub Advisory Database](https://github.com/advisories) | B | Free | Package and ecosystem vulnerability advisories |
| [OSV](https://osv.dev/) | B | Free | Open-source vulnerability database and API |
| [CERT/CC Vulnerability Notes](https://kb.cert.org/vuls/) | A | Free | Coordinated vulnerability disclosures and technical notes |

## Detection and hunting frameworks

| Resource | Class | Level | Use |
|---|---:|---|---|
| [Sigma](https://sigmahq.io/) | C | Tactical | Portable detection-rule format |
| [SigmaHQ Rules](https://github.com/SigmaHQ/sigma) | C | Tactical | Community detection content mapped to behavior |
| [YARA](https://virustotal.github.io/yara/) | B | Technical | Pattern matching for malware and files |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | B | Tactical | Detection engineering examples and ATT&CK mappings |
| [Splunk Security Content](https://github.com/splunk/security_content) | B | Tactical | Detection and analytic content |
| [Microsoft Sentinel Content Hub](https://learn.microsoft.com/azure/sentinel/sentinel-solutions-deploy) | B | Tactical | Analytics, hunting and connector content |
| [Detection.FYI](https://detection.fyi/) | C | Tactical | Search across public detection-rule repositories |

## CTI methods worth pairing with the frameworks

Rather than treating ATT&CK as the entire discipline, combine it with:

1. **Intelligence requirements / PIRs** for collection focus.
2. **Source evaluation** for reliability and credibility.
3. **Competing hypotheses** for analytical discipline.
4. **Campaign and infrastructure analysis** for operational context.
5. **ATT&CK** for behavioral normalization.
6. **Detection mapping** for defensive action.
7. **TLP** for dissemination.
8. **Confidence statements** for decision support.
