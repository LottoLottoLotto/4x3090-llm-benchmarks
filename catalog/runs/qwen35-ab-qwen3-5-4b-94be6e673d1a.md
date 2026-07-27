# `qwen35ab/qwen35-4b-ab/quant_dflash`

| field | value |
|---|---|
| Date | 2026-07-07 |
| Campaign | qwen35-ab |
| Model | Qwen3.5-4B |
| Quant | dflash-quant |
| Quant method | dflash |
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
| `output_tok_s` | 251.87 |
| `total_tok_s` | 384.2 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-024/bin/vllm' serve '${MODEL_ROOT}/qwen35-4b-w4a16' --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.88 --port 18000 --served-model-name bench --host 127.0.0.1 --disable-uvicorn-access-log --disable-fastapi-docs --max-num-batched-tokens 16384 --max-num-seqs 64 --spec-method dflash --spec-model '${MODEL_ROOT}/qwen35-4b-dflash' --spec-tokens 15 --speculative-config '{"attention_backend": "FLASH_ATTN"}'
```

## Quality

```json
{
  "accuracy": 0.3286,
  "by_dataset": {
    "gpqa_diamond": {
      "acc": 0.2,
      "n": 30,
      "ok": 6
    },
    "gsm8k": {
      "acc": 0.9,
      "n": 10,
      "ok": 9
    },
    "mmlu_pro": {
      "acc": 0.2667,
      "n": 30,
      "ok": 8
    }
  },
  "correct": 23,
  "errors": 0,
  "evaluated": 70,
  "total_latency_s": 114.59,
  "total_tokens": 44284
}
```

## Provenance

- `rig:~/benchmarks/qwen35-4b-ab`

## Notes

A/B dflash quant. single speedup x3.082, agg x1.391, acc Δ-0.0285.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
