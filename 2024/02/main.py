#!/usr/bin/env python3

import argparse


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


def main(input_file, part):

    with open(input_file, "r") as f:
        input_str = [line.strip() for line in f.readlines()]

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2024, Day 2:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
