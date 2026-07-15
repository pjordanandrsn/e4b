# e4b — alias packages for `experts4bit-qlora`

This repo publishes thin **alias packages** so every short/variant name people
might type for **[experts4bit-qlora](https://pypi.org/project/experts4bit-qlora/)**
resolves on PyPI and in `import` instead of dead-ending. All code, docs, and
releases live in the real package; these are dependency + re-export shims.

| PyPI name | `import` | installs |
|---|---|---|
| [`e4b`](packages/e4b) | `import e4b` | experts4bit-qlora |
| [`e4b-qlora`](packages/e4b-qlora) | `import e4b_qlora` | experts4bit-qlora |
| [`experts4bit`](packages/experts4bit) | `import experts4bit` | experts4bit-qlora |
| `experts-4bit` | — | *not registrable: PyPI's separator-similarity rule reserves it against `experts4bit`, blocking squatters automatically* |

Each `import <name>` is transparently `experts4bit_qlora` (submodules included).
Extras forward: `pip install e4b[train]` == `experts4bit-qlora[train]`.

Publishing is **tokenless** (PyPI Trusted Publishing / OIDC) — one `git tag`
push builds and publishes all four. See **[SETUP.md](SETUP.md)**.

Project home: <https://cerinamroth.com/ml/> · MIT © Cerin Amroth.
