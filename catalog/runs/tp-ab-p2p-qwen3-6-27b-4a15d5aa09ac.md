# `tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c64`

| field | value |
|---|---|
| Date | 2026-07-26 |
| Campaign | tp-ab-p2p |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-autoround-int4 |
| Quant | autoround-int4 |
| Quant method | autoround |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 64 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 473.1 |
| `ttft_p50_ms` | 8800.41 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/qwen3.6-27b-autoround-int4' --host 127.0.0.1 --port 18001 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.90 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
```

## Engine knobs

```json
{
  "attention_backend": "FLASH_ATTN",
  "driver": "610.43.02",
  "enable_chunked_prefill": true,
  "gpu_memory_utilization": 0.9,
  "max_num_seqs": 256,
  "p2p": "enabled"
}
```

## Samples

```json
{
  "duration_s": 20,
  "requests": 64
}
```

## Provenance

- `repo:llm-bench/results/tp-ab-p2p-2026-07-26/results.jsonl`

## Notes

Controlled TP=2 vs TP=4 A/B with CUDA P2P VERIFIED ON in the same run (driver 610.43.02, nvidia-smi topo -p2p r = OK on all pairs, BAR1 32768 MiB/card; the harness aborts if the topo matrix is not clean). Single variable is --tensor-parallel-size, everything else frozen. single_stream = median of 5 requests after warmup; decode_tok_s excludes TTFT ((n-1)/(e2e-ttft)), output_tok_s is the wall rate (n/e2e). aggregate = concurrency ladder 1/4/16/32/64, 20 s per point, stops when the gain drops under 3%. Reproduces the 2026-06-28 orchestrator sweep within 1.5% on wall rate.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
