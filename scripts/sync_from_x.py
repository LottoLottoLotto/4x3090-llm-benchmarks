#!/usr/bin/env python3
"""Manually refresh the public archive from the working database in x."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path(
    os.environ.get("BENCH_SOURCE_DIR", ROOT.parent / "x" / "llm-bench" / "bench-db")
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args()

    exporter = args.source / "export_public.py"
    if not exporter.is_file():
        raise SystemExit(f"source exporter not found: {exporter}")

    with tempfile.TemporaryDirectory(prefix="bench-public-") as temporary:
        staged = Path(temporary) / "benchmarks.jsonl"
        subprocess.run([sys.executable, str(exporter), str(staged)], check=True)
        destination = ROOT / "data" / "benchmarks.jsonl"
        source_schema = args.source / "schema_v2.py"
        destination_schema = ROOT / "scripts" / "schema_v2.py"
        data_changed = not destination.exists() or staged.read_bytes() != destination.read_bytes()
        schema_changed = (
            source_schema.is_file()
            and (
                not destination_schema.exists()
                or source_schema.read_bytes() != destination_schema.read_bytes()
            )
        )
        if not data_changed and not schema_changed:
            print("Public data and schema already match the working database.")
            return
        if data_changed:
            staged.replace(destination)
        if schema_changed:
            shutil.copy2(source_schema, destination_schema)

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_archive.py")], check=True)
    print("Archive refreshed locally. Review git diff before committing or pushing.")


if __name__ == "__main__":
    main()
