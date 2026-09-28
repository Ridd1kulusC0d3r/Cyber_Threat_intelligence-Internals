# Attribution, Analytic Rigor & Confidence

Back to [README](../README.md).

Threat attribution is not a binary label. It is a structured claim supported by evidence, uncertainty and competing explanations.

## Pyramid of Pain

[David Bianco's Pyramid of Pain](https://www.sans.org/tools/the-pyramid-of-pain) ranks indicator types by how costly they are for an adversary to change:

```text
TTPs
Tools
Network / Host Artifacts
Domain Names
IP Addresses
Hash Values
```

The useful lesson is not “hashes are useless.” Hashes can be precise and operationally valuable. The lesson is that **durability and adversary cost generally increase as analysis moves from atomic indicators toward behavior**.

This now connects directly to CTID's [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/), which treats detection engineering as an evidence problem rather than a colored ATT&CK heatmap.

## Diamond Model

The [Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/) represents an event with four core features:

- adversary;
- capability;
- infrastructure;
- victim.

The model is especially useful for pivoting relationships and building activity threads rather than prematurely attaching a famous actor name to a handful of indicators.

## Unit 42 Attribution Framework

[Unit 42's framework](https://unit42.paloaltonetworks.com/unit-42-attribution-framework/) operationalizes attribution with:

1. **activity clusters**;
2. **temporary threat groups**;
3. **formally named threat actors**.

It combines Diamond Model reasoning with reliability/credibility scoring inspired by the Admiralty System.

The key practice worth copying is **separating clustering from naming**. A cluster can be analytically useful long before the evidence justifies a formal actor identity.

## Source reliability and information credibility

Do not collapse these into a single score.

```text
Source reliability: can this source generally be trusted?
Information credibility: how well is this specific claim supported?
```

A reliable organization can publish a low-confidence hypothesis. A previously unknown source can provide authentic primary evidence.

## Likelihood and confidence

[ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) explicitly separates:

- **likelihood/probability** of an event or explanation;
- **analytic confidence** in the evidence and reasoning supporting the judgment.

Do not invent numerical precision when the evidence does not support it.

## ACH: useful discipline, not sacred machinery

[Analysis of Competing Hypotheses](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) is valuable because it forces analysts to search for **disconfirming** evidence.

But recent empirical reviews matter. A 2024 critical review found little evidence that mandatory/full ACH reliably improves judgment quality, and some studies found potential harms or inconsistency.

Use ACH as a structured challenge mechanism, not an oracle.

### Better questions

- What evidence would falsify the leading hypothesis?
- Which evidence is truly diagnostic?
- Are multiple items actually derived from the same source?
- Could the evidence be deliberately planted?
- Which assumptions are load-bearing?
- What new observation would change the judgment?

## Bayesian extensions

Bayesian networks and Bayesian variants of competing-hypothesis analysis replace simple C/I/N counting with explicit conditional probabilities.

The important conceptual change is:

```text
Instead of:
"E1 is inconsistent with H2"

Ask:
"P(E1 | H2) = ?"
```

This makes assumptions visible and allows sensitivity analysis, but it does not magically create good priors or independent evidence.

## Behavioral attribution research

Current research worth tracking:

| Resource | Evidence | Why it matters |
|---|---|---|
| [ATTRACT](https://github.com/nanda-rani/ATTRACT) | Peer-reviewed | Uses ordered/repeated TTP sequences mapped to kill-chain phases |
| [ThreatMAMBA](https://doi.org/10.1109/TIFS.2026.3685967) | Peer-reviewed | Studies temporally robust attribution during evolving attacks |
| [Synthetic APTs](https://arxiv.org/abs/2606.07158) | Preprint | Tests whether AI agents can imitate known APT tradecraft, challenging TTP-only attribution |
| [Unit 42 Attribution Framework](https://unit42.paloaltonetworks.com/unit-42-attribution-framework/) | Vendor methodology | Practical cluster → temporary group → named actor workflow |

Do **not** interpret any one of these as proof that TTP-based attribution is “dead.” The stronger conclusion is narrower: attribution should be **multi-source, temporal, relational and explicit about uncertainty**.

## Multi-actor operations

Modern criminal operations often involve separate access brokers, infrastructure providers, malware operators, affiliates and monetization actors.

Model relationships separately:

```text
Access provider ──► intrusion access
Operator        ──► lateral movement / deployment
Ransomware svc  ──► encryption / leak infrastructure
Broker          ──► monetization / resale
```

Do not force the entire intrusion into one actor label merely because the final payload is famous.

## Structured analytic techniques

Useful techniques include:

- Key Assumptions Check;
- Devil's Advocacy;
- What-If Analysis;
- indicators/signposts;
- decision trees;
- alternative futures;
- ACH where appropriate.

The method should be proportional to the decision. Applying a heavyweight SAT to every low-risk IOC review merely creates an extremely sophisticated way to miss your deadline.

## Attribution guardrails

Never make a strong attribution from:

- one IP;
- one domain;
- one malware string;
- one ATT&CK technique;
- one language clue;
- one vendor alias;
- one social-media claim.

Preserve the difference between **technical attribution** and claims of state direction or political responsibility, which require evidence beyond routine CTI telemetry.
