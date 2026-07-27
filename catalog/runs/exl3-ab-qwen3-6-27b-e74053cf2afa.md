# `exl3-ab/exllamav3-1.0.0/q4_100_single_ctx2048`

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
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 1 |
| Prompt tokens | 2048 |
| Generated tokens | 256 |
| KV cache | q8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 28.35 |
| `decode_tok_s` | 28.35 |
| `prefill_tok_s` | 685.3 |
| `ttft_p50_ms` | 2988.6 |
| `vram_peak_mib` | 14782 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-4.0bpw-mul1-v100 --mode single --ctx 2048 --gen 256 --repeats 3 --cache-size 8192 --cache-mode q8
```

## Engine knobs

```json
{
  "codebook": "mul1",
  "cuda": "12.8",
  "env": "default",
  "gen_all": [
    28.48,
    28.35,
    28.13
  ],
  "load_s": 4.4,
  "mode": "single",
  "prefill_all": [
    688.1,
    684.6,
    685.3
  ],
  "quantizer_version": "1.0.0",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/q4_100_single_ctx2048.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 4.0bpw codebook=mul1, собран exl3 1.0.0. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
