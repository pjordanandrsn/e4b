"""The alias contract: every variant's import package IS experts4bit_qlora.

Requires experts4bit-qlora (torch + bitsandbytes) installed; skipped otherwise
so the file is safe to collect anywhere.
"""
import pytest

pytest.importorskip("experts4bit_qlora")

IMPORT_NAMES = ["e4b", "e4b_qlora", "experts4bit", "experts_4bit"]


@pytest.mark.parametrize("name", IMPORT_NAMES)
def test_alias_is_experts4bit_qlora(name):
    import importlib

    experts4bit_qlora = importlib.import_module("experts4bit_qlora")
    alias = importlib.import_module(name)
    assert alias is experts4bit_qlora
    assert alias.__name__ == "experts4bit_qlora"
