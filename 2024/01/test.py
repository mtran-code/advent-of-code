import pytest
from main import part1, part2

input_file = "2024/01/input.txt"

with open(input_file, "r") as f:
    input_str = f.readlines()


@pytest.mark.benchmark
def test_1p1():
    assert part1(input_str) == 2031679

@pytest.mark.benchmark
def test_1p2():
    assert part2(input_str) == 19678534

@pytest.mark.benchmark
def test_1():
    assert part1(input_str) == 2031679
    assert part2(input_str) == 19678534