# `ds4/EP/decode-fine`

| field | value |
|---|---|
| Date | 2026-07-10 |
| Campaign | ds4-profiling |
| Model | DeepSeek-V4-Flash |
| Quant | gguf-custom |
| Quant method | gguf |
| Engine | llama.cpp |
| Objective | decode |
| TPS kind | unknown |
| Layout | TP=4 |
| Context | 512 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 23.82 |
| `decode_tok_s` | 23.82 |

## Launch command

```bash
llama-server DSV4_EXPERT_PARALLEL=1
```

## Provenance

- `repo:ds4-profiling-writeup.md, ds4-decode-deep-research-2026-07-10.md; memory ds4-longctx-push`

## Notes

Профайлинг long-ctx на 4x3090 + кастомный P2P-драйвер 610.43.02. Не параметрический свип — замеренные прод-точки. DSV4_CONSTANT_SHAPE (пин decode-графа). EP-decode 36.34→23.82 (-34%, host-оркестрация не NCCL; nsys).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
