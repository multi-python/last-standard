import importlib
from typing import Sequence


def backport(
    modules: Sequence[str] = [
        "zoneinfo",
    ],
    ignore_missing: bool = True
) -> None:
    for module in modules:
        try:
            importlib.import_module(f"last_standard.{module}")
        except ImportError:
            if not ignore_missing:
                raise
