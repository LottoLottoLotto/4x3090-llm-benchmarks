# Methodology and limitations

## What one row means

One row is a measured operating point. It records the model, checkpoint,
quantization, engine, layout, context, workload, power limit, metrics, and launch
configuration that were available for that run.

The archive contains historical measurements produced by several harnesses. A
row is not automatically comparable with every other row for the same model.

## Comparison rule

Use rows from the same campaign when possible. Before calculating a ratio, match
the following fields or explain why they differ:

- checkpoint and quantization recipe;
- engine version and attention backend;
- TP, PP, DP, and independent instance count;
- prompt length, generated length, concurrency, and request content;
- KV-cache dtype and speculative-decoding settings;
- power limit and interconnect state;
- metric definition in `output_tps_kind`.

The catalog preserves rows with `output_tps_kind=unknown`, but those rows should
not enter an automatic ranking.

## Metric meanings

`output_tok_s` historically came from more than one harness. Read it together
with `objective` and `output_tps_kind`.

Common values include:

- `single_stream_wall`: generated tokens divided by end-to-end time;
- `single_stream_decode`: decode rate with TTFT removed;
- `aggregate_output`: total generated tokens per second under concurrent load;
- `unknown`: retained historical value whose exact definition was not recoverable.

The schema also has explicit fields for TTFT, ITL, TPOT, prefill rate, decode
rate, request rate, VRAM, power, and temperature. Empty values mean that the
campaign did not collect the metric.

## Normalization

The public archive uses schema version 2. Numeric measurements are copied from
the source artifacts. Normalization changes labels, structure, references, and
identifiers.

`normalization_status=exact` means the normalized metadata was directly present
in the source. `inferred` means that a label was recovered from a checkpoint,
path, run tag, or campaign context. The original value is retained in fields such
as `quant_raw` and `engine_raw`.

AutoRound INT4, AWQ INT4, the official Laguna symmetric INT4 checkpoint, and the
asymmetric W4A16 RTN checkpoint remain separate categories.

## Launch commands

637 of 638 public rows contain `launch_argv` or `launch_cmd`. Publication replaces
machine-specific roots with variables:

| Variable | Meaning |
|---|---|
| `${MODEL_ROOT}` | Primary model directory |
| `${MODEL_ROOT_ALT}` | Secondary model directory |
| `${ENGINE_ROOT}` | Primary engine directory |
| `${ENGINE_ROOT_ALT}` | Secondary engine directory |
| `${RIG_HOME}` | User home on the benchmark host |

Commands are receipts for the measured run. Flags can change between engine
versions, so check the matching version before reusing a command on a newer
installation.

## Public export

The working database is not committed here. A manual exporter removes
placeholders, rewrites local paths, scans for internal hosts and credentials, and
writes `data/benchmarks.jsonl`. SQLite and the Markdown catalog are generated
from that public JSONL.
