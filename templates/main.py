input_file = "1111/1/input.txt"

with open(input_file, "r") as f:
    input_str = [line.strip() for line in f.readlines()]


def part1(input: list[str]) -> int:
    return 1


def part2(input: list[str]) -> int:
    return 1


# TEST

import pytest


def test_part1():
    assert part1(input_str) == 1


def test_part2():
    assert part2(input_str) == 1


if __name__ == "__main__":
    pytest.main([__file__])
