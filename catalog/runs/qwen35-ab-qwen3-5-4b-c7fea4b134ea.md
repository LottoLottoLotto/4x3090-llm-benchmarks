# `qwen35ab/qwen35-4b-ab-020/quant_dflash`

| field | value |
|---|---|
| Date | 2026-07-07 |
| Campaign | qwen35-ab |
| Model | Qwen3.5-4B |
| Quant | dflash-quant |
| Quant method | dflash |
| Engine | vllm |
| Engine version | 0.20 |
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
| `output_tok_s` | 257.23 |
| `total_tok_s` | 356.56 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-020/bin/vllm' serve '${MODEL_ROOT}/qwen35-4b-w4a16' --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.88 --port 18000 --served-model-name bench --host 127.0.0.1 --no-enable-log-requests --disable-log-stats --language-model-only --max-num-batched-tokens 12288 --max-num-seqs 64 --speculative-config '{"method": "dflash", "model": "${MODEL_ROOT}/qwen35-4b-dflash", "num_speculative_tokens": 15}'
```

## Quality

```json
{
  "accuracy": 0.4,
  "by_dataset": {
    "gpqa_diamond": {
      "acc": 0.3333,
      "n": 30,
      "ok": 10
    },
    "gsm8k": {
      "acc": 0.9,
      "n": 10,
      "ok": 9
    },
    "mmlu_pro": {
      "acc": 0.3,
      "n": 30,
      "ok": 9
    }
  },
  "correct": 28,
  "errors": 0,
  "evaluated": 70,
  "total_latency_s": 117.64,
  "total_tokens": 44776
}
```

## Provenance

- `rig:~/benchmarks/qwen35-4b-ab-020`

## Notes

A/B dflash quant. single speedup x3.124, agg x1.275, acc Δ0.0143.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
