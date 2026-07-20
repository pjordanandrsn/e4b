"""experts-mxfp4 — install/import alias for the MXFP4-family experts stack.

``pip install experts-mxfp4`` installs the real packages (``experts4bit-qlora`` +
``grouped-nf4-gemm``) and this shim re-exports the experts package, so
``import experts_mxfp4`` is identical to ``import experts4bit_qlora`` — submodules
included. The MXFP4 kernel lane imports by its own module names
(``mxfp4_grouped``, ``mxfp4_loader``, ...) from grouped-nf4-gemm.
Project home: https://cerinamroth.com/ml/
"""
import sys as _sys

import experts4bit_qlora as _real

# Canonical transparent-alias idiom: replace this module object in sys.modules
# with the real package, so this name and every submodule resolve to it.
_sys.modules[__name__] = _real
