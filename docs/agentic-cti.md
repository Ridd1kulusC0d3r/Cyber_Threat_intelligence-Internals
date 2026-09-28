# Agentic CTI & AI-Assisted Intelligence

Back to [README](../README.md).

Agentic CTI is moving from summarization toward **multi-step investigation workflows**: planning, search, enrichment, correlation, malware analysis and report generation.

The marketing also moves faster than the evidence. This page therefore separates **capability** from **vendor-reported performance**.

## Current platforms to track

| Platform | Owner | Main CTI use | Evidence treatment |
|---|---|---|---|
| [Google Security AI / Agentic Threat Intelligence](https://cloud.google.com/security/ai) | Google | Threat investigation using Gemini with Google Threat Intelligence, Mandiant and VirusTotal context | Official product source |
| [Prevyn AI](https://www.group-ib.com/prevyn-ai/) | Group-IB | Multi-agent threat research, actor/dark-web/malware intelligence and assistive XDR analysis | Vendor claims |
| [Vellox Reverser](https://www.boozallen.com/expertise/products/vellox.html) | Booz Allen | AI-assisted malware reverse engineering and CTI reporting | Vendor claims |
| [ThreatStream Next-Gen](https://www.anomali.com/press/anomali-launches-threatstream-next-gen-to-turn-intelligence-into-action-at-the-speed-threats-demand) | Anomali | PIRs, intelligence search, cases, prioritization and reporting | Vendor claims |
| [Protos AI](https://www.protoslabs.io/) | Protos Labs | Multi-agent adversary-risk intelligence and report workflows | Vendor claims |

## What “agentic” should mean operationally

A useful CTI agent should be able to perform bounded parts of this loop:

```text
intelligence requirement
        ↓
collection plan
        ↓
source discovery
        ↓
evidence retrieval
        ↓
entity extraction
        ↓
enrichment / correlation
        ↓
hypothesis generation
        ↓
source-backed assessment
        ↓
human review
```

If the system merely rewrites a threat report in friendlier prose, it is a summarizer with excellent branding.

## Human approval is not optional theater

High-value controls include:

- require citations to retrieved evidence;
- distinguish source claims from model inference;
- preserve original publication dates;
- record tool calls and evidence provenance;
- prevent silent promotion of unverified entities;
- gate consequential actions behind human approval;
- expose confidence and contradictions;
- keep sensitive datasets local where required.

## Local models and sovereignty

Projects such as [ACTIC](https://doi.org/10.1049/cmu2.70162) show why local deployment matters for CTI:

- reports may contain sensitive incident details;
- unpublished IOCs may be restricted;
- customer identities may be confidential;
- organization-specific intelligence may have handling restrictions.

Local deployment is therefore an architectural control, not just a cost optimization.

## Agentic knowledge graphs

[Tactic-KG](https://arxiv.org/abs/2607.05001) explores specialized agents for:

- extraction;
- entity typing;
- verification;
- curation.

This modular design is compelling because each stage can be evaluated separately. One monolithic agent that “does CTI” makes failure analysis much harder.

## Adversarial robustness

LLM-backed CTI systems can be influenced by malicious or low-quality source text.

The [False Alarms, Real Damage](https://doi.org/10.1016/j.future.2026.108603) research direction should therefore be treated as part of system design:

- source authentication;
- provenance tracking;
- trust boundaries;
- poisoning resistance;
- validation before knowledge-base insertion.

## Vendor metrics

The catalog stores performance claims as `vendor-claim`.

Examples include:

- workflow acceleration;
- number of specialized agents;
- corpus scale;
- alert-quality improvement;
- investigation speed.

These numbers can be useful for vendor evaluation, but they are **not independent benchmarks unless replicated by third parties**.

## Evaluation checklist

Before trusting an agentic CTI platform, test:

1. Does every material claim link back to evidence?
2. Can the system distinguish inference from retrieved fact?
3. Does it preserve conflicting evidence?
4. Can analysts inspect the investigation trail?
5. How does it handle malicious source text?
6. What data leaves the organization?
7. Can you restrict sources by TLP/classification?
8. What happens when the agent is uncertain?
9. Can the same task be reproduced?
10. Can a human veto every consequential action?

Agentic automation can reduce analyst toil. It should not automate epistemic overconfidence.
