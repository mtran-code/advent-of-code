#!/usr/bin/env python3

import argparse


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        input_str = [line.strip() for line in f.readlines()]
    return input_str


def part1(input: list[str]) -> int:
    # CODE HERE
    return 1


def part2(input: list[str]) -> int:
    # CODE HERE
    return 1


def main(input_file, part):

    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        # UPDATE DAY
        description="""Advent of Code 2024, Day X:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
