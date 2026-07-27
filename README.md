# 4x3090 LLM benchmarks

I run local models on a 4x RTX 3090 rig and keep the speed measurements here.

<!-- archive-summary:start -->
The archive currently has 638 measurements from 20 benchmark campaigns across
14 model families. Most runs use vLLM. The llama.cpp set is smaller, and the 38
exllamav3 rows came from a short experiment rather than broad engine coverage.

This is a benchmark archive, not a leaderboard. The harness and the variable I
was testing changed between campaigns, so some rows should not be compared
directly. Each row keeps its workload, topology, power limit, engine version,
source references, and launch command when available. 637 of 638 measurements
retain an exact argv or command.
<!-- archive-summary:end -->

## Start here

| I want to | Open |
|---|---|
| Browse models, campaigns, and engines | [Benchmark catalog](catalog/README.md) |
| Inspect every field and exact command for one run | Follow a run link from the catalog |
| Query the complete dataset | [Querying the archive](QUERYING.md) |
| Understand what can be compared | [Methodology and limitations](METHODOLOGY.md) |
| Check the physical rig | [Hardware](HARDWARE.md) |

## Snapshot

<!-- archive-stats:start -->
| Coverage | Count |
|---|---:|
| Measurements | 638 |
| Benchmark campaigns | 20 |
| Model families | 14 |
| Quantization categories | 23 |
| vLLM rows | 531 |
| llama.cpp rows | 69 |
| exllamav3 experimental rows | 38 |
| Exact launch argv or command | 637 |
<!-- archive-stats:end -->

The dataset covers single-request decode, saturated aggregate throughput,
context-depth curves, KV-cache formats, quantization comparisons, speculative
decoding, and a few engine or version checks. Coverage varies by campaign.

## Data files

- [`data/benchmarks.jsonl`](data/benchmarks.jsonl) is the public source of truth.
- [`data/benchmarks.sqlite`](data/benchmarks.sqlite) contains the same 638 rows
  in the `runs` table.
- [`data/snapshot.json`](data/snapshot.json) records counts, date range, and the
  SHA256 of the JSONL snapshot.
- [`catalog/`](catalog/README.md) is generated from the JSONL. It includes one
  page per run, with the launch command and retained provenance.

Local paths are replaced with variables such as `${MODEL_ROOT}` and
`${ENGINE_ROOT}` before publication. The public SQLite file is rebuilt from the
sanitized JSONL. It is not copied from my working database.

## Quick query

```bash
sqlite3 -header -column data/benchmarks.sqlite '
  SELECT model, quant, engine, tp, context_len, output_tok_s
  FROM runs
  WHERE model = "Qwen3.6-27B"
    AND output_tps_kind = "single_stream_wall"
  ORDER BY output_tok_s DESC;
'
```

Or use the small JSONL helper:

```bash
python3 scripts/query.py --model Qwen3.5-122B
```

## Related work

- [club-3090 discussion #798](https://github.com/noonghunna/club-3090/discussions/798)
  is where I offered matched slices from this archive.
- [club-3090 discussion #773](https://github.com/noonghunna/club-3090/discussions/773)
  contains the 4-card TP, P2P, power, KV-depth, and custom all-reduce work.
- [laguna-dflash-4x3090](https://github.com/alesha-pro/laguna-dflash-4x3090)
  contains full raw traces for one of the larger campaigns.

Updates are manual. A new snapshot is imported, reviewed, committed, and pushed
only when I choose to publish it.
