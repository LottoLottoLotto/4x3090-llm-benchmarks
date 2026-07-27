# `dflash-depth/dflash/tp4/ctx196608`

| field | value |
|---|---|
| Date | 2026-07-13 |
| Campaign | dflash-depth |
| Model | Qwen3.6-27B |
| Checkpoint | QuantTrio-Qwen3.6-27B-AWQ |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 196608 |
| Generated tokens | 256 |
| KV cache | auto (BF16) |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3.6806876649118143 |
| `decode_tok_s` | 3.6806876649118143 |
| `prefill_tok_s` | 725.3944042776978 |
| `ttft_p50_ms` | 271062.1910095215 |
| `itl_p50_ms` | 350.4599597777776 |
| `e2e_p99_ms` | 340452.88586616516 |

## Launch command

```bash
#!/usr/bin/env bash
set -euo pipefail

VLLM_ENV=${ENGINE_ROOT}/vllm-env
PORT=${PORT:-18100}

export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HOME=${SSD_ROOT}/hf_cache
export NCCL_P2P_DISABLE=1
export CUDA_HOME="$VLLM_ENV/lib/python3.12/site-packages/nvidia/cu13"
export PATH="$CUDA_HOME/bin:$PATH"
export NVCC_PREPEND_FLAGS=-DCCCL_DISABLE_CTK_COMPATIBILITY_CHECK
export VLLM_CACHE_ROOT=${SSD_ROOT}/caches/vllm

exec "$VLLM_ENV/bin/vllm" serve \
  ${MODEL_ROOT}/QuantTrio-Qwen3.6-27B-AWQ \
  --host 127.0.0.1 \
  --port "$PORT" \
  --served-model-name bench \
  --tensor-parallel-size 4 \
  --disable-custom-all-reduce \
  --language-model-only \
  --max-model-len 262144 \
  --max-num-batched-tokens 8192 \
  --gpu-memory-utilization 0.90 \
  --max-num-seqs 1 \
  --kv-cache-dtype auto \
  --attention-backend flash_attn \
  --generation-config vllm \
  --speculative-config '{"method":"dflash","model":"${MODEL_ROOT}/qwen3.6-27b-dflash","num_speculative_tokens":15,"attention_backend":"FLASH_ATTN"}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": 15,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "gpu_memory_utilization": 0.9,
  "max_num_batched_tokens": 8192,
  "max_num_seqs": 1,
  "repeats": null
}
```

## Provenance

- `rig:~/benchmarks/qwen36-depth-sweep-2026-07-13/dflash-tp4.results.json`

## Notes

Depth-свип: один TP4-сервер, output 256, KV auto (BF16), repeats=1. DFlash K=15, acceptance 0.019. no-draft (mode=target) = чистый AWQ, это базовая кривая для кросс-движковых сравнений. Пост: posts/2026-07-12-qwen36-dflash-262k. ВАЖНО: decode здесь = decode_tok_s_after_first, wall_output_tok_s в сырье занижен (включает prefill).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
