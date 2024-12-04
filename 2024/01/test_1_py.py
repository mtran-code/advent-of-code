import subprocess

import pytest

DAY = "01"
YEAR = "2024"

PY_SCRIPT = f"{YEAR}/{DAY}/main.R"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 2031679
SOLUTION_P2 = 19678534


@pytest.mark.benchmark
def test_1p1_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )


@pytest.mark.benchmark
def test_1p2_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )


@pytest.mark.benchmark
def test_1_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )
