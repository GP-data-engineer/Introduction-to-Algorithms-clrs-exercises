#!/usr/bin/env python3
# run_all_tests.py
"""
Run all pytest test files in the current directory and show a summary.
"""

import pytest
import sys

def main():
    print("=" * 60)
    print(" Running all tests in the current directory ".center(60, "="))
    print("=" * 60)

    # Run pytest programmatically
    exit_code = pytest.main([
        ".",        # current directory
        "-v",       # verbose output
        "--maxfail=3",  # stop after 3 failures
        "--disable-warnings",
    ])

    print("=" * 60)
    if exit_code == 0:
        print("✅ All tests passed successfully!".center(60))
    else:
        print("❌ Some tests failed.".center(60))
    print("=" * 60)

    sys.exit(exit_code)

if __name__ == "__main__":
    main()
