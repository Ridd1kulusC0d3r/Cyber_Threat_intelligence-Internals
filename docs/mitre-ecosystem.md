# MITRE & CTID Ecosystem

Back to [README](../README.md).

This page separates **MITRE-maintained knowledge bases**, **MITRE Center for Threat-Informed Defense (CTID) projects**, **related standards**, and **third-party tools that merely appear in ATT&CK**. That distinction matters because provenance is part of intelligence quality.

## Core MITRE knowledge bases and frameworks

| Resource | Status | Domain | Analyst use |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | Active | Enterprise / Mobile / ICS | Normalize observed adversary behavior into tactics and techniques |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Active | Defensive engineering | Map technical countermeasures and defensive concepts |
| [MITRE ATLAS](https://atlas.mitre.org/) | Active | AI / ML / agentic systems | Model adversarial behavior against AI-enabled systems |
| [MITRE EMB3D](https://emb3d.mitre.org/) | Active | Embedded / IoT / critical systems | Connect device properties to threats and mitigations |
| [MITRE Engage](https://engage.mitre.org/) | Reference | Adversary engagement | Plan deception, denial and adversary-engagement activities within governance guardrails |
| [MITRE CAR](https://car.mitre.org/) | Reference | Detection analytics | Study analytics mapped to ATT&CK behaviors |
| [CAPEC](https://capec.mitre.org/) | Active | Attack patterns | Threat modeling and secure-design attack-pattern catalog |
| [CWE](https://cwe.mitre.org/) | Active | Software weaknesses | Normalize weakness classes and root causes |
| [CVE](https://www.cve.org/) | Active | Vulnerability identifiers | Canonical vulnerability identifiers |
| [Caldera](https://caldera.mitre.org/) | Active | Adversary emulation | Validate defensive controls against ATT&CK-informed behaviors |
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | Active | Visualization | Compare technique coverage, campaigns and detection layers |

### D3FEND is not just a defensive ATT&CK matrix

D3FEND is better treated as a **knowledge graph of cybersecurity countermeasures**. Its value is in the semantic relationships between defensive techniques, digital artifacts and offensive behavior, not merely in producing another colored matrix.

Useful entry points:

- [D3FEND Matrix](https://d3fend.mitre.org/)
- [ATT&CK mitigation to D3FEND mappings](https://d3fend.mitre.org/mappings/attack-mitigations/)
- [D3FEND resources and ontology](https://d3fend.mitre.org/resources/)

## MITRE ATLAS

ATLAS is a living knowledge base for adversarial behavior involving AI systems, including predictive, generative and agentic AI. It covers both attacks against AI components and abuse of AI capabilities.

Use ATLAS when the intelligence requirement involves:

- model access and model manipulation;
- prompt or context abuse;
- training-data or inference-path risks;
- autonomous or agentic behavior;
- AI-specific mitigations and case studies.

Do not force ordinary enterprise intrusion activity into ATLAS when ATT&CK already describes the behavior cleanly.

## MITRE EMB3D

EMB3D is a threat model for embedded devices and maps:

```text
Device properties
      ↓
Potential threats
      ↓
Weaknesses / exposure
      ↓
Technical mitigations
```

Relevant environments include IoT, automotive, healthcare, manufacturing and critical infrastructure.

- [EMB3D home](https://emb3d.mitre.org/)
- [Background and model](https://emb3d.mitre.org/background/)

## Center for Threat-Informed Defense: current high-value projects

CTID extends ATT&CK into practical threat-informed-defense workflows. These projects are especially valuable because they turn behavioral intelligence into measurable defensive decisions.

| Project | Release / current work | Why it matters |
|---|---|---|
| [Attack Flow](https://ctid.mitre.org/projects/attack-flow/) | v4 / 2026 | Represent sequences and relationships between adversary actions rather than isolated ATT&CK techniques |
| [Summiting the Pyramid](https://ctid.mitre.org/projects/summiting-the-pyramid) | 2026 | Measure implementation coverage and detection quality beyond ATT&CK heatmaps |
| [INFORM Your Defense](https://ctid.mitre.org/projects/inform-your-defense/) | 2026 | Assess threat-informed-defense maturity across CTI, defensive measures, and test/evaluation |
| [Ambiguous Techniques](https://ctid.mitre.org/projects/ambiguous-techniques/) | 2026 | Improve detection of behaviors that look similar to legitimate activity |
| [Threat-Informed Defense for Cloud Security](https://ctid.mitre.org/projects/tid-for-cloud/) | 2026 | Connect cloud controls to ATT&CK-observed adversary behavior |
| [Fight Financial Fraud](https://ctid.mitre.org/projects/fight-financial-fraud/) | 2026 | Behavior-based model connecting fraud and cyber defense |
| [Technique Inference Engine](https://github.com/center-for-threat-informed-defense/technique-inference-engine) | Active | Infer likely related ATT&CK techniques from known techniques |
| [CTID projects index](https://ctid.mitre.org/projects) | Active | Follow current and historical threat-informed-defense research |

### Attack Flow

Attack Flow addresses a recurring ATT&CK limitation: a technique list does not show **sequence, dependency, branch, condition or relationship**.

Use it to represent:

- multi-stage incidents;
- campaign behavior;
- alternative adversary paths;
- dependencies between actions;
- ATT&CK, ATLAS and D3FEND context in a connected model.

The 2026 Attack Flow release also supports richer context such as TLP markings, mitigations and detection information.

### Summiting the Pyramid

A technique tagged as “covered” does not prove the detection is robust. Summiting the Pyramid asks harder questions:

- Which implementations of the technique can the analytic detect?
- What telemetry is required?
- How precise is the signal?
- How easy is the detection to evade?

This belongs in detection engineering, not merely in CTI documentation.

### INFORM

INFORM operates at program level. It helps assess how mature an organization is at turning adversary knowledge into:

- intelligence;
- defensive measures;
- testing and evaluation;
- investment priorities.

It is useful for CTI program maturity and threat-informed-defense roadmaps.

## Related standards and methods that are not MITRE projects

| Resource | Owner / steward | Correct relationship |
|---|---|---|
| [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) | OASIS | Standard for representing CTI |
| [TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) | OASIS | Protocol/API model for exchanging CTI |
| [TLP 2.0](https://www.first.org/tlp/) | FIRST | Dissemination marking |
| [OCTAVE Allegro](https://sei.cmu.edu/library/introducing-octave-allegro-improving-the-information-security-risk-assessment-process/) | Carnegie Mellon SEI | Information-security risk assessment methodology; **not MITRE** |
| [MAEC](https://maecproject.github.io/) | Community effort maintained with MITRE involvement | Structured language for malware characterization; not a formal OASIS standard |
| [CVSS](https://www.first.org/cvss/) | FIRST | Vulnerability severity scoring |
| [EPSS](https://www.first.org/epss/) | FIRST | Exploitation-probability model |

## Third-party software represented in ATT&CK

ATT&CK includes software used by adversaries. Inclusion does **not** mean MITRE created or endorses the software.

Example:

- [Responder — ATT&CK S0174](https://attack.mitre.org/software/S0174/) is cataloged as a tool observed in adversary activity. It is **not a MITRE tool**.

That distinction should be preserved in documentation, presentations and threat reports.

## Recommended analyst chain

```text
Observed behavior
      ↓
ATT&CK
      ↓
Attack Flow
      ↓
D3FEND / mitigations
      ↓
Detection analytics
      ↓
Summiting the Pyramid
      ↓
Validation / emulation
      ↓
INFORM maturity feedback
```

For AI systems, insert **ATLAS** alongside ATT&CK. For embedded devices, use **EMB3D** as the device-focused threat model.

## What belongs where?

| Question | Best starting point |
|---|---|
| What did the adversary do? | ATT&CK |
| In what sequence did the adversary act? | Attack Flow |
| What defensive technique addresses the behavior? | D3FEND |
| How mature is our threat-informed program? | INFORM |
| How good is our detection coverage really? | Summiting the Pyramid |
| Is the behavior ambiguous with legitimate activity? | Ambiguous Techniques |
| Is this an AI-specific adversarial behavior? | ATLAS |
| Is this embedded-device exposure? | EMB3D |
| How do we emulate the behavior safely in a lab? | Caldera |
| How do we visualize technique coverage? | ATT&CK Navigator |
