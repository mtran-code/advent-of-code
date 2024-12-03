import re

input_file = "2024/03/input.txt"

with open(input_file, "r") as f:
    input_str = "".join([line.strip() for line in f.readlines()])


def part1(input: str) -> int:
    matches = re.findall("(?<=mul\\()[0-9]+,[0-9]+(?=\\))", input)
    sum = 0
    for match in matches:
        a, b = (int(dig) for dig in match.split(","))
        sum += a * b
    return sum


def part2(input: str) -> int:
    matches = re.findall("do\\(\\)|don't\\(\\)|(?<=mul\\()[0-9]+,[0-9]+(?=\\))", input)
    print(matches)
    sum = 0
    mult = 1
    for match_ in matches:
        match match_:
            case "do()":
                mult = 1
            case "don't()":
                mult = 0
            case _:
                a, b = (int(factor) for factor in match_.split(","))
                sum += a * b * mult
    return sum


# TEST

import pytest


def test_part1():
    assert part1(input_str) == 159833790


def test_part2():
    assert part2(input_str) == 89349241


if __name__ == "__main__":
    pytest.main([__file__])
