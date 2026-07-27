# `tli-synth-ext/qwen3-4b--tli-tinyllama-k8/prose/c8`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | tli-synth-ext |
| Model | Qwen3-4B |
| Checkpoint | Qwen3-4B |
| Quant | bf16 |
| Quant method | none |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | synthetic_prompt_continuation |
| TPS kind | aggregate_output |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 8 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 303.98 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Qwen3-4B' --host 127.0.0.1 --port 18240 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --attention-backend flash_attn --generation-config vllm --speculative-config '{"method":"draft_model","model":"${MODEL_ROOT}/TinyLlama-1.1B-Chat-v1.0","num_speculative_tokens":8,"use_heterogeneous_vocab":true}'
```

## Speculative decoding

```json
{
  "acceptance": 0.3731,
  "draft_path": null,
  "draft_ref": "TinyLlama-1.1B",
  "k": 8,
  "method": "draft_model_tli"
}
```

## Engine knobs

```json
{
  "prompt_kind": "prose",
  "repeats": 2,
  "tok_s_all": [
    303.69,
    304.26
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-cross-vocab-extended/qwen3-4b--tli-tinyllama-k8.results.json`

## Notes

СИНТЕТИКА (шаблонные корпуса, prompt-continuation): acceptance и выигрыши спекдекода здесь завышены против реальных промптов (source=tli-real). Пруф-пойнт разрыва — сравнить с tli-real.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
