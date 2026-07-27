# `vllm026-gemma4-mtp/mtp-k2_c1`

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
| `output_tok_s` | 270.39 |
| `total_tok_s` | 811.17 |
| `req_s` | 0.5281 |
| `ttft_p50_ms` | 112.06 |
| `itl_p50_ms` | 6.24 |
| `tpot_p50_ms` | 3.5 |
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
    28.35249042145594,
    42.21422142214221,
    44.50600184672207,
    23.228346456692915,
    40.24713150926743,
    13.461538461538462,
    24.9633431085044,
    35.13738551207327,
    53.22255790533737,
    29.325058184639257,
    39.658194566170025,
    40.93333333333333,
    18.1545636242505,
    20.420110192837466,
    40.89698046181172,
    54.96926229508197,
    40.096830985915496,
    45.52238805970149,
    15.554842847979474,
    58.59872611464968
  ],
  "draft_acceptance_pct_median": 39.877512776042764,
  "output_tok_s_all": [
    237.4958272165382,
    277.03059895974803,
    284.278997231857,
    223.09826034521558,
    272.4691743547493,
    194.6753676123669,
    228.0470696636145,
    258.1579967080828,
    308.24658116907716,
    241.439548031707,
    270.3367285274684,
    274.07747866473665,
    208.0792119379856,
    214.8286921483914,
    273.60271805198863,
    312.204583796759,
    270.44514202115664,
    286.5322750045931,
    200.71344212663743,
    322.3920421105812
  ],
  "output_tok_s_max": 322.3920421105812,
  "output_tok_s_min": 194.6753676123669,
  "repeats": 20
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
