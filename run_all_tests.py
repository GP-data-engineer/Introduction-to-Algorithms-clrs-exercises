# run_all_tests.py
import sys
import pathlib

try:
    import pytest
except ImportError:
    raise SystemExit("pytest is not installed. Run: python -m pip install -U pytest")

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
TESTS = ROOT / "tests"

# Ensure src is importable even if conftest.py is skipped
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

if __name__ == "__main__":
    # -q: quiet, only show test results; change to -vv if chcesz więcej szczegółów
    raise SystemExit(pytest.main(["-q", str(TESTS)]))
