# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x4_spec-ngram_c32768_pl220_aggregate`

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
| `output_tok_s` | 2419.9 |
| `req_s` | 9.45 |
| `ttft_p50_ms` | 280.26 |
| `ttft_p99_ms` | 516.46 |
| `itl_p50_ms` | 44.55 |
| `e2e_p99_ms` | 15086.13 |
| `vram_peak_mib` | 88352 |
| `avg_power_w` | 793.5 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill --speculative-config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 4, "prompt_lookup_min": 2}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": null,
  "method": "ngram"
}
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
    "e2e_p99": 7850.7,
    "errors": 0,
    "itl_p50": 23.55,
    "output_tok_s": 36.1,
    "req_s": 0.14,
    "ttft_p50": 1543.9,
    "ttft_p99": 1575.44
  },
  {
    "concurrency": 2,
    "e2e_p99": 6291.8,
    "errors": 0,
    "itl_p50": 23.68,
    "output_tok_s": 84.5,
    "req_s": 0.33,
    "ttft_p50": 39.8,
    "ttft_p99": 100.62
  },
  {
    "concurrency": 4,
    "e2e_p99": 8454.95,
    "errors": 0,
    "itl_p50": 23.82,
    "output_tok_s": 156.6,
    "req_s": 0.61,
    "ttft_p50": 40.99,
    "ttft_p99": 81.75
  },
  {
    "concurrency": 8,
    "e2e_p99": 6634.89,
    "errors": 0,
    "itl_p50": 24.65,
    "output_tok_s": 322.6,
    "req_s": 1.26,
    "ttft_p50": 60.08,
    "ttft_p99": 178.6
  },
  {
    "concurrency": 16,
    "e2e_p99": 6893.66,
    "errors": 0,
    "itl_p50": 25.37,
    "output_tok_s": 625.4,
    "req_s": 2.44,
    "ttft_p50": 78.1,
    "ttft_p99": 118.08
  },
  {
    "concurrency": 32,
    "e2e_p99": 10250.91,
    "errors": 0,
    "itl_p50": 28.47,
    "output_tok_s": 920.7,
    "req_s": 3.6,
    "ttft_p50": 128.66,
    "ttft_p99": 189.37
  },
  {
    "concurrency": 64,
    "e2e_p99": 10098.81,
    "errors": 0,
    "itl_p50": 35.22,
    "output_tok_s": 1724.4,
    "req_s": 6.74,
    "ttft_p50": 160.95,
    "ttft_p99": 310.57
  },
  {
    "concurrency": 96,
    "e2e_p99": 12377.91,
    "errors": 0,
    "itl_p50": 38.42,
    "output_tok_s": 2217.7,
    "req_s": 8.66,
    "ttft_p50": 268.73,
    "ttft_p99": 403.28
  },
  {
    "concurrency": 128,
    "e2e_p99": 15086.13,
    "errors": 0,
    "itl_p50": 44.55,
    "output_tok_s": 2419.9,
    "req_s": 9.45,
    "ttft_p50": 280.26,
    "ttft_p99": 516.46
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
