import subprocess

import pytest

DAY = "XX"
YEAR = "2024"

R_SCRIPT = f"{YEAR}/{DAY}/main.R"
INPUT_FILE = f"{YEAR}/{DAY}/input.txt"

SOLUTION_P1 = 1
SOLUTION_P2 = 1


@pytest.mark.benchmark
def test_Xp1_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1


@pytest.mark.benchmark
def test_Xp2_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2


@pytest.mark.benchmark
def test_X_R():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
