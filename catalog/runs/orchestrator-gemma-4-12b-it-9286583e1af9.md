# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=1 |
| Context | 32768 |
| Concurrency | 64 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1043.5 |
| `req_s` | 4.08 |
| `ttft_p50_ms` | 628.41 |
| `ttft_p99_ms` | 724.38 |
| `itl_p50_ms` | 59.42 |
| `e2e_p99_ms` | 15805.99 |
| `vram_peak_mib` | 88240 |
| `avg_power_w` | 302.6 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 6572.51,
    "errors": 0,
    "itl_p50": 24.49,
    "output_tok_s": 39.7,
    "req_s": 0.16,
    "ttft_p50": 62.24,
    "ttft_p99": 260.54
  },
  {
    "concurrency": 2,
    "e2e_p99": 6516.38,
    "errors": 0,
    "itl_p50": 24.28,
    "output_tok_s": 79.5,
    "req_s": 0.31,
    "ttft_p50": 71.21,
    "ttft_p99": 92.37
  },
  {
    "concurrency": 4,
    "e2e_p99": 6733.59,
    "errors": 0,
    "itl_p50": 24.95,
    "output_tok_s": 154.2,
    "req_s": 0.6,
    "ttft_p50": 107.33,
    "ttft_p99": 244.43
  },
  {
    "concurrency": 8,
    "e2e_p99": 7120.22,
    "errors": 0,
    "itl_p50": 26.89,
    "output_tok_s": 288.5,
    "req_s": 1.13,
    "ttft_p50": 153.75,
    "ttft_p99": 168.18
  },
  {
    "concurrency": 16,
    "e2e_p99": 8616.55,
    "errors": 0,
    "itl_p50": 31.48,
    "output_tok_s": 488.0,
    "req_s": 1.91,
    "ttft_p50": 240.16,
    "ttft_p99": 522.92
  },
  {
    "concurrency": 32,
    "e2e_p99": 10310.31,
    "errors": 0,
    "itl_p50": 38.85,
    "output_tok_s": 799.0,
    "req_s": 3.12,
    "ttft_p50": 363.08,
    "ttft_p99": 445.8
  },
  {
    "concurrency": 64,
    "e2e_p99": 15805.99,
    "errors": 0,
    "itl_p50": 59.42,
    "output_tok_s": 1043.5,
    "req_s": 4.08,
    "ttft_p50": 628.41,
    "ttft_p99": 724.38
  },
  {
    "concurrency": 96,
    "e2e_p99": 31214.98,
    "errors": 0,
    "itl_p50": 92.08,
    "output_tok_s": 908.1,
    "req_s": 3.55,
    "ttft_p50": 1170.48,
    "ttft_p99": 1300.38
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
