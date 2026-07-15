"""e4b — install/import alias for the ``experts4bit-qlora`` distribution.

``pip install e4b`` installs the real package (``experts4bit-qlora``) and
this shim re-exports it, so ``import e4b`` is identical to
``import experts4bit_qlora`` — submodules included, and
``e4b is experts4bit_qlora`` is True.

The canonical package is ``experts4bit_qlora``; this alias exists only so the
name "e4b" resolves on PyPI and in ``import`` instead of dead-ending.
Project home: https://cerinamroth.com/ml/
"""
import sys as _sys

import experts4bit_qlora as _real

# Canonical transparent-alias idiom: replace this module object in sys.modules
# with the real package, so this name and every submodule resolve to it.
_sys.modules[__name__] = _real
