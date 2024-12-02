input_file = "2024/01/input.txt"

with open(input_file, "r") as f:
    input_str = f.readlines()


def part1(input: list[str]) -> int:

    a = list()
    b = list()

    for line in input:
        left, right = line.split("   ")
        a.append(int(left.strip()))
        b.append(int(right.strip()))

    a.sort()
    b.sort()

    result = 0
    for i in range(len(a)):
        result += abs(a[i] - b[i])

    return result


def part2(input: list[str]) -> int:
    a = list()
    b = dict()

    for line in input:
        left, right = line.split("   ")
        a.append(int(left.strip()))

        b_input = int(right.strip())
        if b_input in b.keys():
            b[b_input] += 1
        else:
            b[b_input] = 1

    result = 0
    for a_i in a:
        if a_i in b.keys():
            result += a_i * b[a_i]

    return result


# TEST

import pytest


def test_part1():
    assert part1(input_str) == 2031679


def test_part2():
    assert part2(input_str) == 19678534


if __name__ == "__main__":
    pytest.main([__file__])
