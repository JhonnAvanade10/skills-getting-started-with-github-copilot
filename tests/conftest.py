import os
import sys

# Ensure project root is on sys.path so running test modules with plain
# `python tests/...` still finds `src` package. pytest already handles this,
# but adding this makes direct execution behave similarly.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
