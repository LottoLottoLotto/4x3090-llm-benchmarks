# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp2x1_spec-none_c32768_pl220_single_stream`

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
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=2 |
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
| `output_tok_s` | 67.8 |
| `req_s` | 0.26 |
| `ttft_p50_ms` | 49.8 |
| `ttft_p99_ms` | 60.31 |
| `itl_p50_ms` | 14.51 |
| `e2e_p99_ms` | 3855.18 |
| `vram_peak_mib` | 87608 |
| `avg_power_w` | 493.2 |
| `max_temp_c` | 70.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 1
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
    "e2e_p99": 3855.18,
    "errors": 0,
    "itl_p50": 14.51,
    "output_tok_s": 67.8,
    "req_s": 0.26,
    "ttft_p50": 49.8,
    "ttft_p99": 60.31
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
