input_file = "2024/2/input.txt"

with open(input_file, "r") as f:
    input_str = [line.strip() for line in f.readlines()]


def part1(input: list[str]) -> int:
    count = 0
    for line in input:
        levels = [int(level) for level in line.split(" ")]
        direction = 1 if levels[-1] - levels[0] > 0 else -1
        safe = True
        for i in range(1, len(levels)):
            diff = (levels[i] - levels[i - 1]) * direction
            if not (1 <= diff <= 3):
                safe = False
                break
        if safe:
            count += 1
    return count


def part2(input: list[str]) -> int:
    def double_check(levels: list[int]) -> bool:
        direction = 1 if levels[-1] - levels[0] > 0 else -1
        for i in range(1, len(levels)):
            diff = (levels[i] - levels[i - 1]) * direction
            if not (1 <= diff <= 3):
                return False
        return True

    count = 0
    for line in input:
        levels = [int(level) for level in line.split(" ")]
        direction = 1 if levels[-1] - levels[0] > 0 else -1
        safe = True
        for i in range(1, len(levels)):
            diff = (levels[i] - levels[i - 1]) * direction
            if not (1 <= diff <= 3):
                safe = double_check(levels[: i - 1] + levels[i:]) or double_check(
                    levels[:i] + levels[i + 1 :]
                )
                if not safe:
                    break
        if safe:
            count += 1
    return count


# TEST

import pytest


def test_part1():
    assert part1(input_str) == 680


def test_part2():
    assert part2(input_str) == 710


if __name__ == "__main__":
    pytest.main([__file__])
