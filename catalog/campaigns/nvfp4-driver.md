# nvfp4-driver

5 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-11 | [nvfp4/unsloth-NVFP4/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-36093148c8bf.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 145.4 output tok/s |
| 2026-07-11 | [nvfp4/unsloth-NVFP4-Fast/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-4605c6b82801.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 145.4 output tok/s |
| 2026-07-11 | [nvfp4/nvidia-NVFP4/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-51d067d3da4f.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 148.8 output tok/s |
| 2026-07-11 | [nvfp4/cyankiwi-AWQ/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-009f33338855.md) | Qwen3.6-35B-A3B | awq-int4 | vllm 0.24 | TP=2 | 131072 | 1 | 131.1 output tok/s |
| 2026-07-11 | [nvfp4/QuantTrio-AWQ/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-7d852d7c79f7.md) | Qwen3.6-35B-A3B | awq-int4 | vllm 0.24 | TP=2 | 131072 | 1 | 129.9 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
