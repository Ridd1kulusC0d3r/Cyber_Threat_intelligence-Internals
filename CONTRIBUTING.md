# Contributing

Contributions are welcome when they make the catalog more useful to a working CTI analyst.

## Required fields for a new resource

Every proposed resource should include:

- **Name**
- **URL**
- **Category**
- **Source class**
  - A — authoritative / standards / government / CERT
  - B — first-party vendor research
  - C — community / aggregation
- **Access model** — free, freemium, commercial, open source
- **Intelligence level** — strategic, operational, tactical, technical
- **Lifecycle status**
  - Active — maintained and suitable for current use
  - Reference — useful methodology/content, but not necessarily a deployment default
  - Legacy — historically useful but aging or effectively unmaintained
  - Archived — explicitly archived or retired
- **Last reviewed date**
- **One-line analyst use case**

## Quality rules

Prefer:

- primary sources;
- official documentation;
- maintained projects;
- original threat research;
- machine-readable data/APIs when available;
- resources with transparent provenance;
- links to the original report rather than reposts.

Avoid:

- link farms with no provenance;
- copied threat reports without attribution;
- abandoned services presented as current;
- low-signal marketing pages;
- resources whose maintenance state cannot be established;
- unsafe handling of malware or unauthorized activity.

## Lifecycle review

A GitHub repository being technically reachable does not make it active.

When reviewing a project, check:

1. archive status;
2. date of recent meaningful commits/releases;
3. issue/PR activity where relevant;
4. current documentation;
5. whether an official successor exists;
6. whether dependencies are still supported.

If a project is historically valuable but no longer maintained, keep it only when that historical/reference value is clear and label it **Legacy** or **Archived**.

## Pull request checklist

- [ ] Link resolves successfully.
- [ ] Resource is in the correct category.
- [ ] Source class is defensible.
- [ ] Intelligence level is identified.
- [ ] Lifecycle status has been checked.
- [ ] Last-reviewed date is included where practical.
- [ ] Description states an analyst use case rather than marketing copy.
- [ ] Duplicate aliases have been checked.
- [ ] Commercial resources are clearly labeled.
- [ ] Secondary reporting is not presented as an authoritative source.
- [ ] Archived/legacy projects are not presented as current production defaults.
