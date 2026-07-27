# Querying the archive

## SQLite

The `runs` table has one row per measurement.

```bash
sqlite3 -header -column data/benchmarks.sqlite '
  SELECT date, model, quant, engine, tp, context_len, output_tok_s
  FROM runs
  WHERE source = "tp-ab-p2p"
  ORDER BY date, model, quant, tp;
'
```

Show every AutoRound INT4 command:

```bash
sqlite3 data/benchmarks.sqlite '
  SELECT run_id, COALESCE(launch_cmd, launch_argv)
  FROM runs
  WHERE quant = "autoround-int4";
'
```

Keep metric semantics fixed when ranking:

```bash
sqlite3 -header -column data/benchmarks.sqlite '
  SELECT model, quant, engine, MAX(output_tok_s) AS tok_s
  FROM runs
  WHERE output_tps_kind = "single_stream_wall"
  GROUP BY model, quant, engine
  ORDER BY tok_s DESC;
'
```

## JSONL

```bash
jq -c 'select(.model == "Qwen3.5-122B")' data/benchmarks.jsonl
```

```bash
jq -r '
  select(.launch_argv != null)
  | .run_id + "\t" + (.launch_argv | join(" "))
' data/benchmarks.jsonl
```

## Python helper

The helper prints matching rows as JSONL:

```bash
python3 scripts/query.py --engine llama.cpp --limit 10
python3 scripts/query.py --campaign kv-sweep
python3 scripts/query.py --run-id 'orch/Qwen3.6-27B/...'
```

For visual browsing, start with [`catalog/README.md`](catalog/README.md).
