# `orch/Qwen3.6-27B/vllm_Int4_tp4x1_spec-none_c32768_pl220_single_stream`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | qwen3.6-27b-autoround-int4 |
| Quant | autoround-int4 |
| Quant method | autoround |
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
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 70.4 |
| `req_s` | 0.27 |
| `ttft_p50_ms` | 450.64 |
| `ttft_p99_ms` | 463.49 |
| `itl_p50_ms` | 12.5 |
| `e2e_p99_ms` | 3649.58 |
| `vram_peak_mib` | 84848 |
| `avg_power_w` | 876.1 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/qwen3.6-27b-autoround-int4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 1
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
    "e2e_p99": 3649.58,
    "errors": 0,
    "itl_p50": 12.5,
    "output_tok_s": 70.4,
    "req_s": 0.27,
    "ttft_p50": 450.64,
    "ttft_p99": 463.49
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
