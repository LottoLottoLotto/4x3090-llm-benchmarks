# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x4_spec-none_c32768_pl220_aggregate`

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
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3063.7 |
| `req_s` | 11.97 |
| `ttft_p50_ms` | 428.66 |
| `ttft_p99_ms` | 486.12 |
| `itl_p50_ms` | 38.42 |
| `e2e_p99_ms` | 11627.33 |
| `vram_peak_mib` | 88320 |
| `avg_power_w` | 814.1 |
| `max_temp_c` | 74.0 |

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
    "e2e_p99": 6616.41,
    "errors": 0,
    "itl_p50": 23.58,
    "output_tok_s": 40.4,
    "req_s": 0.16,
    "ttft_p50": 343.31,
    "ttft_p99": 374.73
  },
  {
    "concurrency": 2,
    "e2e_p99": 6442.28,
    "errors": 0,
    "itl_p50": 23.73,
    "output_tok_s": 82.7,
    "req_s": 0.32,
    "ttft_p50": 58.22,
    "ttft_p99": 97.82
  },
  {
    "concurrency": 4,
    "e2e_p99": 6511.52,
    "errors": 0,
    "itl_p50": 23.92,
    "output_tok_s": 163.9,
    "req_s": 0.64,
    "ttft_p50": 60.92,
    "ttft_p99": 91.19
  },
  {
    "concurrency": 8,
    "e2e_p99": 6608.48,
    "errors": 0,
    "itl_p50": 24.22,
    "output_tok_s": 320.7,
    "req_s": 1.25,
    "ttft_p50": 76.47,
    "ttft_p99": 100.97
  },
  {
    "concurrency": 16,
    "e2e_p99": 6855.47,
    "errors": 0,
    "itl_p50": 24.93,
    "output_tok_s": 619.0,
    "req_s": 2.42,
    "ttft_p50": 108.79,
    "ttft_p99": 143.54
  },
  {
    "concurrency": 32,
    "e2e_p99": 7725.52,
    "errors": 0,
    "itl_p50": 26.69,
    "output_tok_s": 1148.5,
    "req_s": 4.49,
    "ttft_p50": 159.5,
    "ttft_p99": 458.75
  },
  {
    "concurrency": 64,
    "e2e_p99": 8977.65,
    "errors": 0,
    "itl_p50": 31.25,
    "output_tok_s": 1935.5,
    "req_s": 7.56,
    "ttft_p50": 271.25,
    "ttft_p99": 444.66
  },
  {
    "concurrency": 96,
    "e2e_p99": 10600.15,
    "errors": 0,
    "itl_p50": 35.83,
    "output_tok_s": 2508.1,
    "req_s": 9.8,
    "ttft_p50": 333.53,
    "ttft_p99": 445.93
  },
  {
    "concurrency": 128,
    "e2e_p99": 11627.33,
    "errors": 0,
    "itl_p50": 38.42,
    "output_tok_s": 3063.7,
    "req_s": 11.97,
    "ttft_p50": 428.66,
    "ttft_p99": 486.12
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
