#!/usr/bin/env python3
"""Small command-line query helper for the public JSONL archive."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model")
    parser.add_argument("--engine")
    parser.add_argument("--quant")
    parser.add_argument("--campaign")
    parser.add_argument("--run-id")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    rows = [
        json.loads(line)
        for line in (ROOT / "data" / "benchmarks.jsonl").read_text().splitlines()
        if line.strip()
    ]
    filters = {
        "model": args.model,
        "engine": args.engine,
        "quant": args.quant,
        "source": args.campaign,
        "run_id": args.run_id,
    }
    for field, expected in filters.items():
        if expected:
            rows = [row for row in rows if str(row.get(field, "")).lower() == expected.lower()]

    for row in rows[: args.limit]:
        print(json.dumps(row, ensure_ascii=False))
    if len(rows) > args.limit:
        print(f"# {len(rows) - args.limit} more rows", file=sys.stderr)


if __name__ == "__main__":
    import sys

    main()
