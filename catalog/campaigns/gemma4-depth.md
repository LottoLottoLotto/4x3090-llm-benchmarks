# gemma4-depth

8 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-17 | [gemma4-depth/tli-qwen06-k4/ctx4096](../runs/gemma4-depth-gemma-4-12b-it-33bdf9872174.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=2 | 4096 | 1 | 44.9 decode tok/s |
| 2026-07-17 | [gemma4-depth/tli-qwen06-k4/ctx32768](../runs/gemma4-depth-gemma-4-12b-it-a08f01ac5245.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=2 | 32768 | 1 | 27.99 decode tok/s |
| 2026-07-17 | [gemma4-depth/tli-qwen06-k4/ctx16384](../runs/gemma4-depth-gemma-4-12b-it-f8b7b9c77a3a.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=2 | 16384 | 1 | 34.72 decode tok/s |
| 2026-07-17 | [gemma4-depth/no-spec/ctx65536](../runs/gemma4-depth-gemma-4-12b-it-337747966419.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=1 | 65536 | 1 | 95.87 decode tok/s |
| 2026-07-17 | [gemma4-depth/no-spec/ctx4096](../runs/gemma4-depth-gemma-4-12b-it-684ae315e18f.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=1 | 4096 | 1 | 72.77 decode tok/s |
| 2026-07-17 | [gemma4-depth/no-spec/ctx32768](../runs/gemma4-depth-gemma-4-12b-it-3d6553cf9727.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=1 | 32768 | 1 | 92.41 decode tok/s |
| 2026-07-17 | [gemma4-depth/no-spec/ctx16384](../runs/gemma4-depth-gemma-4-12b-it-047fa7fcb95e.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=1 | 16384 | 1 | 87.06 decode tok/s |
| 2026-07-17 | [gemma4-depth/no-spec/ctx122880](../runs/gemma4-depth-gemma-4-12b-it-1b91f988ed6c.md) | Gemma-4-12B-it | awq-int4 | vllm 0.25.0 | TP=1 | 122880 | 1 | 95.99 decode tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
