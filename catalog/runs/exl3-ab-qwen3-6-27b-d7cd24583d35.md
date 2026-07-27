# `exl3-ab/llamacpp/q6k/sm-row/pp2048`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-Q6_K.gguf |
| Quant | gguf-q6_k |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | 7c082bc41 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Concurrency | 1 |
| Prompt tokens | 2048 |
| Generated tokens | 256 |
| KV cache | q8_0/q8_0 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 19.02 |
| `decode_tok_s` | 19.02 |
| `prefill_tok_s` | 150.84 |

## Launch command

```bash
llama-bench -m ${MODEL_ROOT}/Qwen3.6-27B-MTP-GGUF/Qwen3.6-27B-Q6_K.gguf -p ... -n 256 -ngl 99 -fa 1 -ctk q8_0 -ctv q8_0 -sm row -r 3
```

## Engine knobs

```json
{
  "flash_attn": 1,
  "n_gpu_layers": 99,
  "repeats": 3,
  "split_mode": "row",
  "stddev_ts": 2.144361
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/llamacpp_q6k_row.json`

## Notes

Кросс-движковый партнёр для exl3 6.0bpw: Q6_K 22.9GB против exl3 22.0GB. llama-bench меряет tg с пустого контекста, поэтому decode тут — одна величина на все prompt-длины, сравнивать корректно с exl3 на коротком ctx. -sm row на этом риге провальный (нет P2P между картами).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
