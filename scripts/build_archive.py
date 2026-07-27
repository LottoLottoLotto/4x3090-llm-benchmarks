#!/usr/bin/env python3
"""Validate the public JSONL and rebuild SQLite plus Markdown navigation."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from schema_v2 import FIELDS, INTEGER_FIELDS, JSON_FIELDS, REAL_FIELDS, validate_rows


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
README = ROOT / "README.md"
JSONL = DATA / "benchmarks.jsonl"
SQLITE = DATA / "benchmarks.sqlite"
SNAPSHOT = DATA / "snapshot.json"
CATALOG = ROOT / "catalog"

FORBIDDEN = re.compile(
    r"/mnt/|/home/alexey|/Users/kts|192\.168\.1\.3|"
    r"(?:Authorization:\s*Bearer|HF_TOKEN|API_KEY|sk-[A-Za-z0-9])",
    re.IGNORECASE,
)

SUMMARY_START = "<!-- archive-summary:start -->"
SUMMARY_END = "<!-- archive-summary:end -->"
STATS_START = "<!-- archive-stats:start -->"
STATS_END = "<!-- archive-stats:end -->"


def load_rows() -> list[dict[str, Any]]:
    rows = [json.loads(line) for line in JSONL.read_text().splitlines() if line.strip()]
    validate_rows(rows)
    if any(row["record_kind"] != "measurement" for row in rows):
        raise SystemExit("public archive must contain measurement rows only")
    rendered = JSONL.read_text()
    match = FORBIDDEN.search(rendered)
    if match:
        raise SystemExit(f"forbidden public value: {match.group(0)!r}")
    return rows


def sqlite_type(field: str) -> str:
    if field in INTEGER_FIELDS:
        return "INTEGER"
    if field in REAL_FIELDS:
        return "REAL"
    return "TEXT"


def sqlite_value(field: str, value: Any) -> Any:
    if value is None:
        return None
    if field in JSON_FIELDS:
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if field == "symmetric" and isinstance(value, bool):
        return int(value)
    return value


def build_sqlite(rows: list[dict[str, Any]]) -> None:
    temporary = SQLITE.with_suffix(".sqlite.tmp")
    temporary.unlink(missing_ok=True)
    connection = sqlite3.connect(temporary)
    columns = ", ".join(f'"{field}" {sqlite_type(field)}' for field in FIELDS)
    connection.execute(f"CREATE TABLE runs ({columns})")
    placeholders = ", ".join("?" for _ in FIELDS)
    connection.executemany(
        f"INSERT INTO runs VALUES ({placeholders})",
        [[sqlite_value(field, row.get(field)) for field in FIELDS] for row in rows],
    )
    connection.execute("CREATE UNIQUE INDEX runs_run_id_uq ON runs(run_id)")
    connection.execute("CREATE INDEX runs_model_idx ON runs(model)")
    connection.execute("CREATE INDEX runs_source_idx ON runs(source)")
    connection.execute("CREATE INDEX runs_quant_idx ON runs(quant)")
    connection.commit()
    result = connection.execute("PRAGMA quick_check").fetchone()[0]
    count = connection.execute("SELECT COUNT(*) FROM runs").fetchone()[0]
    connection.close()
    if result != "ok" or count != len(rows):
        temporary.unlink(missing_ok=True)
        raise SystemExit(f"SQLite validation failed: quick_check={result}, rows={count}")
    temporary.replace(SQLITE)


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "unknown"


def run_filename(row: dict[str, Any]) -> str:
    digest = hashlib.sha256(row["run_id"].encode()).hexdigest()[:12]
    return f"{slug(row.get('source') or 'run')}-{slug(row.get('model') or 'model')}-{digest}.md"


def md(value: Any) -> str:
    if value is None or value == "":
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def layout(row: dict[str, Any]) -> str:
    parts = []
    for field in ("tp", "pp", "dp", "instances"):
        value = row.get(field)
        if value not in (None, 1) or field == "tp":
            parts.append(f"{field.upper()}={value}")
    return ", ".join(parts)


def primary_metric(row: dict[str, Any]) -> str:
    candidates = (
        ("output_tok_s", "output tok/s"),
        ("decode_tok_s", "decode tok/s"),
        ("prefill_tok_s", "prefill tok/s"),
        ("total_tok_s", "total tok/s"),
        ("ttft_p50_ms", "TTFT p50 ms"),
    )
    for field, label in candidates:
        value = row.get(field)
        if value is not None:
            return f"{value:g} {label}"
    return ""


def relative_run_link(row: dict[str, Any], depth: int = 1) -> str:
    prefix = "../" * depth
    return f"[{md(row['run_id'])}]({prefix}runs/{run_filename(row)})"


def write_index_page(path: Path, title: str, rows: list[dict[str, Any]], depth: int = 1) -> None:
    lines = [
        f"# {title}",
        "",
        f"{len(rows)} measurements.",
        "",
        "| date | run | model | quant | engine | layout | ctx | conc | primary metric |",
        "|---|---|---|---|---|---|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: (item.get("date") or "", item["run_id"]), reverse=True):
        lines.append(
            "| "
            + " | ".join(
                [
                    md(row.get("date")),
                    relative_run_link(row, depth),
                    md(row.get("model")),
                    md(row.get("quant")),
                    md(f"{row.get('engine') or ''} {row.get('engine_version') or ''}".strip()),
                    md(layout(row)),
                    md(row.get("context_len")),
                    md(row.get("concurrency")),
                    md(primary_metric(row)),
                ]
            )
            + " |"
        )
    lines.extend(["", "Generated from `data/benchmarks.jsonl`. Do not edit by hand.", ""])
    path.write_text("\n".join(lines))


def command_for(row: dict[str, Any]) -> str:
    argv = row.get("launch_argv")
    if argv:
        return shlex.join(str(item) for item in argv)
    return row.get("launch_cmd") or "Command was not captured for this historical row."


def write_run_page(path: Path, row: dict[str, Any]) -> None:
    metadata = [
        ("Date", row.get("date")),
        ("Campaign", row.get("source")),
        ("Model", row.get("model")),
        ("Checkpoint", row.get("checkpoint_ref")),
        ("Quant", row.get("quant")),
        ("Quant method", row.get("quant_method")),
        ("Engine", row.get("engine")),
        ("Engine version", row.get("engine_version")),
        ("Objective", row.get("objective")),
        ("TPS kind", row.get("output_tps_kind")),
        ("Layout", layout(row)),
        ("Context", row.get("context_len")),
        ("Concurrency", row.get("concurrency")),
        ("Prompt tokens", row.get("prompt_tokens")),
        ("Generated tokens", row.get("gen_tokens")),
        ("KV cache", row.get("kv_cache_dtype")),
        ("Power limit", f"{row['power_limit_w']} W/GPU" if row.get("power_limit_w") else None),
        ("Normalization", row.get("normalization_status")),
    ]
    metrics = [
        (field, row.get(field))
        for field in (
            "output_tok_s",
            "decode_tok_s",
            "prefill_tok_s",
            "total_tok_s",
            "req_s",
            "ttft_p50_ms",
            "ttft_p99_ms",
            "itl_p50_ms",
            "tpot_p50_ms",
            "e2e_p99_ms",
            "vram_peak_mib",
            "avg_power_w",
            "max_temp_c",
        )
        if row.get(field) is not None
    ]
    lines = [
        f"# `{row['run_id']}`",
        "",
        "| field | value |",
        "|---|---|",
    ]
    lines.extend(f"| {name} | {md(value)} |" for name, value in metadata if value not in (None, ""))
    lines.extend(["", "## Metrics", "", "| metric | value |", "|---|---:|"])
    lines.extend(f"| `{field}` | {md(value)} |" for field, value in metrics)
    lines.extend(["", "## Launch command", "", "```bash", command_for(row), "```", ""])

    for field, heading in (
        ("spec_decode", "Speculative decoding"),
        ("knobs", "Engine knobs"),
        ("quality", "Quality"),
        ("curve", "Throughput curve"),
        ("samples", "Samples"),
    ):
        if row.get(field) is not None:
            lines.extend(
                [
                    f"## {heading}",
                    "",
                    "```json",
                    json.dumps(row[field], ensure_ascii=False, indent=2, sort_keys=True),
                    "```",
                    "",
                ]
            )

    refs = row.get("source_refs") or []
    lines.extend(["## Provenance", ""])
    if refs:
        lines.extend(f"- `{md(ref.get('scope'))}:{md(ref.get('path'))}`" for ref in refs)
    else:
        lines.append("No source reference was retained.")
    if row.get("notes"):
        lines.extend(["", "## Notes", "", str(row["notes"])])
    lines.extend(["", "Generated from `data/benchmarks.jsonl`. Do not edit by hand.", ""])
    path.write_text("\n".join(lines))


def clear_generated_markdown(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for path in directory.glob("*.md"):
        path.unlink()


def build_catalog(rows: list[dict[str, Any]]) -> None:
    groups: dict[str, dict[str, list[dict[str, Any]]]] = {
        "models": defaultdict(list),
        "campaigns": defaultdict(list),
        "engines": defaultdict(list),
    }
    for row in rows:
        groups["models"][row.get("model") or "unknown"].append(row)
        groups["campaigns"][row.get("source") or "unknown"].append(row)
        groups["engines"][row.get("engine") or "unknown"].append(row)

    for kind in groups:
        clear_generated_markdown(CATALOG / kind)
    clear_generated_markdown(CATALOG / "runs")

    for row in rows:
        write_run_page(CATALOG / "runs" / run_filename(row), row)

    for kind, values in groups.items():
        for name, grouped_rows in values.items():
            write_index_page(CATALOG / kind / f"{slug(name)}.md", name, grouped_rows)

    first_date = min(row["date"] for row in rows if row.get("date"))
    last_date = max(row["date"] for row in rows if row.get("date"))
    exact_launch = sum(bool(row.get("launch_argv") or row.get("launch_cmd")) for row in rows)
    inferred = sum(row.get("normalization_status") == "inferred" for row in rows)
    engine_counts = Counter(row.get("engine") or "unknown" for row in rows)

    lines = [
        "# Benchmark catalog",
        "",
        f"{len(rows)} measurements from {first_date} through {last_date}.",
        "",
        "| coverage | count |",
        "|---|---:|",
        f"| campaigns | {len(groups['campaigns'])} |",
        f"| model families | {len(groups['models'])} |",
        f"| quant categories | {len({row.get('quant') for row in rows})} |",
        f"| rows with launch argv or command | {exact_launch} |",
        f"| rows with inferred metadata | {inferred} |",
        "",
        "## Browse by model",
        "",
    ]
    for name in sorted(groups["models"]):
        lines.append(f"- [{name}](models/{slug(name)}.md) ({len(groups['models'][name])})")
    lines.extend(["", "## Browse by campaign", ""])
    for name in sorted(groups["campaigns"]):
        lines.append(f"- [{name}](campaigns/{slug(name)}.md) ({len(groups['campaigns'][name])})")
    lines.extend(["", "## Browse by engine", ""])
    for name, count in engine_counts.most_common():
        label = f"{name} ({count})"
        if name == "exllamav3":
            label += ", experimental slice"
        lines.append(f"- [{label}](engines/{slug(name)}.md)")
    lines.extend(["", "Generated from `data/benchmarks.jsonl`. Do not edit by hand.", ""])
    (CATALOG / "README.md").write_text("\n".join(lines))


def write_snapshot(rows: list[dict[str, Any]]) -> None:
    payload = {
        "schema_version": 2,
        "measurements": len(rows),
        "campaigns": len({row.get("source") for row in rows}),
        "model_families": len({row.get("model") for row in rows}),
        "engines": dict(sorted(Counter(row.get("engine") for row in rows).items())),
        "first_date": min(row["date"] for row in rows if row.get("date")),
        "last_date": max(row["date"] for row in rows if row.get("date")),
        "jsonl_sha256": hashlib.sha256(JSONL.read_bytes()).hexdigest(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    SNAPSHOT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def readme_summary(rows: list[dict[str, Any]]) -> str:
    engine_counts = Counter(row.get("engine") or "unknown" for row in rows)
    exact_launch = sum(bool(row.get("launch_argv") or row.get("launch_cmd")) for row in rows)
    models = len({row.get("model") for row in rows})
    campaigns = len({row.get("source") for row in rows})
    quants = len({row.get("quant") for row in rows})
    return "\n".join(
        [
            SUMMARY_START,
            f"The archive currently has {len(rows)} measurements from {campaigns} benchmark campaigns across",
            f"{models} model families. Most runs use vLLM. The llama.cpp set is smaller, and the {engine_counts.get('exllamav3', 0)}",
            "exllamav3 rows came from a short experiment rather than broad engine coverage.",
            "",
            "This is a benchmark archive, not a leaderboard. The harness and the variable I",
            "was testing changed between campaigns, so some rows should not be compared",
            "directly. Each row keeps its workload, topology, power limit, engine version,",
            f"source references, and launch command when available. {exact_launch} of {len(rows)} measurements",
            "retain an exact argv or command.",
            SUMMARY_END,
        ]
    )


def readme_stats(rows: list[dict[str, Any]]) -> str:
    engine_counts = Counter(row.get("engine") or "unknown" for row in rows)
    exact_launch = sum(bool(row.get("launch_argv") or row.get("launch_cmd")) for row in rows)
    return "\n".join(
        [
            STATS_START,
            "| Coverage | Count |",
            "|---|---:|",
            f"| Measurements | {len(rows)} |",
            f"| Benchmark campaigns | {len({row.get('source') for row in rows})} |",
            f"| Model families | {len({row.get('model') for row in rows})} |",
            f"| Quantization categories | {len({row.get('quant') for row in rows})} |",
            f"| vLLM rows | {engine_counts.get('vllm', 0)} |",
            f"| llama.cpp rows | {engine_counts.get('llama.cpp', 0)} |",
            f"| exllamav3 experimental rows | {engine_counts.get('exllamav3', 0)} |",
            f"| Exact launch argv or command | {exact_launch} |",
            STATS_END,
        ]
    )


def update_readme(rows: list[dict[str, Any]]) -> None:
    current = README.read_text()
    summary_pattern = re.compile(
        re.escape(SUMMARY_START) + r".*?" + re.escape(SUMMARY_END),
        re.DOTALL,
    )
    stats_pattern = re.compile(
        re.escape(STATS_START) + r".*?" + re.escape(STATS_END),
        re.DOTALL,
    )
    if not summary_pattern.search(current):
        raise SystemExit("README archive summary markers are missing")
    if not stats_pattern.search(current):
        raise SystemExit("README archive stats markers are missing")
    current = summary_pattern.sub(readme_summary(rows), current)
    README.write_text(stats_pattern.sub(readme_stats(rows), current))


def verify(rows: list[dict[str, Any]]) -> None:
    connection = sqlite3.connect(SQLITE)
    count = connection.execute("SELECT COUNT(*) FROM runs").fetchone()[0]
    unique = connection.execute("SELECT COUNT(DISTINCT run_id) FROM runs").fetchone()[0]
    quick_check = connection.execute("PRAGMA quick_check").fetchone()[0]
    connection.close()
    run_pages = len(list((CATALOG / "runs").glob("*.md")))
    if (count, unique, run_pages, quick_check) != (len(rows), len(rows), len(rows), "ok"):
        raise SystemExit(
            f"archive parity failed: jsonl={len(rows)}, sqlite={count}/{unique}, "
            f"run_pages={run_pages}, quick_check={quick_check}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate current derived artifacts")
    args = parser.parse_args()
    rows = load_rows()
    if not args.check:
        build_sqlite(rows)
        build_catalog(rows)
        write_snapshot(rows)
        update_readme(rows)
    verify(rows)
    print(
        json.dumps(
            {
                "measurements": len(rows),
                "campaigns": len({row.get("source") for row in rows}),
                "models": len({row.get("model") for row in rows}),
                "run_pages": len(list((CATALOG / "runs").glob("*.md"))),
                "sqlite": "ok",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
