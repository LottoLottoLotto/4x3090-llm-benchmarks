# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x4_spec-none_c32768_pl270_aggregate`

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
| Power limit | 270 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3725.0 |
| `req_s` | 14.55 |
| `ttft_p50_ms` | 342.05 |
| `ttft_p99_ms` | 455.34 |
| `itl_p50_ms` | 32.25 |
| `e2e_p99_ms` | 9076.21 |
| `vram_peak_mib` | 88320 |
| `avg_power_w` | 981.6 |
| `max_temp_c` | 78.0 |

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
    "e2e_p99": 5407.8,
    "errors": 0,
    "itl_p50": 20.03,
    "output_tok_s": 48.1,
    "req_s": 0.19,
    "ttft_p50": 224.61,
    "ttft_p99": 329.77
  },
  {
    "concurrency": 2,
    "e2e_p99": 5237.86,
    "errors": 0,
    "itl_p50": 20.08,
    "output_tok_s": 98.5,
    "req_s": 0.38,
    "ttft_p50": 58.0,
    "ttft_p99": 85.31
  },
  {
    "concurrency": 4,
    "e2e_p99": 5256.58,
    "errors": 0,
    "itl_p50": 20.1,
    "output_tok_s": 196.1,
    "req_s": 0.77,
    "ttft_p50": 57.1,
    "ttft_p99": 72.94
  },
  {
    "concurrency": 8,
    "e2e_p99": 5415.15,
    "errors": 0,
    "itl_p50": 20.47,
    "output_tok_s": 384.7,
    "req_s": 1.5,
    "ttft_p50": 66.66,
    "ttft_p99": 87.29
  },
  {
    "concurrency": 16,
    "e2e_p99": 5679.3,
    "errors": 0,
    "itl_p50": 21.28,
    "output_tok_s": 735.6,
    "req_s": 2.87,
    "ttft_p50": 91.28,
    "ttft_p99": 111.28
  },
  {
    "concurrency": 32,
    "e2e_p99": 6446.8,
    "errors": 0,
    "itl_p50": 22.95,
    "output_tok_s": 1193.8,
    "req_s": 4.66,
    "ttft_p50": 146.47,
    "ttft_p99": 458.96
  },
  {
    "concurrency": 64,
    "e2e_p99": 7150.24,
    "errors": 0,
    "itl_p50": 26.58,
    "output_tok_s": 2331.1,
    "req_s": 9.11,
    "ttft_p50": 213.15,
    "ttft_p99": 264.4
  },
  {
    "concurrency": 96,
    "e2e_p99": 8157.2,
    "errors": 0,
    "itl_p50": 29.69,
    "output_tok_s": 3075.7,
    "req_s": 12.01,
    "ttft_p50": 293.73,
    "ttft_p99": 362.06
  },
  {
    "concurrency": 128,
    "e2e_p99": 9076.21,
    "errors": 0,
    "itl_p50": 32.25,
    "output_tok_s": 3725.0,
    "req_s": 14.55,
    "ttft_p50": 342.05,
    "ttft_p99": 455.34
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
