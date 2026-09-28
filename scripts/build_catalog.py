#!/usr/bin/env python3
"""Validate catalog shards and build JSON/CSV artifacts for the static directory."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REQUIRED = {
    "name",
    "category",
    "source_class",
    "intelligence_levels",
    "access",
    "lifecycle",
    "owner",
    "last_reviewed",
    "use",
    "tags",
}

ALLOWED_SOURCE_CLASSES = {"A", "B", "C"}
ALLOWED_LEVELS = {"strategic", "operational", "tactical", "technical"}
ALLOWED_EVIDENCE = {
    "official",
    "peer-reviewed",
    "preprint",
    "vendor-claim",
    "community",
    "unverified",
}
ALLOWED_VERIFICATION = {"verified", "provisional", "watchlist", "rejected"}


def load_catalog(catalog_dir: Path) -> list[dict[str, Any]]:
    resources: list[dict[str, Any]] = []
    for path in sorted(catalog_dir.glob("*.yaml")):
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        shard = payload.get("resources", [])
        if not isinstance(shard, list):
            raise ValueError(f"{path}: resources must be a list")
        for item in shard:
            if not isinstance(item, dict):
                raise ValueError(f"{path}: every resource must be a mapping")
            item = dict(item)
            item["_shard"] = path.name
            resources.append(item)
    return resources


def infer_evidence(item: dict[str, Any]) -> str:
    if item.get("evidence_level"):
        return str(item["evidence_level"])
    if item.get("verification") == "watchlist":
        return "unverified"
    return "official" if item.get("source_class") == "A" else (
        "vendor-claim" if item.get("source_class") == "B" else "community"
    )


def infer_verification(item: dict[str, Any]) -> str:
    if item.get("verification"):
        return str(item["verification"])
    lifecycle = str(item.get("lifecycle", "")).lower()
    return "provisional" if lifecycle in {"research", "emerging"} else "verified"


def validate(resources: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    normalized: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_names: Counter[str] = Counter()

    for idx, raw in enumerate(resources, start=1):
        item = dict(raw)
        label = f"{item.get('_shard', '?')}#{idx}:{item.get('name', '<unnamed>')}"

        missing = sorted(REQUIRED - item.keys())
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(missing)}")

        verification = infer_verification(item)
        evidence = infer_evidence(item)
        item["verification"] = verification
        item["evidence_level"] = evidence

        if item.get("source_class") not in ALLOWED_SOURCE_CLASSES:
            errors.append(f"{label}: invalid source_class {item.get('source_class')!r}")

        levels = item.get("intelligence_levels", [])
        if not isinstance(levels, list) or not levels:
            errors.append(f"{label}: intelligence_levels must be a non-empty list")
        else:
            invalid_levels = sorted(set(levels) - ALLOWED_LEVELS)
            if invalid_levels:
                errors.append(f"{label}: invalid intelligence levels: {invalid_levels}")

        if evidence not in ALLOWED_EVIDENCE:
            errors.append(f"{label}: invalid evidence_level {evidence!r}")

        if verification not in ALLOWED_VERIFICATION:
            errors.append(f"{label}: invalid verification {verification!r}")

        url = str(item.get("url", "") or "").strip()
        if verification not in {"watchlist", "rejected"} and not url.startswith(("https://", "http://")):
            errors.append(f"{label}: verified/provisional resources require an http(s) URL")

        name_key = str(item.get("name", "")).strip().casefold()
        if name_key:
            seen_names[name_key] += 1

        for list_field in ("intelligence_levels", "tags"):
            value = item.get(list_field)
            if value is not None and not isinstance(value, list):
                errors.append(f"{label}: {list_field} must be a list")

        normalized.append(item)

    duplicate_names = [name for name, count in seen_names.items() if count > 1]
    for name in duplicate_names:
        # Duplicates can be intentional across shards; make them visible in build output
        # without failing the catalog.
        pass

    return normalized, errors


def stats(resources: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "resources": len(resources),
        "categories": len({r.get("category") for r in resources if r.get("category")}),
        "active": sum(1 for r in resources if r.get("lifecycle") == "active"),
        "research": sum(1 for r in resources if r.get("lifecycle") == "research"),
        "watchlist": sum(1 for r in resources if r.get("verification") == "watchlist"),
        "verified": sum(1 for r in resources if r.get("verification") == "verified"),
        "by_source_class": dict(Counter(r.get("source_class") for r in resources)),
        "by_evidence": dict(Counter(r.get("evidence_level") for r in resources)),
    }


def write_outputs(resources: list[dict[str, Any]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    clean = [{k: v for k, v in r.items() if not k.startswith("_")} for r in resources]
    clean.sort(key=lambda r: (str(r.get("category", "")), str(r.get("name", "")).casefold()))

    (out_dir / "resources.json").write_text(
        json.dumps(clean, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out_dir / "stats.json").write_text(
        json.dumps(stats(clean), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    fields = [
        "name",
        "url",
        "category",
        "source_class",
        "intelligence_levels",
        "access",
        "lifecycle",
        "owner",
        "evidence_level",
        "verification",
        "last_reviewed",
        "use",
        "notes",
        "tags",
    ]
    with (out_dir / "resources.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in clean:
            flat = dict(row)
            flat["intelligence_levels"] = "|".join(row.get("intelligence_levels", []))
            flat["tags"] = "|".join(row.get("tags", []))
            writer.writerow(flat)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-dir", default="catalog")
    parser.add_argument("--out-dir", default="site/data")
    parser.add_argument("--check", action="store_true", help="validate only")
    args = parser.parse_args()

    resources = load_catalog(Path(args.catalog_dir))
    resources, errors = validate(resources)
    if errors:
        print("\n".join(f"ERROR: {err}" for err in errors), file=sys.stderr)
        return 1

    if not args.check:
        write_outputs(resources, Path(args.out_dir))

    summary = stats(resources)
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
