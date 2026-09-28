# Threat Hunting Frontier

Back to [README](../README.md).

Threat hunting is increasingly a problem of **telemetry integrity, causal reconstruction and ephemeral evidence**, not merely writing increasingly elaborate SIEM queries.

This page stays defensive: it focuses on what hunters need to observe and validate, not on procedures for bypassing security products.

## 1. Real-time endpoint telemetry

[JPCERT/CC YAMAGoya](https://github.com/JPCERTCC/YAMAGoya) is a useful modern reference because it combines:

- ETW-based monitoring;
- Sigma matching;
- YARA scanning;
- process, file, registry, network and PowerShell telemetry;
- memory-oriented detection.

It demonstrates an important architectural pattern: detection content and endpoint observation can be kept closer together instead of waiting for every event to make a round trip through a central SIEM.

## 2. Whole-system provenance

[ProHunter](https://github.com/xueboQiu/ProHunter) builds provenance graphs from audit data and searches for attack subgraphs derived from CTI.

For hunters, this changes the question from:

> “Which log line matches my query?”

to:

> “Which sequence of causally related system actions resembles the behavior described in threat intelligence?”

## 3. Kernel and runtime visibility

The supplied research notes highlight a useful defensive concern: **the telemetry collection mechanism can itself be manipulated or blinded**.

For Linux/container hunting, treat runtime visibility as layered:

```text
application logs
     ↓
container/runtime events
     ↓
host audit telemetry
     ↓
kernel/eBPF observations
     ↓
memory / provenance corroboration
```

No single layer should be treated as perfect ground truth.

## 4. Cloud and ephemeral evidence

Cloud hunting differs from endpoint hunting because:

- identities often matter more than binaries;
- control-plane API actions can be legitimate in syntax but malicious in intent;
- workloads disappear quickly;
- evidence retention varies by service;
- service principals and workload identities require behavioral baselines.

Useful hunting dimensions include:

- unusual role assumptions;
- new region/resource access;
- unexpected service-to-service relationships;
- anomalous API sequences;
- control-plane actions outside normal deployment patterns;
- rapid evidence capture when short-lived workloads trigger detections.

## 5. Detection quality, not ATT&CK decoration

[Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) is a better companion to hunting than a simple technique heatmap.

For each analytic, ask:

1. Which implementations of the technique can it observe?
2. Which telemetry is mandatory?
3. Which legitimate activities look similar?
4. Which contextual signals improve precision?
5. What would cause the analytic to go blind?
6. How was it validated?

## 6. Adversary emulation for hunters

Use controlled defensive-validation tooling according to scope:

| Need | Resource |
|---|---|
| Small behavior test | [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) |
| Multi-step emulation | [MITRE Caldera](https://caldera.mitre.org/) |
| Cloud behavior validation | [Stratus Red Team](https://github.com/DataDog/stratus-red-team) |
| Instrumented SIEM lab | [Splunk Attack Range](https://github.com/splunk/attack_range) |

Only use emulation in systems you are explicitly authorized to test.

## 7. Infrastructure hunting

An IOC should be treated as a **starting node**, not the finished product.

Useful defensive pivots include:

- certificate relationships;
- passive/active DNS history;
- ASN and hosting context;
- web-stack fingerprints;
- infrastructure reuse;
- first/last-seen timing;
- co-hosting and shared-service context.

The goal is to discover **relationships and infrastructure clusters**, while avoiding the classic error of assuming shared hosting automatically means shared ownership.

## 8. OT/ICS hunting

In OT, threat hunting must include the physical process.

Useful questions include:

- Which control asset is affected?
- Which process function could change?
- What is the safety consequence?
- Is the activity expected for this engineering workstation or controller?
- Does the network behavior align with scheduled maintenance?
- Which ATT&CK for ICS behavior explains the event?
- What process telemetry can corroborate the cyber telemetry?

Technique mapping without process consequence is incomplete OT intelligence.

## 9. Deception as a sensor

Research such as [PHANTOM](https://doi.org/10.1007/s10207-026-01323-0) supports a broader direction: deception artifacts can become **high-signal sensors** when interaction with them has little legitimate explanation.

A mature program records:

- why the decoy exists;
- who should legitimately access it;
- what interaction constitutes signal;
- how evidence will be preserved;
- how false positives will be handled.

## Hunting maturity ladder

```text
IOC queries
   ↓
behavioral hypotheses
   ↓
ATT&CK-informed hunting
   ↓
context-aware detections
   ↓
provenance / graph hunting
   ↓
telemetry-integrity checks
   ↓
cross-layer corroboration
```

The goal is not to abandon logs. It is to stop pretending that one telemetry source has a divine right to be correct.
