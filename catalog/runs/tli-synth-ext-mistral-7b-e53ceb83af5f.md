# `tli-synth-ext/mistral7b--tli-qwen06-k4/code/c8`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | tli-synth-ext |
| Model | Mistral-7B |
| Checkpoint | Mistral-7B-v0.3 |
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
| `output_tok_s` | 346.76 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Mistral-7B-v0.3' --host 127.0.0.1 --port 18240 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --attention-backend flash_attn --generation-config vllm --speculative-config '{"method":"draft_model","model":"${MODEL_ROOT}/Qwen3-0.6B","num_speculative_tokens":4,"use_heterogeneous_vocab":true}'
```

## Speculative decoding

```json
{
  "acceptance": 0.6884,
  "draft_path": null,
  "draft_ref": "Qwen3-0.6B",
  "k": 4,
  "method": "draft_model_tli"
}
```

## Engine knobs

```json
{
  "prompt_kind": "code",
  "repeats": 2,
  "tok_s_all": [
    340.41,
    353.11
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-cross-vocab-extended/mistral7b--tli-qwen06-k4.results.json`

## Notes

СИНТЕТИКА (шаблонные корпуса, prompt-continuation): acceptance и выигрыши спекдекода здесь завышены против реальных промптов (source=tli-real). Пруф-пойнт разрыва — сравнить с tli-real.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
