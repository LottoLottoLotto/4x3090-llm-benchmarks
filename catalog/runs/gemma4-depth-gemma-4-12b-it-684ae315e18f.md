# `gemma4-depth/no-spec/ctx4096`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | gemma4-depth |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12B-it-AWQ-INT4 |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | needle_qa_depth |
| Layout | TP=1 |
| Context | 4096 |
| Concurrency | 1 |
| Prompt tokens | 3586 |
| Generated tokens | 48 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `decode_tok_s` | 72.77 |
| `prefill_tok_s` | 1125.7 |

## Launch command

```bash
-c '${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18260 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 131072 --max-num-seqs 2 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.94 --generation-config vllm
```

## Engine knobs

```json
{
  "filler": "gutenberg pg2600",
  "kv_manager": "hybrid",
  "needles": 8,
  "prefill_s_cold": 3.1855462790699676,
  "repeats": 3
}
```

## Quality

```json
{
  "needle_accuracy": [
    1.0,
    1.0,
    1.0
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/gemma4-context-depth/gemma4-12b-awq-depth--no-spec.results.json`

## Notes

8/8 иголок на всех глубинах. no-spec TP=1 hybrid-KV (122k влезает в один 3090); TLI TP=2 full-KV, драфтер каппит глубину 32k. Конфиги плеч РАЗНЫЕ (TP) — прямое сравнение только с оговоркой.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
