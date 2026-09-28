# Machine-readable catalog

The `catalog/core.yaml` file is the structured seed for the repository.

Its purpose is to make the collection reusable by:

- GitHub Pages;
- static-site generators;
- search/filter interfaces;
- CTI dashboards;
- automated freshness checks;
- exports to JSON/CSV;
- future scoring and tagging pipelines.

## Fields

```yaml
name:
url:
category:
source_class:
intelligence_levels:
access:
lifecycle:
owner:
last_reviewed:
use:
tags:
```

### Lifecycle values

- `active`
- `reference`
- `legacy`
- `archived`

### Source classes

- `A` — authoritative / standards / government / CERT / primary datasets
- `B` — original vendor or research-team intelligence
- `C` — community, aggregator or analyst-maintained collection

The Markdown guides remain the human-readable layer. The YAML catalog is the automation layer.
