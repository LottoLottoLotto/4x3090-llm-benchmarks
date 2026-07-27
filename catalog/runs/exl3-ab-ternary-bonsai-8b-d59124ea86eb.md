# `exl3-ab/llamacpp/bonsai/sm-layer/pp2048`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Ternary-Bonsai-8B |
| Checkpoint | Ternary-Bonsai-8B-F16.gguf |
| Quant | gguf-f16 |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | 7c082bc41 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Concurrency | 1 |
| Prompt tokens | 2048 |
| Generated tokens | 256 |
| KV cache | f16/f16 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 35.6 |
| `decode_tok_s` | 35.6 |
| `prefill_tok_s` | 2095.63 |

## Launch command

```bash
llama-bench -m ${MODEL_ROOT}/Ternary-Bonsai-8B-gguf/Ternary-Bonsai-8B-F16.gguf -p ... -n 256 -ngl 99 -fa 1 -ctk f16 -ctv f16 -sm layer -r 3
```

## Engine knobs

```json
{
  "flash_attn": 1,
  "n_gpu_layers": 99,
  "repeats": 3,
  "split_mode": "layer",
  "stddev_ts": 62.407047
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/llamacpp_bonsai.json`

## Notes

Ternary-Bonsai-8B F16 — тот же файл, что скормлен vLLM (arch qwen3). Соседство: рядом шло квантование, числа предварительные.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
