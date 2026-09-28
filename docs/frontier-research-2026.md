# CTI Frontier Research — 2026

Back to [README](../README.md).

This page is a **research radar**, not a production shopping list.

The useful frontier in CTI is moving from “collect more indicators” toward **structured evidence, temporal reasoning, provenance graphs, adversarially robust pipelines, agentic knowledge extraction and quantitative risk**.

## Research maturity legend

| Label | Meaning |
|---|---|
| **Operational** | Mature enough for routine analyst workflows |
| **Peer-reviewed research** | Published academic evidence; still requires local validation |
| **Preprint** | Public manuscript; promising but not settled |
| **Vendor claim** | Useful product direction; metrics are self-reported |
| **Watchlist** | Interesting lead that lacks adequate primary evidence |

## 1. Attribution under AI-generated tradecraft

### ThreatMAMBA

[ThreatMAMBA](https://doi.org/10.1109/TIFS.2026.3685967) studies **temporally robust threat attribution** using evolving heterogeneous threat information graphs.

The practical lesson is important even if you never implement the model: attribution evidence changes over time, so a system should not assume the final incident graph is already available during early-stage analysis.

### Synthetic APTs

[Synthetic APTs](https://arxiv.org/abs/2606.07158) is a preprint exploring AI-controlled adversaries configured to imitate known APT tradecraft.

Treat its conclusions as a stress test of a common assumption:

> **TTP similarity is evidence, not identity.**

That does not make ATT&CK useless for attribution. It makes single-dimension TTP fingerprinting a weaker basis for actor identity.

### ATTRACT

[ATTRACT](https://github.com/nanda-rani/ATTRACT) uses ordered and repeated sequences of ATT&CK TTPs aligned to kill-chain stages.

This moves attribution from “which techniques overlap?” toward “how are behaviors ordered and repeated?”

## 2. CTI pipeline poisoning and authenticity

The paper [False Alarms, Real Damage](https://doi.org/10.1016/j.future.2026.108603) studies adversarial manipulation of text-based CTI systems, including evasion, flooding and poisoning.

This matters because modern automated pipelines increasingly ingest:

- social posts;
- threat reports;
- forums;
- vendor blogs;
- machine-generated summaries;
- AI-produced text.

A mature CTI pipeline therefore needs **provenance and authenticity checks before promotion into trusted knowledge**.

The repository's own response is deliberately boring and useful:

```text
candidate source
      ↓
primary-source resolution
      ↓
evidence classification
      ↓
verification state
      ↓
analyst use case
      ↓
catalog promotion
```

## 3. Local knowledge-graph construction

### ACTIC

[ACTIC](https://doi.org/10.1049/cmu2.70162) uses a locally deployed large language model to extract threat entities, relationships and attack steps into a two-layer CTI/attack knowledge graph.

The strategic value is not “LLM magic.” It is **data sovereignty plus structured extraction**.

### TACTIC-KG

[TACTIC-KG](https://arxiv.org/abs/2607.05001) decomposes knowledge-graph construction into specialized LLM agents for extraction, typing, verification and curation.

This is a promising architecture for reducing the fragility of one giant prompt doing everything badly.

## 4. Interleaved campaign reconstruction

[TGCM](https://arxiv.org/abs/2606.18651) targets a hard real-world problem: observed technique sequences can contain **multiple campaigns interleaved in time**.

The research direction matters because CTI pipelines often make an unstated assumption:

> one sequence of observed activity = one campaign.

That assumption can fail badly in shared infrastructure, large environments and concurrent intrusions.

## 5. Bayesian CTI

[Quantifying cyber threat using Bayesian statistical analysis](https://doi.org/10.1007/s10207-026-01220-6) explores updating system-specific threat probabilities as new CTI arrives.

This is a more defensible direction than treating:

- CVSS as exploitation probability;
- one vendor score as ground truth;
- analyst confidence as a percentage invented during report formatting.

Bayesian methods force priors and likelihood assumptions into the open, which is inconvenient but healthy.

## 6. Federated CTI and privacy

[Federated Learning and Zero-Trust Architecture for Privacy Preservation and Collaborative Threat Intelligence](https://doi.org/10.1155/jcnc/8893656) explores collaborative modeling without centralizing raw participant data.

It is research, not evidence that centralized MISP/OpenCTI sharing is “dead.” The more defensible conclusion is that **privacy-preserving and trust-aware collaborative analysis is an active research direction**.

## 7. Deception as intelligence

[PHANTOM](https://doi.org/10.1007/s10207-026-01323-0) explores context-aware honeytoken generation and evaluation.

Its interesting idea is broader than any single benchmark: deception becomes more credible when it reflects the **semantic and organizational context** of the environment.

Use the paper as research input, not as a promise that automated deception is universally indistinguishable from legitimate secrets.

## 8. CTI translated into financial risk

[CYREM-ORM](https://doi.org/10.1016/j.cose.2026.104873) explores connecting cyber threat information to quantitative organizational risk and financial-loss reasoning.

This is strategically important because CTI that cannot influence:

- prioritization;
- resource allocation;
- expected-loss scenarios;
- control investment;

risks becoming an expensive publication department.

## 9. Whole-system provenance

[ProHunter](https://github.com/xueboQiu/ProHunter) represents an important threat-hunting direction: use whole-system provenance graphs to reconstruct relationships and match threat patterns derived from CTI.

Provenance does not eliminate telemetry gaps, but it moves analysis from isolated log correlations toward **causal relationships**.

## Watchlist, not doctrine

Several concepts supplied in the research notes are intentionally kept in [catalog/watchlist.yaml](../catalog/watchlist.yaml), including L-TDoA/SynGNN, KubeRTSec, CTI-HAL, TTPXHunter, MLADF, APT-CGLP and HexAttribution.

They may prove valuable. They are not promoted until a sufficiently authoritative primary source is confirmed.

That distinction is the entire point of having a research radar instead of a hype radar.
