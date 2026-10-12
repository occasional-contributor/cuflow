"""CuFlow ("Copper Flow") -- an experimental procedural PCB layout program.

The public API lives in :mod:`cuflow.cuflow`.  Everything is re-exported here
so that both ``import cuflow as cu`` and ``from cuflow import cuflow as cu``
keep working.
"""

from . import cuflow
from .cuflow import *  # noqa: F401,F403

__version__ = "0.1.0"

__all__ = ["cuflow", "__version__"]
