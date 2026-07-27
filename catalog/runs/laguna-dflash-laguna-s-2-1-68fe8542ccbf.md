# `laguna-dflash/target/depth-32768x256-c1`

| field | value |
|---|---|
| Date | 2026-07-22 |
| Campaign | laguna-dflash |
| Model | Laguna-S-2.1 |
| Checkpoint | poolside/Laguna-S-2.1-INT4 |
| Quant | compressed-tensors-int4-g32-symmetric |
| Quant method | compressed-tensors |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | context_depth |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 32768 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 12.585912099100486 |
| `decode_tok_s` | 97.33541414169432 |
| `prefill_tok_s` | 1874.83799621427 |
| `total_tok_s` | 1625.6475369877214 |
| `req_s` | 0.049163719137111275 |
| `ttft_p50_ms` | 17719.720042077824 |
| `ttft_p99_ms` | 17719.720042077824 |
| `itl_p50_ms` | 10.483341058716178 |
| `tpot_p50_ms` | 10.273752968721823 |
| `e2e_p99_ms` | 20339.52704910189 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 749.77625 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-32768x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.016786224022300636,
  "prefix_hit_rate": 0.000975312404754648,
  "throttle_sample_count": 84
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/target/depth-32768x256-c1.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
