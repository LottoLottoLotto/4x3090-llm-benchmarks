# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp4x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12B-it-FP8-Dynamic |
| Quant | fp8-dynamic |
| Quant method | fp8 |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 96 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 892.1 |
| `req_s` | 3.61 |
| `ttft_p50_ms` | 1008.43 |
| `ttft_p99_ms` | 1729.23 |
| `itl_p50_ms` | 98.9 |
| `e2e_p99_ms` | 27741.24 |
| `vram_peak_mib` | 89680 |
| `avg_power_w` | 864.1 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
```

## Engine knobs

```json
{
  "_env_VLLM_ATTENTION_BACKEND": "FLASH_ATTN",
  "_env_VLLM_USE_FLASHINFER_SAMPLER": "0",
  "enable_chunked_prefill": true,
  "enforce_eager": false,
  "gpu_memory_utilization": 0.9,
  "kv_cache_dtype": "auto",
  "max_num_seqs": 256,
  "trust_remote_code": true
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 3251.03,
    "errors": 0,
    "itl_p50": 11.16,
    "output_tok_s": 87.3,
    "req_s": 0.34,
    "ttft_p50": 44.52,
    "ttft_p99": 398.1
  },
  {
    "concurrency": 2,
    "e2e_p99": 3231.73,
    "errors": 0,
    "itl_p50": 11.93,
    "output_tok_s": 162.1,
    "req_s": 0.63,
    "ttft_p50": 74.52,
    "ttft_p99": 91.57
  },
  {
    "concurrency": 4,
    "e2e_p99": 3998.51,
    "errors": 0,
    "itl_p50": 14.46,
    "output_tok_s": 256.8,
    "req_s": 1.02,
    "ttft_p50": 78.3,
    "ttft_p99": 203.8
  },
  {
    "concurrency": 8,
    "e2e_p99": 5536.36,
    "errors": 0,
    "itl_p50": 20.07,
    "output_tok_s": 371.8,
    "req_s": 1.48,
    "ttft_p50": 137.11,
    "ttft_p99": 209.12
  },
  {
    "concurrency": 16,
    "e2e_p99": 8567.64,
    "errors": 0,
    "itl_p50": 31.12,
    "output_tok_s": 464.5,
    "req_s": 1.89,
    "ttft_p50": 256.68,
    "ttft_p99": 368.71
  },
  {
    "concurrency": 32,
    "e2e_p99": 11222.63,
    "errors": 0,
    "itl_p50": 40.11,
    "output_tok_s": 692.8,
    "req_s": 2.8,
    "ttft_p50": 400.47,
    "ttft_p99": 630.73
  },
  {
    "concurrency": 64,
    "e2e_p99": 18725.49,
    "errors": 0,
    "itl_p50": 67.77,
    "output_tok_s": 850.2,
    "req_s": 3.5,
    "ttft_p50": 874.23,
    "ttft_p99": 910.25
  },
  {
    "concurrency": 96,
    "e2e_p99": 27741.24,
    "errors": 0,
    "itl_p50": 98.9,
    "output_tok_s": 892.1,
    "req_s": 3.61,
    "ttft_p50": 1008.43,
    "ttft_p99": 1729.23
  },
  {
    "concurrency": 128,
    "e2e_p99": 34412.12,
    "errors": 0,
    "itl_p50": 125.21,
    "output_tok_s": 869.3,
    "req_s": 3.48,
    "ttft_p50": 873.56,
    "ttft_p99": 1829.85
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
