#!/usr/bin/env python3

import argparse
import re


def read_input(input_file: str) -> str:
    with open(input_file, "r") as f:
        input_str = "".join([line.strip() for line in f.readlines()])
    return input_str


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
    go = True
    for match_ in matches:
        match match_:
            case "do()":
                go = True
            case "don't()":
                go = False
            case _:
                if go:
                    a, b = (int(factor) for factor in match_.split(","))
                    sum += a * b
    return sum


def main(input_file, part):

    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2024, Day 3:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
