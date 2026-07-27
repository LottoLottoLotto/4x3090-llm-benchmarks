# `tli-synth/ngram-k4/repetitive/c1`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | tli-synth |
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
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 104.26 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Mistral-7B-v0.3' --host 127.0.0.1 --port 18220 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --attention-backend flash_attn --generation-config vllm --speculative-config '{"method":"ngram","num_speculative_tokens":4,"prompt_lookup_min":1,"prompt_lookup_max":4}'
```

## Speculative decoding

```json
{
  "acceptance": 0.5181,
  "draft_path": null,
  "draft_ref": null,
  "k": 4,
  "method": "ngram"
}
```

## Engine knobs

```json
{
  "prompt_kind": "repetitive",
  "repeats": 2,
  "tok_s_all": [
    104.2,
    104.31
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-cross-vocab/ngram-k4.results.json`

## Notes

СИНТЕТИКА (шаблонные корпуса, prompt-continuation): acceptance и выигрыши спекдекода здесь завышены против реальных промптов (source=tli-real). Пруф-пойнт разрыва — сравнить с tli-real.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
