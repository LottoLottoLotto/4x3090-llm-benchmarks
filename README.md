# 4x RTX 3090 LLM benchmark archive

**638 local inference measurements from one 96 GB home rig. The exact launch
command is attached to 637 of them.**

Most benchmark posts give you a model name and one `tok/s` number. I kept
losing the rest: which checkpoint, which quant, which KV dtype, which TP layout,
which engine build, and whether the number meant single-stream decode or
aggregate throughput.

This repository is the database I wanted. You can inspect one result in the
[Markdown catalog](catalog/README.md), query all of them in SQLite, or take the
JSONL and run your own analysis.

## Navigation

| Open | What is there |
|---|---|
| [Models](catalog/README.md#browse-by-model) | All 14 model families and their runs |
| [Benchmark campaigns](catalog/README.md#browse-by-campaign) | Matched experiments and test matrices |
| [Engines](catalog/README.md#browse-by-engine) | vLLM, llama.cpp, and the experimental exllamav3 slice |
| [Query guide](QUERYING.md) | Ready-to-run SQLite, JSONL, and Python examples |
| [Methodology](METHODOLOGY.md) | Metric definitions, comparison rules, and limitations |
| [Hardware](HARDWARE.md) | The 4x RTX 3090 rig, topology, power limits, and software versions |
| [Dataset files](data/README.md) | JSONL, SQLite, snapshot metadata, and schema notes |

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

## What makes one row useful

Every result keeps the context needed to understand or reproduce it:

| Recorded with the number | Examples |
|---|---|
| Model artifact | checkpoint, quantization recipe, source revision |
| Runtime | engine, version, attention backend, KV-cache dtype |
| GPU layout | TP, PP, DP, instance count, power limit, P2P state |
| Workload | prompt length, output length, concurrency, context limit |
| Metric meaning | single-stream wall rate, decode rate, aggregate output, TTFT |
| Receipt | exact argv or shell command, source artifact, normalization status |

AutoRound INT4, AWQ INT4, Laguna's official symmetric INT4, and asymmetric
W4A16 RTN are separate categories. They are not collapsed into a generic
"INT4" bucket.

## A few places worth opening first

- [Qwen3.5-122B quant comparison](catalog/campaigns/qwen122b.md): the AutoRound
  INT4 code run reached 110.5 tok/s against 92.7 tok/s for AWQ INT4 on the same
  TP4, 220 W setup. That is a 19.2% difference, with both commands preserved.
- [Qwen3.6-27B TP and P2P matrix](catalog/campaigns/tp-ab-p2p.md): TP4 won the
  matched single-stream AutoRound run, 69.26 versus 53.8 tok/s. At concurrency
  64, TP2 produced 473.1 aggregate tok/s versus 294.76 for TP4. The fastest
  layout depends on the workload.
- [KV-cache sweep](catalog/campaigns/kv-sweep.md): 55 runs across context depth
  and KV formats, with separate metric semantics instead of one mixed ranking.
- [Laguna S 2.1 DFlash matrix](catalog/campaigns/laguna-dflash.md): target-only,
  K7, and K15 measurements across short prompts, long context, prefix reuse,
  and concurrency.

Those are examples, not global winners. Use rows from the same campaign when
calculating ratios.

## Query it in 20 seconds

The SQLite file contains the same 638 rows as the public JSONL:

```bash
git clone https://github.com/alesha-pro/4x3090-llm-benchmarks.git
cd 4x3090-llm-benchmarks

sqlite3 -header -column data/benchmarks.sqlite '
  SELECT model, quant, engine, tp, context_len, output_tok_s
  FROM runs
  WHERE model = "Qwen3.6-27B"
    AND output_tps_kind = "single_stream_wall"
  ORDER BY output_tok_s DESC;
'
```

Or use the JSONL helper:

```bash
python3 scripts/query.py --model Qwen3.5-122B
python3 scripts/query.py --engine llama.cpp --limit 10
python3 scripts/query.py --campaign tp-ab-p2p
```

More examples are in [QUERYING.md](QUERYING.md).

## Prepare a LocalMaxxing import

The dependency-free importer converts archive rows into LocalMaxxing payloads,
reports unresolved model aliases, validates through either `localmaxxing-cli`
or the authenticated API, and resumes explicitly authorized submissions from
append-only receipts.

After authenticating with `lmx`, the reviewed archive has a guarded one-command
upload for a LocalMaxxing Pro account:

```bash
./upload-localmaxxing --allow-aggregate-submit
```

The acknowledgement is required because this archive contains aggregate-
throughput measurements as well as single-stream results. This command is
intentionally a public-write operation. It loads the reviewed `model-map.json`,
includes throughput-only partial rows, excludes unknown semantics and unresolved
artifacts, production-dry-runs every ready payload, and only then begins paced
submission. It reads the API key from `LMX_API_KEY` or the LocalMaxxing CLI
config, writes durable receipts under `.localmaxxing-import/`, and resumes
safely when run again.

Planning is offline and is the safe default. Candidate resolution performs only
public `GET` searches against the LocalMaxxing catalog and Hugging Face; it
never chooses a repository automatically:

```bash
python3 scripts/import_localmaxxing.py plan --model-map model-map.json
python3 scripts/import_localmaxxing.py resolve-models --model-map model-map.json
# model-map.json contains source-verified mappings. Review model-candidates.json
# and add only repositories known to contain the exact measured artifact.
python3 scripts/import_localmaxxing.py validate-local --model-map model-map.json
```

Map the checkpoint artifact, not merely its base model. For example, a GGUF,
AWQ, FP8, or AutoRound local alias should point to the repository containing
that exact artifact. Mapping precedence is exact run ID, checkpoint reference,
model variant, then model family. A family mapping is used only when the row has
no checkpoint or variant alias, so it cannot silently relabel a quantized artifact.

Authenticated API validation does not publish:

```bash
python3 scripts/import_localmaxxing.py dry-run --model-map model-map.json
```

The importer accepts `exllamav3`. LocalMaxxing's production API engine enum and
generated OpenAPI/agent context must also include `exllamav3` before its rows
will pass authenticated dry-run validation.

Rows that contain output throughput but lack TTFT, prefill throughput, total
throughput, and VRAM are excluded by default. Opt them in explicitly with
`--allow-partial-metrics`; the generated payload contains `tokSOut` and omits
the unavailable metrics. This does not opt unknown metric semantics into the
import.

Use `--transport api` with `LMX_API_KEY` to bypass the CLI. Public submission is
available as the separate `submit` action, but it refuses to run without an
exact pending-row count and explicit acknowledgement of aggregate-throughput
rows. The archive-specific `upload` action requires the same aggregate
acknowledgement.

LocalMaxxing Pro accounts have a rolling-hour limit of 300 benchmark
submissions. The archive uploader therefore spaces submissions 13 seconds
apart; other submission commands retain the conservative free-account default
of 121 seconds. Both paths honor `Retry-After` on HTTP 429 responses and default
each CLI or API call to a 60-second client timeout. Override only the client
deadline with `--request-timeout-seconds`; it does not change submission pacing.
Because the API does not document idempotency, a submit timeout is recorded as
`ambiguous`. Later submit runs stop until the operator confirms the run was not
created remotely and explicitly passes `--retry-ambiguous`; dry-run timeouts
remain ordinary, safe-to-repeat errors.

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

The rig is 4x RTX 3090 on PCIe 3.0 x16, with 96 GB of VRAM and no NVLink.
CUDA P2P is enabled and verified through transfers on all 12 directed GPU
pairs. Most runs use a 220 W power limit per card. See [HARDWARE.md](HARDWARE.md)
for the CPU, driver, CUDA, and per-card limits.

## Repository map

| Path | Contents |
|---|---|
| [`data/benchmarks.jsonl`](data/benchmarks.jsonl) | Public source of truth |
| [`data/benchmarks.sqlite`](data/benchmarks.sqlite) | The same rows in a queryable `runs` table |
| [`catalog/`](catalog/README.md) | Models, campaigns, engines, and one page per run |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Comparison rules, metric meanings, and limitations |
| [`scripts/query.py`](scripts/query.py) | Small dependency-free JSONL query helper |
| [`scripts/import_localmaxxing.py`](scripts/import_localmaxxing.py) | Plan, validate, and explicitly submit resumable LocalMaxxing imports |

Local paths are replaced with `${MODEL_ROOT}`, `${ENGINE_ROOT}`, and similar
variables before publication. The public SQLite file is rebuilt from the
sanitized JSONL rather than copied from the working database.

## Related work

- [club-3090 discussion #798](https://github.com/noonghunna/club-3090/discussions/798)
  is where I offered matched slices from this archive.
- [club-3090 discussion #773](https://github.com/noonghunna/club-3090/discussions/773)
  covers the TP, P2P, power, KV-depth, and custom all-reduce investigation.
- [laguna-dflash-4x3090](https://github.com/alesha-pro/laguna-dflash-4x3090)
  contains full raw traces for one of the larger campaigns.

Updates are manual. I import a new snapshot, review the diff, and publish it
when the data is ready.
