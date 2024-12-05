import subprocess

import pytest

DAY = "04"
YEAR = "2024"

R_SCRIPT = f"{YEAR}/{DAY}/main.R"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 2633
SOLUTION_P2 = 1936


@pytest.mark.benchmark
def test_4p1_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1


@pytest.mark.benchmark
def test_4p2_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2


@pytest.mark.benchmark
def test_4_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
