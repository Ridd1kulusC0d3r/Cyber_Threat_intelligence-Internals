# Graph & Provenance Hunting

Back to [README](../README.md).

Graph-based CTI is useful because adversary activity is relational by nature. A list of events answers what happened; a graph can help answer what is connected, what preceded what and which relationships make a hypothesis coherent.

## 1. Three graph layers

### Intelligence graph

~~~text
actor ─uses─► malware
actor ─targets─► sector
malware ─contacts─► infrastructure
campaign ─uses─► technique
~~~

### Attack / behavior graph

~~~text
initial access
   ↓
execution
   ↓
credential access
   ↓
lateral movement
   ↓
collection
~~~

### Provenance graph

~~~text
process
  ├─ spawned → process
  ├─ read → file
  ├─ wrote → file
  └─ connected → endpoint
~~~

The interesting frontier is linking these layers without pretending they are interchangeable.

## 2. ProHunter

[ProHunter](https://github.com/xueboQiu/ProHunter) represents the established provenance-hunting direction: extract attack behavior from CTI and search for corresponding subgraph patterns in whole-system provenance data.

## 3. APT-CGLP

[APT-CGLP](https://doi.org/10.1145/3770854.3780275) reduces the hand-built intermediate attack-graph step through cross-modal graph-language alignment between CTI report text and provenance graphs.

## 4. CTI-Thinker

[CTI-Thinker](https://doi.org/10.1186/s42400-025-00505-y) combines structured CTI extraction, semantic alignment and GraphRAG-style reasoning over ATT&CK-aware knowledge.

Its architecture separates extraction, normalization, graph construction/fusion and reasoning. That separation makes evaluation less mystical.

## 5. Unsupervised reconstruction

[From logs to tactics](https://doi.org/10.1007/s10207-026-01254-w) combines GNN-based event-sequence reconstruction, semantic clustering, LLM summarization and symbolic plus semantic ATT&CK mapping.

The practical idea is **meta-alert reconstruction**: reduce low-level alert volume while preserving the multi-stage intrusion narrative.

## 6. Heterogeneous attribution graphs

The peer-reviewed heterogeneous-GNN attribution work links APT groups, contextualized TTPs and Cyber Kill Chain stages. Two actors can use the same technique at different operational stages, so lifecycle context can improve discrimination compared with flat technique overlap.

## 7. Campaign demixing

TGCM research asks a deceptively important question: what if the observed sequence contains more than one campaign?

That is realistic in large environments where multiple incidents overlap, shared infrastructure exists, admin activity is interleaved and several actors touch the same estate.

## 8. Graph hygiene

A CTI graph should preserve provenance of every edge, first/last observed, confidence, relationship type, source reliability, information credibility, temporal validity, aliases and contradiction/evidence-against relationships.

A knowledge graph without provenance is merely a very confident rumor network.

## 9. Evaluation questions

- How were entities normalized?
- How are aliases handled?
- Can edges expire?
- Is temporal order represented?
- Are negative or contradicting relationships supported?
- Does the model distinguish correlation from causation?
- Can an analyst trace a conclusion to source evidence?
- What happens when the true actor is not represented in training data?