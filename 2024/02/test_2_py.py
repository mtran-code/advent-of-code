import subprocess

import pytest

DAY = "02"
YEAR = "2024"

PY_SCRIPT = f"{YEAR}/{DAY}/main.R"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 680
SOLUTION_P2 = 710


@pytest.mark.benchmark
def test_2p1_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )


@pytest.mark.benchmark
def test_2p2_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )


@pytest.mark.benchmark
def test_2_py():
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    )
    assert (
        int(subprocess.check_output(args=[PY_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
    )
