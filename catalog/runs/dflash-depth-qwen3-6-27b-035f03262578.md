# `dflash-depth/target/tp4/ctx131072`

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
| Prompt tokens | 131072 |
| Generated tokens | 256 |
| KV cache | auto (BF16) |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 57.01567170606816 |
| `decode_tok_s` | 57.01567170606816 |
| `prefill_tok_s` | 788.2116592509027 |
| `ttft_p50_ms` | 166312.55722045898 |
| `itl_p50_ms` | 17.910583670634555 |
| `e2e_p99_ms` | 170879.08267974854 |

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
  --generation-config vllm
```

## Engine knobs

```json
{
  "gpu_memory_utilization": 0.9,
  "max_num_batched_tokens": 8192,
  "max_num_seqs": 1,
  "repeats": 1
}
```

## Provenance

- `rig:~/benchmarks/qwen36-depth-sweep-2026-07-13/target-tp4.results.json`

## Notes

Depth-свип: один TP4-сервер, output 256, KV auto (BF16), repeats=1. no-draft (mode=target) = чистый AWQ, это базовая кривая для кросс-движковых сравнений. Пост: posts/2026-07-12-qwen36-dflash-262k. ВАЖНО: decode здесь = decode_tok_s_after_first, wall_output_tok_s в сырье занижен (включает prefill).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
