# `qwen35ab/qwen35-4b-ab/base_bf16`

| field | value |
|---|---|
| Date | 2026-07-07 |
| Campaign | qwen35-ab |
| Model | Qwen3.5-4B |
| Quant | bf16 |
| Quant method | none |
| Engine | vllm |
| Engine version | 0.19 |
| Objective | single_stream+aggregate |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 32768 |
| Concurrency | 4 |
| Generated tokens | 512 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 75.98 |
| `total_tok_s` | 276.22 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-024/bin/vllm' serve '${MODEL_ROOT}/qwen35-4b-base' --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.88 --port 18000 --served-model-name bench --host 127.0.0.1 --disable-uvicorn-access-log --disable-fastapi-docs --max-num-batched-tokens 16384 --max-num-seqs 64
```

## Quality

```json
{
  "accuracy": 0.3571,
  "by_dataset": {
    "gpqa_diamond": {
      "acc": 0.3,
      "n": 30,
      "ok": 9
    },
    "gsm8k": {
      "acc": 0.9,
      "n": 10,
      "ok": 9
    },
    "mmlu_pro": {
      "acc": 0.2333,
      "n": 30,
      "ok": 7
    }
  },
  "correct": 25,
  "errors": 0,
  "evaluated": 70,
  "total_latency_s": 438.38,
  "total_tokens": 32886
}
```

## Provenance

- `rig:~/benchmarks/qwen35-4b-ab`

## Notes

A/B dflash quant. single speedup x3.082, agg x1.391, acc Δ-0.0285.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
