# `exl3-ab/exllamav3-1.0.0/cb_mul1_tp_ctx2048`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-exl3-6.0bpw-mul1-v100 |
| Quant | exl3-6.0bpw-mul1 |
| Quant method | exl3 |
| Engine | exllamav3 |
| Engine version | 1.0.0+cu128.torch2.8.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
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
| `output_tok_s` | 23.65 |
| `decode_tok_s` | 23.65 |
| `prefill_tok_s` | 361.5 |
| `ttft_p50_ms` | 5665.4 |
| `vram_peak_mib` | 33391 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-6.0bpw-mul1-v100 --mode tp --ctx 2048 --gen 256 --repeats 3 --cache-size 8192 --cache-mode q8
```

## Engine knobs

```json
{
  "codebook": "mul1",
  "cuda": "12.8",
  "env": "default",
  "gen_all": [
    23.65,
    23.7,
    23.53
  ],
  "load_s": 69.6,
  "mode": "tp",
  "prefill_all": [
    377.0,
    341.2,
    361.5
  ],
  "quantizer_version": "1.0.0",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/cb_mul1_tp_ctx2048.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 6.0bpw codebook=mul1, собран exl3 1.0.0. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
