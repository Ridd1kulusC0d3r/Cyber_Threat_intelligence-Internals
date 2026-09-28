# Framework Landscape: MITRE and Alternatives

Back to [README](../README.md).

This guide answers a more useful question than “what competes with ATT&CK?”: **which model belongs at which layer of the security problem?**

## Adversary behavior and threat modeling

| Framework | Steward | Primary lens | Relationship to ATT&CK |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | MITRE | Observed adversary behavior | Behavioral baseline |
| [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) | Lockheed Martin | Intrusion lifecycle | Higher-level sequence model |
| [STRIDE](https://learn.microsoft.com/azure/security/develop/threat-modeling-tool-threats) | Microsoft | System/design threats | Design-time threat modeling rather than actor behavior |
| [SPARTA](https://sparta.aerospace.org/) | The Aerospace Corporation | Space systems / spacecraft | Domain-specific TTP matrix |
| [SITF](https://www.wiz.io/blog/sitf-sdlc-threat-framework) | Wiz | SDLC infrastructure | Focuses on repositories, CI/CD and software-production infrastructure |
| [PR3TACK](https://pr3tack.org/) | Community | Plausible unobserved TTPs | Preemptive complement to retrospective knowledge bases |
| [CAPEC](https://capec.mitre.org/) | MITRE | Attack patterns | More design/exploitation-pattern oriented |

### Practical selection

- Use **ATT&CK** to normalize observed behavior.
- Use **Kill Chain** when a simple lifecycle narrative is more useful than technique detail.
- Use **STRIDE** during architecture and software design.
- Use **SPARTA** for space-cyber analysis.
- Use **SITF** when the software delivery infrastructure itself is the threat surface.
- Treat **PR3TACK** as anticipatory research rather than evidence of observed adversary behavior.

## Defensive frameworks

| Framework | Layer | Best question |
|---|---|---|
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Strategic / governance | What cybersecurity outcomes should the organization manage? |
| [CIS Controls v8.1](https://www.cisecurity.org/controls/v8) | Tactical / control prioritization | Which safeguards should we implement first? |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Technical / countermeasure ontology | How do technical defensive countermeasures relate to artifacts and offensive behavior? |
| [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) | Detection engineering | How strong and complete is a behavioral detection? |

A useful simplification is:

```text
NIST CSF       → governance outcomes
CIS Controls   → prioritized safeguards
D3FEND         → technical defensive knowledge
Detection work → evidence that controls actually see behavior
```

They overlap, but they are not interchangeable.

## Adversary emulation and validation

| Resource | Scope | Positioning |
|---|---|---|
| [MITRE Caldera](https://caldera.mitre.org/) | Automated adversary emulation | Multi-step ATT&CK-informed emulation |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Atomic behavior tests | Granular validation of individual techniques |
| [Stratus Red Team](https://github.com/DataDog/stratus-red-team) | Cloud behavior tests | Lightweight cloud-specific validation |
| [Splunk Attack Range](https://github.com/splunk/attack_range) | Detection lab | Generate telemetry and test security content in a controlled lab |

These resources should be used only in authorized test environments.

## Visualization and coverage

| Tool | Best use |
|---|---|
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | Visual layers and technique comparison |
| [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) | Visibility/detection gap analysis and data-source tracking |
| [Tidal Cyber](https://www.tidalcyber.com/) | Commercial threat-informed defense and technique mapping |
| [Maltego](https://www.maltego.com/) | Entity/link analysis for investigations rather than ATT&CK coverage |

## CTI representation and exchange

| Technology | Steward | Role |
|---|---|---|
| [STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) | OASIS | CTI data model |
| [TAXII 2.1](https://www.oasis-open.org/standard/taxii-version-2-1/) | OASIS | CTI exchange protocol/API model |
| [MISP](https://www.misp-project.org/) | MISP Project | Operational sharing platform and native data model |
| [OpenCTI](https://www.opencti.io/) | Filigran / community | STIX-native CTI knowledge platform |
| OpenIOC | Legacy / reference | Older IOC description format still encountered in tooling |
| CybOX | Historical | Observable model absorbed into the STIX 2.x object model |

## Attack-pattern and weakness ecosystem

```text
CWE       → what weakness exists?
CAPEC     → how can an attack pattern exploit weaknesses?
ATT&CK    → what adversary behavior is observed in operations?
D3FEND    → what technical defensive knowledge can counter behavior?
```

Add [LINDDUN](https://linddun.org/) for privacy threat modeling and STRIDE for security threat modeling.

## AI security

| Resource | Layer | Use |
|---|---|---|
| [MITRE ATLAS](https://atlas.mitre.org/) | Behavioral | Adversarial behavior involving AI-enabled systems |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Risk/governance | Trustworthy AI risk management |
| [OWASP Top 10 for LLM/GenAI](https://genai.owasp.org/llm-top-10/) | Application engineering | Common application-level LLM/GenAI security risks |

Use them together rather than pretending one matrix solves governance, architecture and attacker behavior simultaneously. Humans tried that approach with spreadsheets already.

## Embedded, IoT and OT

| Resource | Focus |
|---|---|
| [MITRE EMB3D](https://emb3d.mitre.org/) | Embedded-device properties, threats and mitigations |
| [MITRE ESTM](https://estm.mitre.org/) | ATT&CK-like tactics and techniques for embedded systems |
| [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) | Observed adversary behavior in ICS |
| [SPARTA](https://sparta.aerospace.org/) | Space systems, spacecraft and ground segment |

EMB3D and ESTM are complementary: EMB3D is a device threat model; ESTM is a behavior-oriented matrix.

## Risk assessment methods

| Method | Style | Best use |
|---|---|---|
| [OCTAVE Allegro](https://sei.cmu.edu/library/introducing-octave-allegro-improving-the-information-security-risk-assessment-process/) | Asset/information-centric | Structured organizational assessment |
| [FAIR](https://www.fairinstitute.org/what-is-fair) | Quantitative | Express cyber risk in financial/probabilistic terms |
| [NIST SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Risk assessment guidance | US/NIST-aligned risk programs |
| [CORAS](https://coras.sourceforge.net/) | Model-based | Diagram-driven security risk analysis |
| [MAGERIT](https://administracionelectronica.gob.es/pae_Home/pae_Documentacion/pae_Metodolog/pae_Magerit.html) | Structured public-sector methodology | Risk analysis and management, especially Spanish public administration |

## Program maturity

Add [CTI-CMM](https://cti-cmm.org/) when the question is not “which TTP?” but **“how mature is our intelligence capability?”**.

That sits naturally beside [INFORM](https://ctid.mitre.org/projects/inform-your-defense/), which evaluates broader threat-informed-defense maturity.
