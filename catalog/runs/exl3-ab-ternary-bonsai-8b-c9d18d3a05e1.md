# `exl3-ab/vllm-gguf/vllm_gguf_bonsai_ctx2048`

| field | value |
|---|---|
| Date | 2026-07-16 |
| Campaign | exl3-ab |
| Model | Ternary-Bonsai-8B |
| Checkpoint | Ternary-Bonsai-8B-F16.gguf |
| Quant | gguf-f16 |
| Quant method | gguf |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 1 |
| Prompt tokens | 2048 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 35.98 |
| `decode_tok_s` | 35.98 |
| `prefill_tok_s` | 3688.7 |
| `ttft_p50_ms` | 555.2 |

## Launch command

```bash
vllm serve ${MODEL_ROOT}/Ternary-Bonsai-8B-gguf/Ternary-Bonsai-8B-F16.gguf --quantization gguf --served-model-name bench --port 18000 --max-model-len 8192 --gpu-memory-utilization 0.90
```

## Engine knobs

```json
{
  "flashinfer_fix": "CUDA_HOME=<venv>/nvidia/cu13 + NVCC_PREPEND_FLAGS",
  "gen_all": [
    36.41,
    35.98,
    35.7
  ],
  "prefill_all": [
    3662.2,
    3709.3,
    3688.7
  ],
  "quantization": "gguf",
  "repeats": 3
}
```

## Provenance

- `rig:~/benchmarks/exl3-ab/raw/vllm_gguf_bonsai_ctx2048.json`

## Notes

vLLM+GGUF работает ТОЛЬКО на классических архитектурах. Qwen3.5/3.6 (arch qwen35) не поддержаны transformers вообще; gemma-4 падает на per-layer num_key_value_heads. Нужен фикс FlashInfer JIT. Разбор: posts/exllamav3-1.0-ab/artifacts/vllm-gguf-findings.md. Соседство: рядом шло квантование, числа предварительные.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
