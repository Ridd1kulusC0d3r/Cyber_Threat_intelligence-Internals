# Cyber Threat Intelligence Internals

> An evidence-aware, machine-readable directory for Cyber Threat Intelligence, threat-informed defense, OT/ICS, probabilistic analysis, graph hunting, detection engineering, attribution, ransomware and emerging research.

[![Link Check](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/link-check.yml)
[![Catalog Validate](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/catalog-build.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/Cyber_Threat_intelligence-Internals/actions/workflows/catalog-build.yml)
![CTI](https://img.shields.io/badge/Focus-Cyber%20Threat%20Intelligence-111827)
![Evidence](https://img.shields.io/badge/Evidence-Tracked-2563eb)
![Lifecycle](https://img.shields.io/badge/Lifecycle-Tracked-0f766e)

**[Open the live CTI Source Directory →](https://ridd1kulusc0d3r.github.io/Cyber_Threat_intelligence-Internals/)**

## From link list to CTI Source Directory

A list with hundreds of links is impressive for roughly eleven minutes. Then an analyst needs to know:

- what problem the source solves;
- who owns it;
- whether it is maintained;
- whether it is official, peer-reviewed, a preprint, a community project or a vendor claim;
- which intelligence level it supports;
- whether it belongs in an operational workflow or a research watchlist.

This repository makes those distinctions explicit.

## Classification model

| Dimension | Values |
|---|---|
| **Source class** | **A** authoritative / standards / government · **B** original vendor research · **C** community / aggregator |
| **Intelligence level** | Strategic · Operational · Tactical · Technical |
| **Evidence** | Official · Peer-reviewed · Preprint · Vendor claim · Community · Unverified |
| **Verification** | Verified · Provisional · Watchlist · Rejected |
| **Lifecycle** | Active · Emerging · Research · Reference · Legacy · Archived · Watchlist |
| **Access** | Free · Open source · Freemium · Commercial · Academic |

## Start here

| Analyst problem | Starting points |
|---|---|
| Adversary behavior | [MITRE ATT&CK](https://attack.mitre.org/) · [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) |
| Attack sequences | [Attack Flow](https://ctid.mitre.org/projects/attack-flow/) · [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) |
| Defensive countermeasures | [D3FEND](https://d3fend.mitre.org/) · [CIS Controls](https://www.cisecurity.org/controls/v8) · [NIST CSF](https://www.nist.gov/cyberframework) |
| Detection quality | [Summiting the Pyramid](https://ctid.mitre.org/projects/summiting-the-pyramid) · [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) · [Sigma](https://sigmahq.io/) |
| Endpoint hunting | [YAMAGoya](https://github.com/JPCERTCC/YAMAGoya) · [Velociraptor](https://docs.velociraptor.app/) |
| Provenance / graph hunting | [Graph & Provenance guide](docs/graph-provenance-hunting.md) · [ProHunter](https://github.com/xueboQiu/ProHunter) · [CTI-Thinker](https://doi.org/10.1186/s42400-025-00505-y) |
| OT / ICS intelligence | [OT/ICS guide](docs/ot-ics-intelligence.md) · [CyOTE CATCH](https://cyote.inl.gov/tools/collection-and-analysis-of-telemetry-for-cyote-heuristics-catch/) · [ACE](https://cyote.inl.gov/tools/attack-chain-estimator-ace/) |
| Probabilistic CTI | [Probabilistic CTI guide](docs/probabilistic-cti.md) · Bayesian threat quantification · CyOTE BAM |
| Instrumented purple teaming | [Purple Teaming guide](docs/instrumented-purple-teaming.md) · ATT&CK · D3FEND · Summiting the Pyramid |
| Attribution | [Diamond Model](docs/attribution-analytics.md) · [Unit 42 framework](https://unit42.paloaltonetworks.com/unit-42-attribution-framework/) · [ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) |
| AI security | [MITRE ATLAS](https://atlas.mitre.org/) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [OWASP GenAI](https://genai.owasp.org/) |
| Embedded / IoT | [EMB3D](https://emb3d.mitre.org/) · [ESTM](https://estm.mitre.org/) · [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) |
| CTI exchange | [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) · [TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) · [TLP 2.0](https://www.first.org/tlp/) |
| CTI platforms | [OpenCTI](https://www.opencti.io/) · [MISP](https://www.misp-project.org/) |
| Vulnerability prioritization | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://www.first.org/epss/) · [NVD](https://nvd.nist.gov/) |
| Ransomware | [Ransomware.live](https://www.ransomware.live/) · [RansomLook](https://www.ransomlook.io/) · [CIG Portal](https://www.mbsd.jp/cig-ransomware-portal/) |
| Influence operations | [DISARM](https://www.disarm.foundation/framework) |
| Agentic CTI | [Agentic CTI guide](docs/agentic-cti.md) |
| 2026 research | [Frontier Research radar](docs/frontier-research-2026.md) |
| Brazil / LATAM | [CERT.br](https://cert.br/) · [CTIR Gov](https://www.gov.br/gsi/pt-br/assuntos/ctir) · [CAIS/RNP](https://www.rnp.br/sistema-rnp/cais) |

## Analyst tracks

### CTI foundations
- [Frameworks, standards and models](docs/frameworks-standards.md)
- [Framework landscape: MITRE and alternatives](docs/framework-landscape.md)
- [Platforms, feeds and enrichment](docs/platforms-sources.md)
- [Source selection & confidence](docs/source-selection.md)
- [Evidence & verification policy](docs/evidence-policy.md)

### Threat-informed defense
- [MITRE & CTID ecosystem](docs/mitre-ecosystem.md)
- [Detection engineering & threat hunting](docs/detection-hunting.md)
- [Threat Hunting Frontier](docs/threat-hunting-frontier.md)

### Intelligence analysis
- [Attribution, analytic rigor & confidence](docs/attribution-analytics.md)
- [Probabilistic CTI](docs/probabilistic-cti.md)
- [Graph & Provenance Hunting](docs/graph-provenance-hunting.md)
- [Research, CERTs, vendors and learning](docs/research-learning.md)

### OT / cyber-physical intelligence
- [OT/ICS Threat Intelligence](docs/ot-ics-intelligence.md)
- CyOTE: CATCH · BAM · OPTIC · ACE
- ATT&CK for ICS · EMB3D · ESTM
- OT-ISAC · ETHOS · EE-ISAC

### Detection validation
- [Instrumented Purple Teaming](docs/instrumented-purple-teaming.md)
- [Detection engineering & threat hunting](docs/detection-hunting.md)
- [Threat Hunting Frontier](docs/threat-hunting-frontier.md)

### Specialized intelligence
- [Ransomware intelligence](docs/ransomware-intelligence.md)
- [Agentic CTI & AI-assisted intelligence](docs/agentic-cti.md)
- [CTI Frontier Research — 2026](docs/frontier-research-2026.md)
- [Curated community collections](docs/curated-collections.md)

## Machine-readable directory

The structured source of truth lives in `catalog/`.

```text
catalog/
├── core.yaml
├── frameworks.yaml
├── detection.yaml
├── attribution.yaml
├── ai-research.yaml
├── vendors.yaml
├── datasets.yaml
├── specialized.yaml
├── ot-ics.yaml
├── probabilistic.yaml
└── watchlist.yaml
```

Run:

```bash
pip install -r requirements.txt
python scripts/build_catalog.py
```

The build produces:

- `site/data/resources.json`
- `site/data/resources.csv`
- `site/data/stats.json`

The static interface in `site/` provides client-side search and filters for category, source class, evidence, lifecycle and verification state.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the complete design.

### Live directory

The GitHub Pages interface is published at:

**https://ridd1kulusc0d3r.github.io/Cyber_Threat_intelligence-Internals/**

It includes full-text search, evidence/lifecycle filters and analyst views for OT/ICS, graph/provenance, probabilistic CTI, detection, ransomware, AI and the research watchlist.

## Analyst workflow

```text
Intelligence Requirements / PIRs
            ↓
Collection Strategy
            ↓
Source & Evidence Evaluation
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
Detection / Hunting / Risk Prioritization
            ↓
Assessment + Confidence
            ↓
Dissemination (TLP)
            ↓
Feedback / Reassessment
```

## Intelligence hygiene

Before promoting a claim into an assessment, capture:

- original source and publication date;
- source provenance;
- evidence level;
- verification state;
- lifecycle / last review date;
- analyst confidence;
- corroborating and contradicting evidence;
- observable first-seen / last-seen when applicable;
- behavioral mapping only when justified;
- dissemination marking such as TLP;
- why the information matters to the intelligence requirement.

> **An IOC without context is an observable, not finished intelligence.**

## Corrections that matter

- **OCTAVE / OCTAVE Allegro** is from Carnegie Mellon University's Software Engineering Institute, not MITRE.
- **Responder** is third-party software cataloged in ATT&CK as S0174, not a MITRE-developed tool.
- **STIX and TAXII** are OASIS standards.
- **TLP** is maintained by FIRST.
- **CybOX** is historical in this context; STIX 2.x integrated cyber-observable objects into its own model.
- Research claims without a sufficiently strong primary source belong in `catalog/watchlist.yaml`, not in the operational directory.

## Repository architecture

```text
catalog/*.yaml
      │
      ▼
scripts/build_catalog.py
      │
      ├── validation
      ├── JSON
      ├── CSV
      └── statistics
              │
              ▼
          site/ Pages
      search + filters
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions are expected to provide provenance and evidence metadata, not merely another URL discovered at 02:00 while falling through a browser-tab singularity.

---

Defensive security, threat research, incident response, intelligence analysis, detection engineering and authorized analysis only.
