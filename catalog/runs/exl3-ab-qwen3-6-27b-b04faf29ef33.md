# `exl3-ab/exllamav3-1.0.0/100fa2_tp_ctx8192`

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
| Layout | TP=4 |
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
| `output_tok_s` | 47.75 |
| `decode_tok_s` | 47.75 |
| `prefill_tok_s` | 720.1 |
| `ttft_p50_ms` | 11376.1 |
| `vram_peak_mib` | 23887 |

## Launch command

```bash
python exl3_bench.py --model ${MODEL_ROOT}/Qwen3.6-27B-exl3-6.0bpw --mode tp --ctx 8192 --gen 256 --repeats 3 --cache-size 16384 --cache-mode q8   [env: EXL3_PREFER_FA2=1]
```

## Engine knobs

```json
{
  "codebook": "mcg",
  "cuda": "12.8",
  "env": "EXL3_PREFER_FA2=1",
  "gen_all": [
    47.86,
    47.48,
    47.75
  ],
  "load_s": 33.5,
  "mode": "tp",
  "prefill_all": [
    720.1,
    722.3,
    714.4
  ],
  "quantizer_version": "0.0.30",
  "repeats": 3,
  "torch": "2.8.0+cu128"
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/100fa2_tp_ctx8192.json`

## Notes

A/B exllamav3 1.0.0 vs 0.0.43, единственная переменная — версия движка (venv-копия, тот же torch 2.8.0+cu128/py3.12). Методика: prefill=ctx/TTFT, gen=(n-1)/(total-TTFT), greedy, медиана 3 повторов после warmup. Квант: 6.0bpw codebook=mcg, собран exl3 0.0.30. ГЛАВНОЕ: INT8 GEMV мёртв на 6bpw by design (use_mgemm: K>=6 -> fused). prefill-регрессию 1.0.0 на длинном ctx лечит EXL3_QC_ATTN=0. Разбор: posts/exllamav3-1.0-ab/artifacts/README.md.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
