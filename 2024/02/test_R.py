import subprocess

import pytest

R_SCRIPT = "2024/02/main.R"
INPUT_FILE = "2024/02/input.txt"

SOLUTION_P1 = 680
SOLUTION_P2 = 710


@pytest.mark.benchmark
def test_2p1():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1


@pytest.mark.benchmark
def test_2p2():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2


@pytest.mark.benchmark
def test_2():
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "1"])) == SOLUTION_P1
    assert int(subprocess.check_output(args=[R_SCRIPT, INPUT_FILE, "2"])) == SOLUTION_P2
