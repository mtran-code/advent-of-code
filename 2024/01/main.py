#!/usr/bin/env python3

import argparse


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        input_str = f.readlines()
    return input_str


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


def main(input_file, part):

    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2024, Day 1:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
