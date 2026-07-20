# expertsmxfp4

**Alias for the MXFP4-family experts work.** The native-byte MXFP4 lane
(table-swap kernel, provenance, QLoRA-on-released-bytes, K3 gather) ships in
[`grouped-nf4-gemm`](https://pypi.org/project/grouped-nf4-gemm/); the MoE
loaders, adapters, serving, and hot-expert residency in
[`experts4bit-qlora`](https://pypi.org/project/experts4bit-qlora/).

```bash
pip install expertsmxfp4   # installs both real packages
```
```python
import expertsmxfp4   # identical to `import experts4bit_qlora`
```
