#!/usr/bin/env python3

import argparse


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        input_str = [line.strip() for line in f.readlines()]
    return input_str


def part1(input: list[str]) -> int:
    pw = 0
    dial = 50
    for line in input:
        if line[0] == "L":
            dial -= int(line[1:])
        elif line[0] == "R":
            dial += int(line[1:])
        else:
            raise NotImplementedError
        dial = dial % 100
        if dial < 0:
            print(f"{dial} is less than 0")
            dial += 100
        if dial == 0:
            pw += 1
    return pw


def part2(input: list[str]) -> int:
    pw = 0
    dial = 50
    for line in input:
        direction = line[0]
        clicks = int(line[1:])

        pw += clicks // 100
        match direction:
            case "L":
                if dial == 0:
                    pw -= 1
                dial -= clicks % 100
                if dial <= 0:
                    pw += 1
                    if dial != 0:
                        dial += 100
            case "R":
                dial += clicks % 100
                if dial > 99:
                    pw += 1
                    dial -= 100
            case _:
                raise NotImplementedError
        # print(f"rotated {line:<3} to {dial:<2}: {pw}")
    return pw


def main(input_file, part):
    input_str = read_input(input_file)

    match part:
        case 1:
            print(part1(input_str))
        case 2:
            print(part2(input_str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Advent of Code 2025, Day 1:
    Take input file containing raw text input, and
    print out solution to either part 1 or part 2."""
    )
    parser.add_argument("input", type=str, help="Input text file path.")
    parser.add_argument("part", type=int, help="Which part to solve, either 1 or 2.")
    args = parser.parse_args()

    if args.part > 2 or args.part < 1:
        parser.error("`part` argument must be 1 or 2.")

    main(args.input, args.part)
