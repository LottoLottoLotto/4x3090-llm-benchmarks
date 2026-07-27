# `gemma4-depth/tli-qwen06-k4/ctx4096`

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
| Layout | TP=2 |
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
| `decode_tok_s` | 44.9 |
| `prefill_tok_s` | 1439.0 |

## Launch command

```bash
-c '${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18261 --served-model-name bench --tensor-parallel-size 2 --language-model-only --max-model-len 36864 --max-num-seqs 2 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.94 --generation-config vllm --disable-hybrid-kv-cache-manager --speculative-config '{"method":"draft_model","model":"${MODEL_ROOT}/Qwen3-0.6B","num_speculative_tokens":4,"use_heterogeneous_vocab":true}'
```

## Speculative decoding

```json
{
  "acceptance": 0.4722,
  "draft_path": null,
  "draft_ref": "Qwen3-0.6B",
  "k": 4,
  "method": "draft_model_tli"
}
```

## Engine knobs

```json
{
  "filler": "gutenberg pg2600",
  "kv_manager": "full (disable-hybrid)",
  "needles": 8,
  "prefill_s_cold": 2.492025936022401,
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

- `repo:llm-bench/results/daily-papers/2026-07-17/gemma4-context-depth/gemma4-12b-awq-depth--tli-qwen06-k4.results.json`

## Notes

8/8 иголок на всех глубинах. no-spec TP=1 hybrid-KV (122k влезает в один 3090); TLI TP=2 full-KV, драфтер каппит глубину 32k. Конфиги плеч РАЗНЫЕ (TP) — прямое сравнение только с оговоркой.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
