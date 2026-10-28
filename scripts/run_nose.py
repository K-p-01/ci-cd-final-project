"""Run Nose 1.x with a Python compatibility alias."""

import collections
import collections.abc
import sys
from pathlib import Path

if not hasattr(collections, "Callable"):
    collections.Callable = collections.abc.Callable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nose import run_exit  # noqa: E402


if __name__ == "__main__":
    run_exit(argv=["nosetests", "-v"])
