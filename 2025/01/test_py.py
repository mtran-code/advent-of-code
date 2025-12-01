import subprocess

import pytest

DAY = "01"
YEAR = "2025"

PY_SCRIPT = f"{YEAR}/{DAY}/main.py"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 1026
SOLUTION_P2 = 5923


@pytest.mark.benchmark
def test_01p1_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )


@pytest.mark.benchmark
def test_01p2_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )


@pytest.mark.benchmark
def test_01_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )
