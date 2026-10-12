"""Root test configuration.

Adds the repository root (for the top-level ``tools`` package) and the ``src``
directory (for ``cuflow``) to ``sys.path`` so the suite runs from a plain
checkout as well as from an editable install.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for path in (ROOT, ROOT / "src"):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)
