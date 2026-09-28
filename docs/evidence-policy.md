# Evidence & Verification Policy

Back to [README](../README.md).

This repository intentionally distinguishes **resource discovery** from **resource validation**.

## Evidence levels

| Level | Meaning | Examples |
|---|---|---|
| `official` | Primary maintainer, government or standards source | MITRE, NIST, FIRST, OASIS, JPCERT/CC |
| `peer-reviewed` | Published research with identifiable venue/DOI | ThreatMAMBA, ACTIC, CYREM-ORM |
| `preprint` | Public manuscript awaiting or independent of peer review | Synthetic APTs, TACTIC-KG, TGCM |
| `vendor-claim` | Product/vendor assertions not treated as independent validation | Prevyn AI performance claims, ThreatStream timing claims |
| `community` | Public project or community collection | Awesome lists, open tooling |
| `unverified` | Mentioned but not adequately sourced | Watchlist only |

## Rules for numbers

Performance numbers belong in documentation only when:

1. the source can be linked;
2. the evaluation population/dataset is known;
3. the number is attributed to the source;
4. limitations are not omitted.

A vendor statement such as “300× faster” is cataloged as **vendor-reported**, not transformed by Markdown into an objective law of physics.

## Research maturity

| Status | Meaning |
|---|---|
| Operational | Mature enough for routine analyst use |
| Emerging | Useful but still evolving |
| Research | Academic/prototype work |
| Watchlist | Interesting claim requiring stronger evidence |
| Legacy | Historically relevant |
| Archived | Retired/archived |

## Verification workflow

```text
Candidate
   ↓
Locate primary source
   ↓
Check owner / publication / DOI
   ↓
Check maintenance or publication date
   ↓
Classify evidence level
   ↓
Separate verified facts from source claims
   ↓
Add analyst use case
   ↓
Promote to catalog
```

## What is not promoted automatically

The following do not become “verified” just because they appear in a pasted list:

- uncited model names;
- performance numbers without a paper or evaluation;
- marketing claims repeated by third parties;
- GitHub projects with unclear provenance;
- frameworks whose only evidence is another awesome-list;
- future roadmap promises.

They can still be valuable leads. That is what `catalog/watchlist.yaml` is for.
