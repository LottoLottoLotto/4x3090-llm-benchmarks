# `orch/Qwen3.6-27B/vllm_FP8-static_tp4x1_spec-none_c32768_pl220_single_stream`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-FP8 |
| Quant | fp8-static |
| Quant method | fp8 |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 55.9 |
| `req_s` | 0.22 |
| `ttft_p50_ms` | 461.13 |
| `ttft_p99_ms` | 472.2 |
| `itl_p50_ms` | 16.12 |
| `e2e_p99_ms` | 4598.86 |
| `vram_peak_mib` | 84584 |
| `avg_power_w` | 877.0 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-FP8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 1
```

## Engine knobs

```json
{
  "_env_VLLM_ATTENTION_BACKEND": "FLASH_ATTN",
  "_env_VLLM_USE_FLASHINFER_SAMPLER": "0",
  "enforce_eager": false,
  "gpu_memory_utilization": 0.9,
  "kv_cache_dtype": "auto",
  "max_num_seqs": 1,
  "trust_remote_code": true
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 4598.86,
    "errors": 0,
    "itl_p50": 16.12,
    "output_tok_s": 55.9,
    "req_s": 0.22,
    "ttft_p50": 461.13,
    "ttft_p99": 472.2
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
