# Contributing

Contributions are welcome when they make the directory more useful to a working CTI analyst.

## Add resources to the catalog, not directly to the website

The machine-readable files under `catalog/` are the source of truth. The website is generated from them.

Choose the shard that best fits the resource:

- `core.yaml` — foundational CTI resources;
- `frameworks.yaml` — frameworks, models and standards;
- `detection.yaml` — detection, hunting and validation;
- `attribution.yaml` — attribution and analytic methods;
- `ai-research.yaml` — CTI/AI academic research;
- `vendors.yaml` — commercial/vendor platforms;
- `datasets.yaml` — datasets and corpora;
- `specialized.yaml` — specialized domains;
- `watchlist.yaml` — promising but insufficiently verified leads.

## Resource fields

Recommended record:

```yaml
- name:
  url:
  category:
  source_class:
  intelligence_levels: []
  access:
  lifecycle:
  owner:
  evidence_level:
  verification:
  last_reviewed:
  use:
  notes:
  tags: []
```

### Source class

- **A** — authoritative / standards / government / CERT / primary institutional dataset
- **B** — first-party vendor or research-team intelligence
- **C** — community / aggregation / analyst-maintained project

### Evidence level

- `official` — primary official/maintainer source
- `peer-reviewed` — identifiable peer-reviewed publication
- `preprint` — public research manuscript not treated as peer-reviewed
- `vendor-claim` — first-party product/vendor assertion
- `community` — maintained community resource
- `unverified` — lead that still needs stronger evidence

### Verification

- `verified` — source located and description validated
- `provisional` — resource exists but important claims/maturity still need validation
- `watchlist` — not ready for operational promotion
- `rejected` — false, misleading, unsafe, duplicate or no longer useful

### Lifecycle

Common values:

- `active`
- `emerging`
- `research`
- `reference`
- `legacy`
- `archived`
- `watchlist`

## Quality rules

Prefer:

- primary sources;
- official documentation;
- maintained projects;
- original threat research;
- identifiable DOIs or proceedings for academic claims;
- machine-readable data/APIs when available;
- transparent provenance;
- links to the original report rather than reposts.

Avoid:

- link farms with no provenance;
- copied threat reports without attribution;
- abandoned services presented as current;
- marketing numbers presented as independent benchmarks;
- preprints described as established scientific consensus;
- “frameworks” whose only source is another list;
- unsafe or unauthorized activity.

## Vendor metrics

If a vendor says a workflow is “300× faster,” “98% accurate,” or uses “N specialized agents,” record the claim only when useful and mark it as **vendor-reported**.

Do not convert marketing into independent evidence through the magical ritual of copying it into Markdown.

## Lifecycle review

For software or GitHub projects, check:

1. archive status;
2. recent meaningful commits/releases;
3. current documentation;
4. issue/PR activity when relevant;
5. supported dependencies;
6. whether an official successor exists.

Historical value is legitimate. Historical value is not the same as current maintenance.

## Validate locally

```bash
pip install -r requirements.txt
python scripts/build_catalog.py --check
python scripts/build_catalog.py
```

## Pull request checklist

- [ ] URL points to the most primary source practical.
- [ ] Category is correct.
- [ ] Source class is defensible.
- [ ] Intelligence level is identified.
- [ ] Evidence level is identified.
- [ ] Verification state is honest.
- [ ] Lifecycle has been checked.
- [ ] Last-reviewed date is present.
- [ ] Use case describes analyst value rather than marketing copy.
- [ ] Commercial resources are labeled.
- [ ] Performance claims are attributed.
- [ ] Archived/legacy projects are not presented as current defaults.
- [ ] Watchlist items are not mixed into verified operational resources.
- [ ] `python scripts/build_catalog.py --check` passes.
