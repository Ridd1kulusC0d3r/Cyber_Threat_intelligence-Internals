# Architecture

Cyber Threat Intelligence Internals is designed as a **data-backed CTI source directory**, not a hand-maintained wall of links.

## System model

```text
                        Human curation
                             │
                 ┌───────────▼───────────┐
                 │   catalog/*.yaml      │
                 │ source of truth       │
                 └───────────┬───────────┘
                             │
                     validate + merge
                             │
                 ┌───────────▼───────────┐
                 │ scripts/build_catalog │
                 └───────┬───────┬───────┘
                         │       │
                      JSON     CSV
                         │       │
                         └───┬───┘
                             │
                  ┌──────────▼──────────┐
                  │ GitHub Pages UI     │
                  │ search + filters    │
                  └──────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
       Analyst docs       API-ready data      Automation
       Markdown           JSON / CSV          link/freshness
```

## Repository layers

| Layer | Path | Purpose |
|---|---|---|
| Human entry point | `README.md` | Explain the project and analyst tracks |
| Knowledge guides | `docs/` | Framework comparisons, methodology and workflow |
| Structured catalog | `catalog/` | Machine-readable resources and metadata |
| Build tooling | `scripts/` | Validate and compile catalog shards |
| Web interface | `site/` | Searchable GitHub Pages directory |
| CI/CD | `.github/workflows/` | Validate links/data and publish Pages |

## Evidence model

Every catalog item should identify **what kind of evidence supports its inclusion**.

| Evidence level | Meaning |
|---|---|
| `official` | Primary standard, government, maintainer or official project source |
| `peer-reviewed` | Published peer-reviewed academic research |
| `preprint` | Public research manuscript not yet treated as peer-reviewed |
| `vendor-claim` | Product/vendor statement that is useful but should not be treated as independent validation |
| `community` | Maintained community project or collection |
| `unverified` | Mentioned or discovered but not supported well enough for the main catalog |

## Verification model

- **verified** — source located and description matches the primary/credible reference.
- **provisional** — source exists, but claims or maturity require more validation.
- **watchlist** — interesting lead; not promoted to the operational directory.
- **rejected** — false, misleading, duplicated, unsafe, or no longer useful.

## Catalog shards

```text
catalog/
├── core.yaml
├── frameworks.yaml
├── detection.yaml
├── attribution.yaml
├── ai-research.yaml
├── vendors.yaml
├── datasets.yaml
└── watchlist.yaml
```

The build script merges all files with a top-level `resources:` array.

## Resource schema

Recommended fields:

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

## Design rule

The website is a **view** of the catalog. Markdown documentation is an **analysis layer**. Neither should become a second source of truth for resource metadata.

That prevents the deeply traditional documentation failure mode where three pages disagree about whether a project is active, archived, free, commercial, or possibly undead.
