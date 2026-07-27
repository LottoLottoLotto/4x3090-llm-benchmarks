# `vllm026-gemma4-mtp/mtp-k1_c1`

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
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 1 |
| Prompt tokens | 1024 |
| Generated tokens | 512 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 233.32 |
| `total_tok_s` | 699.97 |
| `req_s` | 0.4557 |
| `ttft_p50_ms` | 112.75 |
| `itl_p50_ms` | 5.99 |
| `tpot_p50_ms` | 4.1 |
| `vram_peak_mib` | 23078 |
| `avg_power_w` | 166.49 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/vllm' serve '${MODEL_ROOT}/gemma-4-E2B-it-qat-mobile-ct' --host 127.0.0.1 --port 18327 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 64 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --generation-config vllm --speculative-config '{"method":"mtp","model":"${MODEL_ROOT}/gemma-4-E2B-it-assistant","num_speculative_tokens":1}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": 1,
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
  "num_speculative_tokens": 1,
  "prefix_caching": false
}
```

## Samples

```json
{
  "draft_acceptance_pct_all": [
    32.64114211550941,
    35.97074468085106,
    46.38511095204009,
    30.60702875399361,
    41.94444444444444,
    46.80545585068198,
    39.8224043715847,
    59.71896955503513,
    50.62638172439205,
    52.57270693512305,
    48.72727272727273,
    46.59498207885305,
    63.28810853950518,
    29.860228716645487,
    52.61194029850746,
    63.6290967226219,
    51.183431952662716,
    43.13725490196079,
    57.30769230769231,
    47.08842559309849
  ],
  "draft_acceptance_pct_median": 46.946940721890236,
  "output_tok_s_all": [
    211.37032267922146,
    216.60168390951011,
    232.30859514018982,
    208.20605945746632,
    225.58736067372803,
    232.5646948602629,
    221.7204629678472,
    251.54478825461297,
    237.91831279196074,
    240.80685885342598,
    235.26729198660007,
    233.49870753534185,
    258.14417556755535,
    207.2464198484135,
    241.64970252000086,
    257.2886798446375,
    240.08944692601264,
    227.63601985673984,
    248.54260535686626,
    233.14577127053985
  ],
  "output_tok_s_max": 258.14417556755535,
  "output_tok_s_min": 207.2464198484135,
  "repeats": 20
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
