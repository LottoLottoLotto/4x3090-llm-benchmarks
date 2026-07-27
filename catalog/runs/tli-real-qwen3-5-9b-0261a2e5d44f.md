# `tli-real/qwen35-9b-awq--no-spec/c8`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | tli-real |
| Model | Qwen3.5-9B |
| Checkpoint | Qwen3.5-9B-AWQ |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | real_prompt_chat |
| TPS kind | aggregate_output |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 8 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 377.43 |
| `ttft_p50_ms` | 464.4 |

## Launch command

```bash
-c '${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Qwen3.5-9B-AWQ' --host 127.0.0.1 --port 18252 --served-model-name bench --tensor-parallel-size 1 --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --generation-config vllm --language-model-only --attention-backend flash_attn
```

## Engine knobs

```json
{
  "prompts": "dolly-15k x16 real (closed_qa/open_qa/summarization)",
  "repeats": 3,
  "sampling": "greedy",
  "tok_s_all": [
    378.05,
    377.43,
    376.62
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-real-workloads/arms/qwen35-9b-awq/qwen35-9b-awq--no-spec.results.json`

## Notes

Реальные человеческие промпты. Синтетика завышала спекдекод: см. source=tli-synth. Qwen3.5/3.6: TLI draft_model несовместим с hybrid linear attention (vLLM 0.25).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
