# OT/ICS Threat Intelligence

Back to [README](../README.md).

OT/ICS intelligence is not simply enterprise CTI with industrial acronyms attached. The analytical center of gravity changes from **data compromise** to **process consequence**.

## 1. Start with the control loop

A useful OT intelligence model begins with the physical process:

~~~text
Threat actor
    ↓
Access path
    ↓
Engineering / operator layer
    ↓
Control logic / setpoints / commands
    ↓
PLC / RTU / controller behavior
    ↓
Physical process
    ↓
Safety / reliability / availability consequence
~~~

The 2026 Dragos Year in Review is useful context because it describes adversaries moving beyond generic footholds toward mapping industrial control loops and learning where commands originate, how they propagate and what operational effects may be induced.

Treat that as vendor-observed intelligence, not as universal prevalence.

## 2. OT intelligence requirements

Useful OT PIRs look different from generic IT questions:

- Which adversaries are actively targeting our industrial sector?
- Which remote-access pathways expose systems that influence the physical process?
- Which engineering workstations, HMIs, PLCs or gateways are most consequential?
- Which behaviors indicate reconnaissance of the control loop?
- Which operational anomalies should trigger a cyber investigation?
- Which ATT&CK for ICS techniques can we currently observe?
- Which telemetry disappears before incident response can collect it?
- Which threat reports predict behavior relevant to our process, not merely our vendor stack?

## 3. CyOTE: a connected OT intelligence stack

The Idaho National Laboratory CyOTE ecosystem is useful as a connected analytical chain rather than isolated tools.

### OPTIC

[OPTIC](https://cyote.inl.gov/tools/operational-process-for-trigger-identification-and-comprehension-optic/) captures human-observed operational anomalies and contextualizes them for downstream analysis.

~~~text
operator observation
        ↓
structured trigger
        ↓
ATT&CK / historical context
        ↓
STIX 2.1
~~~

### CATCH

[CATCH](https://cyote.inl.gov/tools/collection-and-analysis-of-telemetry-for-cyote-heuristics-catch/) converts OT telemetry into STIX 2.1, preserves relationships in Neo4j and applies graph queries to ATT&CK for ICS behavior.

~~~text
telemetry
   ↓
normalized observable
   ↓
relationship graph
   ↓
behavioral pattern
   ↓
candidate attack activity
~~~

### BAM

The [Bayesian Attack Model](https://cyote.inl.gov/tools/bayesian-attack-model-bam/) adds probabilistic reasoning across attack stages.

Instead of asking only which technique was observed, ask which progression hypothesis becomes more plausible given the new evidence.

### ACE

The [Attack Chain Estimator](https://cyote.inl.gov/tools/attack-chain-estimator-ace/) extends this toward predictive analysis by estimating ATT&CK for ICS behavior from reporting and using historical attack-chain knowledge to estimate likely follow-on behavior.

Use prediction as a **prioritization aid**, not as certainty.

## 4. Detect at the operator layer, corroborate at the controller layer

A useful defensive heuristic is: **Detect at the HMI, validate at the PLC.**

At the operator/engineering layer, correlate unusual sessions, commands outside maintenance windows, unexpected tag or setpoint patterns, engineering-workstation changes and remote-access behavior that deviates from baseline.

At the controller/process layer, corroborate with controller mode changes, project or logic changes, process-variable behavior, expected maintenance state and physical-process consequence.

The point is correlation across layers, not a single magic sensor.

## 5. LOTL in OT

Living-off-the-land behavior is difficult in industrial environments because many legitimate administrative and engineering actions are powerful by design.

~~~text
identity
+ asset role
+ maintenance window
+ command context
+ network path
+ process state
+ historical baseline
~~~

A command that is harmless during planned maintenance can become high-signal at an unusual time from an unexpected remote path.

## 6. Collective defense

| Resource | Model |
|---|---|
| [OT-ISAC](https://www.otisac.org/) | Operator/government/partner intelligence-sharing community |
| [Neighborhood Keeper](https://www.dragos.com/cybersecurity-platform/neighborhood-keeper/) | Anonymized collective defense for Dragos participants |
| [ETHOS](https://github.com/ethos-org/ethos-initiative-information) | Open-source early-warning sharing for emerging OT activity |
| [EE-ISAC](https://www.ee-isac.eu/) | European energy-sector sharing, including MISP/Nextcloud member workflows |

Collective intelligence is valuable when it adds **context and corroboration**, not simply more indicators.

## 7. OT analytical stack

~~~text
Asset / process knowledge
        ↓
OT telemetry + operator observations
        ↓
STIX / graph normalization
        ↓
ATT&CK for ICS mapping
        ↓
probabilistic progression model
        ↓
process-consequence assessment
        ↓
hunting / detection / response priority
~~~

## 8. Evidence discipline

Always record observation population, sector/geography, whether data comes from customers or IR engagements, whether the metric represents organizations/incidents/assets/exercises, and whether the number is vendor-reported or independently reproduced.

Industrial security is complicated enough without converting a vendor sample into a law of nature.