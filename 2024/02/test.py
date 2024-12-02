import pytest
from main import part1, part2

input_file = "2024/02/input.txt"

with open(input_file, "r") as f:
    input_str = [line.strip() for line in f.readlines()]


@pytest.mark.benchmark
def test_2p1():
    assert part1(input_str) == 680

@pytest.mark.benchmark
def test_2p2():
    assert part2(input_str) == 710

@pytest.mark.benchmark
def test_2():
    assert part1(input_str) == 680
    assert part2(input_str) == 710