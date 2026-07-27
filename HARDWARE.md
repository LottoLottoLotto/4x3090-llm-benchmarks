# Hardware

Most measurements come from the same home rig. Individual rows and campaign
notes take precedence when a setting changed.

| Component | Configuration |
|---|---|
| GPUs | 4x RTX 3090, 24 GB each, Ampere `sm_86` |
| Interconnect | PCIe 3.0 x16 on all four cards, no NVLink |
| CUDA P2P | Enabled through the patched open kernel module and verified by cross-process transfers on all 12 directed pairs |
| Default power limit | 220 W per GPU |
| Maximum card limits | 350 / 385 / 365 / 350 W |
| CPU | AMD EPYC 7642, 48 cores |
| Motherboard | HUANANZHI H12D-8D |
| System memory | 125 GiB |
| Driver | 610.43.02 for the latest snapshot |

Most historical vLLM runs used CUDA 12.6. Laguna S 2.1 and some later
experiments used CUDA 12.8. The engine and toolkit recorded on the run or its
campaign page are part of the comparison, not incidental metadata.

The 3090 has no native FP8 or FP4 tensor path. A label such as FP8 or NVFP4
describes the checkpoint or serving format. It does not mean the card executes a
native Blackwell FP4 kernel.
