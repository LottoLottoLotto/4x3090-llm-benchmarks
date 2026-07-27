# `exl3-ab/exllamav3-0.0.43/043_single_ctx32768`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-exl3-6.0bpw |
| Quant | exl3-6.0bpw-mcg |
| Quant method | exl3 |
| Engine | exllamav3 |
| Engine version | 0.0.43+cu128.torch2.8.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 40960 |
| Concurrency | 1 |
| Prompt tokens | 32768 |
| Generated tokens | 256 |
| KV cache | q8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 12.28 |
| `decode_tok_s` | 12.28 |
| `prefill_tok_s` | 680.0 |
| `ttft_p50_ms` | 48185.1 |
| `vram_peak_mib` | 21190 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-6.0bpw --mode single --ctx 32768 --gen 256 --repeats 3 --cache-size 40960 --cache-mode q8
```

## Engine knobs

```json
{
  "codebook": "mcg",
  "cuda": "12.8",
  "env": "default",
  "gen_all": [
    12.28,
    12.27,
    12.31
  ],
  "load_s": 5.0,
  "mode": "single",
  "prefill_all": [
    684.6,
    677.1,
    680.0
  ],
  "quantizer_version": "0.0.30",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/043_single_ctx32768.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 6.0bpw codebook=mcg, собран exl3 0.0.30. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
