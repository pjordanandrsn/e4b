"""Drift guard: every alias must forward the real package's FULL extra set.

The fetch that caught this: `experts4bit[fast]` silently installed without the
kernel because the alias only forwarded {train, serve}. This diffs each alias's
declared optional-dependencies against experts4bit-qlora's PUBLISHED extras
(Provides-Extra on PyPI) and fails on any missing extra — so the next time the
real package gains an extra, the aliases fail the build until they forward it.

Run from the repo root: `python scripts/check_alias_extras.py`.
"""
import json
import re
import sys
import tomllib
import urllib.request
from pathlib import Path

REAL = "experts4bit-qlora"
PKGS_DIR = Path(__file__).resolve().parent.parent / "packages"


def real_extras():
    url = f"https://pypi.org/pypi/{REAL}/json"
    last = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                data = json.load(r)
            break
        except Exception as e:  # noqa: BLE001
            last = e
    else:
        print(f"ERROR: could not reach PyPI for {REAL} metadata: {last}", file=sys.stderr)
        sys.exit(2)
    extras = set()
    for req in data["info"].get("requires_dist") or []:
        m = re.search(r'extra\s*==\s*["\']([^"\']+)["\']', req)
        if m:
            extras.add(m.group(1))
    return extras


def alias_extras(pyproject: Path):
    d = tomllib.load(open(pyproject, "rb"))
    return set(d["project"].get("optional-dependencies", {}).keys())


def main():
    real = real_extras()
    print(f"{REAL} published extras: {sorted(real)}")
    bad = 0
    for pp in sorted(PKGS_DIR.glob("*/pyproject.toml")):
        name = pp.parent.name
        have = alias_extras(pp)
        missing = real - have
        if missing:
            bad += 1
            print(f"  FAIL {name}: missing extras {sorted(missing)} (has {sorted(have)})")
        else:
            print(f"  ok   {name}: {sorted(have)}")
    if bad:
        print(f"\n{bad} alias(es) do not forward the full extra set — fix before publishing.")
        sys.exit(1)
    print("\nall aliases forward the full extra set.")


if __name__ == "__main__":
    main()
