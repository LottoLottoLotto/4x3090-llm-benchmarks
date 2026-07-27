# `ds4/baseline/decode-fine`

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
| `output_tok_s` | 36.34 |
| `decode_tok_s` | 36.34 |

## Launch command

```bash
llama-server (fused idx, no-MTP, no EP)
```

## Provenance

- `repo:ds4-profiling-writeup.md, ds4-decode-deep-research-2026-07-10.md; memory ds4-longctx-push`

## Notes

Профайлинг long-ctx на 4x3090 + кастомный P2P-драйвер 610.43.02. Не параметрический свип — замеренные прод-точки. DSV4_CONSTANT_SHAPE (пин decode-графа).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
