# `exl3-ab/exllamav3-1.0.0/100noqc_single_ctx8192`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-exl3-6.0bpw |
| Quant | exl3-6.0bpw-mcg |
| Quant method | exl3 |
| Engine | exllamav3 |
| Engine version | 1.0.0+cu128.torch2.8.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 16384 |
| Concurrency | 1 |
| Prompt tokens | 8192 |
| Generated tokens | 256 |
| KV cache | q8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 16.94 |
| `decode_tok_s` | 16.94 |
| `prefill_tok_s` | 733.6 |
| `ttft_p50_ms` | 11167.3 |
| `vram_peak_mib` | 20824 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-6.0bpw --mode single --ctx 8192 --gen 256 --repeats 3 --cache-size 16384 --cache-mode q8   [env: EXL3_QC_ATTN=0]
```

## Engine knobs

```json
{
  "codebook": "mcg",
  "cuda": "12.8",
  "env": "EXL3_QC_ATTN=0",
  "gen_all": [
    17.06,
    16.94,
    16.9
  ],
  "load_s": 5.9,
  "mode": "single",
  "prefill_all": [
    745.0,
    733.6,
    729.0
  ],
  "quantizer_version": "0.0.30",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/100noqc_single_ctx8192.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 6.0bpw codebook=mcg, собран exl3 0.0.30. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
