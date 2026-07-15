# experts4bit

**Alias for [`experts4bit-qlora`](https://pypi.org/project/experts4bit-qlora/).**

```bash
pip install experts4bit
```
```python
import experts4bit   # identical to `import experts4bit_qlora`
```

`experts4bit` is one of several short/variant names for **experts4bit-qlora** —
QLoRA fine-tuning of fused 4-bit Mixture-of-Experts on a single small GPU, on
stock bitsandbytes. This package is a thin alias so the name resolves instead
of dead-ending; all code, docs, and releases live in the real package.

- Real package: https://pypi.org/project/experts4bit-qlora/
- Source: https://github.com/pjordanandrsn/experts4bit-qlora
- Project home: https://cerinamroth.com/ml/

Extras forward: `pip install experts4bit[train]` / `[serve]`. MIT © Cerin Amroth.
