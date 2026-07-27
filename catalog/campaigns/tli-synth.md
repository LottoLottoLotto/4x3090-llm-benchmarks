# tli-synth

12 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-17 | [tli-synth/tli-qwen06-k4/repetitive/c8](../runs/tli-synth-mistral-7b-309954dcdbe2.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 8 | 435.24 output tok/s |
| 2026-07-17 | [tli-synth/tli-qwen06-k4/repetitive/c4](../runs/tli-synth-mistral-7b-91db8095e996.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 4 | 238.97 output tok/s |
| 2026-07-17 | [tli-synth/tli-qwen06-k4/repetitive/c2](../runs/tli-synth-mistral-7b-6f4d17361712.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 2 | 107.65 output tok/s |
| 2026-07-17 | [tli-synth/tli-qwen06-k4/repetitive/c1](../runs/tli-synth-mistral-7b-3e137dfaad1b.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 1 | 68.19 output tok/s |
| 2026-07-17 | [tli-synth/ngram-k4/repetitive/c8](../runs/tli-synth-mistral-7b-ded195c260d0.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 8 | 627.41 output tok/s |
| 2026-07-17 | [tli-synth/ngram-k4/repetitive/c4](../runs/tli-synth-mistral-7b-21db9ebadb18.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 4 | 357.66 output tok/s |
| 2026-07-17 | [tli-synth/ngram-k4/repetitive/c2](../runs/tli-synth-mistral-7b-967d2676413a.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 2 | 195.76 output tok/s |
| 2026-07-17 | [tli-synth/ngram-k4/repetitive/c1](../runs/tli-synth-mistral-7b-e76cc0bc3147.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 1 | 104.26 output tok/s |
| 2026-07-17 | [tli-synth/baseline-no-spec/repetitive/c8](../runs/tli-synth-mistral-7b-354aea13ea59.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 8 | 256.67 output tok/s |
| 2026-07-17 | [tli-synth/baseline-no-spec/repetitive/c4](../runs/tli-synth-mistral-7b-df13dfbebfb6.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 4 | 134.08 output tok/s |
| 2026-07-17 | [tli-synth/baseline-no-spec/repetitive/c2](../runs/tli-synth-mistral-7b-7b254e79f0df.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 2 | 68.9 output tok/s |
| 2026-07-17 | [tli-synth/baseline-no-spec/repetitive/c1](../runs/tli-synth-mistral-7b-d17b31991ee6.md) | Mistral-7B | bf16 | vllm 0.25.0 | TP=1 | 8192 | 1 | 35.3 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
