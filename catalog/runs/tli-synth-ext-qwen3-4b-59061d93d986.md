# `tli-synth-ext/qwen3-4b--ngram-k4/code/c4`

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
| Concurrency | 4 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 525.86 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Qwen3-4B' --host 127.0.0.1 --port 18240 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --attention-backend flash_attn --generation-config vllm --speculative-config '{"method":"ngram","num_speculative_tokens":4,"prompt_lookup_min":1,"prompt_lookup_max":4}'
```

## Speculative decoding

```json
{
  "acceptance": 0.4496,
  "draft_path": null,
  "draft_ref": null,
  "k": 4,
  "method": "ngram"
}
```

## Engine knobs

```json
{
  "prompt_kind": "code",
  "repeats": 2,
  "tok_s_all": [
    525.39,
    526.33
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-cross-vocab-extended/qwen3-4b--ngram-k4.results.json`

## Notes

СИНТЕТИКА (шаблонные корпуса, prompt-continuation): acceptance и выигрыши спекдекода здесь завышены против реальных промптов (source=tli-real). Пруф-пойнт разрыва — сравнить с tli-real.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
