# Machine-readable CTI catalog

The files in this directory are the repository's structured source of truth.

## Shards

| File | Scope |
|---|---|
| `core.yaml` | Foundational CTI resources |
| `frameworks.yaml` | Frameworks, models, risk and standards |
| `detection.yaml` | Detection engineering, hunting and validation |
| `attribution.yaml` | Attribution, confidence and analytic methods |
| `ai-research.yaml` | CTI/AI research |
| `vendors.yaml` | Vendor platforms and product capabilities |
| `datasets.yaml` | CTI and provenance datasets |
| `specialized.yaml` | Specialized intelligence domains |
| `watchlist.yaml` | Interesting leads not yet sufficiently verified |

## Schema

```yaml
- name:
  url:
  category:
  source_class:
  intelligence_levels:
    - strategic
    - operational
    - tactical
    - technical
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

The build script can infer evidence/verification defaults for older `core.yaml` entries, but new contributions should set them explicitly.

## Evidence

- `official`
- `peer-reviewed`
- `preprint`
- `vendor-claim`
- `community`
- `unverified`

## Verification

- `verified`
- `provisional`
- `watchlist`
- `rejected`

## Build

```bash
pip install -r requirements.txt
python scripts/build_catalog.py --check
python scripts/build_catalog.py
```

Generated artifacts:

```text
site/data/
├── resources.json
├── resources.csv
└── stats.json
```

Do not edit generated files by hand.

## Design principle

Markdown explains **why** a resource matters. YAML records **what** the resource is. The web UI provides **how to find it**.

Keeping those jobs separate is considerably less glamorous than a 900-link README and considerably more useful.
