# e4b

**This is an alias.** `e4b` is a lookup name for the canonical package
**[`experts4bit-qlora`](https://pypi.org/project/experts4bit-qlora/)** — it depends on it and `import e4b` re-exports `experts4bit_qlora`.
Install the canonical package:

```bash
pip install experts4bit-qlora
```

`pip install e4b` resolves to the same distribution; extras forward (`e4b[x]` = `experts4bit-qlora[x]`).

- **Canonical documentation:** [https://github.com/pjordanandrsn/experts4bit-qlora](https://github.com/pjordanandrsn/experts4bit-qlora) — start with `docs/SOLUTIONS.md` (one page per problem), `docs/STATUS.md` (the current position) and `docs/capabilities.json` (machine-readable capabilities).
- **Canonical source and issues:** [https://github.com/pjordanandrsn/experts4bit-qlora](https://github.com/pjordanandrsn/experts4bit-qlora) · [issues](https://github.com/pjordanandrsn/experts4bit-qlora/issues). File every issue there, not here.

**What the canonical package solves** (Train and serve Mixture-of-Experts models that do not fit in VRAM: fused 4-bit experts, QLoRA, CPU/NVMe offload, and fast inference on consumer NVIDIA GPUs.)

- `load_in_4bit=True` loads your MoE but the fused expert tensors stay bf16 and the model still OOMs
- QLoRA or LoRA on fused MoE experts that PEFT and the bitsandbytes walker never see
- running a Mixture-of-Experts model larger than VRAM (experts in host RAM) or larger than host RAM (experts on NVMe)
- serving or training a 30B-class MoE on a 24–32 GB consumer NVIDIA GPU
- native MXFP4 experts (gpt-oss, DeepSeek-V4): faithful load, arenas, training, serving

This page carries no measurements, changelog or documentation of its own; the canonical repository's claims register is the only source for numbers.

MIT © Cerin Amroth.
