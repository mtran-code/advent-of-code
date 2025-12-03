#!/usr/bin/env python3

import argparse


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        input_str = [line.strip() for line in f.readlines()]
    return input_str


def get_max_with_index(input: list[str]) -> tuple[int, int]:
    print(f"finding max of {input}")
    if len(input) == 1:
        return (0, input[0])

    max = (0, 0)

    for i, j in enumerate(input):
        j = int(j)
        if j > max[1]:
            max = (i, j)

    return max


def part1(input: list[str]) -> int:
    total = 0
    for bank in input:
        left = (-1, -1)
        for i, jolt in enumerate(bank[:-1]):
            if int(jolt) > left[1]:
                left = (i, int(jolt))
        right = -1
        for jolt in bank[left[0] + 1 :]:
            if int(jolt) > right:
                right = int(jolt)
        total += int(str(left[1]) + str(right))
    return total


def part2(input: list[str]) -> int:
    total = 0

    for bank in input:
        print(f"for input: {bank}")
        joltage = []
        last_index = 0

        for digit in range(12, 0, -1):
            if digit * -1 + 1 == 0:
                i, j = get_max_with_index(bank[last_index:])
            else:
                i, j = get_max_with_index(bank[last_index : digit * -1 + 1])
            last_index += i + 1
            joltage.append(j)

        res = int("".join([str(j) for j in joltage]))
        print(f"got {res}")
        assert len(str(res)) == 12
        total += res
    return total


def main(input_file, part):
    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2025, Day 3:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
