# `tli-real/mistral7b-inst--tli-qwen06-k4/c4`

| field | value |
|---|---|
| Date | 2026-07-17 |
| Campaign | tli-real |
| Model | Mistral-7B |
| Checkpoint | Mistral-7B-Instruct-v0.3 |
| Quant | bf16 |
| Quant method | none |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | real_prompt_chat |
| TPS kind | aggregate_output |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 4 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 106.49 |
| `ttft_p50_ms` | 151.1 |

## Launch command

```bash
-c '${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT}/Mistral-7B-Instruct-v0.3' --host 127.0.0.1 --port 18252 --served-model-name bench --tensor-parallel-size 1 --max-model-len 8192 --max-num-seqs 8 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.92 --generation-config vllm --attention-backend flash_attn --speculative-config '{"method":"draft_model","model":"${MODEL_ROOT}/Qwen3-0.6B","num_speculative_tokens":4,"use_heterogeneous_vocab":true}'
```

## Speculative decoding

```json
{
  "acceptance": 0.3129,
  "draft_path": null,
  "draft_ref": "Qwen3-0.6B",
  "k": 4,
  "method": "draft_model_tli"
}
```

## Engine knobs

```json
{
  "prompts": "dolly-15k x16 real (closed_qa/open_qa/summarization)",
  "repeats": 3,
  "sampling": "greedy",
  "tok_s_all": [
    104.38,
    107.12,
    106.49
  ]
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-17/vllm-tli-real-workloads/arms/mistral7b-inst/mistral7b-inst--tli-qwen06-k4.results.json`

## Notes

Реальные человеческие промпты. Синтетика завышала спекдекод: см. source=tli-synth. Qwen3.5/3.6: TLI draft_model несовместим с hybrid linear attention (vLLM 0.25).

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
