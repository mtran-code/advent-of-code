import pytest
from main import part1, part2

input_file = "2024/03/input.txt"

with open(input_file, "r") as f:
    input_str = "".join([line.strip() for line in f.readlines()])


@pytest.mark.benchmark
def test_3p1():
    assert part1(input_str) == 159833790


@pytest.mark.benchmark
def test_3p2():
    assert part2(input_str) == 89349241


@pytest.mark.benchmark
def test_3():
    assert part1(input_str) == 159833790
    assert part2(input_str) == 89349241
