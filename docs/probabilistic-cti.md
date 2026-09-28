# Probabilistic CTI

Back to [README](../README.md).

Most CTI is written with probabilistic language but implemented with deterministic plumbing. That mismatch is expensive.

## 1. From score to belief update

Static scoring asks how severe something is. Probabilistic CTI asks: given this organization, this adversary evidence and this new observation, how should our belief about the threat change?

~~~text
Prior belief
   +
New evidence
   ↓
Likelihood model
   ↓
Posterior belief
   ↓
Decision / collection priority
~~~

## 2. Bayes is not confidence decoration

For hypothesis H and evidence E:

~~~text
P(H | E) ∝ P(E | H) × P(H)
~~~

For CTI analysts the important questions are the defensibility of the prior, how diagnostic the evidence is under competing hypotheses, whether observations are truly independent, and how sensitive the posterior is to uncertain inputs.

The equation is the easy part. Evidence dependence is where humans enthusiastically sabotage the math.

## 3. Dynamic threat prioritization

A vulnerability can be severe but irrelevant to the current threat picture. Another can have lower static severity but become urgent because exploitation is observed, a relevant actor adopted the technique, the affected asset is consequential, the system is exposed, or campaign activity is increasing.

~~~text
technical severity
+ exploitability evidence
+ active threat evidence
+ asset exposure
+ business / process consequence
+ confidence
~~~

## 4. Bayesian attribution

Attribution becomes healthier when the output is a distribution over hypotheses instead of a single actor label.

~~~text
H1: Actor X
H2: Actor Y
H3: shared tooling / affiliate
H4: unknown actor
~~~

The research track around Bayesian scoring over STIX 2.1 is interesting because it combines structured representation, campaign-level evidence aggregation, evidence-class durability and analyst-readable probability distributions.

## 5. Evidence classes decay differently

| Evidence | Typical durability |
|---|---|
| File hash | Very low |
| IP address | Low |
| Domain / infrastructure cluster | Low–moderate |
| Tool implementation detail | Moderate |
| Behavioral sequence | Moderate–high |
| Operational constraint | High |
| Strategic target preference | Potentially high, context dependent |

Treat these as modeling prompts, not universal constants.

## 6. Bayesian networks

Bayesian networks help when evidence has explicit dependencies.

~~~text
Actor
 ├─► Tool choice
 ├─► Target sector
 └─► TTP sequence
        │
        └─► Observed telemetry
~~~

This is stronger than multiplying supposedly independent likelihoods when the evidence is clearly correlated.

## 7. OT-specific probabilistic analysis

The CyOTE ecosystem provides a practical defensive chain: CATCH normalizes and correlates telemetry, BAM reasons about attack progression, and ACE estimates likely follow-on behavior.

That creates **observation → structure → probability → prioritization**.

## 8. Reporting probabilistic judgments

Expose likelihood, analytic confidence, assumptions, competing hypotheses, evidence that would change the judgment, and time of last update.

Do not collapse likelihood and analytic confidence into one number.

## 9. Failure modes

- convenient but undefended priors;
- duplicated evidence counted more than once;
- ignored conditional dependence;
- fake numerical precision;
- model output treated as causal proof;
- closed-world assumption that the real actor must be in the candidate set;
- historical behavior assumed to be stationary.

Probabilistic CTI is better than intuition only when the model is auditable.