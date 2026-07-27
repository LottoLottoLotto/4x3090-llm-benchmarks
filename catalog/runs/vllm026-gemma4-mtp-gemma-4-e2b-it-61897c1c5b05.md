# `vllm026-gemma4-mtp/mtp-k2_c4`

| field | value |
|---|---|
| Date | 2026-07-27 |
| Campaign | vllm026-gemma4-mtp |
| Model | Gemma-4-E2B-it |
| Checkpoint | gemma-4-E2B-it-qat-mobile-ct |
| Quant | qat-mixed-int2-4-8 |
| Quant method | qat |
| Engine | vllm |
| Engine version | 0.26.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 4 |
| Prompt tokens | 1024 |
| Generated tokens | 512 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 535.81 |
| `total_tok_s` | 1607.42 |
| `req_s` | 1.0465 |
| `ttft_p50_ms` | 131.63 |
| `itl_p50_ms` | 10.62 |
| `tpot_p50_ms` | 6.23 |
| `vram_peak_mib` | 23296 |
| `avg_power_w` | 168.29 |
| `max_temp_c` | 70.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/vllm' serve '${MODEL_ROOT}/gemma-4-E2B-it-qat-mobile-ct' --host 127.0.0.1 --port 18327 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 64 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --generation-config vllm --speculative-config '{"method":"mtp","model":"${MODEL_ROOT}/gemma-4-E2B-it-assistant","num_speculative_tokens":2}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": 2,
  "method": "mtp"
}
```

## Engine knobs

```json
{
  "assistant_model": "${MODEL_ROOT}/gemma-4-E2B-it-assistant",
  "centroids_masking": true,
  "client_version": "0.26.0",
  "gpu_memory_utilization": 0.9,
  "max_num_batched_tokens": 8192,
  "max_num_seqs": 64,
  "model_runner_v2": true,
  "num_speculative_tokens": 2,
  "prefix_caching": false
}
```

## Samples

```json
{
  "draft_acceptance_pct_all": [
    32.90113452188007,
    16.639531097362422,
    36.05042016806723,
    34.34281005356407,
    22.759601706970127
  ],
  "draft_acceptance_pct_median": 32.90113452188007,
  "output_tok_s_all": [
    535.8068791699113,
    456.7321512505709,
    539.9935519342201,
    550.0654813298014,
    477.8591881894544
  ],
  "output_tok_s_max": 550.0654813298014,
  "output_tok_s_min": 456.7321512505709,
  "repeats": 5
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
