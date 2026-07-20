# Claiming the alias names on PyPI — turnkey steps

Four thin aliases for `experts4bit-qlora` (`e4b`, `e4b-qlora`, `experts4bit`,
`experts-4bit`), published the same tokenless way the real package is — PyPI
Trusted Publishing (OIDC). No API token is created or stored anywhere.

## 1. Create the empty GitHub repo (you)
```
gh repo create pjordanandrsn/e4b --public --description "Alias packages for experts4bit-qlora"
```
(or the web UI — empty repo, no README).

## 2. Push this staged content (me, once the repo exists)
```
cd ~/code/e4b && git init && git add -A \
  && git commit -m "alias packages (e4b, e4b-qlora, experts4bit, experts-4bit) for experts4bit-qlora" \
  && git branch -M main \
  && git remote add origin git@github.com:pjordanandrsn/e4b.git \
  && git push -u origin main
```

## 3. Register FOUR PyPI pending publishers (you — the only human-gated step)
PyPI → account → **Publishing** → **Add a pending publisher**, once per name.

**The Environment field is REQUIRED and must differ per package** — pending
publishers need a unique (owner, repo, workflow, environment) tuple, or PyPI
rejects the second one ("already registered for a different project name").
Environment name = the same string as the project name:

| PyPI project name | Owner | Repository | Workflow | Environment |
|---|---|---|---|---|
| `e4b` | `pjordanandrsn` | `e4b` | `release.yml` | `e4b` |
| `e4b-qlora` | `pjordanandrsn` | `e4b` | `release.yml` | `e4b-qlora` |
| `experts4bit` | `pjordanandrsn` | `e4b` | `release.yml` | `experts4bit` |
| `experts-4bit` | `pjordanandrsn` | `e4b` | `release.yml` | `experts-4bit` |

> If you already added `e4b` with a **blank** environment, remove that pending
> publisher (trash icon on the Publishing page) and re-add it with
> Environment = `e4b`. The four GitHub environments already exist in the repo.

## 4. Publish all four at once
```
cd ~/code/e4b && git tag v0.1.0 && git push origin v0.1.0
```
The matrix `release.yml` builds and publishes each package via OIDC. Verify:
```
pip install e4b && python -c "import e4b, experts4bit_qlora; assert e4b is experts4bit_qlora; print('ok')"
```

## Notes
- **No token, nothing to leak.** Publish authority is the GitHub Actions OIDC
  identity bound to `pjordanandrsn/e4b` + `release.yml`.
- Aliases track the real package by floor (`>=0.2.0`), so they keep working as
  `experts4bit-qlora` releases without a new alias release.
- If PyPI rejects a name at publish for policy reasons, that one matrix job
  fails independently (`fail-fast: false`); the others still publish.


## Outcome (2026-07-15)

- **Published live at v0.1.0:** `e4b`, `e4b-qlora`, `experts4bit` — all via OIDC, verified installable.
- **`experts-4bit`: not registrable, and that's fine.** PyPI's name-similarity
  rule ("too similar to an existing project") blocks any registration that
  differs from `experts4bit` only by separators — for *everyone*, squatters
  included. The defensive goal is achieved by PyPI itself. `pip install
  experts-4bit` fails with a clean no-match error that points users at the
  working name. If resolution is ever wanted, the owner of `experts4bit` can
  request the name from PyPI admins; until then `packages/experts-4bit/`
  stays staged and out of the release matrix.

## 2026-07-20 batch — the mxfp4-family names

Two new alias packages, same pattern (the fold shipped the MXFP4 lane inside
`grouped-nf4-gemm` 0.2.0, so these are defensive/convenience names):

| PyPI project name | Owner | Repository | Workflow | Environment |
|---|---|---|---|---|
| `experts-mxfp4` | `pjordanandrsn` | `e4b` | `release.yml` | `experts-mxfp4` |

`expertsmxfp4` is staged in `packages/` and CI-verified but **kept out of the
release matrix** — once `experts-mxfp4` publishes, PyPI's separator-similarity
rule auto-defends the squashed spelling (the `experts-4bit`/`experts4bit`
precedent). The kernel-side name (`grouped-mxfp4-gemm`) lives in its own repo
mirroring `gnf4`/`nf4gemm`.
