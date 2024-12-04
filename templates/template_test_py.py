import subprocess

import pytest

DAY = "XX"
YEAR = "2024"

PY_SCRIPT = f"{YEAR}/{DAY}/main.py"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 1
SOLUTION_P2 = 1


@pytest.mark.benchmark
def test_Xp1_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )


@pytest.mark.benchmark
def test_Xp2_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )


@pytest.mark.benchmark
def test_X_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )
