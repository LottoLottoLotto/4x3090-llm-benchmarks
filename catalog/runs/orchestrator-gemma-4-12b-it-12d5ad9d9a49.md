# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x4_spec-none_c32768_pl250_aggregate`

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
| Layout | TP=1, INSTANCES=4 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 250 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3612.3 |
| `req_s` | 14.11 |
| `ttft_p50_ms` | 412.57 |
| `ttft_p99_ms` | 534.05 |
| `itl_p50_ms` | 33.29 |
| `e2e_p99_ms` | 9515.72 |
| `vram_peak_mib` | 88320 |
| `avg_power_w` | 917.8 |
| `max_temp_c` | 77.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 5519.22,
    "errors": 0,
    "itl_p50": 20.34,
    "output_tok_s": 47.2,
    "req_s": 0.18,
    "ttft_p50": 221.94,
    "ttft_p99": 341.14
  },
  {
    "concurrency": 2,
    "e2e_p99": 5329.58,
    "errors": 0,
    "itl_p50": 20.37,
    "output_tok_s": 97.2,
    "req_s": 0.38,
    "ttft_p50": 57.24,
    "ttft_p99": 95.19
  },
  {
    "concurrency": 4,
    "e2e_p99": 5358.87,
    "errors": 0,
    "itl_p50": 20.43,
    "output_tok_s": 192.7,
    "req_s": 0.75,
    "ttft_p50": 58.24,
    "ttft_p99": 80.63
  },
  {
    "concurrency": 8,
    "e2e_p99": 5515.88,
    "errors": 0,
    "itl_p50": 20.9,
    "output_tok_s": 375.6,
    "req_s": 1.47,
    "ttft_p50": 68.94,
    "ttft_p99": 91.67
  },
  {
    "concurrency": 16,
    "e2e_p99": 5739.31,
    "errors": 0,
    "itl_p50": 21.71,
    "output_tok_s": 722.0,
    "req_s": 2.82,
    "ttft_p50": 92.46,
    "ttft_p99": 114.03
  },
  {
    "concurrency": 32,
    "e2e_p99": 6387.24,
    "errors": 0,
    "itl_p50": 23.42,
    "output_tok_s": 1325.6,
    "req_s": 5.18,
    "ttft_p50": 144.08,
    "ttft_p99": 368.14
  },
  {
    "concurrency": 64,
    "e2e_p99": 7505.33,
    "errors": 0,
    "itl_p50": 27.35,
    "output_tok_s": 2240.2,
    "req_s": 8.75,
    "ttft_p50": 231.28,
    "ttft_p99": 285.73
  },
  {
    "concurrency": 96,
    "e2e_p99": 8590.96,
    "errors": 0,
    "itl_p50": 30.77,
    "output_tok_s": 2955.7,
    "req_s": 11.55,
    "ttft_p50": 299.58,
    "ttft_p99": 378.77
  },
  {
    "concurrency": 128,
    "e2e_p99": 9515.72,
    "errors": 0,
    "itl_p50": 33.29,
    "output_tok_s": 3612.3,
    "req_s": 14.11,
    "ttft_p50": 412.57,
    "ttft_p99": 534.05
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
