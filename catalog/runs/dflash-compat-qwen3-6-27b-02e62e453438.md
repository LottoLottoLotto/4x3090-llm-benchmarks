# `dflash-compat/BF16/bf16-dflash/ctx8192`

| field | value |
|---|---|
| Date | 2026-07-13 |
| Campaign | dflash-compat |
| Model | Qwen3.6-27B |
| Checkpoint | QuantTrio-Qwen3.6-27B-AWQ |
| Quant | bf16 |
| Quant method | none |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 8192 |
| Generated tokens | 256 |
| KV cache | auto (BF16) |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 40.195953470033906 |
| `decode_tok_s` | 40.195953470033906 |
| `prefill_tok_s` | 835.1721223926717 |
| `ttft_p50_ms` | 9844.352006912231 |

## Launch command

```bash
#!/usr/bin/env bash
set -euo pipefail

VLLM_ENV=${VLLM_ENV:-${ENGINE_ROOT}/vllm-env}
TARGET_MODEL=${TARGET_MODEL:?set TARGET_MODEL}
MAX_MODEL_LEN=${MAX_MODEL_LEN:-65536}
PORT=${PORT:-18100}

export CUDA_VISIBLE_DEVICES=0,1,2,3
export HF_HOME=${SSD_ROOT}/hf_cache
export NCCL_P2P_DISABLE=1
export CUDA_HOME="$VLLM_ENV/lib/python3.12/site-packages/nvidia/cu13"
export PATH="$CUDA_HOME/bin:$PATH"
export NVCC_PREPEND_FLAGS=-DCCCL_DISABLE_CTK_COMPATIBILITY_CHECK
export VLLM_CACHE_ROOT=${SSD_ROOT}/caches/vllm

exec "$VLLM_ENV/bin/vllm" serve \
  "$TARGET_MODEL" \
  --host 127.0.0.1 \
  --port "$PORT" \
  --served-model-name bench \
  --tensor-parallel-size 4 \
  --disable-custom-all-reduce \
  --language-model-only \
  --max-model-len "$MAX_MODEL_LEN" \
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
  "max_num_seqs": 1
}
```

## Provenance

- `rig:~/benchmarks/dflash-quant-compat/bf16-dflash.results.json`

## Notes

Совместимость DFlash-драфта с разными квантами таргета (13.07).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
