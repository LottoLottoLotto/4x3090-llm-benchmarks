# `exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx512`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-exl3-4.0bpw-mul1-v100 |
| Quant | exl3-4.0bpw-mul1 |
| Quant method | exl3 |
| Engine | exllamav3 |
| Engine version | 1.0.0+cu128.torch2.8.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Context | 4096 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | q8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 65.7 |
| `decode_tok_s` | 65.7 |
| `prefill_tok_s` | 598.8 |
| `ttft_p50_ms` | 855.1 |
| `vram_peak_mib` | 16805 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-4.0bpw-mul1-v100 --mode tp --ctx 512 --gen 256 --repeats 3 --cache-size 4096 --cache-mode q8
```

## Engine knobs

```json
{
  "codebook": "mul1",
  "cuda": "12.8",
  "env": "default",
  "gen_all": [
    59.81,
    66.0,
    65.7
  ],
  "load_s": 31.0,
  "mode": "tp",
  "prefill_all": [
    588.3,
    613.8,
    598.8
  ],
  "quantizer_version": "1.0.0",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/q4_100_tp_ctx512.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 4.0bpw codebook=mul1, собран exl3 1.0.0. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
